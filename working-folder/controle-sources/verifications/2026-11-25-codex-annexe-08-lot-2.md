# Contre-vérification indépendante de l'annexe 8, lot 2

Date : 2026-11-25  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-08-html/index.html`  
Périmètre : section 8.3, tous les flux, avec recalcul de tous les `CALC-A8` de la section  
Accès internet : OUI  
Lecture des sources originales : OUI

## Méthode et limites

Les statistiques, études, rapports d'éco-organismes et textes réglementaires ont été ouverts. Les quatre calculs de la section ont été refaits. Les prix, tarifs, contributions et coûts n'ont pas été recalculés, conformément aux règles de vérification légère. J'ai seulement vérifié qu'ils sont présentés comme prix observés, hypothèses ou valeurs modifiables.

Le contrôle automatique avec `--echantillon 3` a été lancé. Il a de nouveau classé les 70 affirmations du HTML comme sans source, car il ne reconnaît pas les liens internes vers les fiches de preuve. Ce résultat automatique n'est pas utilisé comme verdict.

## Tableau des verdicts

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---:|---|---|---|---|---|---|---|---|
| 1 | 8.3.1 | Emballages ménagers plastiques mis en marché et recyclés | 1 165 kt et 324 kt en 2024 ; 1 174 kt et 346 kt en 2025 | CITEO-RA-2025 | CONFIRMÉ | « Plastique 1 165 1 174 » ; « Plastiques 324 346 » | PDF p. 13 et p. 29 | Même matériau, mêmes années et même unité. |
| 2 | 8.3.1 | Taux de recyclage des emballages ménagers plastiques | 30 % en 2025 | A8-MENA-CITEOMAG-2026 | CONFIRMÉ | « Plastiques : 30% » | Page Citeo, taux par matériau | Estimation de la filière Citeo. |
| 3 | 8.3.1 | Reprise Valorplast | 120 500 t ; 76 % recyclés en France | A8-MENA-VALORPLAST-2025 | CONFIRMÉ | « 120 500 tonnes d'emballages plastiques ménagers repris » ; « 76% [...] recyclés en France » | Pages Valorplast « Nos engagements » et « Nos missions », chiffres 2025 | Déclaration d'entreprise, pas statistique nationale. |
| 4 | 8.3.1 | Recyclabilité et résines sans filière | 66 % recyclables ; 17 % PVC, complexes ou autres sans filière en 2021 | RP2-036 | CONFIRMÉ | « 66 % des emballages plastiques sont recyclables » ; « 17 % [...] sans filière de recyclage » | Rapport cité, données 2021 | Ancien état de filière, correctement daté dans l'annexe. |
| 5 | 8.3.2 et fiche 8.C.g | CALC-A8-FILMS-REPRIS-T | 97 379 t | A8-MENA-PRIXREPRISE-2025 | CONFIRMÉ | « _07.422 Films emballages ménagers PE [...] 25 370 t » ; « _07.423 Films emballages ménagers PE/PP [...] 72 009 t » | PDF p. 27, tableau « Sous-calcul prix de reprise Plastiques » | 25 370 + 72 009 = 97 379. |
| 6 | 8.3.2 | Flux développement repris | 66 005 t en 2024 | A8-MENA-PRIXREPRISE-2025 | CONFIRMÉ | « _07.451 Flux développement [...] hors films PE/PP [...] 66 005 t » | PDF p. 27 | Tonnage repris, pas tonnage réellement recyclé. |
| 7 | 8.3.2 | Films souples utilisés en entrée de recycleurs en Europe | 18 % en 2020 | PRE-FILMS-2023 | CONFIRMÉ | « only 2.4 million tonnes of flexible films were used as input for recyclers » ; « This represents a recycling rate of 18% » | PDF p. 19 et p. 24-25 | UE27+3, tous segments de films, pas France seule. |
| 8 | 8.3.3 | Refus de tri des centres de tri | 800 000 t ; 23,0 % des entrants en 2022 | CITEO-CAHIER-CS-2024 | CONFIRMÉ | « 800 000 tonnes de refus » ; « 23,0 % » | Cahier Citeo, bilan 2022 | Périmètre collecte sélective. |
| 9 | 8.3.3 | Autre estimation nationale des refus | 750 000 t | OCAPEM-2025 | CONFIRMÉ | « TOTAL 750 000 t » | PDF p. 7, tableau 5 | Année du gisement non précisée dans cette étude. |
| 10 | 8.3.3 | Refus du modèle de coûts public | 496 kt | A8-MENB-DGPR-COUTSREF-2026 | CONFIRMÉ | « Refus de tri 496 kt » | Note de calcul, tableau de tonnages | Modèle de coûts, pas mesure nationale indépendante. |
| 11 | 8.3.3 | Refus franciliens | 146 368 t ; 27 % ; 98 % incinérés en 2024 | RP-034 | CONFIRMÉ | « 146 368 tonnes » ; « 27 % » ; « 98 % [...] incinération » | Rapport ORDIF, bilan 2024 | Même flux et même année. |
| 12 | 8.3.3 et fiche 8.C.b | CALC-A8-REFUS-PART-PLASTIQUE | 12 % | OCAPEM-2025 | CONFIRMÉ | « Rigides 7,5% » ; « Souples 4,5% » | PDF p. 5, tableau 3 | 7,5 + 4,5 = 12,0 %. Il s'agit de la composition moyenne de refus, pas d'un flux plastique trié. |
| 13 | 8.3.3 | Capacités de surtri | 30 000, 25 000, 15 000 et 30 000 t/an ; dernier fin 2026 | RP-021 | CONFIRMÉ | « 30 000 tonnes » ; « 25 000 tonnes » ; « 15 000 tonnes » ; « fin 2026 » | Sources des quatre projets regroupées dans la fiche | Capacités annoncées, pas tonnages effectivement traités. |
| 14 | 8.3.4 | Gisement PS ménager | 100 000 t/an, dont 60 000 t de pots | A8-PS-CITEOAO-2022 | CONFIRMÉ | « 100 000 tonnes mises en marché chaque année, dont 60 000 tonnes de pots sécables » | Communiqué Citeo du 21 décembre 2022, p. 1 | Une publication Citeo de septembre 2025 donne désormais 85 000 t pour tous les emballages PS, mais maintient 60 000 t pour le PS compact. Voir E-3. |
| 15 | 8.3.4 et fiche 8.C.h | CALC-A8-PS-PART-TRIE | environ 8 % | A8-PS-QUECHOISIR-2025 ; A8-PS-CITEOAO-2022 | CONFIRMÉ | « seules 5 000 tonnes [...] arrivent dans les centres de tri, d'après Citeo » ; « 60 000 tonnes de pots sécables » | Que Choisir, 1 avril 2025 ; communiqué Citeo p. 1 | 5 000 / 60 000 x 100 = 8,3333 %. Le numérateur est secondaire, attribué à Citeo. |
| 16 | 8.3.4 | Débouchés du PS compact trié | Espagne auparavant ; 80 % Indaver et 20 % Eslava depuis septembre 2025 | A8-PS-CITEOMAP-2024 ; A8-PS-CITEOINDAVER-2025 | CONFIRMÉ | « principalement recyclés en pots de fleurs ou en cintres » ; « Chez Indaver [...] 80 % des tonnages » ; « Chez Eslava [...] 20 % » | Communiqués Citeo, p. unique | Le tonnage effectivement recyclé n'est pas publié, ce que l'annexe dit. |
| 17 | 8.3.5 | PSE ménager | environ 15 000 t ; 1 200 t/an triées ; aucun exutoire propre | A8-PS-CITEOPSE-2025 | CONFIRMÉ | « environ 15 000 tonnes » ; « seulement 1 200 T/an triées » ; « n'a pas d'exutoire en propre » | PDF p. 2-3 | La source ajoute que les recycleurs n'acceptent le PSE en mélange qu'à moins de 5 %. |
| 18 | 8.3.5 | Collecte du PSE en déchèterie | 15 % des déchèteries ; plus de 600 t sur 200 sites | A8-PS-AN14052-2026 ; A8-PS-CITEOPSE-2025 | CONFIRMÉ | « 15% des déchèteries en France » ; « plus de 600 tonnes collectées sur 200 déchetteries » | Amendement AN et feuille de route Citeo p. 4 | Tonnage collecté, pas recyclé. |
| 19 | 8.3.5 | PSE commercial et taux issus de l'industrie | 71 kt ; 33 % tous emballages PSE ; 50 % commerciaux | A8-PRO-NOTE-SOUTIENS-EPRO-2026 ; A8-PS-FAM-2023 | CONFIRMÉ | « 71 kt » ; « 33% des emballages polystyrène expansé ménagers, industriels et commerciaux » ; « recyclés à hauteur de 50% » | Note EPRO ; étude FranceAgriMer p. 23 et p. 37-44 | Les taux 33 % et 50 % viennent de la fédération industrielle EUMEPS, reprise par FranceAgriMer. |
| 20 | 8.3.5 | Seuil POP du HBCDD | 1 000 mg/kg initialement ; 500 mg/kg actuellement ; 200 mg/kg après réexamen éventuel | A8-PS-POP2019-2019 ; A8-PS-OEIL2400-2022 | CONFIRMÉ | « Hexabromocyclododecane [...] 500 mg/kg » ; « shall review [...] and, where appropriate, adopt a legislative proposal [...] not higher than 200 mg/kg » | Règlement (UE) 2022/2400, annexe IV | Le texte de l'annexe dit bien que 200 mg/kg dépend d'un réexamen, ce n'est pas une baisse automatique. |
| 21 | 8.3.6 | Emballages professionnels plastiques | 1 074 kt non dangereux, dont 307 kt de PEBD souple ; recyclage 26 % en 2023 | A8-PRO-NOTE-SOUTIENS-EPRO-2026 | CONFIRMÉ | « Plastiques 1 074 kt » ; « PEBD souple 307 kt » ; « 26 % » | Note de soutien EPRO, tableaux de gisement et de recyclage | Données de cadrage de la nouvelle REP. |
| 22 | 8.3.6 | Déchets plastiques d'activité en Île-de-France | 260 000 t/an ; 17 % recyclés ; moitié de la part commerce en films palettes | A8-PRO-IDF-LIVRET-2023 | CONFIRMÉ | « Sur l'ensemble des 260000 tonnes par an de déchets d'activité économique » ; « seuls 17 % » ; « la moitié est constituée de films étirables pour palettes » | Livret ADEME/Région p. 39-41 | Le tonnage source n'est pas accompagné de sa méthode d'origine. |
| 23 | 8.3.6 | Objectifs REP emballages professionnels | 50 % en 2028 ; 55 % en 2030 | A8-PRO-CDC-EPRO-2025 | CONFIRMÉ | « 50 % en 2028 » ; « 55 % en 2030 » | Arrêté du 2 décembre 2025, cahier des charges | Objectifs légaux exacts. |
| 24 | 8.3.6 | Statut du report de la REP | Report présenté comme provenant d'un projet d'arrêté | A8-PRO-REPORT-EPRO-2026 | DIFFÉRENT | « les mots “1er juillet 2026” sont remplacés par les mots “1er janvier 2027” » | Arrêté définitif du 3 novembre 2026, JORF n° 0259 du 5 novembre 2026 | Le report au 1er janvier 2027 est confirmé, mais il n'est plus au stade de projet. |
| 25 | 8.3.7 | Plastiques agricoles collectés | 84 500 t en 2025 | A8-PRO-ADIVALOR-RA-2025 | CONFIRMÉ | « 84 500 tonnes de plastiques agricoles collectées » | Rapport A.D.I.VALOR 2025, p. 7 | La source compte séparément 21 500 t d'emballages. |
| 26 | 8.3.7 | Taux de collecte associé aux 84 500 t | 75 % | A8-PRO-ADIVALOR-RA-2025 | DIFFÉRENT | « Avec un taux de collecte global de 75 % » | Rapport A.D.I.VALOR 2025, p. 3 et p. 7 | Le 75 % est global à tous les flux A.D.I.VALOR, pas démontré pour les seuls 84 500 t de plastiques d'élevage et de maraîchage. |
| 27 | 8.3.7 | Recyclage des déchets agricoles collectés | 90 % | A8-PRO-ADIVALOR-RA-2025 | CONFIRMÉ | « Près de 90 % des déchets collectés ont été recyclés » | Rapport et actualité A.D.I.VALOR, chiffres 2025 | Taux déclaré par l'éco-organisme. |
| 28 | 8.3.7 | Gisement annuel de films agricoles usagés | 70 000 à 85 000 t/an | A8-PRO-ADIVALOR-RA-2024 | CONFIRMÉ | « La quantité totale de films usagés à collecter annuellement est estimée entre 70 et 85 000 tonnes. » | Rapport A.D.I.VALOR 2024 | Estimation de gisement, pas collecte effectivement disponible. |
| 29 | 8.3.8 | Plastiques collectés et recyclés par la fédération | 1 024 000 t en 2024 ; 69 % d'origine industrielle | RP2-041 | CONFIRMÉ | « 1 024 000 tonnes » ; « 69 % d'origine industrielle » | Bilan FEDEREC 2024 | Le chiffre agrège des plastiques recyclés par la filière, pas les seules chutes propres disponibles. |
| 30 | 8.3.9 | DEEE collectés en France | 1 215 345 t en 2024 | A8-DEV-EUROSTAT-WEEE-2024 | CONFIRMÉ | `"2":1215345` avec `COL:2` | API Eurostat `env_waseleeos`, France, EE6, tonne, 2024 | Tous équipements et matériaux confondus. |
| 31 | 8.3.9 | Plastique estimé dans les EEE ménagers du schéma | environ 315 000 t ; 17 % de la masse | A8-DEV-ECOSYSTEM-RECYCHIM-2020 | CONFIRMÉ | « 315 000 tonnes » ; « 17 % » | Étude ecosystem 2020 | Estimation du schéma ecosystem, pas statistique France entière. |
| 32 | 8.3.9 | Fraction plastique bromée extraite | 39 301,93 t en 2025 | A8-DEV-ECOSYSTEM-RA-2025 | CONFIRMÉ | « Matières plastiques contenant des retardateurs de flamme bromés 39301,93 » | Rapport ecosystem 2025, p. 39 | Périmètre ecosystem uniquement. C'est une fraction orientée en dépollution, pas une teneur mesurée de RFB. |
| 33 | 8.3.9 | Seuil de tri au brome total | 2 000 ppm | A8-DEV-INERIS-BROME-2020 | CONFIRMÉ | « au-delà de 2000 ppm (soit 0,2 %) de brome total, un plastique est réputé en contenir » | Rapport Ineris p. 8-10 | Seuil de tri au brome total, distinct du seuil POP exprimé en somme de PBDE. |
| 34 | 8.3.9 | Seuil POP pour la somme des PBDE | 500, puis 350 mg/kg au 30 décembre 2025, puis 200 mg/kg au 30 décembre 2027 | A8-DEV-POP-PBDE-2025 | CONFIRMÉ | « 500 mg/kg [...] 350 mg/kg as of 30 December 2025 and 200 mg/kg as of 30 December 2027 » | Règlement délégué (UE) 2025/1482 et règlement consolidé 2019/1021 | En vigueur à la date du contrôle : 350 mg/kg. |
| 35 | 8.3.10 | VHU en France et taux de traitement | 1 189 994 t ; 89 % réutilisation-recyclage ; 96,7 % réutilisation-valorisation en 2023 | A8-DEV-EUROSTAT-ELV-2023 | CONFIRMÉ | `GEN T 1189994 ; REU_RCY PC 89 ; REU_RCV PC 96.7` | API Eurostat `env_waselvt`, France, 2023 | Valeurs directement relues dans l'API. |
| 36 | 8.3.10 | Grandes pièces plastiques démontées | 5 203 t recyclées ; 9 834 t réutilisées | A8-DEV-EUROSTAT-ELV-2023 | CONFIRMÉ | `W160119 RCY 5203 ; W160119 REU 9834` | API Eurostat `env_waselv`, France, 2023 | Ces tonnes sont distinctes des résidus de broyage W1910A et W1910B. |
| 37 | 8.3.10 | Composition polymères des VHU | PP 37 % ; PU 15 % ; PA 12 % ; PVC environ 3 % | A8-DEV-JRC-PLASTICS-VEHICLES-2023 | CONFIRMÉ | « PP (37%); PUR (15%); PA (12%) » ; « PVC [...] around 3% » | JRC, tableau 4 p. 22-25 | Composition moyenne des plastiques de véhicules actuels, pas analyse du flux français. |
| 38 | 8.3.10 | Objectifs français PP et PE | 65 % en 2026 ; 70 % en 2028 | A8-DEV-ARRETE-CDC-VHU-2023 | CONFIRMÉ | « Plastiques (Polypropylène (PP) et Polyéthylène (PE) 65% 70% » | Arrêté du 20 novembre 2023, annexe I, §3.4.1 | Il s'agit de valorisation matière, dont recyclage. |
| 39 | 8.3.10 | Contenu recyclé des véhicules neufs | 15 % après 72 mois ; 25 % après 120 mois ; au moins 20 % de l'objectif venant de VHU ; recyclage chimique admis | A8-DEV-ELV-COUNCIL-6180-2026 ; A8-DEV-ELV-REG-2026-1738 | CONFIRMÉ | « minimum of 15 % » ; « minimum of 25 % » ; « At least 20 % of the target » ; « including chemical recycling » | Règlement (UE) 2026/1738, art. 6, §1-2 et considérant 30 | Valeurs du texte final confirmées, pas seulement du compromis. |
| 40 | 8.3.11 | Plastiques du bâtiment recyclés | 20 282 t ; 7,0 % contre objectif 17 % ; plastique 8 % des mises en marché de catégorie 2 | A8-BTX-ADEMEPMCB-2024 | CONFIRMÉ | « Plastique 20 282 7,0 % » ; « 7 % au lieu de 17 % » ; « le plastique (8 %) » | Bilan ADEME PMCB 2024, p. 8 et p. 24 | Aucun détail par polymère, comme le précise l'annexe. |
| 41 | 8.3.11 | Teneur en chlore du PVC | 56,7 % | A8-BTX-INRSPVC-2026 | CONFIRMÉ | « Sa teneur en chlore est de 56,7 %. » | Fiche INRS PVC, p. 1 | Fraction massique du polymère PVC. |
| 42 | 8.3.11 | PVC recyclé en Europe | 765 972 t en 2025 | A8-BTX-VINYLPLUS-2026 | CONFIRMÉ | « A total of 765,972 tonnes of PVC waste were recycled » | VinylPlus Progress Report 2026, p. 20-22 | Chiffre déclaré dans le cadre VinylPlus, pas statistique publique exhaustive. |
| 43 | 8.3.12 | Textiles mis en marché, collectés et triés | 917 604 t ; 272 479 t ; 216 264 t en 2025 | A8-BTX-REFASHIONKPI-2025 | CONFIRMÉ | « Mises en marché (Tonnes) 917 604 | Collecte (Tonnes) 272 479 | Tonnages triés (Tonnes) 216 264 » | PDF Refashion, page unique | Même année et même périmètre TLC. |
| 44 | 8.3.12 et fiche 8.C.i | Devenir des textiles triés et CALC-A8-TEXTILES-CSR-T | 54,47 % réutilisation ; 25,31 % matières à recycler ; 11,03 % essuyage ; 8,4 % CSR ; environ 18 000 t CSR | A8-BTX-REFASHIONKPI-2025 | CONFIRMÉ | « Réutilisation (%) 54,47 | Matières à recycler (%) 25,31 | Chiffons d'essuyage (%) 11,03 | Combustibles Solides de Récupération (%) 8,4 » | PDF Refashion, page unique | 216 264 x 8,4 / 100 = 18 166,176 t, donc environ 18 000 t. « Matières à recycler » est une orientation, pas un recyclage final mesuré. |
| 45 | 8.3.12 | Composition des textiles non réutilisables | polyester 19 % ; acrylique 12 % | A8-BTX-REFASHIONCARAC-2023 | CONFIRMÉ | « Le coton (43%) [...] polyester (19%), l'acrylique (12%) » | Synthèse Refashion p. 8 et p. 13-15 | Échantillon d'environ 14,6 t, données 2021-2022. Ne pas extrapoler sans réserve à tout le gisement national. |
| 46 | 8.3.12 | Recyclage fibre à fibre | moins de 1 % | A8-BTX-EEATEXTILES-2022 | CONFIRMÉ | « Less than 1% of textile waste is recycled into new fibres for clothing » | Rapport EEA 2022, citation secondaire | L'annexe indique correctement que ce chiffre européen est secondaire. |
| 47 | 8.3.13 | Collecte Ecomaison présentée sous « Furniture and household goods » | 1 974 kt | A8-BTX-ECOMAISON-2025 | DIFFÉRENT | « 1 974 kt objets et matériaux collectés » ; ventilation « ameublement 1 549 kt », bâtiment 287 kt, bricolage-jardin 113 kt, jouets 25 kt | Rapport Ecomaison 2025, p. 46-47 | 1 974 kt est le total de tous les flux Ecomaison. Le seul ameublement représente 1 549 kt. Les taux 46 % recyclage, 47 % énergie et les sorties 407 kt CSR, 45 kt mousses, 13 kt plastiques sont eux aussi tous flux. |
| 48 | 8.3.14 | Plastiques dans les OMR | 15,8 % ; 2 329 258 t | ADEME-MODECOM-2024-DATA | CONFIRMÉ | « 07.01 3.4% [...] 496503 ; 07.03 4.2% [...] 619942 ; 07.08 3.0% [...] 443885 » | API ADEME MODECOM, sous-catégories 07.01 à 07.14 | Somme des sous-catégories plastiques : 2 329 258 t ; part publiée 15,8 %. |
| 49 | Contrôle de périmètre | Plastiques triés DEEE/VHU et résidus de broyage | Deux flux distingués | D-037 ; Eurostat | CONFIRMÉ | `W160119 RCY 5203 ; W160119 REU 9834` ; `W1910A` et `W1910B` sont des catégories séparées | API Eurostat `env_waselv` ; section 8.3.9 et 8.3.10 | L'annexe inclut les plastiques triés et exclut explicitement les résidus de broyage. Elle ne mélange pas leurs tonnages. |
| 50 | Contrôle HTML / source | Concordance de la section 8.3 | Même texte et mêmes valeurs | ANNEX-08-Plastic-Waste-Streams.md | CONFIRMÉ | « 97,379 t » ; « 39,301.93 t » ; « 1,974 kt » | Markdown section 8.3 ; HTML correspondant | Aucun écart HTML / source trouvé. Les trois erreurs E-1 à E-3 sont présentes dans les deux versions. |

## Prix et coûts exclus du contrôle chiffré

Les contributions producteurs, prix de reprise, prix garantis, coûts de refus, prix du PSE et autres valeurs commerciales n'ont pas été recalculés. L'annexe les présente comme prix observés à une date donnée, hypothèses de source ou valeurs modifiables. Avant décision, il faut confirmer chaque flux par offre, contrat ou lettre d'intention, avec qualité, humidité, contaminants, conditionnement, transport et volumes garantis.

## Écarts

### E-1 - Le report de la REP des emballages professionnels n'est plus un projet

- Annexe : démarrage reporté « by a draft order ».
- Source en vigueur : arrêté du 3 novembre 2026, publié au JORF le 5 novembre 2026, remplaçant le 1er juillet 2026 par le 1er janvier 2027.
- Gravité : MINEUR.
- Effet : l'échéance est juste, seul le statut juridique est périmé.
- Correction proposée : citer l'arrêté définitif et supprimer « draft ».

### E-2 - Le taux de collecte de 75 % d'A.D.I.VALOR est appliqué à un sous-flux

- Annexe : 84 500 t de plastiques agricoles, taux de collecte 75 %.
- Source : 84 500 t concerne les plastiques d'élevage et de maraîchage ; le 75 % est qualifié de « taux de collecte global » pour tous les flux A.D.I.VALOR.
- Gravité : MINEUR.
- Effet : aucun effet sur la disponibilité à l'échelle d'une URC-2000, mais le dénominateur du taux n'est pas démontré pour ce seul sous-flux.
- Correction proposée : écrire « 84 500 t collectées ; taux global A.D.I.VALOR proche de 75 % ».

### E-3 - Le total Ecomaison est présenté sous un intitulé ameublement

- Annexe : « Furniture and household goods: 1,974 kt collected ».
- Source : 1 974 kt tous flux Ecomaison, dont 1 549 kt d'ameublement, 287 kt de bâtiment, 113 kt de bricolage-jardin et 25 kt de jouets.
- Gravité : MINEUR.
- Effet : le total ameublement est surévalué de 425 kt si la phrase est lue littéralement. Aucun tonnage de plastique disponible pour Urban Rig n'en découle.
- Correction proposée : remplacer l'intitulé par « All Ecomaison schemes » ou donner 1 549 kt pour l'ameublement seul.

## Point d'actualité sans verdict défavorable

Le communiqué Citeo de 2022 confirme bien 100 000 t d'emballages ménagers en PS et 60 000 t de pots. Une publication Citeo plus récente, de septembre 2025, donne 85 000 t pour l'ensemble des emballages PS, dont toujours 60 000 t de PS compact. La valeur citée n'est donc pas absente de sa source, mais elle doit être datée ou actualisée. L'écart de 15 000 t ne menace pas l'approvisionnement du projet et ne modifie pas le calcul de 8,33 % fondé sur les 60 000 t de pots.

## Les erreurs les plus graves

Seulement trois écarts ont été trouvés, tous mineurs. Il n'existe pas cinq erreurs graves à classer.

1. E-3 : périmètre Ecomaison ambigu, 1 974 kt tous flux contre 1 549 kt d'ameublement.
2. E-2 : taux global A.D.I.VALOR de 75 % rattaché à tort au seul sous-flux de 84 500 t.
3. E-1 : texte encore au stade « projet » alors que l'arrêté définitif est publié.

## Autres interprétations utiles

1. **Refus de tri et plastiques triés ne sont pas le même gisement.** Les 750 000 à 800 000 t de refus sont un déchet mélangé. Les 12 % de plastiques sont une composition moyenne, pas 90 000 t de plastique propre immédiatement accessible.

2. **Les 97 379 t de films et 66 005 t du flux développement sont des tonnes reprises.** Elles ne démontrent ni recyclage final, ni disponibilité contractuelle, ni qualité compatible avec Urban Rig.

3. **Le 18 % européen des films est un taux d'entrée chez les recycleurs.** Ce n'est pas un rendement de recyclage ni un taux français.

4. **Le PS compact conserve un gisement de pots stable dans les sources récentes.** Citeo révise le total PS de 100 000 à 85 000 t, mais maintient 60 000 t de PS compact. Le calcul d'environ 8 % reste donc robuste à cette révision.

5. **Le 39 301,93 t ecosystem n'est pas une masse de brome.** C'est la masse de plastiques contenant des retardateurs bromés orientée en dépollution. Le seuil de tri de 2 000 ppm de brome total et le seuil réglementaire de 350 mg/kg pour la somme des PBDE sont deux mesures différentes.

6. **Les pièces plastiques VHU sont distinctes des résidus de broyage.** Eurostat sépare W160119 des fractions W1910A et W1910B. L'annexe respecte cette séparation et n'utilise pas les résidus de broyage exclus par D-037.

7. **Les 20 282 t de plastiques du bâtiment ne donnent aucun tonnage PVC.** La source ne ventile pas par polymère. Les 765 972 t VinylPlus sont européennes et déclarées par l'industrie, sans part française exploitable ici.

8. **Les pourcentages Refashion sont des orientations après tri.** « Matières à recycler » ne prouve pas un recyclage final. Le calcul CSR, lui, est arithmétiquement correct sur cette base.

9. **La composition textile n'est pas nationale au sens statistique.** Les 19 % polyester et 12 % acrylique viennent d'environ 14,6 t de flux non réutilisables analysés. C'est un signal technique, pas une extrapolation robuste à toutes les tonnes françaises.

10. **Les volumes statistiques ne prouvent pas la disponibilité commerciale.** Plusieurs flux dépassent 51 100 t/an, mais les matières propres et triées ont déjà des débouchés. Les fractions mélangées, bromées ou sans exutoire exigent analyses et contrats.

## Conclusion en langage simple

**PASSE.** Les tonnages et devenirs essentiels de la section 8.3 sont correctement repris. Les quatre calculs sont justes : 97 379 t de films, 12 % de plastiques dans les refus moyens, 8,3333 % des pots PS arrivant en centre de tri et 18 166 t de textiles orientés en CSR.

**Aucun point bloquant et aucun écart important.** Les trois écarts sont des problèmes de périmètre ou d'actualisation juridique. Ils ne changent pas la conclusion qu'une unité de 51 100 t/an ne manque pas de gisement théorique.

**Possible sous conditions.** La disponibilité réelle reste à démontrer par contrats et analyses. Les flux triés ont une concurrence de recyclage ; les refus, plastiques bromés, textiles et mélanges nécessitent une caractérisation technique avant décision.

## Ce qui n'a pas été vérifié, et pourquoi

- Tous les prix, soutiens, contributions et coûts : exclus du contrôle chiffré par les règles légères ; à confirmer par offres et contrats.
- Disponibilité contractuelle des flux : aucune statistique ne la prouve ; lettres d'intention et engagements de tonnage requis.
- Composition chimique des refus, textiles, DEEE et plastiques du bâtiment pour l'Urban Rig : analyses représentatives requises, notamment chlore, brome, humidité, cendres et métaux.
- Tonnage réellement recyclé après orientation chez Refashion et A.D.I.VALOR : les sources de filière ne fournissent pas toujours la preuve du traitement final par lot.
- Tonnage national des chutes de production propres : non trouvé, comme l'indique l'annexe.

## Décompte

| Verdict | Nombre |
|---|---:|
| CONFIRMÉ | 47 |
| DIFFÉRENT | 3 |
| ABSENT | 0 |
| INACCESSIBLE | 0 |
| NON SOURCÉ | 0 |
| CALCUL FAUX | 0 |
| **Total** | **50** |

## Compte rendu Trouvé / Partiel / Non trouvé

| Statut | Élément | Résultat |
|---|---|---|
| Trouvé | Quatre calculs CALC-A8 de la section | Tous recalculés et corrects. |
| Trouvé | Données Citeo, OCAPEM, Eurostat, ADEME, Refashion, ecosystem et Ecomaison | Valeurs principales ouvertes et relues. |
| Trouvé | Seuils POP, objectifs VHU et REP professionnels | Textes primaires en vigueur relus. |
| Trouvé | Distinction plastiques triés / résidus de broyage | Catégories Eurostat distinctes et exclusion explicite D-037. |
| Partiel | Disponibilité commerciale et qualité des flux | Statistiques disponibles, mais contrats et analyses absents. |
| Non trouvé | Tonnage national des chutes de production propres | Aucun chiffre national sourcé dans les sources consultées. |
