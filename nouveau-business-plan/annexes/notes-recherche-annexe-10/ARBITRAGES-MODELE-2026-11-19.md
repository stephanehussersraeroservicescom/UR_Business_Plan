# Modèle financier, étape 1 : paramètres à trancher (19/11/2026)

Fiche de décision pour Stéphane. Elle regroupe les 70 entrées de `working-folder/params/_arbitrages.yaml` (annexes 1, 2, 3, 5, 7, 8, 9) et les décisions déjà prises. **Aucune valeur de `params/*.yaml` n'a été modifiée.** Chaque valeur de la partie A vient d'une fiche du registre, d'un calcul ou d'une décision datée. Dans la partie B, les propositions sans référence sont des HYPOTHÈSES de Claude (19/11/2026), sans source, à trancher par toi.

Pour répondre vite : « A : appliquer. B : d'accord avec les propositions sauf B3 et B7 (…). C : d'accord. »

## Deux problèmes de méthode avant tout

1. **Aucune brique n'est validée au sens de la méthode.** Le contrôle automatique est à zéro erreur sur toutes les annexes. En revanche, aucune contre-vérification Codex n'a été faite et aucun échantillon n'a été coché par toi. Or la méthode dit que le modèle ne lit que des briques validées. Proposition : construire le modèle maintenant, en affichant sur chaque valeur le statut de sa brique (« contrôlée, non contre-vérifiée »). On ne le présente pas à un investisseur avant validation.
2. **Le moteur actuel ne connaît qu'un seul déchet moyen.** Il recalcule les produits à partir de `composition.yaml`. Les annexes 5, 7 et 8 donnent déjà, par flux, les produits par tonne en trois scénarios [hyp:D-047]. Proposition : un modèle par flux qui lit directement ces bilans par tonne. Il y aurait quatre flux : plastiques (annexe 8), OMR (annexe 5), DAE (annexe 7), CDG plus tard. Chaque flux a ses trois scénarios, choisis sur la page web.

## A. Déjà décidé : il reste à l'appliquer dans params/

| Paramètre | Valeur héritée | Valeur à appliquer | Fondement |
|---|---|---|---|
| machine | 50 000 000 EUR | 50 000 000 EUR, options PRIMO, SEA CORAL et FORCE 9 comprises, hors livraison | [hyp:D-050] |
| installation | 200 000 EUR | 0 (comprise dans le prix) | [hyp:D-051] |
| fret | 400 000 EUR | 0, non compté, mention « hors transport » | [hyp:D-051] |
| pre_tri | 1 080 000 EUR | 5 000 000 EUR par ligne | [hyp:D-051] |
| Bâtiment, génie civil, ingénierie, permis (lignes surfaces × prix, VRD, ingénierie) | environ 10 lignes | une ligne de 5 000 000 EUR | [hyp:D-051] |
| capacite / densite | 200 × 0,7 | 140 t/jour de charge réacteur | [hyp:D-035] |
| rdt_gaz_plastique | 0,193 | 0,10 | [hyp:D-029] |
| pci_char, pci_residu_plastique | 15 et 25 MJ/kg | 32,09 MJ/kg (char d'OMR) et 24,6 MJ/kg (char de plastique) | [hyp:D-038] |
| Prix de l'huile | 2 prix (350 et 641 EUR/t) | 3 fractions 80/10/10 au prix de référence : 636,8, 1 254 et 541 EUR/t, avec un facteur de qualité (voir B1) | [hyp:D-028] [hyp:D-030] |
| prix_ferreux, prix_alu | 250 et 1 400 EUR/t | 316,4 et 1 723 EUR/t | [A3H-COMEXT-MENSUEL-2025-2026] [hyp:D-030] |
| prix_verre, prix_carbone | 30 EUR/t ; 50 EUR/t CO2 | 0 ; 0 (pas de revenu carbone) | [hyp:D-028] |
| prix_elec | 0,15 EUR/kWh | 0,1212 EUR/kWh | [PRM-EUROSTAT-NRGPC205-ID-2025] [hyp:D-030] |
| prix_fioul | 0,95 EUR/L | 1,3405 EUR/L hors taxes | [A3-DGEC-NPG-2026-10-09-PRIX-FRANCE] [hyp:D-030] |
| gate_fee | 110 EUR/t unique | table par flux, modifiable : OMR et flux payants 100 EUR/t, balles de plastique achetées 249 EUR/t (prix négatif) | [hyp:D-041] [hyp:D-042] |
| Scénarios | aucun | pessimiste, standard, optimiste, choisis sur la page web | [hyp:D-047] |

## B. À trancher : ma proposition et ce qu'elle change

| N° | Sujet | Ma proposition | Pourquoi |
|---|---|---|---|
| B1 | Facteur de qualité de l'huile | 0,80 par défaut, réglable | Sapporo vendait ses huiles à 80 à 90 % du fioul [A3F-SAPPORO-SPR-2009-PRIX-FRACTIONS] ; l'huile d'OMR est hors spécification [A3-ARRETE-SSD-HUILE-PYROLYSE-2024] |
| B2 | Prix du char | 0 EUR/t par défaut, réglable de -50 à 123 EUR/t | Aucun acheteur identifié ; 123 EUR/t est la parité coke de pétrole [calc:CALC-A3-CHAR-PARITE-PETCOKE] |
| B3 | Chaleur manquante sur OMR et DAE | Achetée en combustible par défaut ; option « brûler le char » dans le modèle | Sur OMR, le gaz du plastique ne couvre pas l'évaporation de l'eau [calc:CALC-A5-EAU-KG-T] ; OneWorld indique 10 000 L de combustible par jour [OW-CONSO-ENERGIE]. **C'est le paramètre qui pèse le plus sur les OMR.** |
| B4 | Rendements OMR et DAE par défaut | Scénario standard ; char à 30 % | [hyp:D-044] [hyp:D-045] ; à confirmer par toi (D-043 à D-046, D-048, D-049) |
| B5 | Électricité consommée | 600 kW, soit 14 400 kWh/jour, valeur haute | La fiche OneWorld donne 20 kW, le tableau de consommation 600 kW [UR2000-JP-P08-SPEC] [OW-CONSO-ENERGIE] ; l'annexe 2 prend la plus haute |
| B6 | Besoin de chaleur du procédé | 1 507 MJ/t | Puissance du brûleur OneWorld [calc:CALC-A2-BRULEUR-MJ-T] |
| B7 | ATEX, post-tri, décanteur (1,33 MEUR hérités) | Compris dans les 5 MEUR de pré-traitement ou de bâtiment ; aucune ligne propre | Ces lignes n'ont pas de source (V3-MODEL) ; à toi de dire si D-051 les couvre |
| B8 | Aléas | HYPOTHÈSE de Claude : 10 % du CAPEX | Premier exemplaire en France ; la valeur héritée (5 %) n'a pas de source lue |
| B9 | Montée en charge | HYPOTHÈSE de Claude : 60 % l'année 1, 80 % l'année 2 | Les valeurs héritées (70 et 85 %) n'ont pas de source lue |
| B10 | Jours d'exploitation | HYPOTHÈSE : garder les 330 jours par an hérités | Les sources citées par l'ancien modèle n'ont pas été relues en v3 |
| B11 | Effectif | À fixer par toi avec OneWorld ; HYPOTHÈSE de Claude : 20 ETP par défaut | Les 15 ETP hérités n'ont pas de source lue ; fonctionnement en continu |
| B12 | Maintenance | 1 % les années 1 à 4, puis 4 % | Cotation OneWorld héritée [hyp:D-007] |
| B13 | Assurance | HYPOTHÈSE de Claude : 1 % du CAPEX | Pas de cotation (R-007) ; les 0,5 % hérités n'ont pas de source lue |
| B14 | Financement | HYPOTHÈSE de Claude : deux structures affichées, 100 % fonds propres, et 60 % de dette à 7 % sur 10 ans ; taux à sourcer | Les 12 % d'intérêt avec 70 % de dette hérités paraissent incohérents |
| B15 | TGAP payée par l'usine | Interrupteur, désactivé par défaut ; 16 EUR/t si activé | Non tranché (R-050) [CIBS-TGAP-2026] |
| B16 | Hydrogène (flux plastique seul) | Non compté par défaut ; option à 2 EUR/kg | [hyp:D-031] [A3J-ACER-H2-MARKETS-2025] |
| B17 | Horizon et amortissement | HYPOTHÈSE : garder les 15 ans hérités pour les deux | À inscrire comme décision |

## C. Ordre de construction proposé, après tes réponses

1. Appliquer A et B dans `params/*.yaml` avec une décision datée par groupe, puis vider les entrées correspondantes de `_arbitrages.yaml`.
2. Adapter le moteur : un flux et un scénario choisis donnent les produits par tonne, lus dans `calculs.yaml`.
3. Annexe 13, plastiques, en premier : c'est le seul flux dont le bilan énergétique est bouclé.
4. Ensuite l'annexe 10 (OMR), puis l'annexe 12 (DAE). L'annexe 11 (CDG) reste de côté.
5. Contrôle, échantillon et contre-vérification, comme pour les annexes.
