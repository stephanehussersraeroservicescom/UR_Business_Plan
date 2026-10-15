# Annexe 2 : inventaire des preuves (étape 1)

Chat 1 de la v3, 14/10/2026. Auteur : Claude. Statut : **LU** (lu par Claude, pas encore recontrôlé par un second lecteur). Aucune valeur de `working-folder/params/*.yaml` n'a été modifiée.

## 1. Ce qui a été fait

- **Cherché** : tout chiffre sur ce que la machine produit (rendements, huile, gaz, char, émissions, énergie), dans les seuls documents d'origine de `working-folder/reference/preuves/`. L'ancienne annexe 2 (archive) n'a servi qu'à savoir quoi chercher ; rien n'en est repris.
- **Lu** : 29 fichiers ouverts (28 lisibles), toutes les pages. Les pages scannées ou en tableau ont été lues sur image. Pour le japonais, les traductions sont signalées « [trad. Claude] ».
- **Relevés détaillés page par page** (chaque chiffre, avec citation d'origine, unité, conditions et nature) : dossier `releves/` à côté de ce fichier.
  - `releves/chiba-jp-p01-37.md` et `releves/chiba-jp-p38-74.md` : rapport à la préfecture de Chiba, original japonais.
  - `releves/chiba-eng-docx-xlsx.md` : version anglaise, `test data 2.docx` et tableur des résultats.
  - `releves/emissions-gc.md` : émissions, odeurs, dioxines et chromatographie.
  - `releves/huile-char-essais.md` : huile, char et fiches d'essai.
  - `releves/energie-ur2000-divers.md` : énergie, brochure UR2000-JP et documents divers.
  - `releves/presentations-oneworld.md` : présentations OneWorld et proposition AEPW.
- **Contre-lecture personnelle** sur image : les pages PDF 41, 45 et 56 du rapport japonais, le rapport NKKK reproduit p. 17 de la présentation, KANSO p. 2 et Izumitec. Les relevés concordent avec l'image.
- **Fiches** : les entrées de `_evidence.yaml` sont créées ou annotées (section « Inventaire annexe 2 »). Les demandes à OneWorld sont R-009 à R-022 dans `a-rechercher.yaml`.

### Conventions

- **Pages** : numérotation du fichier PDF, sauf mention « impr. » (page imprimée). Dans le rapport japonais de Chiba, page PDF = page imprimée + 6.
- **Nature** :
  - **T** : mesure par un tiers (laboratoire nommé) ;
  - **E** : mesure de l'exploitant, Asada Shokai, avec OneWorld à la conduite ;
  - **C** : déclaration ou mesure de OneWorld, étiquette CONSTRUCTEUR (D-016) ;
  - **?** : émetteur non identifié.
- **Abréviation** : « OW-ENG p. N » désigne la page N de la brochure OneWorld anglaise (`documents-fournis/Urban RIg ENG　.pdf`, mêmes chiffres dans `Urban Rig Recycling Solutions ENG .pdf`).
- **Étiquette** : tous les chiffres ci-dessous sont **LU**. Ceux de nature C portent en plus **CONSTRUCTEUR**. Aucun n'est VÉRIFIÉ.

## 2. Les documents

| ID `_evidence.yaml` | Fichier (sous `reference/preuves/`) | Pages | Émetteur, date | Nature | Utile à l'annexe 2 |
|---|---|---|---|---|---|
| CHIBA-RAPPORT-2023, CHIBA-ESSAIS-FICHES, CHIBA-DISTILLATION, CHIBA-BILANS, CHIBA-SYNTHESE, CHIBA-JLOS-HUILES, CHIBA-OOSUMI-CHAR, CHIBA-OOSUMI-EAUX, CHIBA-OOSUMI-FUMEES, CHIBA-OOSUMI-ODEURS-BRUIT | `tests-independants/prefecture-shiba-test-data-2.pdf` | 74 | 株式会社 朝田商会 (Asada Shokai), lettre au gouverneur de Chiba du 30/01/2023 ; rapport daté 「2022年9月」 ; essais du 02/03 au 30/09/2022, usine de Noda | E pour les essais et bilans ; T pour les rapports de laboratoire joints (p. 45 à 74) | **oui, document central** |
| CHIBA-ENG-2023 | `documents-fournis/Chiba prefecture report ENG.pdf` | 51 | Traduction anglaise, sans traducteur nommé (métadonnées : S. Husser, 02/11/2023) ; ne couvre que les folios 1 à 41 | traduction, **secondaire** | non : 14 divergences avec l'original ; jamais citée (décision D-019) |
| (pas d'ID) | `documents-fournis/test data 2.docx` | | Même texte que le PDF japonais ; images des folios 23 à 68 remplacées par une image vide | copie incomplète | non |
| (pas d'ID) | `documents-fournis/Chiba prefecture tables of pyrolysis results.xlsx` | 10 feuilles | Recopie des fiches (aucune formule) | copie | non |
| (pas d'ID) | `tests-independants/Fuel-Output-Test-22-4-8-22-4-16.pdf` et `...-22-5-26-22-6-21.pdf` | 1 + 1 | Pages imprimées « -15- » et « -16- » : scans des pages impr. 15 et 16 (PDF 21 et 22) du rapport de Chiba, valeurs identiques | copie | non (doublon) |
| CHIBA-AUTORISATION-2022 | `documents-fournis/test report 1.pdf` | 1 | Préfecture de Chiba, 廃第1840号, 02/03/2022, à Asada Shokai | officiel | contexte : essais autorisés du 02/03 au 30/09/2022, 12 000 kg au plus |
| KANSO-B2002600 | `tests-independants/Analysis-Results-Off-gas-Odor-Exhaust.pdf` p. 1 | 1 | KANSOテクノス, 05/12/2020, client OneWorld | T | oui (gaz) |
| KANSO-20002610 | idem p. 2 | 1 | idem | T | oui (fumées) |
| TES-ODEUR-2020 | idem p. 3 | 1 | トータル環境システム, 27/11/2020 | T | oui (odeur) |
| TANABE-2023 | `documents-fournis/Exhaust Gas Concentration - Bad Smell - Dioxins  .pdf` p. 1 à 8 | 8 | タナベ環境工学 (fumées) et エヌ・イー サポート (odeurs), 09 et 10/2023 | T (odeurs : échantillons prélevés par le client) | oui, avec réserve sur l'identité de l'installation |
| DIOXINES-2023 | `documents-fournis/Dioxins .pdf` (= p. 9 à 11 du précédent) | 3 | 環境公害分析センター, 27/10/2023, « 速報 » (préliminaire) | T, provisoire | oui, avec réserve |
| ORIST-GCMS-DRAIN | `tests-independants/gaschromatography.pdf` ; `documents-fournis/20250317183955.pdf` | 6 + 6 | Institut public de recherche industrielle d'Osaka (centre d'Izumi), non daté | T, envoi préliminaire | faible : échantillon « drain » non identifié |
| NKKK-ZPE8004-2019 | `documents-fournis/Urban Rig Recycling Solutions ENG .pdf` p. 17 (reproduction) | 1 | 日本海事検定協会 (NKKK), Osaka, rapport ZPE8004.1/19 du 10/04/2019, client OneWorld | T, mais lu dans une reproduction insérée dans un document du constructeur (**secondaire** au sens de la règle 2) | oui, avec réserve |
| (pas d'ID) | idem p. 17, rapport YTS | 1 | 上海优测, rapport 201406231001, 2014, client tiers chinois | T, aucun lien documenté avec Urban Rig | non |
| IZUMITEC-R35-339439 | `documents-constructeur/Calorie-content-UR-Carbide-1.pdf` | 1 | イズミテック, 30/01/2023, client ワンワールド・ジャパン | T | oui, avec réserve |
| IZUMITEC-R35-339440 | `documents-constructeur/Calorie-content-UR-Carbide-2.pdf` | 1 | idem ; c'est une **huile**, pas un char | T | oui, avec réserve |
| (pas d'ID) | `tests-independants/Recycled-Fuel-test-report.xlsx` (= `documents-fournis/fuel report.xlsx` = `documents-fournis/Recycled Fuel test report .xlsx`) | 1 feuille | Saisie Excel des valeurs NKKK, sans en-tête ni signature (auteur des métadonnées : koki ichimura, 2023) | recopie | non (remplacé par NKKK-ZPE8004-2019) |
| UR2000-JP (existant), UR2000-JP-P05-BILAN, UR2000-JP-P08-SPEC, UR2000-JP-P14-EMISSIONS | `documents-fournis/UR2000-JP.pdf` | 14 | OneWorld, brochure URC-2000 (PDF 2020-05-20) | C | oui |
| OW-ENG-P16-BILAN, OW-ENG-P02-P14-AFFIRMATIONS | `documents-fournis/Urban RIg ENG　.pdf` et `Urban Rig Recycling Solutions ENG .pdf` | 20 + 20 | OneWorld, brochure, « Up date: 1. OCTOBER. 2019 » ; les deux versions ont les mêmes chiffres | C | oui |
| (même contenu que OW-ENG) | `documents-constructeur/Urban Rig Recycling Solutions ENG .pdf` | 20 | Versé par Stéphane le 14/10/2026 en remplacement d'une copie endommagée ; identique (md5) à la version de `documents-fournis/` | C | oui (déjà lu) |
| OW-CONSO-ENERGIE | `bilan-energie/consommation-electrique-et-fuel.pdf` | 1 | « UR Energy Consumption », sans émetteur ni date (scan du 16/01/2024) | ? (à faire attribuer par OneWorld) | oui, avec réserve |
| LUFTHANSA-WS (existant) | `documents-constructeur/Worksheet-Lufthansa-200MT.xlsx` | 2 feuilles | « Peter », 25/01/2024 ; hypothèses commerciales sans mesure | C (hypothèses) | marginal |
| (pas d'ID) | `bilan-energie/energy-balance.xlsx` | 3 feuilles | Recopie par S. Husser (02/11/2023) de la version anglaise de Chiba, erreurs comprises | recopie | non |
| OWT-DEMO-2020 | `documents-constructeur/Urban-Rig-Demo-Operation-Test-Report.pdf` | 3 | One World Techno, essai du 12/12/2020 sur pneus (machine 4,8 t) | C (mesure du constructeur) | oui (seul essai hors plastique) |
| OWJ-DEMO-2021 | `documents-fournis/20231114110656.pdf` | 9 | One World Japan, URT-10, 01 au 03/12/2021, plastiques | C (mesure du constructeur) | oui |
| (pas d'ID) | `documents-fournis/transport installation and maintenance.pdf` | 1 | Sans émetteur ni date | ? | annexe 9 plutôt |
| (pas d'ID) | `documents-fournis/タイAEPW事業提案書英語版.pdf` | 12 | Proposition IGES / OneWorld (vers 2020) | C (facteurs de calcul) | marginal |
| (pas d'ID) | `tests-independants/prefecture-shiba-carbonisation-experiment.pdf` | 3 | En réalité un rapport OneWorld Japan sur des pales en PRV, sans masses (cases « 0kg », « #DIV/0! »), dates contradictoires | C | non (aucun chiffre exploitable) |

Non retenus (hors annexe 2) : SEA CORAL, vidéos, modèle 3D STEP, liste de brevets, `marches-prix/`, `business-plans/`.

## 3. Inventaire des chiffres

### 3.1 Rendements

**a) Essais Asada Shokai, Noda, 2022 : machine Urban Rig en lots (pas l'URC-2000 continue)**

Source : CHIBA-ESSAIS-FICHES, PDF p. 19 à 26 (impr. 13 à 20). Nature E. La machine est décrite p. 7 : 「株式会社ワンワールド社製の、過熱水蒸気分解再生資源回収処理装置「URBAN RIG」」 (installation « URBAN RIG » de récupération de ressources par décomposition à la vapeur surchauffée, fabriquée par OneWorld [trad. Claude]). La p. 4 nomme 「株式会社ワンワールド：熱分解油化装置メーカー/運転管理」 et 「ランドブレイン株式会社：各種測定・分析」.

Définitions de l'exploitant (p. 27) :
- 「オフガス量：投入重量から取出し重量と生成油重量を差し引いた数値。」 : la quantité d'off-gas est la masse entrante moins la masse retirée et la masse d'huile [trad. Claude]. **L'off-gas est donc un calcul par différence, pas une mesure.**
- 「油化率」 : masse d'huile rapportée à la masse entrante, diminuée des métaux et du verre.

Mesure de l'huile (p. 29) : 「ドラム缶で静置分離後に検尺棒を使用して油水量を計量した」. Huile et eau sont jaugées à la pige dans un fût après décantation [trad. Claude]. La masse d'huile semble déduite du volume (anomalie A2).

| Date | Matière (citation) | Entrée kg | Huile kg | Huile L | Retiré kg | Off-gas kg | 油化率 écrit | PDF p. |
|---|---|---|---|---|---|---|---|---|
| 02/03/2022 | PEペレット | 20 | 14,8 | 18 | 0,3 | 4,9 | 74 % | 19 |
| 09/03/2022 | PE成型端材 | 40 | 30,7 | 37 | 0,5 | 8,8 | 77 % | 19 |
| 17/03/2022 | PSペレット | 20 | 12,2 | 14 | 3,8 | 4,0 | 61 % | 20 |
| 31/03/2022 | PS成型端材 | 40 | 22,0 | 25 | 15,3 | 2,7 | 55 % | 20 |
| 08/04/2022 | PPペレット | 20 | 16,2 | 19 | 0,5 | 3,3 | 81 % | 21 |
| 16/04/2022 | PP成型端材 | 50 | 39,8 | 48 | 0,2 | 10,0 | 80 % | 21 |
| 26/05/2022 | ３P成型端材 | 60 | 43,1 | 51 | 5,2 | 11,7 | 72 % | 22 |
| 21/06/2022 | PEポリ缶 | 50 | 40,7 | 47 | 0,8 | 8,4 | 81 % | 22 |
| 28/06/2022 | PPパレット | 50 | 36,5 | 45 | 6,1 | 7,4 | 73 % | 23 |
| 07/07/2022 | PS発泡材 | 50 | 36,3 | 43 | 9,9 | 3,8 | 73 % | 23 |
| 11/07/2022 | ３P成型端材 | 60 | 49,4 | 60 | 9,3 | 1,3 | 82 % | 24 |
| 09 et 22/08/2022 | シュレッダーダスト (résidus de broyage) | 50 et 20 | 「計量不可能」 | 0 | | | « - » | 24, 25 |
| 09/09/2022 | 容器リプラ (plastiques d'emballage de Noda) | 50 | 16,1 | 18 | 24,4 | 9,5 | 41 % | 26 |
| 15/09/2022 | 不燃物残渣 (résidus incombustibles de Noda) | 50 | 22,5 | 26 | 16,7 | 10,8 | 50 % | 26 |

- Les deux essais sur déchets de Noda sont présentés comme 「参考資料」 (document de référence, p. 26). Leur 油化率 est calculé hors métaux.
- Sur la masse entrante totale, le bilan p. 42 donne 32,2 % et 45,0 % (CALCULÉ : 16,1/50 et 22,5/50).
- Pour les résidus de broyage, l'huile était solidifiée : 「生成油の性状が非常に悪く、油化処理には適さない」 (p. 43 : huile de très mauvaise qualité, jugée inadaptée [trad. Claude]).

**b) Bilans matière et énergie, quatre essais** (CHIBA-BILANS, PDF p. 41 et 42, impr. 35 et 36 ; nature E ; contre-lu sur image)

| | 26/05 3P | 11/07 3P | 09/09 容リプラ | 15/09 不燃残渣 |
|---|---|---|---|---|
| Entrée (投入量合計) | 60,0 kg | 60,0 kg | 50,0 kg | 50,0 kg |
| Huile (生成油) | 43,1 kg | 49,4 kg | 16,1 kg | 22,5 kg |
| Char (油化残渣(炭化物)) | 5,2 kg | 9,3 kg | 10,5 kg | 11,3 kg |
| Métaux, corps étrangers | 0,0 | 0,0 | 13,9 kg | 5,4 kg |
| Off-gas | 11,7 kg | 1,3 kg | 9,5 kg | 10,8 kg |
| 物質収支比率 | 100,0 % | 100,0 % | 100,0 % | 100,0 % |

Les bilans bouclent à 100,0 % par construction, puisque l'off-gas est obtenu par différence.

**c) Essais du constructeur**

- **OWJ-DEMO-2021** (URT-10, 01 au 03/12/2021, plastiques PP, PE et PS principalement ; nature C, pesées sur balance).
  - Total p. 8 : 「投入前重量 299.2kg」, 「油重量 248.2kg」, 「油化率 83% オフガス他 13%」, 「残渣率 4%」.
  - Par jour : 70 %, 88 % et 91 % d'huile (p. 2, 5, 8).
  - Le texte lui-même note que l'huile du jour 2 inclut probablement l'off-gas liquéfié du jour 1 : 「1/3日目の気液分離槽オフガスが液化したものも含まれていると想定」 (p. 5).
- **OWT-DEMO-2020** (pneus, machine 4,8 t, 12/12/2020 ; nature C), p. 1 : « 450kg of waste tires » ; « 111 kg of wire, 133 kg of charcoal, and approximately 180 L of oil ». Le bilan ne peut pas être bouclé (huile en volume, sans densité).

**d) Déclarations de OneWorld sur l'URC-2000 continue** (CONSTRUCTEUR)

- UR2000-JP p. 5, sur des ordures ménagères 「樹脂系類含有率 10% で試算」 (calcul avec 10 % de résines) : 「炭化物 25%」, 「混合油 ( 軽油・重油 ) 5% (10,000ℓ ...)」, 「OFF ガス 5% (10,000ℓ ...)」, 「金属類・ガラス ０〜５%」. 60 à 65 % de l'entrée ne sont pas affectés.
- OW-ENG p. 16, entrée « 200Mt Specific gravity : 0.6 », « Resin content rate 90% (unwashed) » :
  - « Gas (Diesel) Oil 61.2 % 62,424ℓ (62.424ton) » ;
  - « Heating Oil 7.65 % » et « Heavy Oil 7.65 % » ;
  - « Recovery Loss 11.5 % » ;
  - « Carbide 5% » ;
  - « water 5% » ;
  - « Metals and glasses etc. 2% » ;
  - « the fuel oil recovery from resin-based waste is about 85% of the input content ».
  - Les masses totalisent 102 t et non 200 t, et 1 L y est compté pour 1 kg (CALCULÉ, voir relevé).
- OW-ENG p. 15 : « 24 hours throughput: 17 units 51 buckets ». UR2000-JP p. 7 : 「24 時間のバケット搬入台数 48 台」, 「MAX 重量 : 4.17 t」.

**e) Non trouvé** : aucune mesure de rendement sur une URC-2000 continue ; aucun essai sur ordures ménagères brutes, papier, bois, déchets alimentaires, PET ou PVC seuls. La seule observation sur le PVC (OWJ-DEMO-2021 p. 8) est : 「塩ビに関しては融点で止まっている」 (le PVC s'est arrêté au stade de la fusion [trad. Claude]).

### 3.2 Qualité de l'huile

| ID, page | Laboratoire, date | Échantillon | Résultats (citation d'origine) | Nature |
|---|---|---|---|---|
| CHIBA-JLOS-HUILES, PDF p. 45 | 一般社団法人 潤滑油協会 (Japan Lubricating Oil Society), n° 20221020-003-03, 31/10/2022 | 「容リプラ生成油」 (huile de l'essai sur emballages de Noda) | 密度（15℃）0.8642 g/cm³ ; 引火点 (P.M.) 「40 未満」 °C ; 動粘度（50℃）1.706 mm²/s ; 流動点 10.0 °C ; 残留炭素分 0.34 % ; 水分 0.13 % ; 灰分 0.002 % ; 硫黄分 「0.05 未満」 % ; 窒素分 0.24 % ; **塩素分 0.137 質量%** ; **総発熱量（計算）46000 J/g** | T |
| CHIBA-JLOS-HUILES, PDF p. 46 | idem, n° 20221020-003-04 | 「残渣プラ生成油」 (résidus incombustibles) | 密度 0.8762 ; 引火点 「40 未満」 ; 動粘度 1.759 ; 硫黄分 0.06 % ; 窒素分 0.43 % ; **塩素分 0.526 %** ; **総発熱量（計算）45000 J/g** | T |
| NKKK-ZPE8004-2019, OW-ENG p. 17 (reproduction) | 日本海事検定協会 大阪理化学分析センター, Report No. ZPE8004.1/19, 平成31年4月10日 (10/04/2019) | 「燃料油」, 「試料提供者 委嘱者」 (fourni par OneWorld, origine non dite) | 引火点 (PMCC) 「40 以下」 ; 動粘度(50℃) 1.11 mm²/s ; 流動点 -20.0 ; 残留炭素分 0.56 ; 水分 0.40 vol % ; 灰分 0.005 ; 硫黄分 0.014 % ; **総発熱量 43,270 J/g (JIS K 2279)** ; **無機塩素分 0.0001 %** (chlore inorganique seulement) | T, secondaire |
| IZUMITEC-R35-339440 | イズミテック, 30/01/2023 | 「INOウレタン油化物」 (huile d'uréthane) | 43 600 J/g, JIS K 2279 ; PCS ou PCI non précisé | T |
| CHIBA-DISTILLATION, PDF p. 34 (impr. 28) | Tableau signé 「㈱朝田商会」 ; aucun laboratoire, aucune méthode, aucune date | huiles de matières vierges, 200 mL | PE : 第一石油類 61 mL (引火点 18 °C, 0.756), reste 139 mL (55 °C, 0.860) ; PP : 56 et 114 mL, soit 30 mL non comptés ; PS : 90 et 110 mL ; 3P : 96 et 104 mL (16 et 52,5 °C ; 0.788 et 0.834) ; soufre de 19,2 à 147,2 ppm | E |
| ORIST-GCMS-DRAIN, p. 4 à 6 | ORIST Izumi, non daté | « drain » (machine, date et matière inconnues) | 71 pics ; principal 「ジメチルヘプテン」 21,26 % d'aire ; 「ウンデセン」 6,52 % ; 「加熱残量 53.7」 % après 5 min à 350 °C | T, préliminaire |
| CHIBA-ESSAIS-FICHES | | huile brute de chaque essai | densités de 0,811 à 0,887 kg/L (fiches) | E |

- **PCI de l'huile : NON TROUVÉ.** Tous les documents donnent un pouvoir calorifique supérieur (総発熱量), mesuré (NKKK) ou calculé (JLOS).
- **Chlore total d'une huile Urban Rig sur déchet réel : 0,137 % et 0,526 % en masse** (JLOS, Noda 2022). Le seul autre chiffre est du chlore **inorganique** (NKKK, échantillon d'origine inconnue).
- OW-ENG p. 17 donne aussi un tableau de synthèse du constructeur : point éclair « 46° », viscosité « 2.28 », « Total chlorine content 100 under ». Ces valeurs viennent du rapport chinois YTS de 2014 (sans lien documenté avec Urban Rig) ou d'aucun des deux rapports. Étiquette CONSTRUCTEUR, à ne pas reprendre comme mesure.

### 3.3 Gaz (off-gas)

- **KANSO-B2002600** (T, p. 1). Échantillon 「過熱水蒸気炭化装置 オフガス」, prélevé le 25/11/2020 sur l'installation d'un 「[masqué]リサイクルセンター」 (pas Asada : site caviardé, deux ans avant les essais de Noda). Méthode 「ガスクロマトグラフ法」, sans norme.
  - Résultats : CO 0.6 %, CH4 3.2 %, CO2 1.7 %, C2H4 0.2 %, C2H6 0.7 %, C3H8 0.3 %, C3H6 0.3 %, H2 12.7 %, O2 12.3 %, N2 65.8 %, H2S 「0.5 ppm未満」.
  - Somme : 97,8 % (CALCULÉ). Rapport N2/O2 : 5,35 (CALCULÉ). L'échantillon est surtout de l'air ou de l'azote ; le document ne dit pas pourquoi.
- **Facteur 1 323,8 kcal/kg** : appliqué à l'off-gas dans les quatre bilans de Chiba (CHIBA-BILANS, PDF p. 41 et 42 ; CALCULÉ : 15 489/11,7). Aucune analyse n'en est donnée. **Ce n'est pas une mesure.**
- **NON TROUVÉ** : masse d'off-gas mesurée, débit, PCI mesuré, composition sans dilution.

### 3.4 Char et résidus

- **IZUMITEC-R35-339439** (T) :
  - 「試料の種類 INOウレタン炭」 (char d'uréthane) ; 「採取者 ご依頼者」 (prélevé par le client) ; 「採取場所 豊橋市豊清町茶屋ノ下154-1」 (Toyohashi) ;
  - résultat : 「発熱量 32090 J/g」, 「JIS M 8814 熱量計法準拠」.
  - Le document ne dit pas que le char vient d'une machine Urban Rig, ni s'il s'agit d'un PCS ou d'un PCI, ni la base (sèche ou brute).
- **Facteur 5 880 kcal/kg** appliqué au char dans les bilans de Chiba (CALCULÉ : 30 576/5,2). Aucune analyse jointe.
- **Métaux dans le char** (CHIBA-OOSUMI-CHAR, PDF p. 47 et 49, T, base brute) :
  - char 容リプラ (n° F22I0007-1) : 「カドミウム 31 mg/kg」, 「鉛 140」, 「ふっ素化合物 130」 ;
  - char 不燃残渣 (n° F22I0079-1) : Cd 36, Pb 42, B 120 mg/kg.
  - Lixiviation p. 48 et 50 : chlorures 1 700 et 440 mg/L.
- **NON TROUVÉ** : PCI du char sur déchet réel, analyse élémentaire (C, H, cendres, Cl).

### 3.5 Émissions

| ID, page | Date, lieu | Laboratoire | Résultats (citation) | Réserves |
|---|---|---|---|---|
| KANSO-20002610, p. 2 | 25/11/2020, 「排出口」 de l'installation caviardée | KANSOテクノス, 計量証明 大阪府 第10212号 | HCl 「1 ppm未満」 (JIS K 0107) ; SOx 「1 ppm未満」 ; NOx 15 ppm ; ダスト 「0.002 g/m³未満」 ; O2 18.5 % | Pas de correction à un O2 de référence ; pas de CO ; installation non identifiée |
| TES-ODEUR-2020, p. 3 | 25 et 26/11/2020 | トータル環境システム | 発生源(排出口) 14 (25) ; limites nord et ouest 「10未満」 | Sous-traitant de KANSO |
| CHIBA-OOSUMI-FUMEES, PDF p. 55 | 09/09/2022, Noda, 容リプラ, four à 350, 450 et 550 °C | 株式会社オオスミ, rapport marqué 「仮 2022/10/18」 (provisoire) | ばいじん 0.003 / 0.002 / 0.003 g/m³ ; 硫黄酸化物 「0.5未満」 ppm ; 窒素酸化物 「10未満」 / 37 / 30 ppm | Provisoire ; pas d'O2 ; point de prélèvement non précisé |
| CHIBA-OOSUMI-FUMEES, PDF p. 56 (contre-lu) | 15/09/2022, Noda, 不燃残渣 | idem, 「仮 2022/10/18」 | ばいじん 0.004 / 0.002 / 0.002 ; SOx 1.4 / 0.78 / 0.78 ppm ; NOx 「10未満」 / 42 / 43 ppm ; **ダイオキシン類（毒性等量）0.067 ng-TEQ/m³** | Provisoire ; une seule valeur de dioxines ; pas d'O2 |
| CHIBA-OOSUMI-FUMEES, PDF p. 57 et 58 | 2022 | idem | Métaux dans les poussières : tous sous la limite, sauf Pb 0.0061 mg/m³ (15/09) | |
| CHIBA-OOSUMI-ODEURS-BRUIT, PDF p. 62 à 74 | 08 et 09/2022, Noda | オオスミ ; 上総環境調査センター | Odeur : limite de site 「10未満」, près de l'exutoire 16, 18 et 19 ; bruit à 1 m de la machine 76 et 77 dB(A) ; limite de site L5 57 à 59 dB(A) | Rapports 0921061-2 et -4 annoncés mais absents |
| TANABE-2023, p. 1 et 5 | 26 et 27/09/2023, 「排気口」, établissement masqué | タナベ環境工学, 計量証明書 環発 第23T271号 et 23T272号 | NOx 30 ppm (deux jours) ; SOx 「0.5 未満」 ; HCN 「0.5 未満」 ; ばいじん < 0,004 et < 0,005 g/m³N ; débit sec 84 et 90 m³N/h | La machine n'est pas nommée ; aucun lien écrit avec Urban Rig |
| TANABE-2023, p. 2 et 6 | idem | エヌ・イー サポート | 臭気指数 24 (濃度 250) et 22 (160) à la sortie | Prélevé par le client (「採取者 依頼者」) |
| DIOXINES-2023, p. 1 | 26 et 27/09/2023 | 環境公害分析センター, sans numéro | 排ガス(9/26) 0.011 ; 排ガス(9/27) 0.025 ng-TEQ/m³ ; 「基準値 0.1」 | « 速報 » (préliminaire) dans la couche texte ; destinataire Land Brain masqué ; pas de méthode ni d'O2 |
| UR2000-JP p. 14 ; OW-ENG p. 12 | non daté | aucun | SOx jusqu'à 「3788 mg/m3」, NOx jusqu'à 「113 mg/m3」 (option PRIMO) | CONSTRUCTEUR ; série « Reduced » plus haute que « Measured » |
| OW-ENG p. 14 ; UR2000-JP p. 3 | | | « Dioxin and CO₂ are not generated » ; 「ダイオキシンなどの有害物は発生しない」 | CONSTRUCTEUR. Contredit par les mesures : 0,067 ng-TEQ/m³ (2022) et 0,011 à 0,025 (2023) ne sont pas nulles |

**Eaux de procédé** (CHIBA-OOSUMI-EAUX, PDF p. 51 à 54, T, eau brute avant traitement) :
- emballages de Noda : フェノール類 740 mg/L, 窒素 520 mg/L, シアン化合物 14 mg/L ;
- résidus incombustibles : 「水素イオン濃度 0.8 pH」, 「生物化学的酸素要求量 16000 mg/l」.

Eau totale rejetée sur la campagne : 「931ℓ」 (p. 44). Pour l'annexe 2 et pour l'ICPE, ce point est absent de l'ancienne annexe.

### 3.6 Énergie

**a) Essais de Chiba** (CHIBA-BILANS, PDF p. 41 et 42, E ; contre-lu sur image)

| | 26/05 | 11/07 | 09/09 | 15/09 |
|---|---|---|---|---|
| 電力 | 65 kWh | 65 kWh | 59 kWh | 65 kWh |
| 軽油 (gazole) | 66 L | 76 L | 61 L | 61 L |
| 水 | 85 L | 95 L | 100 L | 100 L |
| エネルギー収支比率 | 77.4 % | 80.0 % | 40.7 % | 52.5 % |

- Note ※4 (p. 42) : 「軽油の投入量には、ディーゼル発電機の使用量も含まれている。」 Le gazole inclut celui du groupe électrogène diesel [trad. Claude].
- Les énergies sont des volumes multipliés par des facteurs fixes : 860 kcal/kWh, 9 088 kcal/L, 10 980 kcal/kg d'huile, 1 323,8 kcal/kg d'off-gas, 5 880 kcal/kg de char (CALCULÉ à partir des cellules). Le ratio énergétique n'est donc pas une mesure.
- Rapporté à la tonne (CALCULÉ, essai du 26/05) : 65 kWh / 0,060 t = 1 083 kWh/t et 66 L / 0,060 t = 1 100 L/t de gazole.
- **NON TROUVÉ** : durée de chaque essai et température du four.

**b) Déclarations sur l'URC-2000** (CONSTRUCTEUR ou émetteur non identifié)
- UR2000-JP p. 8 : 「消費電力 ( 連続時 ) 20kw/h」 et 「水蒸気生成 蒸気ボイラ / 軽油」.
- UR2000-JP p. 4 : 「過熱バナー 833kcal/s」.
- OW-CONSO-ENERGIE (émetteur inconnu), ligne 200t : « 10,000L/day(200t) » et « 600kW/h » ; test sample « Plastic 15%. Household trash 80%, Stone/Metal/Glass 5% ».
- Les chiffres se contredisent : 20 contre 600 pour l'électricité. Les 10 000 L/jour de fioul consommés égalent les 10 000 L/jour d'huile annoncés comme produits (UR2000-JP p. 5).
- OW-ENG p. 2 : « It is not necessary for fuel for operation except initial startup ». Aucune mesure n'appuie cette affirmation.

## 4. Anomalies principales relevées dans les documents

1. **Off-gas jamais mesuré.** Il est calculé par différence (Chiba, p. 27). Les bilans bouclent mécaniquement. Sur la même matière (3P, 60 kg), il vaut 19 % puis 2 %.
2. **Facteurs énergétiques appliqués, non mesurés.** Off-gas 1 323,8 kcal/kg, char 5 880 kcal/kg, huile 10 980 kcal/kg, gazole 9 088 kcal/L.
3. **Masses de Chiba incohérentes.** 250 kg déclarés pour les essais mono-matière, contre 310 kg d'après les fiches. Huile : 407 L déclarés contre 451 L sur les fiches. Densité du 09/09 : 0,874 écrit, contre 0,894 recalculé.
4. **Contradiction dans la synthèse de Chiba.** La p. 39 affirme une huile ≥ 40 % 「全試験において」 (pour tous les essais), mais le 09/09 donne 32,2 % sur la masse entrante.
5. **Rapports d'émissions provisoires.** Ceux de 2022 sont marqués 「仮」 ; ceux de 2023 (dioxines) sont « 速報 ». Aucune valeur n'est ramenée à un O2 de référence, aucun CO n'est mesuré dans les fumées, et l'installation de 2020 et de 2023 n'est pas identifiable.
6. **Fichiers mal rangés ou mal nommés.**
   - `gaschromatography.pdf` est une GC-MS de liquide, et non l'analyse de gaz B2002600, qui est p. 1 de `Analysis-Results-Off-gas-Odor-Exhaust.pdf`.
   - `Calorie-content-UR-Carbide-2.pdf` porte sur une huile.
   - `prefecture-shiba-carbonisation-experiment.pdf` n'est pas un document de la préfecture.
   - `test report 1.pdf` est une autorisation.
   - Les deux `Fuel-Output-Test` sont des pages du rapport de Chiba.
   - `documents-constructeur/Urban-Rig-Recycling-Solutions-ENG.pdf` était illisible ; Stéphane l'a remplacé le 14/10/2026 par une copie identique à celle de `documents-fournis/`.
7. **Version anglaise de Chiba à ne pas citer.** Dates fausses (2015, 2014), électricité du 09/09 à 65 au lieu de 59 kWh, énergies du 15/09 recopiées du 11/07, SOx en g/Nm³ au lieu de Nm³/h, rapport sur le char des résidus remplacé par un doublon. `energy-balance.xlsx` reproduit ces erreurs.

## 5. Compte rendu (règle 10)

| Sujet | Statut | Source(s) | Ce qui manque |
|---|---|---|---|
| Rendements huile par polymère (PE, PP, PS, 3P) | **Trouvé** (E, lots de 20 à 60 kg) | CHIBA-ESSAIS-FICHES ; OWJ-DEMO-2021 (C) | Mesure tierce ; masse d'huile pesée et non déduite du volume |
| Rendements sur déchets mélangés | **Partiel** : 2 essais de 50 kg (Noda) | CHIBA-BILANS | Composition de l'entrée ; ordures ménagères, DAE, CDG |
| Rendements PET, PVC, organiques, papier, bois | **Non trouvé** | Cherché dans les 29 fichiers | Essais à demander (R-021) |
| Rendements URC-2000 continue | **Non trouvé** (déclarations seulement) | UR2000-JP p. 5 ; OW-ENG p. 16 (C, contradictoires) | Toute mesure (R-009, R-010) |
| Off-gas : masse | **Partiel** (calculée par différence) | CHIBA p. 27, 41, 42 | Mesure directe |
| Off-gas : composition | **Partiel** (un échantillon de 2020, dilué) | KANSO-B2002600 | Échantillon non dilué, site identifié |
| Off-gas : PCI | **Non trouvé** (facteur sans source) | | R-011 |
| Huile : PCS | **Trouvé** (T) | JLOS 46 000 et 45 000 J/g (calculés) ; NKKK 43 270 J/g (mesuré, échantillon d'origine inconnue) | Lien de l'échantillon NKKK avec une machine |
| Huile : PCI | **Non trouvé** | | R-013 |
| Huile : soufre, chlore, densité, point éclair, viscosité | **Trouvé** (T) | CHIBA-JLOS-HUILES ; NKKK-ZPE8004-2019 | Chlore total NKKK |
| Huile : distillation, fractions | **Partiel** (E, sans méthode) | CHIBA-DISTILLATION | Distillation normée ; répartition par zones de l'URC-2000 |
| Char : PCI | **Partiel** (un char d'uréthane, origine non établie) | IZUMITEC-R35-339439 | Char de déchets mélangés, PCS ou PCI, base |
| Char : métaux, lixiviation | **Trouvé** (T) | CHIBA-OOSUMI-CHAR | |
| Émissions : NOx, SOx, poussières | **Trouvé** (T, provisoire ou site non identifié) | KANSO-20002610 ; CHIBA-OOSUMI-FUMEES ; TANABE-2023 | O2 de référence ; rapports définitifs |
| Émissions : HCl | **Partiel** (2020 seulement) | KANSO-20002610 | Mesure sur déchets chlorés |
| Émissions : CO | **Non trouvé** | | R-016 |
| Dioxines | **Partiel** (T, provisoire) | CHIBA-OOSUMI-FUMEES 0,067 ; DIOXINES-2023 0,011 et 0,025 ng-TEQ/m³ | Rapports définitifs, O2, méthode |
| Odeurs, bruit | **Trouvé** (T) | TES-ODEUR-2020 ; CHIBA-OOSUMI-ODEURS-BRUIT ; TANABE-2023 | |
| Eaux de procédé | **Trouvé** (T, eau brute) | CHIBA-OOSUMI-EAUX | Volume par tonne, traitement prévu (R-017) |
| Énergie des essais en lots | **Trouvé** (E, avec facteurs) | CHIBA-BILANS | Durées, températures, part du groupe électrogène |
| Énergie de l'URC-2000 | **Non trouvé** (déclarations contradictoires) | UR2000-JP p. 8 ; OW-CONSO-ENERGIE | R-015 |
| Autonomie énergétique | **Non trouvé** (affirmation seulement) | OW-ENG p. 2 (C) | R-019 |
| Certificat NKKK d'origine | **Partiel** (reproduction lisible dans la brochure) | NKKK-ZPE8004-2019 | Original (R-013) |

## 6. Points à faire contrôler par Stéphane

1. **Chlore de l'huile.** JLOS mesure 0,137 % et 0,526 % sur les huiles de Noda (PDF p. 45 et 46). L'ancienne annexe et `_evidence.yaml` (NKKK-2020) parlent de 1 ppm. C'est l'écart le plus lourd pour la vente de l'huile.
2. **Identité des installations mesurées en 2020 et en 2023.** Les noms sont caviardés. Rien ne relie ces mesures à une machine Urban Rig, sauf le terme 「過熱水蒸気炭化装置」 en 2020.
3. **Origine de l'échantillon NKKK de 2019 et du char d'uréthane d'Izumitec** (Toyohashi).

Réglé le 14/10/2026 (décision D-019) : la brochure anglaise endommagée est remplacée (copie identique à celle de `documents-fournis/`) ; le chemin de GC-B2002600 est corrigé ; la version anglaise du rapport de Chiba n'est jamais citée.
