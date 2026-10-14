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

## Ajout du 10/10/2026 (après-midi) : devenir des plastiques triés
- Nouveau dossier `04-devenir-plastiques-tries/` : note `README.md`, calcul `bilan_matiere.py` et sa sortie `bilan-matiere-resultats.md`.
- 41 sources ajoutées au registre (section « DEVENIR DES PLASTIQUES TRIES ») ; `index-sources.html` régénéré par `generer_index.py` (125 sources).
- Chiffres clés : 29,5 % des emballages ménagers plastiques recyclés en 2025 (346/1 174 kt, Citeo) ; refus de tri 23,0 % en 2022 (800 kt) ; 15 à 20 % du plastique entrant en centre de tri perdu aux refus ; rendements de régénération PET 73 %, PEHD 71 %, PP 69 %, films ménagers ≈ 50 % (PRE) ; sur 1 t entrant en centre de tri, 55 à 62 % deviennent du recyclat pour les rigides [calcul].
- Point à arbitrer : la composition nationale des refus de collecte sélective (OCAPEM 2025) ne donne que 12 % d'emballages plastiques, ce qui ne soutient pas `part_plastique = 0,30` pour ce gisement.

## Ajout du 10/10/2026 (fin d'après-midi) : analyse approfondie des refus plastiques
- `04-devenir-plastiques-tries/analyse-approfondie-refus-plastiques.md` et notes brutes dans `notes-recherche-2026-10-10/`.
- 84 sources ajoutées au registre (identifiants RP-001 à RP-084, champ `fiabilite` : mesuré, déclaré, modélisé, secondaire, ancien, non-vérifié).
- Chiffres clés recontrôlés : Île-de-France 2024, 539 795 t d'emballages et papiers collectés, 27 % de refus (146 368 t), 98 % incinérés, 18 centres pour 678 200 t/an (ORDIF) ; Syctom 129,4 €/t pour les anomalies de tri (2024) ; arrêté du 20/02/2023 (TGAP réduite : PCI ≥ 9 MJ/kg, refus ≤ 35 % pour les emballages ménagers) ; proposition ETS du 17/07/2026 (incinération à partir de 2031).
- Constat : aucune composition mesurée et documentée des refus français (PCI, chlore, humidité) n'est publique ; la caractérisation du gisement visé est un préalable.

## Ajout du 10/10/2026 (soir) : annexe 8 version 2
- `04-devenir-plastiques-tries/ANNEX-08-v2-plastique-non-recycle-France.md` (anglais), notes dans `notes-recherche-annexe-08-v2/`.
- 78 sources ajoutées au registre (RP2-001 à RP2-078).
- Recontrôlés directement : sous-catégories plastiques MODECOM 2024 (07.01 à 07.14, total 2 329 258 t ; films 1,28 Mt dont sacs poubelle 0,50 Mt) ; Citeo Observatoire de la reprise 2024 (plastiques 473 033 t ; prix moyens 203,4 et 235,3 €/t ; aide transport 10,4 €/t) ; ressource propre plastique France 1,564 Md€ (2023), 1,498 (2024), 1,464 (2025) (Sénat, PLF 2025) ; Bourges RPQS 2024 p. 26 (environ 35 % du flux développement incinéré en 2023, source Citeo) ; Platts 248,81 €/t (juin 2025) ; soutien Citeo 725 €/t (2023) et 776 €/t (2024) ; Ecoembes plastique mélange T3 2026 -0,44 à -0,55 €/kg ; Thermo-sur-Seine (3 × 111 MW, 1,6 TWh, à partir de 2031, tonnage non publié).
- Budget de recherche web épuisé pendant ce tour : pistes ouvertes listées dans la section « Data acquisition plan » de l'annexe (étude ADEME réf. 5955 accessible après saisie d'un e-mail, tonnages Valorplast par flux, diapositives 42 à 51 de l'Observatoire de la reprise, tarifs des syndicats franciliens).

## Ajout du 10/10/2026 (nuit) : contrôle des sources et paramètres du modèle
- Contrôle automatique installé : `working-folder/controle-sources/verifier_sources.py` (README, `calculs.yaml`, `cibles.yaml`). Rapport : `working-folder/out/controle-sources.html`.
- Le moteur (`engine/modele.py`) lit désormais aussi le registre externe : les paramètres peuvent citer des sources PRM-, RP-, RP2-.
- 155 sources de paramètres ajoutées au registre (PRM-xxx), notes dans `controle-sources/notes-parametres-2026-10-10/`.
- 11 paramètres confirmés et rattachés (gate_fee, cout_etp, provision, inflation, prix_carbonate, cout_concentrat, duree_amortissement, criblage_char, rec_metaux_char, rec_alu, pci_char). Aucune valeur modifiée.
- 36 paramètres à arbitrer par Stéphane : `params/_arbitrages.yaml` et `controle-sources/arbitrages-parametres-2026-10-10.md`.
