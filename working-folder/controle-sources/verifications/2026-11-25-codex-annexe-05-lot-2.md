Accès internet : OUI

Lecture des PDF : OUI. Les rapports et articles accessibles ont été ouverts dans leur version d'origine. Pour McNeill 1990 et les deux études sur couches signalées « abstract only » par l'annexe, le contrôle est limité au résumé de l'éditeur ou à PubMed, comme l'indique le HTML.

## Périmètre et question de décision

Lot 2 de l'annexe 5, sections 5.5 à 5.8 : textiles sanitaires et couches, textiles, composites, plastiques, PVC et bilan d'une tonne. Les calculs `CALC-A5-EAU-KG-T`, `CALC-A5-SEC-*`, `CALC-A5-PLAST-*`, `CALC-A5-COUCHE-*` et `CALC-A5-PVC-*` ont été refaits sans changer les hypothèses.

Question pratique : les fractions supplémentaires et le bilan massique modifient-ils la faisabilité d'une machine de 51 100 t/an, ou révèlent-ils un manque évident avant essai sur OMR ?

## Sources d'origine ouvertes

- Environment Agency, *An updated lifecycle assessment study for disposable and reusable nappies*, 2008, tableau 1.2, p. 4.
- Mahon et al., *Applications of super absorbent polymers in sustainable agriculture*, 2020, section 3.3 et figure 8b.
- Grabowska et al., étude TG-FTIR du liant polyacrylate de sodium/dextrine, 2013, tableau 2 et section 4.
- Bhatt et al., *RSC Advances* 16, 2026, résumé, section 2.5 et section 3.3.
- McNeill et Sadeghi, étude de la dégradation des polyacrylates, 1990, résumé de l'éditeur.
- Lam et al., *Chemosphere*, 2019, résumé PubMed.
- Calero et al., *Chemical Engineering Journal*, 2025, résumé et points forts de l'éditeur.
- Malsegna et al., *Energies* 14(9):2399, 2021, tableau 3 et section 3.
- ADEME, jeux MODECOM composition, grille et humidité, copies CSV d'origine du dépôt.
- CIAAW, *Standard Atomic Weights 2024*.
- Arrêté français du 19 février 2024 sur la sortie du statut de déchet des huiles de pyrolyse, version Légifrance.

## Tableau des verdicts

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---|---|---|---|---|---|---|---|---|
| 1 | 5.5 | Textiles sanitaires | 16,99 % | CALC-A5-CAT06-PCT | CONFIRMÉ | `859 734 + 380 662 + 1 265 338 = 2 505 734` ; `2 505 734 / 14 752 013 = 16,9857 %` | CSV composition, lignes 06.01 à 06.03 | Recalcul exact, déjà convergent avec le lot 1. |
| 2 | 5.5 | Papier souillé | 1 265 338 t ; 8,6 % ; 19,2 kg/hab | ADEME-MODECOM-2024-DATA ; RP2-004 | CONFIRMÉ | « Textiles sanitaires 38 kg/hab, dont papiers souillés 19,2 » ; CSV : `06.03`, 1 265 338 t, 8,6 %, 19,17 kg/hab | MODECOM, p. 21-22 ; CSV composition, 06.03 | Le ratio est correctement arrondi. |
| 3 | 5.5 | Couches bébé | 859 734 t ; 5,8 % ; 13,0 kg/hab | ADEME-MODECOM-2024-DATA ; RP2-004 | CONFIRMÉ | « couches bébé 13,0 » ; CSV : `06.01`, 859 734 t, 5,8 %, 13,03 kg/hab | MODECOM, p. 21-22 ; CSV composition, 06.01 | Même périmètre et même année. |
| 4 | 5.5 | Autres produits d'hygiène | 380 662 t ; 2,6 % ; 5,8 kg/hab | ADEME-MODECOM-2024-DATA ; RP2-004 | CONFIRMÉ | « autres déchets hygiéniques 5,8 kg/hab » ; CSV : `06.02`, 380 662 t, 2,6 %, 5,77 kg/hab | MODECOM, p. 21-22 ; CSV composition, 06.02 | Même périmètre et même année. |
| 5 | 5.5 | Humidité et PCI des textiles sanitaires | 60,0 % ; 18 040 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S08,17,0%,60,0%` ; « Textiles sanitaires, PCI moyen en 2024 18 040 » | CSV humidité, S08 ; MODECOM, tableau 2 p. 23 | Valeurs exactes. |
| 6 | 5.5 | Composition d'une couche neuve britannique | 38,6 g ; 34,1 % fluff ; 32,4 % SAP ; 16,6 % PP ; 6,0 % LDPE ; 3,8 % adhésifs ; 2,2 % PET/polyester ; 4,8 % autres | A5-EA-2008-NAPPY-LCA | CONFIRMÉ | « Total 38.6 g ; Fluff pulp 34.1% ; SAP 32.4% ; PP 16.6% ; LDPE 6.0% ; Adhesives 3.8% ; PET/polyester 2.2% ; Other 4.8% » | Rapport, tableau 1.2, p. 4 | Source ancienne et couche neuve britannique, limites correctement dites dans le texte. |
| 7 | 5.C.ar | Polymères classiques dans la couche | 24,8 % | CALC-A5-COUCHE-POLYMERES-PCT | CONFIRMÉ | « PP 16.6% ; LDPE 6.0% ; PET/polyester 2.2% » | Rapport, tableau 1.2, p. 4 | 16,6 + 6,0 + 2,2 = 24,8 %. |
| 8 | 5.5.1 | Zones de chauffe URC-2000 | 150, 300, 450 et 600 °C | UR2000-JP-P08-SPEC | CONFIRMÉ | « 150°C ; 300°C ; 450°C ; 600°C » | Annexe 2, fiche 2.3.b | Valeur reprise identique, nature constructeur. |
| 9 | 5.5.1 | Perte d'eau liée du SAP | 14 % sous 360 °C | A5-MAHON-2020-SNAS-SAP | CONFIRMÉ | « The first stage of decomposition is associated with the loss of water adsorbed on the surface of the particles. » | Section 3.3, figure 8b ; étape 25 à 360 °C | La valeur 14 % est lue dans la courbe et le bilan de masse de l'article. |
| 10 | 5.5.1 | Dévolatilisation principale | 230 à 550 °C | A5-BHATT-2026-RSCADV | CONFIRMÉ | « Thermogravimetric analysis revealed primary devolatilization between 230–550 °C » | Résumé | Essais différents de l'Urban Rig, mais valeur correctement attribuée à la littérature. |
| 11 | 5.5.1 | Dégradation du polyacrylate | stable jusqu'à environ 400 °C ; pertes principales 360 à 592 °C ; gaz entre 300 et 500 °C | A5-MCNEILL-1990-PAANA ; A5-MAHON-2020-SNAS-SAP ; A5-GRABOWSKA-2013-PAANA | CONFIRMÉ | « These materials are stable up to about 400°C » ; étapes 360 à 477 et 477 à 592 °C ; « CO2, H2O, CO and methane between 300 and 500 C » | Résumé McNeill ; Mahon section 3.3 ; Grabowska section 4 | Les conditions diffèrent entre vide, azote et composite avec dextrine. Le texte ne les présente pas comme un essai Urban Rig. |
| 12 | 5.5.1 | Résidu du liant et du polyacrylate | 11,3 % à 1 000 °C ; 40 % à 800 °C | A5-GRABOWSKA-2013-PAANA ; A5-MAHON-2020-SNAS-SAP | CONFIRMÉ | « probably mainly contains carbonised carbon » ; « residue 11.3 % at 1000 C » ; « residue at 800 C 40 % » | Grabowska, tableau 2 et section 6 ; Mahon, figure 8b | Le premier matériau est un composite polyacrylate/dextrine, ce que l'annexe appelle correctement un liant. |
| 13 | 5.5.1 | Pyrolyse micro-ondes de couches usagées | jusqu'à 43 % huile, 29 % gaz, 28 % char | A5-LAM-2019-CHEMOSPHERE-DIAPER | CONFIRMÉ | « up to 43 wt% production of liquid oil, 29 wt% gases and 28 wt% char product » | Résumé PubMed | Résumé uniquement. Les trois « up to » ne doivent pas servir comme bilan de rendement Urban Rig. |
| 14 | 5.5.1 | Pyrolyse Calero | 575 °C ; 23 mmol/g ; plus de 63 % ; 525 °C ; 9,7 m2/g | A5-CALERO-2025-CEJ-DIAPER | CONFIRMÉ | « hydrogen and methane production is maximized at 575 °C » ; « The temperature of 525 °C optimized the production of lighter liquid fractions » | Résumé et points forts de l'éditeur | Les autres valeurs figurent dans le même résumé. Résumé uniquement. |
| 15 | 5.5.1 | Analyses immédiates des couches | 7,5 % cendres et 3,9 % carbone fixe ; 10,7 % et 1,2 % | A5-MALSEGNA-2021-ENERGIES-AHP | CONFIRMÉ | « Ashes 7.5 10.7 ; Volatile matter 82.8 81.5 ; Fixed carbon 3.9 1.2 » | Tableau 3 | Le second matériau est seulement la fraction cellulosique de couches usagées stérilisées. |
| 16 | 5.5.1 | Sodium et cendres fusibles | 2 à 3 % Na ; 500 à 800 °C ; agglomération observée | A5-MALSEGNA-2021-ENERGIES-AHP | CONFIRMÉ | « Na content in AHPam was in the range of 2–3 wt% » ; « can lead to the formation of eutectics [...] low-melting ashes » | Section 3 et analyse ICP-AES | L'agglomération concerne le sable d'un lit fluidisé expérimental, pas l'Urban Rig. |
| 17 | 5.5.1 | Dépôts collants Urban Rig et baisse de valeur du char | effet possible, non mesuré | aucune source directe | NON SOURCÉ | « agglomeration of the sand bed occurred » | Malsegna 2021, lit fluidisé | La source prouve un mécanisme et une agglomération dans un autre réacteur, pas des dépôts Urban Rig ni le PCI ou la valeur commerciale du char. Le conditionnel et R-021 évitent une conclusion fausse. |
| 18 | 5.6 | Textiles et habillement | 4,87 % ; 443 844 t | CALC-A5-CAT05-PCT ; ADEME-MODECOM-2024-DATA | CONFIRMÉ | CSV : `05.02`, 443 844 t ; total catégorie 718 435 t | CSV composition, lignes 05.01 à 05.07 | 718 435 / 14 752 013 = 4,8701 %. |
| 19 | 5.6 | Composites | 2,00 % ; 131 937 ; 78 114 ; 64 087 t | CALC-A5-CAT04-PCT ; ADEME-MODECOM-2024-DATA | CONFIRMÉ | CSV : `04.03` 131 937 ; `04.01` 78 114 ; `04.02` 64 087 | CSV composition, lignes 04.01 à 04.05 | Total 294 383 t, soit 1,9955 %. |
| 20 | 5.6 | Autres matières organiques | 1,54 % ; 227 604 t | CALC-A5-CAT11-PCT ; ADEME-MODECOM-2024-DATA | CONFIRMÉ | CSV : `11.01`, 227 604 t | CSV composition, 11.01 | 227 604 / 14 752 013 = 1,5429 %. |
| 21 | 5.6 | Fines | 5,4 % ; PCI 9 819 J/gMS | ADEME-MODECOM-2024-HUM ; RP2-004 | CONFIRMÉ | `S18,14.02,5,4%,46,3%` ; « Eléments fins < 8mm, PCI moyen en 2024 9 819 » | CSV humidité, S18 ; MODECOM tableau 2 p. 23 | Le terme « surtout putrescible » est également présent en note 16. |
| 22 | 5.C.as | Plastiques souples | 1 281 445 t | CALC-A5-PLAST-SOUPLES-T | CONFIRMÉ | `07.01` 496 503 ; `07.02` 165 000 ; `07.03` 619 942 | CSV composition | Somme indépendante exacte. |
| 23 | 5.C.at | Plastiques rigides et autres | 1 047 813 t | CALC-A5-PLAST-RIGIDES-T | CONFIRMÉ | `07.04` à `07.14` : 160 966 ; 51 533 ; 23 899 ; 44 178 ; 443 885 ; 5 461 ; 40 401 ; 40 123 ; 14 665 ; 5 254 ; 217 448 | CSV composition | Somme indépendante exacte. |
| 24 | 5.7 | Pots, barquettes, gobelets | 443 885 t | ADEME-MODECOM-2024-DATA | CONFIRMÉ | CSV : `07.08`, 443 885 t | CSV composition, 07.08 | Valeur exacte. |
| 25 | 5.7 | Autres plastiques | 217 448 t | ADEME-MODECOM-2024-DATA | CONFIRMÉ | CSV : `07.14`, 217 448 t | CSV composition, 07.14 | La grille inclut notamment tuyaux, panneaux PVC et films étirables. |
| 26 | 5.C.au | Bouteilles PET | 212 499 t | CALC-A5-PLAST-PET-T | CONFIRMÉ | `160 966 + 51 533` | CSV composition, 07.04 et 07.05 | Somme indépendante exacte. |
| 27 | 5.C.av | Bouteilles polyoléfines | 68 077 t | CALC-A5-PLAST-PO-T | CONFIRMÉ | `23 899 + 44 178` | CSV composition, 07.06 et 07.07 | Somme indépendante exacte. |
| 28 | 5.7 | Total plastiques | 2 329 258 t | CALC-A5-CAT07-T | CONFIRMÉ | CSV, somme des lignes `07.01` à `07.14` = 2 329 258 | CSV composition | Les sous-totaux souples et rigides totalisent aussi 2 329 258 t. |
| 29 | 5.7 | Grille par usage, non par polymère | sauf PET et polyoléfines des bouteilles | RP2-002 | CONFIRMÉ | « 07.04 Bouteilles et flacons en PET clair ; 07.06 Bouteilles et flacons en PE ; 07.07 Bouteilles et flacons en PP » | Grille MODECOM 2024, catégorie 07 | L'absence d'une ventilation polymère globale est correctement signalée. |
| 30 | 5.7 | Sous-catégories contenant du PVC | 07.09 : 5 461 t ; 07.14 : 217 448 t | ADEME-MODECOM-2024-DATA ; RP2-002 | CONFIRMÉ | « 07.09 Autres bouteilles, flacons, bonbonnes en PVC, PAN et autres résines » ; « 07.14 autres plastiques (tuyaux, panneaux PVC...) » | CSV composition et grille MODECOM | Les tonnages ne sont pas des tonnages de PVC pur, et l'annexe ne les présente pas ainsi. |
| 31 | 5.C.aw | Chlore dans le PVC, borne basse | 56,7195 % | CALC-A5-PVC-CL-MIN | CONFIRMÉ | « Hydrogen [1.00784, 1.00811] ; Carbon [12.0096, 12.0116] ; Chlorine [35.446, 35.457] » | CIAAW, tableau 2024 | 35,446 / (2 x 12,0116 + 3 x 1,00811 + 35,446) = 56,71947 %. |
| 32 | 5.C.ax | Chlore dans le PVC, borne haute | 56,7315 % | CALC-A5-PVC-CL-MAX | CONFIRMÉ | Même citation CIAAW | CIAAW, tableau 2024 | Résultat indépendant 56,73145 %. |
| 33 | 5.7 | Analyse du chlore des OMR | non trouvée | MODECOM 2024 | ABSENT | Le jeu de composition contient `pourcentage_OMR`, `ratio_OMR`, `tonnage_OMR` ; le jeu d'humidité contient `pourcentage_OMR`, `humidite_OMR`, `IC` | CSV MODECOM composition et humidité | Aucun champ ni résultat d'analyse du chlore. L'absence est importante, mais ne démontre pas une non-conformité. |
| 34 | 5.7 | Chlore dans les huiles municipales de Chiba | 0,137 % et 0,526 % masse | CHIBA-JLOS-HUILES | CONFIRMÉ | « 塩素分 質量% 0.137 » ; second bulletin : `0.526` | Annexe 2, fiche 2.2.a, ligne chlore | Valeurs reprises identiques. La méthode n'est pas indiquée sur les bulletins. |
| 35 | 5.7 | Sortie du statut de déchet | code OMR 20 03 01 absent | A3-ARRETE-SSD-HUILE-PYROLYSE-2024 | CONFIRMÉ | « est au moins de 85 % en masse de matière sèche » ; liste fermée comprenant notamment 20 01 39, sans 20 03 01 | Arrêté du 19 février 2024, annexe I, section 1.1 | L'huile issue d'OMR ne bénéficie pas de cette voie de sortie de statut de déchet. Le texte de l'annexe est juste. |
| 36 | 5.C.c | Eau par tonne | 421,298 kg/t | CALC-A5-EAU-KG-T | CONFIRMÉ | `S01 3,0 %, 59,7 % ... S18 5,4 %, 46,3 % ; moyenne 42,1 %` | CSV humidité, 17 fractions | Somme pondérée indépendante : 421,298 kg/t. |
| 37 | 5.C.e | Plastique sec | 111,142 kg/t | CALC-A5-SEC-PLAST-KG-T | CONFIRMÉ | `S09,8,6%,35,8%` ; `S10,7,0%,20,1%` | CSV humidité, S09-S10 | 8,6 x 64,2 / 10 + 7,0 x 79,9 / 10 = 111,142. |
| 38 | 5.C.ay | Masse sèche dite organique non plastique | 363,770 kg/t | CALC-A5-SEC-ORG-KG-T | CONFIRMÉ | Parts et humidités S01-S08, S11-S12, S15 et S18 | CSV humidité | Arithmétique exacte. L'intitulé est trop fort : les textiles, composites, couches et fines ne sont pas chimiquement séparés. E-1. |
| 39 | 5.C.az | Masse sèche inerte | 91,790 kg/t | CALC-A5-SEC-INERTE-KG-T | CONFIRMÉ | `S13,4,7%,2,2% ; S14,3,3%,13,2% ; S17,2,0%,14,1%` | CSV humidité, S13-S14-S17 | Somme indépendante exacte. |
| 40 | 5.8 | Couverture du bilan d'une tonne | 98,8 % ; 12 kg non décrits | ADEME-MODECOM-2024-HUM | CONFIRMÉ | « Somme des parts : 98,8 % (pas de ligne pour les déchets dangereux) » | CSV humidité | 421,298 + 111,142 + 363,770 + 91,790 = 988,000 kg. L'écart est expliqué, pas une erreur de conservation de masse. |
| 41 | 5.C, couches | PP + PE dans une couche neuve | 22,6 % | CALC-A5-COUCHE-PPPE-PCT | CONFIRMÉ | « PP 16.6% ; LDPE 6.0% » | Rapport EA, tableau 1.2 p. 4 | 16,6 + 6,0 = 22,6 %. |
| 42 | 5.C, matière sèche | Textiles sanitaires secs | 68,000 kg/t | CALC-A5-SEC-SANIT-KG-T | CONFIRMÉ | `S08,17,0%,60,0%` | CSV humidité, S08 | 17,0 x 40,0 / 10 = 68,0. |
| 43 | 5.C, matière sèche | Couches et hygiène sèches | 33,6614 kg/t | CALC-A5-SEC-COUCHES-KG-T | CONFIRMÉ | `06.01 859 734 ; 06.02 380 662 ; total catégorie 2 505 734` | CSV composition ; calculs.yaml | Formule déclarée avec l'intermédiaire arrondi 49,502 % : 68 x 49,502 % = 33,66136. Avec les tonnages non arrondis : 33,66157. Écart négligeable de 0,0002 kg/t. |
| 44 | 5.C, matière sèche | PP et PE des couches et produits d'hygiène | 7,6075 kg/t | CALC-A5-SEC-POLY-COUCHES-KG-T | CONFIRMÉ | « PP 16.6% ; LDPE 6.0% » | Rapport EA, tableau 1.2 ; calculs.yaml | 33,6614 x 22,6 % = 7,6075. Hypothèse d'application discutée sous D-048. |
| 45 | 5.C, matière sèche | Textiles secs | 32,487 kg/t | CALC-A5-SEC-TEXT-KG-T | CONFIRMÉ | `S07,4,9%,33,7%` | CSV humidité, S07 | 4,9 x 66,3 / 10 = 32,487. |
| 46 | 5.C, matière sèche | Textiles sanitaires hors PP/PE plus textiles | 92,8795 kg/t | CALC-A5-SEC-CELLU-ST-KG-T | CONFIRMÉ | `68,0 - 7,6075 + 32,487` | calculs.yaml et entrées ci-dessus | Arithmétique exacte. « CELLU » ne signifie pas cellulose pure : SAP, adhésifs et fibres synthétiques subsistent. |
| 47 | 5.C, matière sèche | Organique hors PP/PE des couches | 356,1625 kg/t | CALC-A5-SEC-ORG2-KG-T | CONFIRMÉ | `363,770 - 7,6075` | calculs.yaml et entrées ci-dessus | Arithmétique exacte. Même réserve de périmètre que la ligne 38. |

## Décompte

- CONFIRMÉ : 45
- ABSENT : 1
- NON SOURCÉ : 1
- DIFFÉRENT : 0
- INACCESSIBLE : 0
- CALCUL FAUX : 0
- Total : 47 verdicts
- Calculs demandés refaits : 18 sur 18, tous conformes à leurs formules déclarées

Le contrôle automatique a trouvé 53 affirmations chiffrées mais les a toutes marquées « sans source » parce qu'il ne reconnaît pas les liens de preuve du HTML généré. Ses 87 erreurs sont donc des faux positifs structurels, pas un résultat de contrôle exploitable pour ce lot.

## Écarts

### E-1. « Masse sèche organique non plastique » n'est pas une caractérisation chimique

- Annexe : section 5.8 et calculs `SEC-ORG`, `SEC-CELLU-ST`, `SEC-ORG2`.
- Source : MODECOM fournit des catégories d'usage, pas une séparation chimique.
- Gravité : IMPORTANT.
- Effet : les 363,77 kg/t comprennent encore le SAP et les adhésifs des couches, les fibres synthétiques inconnues des textiles, les couches polymères des composites et la part minérale des fines. Seuls 7,61 kg/t de PP/PE de couches sont ensuite retirés. Cela peut déplacer les rendements huile, gaz et char du lot 3.
- Correction proposée : renommer la ligne « matière sèche des fractions non inertes classées hors plastiques » et présenter séparément la correction polymère connue et la part polymère encore inconnue. Ne pas décrire 356,16 kg/t comme une masse organique chimiquement non plastique.

### E-2. Chlore réel des OMR et de l'huile non mesuré

- Annexe : section 5.7.
- Sources : MODECOM ne donne pas le chlore ; Chiba mesure 0,137 % et 0,526 % dans deux huiles municipales différentes.
- Gravité : IMPORTANT.
- Effet : le risque HCl, corrosion, traitement des gaz et spécification de l'huile ne peut pas être conclu. À 51 100 t/an, l'installation ne dépend que d'environ 1,5 % du gisement régional, donc un cahier des charges d'approvisionnement ou un pré-tri pourrait réduire le risque, mais son efficacité doit être mesurée.
- Correction proposée : analyse halogènes du flux entrant et de chaque phase de sortie lors d'un essai OMR représentatif, avec bilan massique du chlore. L'absence ne prouve pas une non-conformité.

### E-3. Extrapolation sodium vers l'Urban Rig

- Annexe : section 5.5.1.
- Source : Malsegna observe une agglomération du sable dans un lit fluidisé avec 2 à 3 % de sodium dans les couches neuves.
- Gravité : MINEUR dans la rédaction actuelle.
- Effet : les dépôts collants Urban Rig et la baisse de valeur du char restent possibles, mais non démontrés. Le texte emploie « could » et demande l'essai R-021, donc il ne transforme pas le risque en fait.
- Correction proposée : écrire explicitement « extrapolation d'un lit fluidisé, non observée sur Urban Rig ».

### E-4. Arrondi intermédiaire dans `SEC-COUCHES`

- Annexe : calcul `CALC-A5-SEC-COUCHES-KG-T`.
- Gravité : MINEUR.
- Effet : 33,6614 kg/t avec la part arrondie, contre 33,6616 kg/t à partir des tonnages bruts, soit environ 0,01 t/an à 51 100 t/an. Aucun effet décisionnel.
- Correction proposée : conserver les dépendances non arrondies dans le moteur de calcul.

## Hypothèses D-043 à D-048

| Décision | Étiquetage | Appréciation en cas standard |
|---|---|---|
| D-043 | Clairement « HYPOTHESE » dans `_decisions.yaml`, mais remplacée par D-047 | Prudente car elle excluait les polymères hors catégorie 07 ; elle n'est plus la règle active. |
| D-044 | Clairement « Working assumption » dans la fiche D | La borne 55 % paraît prudente ; 73,07 % au standard paraît plutôt optimiste pour des plastiques OMR sales et mélangés, car elle vient d'essais de plastiques propres. À confirmer par essai. |
| D-045 | Clairement « Working assumption » | Fourchette 25 à 40 % et centre 30 % raisonnables comme ordre de grandeur, convergents avec les essais alimentaires, papier et textiles cités, mais non validés sur Urban Rig. |
| D-046 | Clairement « Working assumption » | Raisonnable pour rapprocher composition et humidité ; la répartition des fines doit rester visible. Le bilan ferme correctement à 98,8 %, pas artificiellement à 100 %. |
| D-047 | Clairement « Decision of the project sponsor » | Décision de présentation, pas mesure. Les trois scénarios sont appropriés tant que le scénario standard n'est pas présenté comme mesuré. |
| D-048 | Clairement « Working assumption » | Trop incertaine pour être dite représentative : composition d'une couche neuve britannique de 2006 étendue aux couches usagées et aux autres produits d'hygiène, humidité supposée identique. Son effet PP/PE reste limité à 7,61 kg/t, soit environ 389 t/an d'entrée à l'échelle de la machine. |

## Autres interprétations

1. Le bilan à 988 kg n'est pas un calcul faux. Il décrit 98,8 % de la tonne, proportion exactement couverte par le jeu d'humidité. Les 12 kg manquants correspondent à la catégorie dangereuse ou spécifique sans humidité. Une fermeture forcée à 1 000 kg serait moins rigoureuse.
2. La littérature sur les couches converge sur la décomposition thermique, la production de gaz/liquide/char et la présence de sodium. Elle ne prouve pas un rendement Urban Rig, car les dispositifs vont de l'ATG au micro-ondes et au lit fluidisé.
3. Les rendements « jusqu'à 43 %, 29 %, 28 % » de Lam sont des maxima de résumé. Ils ne doivent pas être injectés comme un bilan unique dans le modèle, ce que l'annexe ne fait pas.
4. Le fait que l'huile d'OMR reste un déchet est confirmé juridiquement. Cela n'interdit pas toute utilisation comme combustible sous statut de déchet, mais ne démontre ni débouché commercial ni conformité à une installation utilisatrice. Ce point relève du lot 3.

## Cinq points les plus graves

1. Chlore et halogènes réels du flux et de l'huile inconnus : mesure indispensable avant conclusion technique.
2. Les 363,77 puis 356,16 kg/t dits « organiques non plastiques » ne sont pas une séparation chimique et peuvent déplacer les rendements du modèle.
3. D-048 extrapole une couche neuve britannique de 2006 à plusieurs produits usagés ; l'effet quantifié reste toutefois petit à l'échelle de la tonne.
4. Le sodium des couches est un risque expérimental crédible, mais son comportement dans l'Urban Rig n'est pas mesuré.
5. L'huile d'OMR ne peut pas utiliser la voie française de sortie de statut de déchet vérifiée ; le débouché sous statut de déchet reste à démontrer.

## Ce qui n'a pas pu être vérifié

- Composition récente et européenne des couches : non trouvée par le projet, recherche exhaustive non répétée dans ce lot.
- Humidité propre aux couches usagées et à chaque produit d'hygiène : aucune mesure séparée dans MODECOM.
- Ventilation coton, synthétiques et mélanges des textiles OMR : absente de la grille MODECOM.
- Part réelle de PVC et chlore total des OMR : la grille cite des objets pouvant contenir du PVC mais ne mesure pas le polymère.
- Dépôts, corrosion et répartition du sodium dans l'Urban Rig : aucun essai OMR ou couches Urban Rig.
- Vente ou utilisation effective de l'huile sous statut de déchet : pas de contrat ni d'essai utilisateur dans ce lot.

## Conclusion en langage simple

Le lot 2 passe sous conditions. Les statistiques, les études citées et les 18 calculs demandés sont arithmétiquement conformes. Le bilan d'une tonne est cohérent à 988 kg parce que les données d'humidité ne couvrent que 98,8 % du flux.

Il n'y a pas de blocage démontré. Avant une décision technique, il faut cependant mesurer le chlore et les halogènes sur OMR et huile, puis clarifier la vraie part de polymères dans les textiles, composites et produits sanitaires. Sans ces mesures, le risque est une mauvaise répartition huile/gaz/char, pas une impossibilité déjà prouvée.
