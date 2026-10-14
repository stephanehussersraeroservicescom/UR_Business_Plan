# Composition et tonnages des ordures ménagères en France

Recherche du 10/10/2026. Chaque chiffre renvoie à un identifiant de `registre-sources.yaml`. Les citations sont en langue d'origine.

**Point clé :** le MODECOM 2024 (ADEME, décembre 2025) remplace le MODECOM 2017 comme référence de composition. Le plan doit citer 2024 en principal et 2017 en historique.

---

## 1. Composition des OMR (ordures ménagères résiduelles, poubelle grise)

### 1.1 MODECOM 2024 (référence)

Source : [ADEME-MODECOM-2024-DATA](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv) (données ouvertes ADEME, colonnes `pourcentage_OMR`, `ratio_OMR`, `tonnage_OMR`). France hexagonale. Les totaux par catégorie sont la somme des sous-catégories publiées **[calcul]**. Statut : `verifie-recontrole` pour les plastiques.

| Catégorie | % des OMR | kg/hab/an | t/an |
|---|---:|---:|---:|
| Putrescibles | 33,7 % | 75,25 | 4 966 318 |
| Textiles sanitaires | 17,0 % | 37,97 | 2 505 734 |
| **Plastiques** | **15,8 %** | **35,28** | **2 329 258** |
| Cartons | 6,6 % | 14,76 | 973 969 |
| Papiers | 5,8 % | 12,95 | 854 481 |
| Verre | 5,0 % | 11,20 | 739 213 |
| Textiles | 4,9 % | 10,89 | 718 435 |
| Métaux | 3,3 % | 7,48 | 493 070 |
| Autres matières minérales | 2,2 % | 4,86 | 320 842 |
| Composites | 2,0 % | 4,46 | 294 383 |
| Autres matières organiques | 1,5 % | 3,45 | 227 604 |
| Déchets dangereux ou spécifiques | 1,3 % | 2,84 | 186 789 |
| Bois | 1,0 % | 2,15 | 141 917 |
| **Total** | 100 % | **223,54** | **14 752 013** |

Les éléments fins sont répartis dans les catégories ci-dessus.

Recoupement : [ADEME-CP-2025](https://www.ademe.fr/presse/communique-national/poubelles-des-francais-des-progres-sur-le-tri-des-dechets-mais-encore-des-marges-importantes-damelioration/) : « les Français ont produit en moyenne 223,5 kg d'OMR contre 252,7 kg en 2017 ».

**Détail des plastiques dans les OMR, 2024** ([ADEME-MODECOM-2024-DATA](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv))

| Sous-catégorie | % OMR | kg/hab/an |
|---|---:|---:|
| Films plastiques d'emballage | 4,2 | 9,39 |
| Sacs poubelles | 3,4 | 7,52 |
| Boîtes, caisses, pots, barquettes, gobelets | 3,0 | 6,73 |
| Autres plastiques (hors emballage) | 1,5 | 3,29 |
| Autres sacs plastiques | 1,1 | 2,50 |
| Bouteilles et flacons PET, boissons | 1,1 | 2,44 |
| Bouteilles et flacons PET, hors boissons | 0,3 | 0,78 |
| Bouteilles et flacons polyoléfines (boissons et hors boissons) | 0,5 | 1,03 |
| Bouchons, couvercles, capsules | 0,3 | 0,61 |
| Autres emballages plastiques | 0,3 | 0,61 |
| Jouets, articles de sport, autres bouteilles | 0,1 | 0,38 |

Regroupements **[calcul]** :
- films et sacs : **8,7 %** des OMR (≈ 1,28 Mt) ;
- emballages rigides : environ 5,5 % ;
- plastiques hors emballage : environ 1,6 %.

Pour la pyrolyse, les films et sacs (PE majoritaire) sont donc la première fraction plastique des OMR.

**Humidité des OMR, 2024** ([ADEME-MODECOM-2024-HUM](https://data.ademe.fr/data-fair/api/v1/datasets/omrhum)) :
- moyenne : **42,1 %** (demi-intervalle de confiance 5,78 points) ;
- films et sacs : 35,8 % ; autres plastiques : 20,1 % ;
- putrescibles : 59,6 % ; textiles sanitaires : 60,0 %.

**Messages ADEME sur 2024** ([ADEME-ORDIF-2026](https://www.ordif.fr/fileadmin/DataStorageKit/ORDIF/Event/2026_06_23/2026_01.3_ADEME_MODECOM_2024_VF.pdf), présentation du 23/06/2026) :
- « de : 396 kg/hab./an en 1993 à 223 kg/hab./an en 2024 » ;
- « 32 % des OMR (poubelle grise) restent constitués de biodéchets » ;
- « 70% des déchets présents n'y ont pas leur place » ;
- tout-venant de déchèterie : « 18 % » de plastiques.

### 1.2 MODECOM 2017 (historique)

Source : [ADEME-MODECOM-2017](https://medias.amf.asso.fr/upload/files/modecom_2017_analyse_des_resultats_011318.pdf), Tableau 3, p. 16-17, après ventilation des éléments fins. Statut : `verifie`.

| Catégorie | % OMR | kg/hab/an | kt/an |
|---|---:|---:|---:|
| Putrescibles | 32,8 | 83,1 | 5 372 |
| **Plastiques** | **14,7** | **37,3** | **2 410** |
| Textiles sanitaires | 13,9 | 35,3 | 2 282 |
| Papiers | 8,6 | 21,9 | 1 412 |
| Cartons | 6,4 | 16,3 | 1 051 |
| Verre | 5,3 | 13,6 | 877 |
| Combustibles non classés | 4,6 | 11,6 | 750 |
| Incombustibles non classés | 4,3 | 10,8 | 700 |
| Métaux | 3,4 | 8,7 | 564 |
| Textiles | 3,0 | 7,7 | 497 |
| Composites | 2,3 | 5,9 | 383 |
| Déchets dangereux | 0,6 | 1,6 | 102 |
| **Total** | 100 | **253,7** | **16 400** |

Caractéristiques physico-chimiques 2017 (p. 26-27) :
- humidité moyenne : **36,9 %** ;
- carbone organique total des plastiques : 55,0 % ;
- carbone biogénique : 24 % de la masse sèche (Tableau 7).

Composition des OMA (OMR + collectes séparées), Tableau 17, p. 40-41 : plastiques 44,9 kg/hab/an, soit 13 % des OMA.

### 1.3 Points d'attention

- **PCI des OMR : `non-verifie`.** Aucune source officielle française ne donne un PCI. Ne pas citer de valeur sans source.
- La présentation SINOE de 2019 donnait « Plastiques : 15 % » pour 2017. Retenir le rapport final : 14,7 %.
- Les Chiffres-clés ADEME 2023 (p. 25) donnent 83 kg de putrescibles pour l'ensemble « OM, OMR et collectes séparées ». Ce n'est pas la composition des seules OMR.

---

## 2. Tonnages annuels

### 2.1 DMA et OMR

| Indicateur | Valeur | Année | Source | Statut |
|---|---|---|---|---|
| DMA collectés par le service public | **37,8 Mt ; 559 kg/hab** | 2023 | [ADEME-COLLECTE-2023](https://librairie.ademe.fr/economie-circulaire-et-dechets/8644-10426-la-collecte-des-dechets-par-le-service-public-en-france.html) | verifie |
| DMA produits | 571 kg/hab | 2023 | [ADEME-IND-DMA](https://economie-circulaire.ademe.fr/indicateurs-cles-dma) | verifie |
| OMR collectées | **15,2 Mt ; 225 kg/hab** | 2023 | [ADEME-IND-DMA](https://economie-circulaire.ademe.fr/indicateurs-cles-dma) | verifie |
| OMR (base MODECOM) | 14,75 Mt ; 223,5 kg/hab | 2024 | [ADEME-MODECOM-2024-DATA](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv) | calcul |
| DMA collectés | 615 kg/hab | 2021 | [INSEE-IP2055](https://www.insee.fr/fr/statistiques/8574484) | verifie-recontrole |
| OMR collectées | 245,1 kg/hab | 2021 | [INSEE-IP2055](https://www.insee.fr/fr/statistiques/8574484) | verifie-recontrole |
| Origine des OMR | 80 % ménages, 20 % activités économiques | 2017 | [ADEME-CC-2023](https://www.ordeec.org/fileadmin/user_upload/dechets-chiffres-cles-2023_si.pdf), figure 24, p. 27 | verifie |

Série OMR (kg/hab) d'après [ADEME-IND-DMA](https://economie-circulaire.ademe.fr/indicateurs-cles-dma) : 293 (2010), 269 (2013), 254 (2017), 248 (2019), 246 (2021), 225 (2023).

Écart à signaler : 15,2 Mt (ADEME, France entière) contre 14,75 Mt (MODECOM, France hexagonale). Cause probable : périmètre géographique (hypothèse non vérifiée).

### 2.2 Tous déchets, tous secteurs

Source : [SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline), Tableau 1. Statut : `verifie`. Recoupé avec [EUROSTAT-WASGEN](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_wasgen?geo=FR) (343 210 526 t).

| Secteur | Production 2022 |
|---|---:|
| Construction | 247,4 Mt |
| Ménages | 31,3 Mt |
| Traitement des déchets, eau, assainissement | 25,3 Mt |
| Industrie | 19,6 Mt |
| Tertiaire | 17,0 Mt |
| Agriculture et pêche | 2,5 Mt |
| **Total** | **343 Mt (5,1 t/hab)** |

Citation : « En 2022, 343 millions de tonnes ont été produites. » Le SDES précise que 2022 n'est pas directement comparable aux années précédentes (changement de méthode). Pour 2020 : 310 Mt ([ADEME-CC-2024](https://batisseurs-outremer.com/wp-content/uploads/2025/01/ChiffresclesDechets-Synthese2024-012515.pdf)) ou 315 Mt ([ADEME-CC-2023](https://www.ordeec.org/fileadmin/user_upload/dechets-chiffres-cles-2023_si.pdf)).

---

## 3. Modes de traitement

### 3.1 OMR (2021)

[INSEE-IP2055](https://www.insee.fr/fr/statistiques/8574484) (statut `verifie-recontrole`) : « 67,9 % des ordures ménagères résiduelles sont destinées à l'incinération », « 23,1 % au stockage, 7,2 % à la valorisation organique ».

### 3.2 DMA (2021)

[INSEE-IP2055](https://www.insee.fr/fr/statistiques/8574484), figure 3, et [SINOE-DEST-DMA](https://data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-destination-des-dma-collectes-par-type-de-traitement) pour les tonnages **[calcul : sommes]**.

| Mode | % | Tonnes |
|---|---:|---:|
| Valorisation matière | 33,1 % | 13 535 042 |
| Incinération avec récupération d'énergie | 29,9 % | 12 265 799 |
| Stockage (ISDND) | 16,0 % | 6 716 471 |
| Valorisation organique | 15,7 % | 6 412 738 |
| Stockage pour inertes | 3,8 % | 1 583 190 |
| Non précisé | 1,4 % | 503 223 |
| Incinération sans récupération d'énergie | 0,1 % | 61 517 |
| **Total** | 100 % | **≈ 41,1 Mt** |

DMA 2023 ([BDT-2025](https://www.banquedesterritoires.fr/service-public-de-gestion-des-dechets-une-collecte-en-baisse-en-2023), statut `secondaire`) : recyclage 34 %, valorisation organique 16 %, stockage 15 % (31 % en 2007).

### 3.3 Autres repères

- Incinération avec récupération d'énergie : de 10,3 à 14,5 Mt/an entre 2000 et 2020 ; 119 UIOM en 2020 ([ADEME-VE](https://economie-circulaire.ademe.fr/valorisation-energetique-dechets)).
- Stockage de déchets non dangereux non inertes : 13,9 Mt en 2023, 15,1 Mt en 2022 ([ADEME-IND-DMA](https://economie-circulaire.ademe.fr/indicateurs-cles-dma)). Objectif 2025 : 9,7 Mt (non atteint fin 2023).
- CSR : plus de 300 000 t consommées par les cimenteries en 2021 ([ADEME-CC-2024](https://batisseurs-outremer.com/wp-content/uploads/2025/01/ChiffresclesDechets-Synthese2024-012515.pdf), p. 37) ; plus de 470 000 t/an détournées du stockage fin 2025 ([ADEME-VE](https://economie-circulaire.ademe.fr/valorisation-energetique-dechets)).

---

## 4. Plastiques en France

| Indicateur | Valeur | Année | Source | Statut |
|---|---|---|---|---|
| Plastiques dans les OMR | **2,33 Mt** | 2024 | [ADEME-MODECOM-2024-DATA](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv) | calcul |
| Plastiques dans les OMR | 2,41 Mt | 2017 | [ADEME-MODECOM-2017](https://medias.amf.asso.fr/upload/files/modecom_2017_analyse_des_resultats_011318.pdf) ; [FNADE-2023](https://www.fnade.org/ressources/documents/source/1/4866-ANALYSE-PROSPECTIVE-FNADE-D-ORIENTATION-DES-FLUX-DE-DECHETS-A-HORIZON-2050-VDEF.pdf), p. 7 | verifie |
| Déchets plastiques collectés séparément | 2 482 kt (dont 380 kt ménages) | 2022 | [SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline), Tableau 2 | verifie |
| Taux de recyclage des plastiques | 20 % | 2022 | [SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline) | verifie |
| Déchets plastiques, total | 3,76 Mt (pour 6,45 Mt consommées) | 2020 | [OPECST-2023](https://www.senat.fr/rap/r22-808/r22-8081.pdf), p. 2-3 | secondaire (pas de source primaire citée) |
| Recyclés en France | 690 kt (18,3 %) | 2020 | [OPECST-2023](https://www.senat.fr/rap/r22-808/r22-8081.pdf) | secondaire |
| Emballages plastiques générés | 2 428 987 t | 2023 | [EUROSTAT-WASPAC](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_waspac?geo=FR&waste=W150102) | verifie |
| Emballages plastiques recyclés | 625 275 t (**25,7 %**) | 2023 | [EUROSTAT-WASPAC](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_waspac?geo=FR&waste=W150102) | verifie |
| Emballages plastiques valorisés en énergie | 1 213 829 t (≈ 50 %) | 2023 | [EUROSTAT-WASPAC](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_waspac?geo=FR&waste=W150102) | calcul |

Lecture : le total des déchets plastiques dépend du périmètre. Les 2,48 Mt du SDES ne couvrent que les plastiques triés à part. Il faut y ajouter les plastiques en mélange (≈ 2,3 Mt dans les seules OMR, plus les déchèteries et les DAE en mélange). D'où l'ordre de grandeur de 3,8 à 4,1 Mt.

**Gisement plastique non recyclé, ordre de grandeur pour le plan [calcul] :** au moins 2,3 Mt/an dans les OMR, qui partent aujourd'hui à 68 % en incinération et 23 % en stockage ([ADEME-MODECOM-2024-DATA](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv), [INSEE-IP2055](https://www.insee.fr/fr/statistiques/8574484)).
