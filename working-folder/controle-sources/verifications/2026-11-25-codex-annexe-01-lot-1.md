# Contre-vérification indépendante de l'annexe 1, lot 1

Date : 25 novembre 2026  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-01-html/index.html` et fiches liées  
Périmètre : « How to Read This Annex », « Key Messages », sections 1.1 à 1.3  
Accès internet : OUI  
Lecture des PDF : OUI, texte extrait et pages scannées contrôlées visuellement lorsque nécessaire

## Conclusion courte

Le lot 1 **passe sous conditions comme description des données de conception OneWorld**, mais **ne passe pas encore comme preuve de performance de l'URC-2000 continu**. Les documents confirment la gamme, l'architecture en postes, le chemin du procédé et les produits annoncés. En revanche, les essais techniques cités ont été réalisés sur des unités en lots, pas sur l'URC-2000 continu de 200 t/j.

Le point bloquant pour une décision d'investissement est donc documentaire et technique : obtenir une preuve d'exploitation continue à l'échelle visée, ou à défaut une garantie contractuelle de capacité, de rendement, de consommation et de disponibilité assortie d'un essai de réception représentatif.

## Tableau des vérifications

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---:|---|---|---|---|---|---|---|---|
| 1 | How to Read | Les données OneWorld sont présentées comme données constructeur non vérifiées indépendamment | 90 % ou 95 % de confiance éditoriale | D-022, D-016, D-020 | CONFIRMÉ | « these are the company's own figures and have not been verified independently » | HTML, How to Read | Présentation loyale. Les pourcentages sont une convention éditoriale, pas une probabilité scientifique. |
| 2 | Key Messages, 1.1 | Vapeur surchauffée, atmosphère sans oxygène, récupération d'huile, char et métaux non oxydés | 600 °C pour la vapeur injectée | OW-ENG-P14-P15-PROCEDE | CONFIRMÉ | « Inject high-temperature oxygen-free steam(further superheated) at 600 °C into the cracking furnace. » ; « metals can be extracted in a non-oxidizing state » | Brochure OneWorld anglaise, p. 2 et 14 | Nature : constructeur. La source décrit bien le procédé annoncé. |
| 3 | Key Messages, 1.1 | URC-2000 continu nominal et ligne de sept postes | 200 t/j ; 7 unités | UR2000-JP-P08-SPEC ; UR2000-JP-P06-P07-MODULES | CONFIRMÉ | « 処理量 / 日 200 トン / 日 » ; « 本機処理プラント (200T) は 7 ユニットで構成。 » | Brochure URC-2000 japonaise, p. 8 et p. 6 | Nature : constructeur. Capacité nominale annoncée, pas capacité mesurée. |
| 4 | Key Messages | Couverture du brûleur par le gaz du cas riche en résines | 2,9 fois avec 11,5 % de gaz | CALC-A2-COUV-BRULEUR-RESINE ; OW-ENG-P16-BILAN | CALCUL FAUX | « Recovery Loss 11.5 % [...] Mainly discharged as flue gas; a very small amount will be carbide. » | Brochure OneWorld anglaise, p. 16 | Le calcul arithmétique 4 299,4 / 1 506,65 = 2,8536 est exact, mais l'entrée 11,5 % n'est ni une mesure de gaz ni clairement une fraction massique de l'entrée. La table totalise 102 t pour une entrée annoncée de 200 t. L'expression « measured gas [...] with 11.5 % gas » est fausse. |
| 5 | Key Messages | Couverture du brûleur sur plastique pur | 3,7 fois avec 15 % de gaz | CALC-A2-COUV-BRULEUR-PLASTIQUE15 ; D-038 | CONFIRMÉ | « gaz / besoin » ; 5 607,9 / 1 506,65 = 3,7221 | Calculs.yaml, CALC-A2-COUV-BRULEUR-PLASTIQUE15 | Calcul exact sous l'hypothèse déclarée de 15 %. Ce n'est pas une mesure sur l'URC-2000 continu. |
| 6 | Key Messages | Dioxines mesurées en 2023 | 0,011 et 0,025 ng-TEQ/m3 | DIOXINES-2023 | CONFIRMÉ | « 排ガス(9/26) 0.1 0.011 基準値以下 ; 排ガス(9/27) 0.1 0.025 基準値以下 » | Rapport préliminaire Kankyo Kogai Bunseki Center, p. 1 | Mesures de laboratoire tiers. Le document est préliminaire et ne donne pas l'oxygène de référence. |
| 7 | Key Messages | Dioxines mesurées en 2022 | 0,067 ng-TEQ/m3 | CHIBA-OOSUMI-FUMEES | CONFIRMÉ | « ダイオキシン類（毒性等量） ng-TEQ/m³ 0.067 » | Rapport provisoire Oosumi, PDF p. 56, imprimé p. 50 | Mesure de laboratoire tiers. Pas d'oxygène de référence indiqué. |
| 8 | Key Messages | Les trois mesures sont sous la limite UE | 0,1 ng/Nm3 | IED-2010-75-ANX6-P3 | DIFFÉRENT | « They are standardised at 11 % oxygen in waste gas » ; « Dioxins and furans 0,1 » | Directive 2010/75/UE, annexe VI, partie 3, points 1 et 1.4 | Les nombres bruts sont inférieurs à 0,1, mais les rapports ne donnent pas la correction à 11 % O2. La conformité réglementaire ne peut pas être conclue avec ces seules valeurs. |
| 9 | 1.1 | URC-2000 conçu pour des déchets ménagers humides | Résidus alimentaires, boues, sols | OW-ENG-P04-P07-SPEC-PLANS | CONFIRMÉ | « URC-2000 is designed for carbonizing waste with high moisture content such as food residue, waste with sludge and soil » | Brochure OneWorld anglaise, p. 4 | Nature : constructeur. Aucun domaine admissible chiffré d'humidité ou de densité n'est fourni. |
| 10 | 1.1, gamme | URC-2000 | 200 t/j ; 7 étapes ; 3 bennes de 4,5 m3 ; 66 x 7 x 7 m | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « Throughput / day 200 ton / day » ; « Size (Processing Unit) W:66m D:7m H:7m » ; « Size (bucket) [...] 4.5m3 » | Brochure OneWorld anglaise, p. 4 | Nature : constructeur. Le document japonais donne 62 x 10 x 7 m, contradiction déjà visible dans le dossier. |
| 11 | 1.1, gamme | URC-1000 | 100 t/j ; 4 étapes ; 2 bennes de 4,5 m3 ; 20 x 7 x 7 m | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « 100 ton Continuous Process URC-1000 » ; « 2 buckets as 1 batch » ; « W:20m D:7m H:7m » | Brochure OneWorld anglaise, p. 6 | Nature : constructeur. |
| 12 | 1.1, gamme | URC-400 | 40 t/j ; 7 étapes ; 3 bennes de 1 m3 ; 41 x 7 x 7 m | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « Throughput / day 40ton / day » ; « 3 buckets as 1 batch » ; « W:41m D:7m H:7m » | Brochure OneWorld anglaise, p. 5 | Nature : constructeur. |
| 13 | 1.1, gamme | URC-150 | 15 t/j ; 7 étapes ; bennes de 1 ou 2 m3 ; 22 x 6,5 x 6 m | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « Throughput / day 15ton / day » ; « W:22m D:6.5m H:6m » | Brochure OneWorld anglaise, p. 7 | Nature : constructeur. |
| 14 | 1.1, gamme | Unités en lots | URB-50 5 t/j ; URT-10 1 t/j ; URB-10 1 t | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « 5 ton 1 Batch URB-50 » ; « 1 ton 1 Batch URT-10 » ; « 1 ton 1 Batch URB-10 » | Brochure OneWorld anglaise, p. 3, 8 et 9 | Nature : constructeur. |
| 15 | 1.1 | Les essais cités sont des essais en lots | Noda 2022 ; URT-10 2021 | CHIBA-RAPPORT-2023 ; OWJ-DEMO-2021 | CONFIRMÉ | « essais [...] sur la machine URBAN RIG [...] en lots de 20 à 60 kg » ; « 投入前重量 299.2kg » | Rapport Chiba, PDF p. 7 et fiches ; rapport OneWorld 2021, p. 8 | C'est la limite centrale du dossier : aucun de ces essais ne démontre le fonctionnement du continu à 200 t/j. |
| 16 | 1.2.1 | Sept unités d'environ 12 t, fabriquées en série | 7 ; environ 12 t par unité | UR2000-JP-P06-P07-MODULES | CONFIRMÉ | « 本機処理プラント (200T) は 7 ユニットで構成。 ; 約 12 トン処理機 ( 1 ユニット ) を工場量産 » | Brochure URC-2000 japonaise, p. 6 | Nature : constructeur. « 12 t » désigne ici le poids annoncé d'une unité, pas sa capacité par lot. |
| 17 | 1.2.1 | Bennes et cadence de déplacement | 4,5 m3 ; 3 bennes ; 90 min | OW-ENG-P14-P15-PROCEDE | CONFIRMÉ | « 3 bucket movement in 90 minutes » ; « Size (bucket) [...] 4.5m3 » | Brochure OneWorld anglaise, p. 4 et 15 | Nature : constructeur. |
| 18 | 1.2.1, fiche 1.C.a | Temps total de passage | 10,5 h | CALC-A1-UR2000-TEMPS-TOTAL | CONFIRMÉ | « 7-continuous process, 90 minutes » ; 7 x 90 / 60 = 10,5 | Brochure OneWorld anglaise, p. 15 ; recalcul | Calcul exact. |
| 19 | 1.2.1 | Cadence maximale implicite | 48 bennes x 4,17 t = 200,16 t/j | UR2000-JP-P08-SPEC ; CALC-A2-UR2000-CADENCE | CONFIRMÉ | « 24 時間のバケット搬入台数 48 台 » ; « MAX 重量 : 4.17 t » | Brochure URC-2000 japonaise, p. 7 ; recalcul | Arithmétique exacte. La capacité de 200 t/j suppose chaque benne au poids maximal. Le document anglais annonce parallèlement 51 bennes et une densité 0,6, soit 137,7 t/j. |
| 20 | 1.2.1 | Profil thermique de la brochure 2019 | 150, 300, 450, 600, 400, 150 et 60 °C | OW-ENG-P14-P15-PROCEDE | CONFIRMÉ | « 150℃ 300℃ 450℃ 600℃ 400℃ 150℃ 60℃ » | Brochure OneWorld anglaise, p. 15 | Nature : constructeur. |
| 21 | 1.2.1 | Température et pression de spécification | max. 600 °C ; moins de 0,2 MPa | UR2000-JP-P08-SPEC | CONFIRMÉ | « 熱処理分解温度 MAX 600℃ 常圧 0.2MPa 以下 » | Brochure URC-2000 japonaise, p. 8 | Nature : constructeur. Le sens exact de « pression inférieure à 0,2 MPa » doit être spécifié, notamment absolue ou relative. |
| 22 | 1.2.1 | Profils alternatifs et machine à neuf postes | 500 °C par zone en 2014 ; 250, 450, 600 et 350 °C dans l'animation 2024 ; 9 postes à Toyohashi | UR2000-JP-P09-P13-PLANS ; OW-VIDEO-ANIMATION-2024 ; OW-STEP-TOYOHASHI-9 | CONFIRMÉ | « No. 3 ゾーン (max. 500℃ 加熱) » ; « HEATING ZONE » avec 250, 450, 600 et 350 °C ; « 3Dプリンタ用-豊橋9連続機総合組立図 » | Plan OneWorld 2014, p. 12 ; vidéo 2024 ; en-tête STEP | L'annexe montre correctement la contradiction et demande de confirmer la configuration livrée. |
| 23 | 1.2.2 | Chaudière, surchauffeur, réacteur et séparation liquide | 165 °C ; 600 °C ; catalyseur, condenseur, électrovanne, séparation huile-eau | OW-ENG-P14-P15-PROCEDE | CONFIRMÉ | « General purpose boiler max. 165℃ » ; « Superheated steam generator max. 600℃ » ; « Segregate gas-oil and heavy-oil [...] through a solenoid valve » | Brochure OneWorld anglaise, p. 14 | Nature : constructeur. Le schéma illustré est celui de l'URB-50 en lots. |
| 24 | 1.2.2 | Séquence observée sur l'unité Noda | Catalyseur avant condenseur | CHIBA-PROCEDE-HUILE | CONFIRMÉ | « 熱分解炉で発生したガスは、触媒反応槽を通過して、コンデンサーで凝縮され » | Rapport Chiba, PDF p. 29, imprimé p. 23 | Le rapport confirme l'ordre des équipements, pas la fonction de déchloration du catalyseur. |
| 25 | 1.2.2 | Chlore du PVC transformé en HCl dilué sans dommage au réacteur | Déclaration qualitative | UR2000-JP-P03-P04-CHLORE | CONFIRMÉ | « 塩化ビニールなどより発生する塩素も水蒸気により希塩酸になり釜を傷めることはありません。 » | Brochure URC-2000 japonaise, p. 3 | Nature : constructeur. Aucune mesure d'efficacité, capacité ou durée de vie du catalyseur n'est fournie. |
| 26 | 1.2.3 | Composition du gaz analysé | H2, CH4, C2H6, C2H4, C3H8, C3H6 et CO | KANSO-B2002600 | CONFIRMÉ | « 水素 12.7 % ; メタン 3.2 % ; エタン 0.7 % ; エチレン 0.2 % ; プロパン 0.3 % ; プロピレン 0.3 % ; 一酸化炭素 0.6 % » | Rapport KANSO B2002600, p. 1 | Mesure tierce sur un seul échantillon, installation et charge non identifiées dans l'annexe. |
| 27 | 1.2.3 | Part combustible hors air | 91,4 % | CALC-A2-GAZ-PART-COMBUSTIBLE | CONFIRMÉ | 18,0 / (18,0 + 1,7) = 0,9137 | Rapport KANSO p. 1 ; recalcul | Calcul exact sur l'échantillon après retrait de O2 et N2. |
| 28 | 1.2.3 | PCI calculé du gaz hors air | 37,4 MJ/kg | CALC-A2-GAZ-PCI | CONFIRMÉ | « resultat: 37.386 MJ/kg » | Calculs.yaml, CALC-A2-GAZ-PCI | Formule et calcul cohérents avec la composition KANSO et les données thermochimiques citées. Portée limitée à cet échantillon. |
| 29 | 1.2.3 | Utilisation du combustible récupéré dans chaudière et surchauffeur | Déclaration qualitative | OW-ENG-P02-P14-AFFIRMATIONS | CONFIRMÉ | « This facility uses gasified extracted oil as fuel for the boiler and superheater. » | Brochure OneWorld anglaise, p. 2 | Nature : constructeur. La source parle de « gasified extracted oil », pas clairement du circuit de l'off-gas non condensé. L'annexe signale correctement que le routage reste inconnu. |
| 30 | 1.2.4 | Fonctionnement continu et perte de démarrage | 8 premiers lots sans sortie | OW-ENG-P14-P15-PROCEDE | CONFIRMÉ | « Start-up loss (no off-loading) » ; le tableau fait apparaître une première sortie après le huitième chargement | Brochure OneWorld anglaise, p. 15 | Nature : constructeur. |
| 31 | 1.3 | Huile sur charge riche en résines | 76,5 % de l'entrée | CALC-A2-OW16-HUILE-TOTALE ; OW-ENG-P16-BILAN | CALCUL FAUX | « Gas (Diesel) Oil 61.2 % 62,424ℓ (62.424ton) » ; « Amount of input “one day” 200Mt » | Brochure OneWorld anglaise, p. 16 | 61,2 + 7,65 + 7,65 = 76,5, mais la table est une répartition de produits totalisant 100 % et 102 t. Elle ne permet pas d'affirmer 76,5 % des 200 t d'entrée. Les masses imprimées donnent 78,03 t d'huile, soit 39,0 % de 200 t, ou 65,0 % si l'entrée reconstruite est 120 t. |
| 32 | 1.3 | Bilan annoncé pour déchets ménagers à 10 % de résines | huile 5 % ; char 25 % ; gaz 5 % ; métaux et verre 0 à 5 % | UR2000-JP-P05-BILAN | CONFIRMÉ | « 炭化物 25% ; 混合油 (軽油・重油) 5% ; OFF ガス 5% ; 樹脂系類含有率 10% で試算 » | Brochure URC-2000 japonaise, p. 5 | Nature : constructeur. Les pourcentages sont associés à des volumes en m3 ou litres et 60 à 65 % de l'entrée ne sont pas affectés. Utilisation massique à confirmer. |
| 33 | 1.3, huiles | PCS et chlore des huiles municipales | 45 000 à 46 000 J/g ; 0,137 % et 0,526 % | CHIBA-JLOS-HUILES | CONFIRMÉ | « 塩素分 質量% 0.137 ; 総発熱量（計算） J/g 46000 » | Rapports JLOS, PDF p. 45 et 46 | Mesures tierces. Le pouvoir calorifique supérieur est calculé par le laboratoire. |
| 34 | 1.3, fiches 1.C.b à 1.C.d | Répartition des coupes dans l'huile de la table OneWorld | 80 % gazole ; 10 % heating oil ; 10 % heavy oil | CALC-A1-OW16-PART-GAZOLE ; HEATING ; HEAVY | CONFIRMÉ | 61,2 / 76,5 = 80 % ; 7,65 / 76,5 = 10 % ; 7,65 / 76,5 = 10 % | Brochure OneWorld anglaise, p. 16 ; recalcul | Calculs exacts comme répartition interne des trois lignes d'huile. Ils ne valident pas le rendement global de 76,5 % de l'entrée. |
| 35 | 1.3, char | Facteur calorifique du char de résidus plastiques | 24,6 MJ/kg | CALC-A2-PCI-CHAR-PLASTIQUE | CONFIRMÉ | 5 880 kcal/kg x 4,1868 kJ/kcal / 1 000 = 24,62 MJ/kg | Bilans Chiba et recalcul | Le facteur figure dans le bilan Chiba, mais son origine expérimentale n'est pas donnée. |
| 36 | 1.3, char | Valeur attribuée au char de déchets ménagers | 32 090 J/g | IZUMITEC-R35-339439 ; D-038 | DIFFÉRENT | « INOウレタン炭 ; 発熱量 32090 J/g » | Rapport Izumitec R35-339439, p. 1 | La valeur est bien 32 090 J/g, mais l'échantillon est un char d'uréthane, prélevé par le client. Le rapport ne dit ni « déchets ménagers », ni Urban Rig, ni PCI. L'affectation aux déchets ménagers est une hypothèse de projet, pas une mesure sur ce flux. |
| 37 | 1.3, métaux | Fil d'acier récupéré lors de l'essai pneus | 111 kg sur 450 kg | OWT-DEMO-2020 | CONFIRMÉ | « The weight of each component after pyrolysis was 111 kg of wire » | Rapport constructeur One World Techno, p. 3 | Nature : constructeur. Mesure sur une unité en lots de 4,8 t, pas sur l'URC-2000. |
| 38 | Contrôle HTML / source | Concordance HTML et Markdown du lot 1 | Même texte et mêmes valeurs | ANNEX-01-Process-and-Technology.md | CONFIRMÉ | « 76.5 % of input » ; « measured gas [...] 11.5 % gas » ; « 32,090 J/g for char from household waste, measured on a urethane char » | Markdown, sections correspondantes ; HTML du lot 1 | Aucun écart HTML / source Markdown trouvé. Les erreurs relevées sont donc présentes dans les deux versions. |

## Écarts

### E-1. Preuve du continu à 200 t/j absente

- Annexe : l'introduction dit « Annex 2 proves the performance » et le projet retient l'URC-2000 continu de 200 t/j.
- Source : les essais cités sont l'unité Noda en lots de 20 à 60 kg et l'URT-10 en lots d'environ 100 kg. La capacité de 200 t/j est une déclaration constructeur.
- Gravité : **BLOQUANT** pour présenter la performance industrielle du modèle projeté comme démontrée. Ce n'est pas une preuve d'impossibilité technique.
- Correction proposée : écrire que l'annexe 2 documente les performances d'unités en lots et la plausibilité du procédé, pas la performance de l'URC-2000 continu. Conditionner l'investissement à une référence d'exploitation continue, un essai représentatif ou des garanties contractuelles avec essai de réception.

### E-2. Gaz à 11,5 % présenté comme mesuré et couverture thermique à 2,9 fois

- Annexe : « The measured gas [...] 2.9 times [...] with 11.5 % gas ».
- Source : 11,5 % est une ligne « Recovery Loss » d'une table constructeur incohérente, décrite comme principalement rejetée en fumées. Seule la composition d'un échantillon de gaz a été mesurée, pas sa quantité sur cette charge.
- Gravité : **IMPORTANT**. La plausibilité énergétique reste possible, mais l'autonomie thermique n'est pas démontrée par ce calcul.
- Correction proposée : remplacer par une hypothèse de conception et séparer trois éléments : quantité de gaz à mesurer, composition supposée à partir de KANSO, besoin du brûleur à confirmer.

### E-3. Conclusion réglementaire sur les dioxines trop forte

- Annexe : les résultats sont dits inférieurs à la limite UE de 0,1 ng/Nm3.
- Source : la limite est normalisée à 11 % d'oxygène. Les rapports 2022 et 2023 ne donnent pas l'oxygène de référence.
- Gravité : **IMPORTANT**. Les valeurs sont basses, mais la conformité réglementaire n'est pas encore démontrée.
- Correction proposée : « inférieures numériquement à 0,1 telles que rapportées, avant correction à 11 % O2 ; conformité à confirmer sur rapport final avec O2 ».

### E-4. Rendement d'huile de 76,5 % de l'entrée non établi par la table OneWorld

- Annexe : 76,5 % de l'entrée sur une charge riche en résines.
- Source : les pourcentages de produits totalisent 100 %, les masses totalisent 102 t, l'entrée est affichée à 200 « Mt » avec une densité 0,6.
- Gravité : **IMPORTANT**, car le rendement d'huile influence directement le modèle de revenus et le bilan énergétique.
- Correction proposée : ne conserver 76,5 % que comme répartition imprimée des lignes de la table, avec base indéterminée. Pour le modèle, utiliser un rendement mesuré par flux ou une garantie constructeur explicitant masse humide, masse sèche et densité.

### E-5. Portée du char à 32 090 J/g

- Annexe : valeur utilisée pour le char de déchets ménagers.
- Source : le bulletin porte « INOウレタン炭 », char d'uréthane, sans mention d'Urban Rig, de déchets ménagers, de PCI ou de base sèche.
- Gravité : **IMPORTANT** si cette valeur alimente un débouché ou un bilan énergétique de déchets ménagers.
- Correction proposée : présenter 32 090 J/g comme mesure sur un échantillon de char d'uréthane fourni par OneWorld, puis demander une analyse du char produit avec le flux cible.

### E-6. Capacité nominale dépendante d'un chargement maximal

- Annexe : 48 bennes de 4,17 t donnent 200,16 t/j.
- Source : 4,17 t est explicitement un maximum. La brochure anglaise donne parallèlement 51 bennes de 4,5 m3 et une densité 0,6, soit 137,7 t/j.
- Gravité : **IMPORTANT**. La capacité réelle dépend de la densité, de l'humidité et du taux de remplissage du flux.
- Correction proposée : demander une courbe de capacité garantie par densité apparente, humidité, taille des morceaux et composition, puis retenir le cas prudent dans le modèle.

## Autres interprétations

- **Interprétation la plus favorable sur le continu.** Une ligne de postes fixes peut réduire les pertes de cycles par rapport à un four en lots, et les documents décrivent une architecture cohérente. Cela rend l'extrapolation plausible, mais ne remplace pas une mesure de débit, de disponibilité et de rendement sur la ligne continue.
- **Interprétation la plus favorable de la page 16.** « 200Mt » pourrait être une erreur pour 200 m3. Avec une densité de 0,6, l'entrée reconstruite serait 120 t/j et la somme de 102 t correspondrait à 85 % de cette masse. Cette lecture explique une partie de la table, mais ne permet toujours pas de qualifier 76,5 % comme rendement d'huile de l'entrée.
- **Interprétation la plus favorable sur l'énergie.** Même en abaissant 11,5 % à 9,8 % de 120 t, l'ordre de grandeur énergétique du gaz resterait supérieur au besoin théorique du brûleur. Mais « recovery loss » n'est pas une mesure du gaz récupérable, et le besoin de 833 kcal/s est lui aussi une donnée constructeur.
- **Interprétation la plus favorable sur les dioxines.** Les valeurs brutes sont nettement sous 0,1 et peuvent rester conformes après correction si l'oxygène mesuré n'est pas trop élevé. Sans O2, la conclusion correcte est « possible sous conditions », pas « conforme démontré ».
- **Interprétation la plus favorable du char.** Un char d'uréthane à 32,09 MJ/kg montre qu'un char riche en polymères peut avoir un pouvoir calorifique élevé. Il ne prédit pas le char d'un mélange ménager humide et minéral.

## Manques évidents pour un investisseur

- **BLOQUANT** : preuve d'exploitation ou essai de réception d'une ligne continue représentative, avec débit, disponibilité, rendements massiques et consommations.
- **IMPORTANT** : bilan matière fermé par type de charge, en distinguant masse humide, matière sèche, eau, gaz mesuré, fumées, huile, char, métaux et pertes.
- **IMPORTANT** : domaine de fonctionnement garanti pour humidité, densité apparente, granulométrie, taux d'inertes et teneur en chlore.
- **IMPORTANT** : spécification du catalyseur de déchloration, capacité, durée de vie, régénération, coût de remplacement et filière du catalyseur usé.
- **IMPORTANT** : définition de la pression de service, protection contre la surpression et base de sécurité pour les gaz combustibles. Le détail du pilotage et de la sécurité sera repris au lot 2.
- **IMPORTANT** : analyses des produits et effluents obtenus avec le flux cible, notamment char, métaux, eau et quantité réelle d'off-gas.

## Conclusion en langage simple

- **Passe** : OneWorld décrit bien une gamme de machines, une ligne de réacteurs à températures fixes, un procédé à vapeur surchauffée et plusieurs produits de sortie. Les calculs CALC-A1 de temps de passage et de répartition interne des huiles sont exacts.
- **Ne passe pas en l'état** : dire que la performance de l'URC-2000 continu est prouvée, que 76,5 % de l'entrée devient huile, ou que le cas à 11,5 % de gaz est une mesure démontrant 2,9 fois le besoin du brûleur.
- **Possible sous conditions** : capacité de 200 t/j, autonomie thermique et conformité dioxines, sous réserve d'essais continus, d'un bilan massique cohérent, de mesures corrigées à 11 % O2 et de garanties contractuelles.
- **À mesurer ou confirmer** : rendement continu par flux, quantité et routage du gaz, capacité selon densité et humidité, performance du catalyseur, qualité du char de déchets ménagers.

## Ce qui n'a pas été vérifié dans ce lot

- Les prix, coûts, revenus et débouchés commerciaux, hors périmètre de la vérification légère.
- Les sections 1.4 à 1.6, sauf les renvois nécessaires pour comprendre les réserves du lot 1 ; elles seront vérifiées au lot 2.
- La conformité complète d'un CSR et le statut de sortie de déchet du char ; seul l'ordre de grandeur calorifique a été lu ici.
- Les performances industrielles non présentes dans les pièces du dépôt ; elles ne peuvent pas être déduites des animations ou plans.
- Les pièces finales 2022 et 2023 sur les émissions, car le dossier ne contient que des résultats provisoires ou préliminaires.

## Décompte

- CONFIRMÉ : 33
- DIFFÉRENT : 2
- CALCUL FAUX : 2
- ABSENT : 0
- INACCESSIBLE : 0
- NON SOURCÉ : 0
- Total : 37 verdicts de fond, plus 1 contrôle de concordance HTML / Markdown

