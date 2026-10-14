#!/usr/bin/env python3
"""Bilan matiere pour 1 tonne de plastique (France / UE).

Chaque parametre renvoie a un identifiant de ../registre-sources.yaml.
Toutes les sorties sont des valeurs [calcul]. Lancer : python3 bilan_matiere.py
"""

# --- Parametres sources -----------------------------------------------------
# Scenario A : base "mis sur le marche" (emballages menagers plastiques, France)
MIS_SUR_MARCHE_2025_KT = 1174      # CITEO-RA-2025, p.13
RECYCLE_2025_KT = 346              # CITEO-RA-2025, p.29

# Perte de plastique au centre de tri (part du gisement plastique entrant
# envoyee aux refus). Estimation Citeo, pas une mesure.
PERTE_CDT = (0.15, 0.20)           # CITEO-ECT-2020, p.25

# Rendement des regenerateurs (sortie / entree en balles)
REND_PET = 0.73                    # PRE-PET-2020, p.19 (UE28, donnees 2018)
REND_PEHD = 0.71                   # PRE-HDPEPP-2025, section 5b (UE27+3, 2023)
REND_PP = 0.69                     # PRE-HDPEPP-2025, section 5b
REND_FILMS_MENAGERS = 0.50         # PRE-FILMS-2018, p.17 (ordre de grandeur, 2018)
REND_FILMS_MOYEN = 0.75            # PRE-FILMS-2023, p.24-25 (">75 %", 2020)

# Purete moyenne des balles en sortie de centre de tri (France 2023)
PURETE = {"PET clair": 0.96, "PET fonce": 0.969, "PE/PP/PS": 0.881,
          "Films PE": 0.82, "Films PE/PP": 0.901, "Flux developpement": 0.92}
# CITEO-OBSQUAL-2023, p.29 a 34

# Scenario C : 1 tonne de collecte selective (tous materiaux, bac jaune)
TAUX_REFUS_CS_2022 = 0.230         # CITEO-CAHIER-CS-2024, p.19
COMPO_REFUS = {"fibreux": 0.157, "plastiques rigides": 0.075,
               "plastiques souples": 0.045, "acier": 0.004, "alu": 0.012,
               "autres (fines, imbrules, verre, non-emballages)": 0.709}
# OCAPEM-2025, tableau 3 (methode fragile : voir note)


def fmt(x):
    return f"{x:,.0f}".replace(",", " ")


def scenario_a():
    print("## Scenario A : 1 t d'emballages plastiques menagers mis sur le marche (France 2025)\n")
    taux = RECYCLE_2025_KT / MIS_SUR_MARCHE_2025_KT
    recycle = 1000 * taux
    print(f"- Taux de recyclage [calcul] = {RECYCLE_2025_KT} / {MIS_SUR_MARCHE_2025_KT} = {taux:.1%}"
          f"  -> {fmt(recycle)} kg recycles, {fmt(1000 - recycle)} kg non recycles")
    # Remontee : combien a du entrer dans le bac jaune pour produire ce recycle ?
    lo = recycle / ((1 - PERTE_CDT[0]) * REND_PET)
    hi = recycle / ((1 - PERTE_CDT[1]) * REND_PP)
    print(f"- Estimation [calcul] du plastique collecte en bac jaune pour obtenir ce tonnage :"
          f" {fmt(lo)} a {fmt(hi)} kg (hypothese : rendements des rigides)")
    print(f"- Donc environ {fmt(1000 - hi)} a {fmt(1000 - lo)} kg ne sont jamais tries"
          " (OMR, puis UVE ou stockage). Estimation, pas une mesure.\n")


def scenario_b():
    print("## Scenario B : 1 t de plastique arrivant au centre de tri (bac jaune)\n")
    print("| Etape | Rigides PET | Rigides PEHD | Rigides PP | Films menagers |")
    print("|---|---|---|---|---|")
    rows = {"Refus au centre de tri (kg)": [], "Balles produites (kg)": [],
            "Pertes chez le regenerateur (kg)": [], "Matiere recyclee (kg)": [],
            "Rendement global de la chaine": []}
    for rend in (REND_PET, REND_PEHD, REND_PP, REND_FILMS_MENAGERS):
        refus = [1000 * p for p in PERTE_CDT]
        balles = [1000 - r for r in refus]
        recy = [b * rend for b in balles]
        pertes = [b - r for b, r in zip(balles, recy)]
        rows["Refus au centre de tri (kg)"].append(f"{fmt(refus[0])} a {fmt(refus[1])}")
        rows["Balles produites (kg)"].append(f"{fmt(balles[1])} a {fmt(balles[0])}")
        rows["Pertes chez le regenerateur (kg)"].append(f"{fmt(pertes[1])} a {fmt(pertes[0])}")
        rows["Matiere recyclee (kg)"].append(f"{fmt(recy[1])} a {fmt(recy[0])}")
        rows["Rendement global de la chaine"].append(f"{recy[1]/1000:.0%} a {recy[0]/1000:.0%}")
    for k, v in rows.items():
        print(f"| {k} | " + " | ".join(v) + " |")
    print()
    print("Impuretes contenues dans les balles (France 2023, moyenne) :")
    for k, v in PURETE.items():
        print(f"- {k} : {1 - v:.1%} d'impuretes, soit {fmt(1000 * (1 - v))} kg par tonne de balles")
    print()


def scenario_c():
    print("## Scenario C : 1 t de collecte selective (tous materiaux) arrivant au centre de tri\n")
    refus = 1000 * TAUX_REFUS_CS_2022
    print(f"- Refus [calcul] : {fmt(refus)} kg (taux moyen 2022 : {TAUX_REFUS_CS_2022:.1%})")
    for k, v in COMPO_REFUS.items():
        print(f"  - {k} : {fmt(refus * v)} kg")
    plast = refus * (COMPO_REFUS["plastiques rigides"] + COMPO_REFUS["plastiques souples"])
    print(f"- Plastiques d'emballage identifies dans les refus : {fmt(plast)} kg par tonne de collecte selective\n")


if __name__ == "__main__":
    scenario_a()
    scenario_b()
    scenario_c()
