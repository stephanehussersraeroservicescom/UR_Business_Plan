# Extraction annexe 2 : énergie, UR2000, documents divers

Racine : `working-folder/reference/preuves/`
Relevé fait le 2026-10-14. Méthode : pdftotext page par page, puis rastérisation (110 dpi, zooms à 250 ou 300 dpi) et lecture de chaque image ; tableurs lus avec openpyxl (valeurs et formules). Tous les PDF de ce lot, sauf la brochure UR2000-JP, sont des images sans couche texte : tous les chiffres de ces PDF sont « (lu sur image) ».
Les calculs de contrôle sont faits en python ; ils sont signalés « calcul Claude » et ne sont pas des données sources.

---

## 1. bilan-energie/consommation-electrique-et-fuel.pdf

- Pages : 1 ; langue : anglais ; image scannée (Canon iR-ADV C5540 III, métadonnée CreationDate 2024-01-16).
- Titre exact : « UR Energy Consumption » ; second tableau « *Test sample ».
- Auteur/émetteur : NON INDIQUÉ (aucun en-tête, logo ni signature). Destinataire : NON INDIQUÉ. Date : NON INDIQUÉE (seule la date de numérisation est connue). Laboratoire : aucun. Qui a mesuré : NON INDIQUÉ. N° de rapport : aucun. Accréditation : aucune.
- Nature : **déclaration (émetteur non identifié)**. Tableau de consommations par taille de machine, sans méthode, sans date d'essai, sans mesureur ; la ligne « Test sample » donne seulement la matière de test par taille.

| Page | Grandeur | Valeur | Unité | Citation exacte | Traduction [trad. Claude] | Conditions | Nature |
|---|---|---|---|---|---|---|---|
| 1 | Consommation de fioul, mode « Oil + Electricity », UR 1t | 120 | L/batch | « 120L/batcht(1t) » | | matière de test : « Marin garbage, tire, bamboo etc. » ; (lu sur image) | déclaration |
| 1 | Électricité, mode « Oil + Electricity », UR 1t | 25 | « kW/h » (sic) | « 25kW/h » | | idem | déclaration |
| 1 | Électricité, mode « All Electricity », UR 1t | 709 | « kW/batch » (sic) | « 709kW/batch(1t) » | | idem | déclaration |
| 1 | Fioul, UR 5t | 220 | L/batch | « 220L/batcht(5t) » | | « Plastic resin 100% (PP, PE, PS, PVC) » | déclaration |
| 1 | Électricité mode mixte, UR 5t | 50 | « kW/h » | « 50kW/h » | | idem | déclaration |
| 1 | Électricité tout électrique, UR 5t | 1 333 | « kW/batch » | « 1,333kW/batch(5t) » | | idem | déclaration |
| 1 | Fioul, UR 15t | 800 | L/batch | « 800L/batcht(15t) » | | « Plastic resin + tire (composite plastic) » | déclaration |
| 1 | Électricité mode mixte, UR 15t | 150 | « kW/h » | « 150kW/h » | | idem | déclaration |
| 1 | Électricité tout électrique, UR 15t | 6 976 | « kW/batch » | « 6,976kW/batch(15t) » | | idem | déclaration |
| 1 | Fioul, UR 40t | 2 200 | L/jour | « 2,200L/day(40t) » | | « Plastic resin + tire (composite plastic) » | déclaration |
| 1 | Électricité mode mixte, UR 40t | 250 | « kW/h » | « 250kW/h » | | idem | déclaration |
| 1 | Électricité tout électrique, UR 40t | 14 480 | « kW/day » | « 14,480kW/day(40t) » | | idem | déclaration |
| 1 | Fioul, UR 100t | 5 500 | L/jour | « 5,500L/day(100t) » | | « Plastic 15%. Household trash 80%, Stone/Metal/Glass 5% » | déclaration |
| 1 | Électricité mode mixte, UR 100t | 350 | « kW/h » | « 350kW/h » | | idem | déclaration |
| 1 | Électricité tout électrique, UR 100t | 31 720 | « kW/day » | « 31,720kW/day(100t) » | | idem | déclaration |
| 1 | Fioul, UR 200t | 10 000 | L/jour | « 10,000L/day(200t) » | | « Plastic 15%. Household trash 80%, Stone/Metal/Glass 5% » | déclaration |
| 1 | Électricité mode mixte, UR 200t | 600 | « kW/h » | « 600kW/h » | | idem | déclaration |
| 1 | Électricité tout électrique, UR 200t | 56 800 | « kW/day » | « 56,800kW/day(200t) » | | idem | déclaration |

Observations (calcul Claude, pas des données sources) :
- Unités : « kW/h » et « kW/batch », « kW/day » ne sont pas des unités cohérentes ; AMBIGU : probablement kW (puissance) pour le mode mixte et kWh pour le mode tout électrique, non écrit dans le document.
- Le type de fioul (« Oil ») n'est pas précisé.
- Ratios par tonne : fioul 120 L/t (1t), 44 (5t), 53,3 (15t), 55 (40t), 55 (100t), 50 L/t (200t). Tout électrique : 709, 266,6, 465,1, 362, 317,2, 284 kWh/t. Mode mixte 200t : 600 × 24 h = 14 400 kWh/jour soit 72 kWh/t si 600 est une puissance continue (hypothèse).
- La série n'est pas monotone (15t plus gourmand par tonne que 5t et 40t) : à demander.
- Les matières de test diffèrent d'une taille à l'autre, donc les lignes ne sont pas comparables entre elles.

---

## 2. bilan-energie/energy-balance.xlsx

- Feuilles : « page 36 », « page 35 », « Template ». Pas d'image incorporée (pas de dossier xl/media).
- Métadonnées : creator « Husser Stephane », lastModifiedBy « Husser Stephane », créé le 2023-11-02 08:38:23, modifié le 2023-11-02 16:36:56, application Microsoft Excel 16.
- **Qui l'a construit et à partir de quoi** : d'après les métadonnées, Stephane Husser, le 2 novembre 2023. Le contenu reproduit cellule pour cellule les tableaux « Material 2 : Material Balance/Energy Balance » (page imprimée 35, PDF p. 42) et « Reference material : City material balance of recycled plastixc containers ands packaging as well as non combustible residue » (page imprimée 36, PDF p. 43) du document `documents-fournis/Chiba prefecture report ENG.pdf`, vérifié par pdftotext sur ce PDF. Les noms de feuilles « page 35 » et « page 36 » renvoient à cette pagination imprimée. Les erreurs de la source sont recopiées à l'identique (voir anomalies).
- Formules : une seule, « page 35 »!P27 `=P25` (=> « 9.3 kg »). Toutes les autres cellules sont du texte saisi (ex. « 65 kwh », « 554,368 kcal »), y compris les ratios K13/K14 (nombres saisis, non calculés). Le tableur ne calcule donc rien.
- Nature : **retranscription** d'une mesure de l'exploitant de l'essai de Chiba (rapport à la préfecture) ; dans ce rapport, le texte p. 34 imprimée précise : « Regarding the transpiration water of water (drainage) in material balance, the calculated value was used. » (eau évaporée calculée, non mesurée). Le mesureur et le laboratoire ne sont pas nommés dans le tableau.
- Langue : anglais. Machine : non nommée dans le tableau (essai de Chiba, Noda City).

| Page/feuille | Grandeur | Valeur | Unité | Citation exacte (cellule) | Conditions | Nature |
|---|---|---|---|---|---|---|
| page 35 (D6:F6) | Électricité consommée | 65 / 55 900 | kWh / kcal | E6 « 65 kwh », F6 « 55,900 kcal » | 26 mai, « 3P (PE, PP,PS) Pellets », 60 kg (J6, J7, K6) | retranscription mesure exploitant |
| page 35 (E7:F7) | Light oil consommé | 66 / 599 808 | L / kcal | « 66 liters », « 599,808 kcal » | idem | idem |
| page 35 (E8:F8) | Off gas (entrée énergie) | 11,7 / 15 489 | kg / kcal | « 11.7 kg », « 15,489 kcal » | idem | idem |
| page 35 F9 | Énergie totale entrée | 671 197 | kcal | « 671,197 kcal » | idem | idem |
| page 35 E10 | Eau | 85 | L | « 85 liters » | idem | idem |
| page 35 P6:Q6 | Huile produite | 43,1 / 473 238 | kg / kcal | « 43.1 kg », « 473.238 kcal » (point au lieu de virgule) | idem | idem |
| page 35 P7:Q7 | Résidu (« Oil Residu ») | 5,2 / 30 576 | kg / kcal | « 5.2 kg », « 30,576 kcal » | idem | idem |
| page 35 P8 | Métal / corps étrangers | 0,0 | kg | « 0.0 kg » | idem | idem |
| page 35 P10:Q10 | Off gas (sortie) | 11,7 / 15 489 | kg / kcal | « 11.7 kg », « 15,489 kcal » | idem | idem |
| page 35 P11:Q11 | Total produits | 60 / 519 303 | kg / kcal | « 60 kg », « 519,303 kcal » | idem | idem |
| page 35 P12, P13 | Eau de drainage / vapeur d'eau | 73 / 12 | L | « 73 liters », « 12 liters » | idem ; vapeur calculée selon le rapport source | idem |
| page 35 K13, K14 | Ratio matière / énergie | 1 / 0,774 | - | K13 1, K14 0.774 | idem | idem |
| page 35 (bloc 2) E24:F24 | Électricité | 65 / 55 900 | kWh / kcal | « 65 kwh », « 55.900 kcal » | 11 juillet, « 3P molded offcuts », 60 kg | idem |
| page 35 E25:F25 | Light oil | 76 / 690 688 | L / kcal | « 76 liters », « 690,688 kcal » | idem | idem |
| page 35 E26:F26 | Off gas | 1,3 / 1 721 | kg / kcal | « 1.3 kg », « 1,721 kcal » | idem | idem |
| page 35 F27 | Énergie totale entrée | 748 309 | kcal | « 748,309 kcal » | idem | idem |
| page 35 E28 | Eau | 95 | L | « 95 liters » | idem | idem |
| page 35 P24:Q24 | Huile produite | 49,4 / 542 412 | kg / kcal | « 49.4 kg », « 542,412 kcal » | idem | idem |
| page 35 P25:Q25 | Résidu | 9,3 / 54 684 | kg / kcal | « 9.3 kg », « 54,684 kcal » | idem | idem |
| page 35 P29:Q29 | Total produits | 60 / 598 817 | kg / kcal | « 60 kg », « 598,817 kcal » | idem | idem |
| page 35 P30, P31 | Drainage / vapeur | 85 / 10 | L | « 85 liters », « 10 liters » | idem | idem |
| page 35 K32 | Ratio énergie | 0,8 | - | 0.8 | idem | idem |
| page 36 E6:F6 | Électricité | 65 / 50 740 | kWh / kcal | « 65 kwh », « 50,740 kcal » | « Sept. 9th », « mixed waste », 50 kg | idem |
| page 36 E7:F7 | Light oil | 61 / 554 368 | L / kcal | « 61 liters », « 554,368 kcal » | idem | idem |
| page 36 E8:F8 | Off gas | 9,5 / 12 576 | kg / kcal | « 9,5 kg », « 12,576 kcal » | idem | idem |
| page 36 F9 | Énergie entrée | 617 684 | kcal | « 617,684 kcal » | idem | idem |
| page 36 E10 | Eau | 100 | L | « 100 liters » | idem | idem |
| page 36 P6:Q6 | Huile | 16,1 / 176 778 | kg / kcal | « 16.1 kg », « 176,778 kcal » | idem | idem |
| page 36 P7:Q7 | Résidu | 10,5 / 61 740 | kg / kcal | « 10.5 kg », « 61,740 kcal » | idem | idem |
| page 36 P8 | Métal / corps étrangers | 13,9 | kg | « 13.9 kg » | idem | idem |
| page 36 P9 | Résidu total | 24,4 | kg | « 24.4 kg » | idem | idem |
| page 36 Q11 | Énergie produits | 251 094 | kcal | « 251,094 kcal » | idem | idem |
| page 36 P12, P13 | Drainage / vapeur | 73 / 27 | L | « 73 liters », « 27 liters » | idem | idem |
| page 36 K14 | Ratio énergie | 0,407 | - | 0.407 | idem | idem |
| page 36 E24:F24 | Électricité | 65 / 55 900 | kWh / kcal | « 65 kwh », « 55.900 kcal » | « Sept, 15th », « mixed waste », 50 kg | idem |
| page 36 E25:F25 | Light oil | 61 / 554 368 | L / kcal | « 61 liters », « 554,368 kcal » | idem | idem |
| page 36 E26:F26 | Off gas | 10,8 / 14 297 | kg / kcal | « 10.8 kg », « 14,297 kcal » | idem | idem |
| page 36 F27 | Énergie entrée | 624 565 | kcal | « 624,565 kcal » | idem | idem |
| page 36 P24:Q24 | Huile | 22,5 / 542 412 | kg / kcal | « 22.5 kg », « 542,412 kcal » | idem ; voir anomalie | idem |
| page 36 P25:Q25 | Résidu | 11,3 / 54 684 | kg / kcal | « 11.3 kg », « 54,684 kcal » | idem ; voir anomalie | idem |
| page 36 P26, P27 | Métal ; résidu total | 5,4 ; 16,7 | kg | « 5.4 kg », « 16.7 kg » | idem | idem |
| page 36 Q29 | Énergie produits | 327 791 | kcal | « 327,791 kcal » | idem | idem |
| page 36 P30, P31 | Drainage / vapeur | 85 / 15 | L | « 85 liters », « 15 liters » | idem | idem |
| page 36 K32 | Ratio énergie | 0,525 | - | 0.525 | idem | idem |

Contrôles (calcul Claude) :
- Facteurs implicites (ce sont des facteurs appliqués, pas des mesures) : électricité 860 kcal/kWh (780,6 pour le 9 sept., soit 50 740 / 65) ; light oil 9 088 kcal/L ; off gas 1 323,8 kcal/kg ; huile 10 980 kcal/kg ; résidu 5 880 kcal/kg. Aucun de ces pouvoirs calorifiques n'a de source dans le tableau.
- Sommes des entrées : bouclent pour les 4 essais. Ratio énergie = énergie produits / énergie entrée : 0,4065 ; 0,5248 ; 0,7737 ; 0,8002, conformes aux valeurs écrites.
- Bilans matière : huile + résidu total + off gas = masse entrée exactement (50,0 ; 50,0 ; 60,0 ; 60,0 kg). Le ratio matière « 1 » est donc posé par construction ; l'off gas semble obtenu par différence (non écrit).
- **Anomalie 15 septembre** (feuille page 36, bloc 2, et identique dans le rapport de Chiba PDF p. 43) : Q24 « 542,412 kcal » pour 22,5 kg d'huile donne 24 107 kcal/kg, et Q25 « 54,684 kcal » pour 11,3 kg ; ce sont les valeurs de l'essai du 11 juillet. La somme des cellules (542 412 + 54 684 + 14 297 = 611 393) ne donne pas le total écrit 327 791. Avec 10 980 kcal/kg et 5 880 kcal/kg : 247 050 + 66 444 + 14 297 = 327 791, égal au total écrit. Le total et le ratio 52,5 % sont donc cohérents avec les facteurs ; les cellules Q24 et Q25 sont des reports erronés.
- Électricité 9 sept. : 50 740 kcal au lieu de 55 900 pour les mêmes 65 kWh : incohérence non expliquée.
- L'off gas est compté à la fois en entrée et en sortie (recirculé comme combustible), ce qui gonfle les deux termes du ratio.
- Consommation de light oil rapportée à la masse traitée : 1,22 ; 1,22 ; 1,10 ; 1,27 L/kg de déchet ; énergie entrée 11 187 à 12 491 kcal/kg de déchet. Ces ordres de grandeur sont plus de 20 fois supérieurs au tableau du document 1 (50 L/t pour 200t) : petite machine d'essai, non extrapolable sans données du constructeur.
- Eau : drainage + vapeur = eau entrée dans les 4 cas (vapeur calculée par différence selon la source).

---

## 3. documents-constructeur/Worksheet-Lufthansa-200MT.xlsx

- Feuilles : « 200T-Luftanssa (2) » et « Copy of 200T-Luftanssa (2) » (A1:M100). Pas d'image (dossiers xl/drawings vides, pas de xl/media).
- Métadonnées : creator « Peter », créé le 2024-01-25 06:51:08 UTC ; pas de lastModifiedBy ni de date de modification dans le fichier ; entrées du zip datées 2024-08-20 et structure (dossier xl/metadata, « Copy of ») évoquant un export Google Sheets (indice, non vérifié). Identité de « Peter » : NON INDIQUÉE.
- Titre exact : « Worksheet for 200MT UR in USD ».
- Nature : **feuille d'hypothèses commerciales** (aucune mesure) ; les rendements y sont des coefficients saisis dans les formules. Classée ici comme « déclaration du constructeur ou de son représentant » d'après le dossier où elle est rangée, sans auteur identifiable.

Valeurs utiles à l'annexe 2 (feuille 1 = « 200T-Luftanssa (2) », feuille 2 = « Copy of ... ») :

| Feuille!cellule | Grandeur | Valeur | Unité | Citation exacte (libellé / formule) | Conditions | Nature |
|---|---|---|---|---|---|---|
| F1!B2, F2!B2 | Capacité machine | 200 | T | « Machine Capacity (T) » 200 | | hypothèse |
| F1!B16 | Densité des déchets | 0,7 | - | « Density of input waste » 0.7 | | hypothèse |
| F1!B17 | Déchets entrants par jour | 140 | t/jour | `=+$B$16*$B$2` | 0,7 × 200 | hypothèse calculée |
| F1!B18 | Jours d'exploitation | 330 | j/an | « Operation days per annum » 330 | | hypothèse |
| F1!B12 / F2!B12 | Part plastique | 1,0 / 0,3 | - | « - Plastic » | | hypothèse |
| F1!B13 | Part « autres inorganiques » | 0,7 | - | « - Other inorganic » 0.7 | | hypothèse |
| F1!B14, B15 | Métaux, silice/sable | 0 ; 0 | - | « - Metals », « - silica/sands » | | hypothèse |
| F1!E15 | Électricité | 950 400 | USD/an | `=600*24*+$B$18*0.2*$B$2/200` ; libellé « Electricity (@0.2) » | 600 (kW implicite) × 24 h × 330 j × 0,2 USD | facteur appliqué |
| F1!E21 | Huile produite (valeur) | 11 781 000 | USD/an | `=+$B$17*+$B$18*$B$12*0.85*1000*+$B$21*0.5` ; libellé « Heavy  oil generated (0.41/l) » | coefficient 0,85 × 1000 (L ou kg par t, non précisé) ; prix B21 = 0,6 ; facteur 0,5 non expliqué | facteur appliqué |
| F2!E21 | idem | 11 781 000 | « USD/an » | `=+$B$17*+$B$18*$B$12*0.85*1000` | aucun prix appliqué (B21 = 0,41 non utilisé) | facteur appliqué |
| F1!E22 | Consommation interne de fioul | 1 980 000 | USD/an | `=10000*+$B$2/200*+$B$18*+$B$21` ; « Internal consumption » | 10 000 (L/jour implicite) × 330 × 0,6 | facteur appliqué |
| F2!E22 | idem | 3 300 000 | « USD/an » | `=10000*+$B$2/200*+$B$18` | 10 000 × 330, sans prix | facteur appliqué |
| F1!E24 | Carbure (char) | 808 500 | USD/an | `=+$B$17*$B$18*$B$13*0.25*$B$22` ; « Carbide for sales » | 140 × 330 × 0,7 × 0,25 × 100 USD/t | facteur appliqué |
| F1!I24 / J24 / K24 | CO2 par t de déchet | 1,8 / 0,15 / 0 | t CO2/t | « Incinerator » 1.8 ; « UR (internal oil) » `=0.05*3` ; « UR (electric) » 0 | | hypothèse |
| F1!E26 | Crédit carbone | 2 762 100 | USD/an | `=(+$B$17-47*$B$2/200)*$B$18*+$B$25*$B$24` | constante 47 non expliquée | facteur appliqué |
| F1!H27 | CO2 évité | 76 230 | t/an | « One unit of 200T UR machine could prevent at least 76,230 MT of CO2 emission per year. » | | déclaration |
| F1!B4 / F2!B4 | Prix machine | 45 000 000 / 60 000 000 | USD | `=45000000*$B$2/200` / `=60000000*$B$2/200` | hors annexe 2, noté pour mémoire | hypothèse |
| F2!B27 | Redevance de traitement | 350 | USD/t | « Waste Processing Fee/T » 350 | F1 : 0 | hypothèse |
| F2!D31:E31 | (sans objet) | 84 810 000 | | « pour innigham » `=E23*10` | | note de travail |

Observations : les chiffres « 600 » (électricité) et « 10000 » (fioul interne) correspondent aux valeurs 200t du document 1 (« 600kW/h », « 10,000L/day(200t) »). Le coefficient 0,85 de « Heavy oil generated » est un facteur saisi, sans source. La feuille 1 suppose 100 % de plastique, la feuille 2 30 %, avec le même résultat (11 781 000) obtenu par des formules différentes. Les deux feuilles traitent un volume en litres comme un montant en dollars en feuille 2 (E21, E22 sans prix) : incohérence d'unités.

---

## 4. documents-fournis/UR2000-JP.pdf

- Pages : 14 ; langue : japonais (quelques libellés anglais) ; Adobe InDesign, CreationDate 2020-05-20. Texte extrait par pdftotext, chaque page vérifiée sur image.
- Titre exact : « OIL RECOVERY & CABONIZATION PLANT URC-2000 / 過熱水蒸気炭化処理による減容及び油成分回収処理装置 / 『 URBAN RIG 2000 : アーバンリグ 2000 』 » ; [trad. Claude] « Installation de réduction de volume et de récupération de la fraction huileuse par carbonisation à la vapeur d'eau surchauffée ».
- Émetteur : « Oneworld corporation, Headquarters / 1-1-20 Nagayoshinagahara, Hirano-ku, Osaka-city, Osaka, Japan » ; « Copyright Oneworld company. All rights reserved. » Destinataire : aucun. Date : non imprimée (PDF 2020-05-20 ; plans datés 2014.05.22). Laboratoire : aucun. N° : plans « DW11-000000 ».
- Nature : **déclaration du constructeur** (brochure commerciale, aucune mesure attribuée à un tiers ; le graphique d'émissions p. 14 n'a ni date, ni laboratoire, ni conditions).

| Page | Grandeur | Valeur | Unité | Citation exacte | Traduction [trad. Claude] | Conditions | Nature |
|---|---|---|---|---|---|---|---|
| 1 | Rien d'utile au-delà du titre (photo, adresse) | | | | | | |
| 2 | Réduction de volume illustrée | 200 → 10 (+ 50) | ton | « 200 ton », « 10 ton », « 50 ton » (vignettes) | | illustration, sans conditions ; AMBIGU : 10 t (huile ?) et 50 t (charbon ?) non légendés | déclaration |
| 2 | Part de résines dans les ordures ménagères | 10 | % | « 一般ゴミの成分は樹脂系類を 10％程度含んだ、残飯や紙・木片等である » | « les ordures ménagères contiennent environ 10 % de résines, le reste étant restes alimentaires, papier, bois » | | déclaration |
| 2 | Produits annoncés | | | « 回収 ① 樹脂系 : プラスチック類や化繊類 →《軽油相当の油》への変換 » ; « 回収 ② 生ゴミ、残飯、紙類、木片類 他 →《石炭代替の炭》への変換 » | « résines et fibres → huile équivalente au gazole ; déchets organiques, papier, bois → charbon substitut de houille » | | déclaration |
| 3 | Émissions annoncées | 0 | | « ダイオキシンなどの有害物は発生しない大気環境対応器です。 » | « appareil qui ne génère pas de substances nocives telles que les dioxines » | aucune mesure citée | déclaration |
| 3 | Chlore | | | « 塩化ビニールなどより発生する塩素も水蒸気により希塩酸になり釜を傷めることはありません。 » | « le chlore issu du PVC devient de l'acide chlorhydrique dilué via la vapeur et n'abîme pas le réacteur » | | déclaration |
| 3 | Odeur, bruit | | | « 臭いは装置内で熱分解しますのでほとんど発生しません。作動音は、クーリングタワー程度の音量 » | « les odeurs sont décomposées dans l'appareil et presque absentes ; bruit de l'ordre d'une tour de refroidissement » | | déclaration |
| 4 | Températures des zones (chauffe) | 150 / 300 / 450 / 600 | °C | « 150℃ 300℃ 450℃ 600℃ » sous « 灯油系 軽油系 重油系 アスファルテン » et « 過熱処理 ZONE » | « zone de chauffe : fraction kérosène, gazole, fioul lourd, asphaltènes » | (lu sur image et texte) | déclaration |
| 4 | Températures des zones (refroidissement) | 400 / 150 / 60 | °C | « 400℃ 150℃ 60℃ » sous « 冷却処理 ZONE » | « zone de refroidissement » | | déclaration |
| 4 | Temps cumulés par zone | 90 / 180 / 270 / 360 / 450 / 540 / 630 | min | « 90 分 <1.5h> » ... « 630 分 <10.5h> » | | | déclaration |
| 4 | Répartition des fractions d'huile | NON TROUVÉ en pourcentage | | seules les étiquettes « 灯油系 軽油系 重油系 アスファルテン » associées aux zones | « kérosène, gazole, fioul lourd, asphaltènes » | aucune proportion chiffrée | déclaration |
| 4 | Chaudière vapeur | max. 165 | °C | « 水蒸気ボイラ max. 165℃ » | « chaudière vapeur » | | déclaration |
| 4 | Générateur de vapeur surchauffée | max. 600 | °C | « 過熱蒸気発生機 max. 600℃ » | | | déclaration |
| 4 | Brûleur de surchauffe | 833 | kcal/s | « 過熱バナー 833kcal/s » | « brûleur de surchauffe » | nombre de brûleurs non précisé ; 833 kcal/s = 2 998 800 kcal/h ≈ 3 488 kW (calcul Claude) | déclaration |
| 4 | Réacteur | ambiante à 600 | °C | « 反応炉 ( 内釜 ) 常温〜 600℃ » | « réacteur (cuve intérieure) » | | déclaration |
| 5 | Entrée | 200 / 200 / 200 000 | t / m³ / L | « 200ton. ▶ 200m3 (200,000L) 樹脂系類含有率 10% で試算 » | « calcul avec 10 % de résines » | ordures ménagères (« 一般家庭廃棄物 ») ; densité 1 implicite | déclaration |
| 5 | Char (carbonisat) | 25 | % (50 m³) | « 炭化物 25% (50m3/ 加工利用可能 ) » | « carbonisat 25 % (50 m³, valorisable après transformation) » | (lu sur image) | déclaration |
| 5 | Métaux, verre | 0 à 5 | % | « 金属類・ガラス ０〜５% ( 売却 ) » | « métaux, verre 0 à 5 % (vendus) » | | déclaration |
| 5 | Huile mixte (gazole, fioul lourd) | 5 | % (10 000 ℓ) | « 混合油 ( 軽油・重油 ) 5% (10,000ℓ / 再利用可能 ) » | « huile mixte 5 % (10 000 L, réutilisable) » | | déclaration |
| 5 | Off gas | 5 | % (10 000 ℓ) | « OFF ガス 5% (10,000ℓ / 再利用 ) » | « off gas 5 % (10 000 L, réutilisé) » | gaz exprimé en litres (sic) | déclaration |
| 6 | Unités | 7 | unités | « 本機処理プラント (200T) は 7 ユニットで構成。 » | « la plante 200 t se compose de 7 unités » | | déclaration |
| 6 | Capacité par unité | env. 12 | t | « 約 12 トン処理機 ( 1 ユニット ) を工場量産する » | « machine d'environ 12 t (1 unité) produite en série » | | déclaration |
| 6 | Transport | 7 | morceaux | « 処理機本体を７分割しトラック搬送して現地組立方式を採用。 » | « corps divisé en 7 pour transport par camion, assemblage sur site » | | déclaration |
| 6 | Distinction | 2019-06-17 | date | « 海ごみゼロアワード イノベーション部門 日本財団賞受賞 » ; diplôme « 2019年6月17日 » (lu sur image) | « prix Nippon Foundation, catégorie innovation » | | déclaration |
| 7 | Benne de transport | 1 × 3 × 1,5 ; 4,5 | m ; m³ | « SIZE : W1 x D3 x H1.5(m) 容 積 : 4.5m3 » | | | déclaration |
| 7 | Masse max par benne | 4,17 | t | « MAX 重量 : 4.17 t » | | | déclaration |
| 7 | Réduction | env. 12 → env. 3 ; 25 | t ; % | « 約12t » « 減容率 約25% » « 約 3t » | « taux de réduction environ 25 % » (le résidu vaut 25 % de l'entrée) | | déclaration |
| 7 | Temps par unité | 90 | min | « ユニット単位の処理時間 : ７連式 90 分 » | | | déclaration |
| 7 | Cadence | 48 bennes / 24 h ; 10,5 h par benne | | « 24 時間のバケット搬入台数 48 台・１台の処理時間数 10. 5 時間 » | | bennes déplacées par 3 (« 搬送用バケットは三個単位で移動します。 ») | déclaration |
| 7 | Perte au démarrage | | | « 始動ロス ( 無搬出 ) » sur les 8 premiers pas (tableau, lu sur image) | « perte de démarrage (pas de sortie) » | premières sorties à 0h après 8 entrées | déclaration |
| 8 | Capacité | 200 | t/jour | « 処理量 / 日 200 トン / 日 » | | | déclaration |
| 8 | Température de décomposition | MAX 600, ≤ 0,2 MPa | °C | « MAX 600℃ 常圧 0.2MPa 以下 » | | | déclaration |
| 8 | Dimensions machine | 62 × 10 × 7 | m | « W: 62m D: 10m H: 7m » | | | déclaration |
| 8 | Production de vapeur | chaudière / gazole | | « 水蒸気生成 蒸気ボイラ / 軽油 » | « chaudière vapeur au gazole (軽油) » | | déclaration |
| 8 | Mode de surchauffe | | | « 過熱形式 アフターバナー過熱 » | « surchauffe par post-brûleur » | | déclaration |
| 8 | Alimentation électrique | 200 et 360 | V AC triphasé 60 Hz | « 電力 200V AC 三相 60Hz 電力 360V AC 三相 60Hz » | | | déclaration |
| 8 | Consommation électrique continue | 20 | « kw/h » (sic) | « 消費電力 ( 連続時 ) 20kw/h » | « consommation électrique (en continu) » | | déclaration |
| 8 | Vapeur zones 1 à 7 | 150 / 300 / 450 / 600 / 400 / 150 / 60 | °C, ≤ 0,2 MPa | « Zone 1 150℃ / 常圧 0.2MPa 以下 » ... « Zone 7 60℃ / 常圧 0.2MPa 以下 » | | | déclaration |
| 9 | Bâtiment 200t | 4 650 | m² | « 建築面積 4,650 m2 » | « surface bâtie » | site 99 + 18 m × 45 m (lu sur image) | déclaration |
| 9 | Ventilation | 3 000 / 640 / 810 / 200 | m² | « 処理工場 3,000 m2 » « 廃棄物保管所 640 m2 » « 再生品保管場 810 m2 » « 事務所倉庫類 200 m2 » | « usine / stockage déchets / stockage produits / bureaux » | somme 4 650 (calcul Claude) | déclaration |
| 9 | Stockage déchets | 600 « m² » | | « 廃棄物保管場 容積 : 600m2 (３日分 ) » | « volume 600 m² (3 jours) » | unité m² pour un volume (sic) ; 640 m² dans le tableau | déclaration |
| 9 | Hauteur, cuves | 10 m ; 5 t × 8 (huile) ; 5 t × 2 (eau) | | « 天井高 10 m » « 油貯蔵タンク 5t × 8 » « 水貯蔵タンク 5t × 2 » | | | déclaration |
| 10 | Plan 1 000 t/jour | 28 900 ; 170 × 170 ; 12,5 | m² ; m ; m | « 敷地面積 : 28,900 m2 » « 敷地サイズ : 170m × 170m » « 天井高 : 12.5 m » (le texte superposé donne aussi « 12m ») | | 5 × URC-2000 ; bâtiments 14 230 / 3 450 / 3 450 / 640 m² (lu sur image) ; stockage « 6000m2 (３日分 ) » | déclaration |
| 11 | Plan d'ensemble | longueur 61 461 | mm | cote « 61461 » (lu sur image) ; « 全体組立図 » « DATE 2014.05.22 » « DW11-000000 » | « plan d'assemblage général » | | déclaration |
| 12 | Zones (plan de 2014) | 150 / 250 / 350 / 500 / 350 / 150 / <100 | °C | « 減容ゾーン (max. 150℃ 加熱) » « No. 1 ゾーン (max. 250℃ 加熱) » « No. 2 ゾーン (max. 350℃ 加熱) » « No. 3 ゾーン (max. 500℃ 加熱) » « No. 4 ゾーン (max. 350℃ 加熱) » « No. 5 ゾーン (150℃まで冷却) » « 冷却ゾーン (100℃以下まで冷却) » (lu sur image) | « zone de réduction, zones 1 à 4 chauffe, zone 5 et zone de refroidissement » | | déclaration |
| 12 | Brûleurs des surchauffeurs | ON/OFF 300/350, 400/450, 550/600, 400/450 ; max 350, 450, 600, 450 | °C | « バーナー (300℃-ON 350℃-OFF) » ... « 過熱蒸気発生装置 (max. 350℃) » (lu sur image) | | 4 surchauffeurs, 4 chaudières (« ボイラ ») | déclaration |
| 12 | Fluides | | | « 圧縮空気 » « 精製水 » « 灯油 » « 電源 AC200V » « 排水 » | « air comprimé, eau purifiée, kérosène, alimentation 200 V, rejet d'eau » | | déclaration |
| 12 | Spécifications principales | | | « 電源 AC200/220V × 50/60 Hz ×3φ » « 処理用バケット 幅3000×長さ1500×高さ1000mm » « 処理能力 12m3 (4バケット)/ 時間 » « 処理温度 max. 800℃ 蒸気加熱 » « コンベア全長 44m » | « capacité 12 m³ (4 bennes) par heure ; température max 800 °C ; convoyeur 44 m » | (lu sur image, zoom 300 dpi) | déclaration |
| 13 | Délai contrat → mise en service | 4 | mois | « 1 st. Month », « 2〜3 th. Months », « 4 th. Month » ; « 完了 » | | fabrication mois 1 à 3, expédition, installation, essais au mois 4 | déclaration |
| 13 | Fondations | ≥ 5 | t/m² | « 設置する場所の基礎強度は、１m2 当り５トン以上の基礎土台養生が必要となります。 » | « fondation d'au moins 5 t par m² » | | déclaration |
| 13 | Essai final | | | « 一般ゴミ処理物の手配準備 » « 油回収物抽出試験 » | « préparation des déchets ; essai d'extraction de l'huile récupérée » | à la charge de l'acheteur | déclaration |
| 14 | SOx point 1 à 4, « 換算濃度 » | 3 788 / 647 / 567 / 808 | mg/m³ | « 3788 mg/m3 » « 647 mg/m3 » « 567 mg/m3 » « 808 mg/m3 » (lu sur image) | « concentration convertie » | points de mesure 1 à 4 de l'option PRIMO (PUREM 30.8) ; pas de date, d'O2 de référence, de labo | déclaration |
| 14 | SOx point 1 à 4, « 実測濃度 » | 1 067 / 168 / 131 / 72 | mg/m³ | « 1067 mg/m3 » « 168 mg/m3 » « 131 mg/m3 » « 72 mg/m3 » | « concentration mesurée » | idem | déclaration |
| 14 | NOx point 1 à 4, converti | 11 / 49 / 113 / 0 | mg/m³ | « 11 mg/m3 » « 49 mg/m3 » « 113 mg/m3 » « 0 mg/m3 » | | idem | déclaration |
| 14 | NOx point 1 à 4, mesuré | 9 / 33 / 84 / 0 | mg/m³ | « 9 mg/m3 » « 33 mg/m3 » « 84 mg/m3 » « 0 mg/m3 » | | idem ; un seul libellé « 0 mg/m3 » pour les deux courbes au point 4 | déclaration |
| 14 | Option SEA CORAL | | | description qualitative, aucun chiffre | « purification d'eau par céramique » | | déclaration |

Grandeurs demandées et NON TROUVÉES dans la brochure : consommation de fioul ou de kérosène en litres, consommation d'eau, débit de vapeur, personnel d'exploitation, rendement énergétique, composition ou PCI de l'huile, du gaz et du char, dioxines mesurées, HCl, poussières, CO.

Contradictions internes (UR2000-JP) :
- Températures de zones : p. 4 et p. 8 (150/300/450/600/400/150/60 °C, max 600 °C) contre p. 12, plan de 2014 (150/250/350/500/350/150/<100 °C, « max. 800℃ »).
- Capacité horaire : p. 12 « 12m3 (4バケット)/ 時間 » alors que 4 bennes de 3 000 × 1 500 × 1 000 mm font 18 m³ ; p. 7 donne 3 bennes toutes les 90 min, soit 13,5 m³ par 1,5 h (calcul Claude). 12 m³/h × 24 h = 288 m³/jour contre 200 m³/jour en p. 5.
- Longueur : 62 m (p. 8), 61 461 mm (p. 11), convoyeur 44 m (p. 12).
- Combustible de la chaudière : « 軽油 » (gazole, p. 8) contre « 灯油 » (kérosène, p. 12).
- Tension : 200 V et 360 V (p. 8) contre 200/220 V, 50/60 Hz (p. 12).
- Cadence : 48 bennes × 4,17 t = 200,16 t/jour (calcul Claude), cohérent avec 200 t/jour ; mais 12 t par lot de 3 bennes (p. 7) donne 4 t par benne.
- Bilan p. 5 : 25 % + 0 à 5 % + 5 % + 5 % = 35 à 40 % de l'entrée ; 60 à 65 % ne sont pas affectés (probablement l'eau, non écrit).
- Huile p. 5 : 10 000 L/jour produits ; le document 1 annonce 10 000 L/jour de fioul consommés pour 200t (« 10,000L/day(200t) ») : la production annoncée égale la consommation annoncée.
- Électricité : 20 « kw/h » en continu (p. 8) contre 600 « kW/h » pour 200t dans le document 1.
- p. 2 : légende « UN-200 » et p. 6 « UN-200 » au lieu de « URC-2000 ».

---

## 5. documents-constructeur/Urban-Rig-Demo-Operation-Test-Report.pdf

- Pages : 3 ; langue : anglais (traduction du japonais vraisemblable, non indiquée) ; images ; producteur iLovePDF, ModDate 2025-08-07.
- Titre exact : « URBAN RIG Demo Test Operation Test Report ».
- Émetteur : « One World Techno Co., Ltd. » ; « Request destination » : « One World Co., Ltd. » ; date d'essai : « December 12, 2020 » ; lieu : « One World Techno Okayama Head Office Factory » ; « Experiment Manager » : « Sakano » ; « Driver » : « Itakura and Ishikawa ». Laboratoire : aucun. N° de rapport : aucun. Accréditation : aucune.
- Nature : **mesure du constructeur** (essai réalisé et pesé par One World Techno dans son usine, pour One World Co., Ltd.).

| Page | Grandeur | Valeur | Unité | Citation exacte | Conditions | Nature |
|---|---|---|---|---|---|---|
| 1 | Machine | 4,8 t (n° 2) | | « 4.8 ton machine (No. 2) URB-50-2 » | | mesure constructeur |
| 1 | Matière, masse entrée | 450 | kg | « 450kg of waste tires » | pneus usagés ; pesée au peson (photo 1) | idem |
| 1 | Météo, température ext. | 12 | °C | « Sunny », « 12°C » | | idem |
| 1 | Horaires | 9:44 à 5:52 PM | | « Start time 9:44 » « End time 5:52 PM » | durée 488 min (calcul Claude) | idem |
| 1 | Combustible | approx. 280 | AMBIGU : unité coupée | « Heavy oil A: approx. 280 » | fioul lourd A ; l'unité est tronquée par la case (zoom 300 dpi) | idem |
| 1 | Électricité, eau | vides | | « Power consumption » (case vide) ; « Water usage » (case vide) | NON RENSEIGNÉ | idem |
| 1 | Consignes vapeur surchauffée / four | pas 4 : 120 min, 500 / 350 °C ; pas 6 : 150 min, 500 / 450 °C ; pas 9 : 180 min, 530 / 530 °C ; pas 11 et 13 : 0, 530 / 530 ; pas 15 : 60 min, 150 / 150 ; pas 16 : 1, 0 / 0 | min, °C | ligne « 4 120 500 120 350 Driving Open ... » etc. (lu sur image) | colonnes « Superheated steam Time Temperature » et « Pyrolysis Furnace Time Temperature » | idem |
| 1 | Rendements | 111 kg fil ; 133 kg charbon ; env. 180 L huile | kg, L | « The weight of each component after pyrolysis was 111 kg of wire, 133 kg of charcoal, and approximately 180 L of oil. » | | idem |
| 1 | Conclusion | | | « The next challenge is to shorten the processing time. » | | idem |
| 2 | Courbes de température | échelle 100 à 500 °C | | « About the temperature graph » ; TE1 « Steam temperature », TE2 « Superheated steam outlet temperature », TE3 « Superheated steam furnace inlet temperature », TE4 « Combustion chamber temperature », TE5 « Furnace lower temperature », TE6 « Medium temperature inside the furnace », TE7 « Furnace top temperature », TE9 « Off-gas catalyst outlet temperature » ; horodatage « 2020/12/12 17:52:02 » | photo d'écran ; valeurs non lisibles avec précision, aucune valeur relevée | idem |
| 3 | Rendements (rappel) | 133 ; 111 ; env. 180 | kg ; kg ; L | « Charcoal: 133 kg Metal (wire): 111 kg Oil: approx. 180 L » | 12 photos de pesée (« measurementWire1 » à « Wire8 », « Wire Measuring all at once », « Measuring carbides together ») | idem |

Contrôles (calcul Claude) : 450 − 111 − 133 = 206 kg pour l'huile, le gaz et l'eau ; l'huile est donnée en volume sans densité, le bilan ne peut pas être bouclé. Somme des temps de la colonne « Time » : 511 min contre 488 min entre début et fin : AMBIGU (temps par pas ou cumul non précisé). Pas de gaz, pas d'eau, pas d'électricité mesurés.

---

## 6. documents-fournis/transport installation and maintenance.pdf

- Pages : 1 (tableau pivoté) ; langue : anglais ; image (Canon iR-ADV C5540 III, 2024-01-16, même numérisation que le document 1).
- Titre exact : « Transportation, Installation and Maintenance ».
- Émetteur, destinataire, date : NON INDIQUÉS. Nature : **déclaration (émetteur non identifié)**, aucune mesure.

| Page | Grandeur | 1t | 100t | 200t | Citation exacte | Nature |
|---|---|---|---|---|---|---|
| 1 | Conteneurs 40' | 1 | 65 | 100 | « How many 40' containers for shipment » | déclaration |
| 1 | Jours d'installation sur site | 15 | 25 | 30 | « Days needed for installation onsite » | déclaration |
| 1 | Personnel d'installation | 3 | 7 | 10 | « installation staff » | déclaration |
| 1 | Jours de formation | 30 | 30 | 30 | « Trainning days » | déclaration |
| 1 | Formateurs | 2 | 6 | 9 | « Trainers » | déclaration |
| 1 | Maintenance | « One week operation + 2 hours maintenance » | « 3 months operation + 3 days maintenance » | « 3 months operation + 3 days maintenance » | « Maintenance » | déclaration |

Personnel d'exploitation : NON TROUVÉ. Contradiction : 100 conteneurs pour 200t ici, alors que UR2000-JP p. 6 annonce un corps en 7 morceaux transportés par camion et p. 13 un chargement sur remorques.

---

## 7a. documents-fournis/20231114110656.pdf

- Identification : rapport en trois jours d'essais de démonstration sur déchets plastiques. Pages : 9 ; langue : japonais ; numérisation Canon iR-ADV C5540 III du 2023-11-14.
- Titre exact : « 廃プラスチック_デモ実験報告書(1/3日目) » (puis 2/3, 3/3) ; [trad. Claude] « Rapport d'essai de démonstration, déchets plastiques (jour 1/3) ».
- Émetteur : « 株式会社 ワンワールド・ジャパン 〒547-0016 大阪市平野区長吉長原1-1-20 » ; « 作成 : 代田 » [trad. Claude] « One World Japan K.K., rédigé par Shirota/Daita (lecture du nom non vérifiée) ». Destinataire : non indiqué. Lieu : « 前田環境(株) » [trad. Claude] « Maeda Kankyo K.K. ». Dates : 2021/12/1, 12/2, 12/3. Machine : « URT-10 » (montée sur camion, photos). But : « 設置許可取得の為のデータ収集 » [trad. Claude] « collecte de données pour obtenir un permis d'installation ». Laboratoire : aucun ; pesées sur balance (photos).
- Nature : **mesure du constructeur** (One World Japan rédige et pèse).

| Page | Grandeur | Valeur | Unité | Citation exacte | Traduction [trad. Claude] | Conditions | Nature |
|---|---|---|---|---|---|---|---|
| 1 | Horaires J1 | 9:00 / 16:20 / 19:20 | | « 開始時間 9:00 加熱終了 16:20 終了時間 19:20 » | « début, fin de chauffe, fin » | 2021/12/1, URT-10 | mesure constructeur |
| 1 | Matière J1 | 99,7 | kg | « 試料 廃プラスチック類 組成 PP,PE,PS等メイン 重量 99.7kg » | « déchets plastiques, surtout PP, PE, PS » | sac big-bag placé dans un panier | idem |
| 1 | Consignes | 350 / 450 / 500 | °C | « 熱分解炉を350℃、450℃、500℃に設定 » | « four réglé à 350, 450, 500 °C » | | idem |
| 2 | Résultats J1 | entrée 99,7 ; résidu 5,4 ; perte 94,3 ; huile 69,6 | kg | « 投入前重量 99.7kg 取出後重量 5.4kg 減量 94.3kg » ; « 油重量 69.6kg » | « masse avant, masse après, perte ; masse d'huile » | | idem |
| 2 | Taux J1 | réduction 95 ; résidu 5 ; huile 70 ; off gas et autres 25 | % | « 減量率 95% 残渣率 5% » « 油化率 70% オフガス他 25% » | | | idem |
| 2 | Méthode de pesée | 3,2 ; 8,6 ; 28 ; 97,6 | kg | « プラ舟重量は3.2kgであり、処理後残渣を含めた重量は8.6kgであるので、処理後重量は5.4kgとなる。 » ; « ドラム缶＋油の重量(97.6kg)-ドラム缶重量(28kg) =油重量(69.6kg) » | tare du bac 3,2 kg, tare du fût 28 kg | | idem |
| 2 | Observations J1 | | | « 残渣率が5%である為、残りの25%がオフガスもしくは水分と考えられる。 » ; « 触媒層からオフガスの漏れがあったため、改良する必要あり。 » ; « 400℃帯で油の抽出も多く見られた。 » ; « 状態は比較的軽油に近いように見え、燃焼も長持ちし、良好であった。 » | « les 25 % restants seraient de l'off gas ou de l'eau » ; « fuite d'off gas au lit catalytique, à améliorer » ; « extraction d'huile importante vers 400 °C » ; « aspect proche du gazole, combustion longue » | appréciation visuelle, pas d'analyse | idem |
| 3 | Programme four / vapeur J1 | 10 pas, total 620 | min | « 合計 620分 » ; pas 1 « 20分 250℃加熱 / 20分 300℃加熱 » ... pas 10 « 120分 100℃ / 120分 100℃ » (lu sur image, zoom 250 dpi) | « programme du four de pyrolyse / vapeur surchauffée » | four : 250, 350, 450, 500 °C puis 300, 100 ; vapeur : 300, 400, 500, 550 puis 300, 100 | idem |
| 4 | Horaires J2 | 9:10 / 16:30 / 19:30 | | « 開始時間 9:10 加熱終了 16:30 終了時間 19:30 » | | 2021/12/2 | idem |
| 4 | Matière J2 | 99,7 | kg | « PP,PE,PS等メイン(ごく一部FRP有り) 重量 99.7kg » | « avec une très petite part de PRV » | | idem |
| 5 | Résultats J2 | entrée 99,7 ; résidu 4 ; perte 95,7 ; huile 87,3 | kg | « 99.7kg 取出後重量 4kg 減量 95.7kg » ; « 油重量 87.3kg » | | tares 3,2 kg et 28,5 kg ; « ドラム缶＋油の重量(115.8kg)-ドラム缶重量(28.5kg)= 油重量(87.3) » | idem |
| 5 | Taux J2 | réduction 96 ; résidu 4 ; huile 88 ; off gas et autres 8 | % | « 減量率 96% 残渣率 4% » « 油化率 88% オフガス他 8% » | | | idem |
| 5 | Observations J2 | 167 °C après 180 min | | « 1/3日目の気液分離槽オフガスが液化したものも含まれていると想定。 » ; « 今回冷却は蒸気を出さずに行った。 » ; « 炉内温度は180分の冷却で167℃まで下げられていた。 » ; « 油の状態は前回より色が濃く、若干とろみも見られた。 » | « on suppose que l'huile inclut l'off gas du séparateur gaz-liquide du jour 1 » ; « refroidissement sans vapeur » ; « four à 167 °C après 180 min » ; « huile plus sombre, un peu visqueuse » | | idem |
| 6 | Programme J2 | identique au J1, total 620 | min | « 合計 620分 » (lu sur image) | | | idem |
| 7 | Horaires J3 | 8:40 / 16:00 / 18:30 | | « 開始時間 8:40 加熱終了 16:00 終了時間 18:30 » | | 2021/12/3 | idem |
| 7 | Matière J3 | 99,8 | kg | « PP,PE,PS等メイン(塩ビ管含む) 重量 99.8kg » | « avec des tubes PVC » | | idem |
| 8 | Résultats J3 | entrée 99,8 ; résidu 3,6 ; perte 96,2 ; huile 91,3 | kg | « 99.8kg 取出後重量 3.6kg 減量 96.2kg » ; « 油重量 91.3kg » | | tares 3,2 kg et 27,6 kg ; « (118.9kg)-ドラム缶重量(27.6kg)= 油重量(91.3) » | idem |
| 8 | Taux J3 | réduction 96 ; résidu 4 ; huile 91 ; off gas et autres 5 | % | « 減量率 96% 残渣率 4% » « 油化率 91% オフガス他 5% » | | | idem |
| 8 | Observation J3 (PVC) | | | « 処理後残渣はほとんど炭化されているが、塩ビに関しては融点で止まっている。 » | « résidu presque entièrement carbonisé, mais le PVC s'est arrêté au stade de la fusion » | | idem |
| 8 | Total J1 à J3 | entrée 299,2 ; résidu 13 ; perte 286,2 ; huile 248,2 | kg | « 投入前重量 299.2kg 取出後重量 13kg 減量 286.2kg » « 油重量 248.2kg » | | | idem |
| 8 | Taux total | réduction 96 ; résidu 4 ; huile 83 ; off gas et autres 13 | % | « 減量率 96% 残渣率 4% » « 油化率 83% オフガス他 13% » | | | idem |
| 8 | Commentaire | | | « 油化率に関しては83%とあるが、気液分離槽で凝縮化しきれていない油も含めると更に増える可能性がある。 » | « le taux d'huile pourrait augmenter si l'on compte l'huile non condensée dans le séparateur » | | idem |
| 9 | Programme J3 | pas 10 : 90 min ; total 590 | min | « 10 90分 100℃ » « 合計 590分 » (lu sur image) | | | idem |

Contrôles (calcul Claude) : off gas par différence J1 24,7 kg (24,8 %), J2 8,4 kg, J3 4,9 kg ; total 38,0 kg soit 12,7 % ; huile totale 248,2 / 299,2 = 82,95 % : les taux écrits sont des arrondis cohérents. Les sommes 99,7 + 99,7 + 99,8 = 299,2 ; 5,4 + 4 + 3,6 = 13 ; 69,6 + 87,3 + 91,3 = 248,2 bouclent. Durées des programmes (620, 620, 590 min) égales aux écarts début/fin. Électricité, combustible, eau, vapeur : NON TROUVÉ dans ce rapport. Le gaz n'est pas mesuré (calculé par différence avec l'eau). La teneur en eau de l'« huile » n'est pas mesurée.

---

## 7b. documents-fournis/20250317183955.pdf

- Identification : courrier d'accompagnement et résultats d'une analyse GC-MS d'un échantillon de « drain » par un laboratoire public d'Osaka. Pages : 6 ; langue : anglais (p. 1 et 2, traduction vraisemblable du japonais, non indiquée), japonais (p. 3 à 6) ; numérisation Canon iR-ADV C5540 III du 2025-03-17.
- Titre : aucun. Début : « Dear Sirs, Now that the analysis of the samples has been completed, I am pleased to report the results of the drain analysis as shown in the attached file. »
- Émetteur : « Local Incorporated Administrative Agency Osaka Institute of Industrial Science and Technology / Izumi Center, Osaka Industrial Technology Research Institute / Applied Materials Chemistry Research Department ». Signataire : non nommé. Destinataire : « Dear Sirs » (non nommé). Date de l'analyse : NON INDIQUÉE. Identifiant d'échantillon sur le chromatogramme : « 081403-Fr-JCE-ドレン-10C6.D ». N° de rapport : aucun. Accréditation : non mentionnée. Machine, date et matière d'origine de l'échantillon : NON INDIQUÉES.
- Nature : **mesure par un tiers** (laboratoire public nommé) ; c'est une communication préalable et non le rapport formel : « Note that no chart will be included in the report. The "probable compounds" will be listed in the report, but "possible compounds" will not ».

| Page | Grandeur | Valeur | Unité | Citation exacte | Traduction [trad. Claude] | Conditions | Nature |
|---|---|---|---|---|---|---|---|
| 1 | Méthode | 350 °C | | « (1) Analysis chart when heated at 350°C » ; « (3) Result of measurement of strong thermal residues by heating at 350° C for 5 minutes » | | GC-MS, recherche en bibliothèque | tiers |
| 1 | Résidu non volatil | environ 50 | % | « Incidentally, about 50% remained without volatilization after heating at 350° C for 5 minutes. » | | | tiers |
| 2 | Limites | | | « there were not many peaks that could be completely identified. » | | | tiers |
| 3 | Chromatogramme TIC | 8 à 39 | min | « + TIC スキャン 081403-Fr-JCE-ドレン-10C6.D » ; axe « カウント vs. 測定時間 (min) » ; max « x10 7 » (lu sur image) | « balayage TIC ; comptes en fonction du temps » | pic majeur vers 9,3 min | tiers |
| 4 | Pic 13 | 21,26 | % d'aire | « 13 9.33 3.50.E+07 21.26 ジメチルヘプテン » | « diméthylheptène » | probable | tiers |
| 4 | Pic 40 | 7,60 | % | « 40 16.72 1.25.E+07 7.60 » ; possible « トリデセン » | « tridécène » (possible) | | tiers |
| 4 | Pic 42 | 6,52 | % | « 42 16.96 1.07.E+07 6.52 ウンデセン » | « undécène » | probable | tiers |
| 4 | Pic 41 | 3,97 | % | « 41 16.83 6.52.E+06 3.97 » ; possible « トリメチルノネン » | « triméthylnonène » | | tiers |
| 4 | Pics 24 et 25 | 3,21 ; 2,61 | % | « ジメチルオクテン » | « diméthyloctène » | probable | tiers |
| 5 | Pic 77 | 3,45 | % | « 77 22.34 5.67.E+06 3.45 » ; possible « アリルシュウヘキサデシル » | « oxalate d'allyle et d'hexadécyle » (possible) | | tiers |
| 5 | Pic 119 | 2,77 | % | « 119 32.49 4.56.E+06 2.77 不明 » | « inconnu » | | tiers |
| 5 | Pics « 長鎖アルコール » | 1,52 ; 0,96 ; 0,78 ; 1,28 ; 2,66 | % | pics 81, 100, 101, 108, 110 | « alcool à longue chaîne » (possible) | | tiers |
| 5 | Total | 1,64E+08 ; 100 | aire ; % | « 1.64.E+08 100 » | | | tiers |
| 6 | Résidu thermique (creuset) | creuset 20,6505 ; avant 22,3945 ; après 21,5874 ; échantillon 1,744 → 0,9369 ; résidu 53,7 | g ; % | « るつぼ 20.6505 加熱前 22.3945 加熱後 21.5874 加熱前試料量 1.744 加熱後試料量 0.9369 加熱残量 53.7 » (lu sur image) | « creuset, avant chauffe, après chauffe, masse d'échantillon avant/après, résidu de chauffe » | 350 °C, 5 min (p. 1) | tiers |

Tableau GC complet (p. 4 et 5) transcrit et contrôlé en python : 71 pics listés (numéros 7 à 128, avec des trous), somme des aires 1,644E+08, somme des pourcentages 100,02 ; chaque pourcentage est égal à l'aire / somme à 0,03 point près. Répartition (calcul Claude) : composés « probables » nommés 46,0 % ; « 不明 » (inconnus) 14,5 % ; « possibles » seulement 39,5 %. Les pics non listés (1 à 6, 11, 23, etc.) sont exclus du total de 100 %. Le tableau détaillé ligne par ligne est disponible dans `scratchpad/en/gc.py` (transcription), non recopié ici.
Contrôle (calcul Claude) : 22,3945 − 20,6505 = 1,744 ; 21,5874 − 20,6505 = 0,9369 ; 0,9369 / 1,744 = 53,72 %, conforme au 53,7 écrit ; le courrier dit « about 50% ».
Utilité pour l'annexe 2 : composition qualitative d'un « drain » (eau ou huile de purge, non précisé), majoritairement des alcènes ramifiés C9 à C13 et des composés lourds (environ 54 % non volatils à 350 °C). Pas de PCI, pas de soufre, pas de chlore, pas de densité.

---

## Remarques

Ce qui manque :
- Aucun document de ce lot ne donne de pouvoir calorifique mesuré (huile, gaz, char) avec un laboratoire et une méthode ; les PCI de energy-balance.xlsx sont des facteurs appliqués sans source.
- Aucune mesure d'électricité ni d'eau dans les deux rapports d'essai du constructeur (2020 et 2021) ; le combustible de 2020 est « approx. 280 » sans unité lisible.
- Aucune émission mesurée par un tiers dans ce lot ; le graphique SOx/NOx de la brochure n'a ni date, ni O2 de référence, ni laboratoire.
- Le personnel d'exploitation n'est donné nulle part (seulement installation et formation).
- Les documents 1 et 6 ne portent ni émetteur ni date.
- Le courrier du laboratoire d'Osaka n'identifie ni l'échantillon (machine, date, matière), ni l'analyste, ni la méthode normalisée ; le rapport formel annoncé n'est pas dans le dossier.

Contradictions entre documents :
- Électricité 200t : 20 « kw/h » (UR2000-JP p. 8) contre 600 « kW/h » (document 1 et feuille Lufthansa).
- Combustible : « 軽油 » gazole (UR2000-JP p. 8), « 灯油 » kérosène (UR2000-JP p. 12), « Light Oil » (Chiba / energy-balance), « Heavy oil A » (essai 2020), « Oil » (document 1).
- Fioul 200t consommé 10 000 L/jour (document 1) égal à l'huile produite 10 000 L/jour annoncée (UR2000-JP p. 5) : bilan net nul sur cette base déclarative.
- Rendement huile : 5 % de l'entrée (UR2000-JP, ordures ménagères à 10 % de résines) ; 32 à 82 % (Chiba, recalculé : 16,1/50 = 32 % et 22,5/50 = 45 % sur déchets mélangés ; 43,1/60 = 72 % et 49,4/60 = 82 % sur 3P) ; 70 à 91 % (essais One World 2021, plastiques) ; 0,85 coefficient saisi (Lufthansa). Les matières diffèrent ; aucune base commune.
- Températures de zones : deux jeux différents dans la même brochure (p. 4/8 et p. 12).

Points à demander au constructeur :
1. Unité et nature exactes du tableau « UR Energy Consumption » (kW ou kWh, par heure, lot ou jour), auteur, date, et conditions de mesure ; type de fioul.
2. Unité du « Heavy oil A: approx. 280 » de l'essai du 12/12/2020 ; densité de l'huile ; masse de gaz et d'eau.
3. Consommation électrique réelle de l'URC-2000 (20 ou 600) et consommation de combustible mesurée sur une machine en service.
4. Quel combustible pour les chaudières (gazole, kérosène, fioul A) et débit de vapeur.
5. Composition, PCI et teneur en eau de l'huile, du gaz et du char, par un laboratoire nommé, avec méthode.
6. Origine de l'échantillon « 081403-Fr-JCE-ドレン-10C6.D » et le rapport formel du laboratoire d'Osaka.
7. Conditions du graphique SOx/NOx (date, combustible, O2 de référence, laboratoire), dioxines, HCl, poussières mesurés.
8. Effectif d'exploitation par poste pour la 200t.
9. Identité de « Peter » (feuille Lufthansa) et origine du coefficient 0,85, des 10 000 L/jour et de la constante 47.
10. Correction des cellules Q24/Q25 du 15 septembre dans le rapport de Chiba (valeurs reportées du 11 juillet).
