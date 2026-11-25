# Contre-vérification de l'annexe 2, lot 2

Date : 2026-11-25  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-02-html/index.html`, sections 2.4, 2.5 et 2.7 et fiches liées  
Accès internet : OUI  
Lecture des PDF : OUI, originaux locaux ouverts aux pages citées  
Sources publiques : OUI, EUR-Lex et Légifrance ouverts dans leur version primaire

## Périmètre et méthode

Le contrôle porte sur la qualité de l'huile et du char, la composition et le pouvoir calorifique du gaz, les émissions, les odeurs, le bruit et les eaux de procédé. Les valeurs de laboratoire sont tenues pour valides et leur reprise est vérifiée. Les décisions D-016 à D-023, D-027, D-029, D-033 à D-035 et D-038 ne sont pas remises en concurrence avec d'autres hypothèses. Leur cohérence avec les pièces qu'elles citent reste contrôlée.

Le contrôle automatique a été lancé sur la source Markdown : 348 affirmations chiffrées, aucune sans source. Les 34 erreurs globales signalées par l'outil concernent surtout les paramètres et demandes du projet, pas une absence de lien dans ce lot. L'échantillon automatique de trois affirmations est indiqué à la fin.

## Tableau des verdicts

N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire
---|---|---|---|---|---|---|---|---
1 | 2.4.1 | Huile de plastiques d'emballage | PCS 46 000 J/g ; densité 0,8642 ; viscosité 1,706 ; point éclair inférieur à 40 °C ; soufre inférieur à 0,05 % ; cendres 0,002 % ; eau 0,13 % ; chlore 0,137 % | CHIBA-JLOS-HUILES | CONFIRMÉ | « 総発熱量（計算）46000 J/g » ; « 密度（15℃）0.8642 g/cm3 » ; « 動粘度（50℃）1.706 mm2/s » ; « 引火点 40℃未満 » ; « 硫黄分 0.05未満 » ; « 灰分 0.002 » ; « 水分 0.13 » ; « 塩素分 0.137 » | `prefecture-shiba-test-data-2.pdf`, PDF p. 45 | Reprise exacte du bulletin JLOS 2022.
2 | 2.4.1 | Huile de résidus non combustibles | PCS 45 000 J/g ; densité 0,8762 ; viscosité 1,759 ; point éclair inférieur à 40 °C ; soufre 0,06 % ; cendres 0,014 % ; eau 0,20 % ; chlore 0,526 % | CHIBA-JLOS-HUILES | CONFIRMÉ | « 総発熱量（計算）45000 J/g » ; « 密度（15℃）0.8762 g/cm3 » ; « 動粘度（50℃）1.759 mm2/s » ; « 引火点 40℃未満 » ; « 硫黄分 0.06 » ; « 灰分 0.014 » ; « 水分 0.20 » ; « 塩素分 0.526 » | même PDF, p. 46 | Reprise exacte.
3 | 2.4.1 | Huile fournie par OneWorld en 2019 | 43 270 J/g ; viscosité 1,11 ; point éclair inférieur ou égal à 40 °C ; soufre 0,014 % ; cendres 0,005 % ; eau 0,40 % vol. ; chlore inorganique 0,0001 % | NKKK-ZPE8004-2019 | CONFIRMÉ | « Gross calorific value 43,270 J/g » ; « Kinematic viscosity 1.11 mm2/s » ; « Flash point 40 or below » ; « Sulfur 0.014 mass% » ; « Inorganic chlorine 0.0001 mass% » | `Urban Rig Recycling Solutions ENG .pdf`, p. 17 | nature: constructeur pour la transmission et l'origine de l'échantillon ; analyse attribuée à NKKK.
4 | 2.4.1, fiches 2.5.f.8 et 2.5.f.9 | Conversion du chlore | 0,137 % = 1 370 ppm ; 0,526 % = 5 260 ppm | CALC-A2-JLOS-CL-EMB-PPM ; CALC-A2-JLOS-CL-RES-PPM | CONFIRMÉ | « resultat: 1370 ppm » ; « resultat: 5260 ppm » | `calculs.yaml`, calculs cités ; recalcul 0,137 x 10 000 et 0,526 x 10 000 | Arithmétique exacte.
5 | 2.4.1, fiche 2.4.i | Seuil de 1 % d'organohalogénés exprimés en chlore | au-dessus de 1 %, température minimale 1 100 °C | IED-2010-75-ART50 | CONFIRMÉ | « If hazardous waste with a content of more than 1 % of halogenated organic substances, expressed as chlorine, is incinerated or co-incinerated, [...] at least 1 100 °C. » | Directive 2010/75/UE, article 50(2) | Les deux teneurs totales mesurées sont sous 1 %. Le seuil concerne les déchets dangereux et ne constitue ni une homologation du combustible, ni une limite générale d'acceptation.
6 | 2.4.4 | Métaux du char de plastiques d'emballage | Cd 31 ; Pb 140 ; Hg 0,06 ; As 0,95 mg/kg | CHIBA-OOSUMI-CHAR | CONFIRMÉ | « カドミウム 31 mg/kg » ; « 鉛 140 mg/kg » ; « 総水銀 0.06 mg/kg » ; « 砒素 0.95 mg/kg » | `prefecture-shiba-test-data-2.pdf`, PDF p. 47 | Reprise exacte.
7 | 2.4.4 | Métaux du char de résidus non combustibles | Cd 36 ; Pb 42 ; Hg inférieur à 0,02 ; As 1,8 mg/kg | CHIBA-OOSUMI-CHAR | CONFIRMÉ | « カドミウム 36 mg/kg » ; « 鉛 42 mg/kg » ; « 総水銀 0.02未満 mg/kg » ; « 砒素 1.8 mg/kg » | même PDF, p. 49 | Reprise exacte.
8 | 2.4.4 | Limites d'un amendement organique UE | Cd 2 ; Pb 120 ; Hg 1 ; As inorganique 40 mg/kg sec | FPR-2019-1009 | CONFIRMÉ | « cadmium (Cd): 2 mg/kg dry matter » ; « mercury (Hg): 1 mg/kg dry matter » ; « lead (Pb): 120 mg/kg dry matter » ; « inorganic arsenic (As): 40 mg/kg dry matter » | Règlement (UE) 2019/1009, annexe I, PFC 3(A), point 2 | Le refus de l'usage comme amendement est solidement étayé, notamment par le cadmium.
9 | 2.4.4 | Paramètres CSR français | PCI au moins 12 000 kJ/kg ; Hg au plus 3 mg/kg sec ; chlore à mesurer | ARRETE-CSR-2016 | CONFIRMÉ | « a un PCI sur CSR brut supérieur ou égal à 12 000 kJ/kg » ; « mercure (Hg) : 3 mg/kg de matière sèche » ; « chlore (Cl) : 15 000 mg/kg de matière sèche » | Arrêté du 23 mai 2016, articles 3 et annexe, version en vigueur | Le PCI et le mercure passent sur les valeurs utilisées. La qualification CSR n'est pas démontrée tant que le chlore, l'homogénéité et les autres caractérisations requises ne sont pas établis.
10 | 2.4.4, fiche 2.2.l | Pouvoir calorifique attribué au char ménager comme hypothèse | 32,09 MJ/kg mesurés sur un char d'uréthane | IZUMITEC-R35-339439 ; D-038 | CONFIRMÉ | « INOウレタン炭 » ; « 発熱量 32090 J/g » | `Calorie-content-UR-Carbide-1.pdf`, p. 1 | Le HTML dit correctement qu'il s'agit d'un char d'uréthane et d'une hypothèse du porteur, pas d'une mesure sur ordures ménagères.
11 | 2.5.1 | Composition brute du gaz | H2 12,7 % ; CH4 3,2 % ; C2H6 0,7 % ; C2H4 0,2 % ; C3H8 0,3 % ; C3H6 0,3 % ; CO 0,6 % ; CO2 1,7 % ; O2 12,3 % ; N2 65,8 % vol. | KANSO-B2002600 | CONFIRMÉ | « 水素 12.7 % » ; « メタン 3.2 % » ; « エタン 0.7 % » ; « エチレン 0.2 % » ; « プロパン 0.3 % » ; « プロピレン 0.3 % » ; « 一酸化炭素 0.6 % » ; « 二酸化炭素 1.7 % » ; « 酸素 12.3 % » ; « 窒素 65.8 % » | `Analysis-Results-Off-gas-Odor-Exhaust.pdf`, p. 1 | Un seul échantillon ; charge et point de prélèvement non renseignés.
12 | 2.5.1 | Composition hors O2 et N2 et part combustible | H2 64,5 % ; CH4 16,2 % ; combustible 91,4 % vol. | CALC-A2-GAZ-PART-COMBUSTIBLE ; D-021 | CONFIRMÉ | « 12,7 / 19,7 = 64,47 % » ; « 3,2 / 19,7 = 16,24 % » ; « 18,0 / (18,0 + 1,7) = 0,9137 » | rapport KANSO p. 1 ; recalcul | Calcul mécanique exact sous l'hypothèse déclarée que O2 et N2 sont de l'air de dilution.
13 | 2.5.2, fiche 2.5.c.12 | PCI massique du gaz hors air | 37,4 MJ/kg | CALC-A2-GAZ-PCI | CONFIRMÉ | « resultat: 37.386 MJ/kg » | `calculs.yaml`, CALC-A2-GAZ-PCI ; recalcul avec les fractions molaires et PCI molaires cités | Arithmétique cohérente pour la composition KANSO hors air. D-038 rend visible le caractère choisi de son transfert.
14 | 2.5.3 | La brochure OneWorld donne 11,5 % de gaz combustible | 11,5 % de l'entrée | OW-ENG-P16-BILAN ; D-038 | DIFFÉRENT | « Recovery Loss 11.5 % » ; « Mainly discharged as flue gas; a very small amount will be carbide. » | `Urban Rig Recycling Solutions ENG .pdf`, p. 16 | nature: constructeur. La source ne nomme pas cette ligne « off-gas » et dit qu'elle inclut aussi du char. Assimiler toute la perte au gaz de pyrolyse KANSO est une hypothèse, pas une donnée OneWorld mesurée.
15 | 2.5.3, fiche 2.5.d.10 | Énergie du gaz sur charge riche en résines | 4 299 MJ/t | CALC-A2-NRJ-GAZ-RESINE | CALCUL FAUX | « part: 0.115 [...] source: OW-ENG-P16-BILAN » ; source réelle : « Recovery Loss 11.5 % » | `calculs.yaml`, CALC-A2-NRJ-GAZ-RESINE ; brochure p. 16 | 0,115 x 1 000 x 37,386 = 4 299 MJ/t est exact, mais l'entrée 11,5 % n'est pas une fraction démontrée de gaz combustible. Le résultat doit être étiqueté hypothèse D-038 et non donnée de conception mesurée.
16 | 2.7.1 | Limites IED utilisées | poussières 10 ; HCl 10 ; SO2 50 ; NOx 200 ; CO 50 mg/Nm3 ; dioxines 0,1 ng/Nm3 | IED-2010-75-ANX6-P3 | CONFIRMÉ | « Total dust 10 » ; « Hydrogen chloride (HCl) 10 » ; « Sulphur dioxide (SO2) 50 » ; « Nitrogen monoxide (NO) and nitrogen dioxide (NO2), expressed as NO2 200 » ; « 50 as daily average value » ; « Dioxins and furans 0,1 » | Directive 2010/75/UE, annexe VI, partie 3, points 1.1, 1.4 et 1.5 | Les périodes diffèrent : les dioxines sont une moyenne sur 6 à 8 h, pas une moyenne journalière.
17 | 2.7.1 | BAT-AEL d'une installation neuve | poussières inférieur à 2-5 ; HCl inférieur à 2-6 ; SO2 5-30 ; NOx 50-120 mg/Nm3 ; PCDD/F inférieur à 0,01-0,04 ng I-TEQ/Nm3 | BAT-WI-2019-2010 | CONFIRMÉ | « Dust < 2-5 » ; « HCl < 2-6 » ; « SO2 5-30 » ; « NOX 50-120 » ; « PCDD/F [...] < 0,01-0,04 » | Décision d'exécution (UE) 2019/2010, tableaux 6 et 7 | Valeurs exactes. Les périodes de moyenne dépendent du polluant.
18 | 2.7.2 | Pires mesures 2022 | NOx 43 ppm ; SOx 1,4 ppm ; poussières 0,004 g/m3 ; dioxines 0,067 ng-TEQ/m3 | CHIBA-OOSUMI-FUMEES | CONFIRMÉ | « 窒素酸化物濃度 43 ppm » ; « 硫黄酸化物濃度 1.4 ppm » ; « ばいじん濃度 0.004 g/m3 » ; « ダイオキシン類 0.067 ng-TEQ/m3 » | `prefecture-shiba-test-data-2.pdf`, PDF p. 56 | Rapport marqué provisoire ; O2 non indiqué.
19 | 2.7.2 | Mesures 2023 | NOx 30 ppm ; SOx inférieur à 0,5 ppm ; poussières inférieures à 0,005 g/m3N ; dioxines 0,011 et 0,025 ng-TEQ/m3 | TANABE-2023 ; DIOXINES-2023 | CONFIRMÉ | « 窒素酸化物濃度 30 ppm » ; « 硫黄酸化物濃度 0.5未満 ppm » ; « ばいじん濃度 0.005未満 g/m3N » ; « 排ガス(9/26) 0.011 » ; « 排ガス(9/27) 0.025 » | `Exhaust Gas Concentration - Bad Smell - Dioxins  .pdf`, p. 1 et 5 ; `Dioxins .pdf`, p. 1 | Reprise exacte ; rapport dioxines annoncé comme rapide ou préliminaire.
20 | 2.7.2 | Mesures 2020 | NOx 15 ppm ; HCl inférieur à 1 ppm ; SOx inférieur à 1 ppm ; poussières inférieures à 0,002 g/m3 ; O2 18,5 % | KANSO-20002610 | CONFIRMÉ | « 窒素酸化物濃度 15 ppm » ; « 塩化水素濃度 1 ppm未満 » ; « 硫黄酸化物濃度 1 ppm未満 » ; « ダスト濃度 0.002 g/m3未満 » ; « 酸素濃度 18.5 % » | `Analysis-Results-Off-gas-Odor-Exhaust.pdf`, p. 2 | Reprise exacte.
21 | 2.7.2, fiches 2.5.e.1 à 2.5.e.4 | Correction 2020 à 11 % O2 | facteur 4 ; NOx 123 ; HCl inférieur à 6,52 ; poussières inférieures à 8 mg/Nm3 | CALC-A2-FACTEUR-O2-2020 et calculs liés | CONFIRMÉ | « (21 - 11) / (21 - 18,5) = 4 » ; « 15 x 2,05 x 4 = 123 » ; « 1 x 1,63 x 4 = 6,52 » ; « 0,002 x 1 000 x 4 = 8 » | recalcul à partir du rapport KANSO p. 2 et de la formule de correction | Arithmétique exacte. Elle soutient seulement les polluants mesurés lors de cette campagne.
22 | 2.7.2, fiches 2.5.e.8 à 2.5.e.11 | O2 maximal pour respecter les seuils avec les résultats 2022 | NOx IED 16,6 % ; poussières IED 17,0 % ; dioxines IED 14,3 % ; NOx BAT 13,7 % | calculs CALC-A2-O2MAX | CONFIRMÉ | « resultat: 16.59 % O2 » ; « resultat: 17.0 % O2 » ; « resultat: 14.3 % O2 » ; « resultat: 13.65 % O2 » | `calculs.yaml`, calculs cités ; recalcul de la formule | Calculs exacts. Ils montrent précisément que la conformité 2022 dépend d'un O2 non mesuré.
23 | 2.7.2, tableau et lecture investisseurs | Chaque polluant mesuré passe la limite légale dans les trois campagnes | « Yes » ; « every measured pollutant passes » | IED-2010-75-ANX6-P3 et campagnes japonaises | ABSENT | « They are standardised at 11 % oxygen in waste gas » ; rapports 2022 et 2023 : aucune teneur en O2 reportée | Directive 2010/75/UE, annexe VI, partie 3 ; rapports 2022 et 2023 | Les valeurs brutes sont numériquement sous les limites, mais la conformité n'est pas démontrée sans correction O2. Pour NOx, SO2 et poussières, des mesures ponctuelles ne démontrent pas non plus une moyenne journalière. Conclusion : POSSIBLE SOUS CONDITIONS, pas « Yes » réglementaire.
24 | 2.7.2 | Comparaison des dioxines aux BAT-AEL | 2022 : 0,067, au-dessus de 0,04 ; 2023 : 0,011 et 0,025, dans la plage brute | CHIBA-OOSUMI-FUMEES ; DIOXINES-2023 ; BAT-WI-2019-2010 | CONFIRMÉ | « 0.067 ng-TEQ/m3 » ; « 0.011 » ; « 0.025 » ; BAT : « PCDD/F [...] < 0,01-0,04 ng I-TEQ/Nm3 » | rapports cités ; décision 2019/2010, tableau 7 | Comparaison numérique correcte, avec les réserves déjà indiquées dans le HTML sur l'O2 et le schéma TEQ.
25 | 2.7.3 | Odeurs | limite de rapport inférieure à 10 au périmètre ; 14 en 2020, 16, 18, 19 en 2022 et 24, 22 en 2023 près ou à l'exutoire | TES-ODEUR-2020 ; CHIBA-OOSUMI-ODEURS-BRUIT ; TANABE-2023 | CONFIRMÉ | « 敷地境界 [...] 10未満 » ; « 発生源（排出口）14 » ; « 排出口付近 16 » ; « 排出口付近 18 » ; résultats 2023 « 臭気指数 24 » et « 臭気指数 22 » | rapport KANSO p. 3 ; rapport Chiba PDF p. 62 à 67 ; rapport Tanabe p. 2 et 6 | Reprise exacte. Le texte ne prétend pas démontrer le respect d'une règle française.
26 | 2.7.3 | Bruit à 1 m de la machine | 76, 76 et 77 dB(A) | CHIBA-OOSUMI-ODEURS-BRUIT | CONFIRMÉ | « 発生源（機側1m）10:00 76 ; 12:30 76 ; 15:30 77 » | `prefecture-shiba-test-data-2.pdf`, PDF p. 74 | Reprise exacte. Le même dossier indique 57 à 59 dB(A) L5 à la limite du site, PDF p. 72.
27 | 2.7.4 | Eau brute de procédé | emballages : phénols 740 mg/L et cyanure 14 mg/L ; résidus : pH 0,8 et DBO 16 000 mg/L | CHIBA-OOSUMI-EAUX | CONFIRMÉ | « フェノール類 740 mg/L » ; « シアン化合物 14 mg/L » ; « 水素イオン濃度 0.8 pH » ; « 生物化学的酸素要求量 16000 mg/L » | `prefecture-shiba-test-data-2.pdf`, PDF p. 51 à 53 | Reprise exacte. Le besoin d'un traitement dédié est évident.
28 | 2.7.4 | Essai SEA CORAL | chlorures 31 000 vers 31 mg/L ; résiduel 140 000 mg/L ; environ 330 t/j par soufflante | SEACORAL-DETAIL-ENG | CONFIRMÉ | « Chloride ion mg/L Raw water 31,000 ; Treated water 31 ; Residual water 140,000 » ; « About 330ton/Day » | `SEA CORALdetail.pdf`, pages non numérotées, tableau d'essai et calcul de capacité | nature: constructeur. Il s'agit d'un essai d'eau de mer, sans laboratoire ni date, pas d'un essai sur eau de pyrolyse. Le HTML le dit correctement.

## Écarts à signaler

### E-1. La ligne « Recovery Loss 11,5 % » est transformée en gaz combustible

- Annexe : section 2.5.3, puis calcul CALC-A2-NRJ-GAZ-RESINE et conclusions énergétiques liées.
- Source : brochure OneWorld, p. 16.
- Gravité : IMPORTANTE.
- Constat : OneWorld écrit « Recovery Loss 11.5 % » et « Mainly discharged as flue gas; a very small amount will be carbide ». La source ne donne ni masse de gaz de pyrolyse combustible, ni composition de cette perte.
- Correction proposée : écrire « hypothèse D-038 : toute la recovery loss est provisoirement assimilée au gaz KANSO » ou retirer les 4 299 MJ/t et les ratios qui en dépendent jusqu'à un bilan gazeux mesuré. La voie indépendante à 15 % de gaz par différence reste une hypothèse distincte.

### E-2. Le tableau transforme une comparaison brute en conformité réglementaire

- Annexe : section 2.7.2, colonnes « Passes the legal limit? » et lecture investisseurs.
- Sources : rapports 2022 et 2023 ; directive 2010/75/UE.
- Gravité : IMPORTANTE.
- Constat : l'O2 n'est pas reporté en 2022 et 2023, alors que les limites sont à 11 % O2. Pour NOx, SO2 et poussières, les valeurs limites citées sont des moyennes journalières, tandis que les rapports versés montrent des mesures ponctuelles.
- Correction proposée : remplacer « Yes » par « raw value below the numerical limit; regulatory compliance not demonstrated » et conclure « POSSIBLE SOUS CONDITIONS ».

### E-3. La liste de mesures demandées pour une démonstration de permis est incomplète

- Annexe : section 2.7.2, « Conditions for a permit-grade demonstration ».
- Source : directive 2010/75/UE, annexe VI, et décision 2019/2010.
- Gravité : IMPORTANTE.
- Constat : la liste demande O2, CO et HCl, mais la démonstration complète exige aussi les autres polluants applicables et les bonnes périodes de moyenne. Le dossier présenté ne couvre notamment pas de façon complète COT, HF et métaux à l'émission.
- Correction proposée : demander une campagne sur la charge cible couvrant l'ensemble du permis, aux conditions normalisées, avec rapports finaux et périodes de mesure réglementaires.

### E-4. Le traitement de l'eau industrielle n'est pas démontré

- Annexe : section 2.7.4.
- Sources : analyses Oosumi p. 51 à 54 et documentation SEA CORAL.
- Gravité : IMPORTANTE avant décision d'investissement, non bloquante pour la plausibilité technique.
- Constat : l'eau brute contient notamment phénols, cyanures, forte DBO et pH très acide. SEA CORAL n'est documenté que sur une eau salée.
- Correction proposée : essai de traitabilité sur eau réelle, bilan eau continu, filière de traitement, destination des concentrats, critères de rejet et garantie de performance.

### E-5. Le seuil de 1 % de chlore est présenté sans son périmètre complet

- Annexe : section 2.4.1.
- Source : directive 2010/75/UE, article 50(2).
- Gravité : MINEURE.
- Constat : le texte européen vise un déchet dangereux contenant plus de 1 % de substances organiques halogénées exprimées en chlore. Être sous 1 % évite ce déclencheur particulier de 1 100 °C, mais ne prouve pas l'acceptabilité du combustible.
- Correction proposée : ajouter « this threshold is only the Article 50 temperature trigger for hazardous waste; it is not a fuel acceptance limit ».

## Autres interprétations

1. La lecture favorable des émissions est que trois campagnes indépendantes convergent vers des concentrations brutes faibles, avec une campagne 2020 qui reste sous les limites après correction à 11 % O2. Cela rend une conformité future plausible.
2. La lecture prudente, plus solide pour une décision d'investissement, est que les campagnes 2022 et 2023 ne peuvent pas être qualifiées de conformes : O2 absent, rapports provisoires ou préliminaires, CO absent et périodes de moyenne non démontrées. Il ne s'agit pas d'une non-conformité prouvée, mais d'une conformité non documentée.
3. Le char passe nettement les deux paramètres CSR chiffrés dans l'annexe, PCI et mercure. Cela ne suffit pas à qualifier un lot de CSR : le chlore, l'homogénéité, les cendres, l'humidité et les autres caractérisations restent à établir. « Possible sous conditions » est la bonne conclusion.
4. L'huile est énergétiquement proche d'un combustible liquide et sous le déclencheur de 1 % de l'article 50. Sa teneur en chlore de 1 370 à 5 260 ppm ferme cependant les débouchés exigeants sans purification. Le débouché combustible industriel reste possible uniquement avec acceptation contractuelle et préfectorale.
5. D-038 est raisonnable pour conserver 37,4 MJ/kg comme ordre de grandeur du gaz hors air. Elle devient déraisonnable si elle transforme sans étiquette toute la « recovery loss » de 11,5 % en gaz combustible de cette composition. La correction d'étiquette est nécessaire.

## Les cinq erreurs ou manques les plus graves

1. IMPORTANTE : 11,5 % de « recovery loss » traité comme 11,5 % de gaz combustible, ce qui rend les 4 299 MJ/t non démontrés.
2. IMPORTANTE : conformité IED affichée « Yes » pour 2022 et 2023 sans O2 de référence ni démonstration des moyennes réglementaires.
3. IMPORTANTE : campagne d'émissions de permis incomplète, notamment CO, COT, HF et métaux selon le périmètre applicable.
4. IMPORTANTE : traitement de l'eau de procédé non testé sur l'effluent réel.
5. MINEURE : seuil de 1 % de chlore présenté comme référence de débouché sans rappeler qu'il s'agit seulement du déclencheur de température de l'article 50 pour certains déchets dangereux.

## Manques évidents avant investissement

| Point à obtenir | Gravité avant décision d'investissement | Pourquoi |
|---|---|---|
| Campagne continue sur la charge cible, avec émissions complètes, O2, débits et périodes réglementaires | BLOQUANT avant engagement industriel | Elle seule peut transformer les résultats ponctuels encourageants en démonstration de conformité et de performance stable. |
| Garanties contractuelles sur émissions, qualité de l'huile et du char, débit de gaz et traitement des eaux | BLOQUANT avant commande ferme | Les brochures, hypothèses et essais en lots ne créent pas de recours contractuel. |
| Essai de traitement de l'eau réelle et filière des concentrats | IMPORTANT | La solution SEA CORAL n'est pas testée sur les contaminants observés. |
| Mesure du chlore du char et spécification complète par lot | IMPORTANT | Nécessaire pour le débouché CSR et le permis de l'utilisateur. |
| Spécification contractuelle de l'huile, avec chlore total et organique | IMPORTANT | Nécessaire pour confirmer le débouché, le prix et le traitement requis. |

Ces manques ne démontrent pas une impossibilité technique. Les deux premiers empêchent cependant un investissement ferme fondé sur des performances garanties.

## Conclusion en langage simple

**PASSE pour les valeurs de laboratoire.** Les résultats d'huile, de char, de gaz, d'odeur, de bruit et d'eau sont fidèlement repris. Le PCI calculé du gaz, 37,4 MJ/kg hors air, est arithmétiquement cohérent avec l'échantillon KANSO.

**NE PASSE PAS comme donnée de gaz mesurée :** les 11,5 % de la brochure sont une « recovery loss », pas une fraction mesurée de gaz combustible. Les 4 299 MJ/t qui en résultent doivent être requalifiés en hypothèse ou retirés.

**POSSIBLE SOUS CONDITIONS pour les émissions.** Les mesures brutes sont encourageantes et la campagne 2020 passe après correction O2 pour les polluants mesurés. Les campagnes 2022 et 2023 ne démontrent pas la conformité européenne sans O2, périodes de moyenne et panel complet.

**POSSIBLE SOUS CONDITIONS pour les produits.** L'huile peut viser un usage combustible permis ; le char peut viser un CSR. Les deux nécessitent des spécifications de lot, du chlore mesuré et une acceptation réglementaire et commerciale.

**À MESURER OU CONFIRMER :** campagne continue sur la charge cible, panel d'émissions complet, débit et composition du gaz, traitement de l'eau réelle, chlore du char et garanties de performance.

## Ce qui n'a pas été vérifié dans ce lot

- Les prix, coûts de traitement et valeurs de débouché : exclus par les règles de vérification légère.
- Le rendement jet fuel de 18 % à 27 % : hypothèse de correspondance aire GC-MS / masse déclarée comme ordre de grandeur, non utilisée dans le modèle financier.
- La performance industrielle continue de SEA CORAL sur eau de pyrolyse : aucun essai de cette nature n'est versé.
- La conformité française finale : elle dépend du classement ICPE, du permis et des conditions de la future installation, traités dans l'annexe 4.
- Les sections 2.6, 2.8, 2.9, 2.10 et les messages investisseurs : lot 3.

## Décompte

28 verdicts :

- CONFIRMÉ : 25
- DIFFÉRENT : 1
- ABSENT : 1
- INACCESSIBLE : 0
- NON SOURCÉ : 0
- CALCUL FAUX : 1

Gravité des écarts dans l'annexe actuelle : 0 BLOQUANT, 4 IMPORTANTS, 1 MINEUR.  
Manques avant investissement ferme : 2 BLOQUANTS, 3 IMPORTANTS.

## Échantillon automatique de trois affirmations à faire contrôler par Stéphane

Le tirage du contrôle automatique a donné :

1. Fiche 2.1.a : identification du dossier préfectoral japonais et de ses 74 pages.
2. Fiche 2.1.b : température de 600 °C et pression de 0,15 MPa du schéma du réacteur d'essai.
3. Fiche 2.1.d : total de 931 L d'eaux usées pour les onze essais.
