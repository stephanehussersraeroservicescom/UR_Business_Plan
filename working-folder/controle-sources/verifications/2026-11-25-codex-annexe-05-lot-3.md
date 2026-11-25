Accès internet : OUI

Lecture des PDF : OUI. Les sources primaires accessibles, les fiches des annexes 2, 3, 8 et 9, les articles en libre accès et le NIST Chemistry WebBook ont été ouverts. Les prix et hypothèses D-xxx n'ont pas été recherchés à nouveau, conformément aux règles de vérification légère.

## Périmètre et question de décision

Lot 3, sections 5.9 à 5.17 et « Key Messages ». Les 34 calculs demandés des familles `CALC-A5-HUILE-*`, `GAZ-*`, `CHAR*`, `LIQ-*`, `LATENT-MJ-KG`, `EAU-MJ-T` et `COUV-*` ont été refaits. Le calcul auxiliaire du PCS du char alimentaire a aussi été contrôlé.

Question décisive : dans un cas standard, le gaz du plastique couvre-t-il la chaleur du procédé, et le bilan suffit-il pour conclure à la faisabilité sur 51 100 t/an d'OMR ?

## Sources d'origine ouvertes

- Rapport Chiba 2022 et fiches de calcul de l'annexe 2, essais de plastiques propres et de deux flux municipaux riches en plastiques.
- Brochures OneWorld URC-2000, p. 5 et fiche technique p. 4 et 8.
- Bhatt et al., *RSC Advances* 16, 2026, résumé, sections 2.5 et 3.3, tableau 3.
- Khan et al., *Polymers* 14(4):821, 2022, figure 1 et tableau 1.
- Jia et al., *Polymers* 12(3):705, 2020, figure 3 et tableau 1.
- Czajczyńska et al., *Energy Procedia* 123, 2017, tableau 1, source secondaire.
- Sørum et al., SINTEF, 2001, tableau 8.
- NIST Chemistry WebBook, eau : masse molaire 18,0153 g/mol ; enthalpies standard de formation liquide et gaz.
- Malsegna et al., *Energies* 14(9):2399, 2021, tableau 3 et tableau A1.
- Documentation commerciale OREX et Anaergia, étude Torretta et al. 2014, revue Velis et al. 2009.

## Tableau des verdicts

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---|---|---|---|---|---|---|---|---|
| 1 | Key Messages | Tonnage national attribué à 2024 | 14 752 013 t ; 223,46 kg/hab ; 2024 | RP2-004 | DIFFÉRENT | « Tonnage 2023 14 752 013 ; Ratio 2023 223,46 » | MODECOM 2024, tableau 6 p. 39 | Écart déjà trouvé au lot 1 : valeurs exactes, mais année de collecte 2023. |
| 2 | 5.9 | Rendements d'huile PE, PP, PS | PE 74 à 81 % ; PP 73 à 81 % ; PS 55 à 73 % | CHIBA-ESSAIS-FICHES | CONFIRMÉ | PE : 14,8/20, 30,7/40, 40,7/50 ; PP : 16,2/20, 39,8/50, 36,5/50 ; PS : 36,3/50, 12,2/20, 22,0/40 | Rapport Chiba, fiches p. 19 à 23 | Valeurs reprises identiques de l'annexe 2. |
| 3 | 5.9 | Moyenne pondérée des dix essais | 73,07 % | CALC-A2-HUILE10-MOY-POND | CONFIRMÉ | `292,3 kg / 400 kg = 73,075 %` | Annexe 2, fiche 2.5.f.7 | 73,07 % est la valeur enregistrée, mais l'arrondi usuel à deux décimales serait 73,08 %. Effet négligeable. |
| 4 | 5.9 | Deux flux municipaux, hors métaux | 44,6 % et 50,4 % | CALC-A2-HUILE-NODA-0909/0915-HORSMETAUX | CONFIRMÉ | `16,1 / (50 - 13,9) = 0,446` ; `22,5 / (50 - 5,4) = 0,5045` | Annexe 2, fiches 2.5.b.8 et 2.5.b.10 | Ce ne sont pas des OMR brutes. |
| 5 | 5.9 | Deux flux municipaux, entrée brute | 32,2 % et 45,0 % | CALC-A2-HUILE-NODA-0909/0915-BRUT | CONFIRMÉ | `16,1 / 50 = 0,322` ; `22,5 / 50 = 0,45` | Annexe 2, fiches 2.5.b.7 et 2.5.b.9 | Valeurs exactes. |
| 6 | 5.9 | Bilan OneWorld OMR à 10 % de résines | 25 % char ; 5 % huile ; 5 % gaz | UR2000-JP-P05-BILAN | CONFIRMÉ | « 炭化物 25% ; 混合油 5% ; OFF ガス 5% ; 樹脂系類含有率 10% で試算 » | Brochure OneWorld, p. 5 | `nature: constructeur`. Aucun rapport de mesure joint. |
| 7 | 5.9 | Part non allouée du bilan OneWorld | environ 60 à 65 % | UR2000-JP-P05-BILAN | CONFIRMÉ | « char 25 % ; oil 5 % ; off-gas 5 % ; metals and glass 0 to 5 % » | Brochure OneWorld, p. 5 | 100 moins 35 à 40 = 60 à 65 %. |
| 8 | 5.10 | Papier et textiles | liquide 20 à 25 % ; gaz 45 à 48 % ; char 28 à 32 % | A5-BHATT-2026-RSCADV | CONFIRMÉ | « Waste paper and textile wastes exhibit [...] oil yields (20–25 wt%) and higher char (28–32 wt%). The gas yield [...] (45–48 wt%) » | Section 3.3 | Essais à 500 °C, four rotatif de 2 kg. |
| 9 | 5.10 | Plastiques mélangés | liquide 40 à 45 % ; char 5 à 7 % | A5-BHATT-2026-RSCADV | CONFIRMÉ | « pure plastics [...] oil content (40–45 wt%) and [...] char content (5–7 wt%) » | Section 3.3 | Le résumé de l'article donne ailleurs 16 % de char, conflit correctement signalé en 5.14. |
| 10 | 5.10 | Char de déchets alimentaires | 28,45 % à 500 °C | A5-KHAN-2022-POLYMERS-FOOD | CONFIRMÉ | « mass yield [...] after PY (28.45 to 26.67%) [...] from 500 to 700 °C » | Figure 1 et résultats | Mélange simulé de lentilles et pois chiches. |
| 11 | 5.10 | PET sans catalyseur | cires 59,50 et 67,70 % ; gaz environ 20 % | A5-JIA-2020-POLYMERS-PET | CONFIRMÉ | « waxy products [...] about 59.50 wt % and 67.70 wt % » ; « yield of gases increased from about 20 wt % » | Figure 3 | Conditions laboratoire à 450 et 600 °C. |
| 12 | 5.10 | Valeurs de la revue sur cinq matières | nourriture 46/29/25 ; bois 45,0/24,7/27,6 et 55,9/19,9/26,2 ; papier 19/41/40 ; coton 14,00/60,35/25,26 ; OMR 48/34/18 | A5-CZAJCZYNSKA-2017-REVIEW | CONFIRMÉ | « Slow pyrolysis produced approximately 48 wt. % of liquid ; about 18 wt. % of solid residue and 34 wt. % of gas » | Tableau 1 | Source secondaire, valeurs reprises d'études hétérogènes. |
| 13 | 5.10 | Eau dans le liquide | papier 8,01 % ; plastiques 1,22 % | A5-BHATT-2026-RSCADV | CONFIRMÉ | « paper 8.01 % ; textile 3.21 % ; plastics 1.22 % » | Tableau 3 | Confirme que le liquide du papier n'est pas équivalent à l'huile de plastiques. |
| 14 | 5.10 | Carbone fixe des polymères | PE et PP 0 % ; PS 0,2 % ; PVC 4,5 à 4,8 % | A5-SORUM-2001-SINTEF | CONFIRMÉ | « PVC: UPVC [...] fixed carbon 4.8 ; PPVC [...] 4.5 » ; tableau : HDPE, LDPE et PP 0 ; PS 0,2 | Tableau 8 | Valeurs exactes. |
| 15 | 5.C.ba | PCS du char alimentaire | 5 864 kcal/kg = 24,5514 MJ/kg | A5-KHAN-2022-POLYMERS-FOOD ; NIST-SP811-B9 | CONFIRMÉ | « HHV (kcal/kg) [...] PY500 5864.00 » | Khan, tableau 1 | 5 864 x 4,1868 / 1 000 = 24,5514 MJ/kg. |
| 16 | Calculs huile plastique | Bas, centre, haut | 61,1281 ; 81,2115 ; 90,0250 kg/t | CALC-A5-HUILE-BAS/CENT/HAUT-KG-T | CONFIRMÉ | `111,142 x 55 %` ; `111,142 x 73,07 %` ; `111,142 x 81 %` | calculs.yaml | Conformes à l'hypothèse enregistrée D-044. Avec le taux brut 73,075 %, le centre serait 81,2170 kg/t. |
| 17 | Calculs huile couches | Bas, centre, haut | 4,1841 ; 5,5588 ; 6,1621 kg/t | CALC-A5-HUILE-COUCHES-* | CONFIRMÉ | `7,6075 x 55 %` ; `x 73,07 %` ; `x 81 %` | calculs.yaml | Conformes aux entrées enregistrées. |
| 18 | Calculs huile totale, bas et haut | 65,3122 ; 96,1871 kg/t | CALC-A5-HUILE-TOT-BAS/HAUT-KG-T | CONFIRMÉ | `61,1281 + 4,1841` ; `90,0250 + 6,1621` | calculs.yaml | Résultats exacts. |
| 19 | Calcul huile totale, centre | 86,7758 kg/t | CALC-A5-HUILE-TOT-CENT-KG-T | CALCUL FAUX | `81,2115 + 5,5588 = 86,7703` | calculs.yaml | Incohérence de précision. Avec 73,075 % non arrondi, le résultat est 86,7762. L'affichage reste 87 kg/t dans les deux cas ; effet annuel inférieur à 0,3 t. |
| 20 | Calculs liquide textiles | Bas, centre, haut | 18,5759 ; 20,8979 ; 23,2199 kg/t | CALC-A5-LIQ-ST-* | CONFIRMÉ | `92,8795 x 20 %` ; `x 22,5 %` ; `x 25 %` | calculs.yaml | Arithmétique exacte. |
| 21 | Gaz du plastique | 11,1142 kg/t ; 415,6711 MJ/t | CALC-A5-GAZ-PLAST-KG-T ; -MJ-T | CONFIRMÉ | `111,142 x 10 % = 11,1142` ; `11,1142 x 37,4 = 415,6711` | calculs.yaml | Conformes à D-029 et D-038. |
| 22 | Gaz des couches | 0,76075 kg/t | CALC-A5-GAZ-COUCHES-KG-T | CONFIRMÉ | `7,6075 x 10 % = 0,76075` | calculs.yaml | Exact. |
| 23 | Gaz hydrocarboné total | 11,875 kg/t ; 444,125 MJ/t | CALC-A5-GAZ-HC-TOT-KG-T ; -MJ-T | CONFIRMÉ | `11,1142 + 0,76075 = 11,87495` ; `11,875 x 37,4 = 444,125` | calculs.yaml | Arrondis conformes. |
| 24 | Gaz des textiles | Bas, centre, haut | 41,7958 ; 43,1890 ; 44,5822 kg/t | CALC-A5-GAZ-ST-* | CONFIRMÉ | `92,8795 x 45 %` ; `x 46,5 %` ; `x 48 %` | calculs.yaml | Exact aux arrondis indiqués. |
| 25 | Char, ancienne base | Bas, centre, haut | 90,9425 ; 109,131 ; 145,508 kg/t | CALC-A5-CHAR-BAS/CENT/HAUT-KG-T | CONFIRMÉ | `363,770 x 25 %` ; `x 30 %` ; `x 40 %` | calculs.yaml | Calculs devenus secondaires après D-048, mais exacts. |
| 26 | Char, base corrigée couches | Bas, centre, haut | 89,0406 ; 106,8487 ; 142,4650 kg/t | CALC-A5-CHAR2-BAS/CENT/HAUT-KG-T | CONFIRMÉ | `356,1625 x 25 %` ; `x 30 %` ; `x 40 %` | calculs.yaml | Exact aux arrondis indiqués. |
| 27 | Énergie du char, ancienne et nouvelle base | 3 502,01 ; 3 428,78 MJ/t | CALC-A5-CHAR-MJ-T ; CALC-A5-CHAR2-MJ-T | CONFIRMÉ | `109,131 x 32,09` ; `106,8487 x 32,09` | calculs.yaml | Arithmétique exacte, mais 32,09 MJ/kg est l'hypothèse D-038, pas une mesure sur char d'OMR. |
| 28 | 5.C.bn | Chaleur latente de l'eau | 2,4426 MJ/kg | CALC-A5-LATENT-MJ-KG | CONFIRMÉ | NIST : `ΔfH°liquid -285.830 kJ/mol`, `ΔfH°gas -241.826 kJ/mol`, masse molaire `18.0153` | NIST Chemistry WebBook, Water | (285,830 - 241,826) / 18,0153 = 2,44259 MJ/kg. |
| 29 | 5.C.r | Chaleur latente par tonne d'OMR | 1 029,06 MJ/t | CALC-A5-EAU-MJ-T | CONFIRMÉ | `421,298 x 2,4426 = 1 029,0625` | calculs.yaml | C'est un minimum : chauffage de l'eau, vapeur surchauffée et pertes exclus. |
| 30 | Anciens ratios de couverture | 0,4039 de l'eau ; 0,2759 du brûleur | CALC-A5-COUV-GAZ-EAU ; -BRULEUR | CONFIRMÉ | `415,6711 / 1 029,06` ; `415,6711 / 1 506,65` | calculs.yaml | Exact. |
| 31 | Ratios actuels de couverture | 0,4316 de l'eau ; 0,2948 du brûleur | CALC-A5-COUV-GAZHC-EAU ; -BRULEUR | CONFIRMÉ | `444,125 / 1 029,06` ; `444,125 / 1 506,65` | calculs.yaml | Exact. |
| 32 | 5.12 | Besoin du brûleur | 1 506,65 MJ/t | CALC-A2-BRULEUR-MJ-T | CONFIRMÉ | `833 kcal/s x 86 400 s x 4,1868 kJ/kcal / 1 000 / 200 t = 1 506,65 MJ/t` | Annexe 2, fiche 2.5.d.1 | `nature: constructeur` pour 833 kcal/s et 200 t/j. Le périmètre thermique du chiffre n'est pas documenté. |
| 33 | 5.12 | Gaz organique de couches sous azote | CO2 23,5 à 33,3 % ; CO 27,8 à 33,4 % ; H2 7,90 à 10,7 % ; CH4 14,5 à 14,7 % ; autres HC 16,5 à 17,7 % | A5-MALSEGNA-2021-ENERGIES-AHP | CONFIRMÉ | Tableau A1 : `H2 7.90/10.7 ; C3H8 eq. 16.5/17.7 ; CO 27.8/33.4 ; CO2 33.3/23.5 ; CH4 14.5/14.7` | Tableau A1, 500 et 600 °C | Gaz sec hors azote. Il est combustible sauf CO2, mais sa masse et son PCI par tonne Urban Rig sont inconnus. |
| 34 | 5.12 | Oxygène des matières | 48,0 % dans fraction cellulosique de couches ; 49,38 % dans mélange alimentaire | A5-MALSEGNA-2021-ENERGIES-AHP ; A5-KHAN-2022-POLYMERS-FOOD | CONFIRMÉ | « O 48.0 % » ; Khan tableau 1 : « O (%) 49.38 » | Malsegna tableau 3 ; Khan tableau 1 | Valeurs exactes sur base sèche. |
| 35 | 5.11 | Fermeture des trois bilans indicatifs | 739,7 ; 782,7 ; 831,4 kg/t quantifiés | calculs du tableau | CONFIRMÉ | Somme des lignes chiffrées du tableau 5.11 | Recalcul indépendant | Restent non alloués, sur les 988 kg couverts : 248,3 ; 205,3 ; 156,6 kg/t. Le tableau le signale par une ligne INCONNU. |
| 36 | 5.12, Key Messages | Le gaz hydrocarboné ne couvre pas la chaleur | 444 contre 1 029 et 1 507 MJ/t | calculs ci-dessus | CONFIRMÉ | `444 / 1 029 = 0,432` ; `444 / 1 507 = 0,295` | Recalcul indépendant | Conclusion robuste : le gaz du plastique et des couches ne suffit pas. Le besoin total exact reste inconnu. |
| 37 | 5.12 | Le char pourrait combler l'écart | 3 429 MJ/t à 32,09 MJ/kg | D-038 ; CALC-A5-CHAR2-MJ-T | CONFIRMÉ | `106,8487 x 32,09 = 3 428,78` | calculs.yaml | « Could » est justifié. Avec le PCS mesuré du char alimentaire, 24,5514 MJ/kg, le contenu brut serait encore 2 623 MJ/t, avant rendement de combustion. |
| 38 | 5.12.1 | Fraction sèche OREX | 18 à 20 % eau ; 12 à 16 MJ/kg ; 25 % inertes | A9-DBTECH-OREX-MSW | CONFIRMÉ | « humidity: 18-20 % ; low heating value: 12.000–16.000 kJ/kg » | Présentation commerciale, pages OREX | Source commerciale, non indépendante. |
| 39 | 5.12.1 | Pâte humide OREX | 55 à 85 % eau ; 65 à 85 % organique ; 30 à 35 % solides | A9-DBTECH-OREX-MSW | CONFIRMÉ | « Humidity: 55-85 % » | Présentation commerciale, pages fractions | Les trois valeurs figurent dans la même présentation. |
| 40 | 5.12.1 | Presse Anaergia | 9 à 15 t/h ; 120 kW ; 8,0 à 13,3 kWh/t | A9-ANAERGIA-OREX400 ; CALC-A9-OREX-KWH-T-* | CONFIRMÉ | « 120 kW average electric power consumption ; 9 to 15 t/h of material treated » | Fiche produit | 120/15 = 8,0 ; 120/9 = 13,333. |
| 41 | 5.12.1 | Étude de bilan avec presse | 11 kWh/t ; 17 766 contre 14 899 kJ/kg | A9-TORRETTA-2014-WIT | CONFIRMÉ | « separates the stream in two flows: wet and dry fractions » | Tableaux 2 et 3 | Les valeurs sont celles d'un schéma intégré italien, pas d'un essai Urban Rig. |
| 42 | 5.12.1 | Bioséchage | moins de 20 % en 7 à 15 jours ; perte 25 à 30 % | A9-VELIS-2009-BIODRYING | CONFIRMÉ | « moisture contents of <20% w/w ; Commercial process cycles are completed within 7–15 days » | Résumé | Perte de masse eau plus CO2, pas seulement eau. |
| 43 | 5.13 | Prix d'entrée du modèle | 100 EUR/t modifiable | D-039 ; D-042 | CONFIRMÉ | « Gate fee [...] taken at 100 EUR/t by default, a value the operator can change » | Fiche D, décisions du sponsor | Hypothèse clairement étiquetée et exclue de la contre-vérification chiffrée. |
| 44 | 5.14 | Conflits entre sources | six conflits listés | sources citées | CONFIRMÉ | `223,46` contre somme `223,54` ; papier `28–32` contre `30–40` ; plastiques `5–7` contre `16` | Sources et emplacements indiqués en 5.14 | Les contradictions utiles sont visibles, pas dissimulées. |
| 45 | 5.17 | Rendement standard présenté | 87 kg huile ; 107 kg char | CALC-A5-HUILE-TOT-CENT ; CALC-A5-CHAR2-CENT | CONFIRMÉ | résultats non arrondis environ `86,77` et `106,85` kg/t | calculs.yaml | Arrondis corrects malgré l'incohérence de précision de 0,0055 kg/t sur l'huile. |
| 46 | HTML contre source Markdown | Valeurs et conclusions des sections 5.9 à 5.17 | identiques | HTML et ANNEX-05 | CONFIRMÉ | « Energy self-sufficiency is not established on this feed » | Key Messages et section 5.12 des deux versions | Aucun écart HTML/source trouvé dans le périmètre. |

## Décompte

- CONFIRMÉ : 43
- DIFFÉRENT : 1
- CALCUL FAUX : 1
- ABSENT : 0
- INACCESSIBLE : 0
- NON SOURCÉ : 0
- Total : 45 verdicts chiffrés ou factuels, plus 1 contrôle HTML/source
- Calculs demandés refaits : 34 sur 34

## Écarts

### E-1. Le bilan matière standard laisse environ 205 kg/t non quantifiés

- Annexe : section 5.11.
- Gravité : BLOQUANT avant conception finale et décision d'investissement, mais pas preuve d'une impossibilité technique.
- Recalcul : les sorties chiffrées du scénario standard totalisent 782,7 kg/t. Sur les 988 kg couverts par MODECOM, 205,3 kg/t restent dans les gaz et liquides des aliments, déchets verts, papiers, cartons et autres fractions. À 51 100 t/an, cela représente environ 10 490 t/an de produits non quantifiés, plus environ 613 t/an de catégorie dangereuse hors bilan d'humidité.
- Lecture : l'annexe ne cache pas le trou, puisqu'elle écrit INCONNU et ouvre R-021. Mais aucune ligne de traitement, stockage, condensation ou épuration ne peut être dimensionnée à partir de ce bilan.
- Correction proposée : ajouter sous le tableau la somme quantifiée et la masse non allouée de chaque scénario, puis exiger un bilan massique complet lors de l'essai OMR.

### E-2. Le besoin thermique net ne peut pas être calculé

- Annexe : section 5.12 et Key Messages.
- Gravité : IMPORTANT.
- Faits confirmés : le gaz hydrocarboné vaut environ 444 MJ/t ; il ne couvre ni les 1 029 MJ/t de chaleur latente ni les 1 507 MJ/t du brûleur.
- Manques : OneWorld ne précise pas si les 1 507 MJ/t incluent déjà l'évaporation de l'eau ; 1 029 MJ/t exclut la chaleur sensible, la surchauffe de la vapeur et les pertes ; le gaz organique n'est pas quantifié.
- Conclusion corrigée : « Le gaz hydrocarboné seul ne suffit pas. L'autosuffisance totale reste indéterminée ; le modèle prudent doit prévoir une ligne de char, d'huile ou de combustible acheté jusqu'à l'essai. » Dire que l'achat ou la combustion d'un produit est nécessaire dans tous les cas serait trop affirmatif, car le gaz organique peut réduire l'écart.

### E-3. Le PCI du char standard est trop optimiste pour être une valeur de conception

- Annexe : section 5.12, D-038.
- Gravité : IMPORTANT.
- Source réelle : 32,09 MJ/kg est mesuré sur un char d'uréthane, puis appliqué par hypothèse au char d'OMR. Le char alimentaire publié atteint 24,55 MJ/kg PCS ; cendres, verre fin, sodium et minéraux des OMR peuvent encore réduire la valeur utile.
- Effet : à 24,55 MJ/kg, le char standard contient environ 2 623 MJ/t brut, toujours supérieur au seul brûleur de 1 507 MJ/t mais pas nécessairement au besoin combiné après rendement de combustion et pertes.
- Correction proposée : garder 32,09 comme scénario haut, utiliser 24,55 comme comparaison prudente, et ne calculer la chaleur utile qu'après mesure du PCI/PCS, humidité, cendres et rendement du système de combustion.

### E-4. Incohérence de précision du calcul central d'huile

- Annexe : `CALC-A5-HUILE-TOT-CENT-KG-T`.
- Gravité : MINEUR.
- Recalcul : les deux sous-calculs enregistrés donnent 81,2115 + 5,5588 = 86,7703 kg/t, pas 86,7758. Avec le taux amont non arrondi de 73,075 %, le résultat est 86,7762 kg/t.
- Effet : aucun sur l'affichage 87 kg/t ; moins de 0,3 t/an à l'échelle de la machine.
- Correction proposée : une règle unique de précision des dépendances et un arrondi seulement à l'affichage.

### E-5. Année 2023 appelée 2024 dans les Key Messages

- Annexe : premier Key Message.
- Gravité : MINEUR.
- Correction proposée : « caractérisation MODECOM 2024, tonnage et ratio issus de l'Enquête Collecte 2023 ».

## Hypothèses exclues du recalcul de fond

| Hypothèse | Étiquetage | Appréciation en cas standard |
|---|---|---|
| D-029, gaz plastique à 10 % | Clairement HYPOTHÈSE | Prudente par rapport aux bilans par différence des plastiques purs ; non mesurée sur OMR. |
| D-035, 140 t/j soit 51 100 t/an | Clairement HYPOTHÈSE | Cohérente pour mettre les risques à l'échelle, mais différente de la fiche URC-2000 à 200 t/j ; la capacité contractuelle devra trancher. |
| D-038, gaz 37,4 MJ/kg et char OMR 32,09 MJ/kg | Clairement HYPOTHÈSE pour le char | 37,4 MJ/kg est une base plausible pour le gaz hydrocarboné. 32,09 MJ/kg paraît optimiste pour un char d'OMR humide et minéral, car la mesure porte sur l'uréthane. |
| D-039 et D-042, prix d'entrée 100 EUR/t | Clairement modifiable | Non vérifié en chiffres. À confirmer par contrat ou lettre d'intention ; un tarif public ne prouve pas le prix accessible au projet. |
| D-044 à D-048 | Clairement HYPOTHÈSES ou décision du sponsor | Les réserves du lot 2 restent valables. Pour le standard, 73,07 % d'huile sur plastique OMR paraît plutôt optimiste ; le scénario bas est plus prudent avant essai. |

## Autres interprétations

1. La conclusion centrale passe : 444 MJ/t de gaz hydrocarboné ne couvrent pas le besoin thermique. Ce résultat ne dépend pas du petit écart d'arrondi sur l'huile.
2. L'annexe est prudente sur l'autosuffisance, mais le modèle ne doit pas transformer cette prudence en achat certain de combustible. Le gaz des matières organiques contient CO, H2, CH4 et hydrocarbures ; sa masse et son PCI peuvent réduire le déficit.
3. Le char est le plus gros produit marchand quantifié, pas le principal flux de sortie : l'eau seule vaut 421 kg/t et 205 kg/t restent non alloués au standard.
4. La presse d'extrusion pourrait réduire fortement l'eau, mais elle déplace une pâte humide vers la méthanisation. Sans test, prix et exutoire, elle ne résout pas encore le modèle économique.
5. La valeur commerciale du char n'est pas démontrée par son contenu énergétique. Chlore, métaux, sodium, cendres et statut réglementaire doivent être testés avant de compter une vente ou même une combustion sur site.

## Cinq points les plus graves

1. Plus de 10 000 t/an de gaz ou liquide ne sont pas quantifiées dans le scénario standard.
2. Le besoin thermique net et le périmètre des 1 507 MJ/t OneWorld ne sont pas documentés.
3. Le gaz organique, potentiellement combustible, n'a ni masse ni PCI mesurés sur Urban Rig.
4. Le char standard est valorisé énergétiquement avec une mesure sur char d'uréthane, pas d'OMR.
5. La qualité et l'exutoire de l'huile, du char, du condensat et de la pâte humide ne sont pas démontrés à l'échelle du projet.

## Ce qui n'a pas pu être vérifié

- Bilan complet masse et énergie d'un essai Urban Rig sur OMR françaises : inexistant.
- Inclusion ou non de l'évaporation dans les 833 kcal/s du brûleur : non précisée par OneWorld.
- Masse, humidité et PCI du gaz organique Urban Rig : non mesurés.
- Rendement de combustion et de transfert thermique si le char ou l'huile alimente le brûleur : non fourni.
- PCI, cendres, chlore, métaux, sodium et débouché du char d'OMR : non mesurés.
- Eau, chlore et débouché du liquide d'OMR : non mesurés.
- Performance de la presse sur OMR françaises à 42,1 % d'humidité : seulement données commerciales ou autre schéma de traitement.
- Prix d'entrée, prix de la presse et exutoires : à confirmer par offres et contrats, pas par comparaison de tarifs publics.

## Conclusion en langage simple

Le lot 3 passe sous conditions strictes. La conclusion la plus importante est juste : le gaz hydrocarboné du plastique ne couvre pas la chaleur. Un modèle bancaire prudent doit donc prévoir la consommation de char ou d'huile, ou l'achat de combustible.

La faisabilité énergétique complète n'est toutefois pas encore démontrée, car le gaz organique peut fournir une énergie non mesurée et le périmètre du besoin OneWorld est inconnu. Surtout, environ 205 kg par tonne, soit près de 10 500 t/an, restent sans produit quantifié dans le scénario standard. L'essai R-021 avec bilans massique, énergétique, chlore, condensats et char est bloquant avant conception finale ou décision d'investissement, sans constituer à ce stade une preuve que le procédé ne fonctionne pas.
