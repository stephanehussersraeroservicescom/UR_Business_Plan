# Extraction : émissions, odeurs, dioxines, chromatographie (annexe 2, Urban Rig)

Relevé du 2026-10-14. Racine : `working-folder/reference/preuves/`. Méthode : `pdftotext` (vide ou inutilisable pour les pages japonaises : polices Adobe-Japan1 absentes ou scans) puis lecture de chaque page rastérisée (110 dpi, recadrages 200 à 300 dpi pour les numéros, en-têtes et limites de quantification). Tous les chiffres japonais ci-dessous sont donc « (lu sur image) » sauf mention contraire.

Abréviations : LQ = limite de quantification (定量下限値) ; m³N = mètre cube normal.

---

## Document 1 : `tests-independants/Analysis-Results-Off-gas-Odor-Exhaust.pdf`

- Pages : 3 (scan Canon iR-ADV C5540 III, PDF créé le 2020-12-09 selon les métadonnées du fichier).
- Langue : japonais.
- Contient trois rapports distincts :

| Page | Titre exact | Traduction [trad. Claude] | Émetteur / laboratoire | Destinataire | N° de rapport | Date du rapport | Agrément |
|---|---|---|---|---|---|---|---|
| 1 | 分析結果報告書 | Rapport de résultats d'analyse | 株式会社 KANSOテクノス 計量証明事業所 計測分析所 (Kansō Technos, bureau de certification de mesure, laboratoire de mesure et d'analyse, 〒576-0061 大阪府交野市東倉治3丁目1番1号) | 株式会社 ワンワールド 殿 (OneWorld K.K.) | 発行番号 B2002600 | 発行年月日 2020年12月5日 | 計量証明事業登録番号 大阪府 第 10212 号(濃度) ; 環境計量士 [登録番号 第 3414号] 西浦 伸弥 |
| 2 | 分析結果報告書 | Rapport de résultats d'analyse | idem KANSOテクノス | 株式会社 ワンワールド 殿 | 発行番号 20002610 | 2020年12月5日 | idem |
| 3 | 分析結果報告書 | Rapport de résultats d'analyse | 株式会社 トータル環境システム (Total Kankyō System, 大阪市平野区長吉川辺3丁目3番8号), 臭気判定士 山口 隆広 | 株式会社 KANSOテクノス 計測分析所 殿 (donc sous-traitant de KANSO) | aucun numéro visible | 2020年11月27日 | aucun numéro d'agrément visible, seulement la qualité « 臭気判定士 » (opérateur agréé d'olfactométrie) |

- Installation mesurée (identique sur les 3 pages) : « [nom masqué au marqueur noir]産業株式会社 [nom masqué]リサイクルセンター 過熱水蒸気炭化装置 » = « centre de recyclage de la société [masquée], appareil de carbonisation à vapeur surchauffée » [trad. Claude]. Le nom de la société et du centre est caviardé ; il n'est pas lisible de façon fiable (AMBIGU, non transcrit).
- Nature du document : **mesure par un tiers**. Justification : prélèvement (試料採取者) et analyse par 株式会社 KANSOテクノス 計測分析所, laboratoire nommé avec numéro d'enregistrement préfectoral de certification de mesure (p. 1 et 2) ; odeur prélevée et mesurée par 株式会社 トータル環境システム (p. 3).

### Source d'émission mesurée (doc. 1)

| Page | Échantillon (試料名) | Point de prélèvement (採取箇所) | Lecture |
|---|---|---|---|
| 1 | 過熱水蒸気炭化装置 オフガス | « ー » (non renseigné) | « Off-gas » de l'appareil de carbonisation à vapeur surchauffée [trad. Claude]. Le document ne dit pas s'il s'agit du gaz de pyrolyse brut, du gaz après traitement, ou des fumées d'un brûleur. |
| 2 | 過熱水蒸気炭化装置 排ガス | 排出口 (bouche de sortie / point de rejet) | « Gaz d'échappement » de l'appareil [trad. Claude]. Le document ne dit pas s'il s'agit de la cheminée d'un brûleur ou d'un autre exutoire. |
| 3 | 発生源(排出口) ; 敷地境界(北側) ; 敷地境界(西側) | source (bouche de sortie) ; limite de propriété nord ; limite de propriété ouest | Odeur à la source et en limite de site. |

### Tableau des chiffres (doc. 1)

| Page | Grandeur | Valeur | Unité | Citation exacte | Traduction [trad. Claude] | Conditions | Nature |
|---|---|---|---|---|---|---|---|
| 1 | Date de prélèvement | 2020-11-25 | date | 採取年月日 2020年11月25日 | Date de prélèvement 25/11/2020 | prélevé par 株式会社 KANSOテクノス 計測分析所 | mesure par un tiers |
| 1 | Sulfure d'hydrogène (H2S) dans l'off-gas | < 0,5 | ppm | 硫化水素 ガスクロマトグラフ法 0.5 ppm未満 | H2S, chromatographie gazeuse, moins de 0,5 ppm | off-gas, point « ー », 2020-11-25 ; pas de norme JIS citée, seulement « méthode par chromatographie gazeuse » ; base O2, humide/sec : non indiquées | mesure par un tiers (lu sur image) |
| 1 | Monoxyde de carbone (CO) | 0,6 | % | 一酸化炭素 ガスクロマトグラフ法 0.6 % | CO, CG, 0,6 % | idem | idem |
| 1 | Méthane (CH4) | 3,2 | % | メタン ガスクロマトグラフ法 3.2 % | méthane | idem | idem |
| 1 | Dioxyde de carbone (CO2) | 1,7 | % | 二酸化炭素 ガスクロマトグラフ法 1.7 % | CO2 | idem | idem |
| 1 | Éthylène (C2H4) | 0,2 | % | エチレン ガスクロマトグラフ法 0.2 % | éthylène | idem | idem |
| 1 | Éthane (C2H6) | 0,7 | % | エタン ガスクロマトグラフ法 0.7 % | éthane | idem | idem |
| 1 | Propane (C3H8) | 0,3 | % | プロパン ガスクロマトグラフ法 0.3 % | propane | idem | idem |
| 1 | Propylène (C3H6) | 0,3 | % | プロピレン ガスクロマトグラフ法 0.3 % | propylène | idem | idem |
| 1 | Hydrogène (H2) | 12,7 | % | 水素 ガスクロマトグラフ法 12.7 % | hydrogène | idem | idem |
| 1 | Oxygène (O2) | 12,3 | % | 酸素 ガスクロマトグラフ法 12.3 % | oxygène | idem | idem |
| 1 | Azote (N2) | 65,8 | % | 窒素 ガスクロマトグラフ法 65.8 % | azote | idem ; suivi de « 以下余白 » (fin de liste) | idem |
| 2 | Date de prélèvement | 2020-11-25 | date | 採取年月日 2020年11月25日 | 25/11/2020 | prélevé par KANSOテクノス 計測分析所 | mesure par un tiers |
| 2 | Chlorure d'hydrogène (HCl) | < 1 | ppm | 塩化水素濃度 JIS K 0107(2012) 排ガス中の塩化水素分析方法 準拠 イオンクロマトグラフ法による塩化水素及び硫黄酸化物の同時分析方法 1 ppm未満 | HCl, JIS K 0107(2012), chromatographie ionique (analyse simultanée HCl et SOx), moins de 1 ppm | 排ガス, 排出口, 2020-11-25 ; base O2 de correction : non indiquée ; humide/sec : non indiqué | mesure par un tiers (lu sur image) |
| 2 | Oxydes de soufre (SOx) | < 1 | ppm | 硫黄酸化物濃度 JIS K 0103(2011) ... イオンクロマトグラフ法による硫黄酸化物及び塩化水素の同時分析方法 1 ppm未満 | SOx, JIS K 0103(2011), chromatographie ionique, moins de 1 ppm | idem | idem |
| 2 | Oxydes d'azote (NOx) | 15 | ppm | 窒素酸化物濃度 JIS K 0104(2011) 排ガス中の窒素酸化物濃度の測定方法 準拠 自動計測法(化学発光方式) 15 ppm | NOx, JIS K 0104(2011), mesure automatique par chimiluminescence, 15 ppm | idem ; aucune correction O2 indiquée | idem |
| 2 | Poussières | < 0,002 | g/m³ (écrit « g/m³ », sans « N ») | ダスト濃度 JIS Z 8808(2013) 排ガス中のダスト濃度の測定方法 準拠 円形ろ紙法 0.002 g/m³未満 | poussières, JIS Z 8808(2013), méthode du filtre circulaire, moins de 0,002 g/m³ | idem | idem |
| 2 | Oxygène (O2) dans l'échappement | 18,5 | % | 酸素濃度 JIS K 0301(2016) 排ガス中の酸素分析方法 準拠 ガス吸収法(オルザット式) 18.5 % | O2, JIS K 0301(2016), absorption (Orsat), 18,5 % | idem ; c'est la teneur mesurée, aucune valeur de référence O2 n'est appliquée aux résultats | idem |
| 3 | Date de prélèvement (odeur) | 2020-11-25 | date | 試料採取日 2020年11月25日 | date de prélèvement | prélevé par 株式会社 トータル環境システム | mesure par un tiers |
| 3 | Date de mesure (odeur) | 2020-11-26 | date | 測定年月日 2020年11月26日 | date de mesure | idem | idem |
| 3 | Indice d'odeur à la source | 14 | indice (臭気指数) | 発生源(排出口) 14 (25) | source (bouche de sortie) 14 (25) | méthode : 臭気指数及び臭気排出強度の算定の方法 環境庁告示第６３号 平成７年９月１３日 (avis n° 63 de l'Agence de l'environnement du 13/09/1995) | mesure par un tiers (lu sur image) |
| 3 | Concentration d'odeur à la source | 25 | concentration d'odeur (臭気濃度, sans unité) | 14 (25) ; 【備考】表中の（ ）内の数字は、臭気濃度を示す。 | « le nombre entre parenthèses est la concentration d'odeur » | idem | idem |
| 3 | Indice d'odeur limite nord | < 10 (concentration < 10) | indice | 敷地境界(北側) 10未満(10未満) | limite de site nord, moins de 10 | idem | idem |
| 3 | Indice d'odeur limite ouest | < 10 (concentration < 10) | indice | 敷地境界(西側) 10未満(10未満) | limite de site ouest, moins de 10 | idem | idem |

Limites de quantification (doc. 1) : non indiquées en tant que telles ; seules les valeurs « 未満 » (inférieur à) 0,5 ppm H2S, 1 ppm HCl, 1 ppm SOx, 0,002 g/m³ poussières, 10 (odeur) donnent un seuil de rendu.

Non mesuré dans le doc. 1 : CO dans l'échappement (p. 2), dioxines, débit de gaz, température, humidité, teneur en eau des fumées.

### Contrôles (doc. 1)

- Somme des constituants de l'off-gas p. 1 (python) : 0,6 + 3,2 + 1,7 + 0,2 + 0,7 + 0,3 + 0,3 + 12,7 + 12,3 + 65,8 = **97,8 %**. Il manque 2,2 % ; le rapport ne commente pas (argon, eau, hydrocarbures C4+ non analysés ? non indiqué).
- Rapport N2/O2 dans l'off-gas : 65,8 / 12,3 = 5,35 ; dans l'air sec il vaut environ 3,73 (78,08/20,95). Fait relevé sans interprétation ; la présence de 12,3 % d'O2 et 65,8 % de N2 indique que l'échantillon d'« off-gas » contient majoritairement un gaz de type air ou un gaz inerte. Le document ne dit pas s'il y a eu dilution, balayage à l'azote ou entrée d'air.
- Odeur : indice 14 et concentration 25 : 10 × log10(25) = 13,98, cohérent.
- Numérotation : p. 1 « B2002600 », p. 2 « 20002610 » (lus à 300 dpi). Le préfixe « B » sur l'un et pas sur l'autre est relevé tel quel (AMBIGU : préfixe ou caractère « 2 » imprimé différemment ; à l'image, p. 1 montre nettement « B »).

---

## Document 2 : `tests-independants/gaschromatography.pdf`

- Pages : 6. Métadonnées PDF : titre « 20250317183955.pdf », création 2025-03-18 (Adobe Acrobat Pro Paper Capture). Ces métadonnées ne sont pas une date de rapport.
- Langue : anglais (p. 1-2, lettre traduite) et japonais (p. 3-6, tableaux et graphique).
- Titre exact : aucun titre ; p. 1 commence par « Dear Sirs, ».
- Émetteur : « Local Incorporated Administrative Agency Osaka Institute of Industrial Science and Technology / Izumi Center, Osaka Industrial Technology Research Institute / Applied Materials Chemistry Research Department » (p. 2).
- Destinataire : non nommé (« Dear Sirs »).
- Date : **non indiquée** dans le document.
- Numéro de rapport : aucun. Identifiant de fichier d'acquisition sur le chromatogramme : « 081403-Fr-JCE-ドレン-10C6.D » (p. 3, lu à 300 dpi ; ドレン = « drain » [trad. Claude]).
- Accréditation : aucune mentionnée.
- Nature du document : **mesure par un tiers** (institut public de recherche industrielle d'Osaka nommé comme signataire de la lettre, p. 2). Réserve : la lettre est une traduction anglaise non signée et précise que ce n'est pas le rapport officiel (« Note that no chart will be included in the report », p. 2) : c'est un envoi préliminaire de fichiers de travail.

### Ce qui a été analysé (doc. 2)

- **Ce n'est pas une analyse de gaz.** p. 1 : « I am pleased to report the results of the drain analysis » ; l'échantillon est un « drain » (liquide de purge / condensat, ドレン). Il a été chauffé à 350 °C et les volatils analysés (« Analysis chart when heated at 350°C »). Le chromatogramme est un « TIC スキャン » (courant ionique total, balayage), ce qui correspond à une CG couplée à la spectrométrie de masse avec recherche en bibliothèque (« Library search result ») ; le mot « GC-MS » n'est pas écrit.
- Gaz vecteur / diluant : **non indiqué**.
- Point de prélèvement : **non indiqué** (ni machine, ni site, ni date de prélèvement, ni qui a prélevé).
- Machine / site : **non indiqués**.

### Tableau des chiffres (doc. 2)

| Page | Grandeur | Valeur | Unité | Citation exacte | Traduction [trad. Claude] | Conditions | Nature |
|---|---|---|---|---|---|---|---|
| 1 | Température de chauffe de l'échantillon | 350 | °C | « (1) Analysis chart when heated at 350°C » | | échantillon « drain », date et origine non indiquées | mesure par un tiers |
| 1 | Fraction non volatilisée | environ 50 | % | « Incidentally, about 50% remained without volatilization after heating at 350° C for 5 minutes. » | | 350 °C, 5 min | idem |
| 1 | Définition du ratio de pic | 100 | % total | « Peak area ratio (ratio of individual peaks when the total area value is 100) » | | Les pourcentages ci-dessous sont des **ratios d'aire de pic**, pas des % massiques ni volumiques | idem |
| 3 | Chromatogramme | intensité max. du plus grand pic environ 2,4 × 10^7 vers 9,3 min | coups | « + TIC スキャン 081403-Fr-JCE-ドレン-10C6.D » ; axe « カウント vs. 測定時間 (min) » | TIC scan ; « comptes vs temps de mesure (min) » | axe de 8 à 39 min (lu sur image) | idem |
| 6 | Masse du creuset | 20,6505 | g | るつぼ g 20.6505 | creuset | essai de résidu thermique, 350 °C 5 min (selon p. 1, point (3)) | idem (lu sur image) |
| 6 | Creuset + échantillon avant chauffe | 22,3945 | g | 加熱前 g 22.3945 | avant chauffe | idem | idem |
| 6 | Creuset + échantillon après chauffe | 21,5874 | g | 加熱後 g 21.5874 | après chauffe | idem | idem |
| 6 | Masse d'échantillon avant chauffe | 1,744 | g | 加熱前試料量 g 1.744 | quantité d'échantillon avant chauffe | idem | idem |
| 6 | Masse d'échantillon après chauffe | 0,9369 | g | 加熱後試料量 g 0.9369 | après chauffe | idem | idem |
| 6 | Résidu après chauffe | 53,7 | % | 加熱残量 % 53.7 | résidu de chauffe | idem | idem |

Contrôle p. 6 (python) : 22,3945 − 20,6505 = 1,7440 g ; 21,5874 − 20,6505 = 0,9369 g ; 0,9369 / 1,7440 = 53,72 %. Le tableau boucle. Il est cohérent avec « about 50% » de la p. 1.

### Composants (pics) du chromatogramme, p. 4 à 5 (lu sur image, tableaux vérifiés à 200 dpi)

Colonnes d'origine : ピーク (pic) | RT (temps de rétention, min) | 面積 (aire) | 面積比(%) (ratio d'aire, %) | 推定される化合物 (composé estimé : forte concordance avec la bibliothèque) | 可能性のある化合物 (composé possible : faible concordance ; p. 2 : ne sera pas repris dans le rapport officiel).

| Page | Pic | RT (min) | Aire | Ratio d'aire (%) | Composé estimé (citation) | Composé possible (citation) | Traduction [trad. Claude] |
|---|---|---|---|---|---|---|---|
| 4 | 7 | 7.98 | 2.11.E+05 | 0.13 | オクテン | | octène |
| 4 | 8 | 8.15 | 9.76.E+05 | 0.59 | メチルヘプタン | | méthylheptane |
| 4 | 9 | 8.59 | 1.57.E+05 | 0.10 | イソプロピルシクロペンテン | | isopropylcyclopentène |
| 4 | 10 | 8.90 | 4.16.E+05 | 0.25 | テトラメチルシクロペンタン | | tétraméthylcyclopentane |
| 4 | 12 | 9.23 | 7.94.E+05 | 0.48 | トリメチルシクロヘキサン | | triméthylcyclohexane |
| 4 | 13 | 9.33 | 3.50.E+07 | 21.26 | ジメチルヘプテン | | diméthylheptène |
| 4 | 14 | 9.64 | 1.78.E+06 | 1.08 | トリメチルシクロヘキサン | | triméthylcyclohexane |
| 4 | 15 | 9.83 | 1.96.E+05 | 0.12 | トリメチルシクロヘキセン | | triméthylcyclohexène |
| 4 | 16 | 10.22 | 7.61.E+05 | 0.46 | ジメチルオクタン | | diméthyloctane |
| 4 | 17 | 10.53 | 3.44.E+05 | 0.21 | ジメチルオクタジエン | | diméthyloctadiène |
| 4 | 18 | 11.88 | 7.81.E+05 | 0.47 | Si系化合物 | | composé siliconé (à base de Si) |
| 4 | 19 | 11.97 | 4.91.E+05 | 0.30 | 不明 | | inconnu |
| 4 | 20 | 12.18 | 9.31.E+05 | 0.57 | ジメチルオクタン | | diméthyloctane |
| 4 | 21 | 12.25 | 9.99.E+05 | 0.61 | ジメチルオクタン | | diméthyloctane |
| 4 | 22 | 12.98 | 2.99.E+05 | 0.18 | 不明 | | inconnu |
| 4 | 24 | 13.32 | 5.28.E+06 | 3.21 | ジメチルオクテン | | diméthyloctène |
| 4 | 25 | 13.38 | 4.29.E+06 | 2.61 | ジメチルオクテン | | diméthyloctène |
| 4 | 26 | 13.99 | 1.44.E+05 | 0.09 | 不明 | | inconnu |
| 4 | 27 | 14.09 | 5.85.E+05 | 0.36 | 不明 | | inconnu |
| 4 | 30 | 14.43 | 1.81.E+06 | 1.10 | 脂肪族炭化水素 | 不明 | hydrocarbure aliphatique / inconnu |
| 4 | 31 | 14.72 | 6.31.E+05 | 0.38 | 脂肪族炭化水素 | | hydrocarbure aliphatique |
| 4 | 32 | 14.94 | 4.07.E+05 | 0.25 | | テトラメチルシクロヘキサン | (possible) tétraméthylcyclohexane |
| 4 | 33 | 15.32 | 3.94.E+05 | 0.24 | | テトラメチルシクロヘキサン | (possible) tétraméthylcyclohexane |
| 4 | 36 | 15.72 | 3.38.E+05 | 0.21 | | テトラメチルデカン | (possible) tétraméthyldécane |
| 4 | 37 | 15.84 | 2.19.E+05 | 0.13 | 脂肪族炭化水素 | | hydrocarbure aliphatique |
| 4 | 39 | 16.39 | 2.95.E+05 | 0.18 | | メチルウンデカチオール | (possible) méthylundécanethiol |
| 4 | 40 | 16.72 | 1.25.E+07 | 7.60 | | トリデセン | (possible) tridécène |
| 4 | 41 | 16.83 | 6.52.E+06 | 3.97 | | トリメチルノネン | (possible) triméthylnonène |
| 4 | 42 | 16.96 | 1.07.E+07 | 6.52 | ウンデセン | | undécène |
| 4 | 44 | 17.68 | 1.80.E+06 | 1.10 | 脂肪族炭化水素 | | hydrocarbure aliphatique |
| 4 | 58 | 19.56 | 2.88.E+06 | 1.75 | | トリメチルノネン | (possible) triméthylnonène |
| 4 | 59 | 19.67 | 1.89.E+06 | 1.15 | | トリメチルノネン | (possible) triméthylnonène |
| 4 | 60 | 19.76 | 1.16.E+06 | 0.70 | | トリメチルノネン | (possible) triméthylnonène |
| 4 | 61 | 19.89 | 2.40.E+06 | 1.46 | | トリメチルノネン | (possible) triméthylnonène |
| 4 | 62 | 20.02 | 1.10.E+06 | 0.67 | | トリデセン | (possible) tridécène |
| 4 | 63 | 20.10 | 3.04.E+05 | 0.18 | | トリデセン | (possible) tridécène |
| 4 | 65 | 20.52 | 3.05.E+05 | 0.19 | 不明 | | inconnu |
| 5 | 67 | 20.72 | 6.13.E+05 | 0.37 | 不明 | | inconnu |
| 5 | 72 | 21.81 | 2.83.E+05 | 0.17 | 不明 | | inconnu |
| 5 | 74 | 22.05 | 4.00.E+06 | 2.44 | | アリルシュウ酸ヘキサデシル | (possible) oxalate d'allyle et d'hexadécyle |
| 5 | 75 | 22.14 | 1.16.E+06 | 0.71 | 脂肪族炭化水素 | | hydrocarbure aliphatique |
| 5 | 76 | 22.22 | 1.09.E+06 | 0.66 | 脂肪族炭化水素 | | hydrocarbure aliphatique |
| 5 | 77 | 22.34 | 5.67.E+06 | 3.45 | | アリルシュウヘキサデシル | (possible) « oxal(ate) d'allyle hexadécyle », graphie tronquée dans l'original |
| 5 | 78 | 22.43 | 1.16.E+06 | 0.71 | 不明 | | inconnu |
| 5 | 79 | 22.56 | 1.08.E+06 | 0.66 | 不明 | | inconnu |
| 5 | 80 | 22.69 | 2.10.E+06 | 1.28 | メチルオクタデセン | | méthyloctadécène |
| 5 | 81 | 22.82 | 2.50.E+06 | 1.52 | | 長鎖アルコール | (possible) alcool à longue chaîne |
| 5 | 82 | 23.10 | 6.88.E+05 | 0.42 | | メチルウンデセン | (possible) méthylundécène |
| 5 | 83 | 24.25 | 2.05.E+06 | 1.25 | 脂肪族炭化水素 | | hydrocarbure aliphatique |
| 5 | 86 | 24.49 | 1.61.E+06 | 0.98 | | アリルシュウオクタデシル | (possible) « oxal(ate) d'allyle octadécyle » |
| 5 | 90 | 24.96 | 2.20.E+06 | 1.34 | 不明 | | inconnu |
| 5 | 92 | 25.19 | 7.57.E+05 | 0.46 | | メチルウンデセン | (possible) méthylundécène |
| 5 | 94 | 26.03 | 2.70.E+05 | 0.16 | | トリメチルオクタデシルシクロヘキサン | (possible) triméthyloctadécylcyclohexane |
| 5 | 96 | 26.23 | 2.10.E+06 | 1.28 | | トリデセン | (possible) tridécène |
| 5 | 99 | 26.44 | 2.03.E+06 | 1.24 | | アリルシュウオクタデシル | (possible) « oxal(ate) d'allyle octadécyle » |
| 5 | 100 | 26.53 | 1.57.E+06 | 0.96 | | 長鎖アルコール | (possible) alcool à longue chaîne |
| 5 | 101 | 26.64 | 1.29.E+06 | 0.78 | | 長鎖アルコール | (possible) alcool à longue chaîne |
| 5 | 104 | 26.89 | 4.13.E+06 | 2.51 | | メチルオクタデセン | (possible) méthyloctadécène |
| 5 | 105 | 27.08 | 8.17.E+05 | 0.50 | 不明 | | inconnu |
| 5 | 106 | 27.14 | 8.95.E+05 | 0.54 | 不明 | | inconnu |
| 5 | 107 | 27.84 | 4.07.E+05 | 0.25 | 不明 | | inconnu |
| 5 | 108 | 28.03 | 2.11.E+06 | 1.28 | | 長鎖アルコール | (possible) alcool à longue chaîne |
| 5 | 110 | 28.65 | 4.37.E+06 | 2.66 | | 長鎖アルコール | (possible) alcool à longue chaîne |
| 5 | 112 | 29.78 | 2.16.E+06 | 1.31 | 不明 | | inconnu |
| 5 | 116 | 30.63 | 7.39.E+05 | 0.45 | | トリメチルオクタデシルシクロヘキサン | (possible) triméthyloctadécylcyclohexane |
| 5 | 118 | 31.70 | 1.47.E+06 | 0.89 | 不明 | | inconnu |
| 5 | 119 | 32.49 | 4.56.E+06 | 2.77 | 不明 | | inconnu |
| 5 | 120 | 32.71 | 8.47.E+05 | 0.52 | | トリメチルオクタデシルシクロヘキサン | (possible) triméthyloctadécylcyclohexane |
| 5 | 122 | 34.03 | 1.22.E+06 | 0.74 | 脂肪族炭化水素 | | hydrocarbure aliphatique |
| 5 | 125 | 35.05 | 3.86.E+06 | 2.35 | 不明 | | inconnu |
| 5 | 128 | 38.46 | 2.55.E+06 | 1.55 | 不明 | | inconnu |
| 5 | Total | | 1.64.E+08 | 100 | | | total |

Contrôles (python) :
- 71 pics listés ; somme des ratios = **100,02 %** (arrondis), cohérente avec « 100 ».
- Pic 13 : 3,50E+07 / 1,64E+08 = 21,34 % contre 21,26 % écrit : écart dû à l'arrondi de l'aire à 3 chiffres, cohérent.
- Les numéros de pics sautent (1-6, 11, 23, 28-29, 34-35, 38, 43, 45-57, etc. absents) : le tableau ne liste qu'une sélection de pics, mais le total vaut 100 %. Le document n'explique pas ce choix.

---

## Document 3 : `documents-fournis/Dioxins .pdf`

- Pages : 3. Métadonnées : créé le 2023-10-27 (pdf_as / 3-Heights). Fichier texte natif (non scanné) pour p. 1-2 ; p. 3 : libellés japonais non extraits (polices absentes), seulement les nombres.
- Langue : japonais.
- Titre exact : pas de titre de document ; objet : « 工事件名 廃プラスチック油化実証施設 排ガス中のダイオキシン類測定 » = « Objet : mesure des dioxines dans les gaz d'échappement de l'installation de démonstration de conversion des déchets plastiques en huile » [trad. Claude].
- Émetteur / laboratoire : 株式会社 環境公害分析センター (Kankyō Kōgai Bunseki Center), 〒321-0911 栃木県宇都宮市問屋町3172-85, TEL 028-601-8835, 担当：菅原 (responsable : Sugawara).
- Destinataire : sur l'image, le champ « 報告書宛名 » est vide (texte effacé ou masqué en blanc). **La couche texte du PDF contient encore** : « 速報 » (rapport préliminaire / flash [trad. Claude]), « ランドブレイン 株式会社 山崎 様 » et « 報告書宛名 ランドブレイン 株式会社 様 » (Land Brain K.K., M. Yamazaki). Ces mentions ne sont pas visibles sur le rendu de la page.
- Date : 2023年10月27日.
- Numéro de rapport : **aucun**.
- Accréditation : aucun numéro d'enregistrement de certification de mesure, aucun signataire environnemental (環境計量士) ni sceau visible.
- Nature du document : **mesure par un tiers** (laboratoire nommé, en-tête du laboratoire), avec réserve : le document est une lettre d'envoi de résultats « 速報 » (préliminaire, selon la couche texte), pas un certificat de mesure (計量証明書) ; pas de méthode, pas de norme (ex. JIS K 0311), pas de détail par congénère.

### Tableau des chiffres (doc. 3)

| Page | Grandeur | Valeur | Unité | Citation exacte | Traduction [trad. Claude] | Conditions | Nature |
|---|---|---|---|---|---|---|---|
| 1 | Dioxines, échantillon du 26/09 | 0,011 | ng-TEQ/m³ | 排ガス(9/26) 0.1 0.011 基準値以下 | gaz d'échappement (26/09) : valeur de référence 0,1 ; résultat 0,011 ; « inférieur à la valeur de référence » | 試料種 排ガス ; année non écrite dans la ligne (9/26), lettre datée du 27/10/2023 ; point de prélèvement, base O2 (12 % ou autre), humide/sec, norme, LQ : **non indiqués** ; unité écrite « m³ » sans « N » | mesure par un tiers (lu sur image et couche texte) |
| 1 | Dioxines, échantillon du 27/09 | 0,025 | ng-TEQ/m³ | 排ガス(9/27) 0.1 0.025 基準値以下 | idem (27/09) : résultat 0,025 | idem | idem |
| 1 | Valeur de référence utilisée | 0,1 | ng-TEQ/m³ | 基準値 ng-TEQ/㎥ 0.1 | valeur de référence (norme) | la base réglementaire de ce 0,1 n'est pas citée sur la page | déclaration du laboratoire |
| 1 | Nombre de feuilles | 3 | feuilles | 計 3 枚 (本書含む) | total 3 feuilles (y compris celle-ci) | | |
| 2 | Nombre de congénères | 75 / 135 / 12 | nombre | さらに、PCDDsは75種類、PCDFsは135種類、DL-PCBsは12種類も仲間があります。 | 75 PCDD, 135 PCDF, 12 PCB de type dioxine | texte pédagogique (添付資料 « Annexe : à propos des dioxines »), pas une mesure | rien d'utile pour la machine |
| 3 | Tableau de valeurs de référence | 0.6pg-TEQ m³ ; 1pg-TEQ l ; 150pg-TEQ g ; 1,000pg-TEQ g | | (couche texte, libellés japonais absents) | AMBIGU : les libellés des lignes ne sont pas extraits ni visibles sur l'image ; les valeurs correspondent par leur forme à des normes environnementales (air, eau, sol...) mais le document lisible ne le dit pas | | non-mesure |
| 3 | Tableau de normes d'émission | 0.1 / 0.5 / 1 / 1 / 0.1 / 1 / 5 ; 2 / 20 / 40 / 20 / 80 ; 1 / 5 / 10 / 5 / 1 / 5 / 10 | ng-TEQ/m³N | colonnes « H12.1 », « H13.1 H14.11 », « H14.12 » ; capacités « 1t/h », « 1000KVA », « 0.5t/h », « 4t/h », « 2 4t/h », « 2t/h », « 50kg/h », « 0.5 », « 1t » ; notes « 12 », « 15 » | AMBIGU : libellés japonais absents (polices non incorporées). Colonnes datées en ère Heisei (H12 = 2000 à H14 = 2002) ; le tableau a l'apparence d'un barème réglementaire par type et taille d'installation, sans libellés lisibles | | non-mesure |

---

## Document 4 : `documents-fournis/Exhaust Gas Concentration - Bad Smell - Dioxins  .pdf`

- Pages : 11. Métadonnées : assemblé avec iLovePDF le 2023-11-27.
- Langue : japonais.
- Composition : 4 rapports de laboratoire (p. 1 à 8) + **une copie des 3 pages du doc. 3** (p. 9 à 11).
- Site / installation : partout, le nom de l'établissement (事業所名又は工場名) et le lieu de prélèvement (採取場所・住所) sont **masqués en blanc** sur l'image ; aucune couche texte sous les p. 1 à 8 (scans). Sur p. 9 : « 廃プラスチック油化実証施設 » (installation de démonstration de liquéfaction des déchets plastiques).
- Machine : non nommée (ni UR, ni URC-2000, ni OneWorld dans les pages 1 à 11).

| Pages | Titre exact | Traduction [trad. Claude] | Laboratoire | N° | Date du rapport | Prélèvement | Agrément |
|---|---|---|---|---|---|---|---|
| 1 | 計量証明書 | Certificat de mesure | タナベ環境工学株式会社 (Tanabe Kankyō Kōgaku), 大分県大分市高江西一丁目4323番地の4 ; 代表取締役 藤澤 剛 ; 環境計量士 庄 澄人 | 環発 第23T271号 | 令和 5年10月25日 (2023-10-25) | 令和 5年 9月26日 (10:07 ～ 12:30) | 濃度計量証明事業所 大分県知事登録77号 ; 音圧レベル 78号 ; 振動加速度レベル 107号 |
| 2 | 臭気判定試験結果書 | Résultat d'essai de détermination d'odeur | 株式会社 エヌ・イー サポート 九州支社 (N.E. Support, agence Kyūshū, Fukuoka) ; 臭気判定士 伊与田 侑紀 | No. f23010121 | 令和5年10月2日 (2023-10-02) | 令和5年9月26日 13時28分 ; 採取者 : 依頼者 | aucun numéro sur cette page |
| 3-4 | 濃度計量証明書 (1/2, 2/2) | Certificat de mesure de concentration | 株式会社 エヌ・イー サポート (siège Hiroshima ; 事業所 九州支社) ; 環境計量士 西 敏広 | No. F23010006 | 令和 5年 10月 13日 (2023-10-13) | 令和5年9月26日 12時41分 ; 採取者 : 依頼者 ; demande du 令和5年9月29日 | 計量証明登録番号 (広島県)第K-9号 ; 計量士登録番号 3552 ; pour l'ammoniac (※) : 計量証明登録番号(濃度)第37号, 環境計量士 伊与田 侑紀, 計量士登録番号第9702号 |
| 5 | 計量証明書 | Certificat de mesure | タナベ環境工学株式会社 | 環発 第23T272号 | 令和 5年10月25日 | 令和 5年 9月27日 (10:03 ～ 12:21) | idem p. 1 |
| 6 | 臭気判定試験結果書 | Résultat d'essai d'odeur | エヌ・イー サポート 九州支社 | No. f23010122 | 令和5年10月2日 | 令和5年9月27日 13時35分 ; 採取者 : 依頼者 | |
| 7-8 | 濃度計量証明書 (1/2, 2/2) | Certificat de concentration | エヌ・イー サポート | No. F23010007 | 令和 5年 10月 13日 | 令和5年9月27日 12時40分 ; 採取者 : 依頼者 | idem p. 3 |
| 9-11 | (copie du doc. 3) | | 株式会社 環境公害分析センター | aucun | 2023年10月27日 | 9/26 et 9/27 | aucun |

- Nature du document : **mesure par un tiers** pour p. 1 et 5 (certificats Tanabe avec enregistrement préfectoral). Pour p. 2-4 et 6-8 : **analyse par un tiers sur échantillons prélevés par le client** : « 採取者 依頼者 » = « préleveur : le demandeur » [trad. Claude]. Le laboratoire n'a donc pas prélevé lui-même les échantillons d'odeur. p. 9-11 : voir doc. 3.

### Source d'émission mesurée (doc. 4)

- p. 1 et 5 : « 貴依頼によるばい煙発生施設に係るばい煙量等の計量結果 » = « résultats de mesure des fumées d'une installation génératrice de fumées (ばい煙発生施設) à votre demande » [trad. Claude] ; 施設番号 « ー » ; 測定箇所 « 排気口 » (bouche d'échappement) ; 燃原料使用状況 « 通常 » (utilisation de combustible/matière : normale). Le terme « ばい煙発生施設 » désigne au Japon une installation de combustion soumise à la loi sur la pollution de l'air, mais le document ne précise pas s'il s'agit du brûleur du réacteur, d'une torchère, ou d'un autre équipement. **Non indiqué : brûleur ou gaz de pyrolyse.**
- p. 2 et 6 : « 試験対象 排出口試料 » = échantillon à la bouche de sortie.
- p. 3-4, 7-8 : 試料名 « 悪臭 » (mauvaise odeur) ; lieu masqué.

### Tableau des chiffres (doc. 4)

| Page | Grandeur | Valeur | Unité | Citation exacte | Traduction [trad. Claude] | Conditions | Nature |
|---|---|---|---|---|---|---|---|
| 1 | Débit de gaz sec | 84 | m³N/h | 排出ガス量 (㎥N/h) (乾き) 84 | débit de gaz émis (sec) 84 m³N/h | 2023-09-26, 10:07-12:30, 排気口 | mesure par un tiers (lu sur image) |
| 1 | Poussières (ばいじん) | < 0,004 | g/m³N | ばいじん濃度 g/㎥N 0.004 未満 JIS Z 8808 (円筒ろ紙法) | poussières < 0,004 g/m³N, JIS Z 8808, filtre cylindrique | idem ; base O2 : non indiquée ; humide/sec : non indiqué pour la concentration (débit en sec) ; O2 non mesuré | idem |
| 1 | Oxydes de soufre | < 0,5 | ppm | 硫黄酸化物量 ppm 0.5 未満 JIS K 0103 (イオンクロマトグラフ法 附属書4に規定) | SOx < 0,5 ppm, JIS K 0103, chromatographie ionique (annexe 4) | idem ; noter « 量 » (quantité) dans le libellé mais unité ppm | idem |
| 1 | Oxydes d'azote | 30 | ppm | 窒素酸化物濃度 ppm 30 JIS K 0104 (化学発光法 JIS B 7982に規定) | NOx 30 ppm, chimiluminescence (JIS B 7982) | idem ; pas de correction O2 indiquée | idem |
| 1 | Cyanure d'hydrogène (HCN) | < 0,5 | ppm | シアン化水素濃度 ppm 0.5 未満 JIS K 0109 (PCP吸光光度法) | HCN < 0,5 ppm, spectrophotométrie PCP | idem | idem |
| 5 | Débit de gaz sec | 90 | m³N/h | 排出ガス量 (㎥N/h) (乾き) 90 | | 2023-09-27, 10:03-12:21, 排気口 | idem |
| 5 | Poussières | < 0,005 | g/m³N | ばいじん濃度 g/㎥N 0.005 未満 JIS Z 8808 | | idem | idem |
| 5 | SOx | < 0,5 | ppm | 硫黄酸化物量 ppm 0.5 未満 JIS K 0103 | | idem | idem |
| 5 | NOx | 30 | ppm | 窒素酸化物濃度 ppm 30 JIS K 0104 | | idem | idem |
| 5 | HCN | < 0,5 | ppm | シアン化水素濃度 ppm 0.5 未満 JIS K 0109 | | idem | idem |
| 2 | Seuil des panélistes A à F | 2.74 ; 2.24 ; 2.24 ; 2.24 ; 3.24 ; 2.24 | log10 dilution | パネルの閾値 A 2.74 / B 2.24 カット / C 2.24 / D 2.24 / E 3.24 カット / F 2.24 | seuil de panel ; B et E écartés (« カット », coupe haut/bas) | dilutions 30/100/300/1000/3000 (log 1.48/2.00/2.48/3.00/3.48) ; prélèvement 2023-09-26 13:28 par le demandeur ; méthode 平成7年9月13日 環境庁告示第63号 | analyse par un tiers |
| 2 | Moyenne des seuils | 2,37 | log | X = (2.74+2.24+2.24+2.24) / 4 = 2.37 | | | idem |
| 2 | Indice d'odeur calculé | 23,7 | | Y = 2.37×10= 23.7 | | | idem |
| 2 | Concentration d'odeur | 250 | (sans unité) | 判定 臭気濃度 250 | jugement : concentration d'odeur 250 | à la bouche de sortie, 26/09/2023 | idem |
| 2 | Indice d'odeur | 24 | | 臭気指数 24 | indice d'odeur 24 | idem | idem |
| 6 | Seuils panélistes | A 2.24 カット ; B 2.24 ; C 2.24 ; D 2.24 ; E 2.74 カット ; F 2.24 | log | | | 2023-09-27 13:35, demandeur | idem |
| 6 | Moyenne | 2,24 | log | X = (2.24+2.24+2.24+2.24) / 4 = 2.24 | | | idem |
| 6 | Indice calculé | 22,4 | | Y = 2.24×10= 22.4 | | | idem |
| 6 | Concentration d'odeur | 160 | | 臭気濃度 160 | | 27/09/2023 | idem |
| 6 | Indice d'odeur | 22 | | 臭気指数 22 | | | idem |
| 3 | Ammoniac | 0,4 | ppm | ※アンモニア(ppm) 0.4 定量下限値 0.1 S47環告9号別表1 | ammoniac 0,4 ppm, LQ 0,1 ppm | prélevé 2023-09-26 12:41 par le demandeur ; méthode : 特定悪臭物質の測定の方法 (昭和47年5月30日環境庁告示第9号) ; air 30,0 °C, humidité 65 %, vent nord-ouest 2,0 m/s | analyse par un tiers (lu sur image, 250 dpi) |
| 3 | Méthylmercaptan | < LQ (0,0002) | ppm | メチルメルカプタン(ppm) 定量下限値未満 0.0002 S47環告9号別表2 | inférieur à la LQ | idem | idem |
| 3 | Sulfure d'hydrogène | < LQ (0,001) | ppm | 硫化水素(ppm) 定量下限値未満 0.001 別表2 | | idem | idem |
| 3 | Sulfure de méthyle | < LQ (0,001) | ppm | 硫化メチル(ppm) 定量下限値未満 0.001 別表2 | | idem | idem |
| 3 | Disulfure de méthyle | < LQ (0,001) | ppm | 二硫化メチル(ppm) 定量下限値未満 0.001 別表2 | | idem | idem |
| 3 | Triméthylamine | < LQ (0,001) | ppm | トリメチルアミン(ppm) 定量下限値未満 0.001 別表3 | | idem | idem |
| 3 | Acétaldéhyde | < LQ (0,001) | ppm | アセトアルデヒド(ppm) 定量下限値未満 0.001 別表4 | | idem | idem |
| 3 | Propionaldéhyde | < LQ (0,005) | ppm | プロピオンアルデヒド(ppm) 定量下限値未満 0.005 別表4 | | idem | idem |
| 3 | n-Butyraldéhyde | < LQ (0,0009) | ppm | ノルマルブチルアルデヒド(ppm) 定量下限値未満 0.0009 別表4 | | idem | idem |
| 3 | Isobutyraldéhyde | < LQ (0,002) | ppm | イソブチルアルデヒド(ppm) 定量下限値未満 0.002 別表4 | | idem | idem |
| 3 | n-Valéraldéhyde | < LQ (0,0009) | ppm | ノルマルバレルアルデヒド(ppm) 定量下限値未満 0.0009 別表4 | | idem | idem |
| 3 | Isovaléraldéhyde | < LQ (0,0003) | ppm | イソバレルアルデヒド(ppm) 定量下限値未満 0.0003 別表4 | | idem | idem |
| 3 | Isobutanol | < LQ (0,09) | ppm | イソブタノール(ppm) 定量下限値未満 0.09 別表5 | | idem | idem |
| 3 | Acétate d'éthyle | < LQ (0,3) | ppm | 酢酸エチル(ppm) 定量下限値未満 0.3 別表6 | | idem | idem |
| 3 | Méthylisobutylcétone | < LQ (0,1) | ppm | メチルイソブチルケトン(ppm) 定量下限値未満 0.1 別表6 | | idem | idem |
| 3 | Toluène | < LQ (1) | ppm | トルエン(ppm) 定量下限値未満 1 別表7 | | idem | idem |
| 3 | Styrène | < LQ (0,01) | ppm | スチレン(ppm) 定量下限値未満 0.01 別表7 | | idem | idem |
| 3 | Xylène | < LQ (0,1) | ppm | キシレン(ppm) 定量下限値未満 0.1 別表7 | | idem | idem |
| 3 | Acide propionique | < LQ (0,002) | ppm | プロピオン酸(ppm) 定量下限値未満 0.002 別表8 | | idem | idem |
| 3 | Acide n-butyrique | < LQ (0,0002) | ppm | ノルマル酪酸(ppm) 定量下限値未満 0.0002 別表8 | | idem | idem |
| 4 | Acide n-valérique | < LQ (0,0002) | ppm | ノルマル吉草酸(ppm) 定量下限値未満 0.0002 S47環告9号別表8 | | idem (feuille 2/2 du F23010006) | idem |
| 4 | Acide isovalérique | < LQ (0,0002) | ppm | イソ吉草酸(ppm) 定量下限値未満 0.0002 別表8 ; 以下余白 | | idem | idem |
| 7 | Ammoniac | 0,3 | ppm | ※アンモニア(ppm) 0.3 定量下限値 0.1 | | prélevé 2023-09-27 12:40 par le demandeur ; air 31,0 °C, humidité 68 %, vent nord-ouest 2,3 m/s | idem |
| 7 | 19 autres substances (mêmes que p. 3) | toutes < LQ | ppm | 定量下限値未満 (LQ identiques à la p. 3 : 0.0002, 0.001 ×5, 0.005, 0.0009, 0.002, 0.0009, 0.0003, 0.09, 0.3, 0.1, 1, 0.01, 0.1, 0.002, 0.0002) | | idem | idem |
| 8 | Acide n-valérique, acide isovalérique | < LQ (0,0002 chacun) | ppm | ノルマル吉草酸 / イソ吉草酸 定量下限値未満 0.0002 | | F23010007 feuille 2/2 | idem |
| 9 | Dioxines 26/09 et 27/09 | 0,011 et 0,025 | ng-TEQ/m³ | voir doc. 3 p. 1 | | | voir doc. 3 |
| 10-11 | voir doc. 3 p. 2-3 | | | | | | rien d'utile (annexe explicative et barème) |

### Contrôles (doc. 4)

- Odeur p. 2 : moyenne (2,74+2,24+2,24+2,24)/4 = 2,365, arrondi 2,37 ; indice 23,7 arrondi 24 ; 10^(24/10) = 251, rendu 250 : cohérent.
- Odeur p. 6 : moyenne 2,24 ; indice 22,4 arrondi 22 ; 10^(22/10) = 158, rendu 160 : cohérent.
- Panel p. 2 : le panéliste B (2,24) est écarté alors que C, D, F ont la même valeur ; la règle d'écartement (plus haute et plus basse) le permet, aucune anomalie de calcul.
- Les concentrations d'odeur sont mesurées environ 1 h après la fin des mesures de fumées Tanabe (12:30 → 13:28 ; 12:21 → 13:35), et les substances odorantes environ 10 à 20 min après (12:41 ; 12:40). Le document ne dit pas si l'installation fonctionnait dans les mêmes conditions.

---

## Comparaison des documents 1, 3 et 4

| Critère | Doc. 1 (Analysis-Results-Off-gas-Odor-Exhaust) | Doc. 3 (Dioxins) | Doc. 4 (Exhaust Gas Concentration - Bad Smell - Dioxins) |
|---|---|---|---|
| Date de prélèvement | 2020-11-25 | 9/26 et 9/27 (année implicite 2023) | 2023-09-26 et 2023-09-27 |
| Dates des rapports | 2020-11-27 ; 2020-12-05 | 2023-10-27 | 2023-10-02 ; 2023-10-13 ; 2023-10-25 ; 2023-10-27 |
| Numéros | B2002600 ; 20002610 ; (sans n°) | aucun | 23T271 ; 23T272 ; f23010121 ; f23010122 ; F23010006 ; F23010007 ; (sans n°) |
| Laboratoires | KANSOテクノス (Osaka) ; トータル環境システム (Osaka) | 環境公害分析センター (Utsunomiya, Tochigi) | タナベ環境工学 (Ōita) ; エヌ・イー サポート (Hiroshima/Fukuoka) ; 環境公害分析センター |
| Client | 株式会社 ワンワールド (OneWorld) | masqué ; couche texte : ランドブレイン 株式会社 (Land Brain) | masqué |
| Installation | 過熱水蒸気炭化装置, centre de recyclage d'une société masquée | 廃プラスチック油化実証施設 | idem doc. 3 (p. 9) ; p. 1-8 : établissement masqué, « ばい煙発生施設 » |
| Point | off-gas (point « ー ») ; 排出口 ; limites de site | 排ガス (point non indiqué) | 排気口 ; 排出口 |

Conclusions factuelles :
1. **Doc. 3 = doc. 4 pages 9 à 11** : comparaison pixel par pixel des rendus 110 dpi (aucune différence, `ImageChops.difference(...).getbbox()` = None pour les 3 pages) et texte extrait identique (`diff` sans écart). Doc. 3 est donc un **doublon** d'une partie du doc. 4 : ce n'est pas une mesure supplémentaire.
2. **Doc. 1 est une campagne différente** du doc. 4 : 2020 contre 2023, laboratoires différents, numéros différents, type d'installation décrit différemment (« appareil de carbonisation à vapeur surchauffée » contre « installation de démonstration de liquéfaction de plastique »), client différent (OneWorld contre Land Brain selon la couche texte). Rien dans les documents ne relie explicitement les deux à la même machine.
3. Au sein du doc. 4, les deux jours (26 et 27/09/2023) sont deux séries de mesures distinctes de la même campagne (numéros consécutifs 23T271/23T272, f23010121/122, F23010006/007).

## Valeurs comparables entre campagnes (relevé, sans conclusion)

| Polluant | Doc. 1 (2020-11-25, 排出口) | Doc. 4 (2023-09-26) | Doc. 4 (2023-09-27) |
|---|---|---|---|
| NOx | 15 ppm (JIS K 0104:2011) | 30 ppm (JIS K 0104) | 30 ppm |
| SOx | < 1 ppm (JIS K 0103:2011) | < 0,5 ppm | < 0,5 ppm |
| Poussières | < 0,002 g/m³ (JIS Z 8808:2013) | < 0,004 g/m³N | < 0,005 g/m³N |
| HCl | < 1 ppm (JIS K 0107:2012) | non mesuré | non mesuré |
| HCN | non mesuré | < 0,5 ppm (JIS K 0109) | < 0,5 ppm |
| O2 | 18,5 % (JIS K 0301:2016) | non mesuré | non mesuré |
| Dioxines | non mesuré | 0,011 ng-TEQ/m³ | 0,025 ng-TEQ/m³ |
| Odeur à la sortie | indice 14 (conc. 25) | indice 24 (conc. 250) | indice 22 (conc. 160) |
| H2S | < 0,5 ppm (dans l'off-gas, CG) | < 0,001 ppm (odeur) | < 0,001 ppm |

Aucune de ces valeurs n'est ramenée à une teneur de référence en O2 dans les documents. Les valeurs en ppm sont des concentrations brutes ; la base humide ou sèche n'est indiquée que pour le débit (doc. 4, « 乾き » = sec).

---

## Remarques

Ce qui manque :
- **Identification de la machine** : aucun document ne nomme UR-2000, URC-2000, OneWorld (sauf comme destinataire du doc. 1) ni un numéro de série. Les noms de site et d'établissement sont caviardés (doc. 1 au marqueur noir ; doc. 4 en blanc).
- **Source d'émission** : aucun document ne précise si le point « 排出口 / 排気口 » est la cheminée du brûleur (combustion du gaz de pyrolyse, du kérosène ou d'un autre combustible), une torchère, ou l'évent du réacteur. Le doc. 1 p. 1 « オフガス » n'est pas défini.
- **Teneur en O2 de référence** : absente partout ; O2 mesuré seulement dans le doc. 1 (18,5 %), donc les valeurs ne peuvent pas être ramenées à une base normalisée (ex. 11 % ou 12 % O2) pour le doc. 4.
- **CO dans les fumées** : non mesuré dans aucun document (seul le CO de l'off-gas, 0,6 %, est donné).
- **Dioxines** : document « 速報 » (préliminaire, selon la couche texte), sans numéro, sans méthode, sans signataire agréé, sans base O2, sans point de prélèvement, sans débit, sans détail des congénères. Le rapport final n'est pas dans les fichiers lus.
- **Odeurs (doc. 4)** : échantillons prélevés par le client (« 採取者 依頼者 »), pas par le laboratoire.
- **Conditions de fonctionnement** : aucune matière entrante, débit de matière, température, durée de cycle ou combustible n'est indiqué dans les docs 1, 3, 4 (seulement « 燃原料使用状況 通常 », fonctionnement normal).
- **Doc. 2 (chromatographie)** : il s'agit d'un liquide « drain » chauffé à 350 °C, pas d'un gaz ; pas de date, pas d'origine de l'échantillon, pas de machine, pas de gaz vecteur, pas de colonne, pas de méthode normalisée ; les pourcentages sont des ratios d'aire de pics, pas des compositions massiques ; une grande partie des pics est « possible » ou « 不明 » (inconnu) ; environ 50 % (53,7 %) de l'échantillon ne se volatilise pas à 350 °C. Les métadonnées indiquent un nom de fichier d'origine « 20250317183955.pdf » ; un fichier de ce nom existe dans `documents-fournis/` (non ouvert ici, taille différente : 272 164 octets contre 4 673 327) : à rapprocher dans une autre brique.
- **Off-gas doc. 1** : somme 97,8 % (2,2 % non expliqués) ; 65,8 % N2 et 12,3 % O2 dans un gaz dit « off-gas ».

Points à demander au constructeur / à l'exploitant :
1. Quelle machine (modèle, n° de série, capacité) et quel site pour chaque campagne (2020 doc. 1 ; 2023 doc. 4) ; lien entre « 過熱水蒸気炭化装置 » (2020) et « 廃プラスチック油化実証施設 » (2023).
2. Nature exacte des points « オフガス », « 排出口 », « 排気口 » : cheminée du brûleur de chauffe ? combustible brûlé (gaz de pyrolyse, kérosène, huile produite) ? traitement des fumées en amont ?
3. Pourquoi l'off-gas 2020 contient 65,8 % N2 et 12,3 % O2 (balayage à l'azote, entrée d'air, dilution au prélèvement ?).
4. Le rapport définitif des dioxines (numéro, méthode JIS K 0311, base O2, congénères, débit, signataire agréé) et l'identité du préleveur.
5. La teneur en O2 des fumées les 26 et 27/09/2023 (pour ramener NOx, poussières et dioxines à une base de référence) et le CO.
6. Les conditions d'essai pendant les mesures 2023 : matière et masse traitées, cadence, températures, durée.
7. Pour la chromatographie : origine du « drain » (quel point de la machine, quelle date, quelle matière), date du rapport officiel, et rapport officiel lui-même.
