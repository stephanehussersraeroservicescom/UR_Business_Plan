# Contre-vérification indépendante de l'annexe 8, lot 1

Date : 2026-11-25  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-08-html/index.html`  
Périmètre : sections 8.1 et 8.2, avec les trois calculs demandés  
Accès internet : OUI  
Lecture des PDF en ligne : OUI  

## Méthode et limites

Les documents d'origine ont été ouverts. Les statistiques publiques, les textes réglementaires, les taux et devenirs, les exportations, les données CSR et la capacité francilienne ont été relus. Les coûts d'élimination, prix de marché et indices de prix n'ont pas été recalculés, conformément aux règles de vérification légère. J'ai seulement vérifié qu'ils sont présentés comme des valeurs hétérogènes, des ordres de grandeur ou des valeurs modélisées.

Le contrôle automatique a été lancé sur le HTML. Il a recensé 70 affirmations, mais les a toutes déclarées sans source parce qu'il ne reconnaît pas les liens vers les fiches HTML. Ce résultat automatique n'est donc pas utilisé comme verdict. La contre-vérification ci-dessous repose sur l'ouverture manuelle des fiches et des documents d'origine.

## Tableau des verdicts

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---:|---|---|---|---|---|---|---|---|
| 1 | 8.1.1 | Déchets plastiques produits en France, dont ménages | 2 482 kt ; 380 kt | SDES-2022 | CONFIRMÉ | « Déchets de matières plastiques 2 482 380 15,3 » | PDF p. 2, tableau 2 | Même année, même pays et même catégorie statistique. |
| 2 | 8.1.1 | Le total de 2,482 Mt exclut le plastique collecté en déchets mélangés | Collecte en tant que plastique seulement | A8-CAD-EUROSTAT-META-W074 | CONFIRMÉ | « a lot of plastic waste and plastic packaging waste is collected as mixed waste » | Métadonnées Eurostat, section 15.3 | La phrase de l'annexe évite correctement de présenter 2,482 Mt comme le gisement plastique total. |
| 3 | 8.1.1 | Estimation PlasticsEurope par application | Total 4 160 kt ; emballages 2 410 ; BTP 326 ; DEEE 285 ; ménager-loisirs-sport 210 ; automobile 185 ; agriculture 175 ; autres 569 kt | A8-CAD-PLASTICSEUROPE-NATINFO-FR-2024 | CONFIRMÉ | « 4,160 kt in 2024 » ; « AGRICULTURE 175 kt ; AUTOMOTIVE 185 kt ; ELECTRICAL & ELECTRONICS 285 kt ; BUILDING & CONSTRUCTION 326 kt ; HOUSEWARE, LEISURE & SPORTS 210 kt ; OTHERS 569 kt » | PDF p. 10 et 12, panneaux France | La source dit explicitement que les données sont des estimations arrondies. La somme des applications est bien 4 160 kt. |
| 4 | Key Messages et 8.1.2 | Emballages plastiques France en 2023 | 2 428 987 t générées ; 625 275 t recyclées ; 25,7 % | EUROSTAT-WASPAC | CONFIRMÉ | `GEN T 2023: 2428987 ; RCY T 2023: 625275 ; RCY PC 2023: 25.7` | API Eurostat `env_waspac`, France, W150102, 2023 | Valeurs encore identiques après la mise à jour du 10 novembre 2026. |
| 5 | Key Messages et 8.1.2 | Taux UE de recyclage des emballages plastiques | 41,7 % en 2023 | A8-CAD-EUROSTAT-WASPAC-UE-2023 | DIFFÉRENT | `RCY PC 2023: 41.6 (i)` | API Eurostat `env_waspac`, EU27_2020, 2023, mise à jour 2026-11-10 | La base a été révisée de 41,7 % à 41,6 %. Valeur imputée. Écart de 0,1 point, sans effet sur la conclusion. |
| 6 | 8.1.2 | Taux Citeo des emballages ménagers plastiques | 30 % en 2025 | A8-MENA-CITEOMAG-2026 | CONFIRMÉ | « Plastiques : 30% » | Page Citeo, rubrique « Taux de recyclage par matériau » | Le périmètre de la page est celui des emballages ménagers et papiers. La mention « estimation » est explicitement rattachée au taux global de 73 %, pas au seul 30 %. |
| 7 | 8.1.2 | Recyclage des déchets plastiques collectés comme tels | 20 % en 2022 | SDES-2022 | CONFIRMÉ | « Le taux de recyclage des plastiques est de 20 % » | PDF p. 4 | L'annexe précise correctement que la formule n'est pas définie dans la source. |
| 8 | 8.1.2 | Recyclage des plastiques post-consommation | 23,1 % en 2024 | A8-CAD-PLASTICSEUROPE-NATINFO-FR-2024 | CONFIRMÉ | « Recycling 23.1% ; Incineration 49.2% ; Landfill 27.6% » | PDF p. 10, panneau France | Estimation d'une fédération industrielle, correctement signalée comme telle. |
| 9 | 8.1.2 | Point de calcul du recyclage des plastiques | Triés par polymère avant pelletisation, extrusion ou moulage | A8-CAD-UE-DEC-2019-665 | CONFIRMÉ | « Plastiques triés par polymères ne faisant pas l'objet d'un traitement supplémentaire avant d'être soumis à des opérations de pelletisation, d'extrusion ou de moulage. » | JOUE L 112 du 26 avril 2019, annexe II, p. 34 | Même périmètre réglementaire. |
| 10 | 8.1.2 | La production de combustible n'est pas du recyclage matière | Exclue | A8-CAD-UE-PPWR-2025 | CONFIRMÉ | « à l'exception [...] de la valorisation énergétique et de la conversion pour l'utilisation comme combustible » | Règlement (UE) 2025/40, art. 3, point 40 | Le règlement est applicable depuis le 12 août 2026. |
| 11 | 8.1.2 | Objectifs de recyclage des emballages plastiques | 50 % fin 2025 ; 55 % fin 2030 | A8-CAD-UE-PPWR-2025 | CONFIRMÉ | « au plus tard le 31 décembre 2025 [...] 50 % pour le plastique » ; « au plus tard le 31 décembre 2030 [...] 55 % pour le plastique » | Règlement (UE) 2025/40, art. 52, §1 | Valeurs et échéances exactes. |
| 12 | 8.1.2 | Objectif français de plastique recyclé | Tendre vers 100 % au 1er janvier 2025 | A8-CAD-AGEC-LOI-2020 | CONFIRMÉ | « Tendre vers l'objectif de 100 % de plastique recyclé d'ici le 1er janvier 2025 » | Loi n° 2020-105, art. 5 | Il s'agit d'un objectif de politique publique, pas d'une conformité atteinte. Le verbe « aimed » de l'annexe est approprié. |
| 13 | 8.1.2 | Emballages plastiques à usage unique sans filière | 19 % | STRAT3R-2025 | CONFIRMÉ | « malgré l'absence de filière de recyclage pour 19% des emballages en plastique à usage unique » | PDF p. 13 | La source parle de recyclabilité et de filière, pas du taux réellement recyclé. L'annexe conserve cette distinction. |
| 14 | Key Messages et 8.1.3 | Valorisation énergétique des emballages plastiques | 1 213 829 t en 2023 | EUROSTAT-WASPAC | CONFIRMÉ | `RCV_E_PAC T 2023: 1213829 ; RCV_E_PAC PC 2023: 50` | API Eurostat `env_waspac`, France, 2023 | Correspond à 50,0 % du tonnage généré. |
| 15 | 8.1.3 | Devenir des plastiques post-consommation | Incinération 49,2 % ; stockage 27,6 % en 2024 | A8-CAD-PLASTICSEUROPE-NATINFO-FR-2024 | CONFIRMÉ | « Recycling 23.1% ; Incineration 49.2% ; Landfill 27.6% » | PDF p. 10 | Source industrielle, estimations arrondies. |
| 16 | 8.1.3 et fiche 8.C.f | CALC-A8-EXPORT-3915-T | 403 986,271 t, présenté comme environ 404 000 t | A8-CAD-COMEXT-3915-2025 | CONFIRMÉ | `WORLD 4039862.71` en unités de 100 kg | API Comext DS-045409, France, SH 3915, export, 2025 | Recalcul : 4 039 862,71 x 100 / 1 000 = 403 986,271 t. |
| 17 | 8.1.3 | Exportations surtout vers l'UE, d'abord Espagne, Allemagne, Belgique | Intra-UE 386 516,942 t ; ES, DE, BE premiers | A8-CAD-COMEXT-3915-2025 | CONFIRMÉ | `INT_EU27_2020 3865169.42 ; ES 1234039.33 ; DE 576281.15 ; BE 565077.91` | API Comext, dimension partenaire, unité de 100 kg | L'intra-UE représente environ 95,7 % du total. Il s'agit d'exportations douanières brutes SH 3915, pas d'un gisement disponible. |
| 18 | Key Messages et fiche 8.C.a | CALC-A8-EMB-RECY-HORS-FRANCE | 49,1695 % ; texte « environ 49 % » | EUROSTAT-WASPAC | CALCUL FAUX | `RCY_EU_FOR 296981 ; RCY_NEU 10463 ; RCY 625275` | API Eurostat, France, 2023 | Recalcul exact : (296 981 + 10 463) / 625 275 x 100 = 49,169405 %. À quatre décimales : 49,1694 %, pas 49,1695 %. Le texte arrondi à 49 % reste correct. |
| 19 | 8.1.4 | Ressource propre UE sur le plastique non recyclé | 0,80 EUR/kg | RP2-055 | CONFIRMÉ | « Le taux d'appel uniforme est de 0,80 EUR par kilogramme. » | Décision (UE, Euratom) 2020/2053, art. 2, §1 c) | Taux exact. |
| 20 | 8.1.4 | Contribution française et absence de taxe directe | 1,564 Md EUR en 2023 ; budget de l'État | RP2-056 | CONFIRMÉ | « a connu un pic à 1,564 milliards d'euros en 2023 » ; « ne se traduit pas par une taxe directement acquittée par les ménages et les entreprises » | Note du Sénat, PLF 2025, p. 6 | La note qualifie cette ressource de modulation de la ressource RNB. |
| 21 | 8.1.4 | La taxe nationale proposée pour 2026 a été supprimée | Pas de paiement direct du détenteur | RP2-057 | CONFIRMÉ | « La suppression de la taxe sur les emballages plastiques [...] est maintenue. » | Rapport Sénat sur le texte en nouvelle lecture, article 21 ; confirmation ultérieure par rapport AN n° 3278 | La fiche citée ne montre que l'amendement adopté au Sénat. La conclusion finale est correcte, mais la preuve devrait viser le rapport sur le texte final ou la loi promulguée. |
| 22 | 8.2 | TGAP stockage de déchets non dangereux | 69 ; 73 ; 77 ; 81 ; 85 EUR/t de 2026 à 2030 | CIBS-TGAP-2026 | CONFIRMÉ | « Non dangereux 69 73 77 81 85 » | Loi n° 2026-103, art. L. 433-57 du CIBS, PDF JORF p. 58 | Les tarifs à compter de 2027 sont en outre soumis à l'indexation prévue à l'article L. 433-56. |
| 23 | 8.2 | TGAP incinération, performance de 65 % à 100 % | 16 ; 17 ; 18 ; 19 ; 20 EUR/t | CIBS-TGAP-2026 | CONFIRMÉ | « Non dangereux De 65 % à 100 % 16 17 18 19 20 » | Loi n° 2026-103, art. L. 433-86 du CIBS, PDF JORF p. 60 | Valeurs exactes. |
| 24 | 8.2 | TGAP incinération, performance inférieure à 65 % | 29 ; 33 ; 37 ; 41 ; 45 EUR/t | CIBS-TGAP-2026 | CONFIRMÉ | « Inférieure à 65 % 29 33 37 41 45 » | Loi n° 2026-103, art. L. 433-86 du CIBS, PDF JORF p. 60 | Valeurs exactes. |
| 25 | 8.2 | TGAP résidus de tri performant | 8 ; 8,5 ; 9 ; 9,5 ; 10 EUR/t | CIBS-TGAP-2026 | CONFIRMÉ | « 2026 2027 2028 2029 2030 ; 8 8,5 9 9,5 10 » | Loi n° 2026-103, art. L. 433-89 et L. 433-90 du CIBS, PDF JORF p. 61 | Le taux réduit exige à la fois une installation performante à au moins 70 % et un résidu d'un tri répondant aux critères réglementaires. |
| 26 | 8.2 | Combustibles alternatifs en cimenterie | 52 % de la chaleur en 2023 ; objectif 80 % en 2030 | A8-CST-FRANCECIMENT-2025 | CONFIRMÉ | « En 2023, 52 % des besoins en énergie thermique » ; « combustibles alternatifs de 80 % en 2030 » | Communiqué France Ciment, p. 2 | Déclaration d'une fédération industrielle. Elle couvre tous les combustibles alternatifs, pas spécifiquement les CSR plastiques. |
| 27 | 8.2 | Parc d'incinération francilien | 18 unités ; 4 270 900 t/an autorisées en 2023 ; 3 810 761 t en 2022 ; 93 % de la capacité technique | A8-CST-ORDIF-UIDND-2023 | CONFIRMÉ | « 18 installations » ; « 3 810 761 tonnes en 2022 » ; « 4 270 900 t/an en 2023 » ; « 93% de la capacité technique des fours » | PDF ORDIF p. 2 et p. 7 | La source ajoute 90 % de la capacité autorisée. Les années des flux et de la capacité sont correctement distinguées dans l'annexe. |
| 28 | Calcul demandé | CALC-A8-CAPACITE-AN | 51 100 t/an | D-035 | CONFIRMÉ | « masse = volume x 0,7 t/m3 = 140 t/jour (HYPOTHESE de Stephane) » | `_decisions.yaml`, D-035 ; `calculs.yaml` | 140 x 365 = 51 100. Borne haute sans arrêt, explicitement fondée sur une hypothèse du sponsor. |
| 29 | Contrôle HTML / source | Concordance des sections 8.1 et 8.2 | Même texte et mêmes valeurs | ANNEX-08-Plastic-Waste-Streams.md | CONFIRMÉ | « 2,482 kt » ; « 41.7 % » ; « 4,270,900 t per year » | Markdown, sections 8.1 et 8.2 ; HTML correspondant | Aucun écart HTML / source trouvé dans le lot 1. Les deux portent donc les mêmes deux erreurs mineures E-1 et E-2. |

## Coûts exclus du contrôle chiffré

Les prix d'incinération, de stockage, de refus de tri, les indices d'évolution, le montant modélisé de 40 à 50 EUR/t pour les CSR et la prévision ETS de 30 à 40 % n'ont pas été recalculés. L'annexe les présente avec leurs bases hétérogènes, avertit qu'ils ne forment pas une série temporelle comparable et qualifie le chiffre CSR de « modelled ». Cette présentation satisfait la règle légère. À confirmer ultérieurement par devis, contrat, lettre d'intention ou offre ferme avant intégration commerciale.

## Écarts

### E-1 - Taux UE révisé

- Annexe : 41,7 % en 2023.
- Source actuelle : 41,6 %, valeur imputée, API mise à jour le 10 novembre 2026.
- Gravité : MINEUR.
- Correction proposée : remplacer 41,7 % par 41,6 % et mettre à jour la date de lecture de la fiche.

### E-2 - Arrondi erroné de CALC-A8-EMB-RECY-HORS-FRANCE

- Annexe / calculs : 49,1695 %.
- Recalcul : 49,169405 %, soit 49,1694 % à quatre décimales.
- Gravité : MINEUR.
- Correction proposée : corriger le résultat détaillé. Conserver « about 49 % » dans le texte.

### E-3 - Mauvaise nature de source dans la fiche TGAP 3.M.c

- Annexe : la fiche qualifie le Journal officiel de « OneWorld documentation » et « CONSTRUCTEUR ».
- Source : `joe_20260220_0043_0001.pdf`, Journal officiel de la République française, loi n° 2026-103.
- Gravité : MINEUR.
- Correction proposée : nature `reglementaire` ou `publique`, label `LU` ou `VÉRIFIÉ`, jamais `constructeur`.

### E-4 - Preuve intermédiaire pour la suppression de la taxe plastique

- Annexe : « removed by Parliament », avec la seule fiche RP2-057 sur un amendement adopté au Sénat.
- Source complémentaire : le rapport du Sénat sur la nouvelle lecture dit que « la suppression [...] est maintenue » ; un rapport de l'Assemblée nationale de 2026 confirme que le dispositif a été supprimé pendant l'examen du PLF 2026.
- Gravité : MINEUR.
- Correction proposée : remplacer ou compléter RP2-057 par une preuve du texte final ou de la loi promulguée.

## Les erreurs les plus graves

Seulement quatre écarts ont été trouvés, tous mineurs. Il n'existe donc pas cinq erreurs graves à classer.

1. E-3 : provenance officielle mal étiquetée comme constructeur.
2. E-4 : preuve législative intermédiaire au lieu du résultat final.
3. E-1 : taux UE révisé de 0,1 point.
4. E-2 : erreur de 0,000095 point dans un résultat détaillé, sans effet sur « environ 49 % ».

## Autres interprétations

1. **2,482 Mt et 4,160 Mt ne se contredisent pas.** Le premier chiffre est une catégorie statistique officielle qui exclut le plastique collecté en mélange. Le second est une estimation industrielle de déchets post-consommation collectés, incluant collecte séparée et collecte en mélange. La lecture la plus solide est celle déjà retenue par l'annexe : 2,482 Mt n'est pas le gisement plastique total.

2. **25,7 % et 23,1 % ne portent pas sur le même périmètre.** Eurostat mesure les emballages plastiques en 2023 selon la méthode UE. PlasticsEurope estime tous les plastiques post-consommation en 2024. Aucun écart de fond.

3. **Les 404 kt exportées ne sont pas un gisement disponible.** C'est un flux douanier brut SH 3915. Il peut contenir des matières triées déjà commercialisées et concurrentielles. Il confirme un mouvement de matière, pas l'accès contractuel de l'Urban Rig à ces tonnes.

4. **49 % recyclé hors de France ne veut pas dire 49 % exporté comme déchet final.** La statistique décrit le lieu du recyclage reconnu par Eurostat. Elle ne décrit ni la qualité, ni le prix, ni la disponibilité des flux.

5. **19 % sans filière de recyclage n'équivaut pas à 19 % immédiatement accessible.** Ce chiffre porte sur des catégories d'emballages à usage unique et leur recyclabilité. Le passage à un gisement contractuel exige collecte, tri, conformité technique et accord commercial.

6. **93 % de capacité technique utilisée ne démontre pas l'indisponibilité des flux.** L'installation Urban Rig représenterait 51 100 / 4 270 900 = 1,20 % de la capacité autorisée régionale. La différence arithmétique entre capacité autorisée 2023 et tonnage incinéré 2022 est 460 139 t, mais cette comparaison mélange deux années et ne constitue pas une capacité libre garantie. À l'échelle du projet, la saturation régionale est une pression concurrentielle, pas un blocage d'approvisionnement démontré.

7. **La ressource propre UE n'est pas une recette pour le détenteur de déchets.** Elle est payée via le budget de l'État. L'annexe le dit correctement et ne doit pas l'utiliser comme gate fee.

8. **Les 52 % des cimenteries ne sont pas une part de CSR plastiques.** La source parle de déchets et de combustibles alternatifs au sens large. Elle montre une concurrence énergétique possible, sans quantifier le flux plastique visé par Urban Rig.

## Conclusion en langage simple

**PASSE.** Les tonnages français, les taux de recyclage, les devenirs, les exportations, les taux TGAP et la capacité francilienne sont correctement repris dans un cas standard. Les trois calculs demandés conduisent bien à environ 404 000 t exportées, environ 49 % du recyclage réalisé hors de France et 51 100 t/an de capacité théorique. Le résultat détaillé du calcul de 49 % est mal arrondi à la quatrième décimale, mais la valeur utilisée dans l'analyse reste juste.

**Aucun point bloquant.** La révision du taux UE de 41,7 % à 41,6 % et les trois problèmes de preuve ou d'étiquette ne changent ni l'ordre de grandeur du gisement, ni la faisabilité, ni un chiffre sensible du modèle.

**Sous conditions commerciales.** Les sources démontrent l'existence de volumes très supérieurs aux 51 100 t/an du projet. Elles ne démontrent pas que ces volumes sont disponibles au bon prix, dans la bonne composition ou sans contrat concurrent. Ce point relève des devis, analyses et contrats, pas d'une erreur du lot 1.

## Ce qui n'a pas été vérifié, et pourquoi

- Prix d'incinération, de stockage et de traitement des refus : exclus par les règles légères ; à confirmer par devis ou contrat.
- Indices 2024-2026 des prix d'incinération et de stockage : exclus du recalcul des coûts ; à confirmer avant modélisation financière.
- Gate fee CSR de 40 à 50 EUR/t : valeur modélisée, correctement présentée comme telle ; à confirmer par offre d'un utilisateur de CSR.
- Hausse ETS de 30 à 40 % : prévision de presse, pas un taux légal ; à actualiser lors de la décision d'investissement.
- Disponibilité contractuelle des déchets exportés ou incinérés : aucune source statistique ne peut la démontrer ; lettres d'intention et contrats requis.
- Disponibilité réelle des fours franciliens : le rapport donne capacité autorisée et utilisation technique, pas les créneaux contractuels ; confirmation opérateur requise.

## Décompte

| Verdict | Nombre |
|---|---:|
| CONFIRMÉ | 27 |
| DIFFÉRENT | 1 |
| ABSENT | 0 |
| INACCESSIBLE | 0 |
| NON SOURCÉ | 0 |
| CALCUL FAUX | 1 |
| **Total** | **29** |

## Compte rendu Trouvé / Partiel / Non trouvé

| Statut | Élément | Résultat |
|---|---|---|
| Trouvé | Statistiques officielles France et Eurostat | Valeurs principales ouvertes et vérifiées. |
| Trouvé | PlasticsEurope 2026, données France 2024 | Tonnages, applications et devenirs ouverts dans le PDF. |
| Trouvé | Exportations SH 3915 | API Comext relue, calcul exact. |
| Trouvé | TGAP 2026-2030 | Articles L. 433-57, L. 433-86 et L. 433-90 lus dans le JORF. |
| Trouvé | CSR et cimenteries | 52 % et objectif 80 % relus ; aucun tonnage propre aux CSR plastiques. |
| Trouvé | Capacité francilienne | 18 unités, capacités et tonnages relus dans l'ORDIF. |
| Partiel | Suppression de la taxe plastique | Conclusion correcte, mais la fiche citée doit être complétée par une preuve du texte final. |
| Non trouvé | Disponibilité commerciale des flux | Non démontrable par les statistiques ; contrats nécessaires. |
