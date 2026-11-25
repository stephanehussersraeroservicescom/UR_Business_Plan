"""
Modele financier par flux (decision D-070, 25/11/2026).

Principe :
  - aucun chiffre de bilan n'est ecrit ici : les produits par tonne sont lus dans
    controle-sources/calculs.yaml, via la table engine/flux_bilans.yaml ;
  - les prix, couts et hypotheses viennent de params/*.yaml (chacun avec sa decision) ;
  - les valeurs non tranchees viennent de la section en_attente de flux_bilans.yaml ;
  - chaque valeur utilisee est decrite : source, confiance (echelle D-022), statut.

Usage en ligne de commande :
    python3 -m engine.flux                       # plastiques, standard
    python3 -m engine.flux --flux omr --scenario pessimiste
    python3 -m engine.flux --flux dae --set prix_entree_dae=200 --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ICI = Path(__file__).resolve().parent
WF = ICI.parent
PARAMS = WF / "params"
CALCULS = WF / "controle-sources" / "calculs.yaml"
VERIFS = WF / "controle-sources" / "verifications"
REG_EXT = WF / "reference" / "sources-externes" / "registre-sources.yaml"
EVIDENCE = PARAMS / "_evidence.yaml"
DECISIONS = PARAMS / "_decisions.yaml"
BILANS = ICI / "flux_bilans.yaml"

SCENARIOS = ["pessimiste", "standard", "optimiste"]
SOURCES_CHALEUR = {
    "huile": "Huile produite (defaut, D-069)",
    "char": "Char (si foyer solide ajoute)",
    "gazole": "Gazole achete",
}
STATUT_CODEX = "contre-verifie Codex"
STATUT_CONTROLE = "controle, non contre-verifie"
STATUT_ATTENTE = "en attente de decision"
STATUT_HERITE = "valeur heritee, non sourcee"

# Parametres modifiables sur la page, regroupes (cle params/*.yaml)
CHAMPS = {
    "Prix des produits": ["prix_huile_legere", "prix_huile_gazole", "prix_huile_lourde",
                          "part_huile_legere", "part_huile_gazole", "part_huile_lourde",
                          "facteur_qualite_huile", "prix_char", "prix_ferreux", "prix_alu",
                          "prix_hydrogene", "recuperation_h2"],
    "Energie achetee": ["prix_elec", "elec_par_unite", "prix_fioul"],
    "Couts d'exploitation": ["etp_coeur_base", "cout_etp", "maintenance_bas", "maintenance_haut",
                             "maintenance_an_bas", "maintenance_an_haut", "assurance",
                             "tgap_incineration", "cout_elimination", "cout_concentrat",
                             "rendement_eau_seacoral", "conso_carbonate", "prix_carbonate",
                             "couche_catalytique", "ceramique_seacoral", "charbon_actif", "provision",
                             "pci_gaz_organique"],
    "Investissement": ["nb_unites", "machine", "pre_tri", "batiment_gc_ingenierie_permis",
                       "installation", "fret", "formation", "pieces", "post_tri", "atex",
                       "decanteur", "taux_aleas"],
    "Exploitation et financement": ["charge_reacteur", "jours_exploitation", "charge_an1", "charge_an2",
                                    "inflation", "part_dette", "taux_interet", "duree_pret",
                                    "impot_societes", "duree_amortissement", "horizon"],
}
OPTIONS = ["tgap_payee_usine", "compter_hydrogene", "compter_metaux"]


def _charger(p: Path) -> dict:
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


# ---------------------------------------------------------------------------
# Donnees : parametres, calculs, sources, statut de contre-verification
# ---------------------------------------------------------------------------

class Donnees:
    def __init__(self):
        self.params = {}
        for f in sorted(PARAMS.glob("*.yaml")):
            if f.name.startswith("_"):
                continue
            for k, d in _charger(f).items():
                if isinstance(d, dict) and "valeur" in d:
                    self.params[k] = dict(d, _fichier=f.name)
        self.calculs = _charger(CALCULS)
        self.ext = _charger(REG_EXT) if REG_EXT.exists() else {}
        self.ev = _charger(EVIDENCE)
        self.decisions = _charger(DECISIONS)
        self.bilans = _charger(BILANS)
        self.en_attente = self.bilans.get("en_attente", {})
        textes = []
        for f in sorted(VERIFS.glob("*codex*.md")):
            textes.append(f.read_text(encoding="utf-8", errors="replace"))
        self._codex = "\n".join(textes)
        self._conf = {}

    # -- statut
    def contre_verifie(self, ident: str) -> bool:
        return bool(ident) and re.search(rf"(?<![\w-]){re.escape(ident)}(?![\w-])", self._codex) is not None

    # -- confiance d'une source (echelle D-022)
    def confiance_source(self, ident: str):
        if ident in ("AUCUNE", "V3-MODEL") or not ident:
            return None
        if re.match(r"^D-\d+$", ident):
            return 90                                   # hypothese de travail
        f = self.ext.get(ident) or self.ev.get(ident)
        if not isinstance(f, dict):
            return None
        statut, typ = str(f.get("statut", "")), str(f.get("type", ""))
        fiab = str(f.get("fiabilite", ""))
        if "ARCHIVE-NON-VERIFIE" in str(f.get("chemin", "")) + str(f.get("url", "")):
            return None
        if statut in ("secondaire", "non-verifie"):
            return 80
        if typ in ("statistique_publique", "reglementaire", "donnees_ouvertes", "norme", "reference"):
            return 100
        if ident.startswith("NIST"):
            return 100
        if fiab in ("certifie_tiers", "mesure_interne") or typ in ("rapport_essai", "rapport_laboratoire"):
            return 100
        if fiab == "constructeur":
            return 90 if typ == "declaration" else 95
        return 95

    def confiance_calcul(self, ident: str, pile=()):
        if ident in self._conf:
            return self._conf[ident]
        fiche = self.calculs.get(ident)
        if fiche is None or ident in pile:
            return None
        vals = []
        for e in (fiche.get("entrees") or {}).values():
            if "calc" in e:
                vals.append(self.confiance_calcul(e["calc"], pile + (ident,)))
            else:
                srcs = e.get("source")
                srcs = srcs if isinstance(srcs, list) else [srcs]
                vals.append(min([self.confiance_source(s) or 0 for s in srcs] or [0]))
        vals = [v for v in vals if v is not None]
        c = min(min(vals) if vals else 0, 95)
        c = c if c >= 80 else (80 if c else None)
        self._conf[ident] = c
        return c

    def calcul(self, ident: str) -> float:
        if ident not in self.calculs:
            raise KeyError(f"Calcul absent de calculs.yaml : {ident}")
        return float(self.calculs[ident]["resultat"])

    # -- description d'un parametre
    def decrire_param(self, cle: str) -> dict:
        if cle in self.en_attente:
            a = self.en_attente[cle]
            confs = [self.confiance_source(x) for x in a.get("preuves", [])]
            return {"cle": cle, "label": a["label"], "valeur": a["valeur"], "unite": a.get("unite", ""),
                    "source": f"en attente {a.get('point')}", "preuves": a.get("preuves", []),
                    "confiance": None, "confiance_ref": max([c for c in confs if c] or [0]) or None,
                    "statut": STATUT_ATTENTE, "note": a.get("note", "")}
        p = self.params[cle]
        preuves = [x for x in p.get("preuves", []) if x not in ("AUCUNE", "V3-MODEL")]
        confs = [self.confiance_source(x) for x in preuves]
        confs = [c for c in confs if c]
        dec = p.get("decision")
        if confs:
            conf = min(confs)
            statut = STATUT_CODEX if all(self.contre_verifie(x) for x in preuves) else STATUT_CONTROLE
            source = ", ".join(preuves) + (f" ; decision {dec}" if dec else "")
        elif dec:
            conf, statut = None, STATUT_CONTROLE
            source = f"decision {dec}"
        else:
            conf, statut, source = None, STATUT_HERITE, "aucune source (valeur heritee)"
        return {"cle": cle, "label": p.get("label", cle), "valeur": p["valeur"], "unite": p.get("unite", ""),
                "source": source, "preuves": preuves, "decision": dec, "confiance": conf,
                "statut": statut, "note": p.get("note", ""), "type_decision": self._type_decision(dec)}

    def _type_decision(self, dec):
        d = self.decisions.get(dec) if dec else None
        if not d:
            return None
        motif = str(d.get("motif", ""))
        if "HYPOTHESE posee par Claude" in motif:
            return "hypothese de Claude, a trancher"
        if "HYPOTHESE" in motif:
            return "decision de Stephane (hypothese)"
        return "decision de Stephane"

    def decrire_calcul(self, ident: str) -> dict:
        f = self.calculs[ident]
        hyp = sorted({e["source"] for e in (f.get("entrees") or {}).values()
                      if isinstance(e.get("source"), str) and re.match(r"^D-\d+$", e["source"])})
        return {"id": ident, "valeur": float(f["resultat"]), "unite": f.get("unite", ""),
                "description": f.get("description", ""), "confiance": self.confiance_calcul(ident),
                "statut": STATUT_CODEX if self.contre_verifie(ident) else STATUT_CONTROLE,
                "hypotheses": hyp}


# ---------------------------------------------------------------------------
# Calcul
# ---------------------------------------------------------------------------

def tri(flux):
    """Taux de rendement interne par dichotomie ; None si pas de changement de signe."""
    def van(r):
        return sum(f / (1 + r) ** i for i, f in enumerate(flux))
    lo, hi = -0.99, 1.0
    if van(lo) * van(hi) > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        if van(lo) * van(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def calculer(flux="plastiques", scenario="standard", surcharges=None, choix=None, donnees=None):
    """
    surcharges : {cle_parametre: valeur} (params/ ou en_attente)
    choix : {prix_entree: cle, source_chaleur: huile|char|gazole, compter_gaz_organique: bool}
    """
    D = donnees or Donnees()
    surcharges = dict(surcharges or {})
    choix = dict(choix or {})
    if flux not in D.bilans or flux.startswith("_") or flux == "en_attente":
        raise KeyError(f"Flux inconnu : {flux}")
    F = D.bilans[flux]
    if F.get("inactif"):
        raise ValueError(f"Flux {flux} non disponible : {F.get('annexe')}")
    if scenario not in SCENARIOS:
        raise KeyError(f"Scenario inconnu : {scenario}")

    utilises = {}

    def p(cle):
        if cle not in utilises:
            utilises[cle] = D.decrire_param(cle)
        v = surcharges.get(cle, utilises[cle]["valeur"])
        if cle in surcharges:
            utilises[cle]["surcharge"] = v
        return v

    # ---- bilan par tonne (kg/t), lu dans calculs.yaml
    table = dict(F.get("communs_scenarios") or {})
    table.update(F["scenarios"][scenario])
    q, calculs_lus = {}, {}
    for produit, ref in table.items():
        ident, fac = (ref["calc"], ref.get("facteur", 1)) if isinstance(ref, dict) else (ref, 1)
        q[produit] = D.calcul(ident) * fac
        calculs_lus[produit] = dict(D.decrire_calcul(ident), facteur=fac, kg_t=q[produit])
    g = lambda k: q.get(k, 0.0)
    com = D.bilans["_communs"]
    cst = {k: D.calcul(v) for k, v in com.items()}
    for k, v in com.items():
        calculs_lus["_" + k] = D.decrire_calcul(v)

    n = p("nb_unites")
    charge = p("charge_reacteur")
    jours = p("jours_exploitation")

    # ---- energie par tonne (MJ/t)
    besoin = cst["bruleur_mj_jour"] / charge                      # D-072
    gaz_hc_mj = g("gaz_hc") * cst["pci_gaz_hc"]
    h2_kg = 0.0
    h2 = bool(p("compter_hydrogene")) and F.get("hydrogene_possible", False)
    if h2:
        rec = p("recuperation_h2")
        h2_kg = g("gaz_hc") * cst["h2_part_masse"] / 100 * rec
        gaz_hc_mj *= 1 - cst["h2_part_energie"] / 100 * rec
    gaz_org = bool(choix.get("compter_gaz_organique", False))
    gaz_org_mj = (g("gaz_org") + g("non_alloue_gaz")) * p("pci_gaz_organique") if gaz_org else 0.0
    dispo = gaz_hc_mj + gaz_org_mj
    deficit = max(0.0, besoin - dispo)
    source = choix.get("source_chaleur", "huile")
    if source not in SOURCES_CHALEUR:
        raise KeyError(f"Source de chaleur inconnue : {source}")
    huile_brulee = char_brule = 0.0
    reste = deficit
    if source == "huile" and reste > 0:
        huile_brulee = min(g("huile"), reste / cst["pci_huile"])
        reste -= huile_brulee * cst["pci_huile"]
    elif source == "char" and reste > 0:
        pci_c = p(F["pci_char_param"])
        char_brule = min(g("char"), reste / pci_c)
        reste -= char_brule * pci_c
    gazole_l = reste / cst["pci_gazole"]
    energie = {"besoin_mj_t": besoin, "gaz_hc_mj_t": gaz_hc_mj, "gaz_organique_mj_t": gaz_org_mj,
               "couverture": dispo / besoin if besoin else None, "deficit_mj_t": deficit,
               "huile_brulee_kg_t": huile_brulee, "char_brule_kg_t": char_brule,
               "gazole_l_t": gazole_l, "h2_kg_t": h2_kg, "source_chaleur": source,
               "surplus_mj_t": max(0.0, dispo - besoin)}

    # ---- prix et couts unitaires (annee 1, avant inflation)
    prix_huile = (p("part_huile_legere") * p("prix_huile_legere")
                  + p("part_huile_gazole") * p("prix_huile_gazole")
                  + p("part_huile_lourde") * p("prix_huile_lourde")) * p("facteur_qualite_huile")
    cle_entree = choix.get("prix_entree") or F["prix_entree"]["defaut"]
    if cle_entree not in F["prix_entree"]["choix"]:
        raise KeyError(f"Prix d'entree {cle_entree} non prevu pour le flux {flux}")
    prix_entree = p(cle_entree)
    metaux = bool(p("compter_metaux")) and g("metaux") > 0
    rev_t = {
        "prix_entree": prix_entree,
        "huile": (g("huile") - huile_brulee) / 1000 * prix_huile,
        "char": (g("char") - char_brule) / 1000 * p("prix_char"),
        "hydrogene": h2_kg * p("prix_hydrogene") if h2 else 0.0,
        "metaux": (g("metaux") / 1000 * (p("part_ferreux") * p("rec_ferreux") * p("prix_ferreux")
                                         + p("part_alu") * p("rec_alu") * p("prix_alu"))) if metaux else 0.0,
    }
    liquides = g("eau") + g("liquide") + g("non_alloue_liq")
    ch_t = {
        "gazole": gazole_l * p("prix_fioul"),
        "tgap": p("tgap_incineration") if p("tgap_payee_usine") else 0.0,
        "elimination_inertes": g("inertes") / 1000 * p("cout_elimination"),
        "liquides_a_traiter": liquides / 1000 * (1 - p("rendement_eau_seacoral")) * p("cout_concentrat"),
        "carbonate": p("conso_carbonate") / 1000 * p("prix_carbonate"),
    }

    # ---- investissement
    postes = ["machine", "installation", "fret", "formation", "pieces", "pre_tri", "post_tri",
              "atex", "decanteur", "batiment_gc_ingenierie_permis"]
    capex_postes = {k: p(k) * n for k in postes}
    capex_hors_aleas = sum(capex_postes.values())
    aleas = capex_hors_aleas * p("taux_aleas")
    capex = capex_hors_aleas + aleas
    capex_equip = capex_postes["machine"] + capex_postes["pre_tri"]
    amort = capex / p("duree_amortissement")

    def taux_maint(an):
        a1, a2 = p("maintenance_an_bas"), p("maintenance_an_haut")
        lo, hi = p("maintenance_bas"), p("maintenance_haut")
        if an <= a1:
            return lo
        if an >= a2:
            return hi
        return lo + (hi - lo) * (an - a1) / (a2 - a1)

    # ---- annees
    H = int(p("horizon"))
    infl = p("inflation")
    is_ = p("impot_societes")
    t_nom = charge * jours * n

    def structure(part_dette):
        dette = capex * part_dette
        duree, taux = int(p("duree_pret")), p("taux_interet")
        lignes, cum_p, cum_a = [], -capex, -(capex - dette)
        flux_p, flux_a = [-capex], [-(capex - dette)]
        payback = None
        for an in range(1, H + 1):
            u = p("charge_an1") if an == 1 else (p("charge_an2") if an == 2 else 1.0)
            k = (1 + infl) ** (an - 1)
            t = t_nom * u
            rec = {f"rec_{x}": v * t * k for x, v in rev_t.items()}
            ch = {f"ch_{x}": v * t * k for x, v in ch_t.items()}
            ch["ch_electricite"] = p("elec_par_unite") * n * jours * u * p("prix_elec") * k
            ch["ch_personnel"] = ((p("etp_coeur_base") + p("etp_coeur_step") * (n - 1) + p("etp_tri") * n)
                                  * p("cout_etp") * k)
            ch["ch_maintenance"] = taux_maint(an) * capex_equip * k
            ch["ch_assurance"] = p("assurance") * capex * k
            ch["ch_consommables"] = (p("couche_catalytique") + p("ceramique_seacoral") + p("charbon_actif")) * n * k
            ch["ch_provision_divers"] = p("provision") * capex * k
            ca = sum(rec.values())
            charges = sum(ch.values())
            ebitda = ca - charges
            dep = amort if an <= p("duree_amortissement") else 0.0
            solde = dette * max(0.0, 1 - (an - 1) / duree) if an <= duree else 0.0
            interets = solde * taux
            principal = dette / duree if an <= duree else 0.0
            impot_p = max(0.0, ebitda - dep) * is_
            impot_a = max(0.0, ebitda - dep - interets) * is_
            cf_p = ebitda - impot_p
            cf_a = ebitda - interets - principal - impot_a
            cum_p += cf_p
            cum_a += cf_a
            if payback is None and cum_p >= 0:
                payback = an - cum_p / cf_p if cf_p else an
            flux_p.append(cf_p)
            flux_a.append(cf_a)
            lignes.append(dict(annee=an, taux_charge=u, tonnage=t, **rec, chiffre_affaires=ca, **ch,
                               charges=charges, ebitda=ebitda, marge_ebitda=ebitda / ca if ca else None,
                               amortissement=dep, interets=interets, impot=impot_a,
                               resultat_net=ebitda - dep - interets - impot_a,
                               remboursement_dette=principal, cash_flow_projet=cf_p,
                               cash_flow_actionnaire=cf_a, cumul_projet=cum_p, cumul_actionnaire=cum_a))
        return {"part_dette": part_dette, "dette": dette, "fonds_propres": capex - dette,
                "annees": lignes, "tri_projet": tri(flux_p), "tri_fonds_propres": tri(flux_a),
                "retour_annees": payback,
                "roi_horizon": (sum(flux_p[1:]) - capex) / capex if capex else None,
                "cumul_actionnaire_fin": cum_a}

    s_defaut = structure(p("part_dette"))
    s_fp = structure(0.0)
    a3 = s_defaut["annees"][min(2, H - 1)]

    # ---- signalements
    alertes = []
    if any(u["statut"] == STATUT_HERITE for u in utilises.values()):
        alertes.append("Des valeurs heritees sans source sont utilisees (voir la liste des parametres).")
    if any(u["statut"] == STATUT_ATTENTE for u in utilises.values()):
        alertes.append("Des valeurs en attente de decision sont utilisees (B18).")
    if flux == "dae":
        alertes.append("DAE : humidite et PCI inconnus (R-048) ; eau non comptee ; fines (340 kg/t) sans produit ni cout.")
    if flux in ("omr", "dae"):
        alertes.append("Huile d'OMR et de DAE hors du champ de l'arrete de sortie du statut de dechet ; huile de dechets "
                       "municipaux classee dangereuse HP 3 (annexe 3).")
    if flux == "plastiques" and scenario == "optimiste":
        alertes.append("Plastiques optimiste : char limite au complement a une tonne (D-071, hypothese de Claude).")
    alertes.append("Besoin du bruleur rapporte a 140 t/jour (D-072, hypothese de Claude, a trancher avec B6).")
    alertes.append("Essais en lots ; performance continue de l'URC-2000 a garantir par contrat (annexe 1). "
                   "Modele non presentable a un investisseur avant validation des briques (D-070).")

    return {
        "flux": flux, "label": F["label"], "annexe": F["annexe"], "scenario": scenario,
        "bilan_energie_flux": F.get("bilan_energie"),
        "choix": {"prix_entree": cle_entree, "source_chaleur": source, "compter_gaz_organique": gaz_org},
        "bilan_kg_t": q, "calculs": calculs_lus, "energie": energie,
        "prix_huile_eur_t": prix_huile, "recettes_eur_t": rev_t, "charges_variables_eur_t": ch_t,
        "tonnage_nominal": t_nom,
        "capex": {"postes": capex_postes, "aleas": aleas, "total": capex, "equipement": capex_equip,
                  "amortissement_annuel": amort},
        "structure_defaut": s_defaut, "structure_fonds_propres": s_fp,
        "synthese_an3": {k: a3[k] for k in ("chiffre_affaires", "charges", "ebitda", "marge_ebitda",
                                            "cash_flow_projet")},
        "parametres": utilises, "alertes": alertes,
    }


def description_page(donnees=None):
    """Tout ce dont la page a besoin pour construire les champs."""
    D = donnees or Donnees()
    flux = {k: {"label": v["label"], "annexe": v["annexe"], "inactif": bool(v.get("inactif")),
                "prix_entree": v.get("prix_entree"), "hydrogene_possible": v.get("hydrogene_possible", False),
                "bilan_energie": v.get("bilan_energie")}
            for k, v in sorted(D.bilans.items(), key=lambda kv: (kv[1].get("ordre", 99) if isinstance(kv[1], dict) else 99))
            if not k.startswith("_") and k != "en_attente"}
    cles = {c for g in CHAMPS.values() for c in g} | set(OPTIONS)
    for v in flux.values():
        cles |= set((v.get("prix_entree") or {}).get("choix", []))
    champs = {c: D.decrire_param(c) for c in sorted(cles)}
    return {"flux": flux, "scenarios": SCENARIOS, "sources_chaleur": SOURCES_CHALEUR,
            "groupes": CHAMPS, "options": OPTIONS, "champs": champs}


def _convertir(v: str):
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v


def main(argv=None):
    ap = argparse.ArgumentParser(description="Modele financier par flux (D-070)")
    ap.add_argument("--flux", default="plastiques")
    ap.add_argument("--scenario", default="standard", choices=SCENARIOS)
    ap.add_argument("--chaleur", default="huile", choices=list(SOURCES_CHALEUR))
    ap.add_argument("--gaz-organique", action="store_true")
    ap.add_argument("--prix-entree", default=None, help="cle du prix d'entree (ex. prix_entree_pse_blanc)")
    ap.add_argument("--set", action="append", default=[], metavar="CLE=VALEUR")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    sur = {k: _convertir(v) for k, v in (s.split("=", 1) for s in a.set)}
    r = calculer(a.flux, a.scenario, sur, {"source_chaleur": a.chaleur, "compter_gaz_organique": a.gaz_organique,
                                           "prix_entree": a.prix_entree})
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1, default=str))
        return 0
    m = lambda x: f"{x / 1e6:,.2f} MEUR".replace(",", " ")
    pct = lambda x: "n.d." if x is None else f"{x * 100:.1f} %"
    print(f"{r['label']} ; scenario {r['scenario']} ; prix d'entree {r['choix']['prix_entree']} ; chaleur {r['choix']['source_chaleur']}")
    print("Bilan kg/t :", ", ".join(f"{k} {v:.1f}" for k, v in r["bilan_kg_t"].items()))
    e = r["energie"]
    print(f"Energie : besoin {e['besoin_mj_t']:.0f} MJ/t, gaz {e['gaz_hc_mj_t']:.0f} MJ/t, couverture {e['couverture']:.2f} ; "
          f"huile brulee {e['huile_brulee_kg_t']:.1f} kg/t, gazole {e['gazole_l_t']:.1f} L/t")
    print(f"CAPEX {m(r['capex']['total'])} ; tonnage nominal {r['tonnage_nominal']:,.0f} t/an".replace(",", " "))
    for nom, s in (("dette " + pct(r["structure_defaut"]["part_dette"]), r["structure_defaut"]),
                   ("100 % fonds propres", r["structure_fonds_propres"])):
        print(f"[{nom}] TRI projet {pct(s['tri_projet'])} ; TRI fonds propres {pct(s['tri_fonds_propres'])} ; "
              f"retour {s['retour_annees'] and round(s['retour_annees'], 1)} ans ; ROI horizon {pct(s['roi_horizon'])}")
    print("an | CA | charges | EBITDA | cash-flow projet | cumul")
    for l in r["structure_defaut"]["annees"]:
        print(f"{l['annee']:>2} | {m(l['chiffre_affaires'])} | {m(l['charges'])} | {m(l['ebitda'])} | "
              f"{m(l['cash_flow_projet'])} | {m(l['cumul_projet'])}")
    for x in r["alertes"]:
        print("!", x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
