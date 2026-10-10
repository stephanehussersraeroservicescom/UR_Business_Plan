# Passation : session du 10/10/2026 (sources externes)

## Objectif
Créer un référentiel de sources externes pour le business plan Urban Rig. Règle fixée par Stéphane : toute affirmation chiffrée du plan doit renvoyer à une source exacte (titre, éditeur, date, URL, page ou tableau, citation).

## Ce qui a été fait
Dossier créé : `working-folder/reference/sources-externes/`
- `README.md` : règle, statuts (verifie, verifie-recontrole, secondaire, ancien, calcul, non-verifie), liste des fichiers, incidences sur `params/`.
- `registre-sources.yaml` : 84 sources (id, titre, éditeur, date, url, emplacement, contenu, citation, statut, fichier local). Complète `params/_evidence.yaml`, qui reste dédié aux preuves internes.
- `01-composition-tonnages-OMR-France.md` : MODECOM 2024 (référence) et 2017, tonnages DMA et OMR, modes de traitement, plastiques.
- `02-gate-fees-DMA-et-TGAP-France.md` : coûts par mode de traitement, barèmes TGAP 2021 à 2030.
- `03-filieres-specialisees-France.md` : DASRI, DAE, plastiques, déchets dangereux, REP, boues, biodéchets, BTP, huiles, aéroports et ICW.
- `index-sources.html` : tableau cliquable de toutes les sources et des fichiers locaux.
- `telecharger-sources.sh` : script à lancer par Stéphane dans son terminal (le shell de Claude sur sa machine a un réseau filtré, erreur 403 du proxy) ; il télécharge les sources dans `pdf/`.
- `pdf/` : Stéphane y a déposé à la main les référentiels des coûts ADEME 2022 et 2023 (PDF et XLSX) et le JORF du 20/02/2026 (loi de finances 2026). Les trois ont été lus.

Dans les fichiers .md, chaque identifiant de source est un lien cliquable vers la source. Aucun fichier de `params/` n'a été modifié.

## Chiffres clés vérifiés
- OMR 2024 (MODECOM 2024, données ouvertes ADEME) : plastiques **15,8 %** (35,3 kg/hab, 2,33 Mt) ; putrescibles 33,7 % ; textiles sanitaires 17 % ; humidité **42,1 %** ; total 223,5 kg/hab.
- OMR 2021 (INSEE) : 67,9 % incinérées, 23,1 % stockées, 7,2 % en valorisation organique.
- Coûts nets médians de traitement des OMR, € HT/t, TGAP comprise (référentiel ADEME 2023, fig. 33, p. 36) : incinération **107**, stockage **138**, TMB compostage **156**. Données 2022 (fig. 66, p. 63) : 106, 122, 150.
- TGAP (CIBS L. 433-57 et L. 433-86, loi n° 2026-103) : stockage 69 €/t (2026) jusqu'à 85 €/t (2030) ; incinération 16 à 20 €/t (performance ≥ 65 %) ou 29 à 45 €/t (< 65 %) ; résidus de tri performants 8 à 10 €/t.
- DASRI : ≈ 170 kt/an ; 81 % incinérés, 19 % désinfectés (HCSP 2019) ; 500 à 1 000 €/t (chiffre ancien, ADEME 2007-2008).
- Déchets dangereux : 11,4 Mt (SDES 2022). Restauration internationale (ICW) : incinération obligatoire (règlement UE 1069/2009).

## Écarts relevés avec le modèle (à arbitrer avec Stéphane)
- `composition.part_plastique` = 0,30 contre 0,158 sourcé pour des OMR brutes. 0,30 n'est défendable que pour un gisement enrichi (refus de tri, DAE plastiques).
- `composition.part_humidite` = 0,08 contre 0,42 sourcé. C'est l'écart le plus important.
- `prix.gate_fee` = 110 €/t : prudent. Estimation 2026 [calcul] : stockage 145 à 155 €/t, incinération ≈ 110 €/t.

## Restant à faire
- Date d'effet des tarifs TGAP 2026 (19/02 ou 01/03/2026).
- Prix DASRI récent (bordereau d'appel d'offres CHU ou GHT, guide RESAH).
- Prix récents pour les déchets dangereux, l'incinération sans valorisation, les refus plastiques, les tonnages et coûts d'ICW à CDG (Groupe ADP).
- Lancer `telecharger-sources.sh`, puis relire les sources encore marquées « secondaire ».
- Décider si les paramètres de `params/` doivent pointer vers les identifiants du registre.

Style de Stéphane : français, ton direct, pas de tiret long.
