"""
Moteur de calcul Urban Rig.

Principe : aucune valeur numerique n'est ecrite ici. Tout vient de params/*.yaml.
Chaque resultat enregistre les parametres qu'il a consommes, ce qui permet de
remonter automatiquement la chaine parametre -> decision -> preuve.
"""
from pathlib import Path
import yaml

RACINE = Path(__file__).resolve().parent.parent
PARAMS = RACINE / "params"


CONFIANCE_BASE = {
    "experience_interne": 1.0,
    "experience_industrielle": 1.0,
    "loi_physique": 1.0,
    "mesure_certifiee": 1.0,
    "decision_commerciale": 1.0,
    "reglementaire": 1.0,
    "publication_scientifique": 0.8,
    "specification_constructeur": 0.9,
    "declaration": 0.6,
    "hypothese": 0.5,
    "calcul": 1.0,
    "inconnu": 0.0,
}
A_DISCUTER = {"publication_scientifique", "specification_constructeur", "declaration"}

# Confiance attribuee a un parametre non encore instruit, selon sa meilleure preuve
CONFIANCE_PREUVE = {
    "certifie_tiers": 1.0, "mesure_interne": 1.0, "constructeur": 0.8,
    "litterature": 0.8, "aucune": 0.3,
}


class Registre:
    """Charge les parametres et trace chaque lecture."""

    def __init__(self, surcharges=None):
        self.params, self.domaines = {}, {}
        self.preuves = yaml.safe_load((PARAMS / "_evidence.yaml").read_text(encoding="utf-8"))
        self.decisions = yaml.safe_load((PARAMS / "_decisions.yaml").read_text(encoding="utf-8"))
        fj = PARAMS / "_justifications.yaml"
        self.justifs = yaml.safe_load(fj.read_text(encoding="utf-8")) if fj.exists() else {}
        self._conf_cache = {}
        for f in sorted(PARAMS.glob("*.yaml")):
            if f.name.startswith("_"):
                continue
            bloc = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
            domaine = bloc.pop("_domaine", f.stem)
            for cle, d in bloc.items():
                if cle in self.params:
                    raise ValueError(f"Parametre duplique : {cle} ({f.name})")
                d["_fichier"], d["_domaine"], d["_cle"] = f.name, domaine, cle
                self.params[cle] = d
                self.domaines.setdefault(domaine, []).append(cle)
        for cle, val in (surcharges or {}).items():
            if cle not in self.params:
                raise KeyError(f"Surcharge inconnue : {cle}")
            self.params[cle]["_origine"] = self.params[cle]["valeur"]
            self.params[cle]["valeur"] = val
            self.params[cle]["_surcharge"] = True
        self.lectures = {}

    def __call__(self, cle, consommateur=None):
        if cle not in self.params:
            raise KeyError(f"Parametre inconnu : {cle}")
        if consommateur:
            self.lectures.setdefault(consommateur, set()).add(cle)
        return self.params[cle]["valeur"]

    # ------------------------------------------------ confiance
    def confiance_affirmation(self, aid, pile=()):
        """Confiance effective d'une affirmation, propagee depuis ses appuis."""
        if aid in self._conf_cache:
            return self._conf_cache[aid]
        if aid in pile:
            raise ValueError(f"Boucle dans les justifications : {' -> '.join(pile + (aid,))}")
        a = self.justifs[aid]
        propre = a.get("confiance", CONFIANCE_BASE.get(a.get("base", "hypothese"), 0.5))
        appuis = a.get("appuis", [])
        if appuis:
            vals = [self.confiance_affirmation(x, pile + (aid,)) for x in appuis]
            agr = max(vals) if a.get("mode") == "un_suffit" else min(vals)
            eff = min(propre, agr)
        else:
            eff = propre
        self._conf_cache[aid] = eff
        return eff

    def confiance_parametre(self, cle):
        """Retourne (confiance, instruit). instruit = une justification existe."""
        p = self.params[cle]
        if p.get("justification"):
            return self.confiance_affirmation(p["justification"]), True
        rangs = [CONFIANCE_PREUVE[self.preuves[x]["fiabilite"]]
                 for x in p.get("preuves", []) if x in self.preuves]
        return (max(rangs) if rangs else 0.3), False

    def controle(self):
        """Verifie que chaque preuve et chaque decision citee existe."""
        pbs = []
        for aid, a in self.justifs.items():
            for x in a.get("appuis", []) + a.get("contre_indications", []):
                if x not in self.justifs:
                    pbs.append(f"{aid}: appui inconnu '{x}'")
            for x in a.get("preuves", []):
                if x not in self.preuves:
                    pbs.append(f"{aid}: preuve inconnue '{x}'")
            if a.get("base") not in CONFIANCE_BASE:
                pbs.append(f"{aid}: base inconnue '{a.get('base')}'")
            try:
                self.confiance_affirmation(aid)
            except ValueError as e:
                pbs.append(str(e))
        for cle, d in self.params.items():
            for p in d.get("preuves", []):
                if p not in self.preuves:
                    pbs.append(f"{cle}: preuve inconnue '{p}'")
            j = d.get("justification")
            if j and j not in self.justifs:
                pbs.append(f"{cle}: justification inconnue '{j}'")
            dec = d.get("decision")
            if dec and dec not in self.decisions:
                pbs.append(f"{cle}: decision inconnue '{dec}'")
            if not d.get("preuves"):
                pbs.append(f"{cle}: aucune preuve citee")
            v, b = d.get("valeur"), d.get("bornes")
            if b and isinstance(v, (int, float)) and not (b["bas"] <= v <= b["haut"]):
                pbs.append(f"{cle}: valeur {v} hors bornes [{b['bas']} ; {b['haut']}]")
        return pbs


class Modele:
    def __init__(self, reg):
        self.p, self.r = reg, {}

    def _set(self, cle, valeur, unite, depend):
        for d in depend:
            self.p(d, cle)
        self.r[cle] = {"valeur": valeur, "unite": unite, "depend": depend}
        return valeur

    # ---------------------------------------------------------------- matiere
    def bilan_matiere(self):
        p = self.p
        n = p("nb_unites")
        j = p("jours_exploitation")
        debit = p("capacite_volumetrique") * p("densite_dechet")
        self._set("debit_massique", debit, "T/j",
                  ["capacite_volumetrique", "densite_dechet"])
        tonnage = debit * j * n
        self._set("tonnage_annuel", tonnage, "T/an",
                  ["capacite_volumetrique", "densite_dechet", "jours_exploitation", "nb_unites"])

        net = debit * 1000 * (1 - p("taux_refus"))          # kg/j par unite
        plast, org = net * p("part_plastique"), net * p("part_organique")
        met, verre = net * p("part_metaux"), net * p("part_verre")
        inert = net * p("part_inertes")

        huile_reac = plast * p("rdt_huile_plastique") * j / 1000 * n
        gaz_p = plast * p("rdt_gaz_plastique")
        res_p = plast * p("rdt_residu_plastique")
        char_o = org * p("rdt_char_organique")
        gaz_o = org - char_o

        eau = net * p("part_humidite") * j / 1000 * n
        org_dec = eau * p("part_organique_eau")
        org_rec = org_dec * p("part_organique_recyclee")
        huile_rec = org_rec * p("rdt_huile_recyclage")

        self._set("huile", huile_reac + huile_rec, "T/an",
                  ["part_plastique", "rdt_huile_plastique", "jours_exploitation",
                   "nb_unites", "part_organique_recyclee", "rdt_huile_recyclage"])
        self._set("char", (char_o + res_p) * p("criblage_char") * j / 1000 * n, "T/an",
                  ["part_organique", "rdt_char_organique", "rdt_residu_plastique", "criblage_char"])
        self._set("ferreux", met * p("part_ferreux") * p("rec_ferreux") * j / 1000 * n, "T/an",
                  ["part_metaux", "part_ferreux", "rec_ferreux"])
        self._set("aluminium", met * p("part_alu") * p("rec_alu") * j / 1000 * n, "T/an",
                  ["part_metaux", "part_alu", "rec_alu"])
        self._set("autres_metaux",
                  met * (1 - p("part_ferreux") - p("part_alu")) * p("rec_metaux_char") * j / 1000 * n,
                  "T/an", ["part_metaux", "rec_metaux_char"])
        self._set("verre", verre * p("rec_verre") * j / 1000 * n, "T/an",
                  ["part_verre", "rec_verre"])
        self._set("eau_procede", eau, "T/an", ["part_humidite"])
        self._set("phase_organique_decantee", org_dec, "T/an", ["part_organique_eau"])
        self._set("eau_douce", (eau - org_dec) * p("rendement_eau_seacoral"), "T/an",
                  ["rendement_eau_seacoral"])
        self._set("concentrat", (eau - org_dec) * (1 - p("rendement_eau_seacoral")), "T/an",
                  ["rendement_eau_seacoral"])
        self._set("residus",
                  (org_dec - org_rec)
                  + (net * p("taux_refus") / (1 - p("taux_refus"))
                     + (char_o + res_p) * (1 - p("criblage_char"))
                     + verre * (1 - p("rec_verre")) + inert) * j / 1000 * n,
                  "T/an", ["taux_refus", "criblage_char", "rec_verre", "part_inertes"])
        self._gaz_p, self._gaz_o, self._res_p = gaz_p, gaz_o, res_p
        self._plast, self._org, self._char_o = plast, org, char_o

    # ---------------------------------------------------------------- energie
    def bilan_energie(self):
        p, j, n = self.p, self.p("jours_exploitation"), self.p("nb_unites")
        dispo = self._gaz_p * p("pci_gaz_plastique") + self._gaz_o * p("pci_gaz_organique")
        utile = dispo * p("rendement_bruleur")
        besoin = p("capacite_volumetrique") * p("densite_dechet") * p("besoin_thermique")
        self._set("energie_gaz_disponible", dispo, "MJ/j",
                  ["pci_gaz_plastique", "pci_gaz_organique", "rdt_gaz_plastique", "rdt_char_organique"])
        self._set("couverture_thermique", utile / besoin, "fraction",
                  ["pci_gaz_plastique", "pci_gaz_organique", "rendement_bruleur", "besoin_thermique"])
        deficit = max(0.0, besoin - utile)
        fioul = (deficit + p("provision_fioul_secours") * besoin) / p("pci_fioul") / p("rendement_bruleur")
        self._set("fioul_litres_jour", fioul, "L/j",
                  ["provision_fioul_secours", "pci_fioul", "besoin_thermique"])
        self._set("fioul_annuel", fioul * j * n, "L/an", ["jours_exploitation", "nb_unites"])
        self._set("energie_exportee",
                  self.r["huile"]["valeur"] * p("pci_huile_gj")
                  + self.r["char"]["valeur"] * p("pci_char"),
                  "GJ/an", ["pci_huile_gj", "pci_char"])

    # ---------------------------------------------------------------- carbone
    def bilan_carbone(self):
        p, j, n = self.p, self.p("jours_exploitation"), self.p("nb_unites")
        entrant = self._plast * p("teneur_c_plastique") * 3.667 * j / 1000 * n
        site = (self._gaz_p * p("teneur_c_gaz") * 3.667 * j / 1000 * n
                + self.r["fioul_annuel"]["valeur"] * p("co2_fioul") / 1000)
        aval = (self.r["huile"]["valeur"] * p("co2_huile")
                + self._res_p * p("criblage_char") * p("teneur_c_residu") * 3.667 * j / 1000 * n)
        stocke = self._res_p * (1 - p("criblage_char")) * p("teneur_c_residu") * 3.667 * j / 1000 * n
        self._set("carbone_fossile_entrant", entrant, "T CO2/an", ["teneur_c_plastique", "part_plastique"])
        self._set("emissions_directes_site", site, "T CO2/an", ["teneur_c_gaz", "co2_fioul"])
        self._set("intensite_carbone_site", site / self.r["tonnage_annuel"]["valeur"], "T CO2/T", [])
        self._set("carbone_sortant_produits", aval, "T CO2/an", ["co2_huile", "teneur_c_residu"])
        self._set("carbone_stocke", stocke, "T CO2/an", ["criblage_char"])
        self._set("ecart_bouclage_carbone", (site + aval + stocke) / entrant - 1, "fraction", [])

    # ------------------------------------------------------------------ capex
    def capex(self):
        p, n = self.p, self.p("nb_unites")
        eq = sum(p(k) for k in ["machine", "installation", "fret", "formation", "pieces",
                                "pre_tri", "post_tri", "atex", "decanteur"]) * n
        s_us = max(2600, p("surface_usine_1") + p("surface_usine_d") * (n - 1)) * n
        s_sd = (p("surface_stock_dechets_1") + p("surface_stock_dechets_d") * (n - 1)) * n
        s_sp = max(600, p("surface_stock_produits_1") + p("surface_stock_produits_d") * (n - 1)) * n
        s_bu = max(64, p("surface_bureaux_1") + p("surface_bureaux_d") * (n - 1)) * n
        bat = (s_us * p("prix_usine") + (s_sd + s_sp) * p("prix_stockage") + s_bu * p("prix_bureaux")
               + p("vrd_base") + p("vrd_par_unite") * (n - 1))
        ing = p("ingenierie_base") * (1 + p("ingenierie_step") * (n - 1))
        aleas = p("taux_aleas") * (eq + bat)
        self._set("surface_batie", s_us + s_sd + s_sp + s_bu, "m2",
                  ["surface_usine_1", "surface_stock_dechets_1", "surface_stock_produits_1", "surface_bureaux_1"])
        self._set("capex_equipement", eq, "EUR", ["machine", "pre_tri", "post_tri", "atex", "decanteur"])
        self._set("capex_genie_civil", bat, "EUR", ["prix_usine", "prix_stockage", "prix_bureaux", "vrd_base"])
        total = eq + bat + ing + aleas
        self._set("capex_total", total, "EUR", ["taux_aleas", "ingenierie_base"])
        self._set("capex_par_tonne_an", total / self.r["tonnage_annuel"]["valeur"], "EUR/T-an", [])
        self._set("amortissement_annuel", total / p("duree_amortissement"), "EUR/an", ["duree_amortissement"])
        self._set("dette", total * p("part_dette"), "EUR", ["part_dette"])
        self._set("fonds_propres", total * (1 - p("part_dette")), "EUR", ["part_dette"])

    # -------------------------------------------------------------------- p&l
    def taux_maintenance(self, an):
        p = self.p
        a1, a2 = p("maintenance_an_bas"), p("maintenance_an_haut")
        lo, hi = p("maintenance_bas"), p("maintenance_haut")
        if an <= a1:
            return lo
        if an >= a2:
            return hi
        return lo + (hi - lo) * (an - a1) / (a2 - a1)

    def compte_resultat(self):
        p, n = self.p, self.p("nb_unites")
        prix_huile = (p("prix_huile_craqueur") if p("qualite_huile") == "craqueur"
                      else p("prix_huile_combustible"))
        lignes = []
        capex, amort = self.r["capex_total"]["valeur"], self.r["amortissement_annuel"]["valeur"]
        dette, cum = self.r["dette"]["valeur"], 0.0
        for an in range(1, int(p("horizon")) + 1):
            u = p("charge_an1") if an == 1 else (p("charge_an2") if an == 2 else 1.0)
            inf = (1 + p("inflation")) ** (an - 1)
            rec = {
                "gate_fees": self.r["tonnage_annuel"]["valeur"] * u * p("gate_fee") * inf,
                "huile": self.r["huile"]["valeur"] * u * prix_huile * inf,
                "char": self.r["char"]["valeur"] * u * p("prix_char") * inf,
                "metaux": (self.r["ferreux"]["valeur"] * p("prix_ferreux")
                           + self.r["aluminium"]["valeur"] * p("prix_alu")
                           + self.r["autres_metaux"]["valeur"] * p("prix_autres_metaux")) * u * inf,
                "verre": self.r["verre"]["valeur"] * u * p("prix_verre") * inf,
                "carbone": (self.r["tonnage_annuel"]["valeur"] * u
                            * p("reduction_carbone_certifiee") * p("prix_carbone") * inf),
            }
            ch = {
                "personnel": ((p("etp_coeur_base") + p("etp_coeur_step") * (n - 1) + p("etp_tri") * n)
                              * p("cout_etp") * u * inf),
                "maintenance": self.taux_maintenance(an) * self.r["capex_equipement"]["valeur"] * u * inf,
                "electricite": (p("elec_par_unite") * n * p("jours_exploitation")
                                * p("prix_elec") * u * inf),
                "fioul_secours": self.r["fioul_annuel"]["valeur"] * p("prix_fioul") * u * inf,
                "elimination_residus": self.r["residus"]["valeur"] * p("cout_elimination") * u * inf,
                "carbonate": (self.r["tonnage_annuel"]["valeur"] * p("conso_carbonate") / 1000
                              * p("prix_carbonate") * u * inf),
                "concentrat": self.r["concentrat"]["valeur"] * p("cout_concentrat") * u * inf,
                "couche_catalytique": p("couche_catalytique") * n * u * inf,
                "ceramique_seacoral": p("ceramique_seacoral") * n * inf,
                "charbon_actif": p("charbon_actif") * n * u * inf,
                "assurance": p("assurance") * capex * inf,
                "provision_divers": p("provision") * capex * u * inf,
            }
            ebitda = sum(rec.values()) - sum(ch.values())
            dep = amort if an <= p("duree_amortissement") else 0.0
            solde = max(0.0, dette * (1 - (an - 1) / p("duree_pret"))) if an <= p("duree_pret") else 0.0
            interets = solde * p("taux_interet")
            ebt = ebitda - dep - interets
            impot = max(0.0, ebt) * p("impot_societes")
            principal = dette / p("duree_pret") if an <= p("duree_pret") else 0.0
            fcf = ebitda - impot - principal
            cum += fcf
            lignes.append(dict(annee=an, charge=u, tonnage=self.r["tonnage_annuel"]["valeur"] * u,
                               **{f"rec_{k}": v for k, v in rec.items()},
                               recettes=sum(rec.values()),
                               **{f"ch_{k}": v for k, v in ch.items()},
                               charges=sum(ch.values()), ebitda=ebitda,
                               marge=ebitda / sum(rec.values()), amortissement=-dep,
                               interets=-interets, resultat_avant_impot=ebt, impot=-impot,
                               resultat_net=ebt - impot, flux_libre=fcf, flux_cumule=cum))
        self.pl = lignes
        an3 = lignes[2]
        self._set("ebitda_an3", an3["ebitda"], "EUR/an", ["gate_fee", "prix_huile_craqueur", "prix_char"])
        self._set("marge_ebitda_an3", an3["marge"], "fraction", [])
        cout_complet = an3["charges"] + amort
        produits = an3["recettes"] - an3["rec_gate_fees"]
        self._set("gate_fee_equilibre", (cout_complet - produits) / an3["tonnage"], "EUR/T", [])
        return lignes

    def gate_fee_requis(self, annees_exploitation):
        """Gate fee necessaire pour rembourser 100% du CAPEX (sans dette, sans interets)."""
        p = self.p
        capex, amort = self.r["capex_total"]["valeur"], self.r["amortissement_annuel"]["valeur"]
        besoin = (capex - annees_exploitation * p("impot_societes") * amort) / (1 - p("impot_societes"))
        somme_ebitda = sum(self.pl[i]["ebitda"] for i in range(annees_exploitation))
        sensibilite = sum(self.pl[i]["tonnage"] * (1 + p("inflation")) ** i
                          for i in range(annees_exploitation))
        return p("gate_fee") + (besoin - somme_ebitda) / sensibilite

    def tout(self):
        self.bilan_matiere()
        self.bilan_energie()
        self.capex()
        self.compte_resultat()
        self.bilan_carbone()
        return self


def executer(surcharges=None):
    reg = Registre(surcharges)
    return reg, Modele(reg).tout()
