Accès internet : OUI
Lecture des PDF : OUI. La synthèse MODECOM 2024 de l'ADEME et le rapport ORDIF sur les DMA 2022 ont été ouverts et lus directement en ligne. Les deux jeux de données ADEME ont été relus dans les copies CSV d'origine conservées dans le dépôt.

## Périmètre et question de décision

Lot 1 de l'annexe 5, sections 5.1 à 5.4 : tonnages, composition par catégorie, humidité, pouvoir calorifique et matières non convertibles. Tous les calculs `CALC-A5-CAT*`, `CALC-A5-OMR-T` et `CALC-A5-NONPROC-*` ont été refaits.

La question pratique est la suivante : la caractérisation des OMR françaises est-elle suffisamment juste pour servir de base au modèle d'une machine de 51 100 t/an, et révèle-t-elle dès maintenant un obstacle évident ?

## Sources d'origine ouvertes

- ADEME, *Caractérisation des déchets ménagers et assimilés, MODECOM 2024* : https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf
- ADEME, jeu de composition `omrcs-compo-jdd` : https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv ; copie lue : `working-folder/reference/sources-externes/pdf/ADEME-MODECOM-2024-omrcs-compo-jdd-2026-11-19.csv`.
- ADEME, jeu d'humidité `omrhum` : https://data.ademe.fr/data-fair/api/v1/datasets/omrhum/lines?format=csv&size=10000 ; copie lue : `working-folder/reference/sources-externes/pdf/ADEME-MODECOM-2024-omrhum-2026-11-19.csv`.
- ADEME, grille de tri `omrcs-grille` : https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-grille/lines?format=csv&size=200 ; copie lue : `working-folder/reference/sources-externes/pdf/ADEME-MODECOM-2024-omrcs-grille-extrait-2026-11-19.csv`.
- ORDIF, *Les déchets ménagers et assimilés en Île-de-France, données 2022* : https://www.ordif.fr/fileadmin/DataStorage/user_upload/ORDIF_Rapp_DMA_2022_V1b.pdf

## Tableau des verdicts

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---|---|---|---|---|---|---|---|---|
| 1 | 5.1, 5.L.a | OMR métropolitaines | 14 752 013 t ; 223,46 kg/hab ; année 2024 | RP2-004 | DIFFÉRENT | « Tonnage 2023 14 752 013 ; Ratio 2023 223,46 » | MODECOM 2024, tableau 6, p. 39 du PDF | Valeurs exactes, mais le tonnage et le ratio viennent de l'Enquête Collecte 2023. L'année 2024 est celle de la caractérisation et du bilan recomposé. E-1. |
| 2 | 5.1, 5.C.s | Somme des catégories ouvertes | 14 752 013 t ; 223,54 kg/hab | ADEME-MODECOM-2024-DATA ; CALC-A5-OMR-T | CONFIRMÉ | Colonne `tonnage_OMR`, somme = 14 752 013 ; colonne `ratio_OMR`, somme = 223,54 | CSV `omrcs-compo-jdd`, 71 lignes de sous-catégories | Recalcul indépendant exact. Le petit écart avec 223,46 vient de l'addition de ratios arrondis. |
| 3 | 5.1, 5.P.a | OMR d'Île-de-France | 3,32 Mt ; 268 kg/hab ; 2022 | ORDIF-DMA-2022 | CONFIRMÉ | « avec 3,32 Mt d'Omr (268 kg/hab) » | ORDIF, Données 2022, p. 18 du PDF | Même valeur, unité, année et périmètre. |
| 4 | 5.1, 5.L.a | Échantillonnage national | 100 échantillons prévus, 50 communes, 5 exclus, 95 analysés | RP2-004 | CONFIRMÉ | « 100 échantillons d'OMR [...] issus de 50 communes » ; « Cinq échantillons [...] retirés [...] ce qui porte à 95 le nombre d'échantillons analysés » | MODECOM 2024, p. 13 du PDF | Échantillonnage national, pas une mesure propre au futur bassin d'approvisionnement. |
| 5 | 5.1, 5.P.a | Destination des DMA résiduels franciliens | 94 % vers 18 incinérateurs | ORDIF-DMA-2022 | CONFIRMÉ | « Le flux des déchets ménagers et assimilés résiduels de l'Île-de-France est à 94 % acheminé vers 18 unités d'incinération » | ORDIF, p. 20 du PDF | Le texte de l'annexe conserve le bon périmètre. |
| 6 | 5.1, fiche 8.P.f | Incinération régionale | 3 810 761 t ; 93 % de la capacité technique ; 2022 | A8-CST-ORDIF-UIDND-2023 | CONFIRMÉ | « 3 810 761 tonnes en 2022 » ; « 93% de la capacité technique des fours » | Fiche 8.P.f, valeurs reprises de la notice ORDIF | Valeurs reprises identiques à l'annexe 8, conformément à la consigne de comparaison simple. |
| 7 | 5.2, 5.C.t et 5.C.a | Putrescibles | 4 966 318 t ; 33,67 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT01-* | CONFIRMÉ | `01.01` 2 873 916 ; `01.02` 717 838 ; `01.03` 566 819 ; `01.04` 61 807 ; `01.05` 477 767 ; `01.06` 268 171 | CSV composition, lignes 01.01 à 01.06 | Somme 4 966 318 ; division par 14 752 013 = 33,6654 %. |
| 8 | 5.2, 5.C.y et 5.C.z | Papiers | 854 481 t ; 5,79 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT02-* | CONFIRMÉ | `02.01` 250 784 ; `02.02` 452 203 ; `02.03` 151 494 | CSV composition, lignes 02.01 à 02.03 | Somme 854 481 ; part 5,7923 %. |
| 9 | 5.2, 5.C.w et 5.C.x | Cartons | 973 969 t ; 6,60 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT03-* | CONFIRMÉ | `03.01` 581 627 ; `03.02` 337 191 ; `03.03` 3 024 ; `03.04` 52 127 | CSV composition, lignes 03.01 à 03.04 | Somme 973 969 ; part 6,6023 %. |
| 10 | 5.2, 5.C.ai et 5.C.aj | Composites | 294 383 t ; 2,00 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT04-* | CONFIRMÉ | `04.01` 78 114 ; `04.02` 64 087 ; `04.03` 131 937 ; `04.04` 2 495 ; `04.05` 17 750 | CSV composition, lignes 04.01 à 04.05 | Somme 294 383 ; part 1,9955 %. |
| 11 | 5.2, 5.C.ac et 5.C.ad | Textiles | 718 435 t ; 4,87 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT05-* | CONFIRMÉ | `05.01` 51 298 ; `05.02` 443 844 ; `05.03` 79 126 ; `05.04` 76 452 ; `05.05` 29 637 ; `05.06` 1 929 ; `05.07` 36 149 | CSV composition, lignes 05.01 à 05.07 | Somme 718 435 ; part 4,8701 %. |
| 12 | 5.2, 5.C.u et 5.C.b | Textiles sanitaires | 2 505 734 t ; 16,99 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT06-* | CONFIRMÉ | `06.01` 859 734 ; `06.02` 380 662 ; `06.03` 1 265 338 | CSV composition, lignes 06.01 à 06.03 | Somme 2 505 734 ; part 16,9857 %. |
| 13 | 5.2, 5.C.v et 5.C.d | Plastiques | 2 329 258 t ; 15,79 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT07-* | CONFIRMÉ | `07.01` 496 503 ; `07.02` 165 000 ; `07.03` 619 942 ; `07.04` 160 966 ; `07.05` 51 533 ; `07.06` 23 899 ; `07.07` 44 178 ; `07.08` 443 885 ; `07.09` 5 461 ; `07.10` 40 401 ; `07.11` 40 123 ; `07.12` 14 665 ; `07.13` 5 254 ; `07.14` 217 448 | CSV composition, lignes 07.01 à 07.14 | Somme 2 329 258 ; part 15,7894 %. |
| 14 | 5.2, 5.C.ao et 5.C.ap | Bois | 141 917 t ; 0,96 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT08-* | CONFIRMÉ | `08.01` 40 628 ; `08.02` 1 186 ; `08.03` 1 531 ; `08.04` 98 572 | CSV composition, lignes 08.01 à 08.04 | Somme 141 917 ; part 0,9620 %. |
| 15 | 5.2, 5.C.aa et 5.C.ab | Verre | 739 213 t ; 5,01 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT09-* | CONFIRMÉ | `09.01` 699 571 ; `09.02` 39 642 | CSV composition, lignes 09.01 et 09.02 | Somme 739 213 ; part 5,0109 %. |
| 16 | 5.2, 5.C.ae et 5.C.af | Métaux | 493 070 t ; 3,34 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT10-* | CONFIRMÉ | `10.01` 17 735 ; `10.02` 178 647 ; `10.03` 82 936 ; `10.04` 92 317 ; `10.05` 75 637 ; `10.06` 40 981 ; `10.07` 813 ; `10.08` 4 004 | CSV composition, lignes 10.01 à 10.08 | Somme 493 070 ; part 3,3424 %. |
| 17 | 5.2, 5.C.ak et 5.C.al | Autres matières organiques | 227 604 t ; 1,54 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT11-* | CONFIRMÉ | `11.01`, `tonnage_OMR` = 227 604 | CSV composition, ligne 11.01 | Part 1,5429 %. |
| 18 | 5.2, 5.C.ag et 5.C.ah | Autres matières minérales | 320 842 t ; 2,17 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT12-* | CONFIRMÉ | `12.01` 17 806 ; `12.02` 303 036 | CSV composition, lignes 12.01 et 12.02 | Somme 320 842 ; part 2,1749 %. |
| 19 | 5.2, 5.C.am et 5.C.an | Déchets dangereux ou spécifiques | 186 789 t ; 1,27 % | ADEME-MODECOM-2024-DATA ; CALC-A5-CAT13-* | CONFIRMÉ | `13.01` 97 698 ; `13.02` 792 ; `13.03` 5 178 ; `13.04` 3 790 ; `13.05` 17 548 ; `13.06` 2 874 ; `13.07` 1 879 ; `13.08` 9 693 ; `13.09` 23 530 ; `13.10` 23 807 | CSV composition, lignes 13.01 à 13.10 | Somme 186 789 ; part 1,2662 %. |
| 20 | 5.2, 5.C.s | Total des 13 catégories | 14 752 013 t ; 100 % | CALC-A5-OMR-T | CONFIRMÉ | `4 966 318 + 854 481 + 973 969 + 294 383 + 718 435 + 2 505 734 + 2 329 258 + 141 917 + 739 213 + 493 070 + 227 604 + 320 842 + 186 789` | Recalcul indépendant à partir du CSV | Résultat exact : 14 752 013. |
| 21 | 5.2, 5.P.b, 5.P.c, 5.L.a | Traitement des fines | Absentes du jeu de composition ; 5,4 % dans le jeu humidité ; surtout putrescibles | ADEME-MODECOM-2024-DATA ; ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | Composition : `14.02`, colonnes OMR vides ; humidité : `S18`,`14.02`,`5,4%`,`46,3%` ; « Les éléments fins < 8 mm des OMR sont majoritairement composés de déchets putrescibles » | CSV composition, ligne 14.02 ; CSV humidité, ligne S18 ; MODECOM, note 16 p. 22 | D-046 est explicitement présentée comme hypothèse de raccordement entre deux jeux. Elle est raisonnable provisoirement, mais le rapport technique complet doit confirmer l'allocation. |
| 22 | 5.2, 5.P.d et 5.L.a | Évolution depuis 2017 | 252,7 à 223,5 kg/hab ; humidité 36,9 % à 42,1 % | ADEME-CP-2025 ; RP2-004 | CONFIRMÉ | « 2017 252,7 ; 2024 223,5 » ; « Taux d'humidité 2017 36,9 % [...] Taux d'humidité 2024 42,1 % » | MODECOM 2024, figure p. 14 et tableau 1 p. 22 | Les valeurs sont exactes. |
| 23 | 5.3 | Déchets de jardin | 3,0 % ; humidité 59,7 % ; PCI 16 606 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S01`,`3,0%`,`59,7%` ; « Déchets de Jardin [...] PCI moyen en 2024 16 606 » | CSV humidité, S01 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 24 | 5.3 | Autres putrescibles | 26,3 % ; 59,6 % ; 16 975 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S02`,`26,3%`,`59,6%` ; « Autres fractions putrescibles [...] 16 975 » | CSV humidité, S02 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 25 | 5.3 | Papiers | 5,7 % ; 28,9 % ; 14 398 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S03`,`5,7%`,`28,9%` ; « Papiers [...] 14 398 » | CSV humidité, S03 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 26 | 5.3 | Cartons | 6,6 % ; 33,7 % ; 15 635 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S04`,`6,6%`,`33,7%` ; « Cartons [...] 15 635 » | CSV humidité, S04 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 27 | 5.3 | Emballages composites | 1,8 % ; 28,3 % ; 19 794 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S05`,`1,8%`,`28,3%` ; « Emballages composites [...] 19 794 » | CSV humidité, S05 ; MODECOM, tableau 2 p. 23 | La fraction S06, autres composites, est omise du tableau de l'annexe. E-5. |
| 28 | 5.3 | Textiles | 4,9 % ; 33,7 % ; 18 466 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S07`,`4,9%`,`33,7%` ; « Textiles [...] 18 466 » | CSV humidité, S07 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 29 | 5.3 | Textiles sanitaires | 17,0 % ; 60,0 % ; 18 040 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S08`,`17,0%`,`60,0%` ; « Textiles sanitaires [...] 18 040 » | CSV humidité, S08 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 30 | 5.3 | Films plastiques | 8,6 % ; 35,8 % ; 27 808 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S09`,`8,6%`,`35,8%` ; « Films plastiques [...] 27 808 » | CSV humidité, S09 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 31 | 5.3 | Autres plastiques | 7,0 % ; 20,1 % ; 25 616 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S10`,`7,0%`,`20,1%` ; « Autres fractions plastiques [...] 25 616 » | CSV humidité, S10 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 32 | 5.3 | Bois, emballages et autres | 0,3 % / 0,7 % ; 13,0 % / 26,0 % ; 17 300 / 17 822 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S11`,`0,3%`,`13,0%` ; `S12`,`0,7%`,`26,0%` ; « Emballages en bois [...] 17 300 » ; « Autres fractions en bois [...] 17 822 » | CSV humidité, S11-S12 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 33 | 5.3 | Autres matières organiques | 1,4 % ; 27,5 % ; 16 781 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S15`,`1,4%`,`27,5%` ; « Autres matières organiques [...] 16 781 » | CSV humidité, S15 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 34 | 5.3 | Verre | 4,7 % ; 2,2 % ; PCI non analysé | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S13`,`4,7%`,`2,2%` ; « Verre [...] NA » | CSV humidité, S13 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 35 | 5.3 | Métaux | 3,3 % ; 13,2 % ; PCI non analysé | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S14`,`3,3%`,`13,2%` ; « Métaux [...] NA » | CSV humidité, S14 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 36 | 5.3 | Autres matières minérales | 2,0 % ; 14,1 % ; PCI non analysé | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S17`,`2,0%`,`14,1%` ; « Autres matières minérales [...] NA » | CSV humidité, S17 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 37 | 5.3 | Fines de moins de 8 mm | 5,4 % ; 46,3 % ; 9 819 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S18`,`5,4%`,`46,3%` ; « Eléments fins < 8mm [...] 9 819 » | CSV humidité, S18 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 38 | 5.3 | Moyenne des OMR | Humidité 42,1 % ; PCI 16,3 MJ/kgMS et 8,4 MJ/kg brut | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | « Le taux d'humidité moyen des OMR est ainsi de 42,1 %, avec un large intervalle de confiance (± 6,3 %) » ; « 16,3 MJ/kgMS (± 2,9 MJ/kgMS) » ; « 8,4 MJ/kgMB » | MODECOM, p. 22-23 du PDF | Valeurs centrales exactes. L'annexe omet les intervalles dans son tableau, alors que la source demande de la prudence. E-2. |
| 39 | 5.3 | Nombre d'analyses de laboratoire | Humidité sur 20 échantillons ; PCI sur 15 | RP2-004 | CONFIRMÉ | « des mesures d'humidité sur 20 échantillons d'OMR et des mesures de pouvoir calorifique inférieur sur 15 échantillons d'OMR » | MODECOM, p. 13 du PDF | Exact. Les effectifs limités expliquent les intervalles larges. |
| 40 | 5.3 | Traitement des fractions non analysées dans le PCI | Valeur zéro, moyenne légèrement sous-estimée | RP2-004 | CONFIRMÉ | « calculé avec une valeur de PCI nulle pour les fractions non analysées de verre, de métaux, d'autres matières minérales et de DMS, sa valeur est légèrement sous-estimée » | MODECOM, p. 23 du PDF | Exact. |
| 41 | 5.3 | Origine de l'humidité des plastiques | « mostly water and food soiling stuck to the plastic » | ADEME-MODECOM-2024-HUM ; RP2-004 | ABSENT | « ont absorbé de l'humidité au contact des autres déchets présents au sein des OMR » | MODECOM, p. 22 du PDF | La source confirme l'humidité acquise au contact, mais pas que les salissures alimentaires en sont la cause principale. E-4. |
| 42 | 5.3 | Plastiques, fractions au PCI sec le plus élevé | 27 808 et 25 616 J/gMS | RP2-004 | CONFIRMÉ | « Films plastiques [...] 27 808 » ; « Autres fractions plastiques [...] 25 616 » | MODECOM, tableau 2 p. 23 | Ce sont bien les deux valeurs les plus hautes des fractions analysées. |
| 43 | 5.4, 5.C.aq et 5.C.f | Somme dite non convertible | 1 739 914 t ; 11,79 % | CALC-A5-NONPROC-* | CONFIRMÉ | `739 213 + 493 070 + 320 842 + 186 789` | Recalcul indépendant à partir des catégories 09, 10, 12 et 13 | Résultat exact : 1 739 914 t et 11,7944 %. À 51 100 t/an, cela représente environ 6 027 t/an. |
| 44 | 5.4 | Les quatre catégories sont toutes « non convertibles » | Verre, métaux, minéraux, déchets dangereux ou spécifiques | Aucune source technique citée pour ce classement | NON SOURCÉ | Aucune citation technique fournie | Section 5.4 | Verre, métaux et minéraux sont raisonnablement inertes en pyrolyse. La catégorie 13 mélange toutefois DEEE, piles, médicaments, huiles, cartouches et bouteilles de gaz : « à retirer pour sécurité et conformité » serait plus exact que « non convertible ». E-3. |
| 45 | 5.4, fiche 2.5.b.11 | Métaux et corps étrangers d'un essai municipal à Chiba | 27,8 % de l'entrée | CALC-A2-NONPLAST-NODA-0909 | CONFIRMÉ | `13,9 kg / 50 kg = 0,278` | Fiche 2.5.b.11, essai du 09/09/2022, valeurs reprises | Le calcul est exact. Le flux est celui de plastiques d'emballages municipaux, pas des OMR françaises brutes. |
| 46 | 5.4 | Les inertes passent inchangés et sortent avec le résidu solide | Affirmation qualitative | Aucune source directement reliée à la phrase | NON SOURCÉ | Aucune citation directe fournie | Section 5.4 | Lecture physiquement plausible dans un cas standard, mais le mot « inchangés » et le chemin de sortie doivent être confirmés sur l'équipement et son prétraitement. |
| 47 | 5.4 | Les objets dangereux relèvent surtout de la sécurité et des permis | Affirmation qualitative | Aucune source réglementaire ou technique citée | NON SOURCÉ | Aucune citation directe fournie | Section 5.4 | Conclusion raisonnable, mais la ligne de tri, les critères d'acceptation et le traitement des refus ne sont pas encore définis. E-3. |

## Recalcul des calculs demandés

Les 29 calculs demandés ont été refaits indépendamment : 13 tonnages de catégories, 13 pourcentages, le total OMR, le tonnage non convertible et son pourcentage.

Résultat : **29 calculs exacts, 0 CALCUL FAUX**.

Les pourcentages sont cependant affichés avec une précision supérieure à celle des pourcentages publiés par l'ADEME, qui sont arrondis à 0,1 point et accompagnés d'intervalles de confiance. Cette précision calculatoire ne doit pas être confondue avec une précision statistique.

## Mise à l'échelle du projet

Pour 51 100 t/an d'OMR moyennes :

| Élément | Part | Ordre de grandeur annuel |
|---|---:|---:|
| Verre | 5,01 % | 2 561 t/an |
| Métaux | 3,34 % | 1 708 t/an |
| Autres minéraux | 2,17 % | 1 111 t/an |
| Déchets dangereux ou spécifiques | 1,27 % | 647 t/an |
| Total classé non convertible | 11,79 % | 6 027 t/an |

Avec l'intervalle d'humidité publié, 42,1 % ± 6,3 %, une tonne moyenne peut contenir environ 358 à 484 kg d'eau. À l'échelle d'une machine, cela correspond à environ 18 300 à 24 700 t d'eau par an. Cette dispersion n'empêche pas de retenir 42,1 % comme cas standard, mais elle doit être conservée dans le bilan énergétique et le dimensionnement du prétraitement.

## Écarts

### E-1. Année du tonnage national mal étiquetée

- Annexe : 14 752 013 t et 223,46 kg/hab, année 2024.
- Source : tableau 6, Enquête Collecte 2023, 14 752 013 t et 223,46 kg/hab.
- Gravité : **MINEUR**.
- Incidence : aucune sur l'ordre de grandeur ou l'approvisionnement. La distinction importe pour la traçabilité statistique.
- Correction proposée : écrire « volume de collecte 2023, utilisé dans le bilan MODECOM 2024 ».

### E-2. Incertitude statistique insuffisamment visible

- Annexe : 42,1 % d'humidité et 16,3 MJ/kgMS dans le tableau principal.
- Source : 42,1 % ± 6,3 % et 16,3 ± 2,9 MJ/kgMS ; elle précise que les résultats doivent être considérés « avec beaucoup de prudence ».
- Gravité : **IMPORTANT**.
- Incidence : la valeur standard passe, mais les variantes humide et sèche peuvent modifier fortement les besoins de chaleur, sujet central du lot 3.
- Correction proposée : ajouter les intervalles de confiance au tableau et propager au moins une sensibilité sur l'eau et l'énergie.

### E-3. Classement opérationnel des refus non démontré

- Annexe : 11,79 % « cannot convert », incluant toute la catégorie des déchets dangereux ou spécifiques.
- Source statistique : elle mesure ces catégories, mais ne décrit ni leur comportement dans l'Urban Rig ni la ligne de retrait.
- Gravité : **IMPORTANT**.
- Incidence : environ 6 027 t/an de solides ou refus, dont environ 647 t/an de catégorie 13, doivent avoir une voie de séparation et de traitement. Ce n'est pas bloquant si un prétri et une filière de refus sont prévus.
- Correction proposée : distinguer les inertes physiquement non convertibles des objets exclus pour sécurité ou conformité, puis définir les performances du prétri et les exutoires.

### E-4. Salissures alimentaires présentées comme cause principale sans preuve

- Annexe : l'humidité des plastiques est « mostly water and food soiling ».
- Source : elle dit seulement que les fractions ont absorbé de l'humidité au contact des autres déchets.
- Gravité : **MINEUR**.
- Incidence : aucune sur les humidités mesurées ni sur le calcul de matière sèche.
- Correction proposée : remplacer par « humidité acquise au contact des autres déchets ».

### E-5. Tableau physico-chimique incomplet

- Fraction omise : autres composites, 0,1 % de la masse, 18,8 % d'humidité et PCI 19 251 J/gMS.
- La catégorie dangereuse, environ 1,2 % dans le jeu d'humidité, n'a pas de ligne de mesure.
- Gravité : **MINEUR**.
- Incidence : la somme des parts affichées n'atteint que 98,7 % après arrondis. L'effet sur le cas standard est faible.
- Correction proposée : ajouter la ligne des autres composites et une note explicite « humidité non mesurée pour la catégorie dangereuse ».

## Autres interprétations

**Lecture favorable.** Les données nationales sont récentes, publiques et cohérentes entre la synthèse ADEME et les jeux ouverts. Les 29 calculs sont exacts. À l'échelle du marché, une machine ne représente qu'environ 1,5 % des OMR franciliennes. Une composition moyenne nationale est donc suffisante pour un premier modèle.

**Lecture prudente.** Une moyenne nationale issue de 95 échantillons ne décrit pas automatiquement un contrat local. L'humidité repose sur 20 échantillons et le PCI sur 15, avec des intervalles larges. Le modèle ne doit donc pas transformer 42,1 % ou 15,79 % en spécifications garanties de matière entrante.

**Lecture retenue.** Pour un cas standard et raisonnable, les valeurs centrales passent. Le point à sécuriser n'est pas le volume national, mais la variabilité du flux réel et la gestion de plus de 6 000 t/an d'inertes ou de refus. Une campagne d'échantillonnage du flux contractuel, des critères d'acceptation et un schéma de prétri suffisent à transformer ce point en condition de projet plutôt qu'en blocage.

## Hypothèses exclues du contrôle chiffré

- **D-046, raccordement des deux jeux MODECOM : raisonnable provisoirement.** Elle est clairement présentée comme hypothèse et évite de mélanger silencieusement les fines. Le rapport technique complet doit confirmer leur allocation.
- **D-043, huile issue des plastiques : hors lot 1.** Elle sera appréciée avec les produits de sortie au lot 3.
- **D-044, rendements appliqués sur matière sèche : raisonnable comme structure de calcul, mais hors lot 1.** Le choix du rendement sera examiné dans les lots 2 et 3.
- **D-045, char de la matière organique : hors lot 1.** Son caractère prudent ou optimiste dépend des sources de rendement du lot 3.
- **D-048, couches et textiles : hors lot 1.** Sa plausibilité sera examinée au lot 2 puis dans le bilan du lot 3.

## Manques évidents pour juger la faisabilité OMR

- **IMPORTANT : performance du prétri.** Taux réel de retrait du verre, des métaux, des minéraux, des piles, des bouteilles de gaz et des DEEE à mesurer sur la ligne choisie.
- **IMPORTANT : exutoire des refus et du résidu minéral.** Environ 6 027 t/an avant concentration éventuelle dans le solide.
- **IMPORTANT : caractérisation contractuelle locale.** Humidité, PCI, chlore, métaux et granulométrie doivent être mesurés sur un échantillonnage représentatif du flux réellement offert.
- **IMPORTANT : sécurité des déchets indésirables.** Piles, bouteilles de gaz, huiles et déchets de soins perforants exigent un protocole d'acceptation et de détection.
- **MINEUR dans ce lot : odeurs et stockage humide.** À documenter dans la conception du stockage, sans effet sur les statistiques de composition.

## Conclusion en langage simple

- **PASSE** pour les tonnages, la composition moyenne, l'humidité centrale et les PCI publiés.
- **PASSE** pour les 29 calculs demandés : aucune erreur arithmétique.
- **POSSIBLE SOUS CONDITIONS** pour l'utilisation de ces valeurs dans le projet : conserver l'incertitude, caractériser le flux local et définir le prétri ainsi que les exutoires.
- **NE PASSE PAS** comme spécification garantie d'entrée : les moyennes nationales ne prouvent pas qu'un lot local aura exactement 42,1 % d'humidité ou 11,79 % d'inertes.
- **Aucun écart bloquant** n'est démontré dans le lot 1.

## Ce qui n'a pas pu être vérifié, et pourquoi

- Le rapport technique MODECOM complet n'a pas été lu : l'accès ADEME passe par un formulaire. Il est nécessaire pour comprendre l'allocation exacte des fines.
- Le comportement exact du verre, des métaux, des minéraux et de chaque sous-catégorie dangereuse dans l'Urban Rig n'est pas documenté dans les sources citées en section 5.4.
- L'efficacité d'une future ligne de prétri n'est pas connue, car aucune ligne n'est encore choisie.
- Les données locales du futur fournisseur ne sont pas disponibles.
- Le contrôle automatique a signalé 53 affirmations « sans source » et 87 erreurs sur le HTML généré. Ce résultat est un défaut de reconnaissance des renvois vers les fiches `preuves/*.html` par le script, pas une absence réelle de tous les liens. Le contrôle manuel ci-dessus a donc été nécessaire. Aucun fichier source n'a été corrigé.

## Décompte

47 verdicts : **42 CONFIRMÉ**, **1 DIFFÉRENT**, **1 ABSENT**, **3 NON SOURCÉ**, **0 CALCUL FAUX**, **0 INACCESSIBLE**.

Écarts : **0 BLOQUANT, 2 IMPORTANT, 3 MINEUR**.

Les 29 calculs demandés sont tous exacts. Les 44 verdicts assortis d'une citation exacte sont ajoutés au registre ; les trois verdicts NON SOURCÉ n'y sont pas inscrits, conformément à la règle du registre.
