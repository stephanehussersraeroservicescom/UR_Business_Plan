# Sources externes du business plan Urban Rig

Ce dossier contient les preuves externes : statistiques publiques, études, textes réglementaires et prix de marché. Les preuves internes (constructeur, essais) restent dans `../preuves/`.

## Règle

Toute affirmation chiffrée du business plan doit renvoyer à un identifiant de `registre-sources.yaml`.

- Pas d'identifiant = pas de chiffre dans le plan.
- Un chiffre calculé à partir de sources (somme, soustraction, ratio) est marqué **[calcul]**, avec ses sources d'entrée.
- Une source secondaire (presse, site d'entreprise) peut être citée, mais elle est marquée comme telle et doit être remplacée par la source primaire dès que possible.

## Statuts utilisés

| Statut | Signification |
|---|---|
| `verifie` | Chiffre lu dans la source primaire, citation relevée |
| `verifie-recontrole` | Idem, et recontrôlé une seconde fois le 10/10/2026 |
| `secondaire` | Chiffre lu dans une source qui cite une autre source (presse, observatoire, entreprise) |
| `ancien` | Source primaire, mais données de plus de 8 ans : à actualiser |
| `calcul` | Valeur dérivée par nous de chiffres sourcés |
| `non-verifie` | Recherché sans succès ; ne pas utiliser dans le plan |

## Contenu

| Fichier | Objet |
|---|---|
| `registre-sources.yaml` | Registre unique : identifiant, titre, éditeur, date, URL, emplacement (page, tableau), statut |
| `01-composition-tonnages-OMR-France.md` | Composition des OMR (MODECOM 2024 et 2017), part plastique, tonnages DMA et OMR, modes de traitement, plastiques en France |
| `02-gate-fees-DMA-et-TGAP-France.md` | Coûts de traitement par mode (stockage, incinération, tri, TMB, compostage, méthanisation, CSR) et barèmes TGAP 2021 à 2030 |
| `index-sources.html` | Les 83 sources sous forme de liens cliquables, à ouvrir dans un navigateur |
| `telecharger-sources.sh` | Script à lancer sur ton ordinateur : télécharge les documents dans `pdf/` |
| `03-filieres-specialisees-France.md` | DASRI, DAE, plastiques, déchets dangereux, REP (pneus, VHU, DEEE, mobilier, textiles), boues, biodéchets, BTP, huiles, aéroports et ICW |

## Accès aux sources

Recherche faite le 10/10/2026. Les sources ont été lues en ligne. Le shell que Claude utilise sur l'ordinateur a un accès réseau filtré (liste blanche de la session) : les PDF se téléchargent avec `./telecharger-sources.sh`, lancé depuis un terminal normal.

Documents non lus directement, à récupérer à la main (navigateur) :

1. ~~Référentiel des coûts ADEME 2022 et 2023, loi de finances 2026 (TGAP)~~ : déposés dans `pdf/` et lus le 10/10/2026.
2. ADEME, *MODECOM 2024, analyse des résultats* (réf. 013089). Les chiffres sont repris ici depuis les données ouvertes ADEME, qui sont la même source.
3. ADEME, *Le traitement des DMA, édition 2024* (réf. 9470) et enquête ITOM 2022.
4. AMORCE, *Observatoire des coûts de stockage* (DT141).
5. Code des impositions sur les biens et services, art. L. 433-57 et L. 433-86 (tarifs TGAP 2026 et suivants), sur Légifrance.
6. Un bordereau de prix réel DASRI (appel d'offres CHU ou GHT, guide RESAH).

## Incidences sur les paramètres du modèle (`working-folder/params/`)

À arbitrer ; aucun fichier de paramètres n'a été modifié.

| Paramètre | Valeur actuelle | Ce que disent les sources | Point à trancher |
|---|---|---|---|
| `composition.part_plastique` | 0,30 | OMR France 2024 : **15,8 %** (MODECOM 2024). Tout-venant de déchèterie : 18 % | 0,30 n'est défendable que pour un gisement enrichi (refus de tri, DAE plastiques). Sur OMR brutes, la valeur sourcée est 0,158 |
| `composition.part_humidite` | 0,08 | OMR France 2024 : **42,1 %** (2017 : 36,9 %) | Écart majeur. 8 % ne correspond pas à des OMR brutes |
| `composition.part_organique` | 0,47 | Putrescibles 33,7 % + papiers-cartons 12,4 % + textiles sanitaires 17,0 % (2024) | Cohérent en ordre de grandeur si l'on regroupe organique et cellulose |
| `prix.gate_fee` | 110 €/t | Médianes nationales 2023 des OMR, TGAP comprise (ADEME) : stockage **138**, incinération **107**, TMB 156 €/t. En 2026, la TGAP passe à 69 €/t en stockage et à 16 ou 29 €/t en incinération (loi de finances 2026) ; estimation 2026 [calcul] : stockage 145 à 155, incinération ≈ 110 €/t | 110 €/t est aligné sur l'incinération et en dessous du stockage : hypothèse prudente pour des OMR. Le haut de fourchette (800) correspond aux DASRI (500 à 1 000 €/t, source ancienne) |
