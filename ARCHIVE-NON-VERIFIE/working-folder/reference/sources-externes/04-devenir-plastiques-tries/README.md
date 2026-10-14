# Devenir des plastiques triés : du bac jaune au recyclat, et ce que deviennent les refus

Recherche du 10/10/2026. France en priorité, Union européenne en complément.
Identifiants de sources : voir `../registre-sources.yaml` (section « DEVENIR DES PLASTIQUES TRIES ») et `../index-sources.html`.
**[calcul]** = valeur dérivée par nous de chiffres sourcés ; le détail est dans `bilan_matiere.py` (sortie : `bilan-matiere-resultats.md`).

## Fichiers du dossier

| Fichier | Objet |
|---|---|
| `README.md` | Cette note : chaîne, bilan matière, rapports, devenir des refus, incidences pour Urban Rig |
| `bilan_matiere.py` | Calcul du bilan pour 1 tonne, chaque paramètre renvoie à un identifiant du registre |
| `bilan-matiere-resultats.md` | Sortie du script (à régénérer après toute modification) |
| `verification-annexe-08.md` | Première vérification de l'annexe 8 (remplacée par l'analyse approfondie) |
| **`analyse-approfondie-refus-plastiques.md`** | **Analyse approfondie du 10/10/2026 (après-midi) : données mesurées France, UE et pays voisins, composition des refus, gisements Île-de-France, coûts, revérification de l'annexe 8. Sources RP-xxx du registre** |
| `notes-recherche-2026-10-10/` | Notes brutes des cinq axes de recherche, avec citations et URL |
| **`ANNEX-08-v2-plastique-non-recycle-France.md`** | **Annexe 8 version 2 (anglais) : plastique dans les OMR, plastique impropre au recyclage, bilans entrées-sorties, flux financiers, plan d'acquisition des données. Sources RP2-xxx du registre** |
| `notes-recherche-annexe-08-v2/` | Notes brutes des cinq axes d'enquête de l'annexe 8 v2 |

---

## 1. Réponse courte

1. **L'ordre de grandeur de 30 % est juste, mais pas pour la raison supposée.** En France, 346 kt d'emballages ménagers plastiques ont été recyclées en 2025 pour 1 174 kt mises sur le marché, soit **29,5 %** [calcul] ([CITEO-RA-2025](https://www.citeo.com/wp-content/uploads/2026/06/Rapport-dactivite-2025_Citeo.pdf), p. 13 et 29). Citeo annonce 30 % (p. 5).
2. **Ce taux se mesure sur ce qui est mis sur le marché, pas sur ce qui entre en centre de recyclage.** La plus grosse perte est l'absence de tri par l'habitant : environ la moitié du plastique n'arrive jamais dans le bac jaune [calcul, estimation].
3. **Sur une tonne de plastique qui entre réellement dans la chaîne de tri, 55 à 62 % deviennent du recyclat pour les emballages rigides, et 40 à 42 % pour les films ménagers** [calcul]. Les pertes se répartissent entre le centre de tri (15 à 20 %) et le régénérateur (27 à 31 % de ce qu'il reçoit pour les rigides, environ 50 % pour les films ménagers).
4. **Les refus et les pertes ne sont pas vendus : leur détenteur paie pour s'en débarrasser.** Ils partent en incinération (UVE), en stockage (ISDND) ou en CSR (cimenteries, chaufferies). Seuls les flux de balles de bonne qualité ont un prix positif ; les balles de plastiques en mélange ont un prix plancher de 0 €/t.
5. **L'export est en train de se fermer** : interdiction d'exporter des déchets plastiques hors OCDE à partir du **21 novembre 2026** ([EC-WSR-PLASTIC](https://environment.ec.europa.eu/topics/waste-and-recycling/waste-shipments/plastic-waste-shipments_en)).

---

## 2. La chaîne, étape par étape

```
Mise sur le marché ─► Geste de tri ─► Collecte sélective (bac jaune) ─► Centre de tri ─► Balles par flux ─► Régénérateur ─► Paillettes / granulés ─► Nouveau produit
                         │                                                │                                    │
                         └─► OMR (poubelle grise) ─► UVE / ISDND           └─► REFUS DE TRI                      └─► PERTES DE RÉGÉNÉRATION
                                                                              (UVE, CSR, ISDND)                    (étiquettes, bouchons, fines,
                                                                                                                   humidité, autres polymères)
```

### 2.1 Geste de tri et collecte

- Taux de collecte des bouteilles plastiques de boisson : **58,2 %** (« chiffres ADEME 2024 », cité par [CITEO-CONSIGNE-2026](https://www.citeo.com/wp-content/uploads/2026/05/La-Consigne-une-solution-indispensable-au-reemploi-et-au-recyclage.pdf), `secondaire`).
- Les plastiques représentent **15,8 %** des ordures ménagères résiduelles en 2024, soit 2,33 Mt ([ADEME-MODECOM-2024-DATA](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv)). Ce chiffre inclut des plastiques qui ne sont pas des emballages.

### 2.2 Centre de tri

**Taux de refus de la collecte sélective (tous matériaux)** ([CITEO-CAHIER-CS-2024](https://bo.citeo.com/sites/default/files/2024-11/CITEO_Cahier_Collecte%20s%C3%A9lective_nov%202024.pdf), p. 19, `verifie-recontrole`)

| 2018 | 2019 | 2020 | 2021 | 2022 |
|---|---|---|---|---|
| 18,9 % | 19,9 % | 21,5 % | 22,3 % | **23,0 %** |

- « 800 000 tonnes de refus issus des centres de tri de collecte sélective en 2022 » (même source, p. 19).
- Dispersion 2020 : quartiles nationaux 14,4 % / 18,2 % / 23,4 % ; porte-à-porte 24,4 %, apport volontaire 18,4 % ([CITEO-2023](https://bo.citeo.com/sites/default/files/2023-03/2023_Citeo_Brochure%20co%C3%BBts%20et%20performances.pdf), p. 8-13 ; lu par un sous-agent).
- La hausse suit l'extension des consignes de tri : « On observe une tendance à la hausse du taux de refus pour les territoires en ECT » ([CITEO-ECT-2020](https://bo.citeo.com/sites/default/files/2022-06/CITEO_RAPPORT%20ECT%202020.pdf), p. 4-5).
- Exemples locaux : Saumur Val de Loire 24,61 % en 2023 ([SAUMUR-2024](https://www.saumurvaldeloire.fr/images/actualites/2024/DECHETS/0-Dossier_Presse_Refus-tri-CASVL_2024.pdf)) ; Seine-Eure 1 119 t de refus pour 5 491 t collectées, soit environ 20 % [calcul] ([SEINE-EURE-2024](https://www.agglo-seine-eure.fr/wp-content/uploads/2025/10/AggloSeineEure_RA-dechets-2024.pdf)).
- Aucun taux national 2023 à 2025 n'a été trouvé.

**Part du plastique perdue au centre de tri**
- « environ 15 à 20 % du gisement plastiques entrant dans les centres de tri » finit aux refus ([CITEO-ECT-2020](https://bo.citeo.com/sites/default/files/2022-06/CITEO_RAPPORT%20ECT%202020.pdf), p. 25). Il s'agit d'une estimation Citeo, pas d'une mesure.
- Cause principale : les petits emballages. Taux de captage moyen des matériaux valorisables : 81,7 % au-dessus de 100 mm, 67,4 % entre 50 et 100 mm, 24 % entre 20 et 50 mm, 0 % sous 20 mm ([OCAPEM-2025](https://www.citeo.com/wp-content/uploads/2026/02/Synthese-du-Rapport-OCAPEM-Amelioration-du-tri-des-petits-emballages.pdf), tableau 4 p. 6).

**Que contiennent les refus ?** ([OCAPEM-2025](https://www.citeo.com/wp-content/uploads/2026/02/Synthese-du-Rapport-OCAPEM-Amelioration-du-tri-des-petits-emballages.pdf), tableau 3 p. 5)

| Fibreux | Plastiques rigides | Plastiques souples | Acier | Alu | Autres (fines, imbrûlés, verre, non-emballages) |
|---|---|---|---|---|---|
| 15,7 % | 7,5 % | 4,5 % | 0,4 % | 1,2 % | **70,9 %** |

Réserve importante : caractérisation des fines sur 200 kg prélevés sur deux journées dans un seul centre de tri. L'étude reconnaît elle-même le manque de représentativité.

**Ce qui sort en balles**
- Aucun bilan national de sortie par flux n'a été trouvé. Exemple local (Seine-Eure 2024, [SEINE-EURE-2024](https://www.agglo-seine-eure.fr/wp-content/uploads/2025/10/AggloSeineEure_RA-dechets-2024.pdf), p. 10-11) : PET clair 420,5 t ; flux développement et PET coloré 231,6 t ; PEHD/PP 301,6 t ; films PE 266,4 t.

### 2.3 Qualité des balles : où apparaît la « contamination »

Les balles doivent respecter des **standards** fixés dans le cadre de la filière REP emballages ([CITEO-STANDARDS-2019](https://bo.citeo.com/sites/default/files/2019-12/STANDARDS-PAR-MATERIAUX-V2019.pdf)) :
- PET clair, PET foncé : « teneur en bouteilles et flacons ménagers [...] de 98 % au minimum » ;
- films : 95 % minimum de films et sacs PE ;
- PEHD/PP/PS : 98 %, avec tolérance à 95 % ;
- flux développement : 90 % minimum ;
- aucune limite d'humidité n'est fixée.

**Mesure réelle, France 2023** ([CITEO-OBSQUAL-2023](https://bo.citeo.com/sites/default/files/2024-04/Citeo%20-%20Observatoire%20de%20la%20qualit%C3%A9%202023.pdf), p. 29 à 34, `verifie-recontrole`)

| Flux | Teneur moyenne mesurée | Standard | Impuretés par tonne de balles [calcul] |
|---|---|---|---|
| PET clair | 96 % | 98 % | 40 kg |
| PET foncé | 96,9 % | 98 % | 31 kg |
| PE/PP/PS | **88,1 %** | 98 % | 119 kg |
| Films PE/PP | 90,1 % | 90 % | 99 kg |
| Films PE | **82 %** | 95 % | 180 kg |
| Flux développement | 92 % | 90 % | 80 kg |

Méthode (p. 43) : balle tirée au hasard, échantillon trié par matériau, pesée, comparaison au standard. Campagne 2023 : 123 centres de tri, 19 recycleurs, 1 559 caractérisations, réalisées par les bureaux d'études V2R, Austral, Atlance et Terra (p. 8-9).

### 2.4 Régénération (recycleur)

| Flux | Rendement (sortie / entrée) | Année, périmètre | Source |
|---|---|---|---|
| PET | **73 %** (1,87 Mt entrées, 1,35 Mt de rPET) | 2018, UE28 | [PRE-PET-2020](https://www.plasticsrecyclers.eu/wp-content/uploads/2022/10/pet-market-in-europe-state-of-play-2020.pdf), p. 19 |
| PET (tendance) | 73 % en 2011, 68 % en 2017 | UE | [PRE-PET-2017](https://plastics-recyclers-europe.prezly.com/pet-recyclers-suffer-lower-input-qualities) (`secondaire`) |
| PEHD rigide | **71 %** | 2023, UE27+3 | [PRE-HDPEPP-2025](https://plasticker.de/docs/news/HDPE_REPORT_2023_screen_spreads_VF%20(1).pdf), section 5b |
| PP rigide | **69 %** | 2023, UE27+3 | idem |
| Films ménagers | **environ 50 %** | 2018, UE28+2 | [PRE-FILMS-2018](https://www.plasticsrecyclers.eu/wp-content/uploads/2022/10/flexible-films-market.pdf), p. 17 |
| Films commerciaux | 80 % | 2018 | idem |
| Films, toutes origines | > 75 % | 2020, UE27+3 | [PRE-FILMS-2023](https://www.plasticsrecyclers.eu/wp-content/uploads/2023/06/2023-Flexible-Films-Market-in-Europe_State-of-Play_June-2023.pdf), p. 24-25 |

**Causes des pertes chez le régénérateur** ([PRE-PET-2020](https://www.plasticsrecyclers.eu/wp-content/uploads/2022/10/pet-market-in-europe-state-of-play-2020.pdf), p. 13, 23-25 ; [PRE-FILMS-2018](https://www.plasticsrecyclers.eu/wp-content/uploads/2022/10/flexible-films-market.pdf), p. 13 et 17) :
- matériaux non cibles dans les balles (papier, textiles, verre, autres polymères dont le PVC) ;
- étiquettes et colles (« Higher adhesives and labels content ») ;
- humidité contenue dans les balles ;
- pour les films ménagers : « high levels of non-PE films (PP films, multilayers) » et « food contamination ».

Aucune source française (Valorplast, COTREP, Paprec, Suez) donnant un rendement de régénération n'a été trouvée. Les chiffres européens de PRE sont la meilleure référence disponible.

**Usage du recyclat PET** : bouteilles alimentaires 18 % et non alimentaires 10 % du rPET vendu en 2018 ([PRE-PET-2020](https://www.plasticsrecyclers.eu/wp-content/uploads/2022/10/pet-market-in-europe-state-of-play-2020.pdf), p. 19) ; 48 % en bouteilles en 2022 ([PRE-PET-2024](https://www.plasticsrecyclers.eu/news/pet-on-the-road-to-circularity-but-disparities-are-creating-potholes/), `secondaire`). Le PEHD recyclé ne retourne pas en bouteille de lait alimentaire de façon significative dans les sources lues ; aucun chiffre trouvé.

---

## 3. Bilan matière pour 1 tonne [calcul]

Détail et paramètres : `bilan_matiere.py`.

### Scénario A : 1 t d'emballages plastiques ménagers mis sur le marché (France 2025)

| Destination | kg | Base |
|---|---|---|
| Recyclé | **295** | 346 / 1 174 kt ([CITEO-RA-2025](https://www.citeo.com/wp-content/uploads/2026/06/Rapport-dactivite-2025_Citeo.pdf)) |
| Collecté en bac jaune mais perdu (refus et pertes de régénération) | environ 180 à 240 | estimation [calcul] |
| Jamais trié (OMR, puis UVE ou stockage) | environ 470 à 525 | estimation [calcul] |

La répartition des 705 kg non recyclés est une **estimation** : on remonte du tonnage recyclé avec les rendements des rigides (perte au centre de tri 15 à 20 %, rendement de régénération 69 à 73 %). Elle est cohérente avec le taux de collecte de 58,2 % des bouteilles.

### Scénario B : 1 t de plastique arrivant au centre de tri

| Étape | PET | PEHD | PP | Films ménagers |
|---|---|---|---|---|
| Refus au centre de tri (kg) | 150 à 200 | 150 à 200 | 150 à 200 | 150 à 200 |
| Balles produites (kg) | 800 à 850 | 800 à 850 | 800 à 850 | 800 à 850 |
| Pertes chez le régénérateur (kg) | 216 à 230 | 232 à 246 | 248 à 264 | 400 à 425 |
| **Matière recyclée (kg)** | **584 à 620** | **568 à 604** | **552 à 586** | **400 à 425** |
| Rendement global | 58 à 62 % | 57 à 60 % | 55 à 59 % | 40 à 42 % |

Limite : ce calcul applique des rendements européens de PRE à une perte au centre de tri estimée par Citeo. Les pertes de régénération incluent les impuretés des balles (section 2.3), qui ne doivent pas être comptées deux fois.

### Scénario C : 1 t de collecte sélective (tous matériaux)

- 230 kg de refus (taux 2022), dont environ **28 kg** de plastiques d'emballage identifiés et 163 kg d'« autres » [calcul, sur la composition OCAPEM-2025, méthode fragile].

### Comparaison avec l'Europe

| Indicateur | Valeur | Source |
|---|---|---|
| Taux de recyclage des emballages plastiques, France 2023 | **25,7 %** | [EUROSTAT-SE-PACK](https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/10547.pdf), figure 6 ; [EUROSTAT-WASPAC](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_waspac?geo=FR&waste=W150102) |
| Idem, UE 2023 | 42,1 % | [LETSRECYCLE-2025](https://www.letsrecycle.com/news/belgium-leads-as-eu-plastic-packaging-recycling-tops-42/) (`secondaire`) |
| PET : part du gisement en fin de vie devenue rPET, UE28 2018 | 1,35 / 4,3 Mt, soit **31 %** [calcul] | [PRE-PET-2020](https://www.plasticsrecyclers.eu/wp-content/uploads/2022/10/pet-market-in-europe-state-of-play-2020.pdf), p. 13 et 19 |
| Taux de recyclage réel PEHD / PP, UE 2023 | **32 % / 30 %** | [PRE-HDPEPP-2025](https://plasticker.de/docs/news/HDPE_REPORT_2023_screen_spreads_VF%20(1).pdf) |
| Films : part des mises sur le marché recyclée, UE 2020 | 18 % | [PRE-FILMS-2023](https://www.plasticsrecyclers.eu/wp-content/uploads/2023/06/2023-Flexible-Films-Market-in-Europe_State-of-Play_June-2023.pdf), p. 19 |
| Tous déchets plastiques, recyclage effectif, UE 2020 | 14 % | [SYSTEMIQ-2022](https://www.maastrichtuniversity.nl/file/cce-systemiq-reshaping-plastics-reportpdf), p. 24 et 28 |
| Tous déchets plastiques post-consommation, UE 2024 | 29,6 % | [PE-CE-2026](https://en.newspackaging.es/desaceleracion-en-la-transicion-de-europa-hacia-un-ecosistema-circular-de-los-plasticos/) (`secondaire`) |

L'écart entre 25,7 % (Eurostat) et 30 % (Citeo) vient du périmètre : Eurostat couvre tous les emballages plastiques (ménagers, commerciaux, industriels), Citeo les seuls emballages ménagers, et les années diffèrent.

---

## 4. Où apparaissent la contamination et les pertes, et qui publie

| Donnée | Où elle apparaît | Qui la produit | Obligation |
|---|---|---|---|
| Taux de refus du centre de tri | Cahiers et brochures Citeo ; rapports annuels des collectivités | Collectivités (déclarations à Citeo), Citeo | Le RPQS impose les tonnages par flux et le taux de valorisation, **pas le taux de refus** ([DECRET-2015-1827](https://aida.ineris.fr/node/35508), `secondaire`) |
| Pureté des balles (impuretés) | Observatoire de la qualité Citeo | Bureaux d'études mandatés par Citeo (V2R, Austral, Atlance, Terra) | Contrôle du respect des standards de reprise |
| Composition des refus | Études Citeo / OCAPEM | Bureaux d'études (Inddigo) | Aucune |
| Rendement de régénération | Rapports « State of Play » | Plastics Recyclers Europe, avec Eunomia ou ICIS | Aucune (données sectorielles déclaratives) |
| Taux de recyclage officiel | Eurostat env_waspac | États membres, selon le point de calcul UE | Directive 94/62/CE modifiée par 2018/852 ; règles de calcul de la décision 2019/665 |
| Destination des refus | Enquête ITOM / SINOE | ADEME | Enquête périodique ; dernier chiffre national trouvé : données 2012 |

**Le point de calcul européen.** Depuis 2020, le recyclage se mesure au point où le plastique, trié par polymère, « does not undergo further processing before entering pelletisation, extrusion, or moulding operations », humidité et contamination déduites ([EC-GUIDANCE-PACK-2022](https://apambiente.pt/sites/default/files/_Residuos/PPWDGuidance2022final_abril2022.pdf), par. 3.2.1, `secondaire`). Conséquences :
- baisse du taux UE de 41 % (2019) à 38 % (2020), attribuée notamment à « a harmonised calculation point for recycling » ([EUROSTAT-NEWS-2022](https://ec.europa.eu/eurostat/web/products-eurostat-news/-/ddn-20221020-1)) ;
- la Cour des comptes européenne anticipait un passage « de leur niveau actuel de 42 % [...] à un chiffre d'à peine 30 % » ([ECA-2020](https://www.eca.europa.eu/Lists/News/NEWS2010_06/INRW_Plastic_waste_FR.pdf), `secondaire`) ;
- Citeo : « Ce calcul prend en compte non pas les quantités acceptées par les recycleurs à l'entrée du process [...] mais celles effectivement recyclées » ([CITEO-CC-2023](https://www.citeo.com/wp-content/uploads/2025/01/241223_CITEO_Fiche_Chiffres_cles-2023_Notre_Impact.pdf), note 3).

C'est probablement ce qui explique l'écart entre 379,5 kt recyclées en 2022 ([CITEO-CAHIER-CS-2024](https://bo.citeo.com/sites/default/files/2024-11/CITEO_Cahier_Collecte%20s%C3%A9lective_nov%202024.pdf), p. 14) et 324 kt en 2024 ([CITEO-RA-2025](https://www.citeo.com/wp-content/uploads/2026/06/Rapport-dactivite-2025_Citeo.pdf), p. 29). Aucune source ne l'énonce : **à confirmer** avant de citer l'un ou l'autre en série.

---

## 5. Ce que deviennent les plastiques non recyclés

### 5.1 Débouchés des refus de tri

| Débouché | Chiffre | Source | Statut |
|---|---|---|---|
| Stockage (ISDND) | 75 % des refus | [SINOE-ITOM2012](https://www.sinoe.org/documents/consult-and-count-doc/doc/1200/rubrique/6), p. 7 (données 2012) | `ancien` |
| Valorisation énergétique | 20 % des refus | idem | `ancien` |
| Valorisation énergétique (territoires en ECT) | refus valorisés en énergie pour 85 % (2019) à 86 % de la population couverte | [CITEO-ECT-2020](https://bo.citeo.com/sites/default/files/2022-06/CITEO_RAPPORT%20ECT%202020.pdf), p. 4-5 et 25 | `verifie` |
| CSR (cimenteries, chaufferies) | 510 kt de CSR consommés en 2023, dont 61 kt en chaufferies ; capacité 2,5 Mt utilisée à 20 % | [SENAT-I980-2025](https://www.senat.fr/enseance/2025-2026/138/Amdt_I-980.html) | `secondaire` |
| CSR, 2021 | 370 kt consommées | [FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf), p. 3 | `verifie` |

**Lecture** : la répartition nationale actuelle n'est pas publiée (dernier chiffre : 2012). Les sources récentes indiquent un basculement vers l'incinération et le CSR, poussé par la TGAP.

### 5.2 Flux financiers : qui paie, qui encaisse

**Refus de tri : un coût, jamais une recette.**
- Saumur Val de Loire : transport et traitement des refus (incinération à l'UVE de Lasse) **291,96 € HT/t en 2022, 363,65 € HT/t en 2023** ([SAUMUR-2024](https://www.saumurvaldeloire.fr/images/actualites/2024/DECHETS/0-Dossier_Presse_Refus-tri-CASVL_2024.pdf)).
- Coût médian national des OMR, TGAP comprise, 2023 : incinération 107 €/t, stockage 138 €/t ([ADEME-REFCOUTS-2023](https://librairie.ademe.fr/societe-et-politiques-publiques/8811-10587-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-hexagonale-donnees-2023.html), figure 33 p. 36 ; voir `../02-gate-fees-DMA-et-TGAP-France.md`).
- CSR : le producteur paie la chaufferie, gate fee modélisé de 40 à 50 €/t ([FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf), p. 5) ; marché observé en Normandie : accueil en chaufferie 10 à 30 €/t, coût de production 85 à 115 €/t ([NORMANDIE-CSR-2021](https://neci.normandie.fr/sites/default/files/2024-04/02%20info-dechet%20V1.0.pdf), p. 6).
- Prix d'enfouissement des refus au 01/01/2026 : hausse de 1,8 à 6,0 €/t selon les régions, hors TGAP ; aucun prix absolu publié ([FEDEREC-Q3000-2026](https://www.rydge.fr/hubfs/federec/refus-de-tri-dechets-non-dangereux/indice-Q3000-enfouissement-janvier-2026-synthese.pdf), `secondaire`).

**TGAP applicable** ([CIBS-TGAP-2026](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053508155), loi n° 2026-103) :
- stockage : 69 €/t en 2026, jusqu'à 85 €/t en 2030 ;
- incinération à haute performance énergétique : 16 €/t en 2026, jusqu'à 20 €/t en 2030 ;
- **résidus de tri performants en traitement thermique (art. L. 433-90) : 8 €/t en 2026, jusqu'à 10 €/t en 2030** ;
- aucun taux réduit équivalent en stockage : « aucun dispositif miroir n'existe » ([SENAT-I981-2025](https://www.senat.fr/enseance/2025-2026/138/Amdt_I-981.html), amendement rejeté).
- Les refus de tri performants bénéficient aussi d'un accès prioritaire à prix encadré en ISDND (décret 2021-838, [LANDOT-2021](https://blog.landot-avocats.net/2021/07/01/isdnd-encadrement-des-prix-plafonnes-applicables-aux-refus-de-tri-et-aux-dechets-du-recyclage/), `secondaire`).

**Balles triées : un prix de reprise, positif ou nul.** Prix planchers annuels Valorplast, option Reprise Filière, barème G, jusqu'au 31/12/2029 ([VALORPLAST-G-2024](https://www.grandchambery.fr/fileadmin/mediatheque/Oxyad/DelmDec/indexdelm_20240530/Annexe34598.pdf), article 11) :

| Flux | Plancher €/t |
|---|---|
| Bouteilles PET clair / emballages PET clair | 160 |
| Bouteilles PET foncé | 90 |
| Bouteilles et flacons PEHD et PP | 80 |
| Mix PE | 80 |
| Mix PP | 60 |
| Mix PE/PP | 20 |
| **Films et sacs ; mix PE/PP/PS ; PS ; PET opaque ; pots et barquettes** | **0** |

Le contrat engage Valorplast sur un prix « positif ou nul » départ centre de tri. Prix de marché constatés : PET clair +240 €/t et PEHD/PP +90 €/t en septembre 2023 ([DOMITIENNE-2023](https://www.ladomitienne.com/wp-content/uploads/2024/02/24.010.3_Annexe_DECH_Contrats_Plastiques_lot_3.pdf)). Les prix mensuels réels (mercuriales) ne sont pas publics.

**Résidus des régénérateurs** (étiquettes, bouchons, fines, boues de lavage) : aucune donnée publique sur leur destination ni sur leur coût n'a été trouvée. Point ouvert.

### 5.3 Export

- UE 2025 : **1,4 Mt** de déchets plastiques exportés hors UE, dont 730 kt vers l'OCDE ; la Turquie en reçoit 510 kt, soit 36 % du total ([EC-SWD-2026-274](https://data.consilium.europa.eu/doc/document/ST-12685-2026-INIT/en/pdf), p. 2).
- Interdiction d'export hors OCDE « From 21 November 2026 [...] at least until 21 May 2029 » ; exportations vers l'OCDE suspendables si la gestion n'est pas écologiquement rationnelle ([EC-WSR-PLASTIC](https://environment.ec.europa.eu/topics/waste-and-recycling/waste-shipments/plastic-waste-shipments_en), règlement (UE) 2024/1157).
- France 2025 : 398 kt de déchets plastiques exportés ([STATISTA-FR-EXPORT-2025](https://statista.com/statistics/1607826/plastic-waste-export-volume-france), `secondaire`, à remplacer par Comext). Transferts notifiés 2023 : 28 kt, vers l'Espagne (46 %), le Royaume-Uni (22 %), l'Allemagne (15 %) et la Belgique (8 %) ([SDES-TRANSFERTS-2023](https://www.statistiques.developpement-durable.gouv.fr/les-echanges-transfrontieres-de-dechets-faisant-lobjet-dune-notification-prealable-en-2023)).
- Convention de Bâle : rubriques Y48, A3210 et B3011 en vigueur depuis le 01/01/2021 ([BASEL-PLASTIC-2019](https://www.basel.int/Implementation/Plasticwaste/Amendments/Overview/tabid/8426/Default.aspx)).

### 5.4 Recyclage chimique et pyrolyse

- TotalEnergies Grandpuits : pyrolyse (technologie Plastic Energy), **15 000 t/an**, démarrage 2026, intrants « hard-to-recycle plastic waste from French households » fournis avec Citeo et Paprec ([TOTAL-GRANDPUITS-2026](https://totalenergies.com/system/files/documents/totalenergies_pr-totalenergies-starts-production-France-s-first-advanced-plastics-recycling-plant_2026_en.pdf), `secondaire`).
- Projets ralentis : Eastman (Port-Jérôme) reporté ; Loop, Suez et SK Geo Centric (Saint-Avold) suspendu ([INFODURABLE-2024](https://linfodurable.fr/economie/recyclage-du-plastique-des-projets-freines-par-le-contexte-reglementaire-48122)).
- Règle de comptage UE (directive SUP) : bilan massique « fuel use excluded », seules les fractions non transformées en combustibles comptent comme recyclées ([BKV-SUPD-2026](https://bkv-gmbh.de/news-reader-4/implementing-decision-on-supd-published.html), `secondaire`, numéro de la décision à vérifier).
- Position critique : selon Zero Waste Europe, environ 2 % du plastique entrant en pyrolyse se retrouve dans le produit recyclé ([ZWE-2023](https://zerowasteeurope.eu/press-release/new-report-blasts-the-limitations-of-pyrolysis-technology-dubbed-miracle-by-industry/), position militante).
- Prix des intrants pour pyrolyse (balles de refus, polyoléfines en mélange) : publiés par ICIS et Platts, derrière un accès payant. Non disponibles.

---

## 6. Incidences pour Urban Rig (à arbitrer)

1. **Gisement disponible.** 750 à 800 kt/an de refus de tri de collecte sélective ([CITEO-CAHIER-CS-2024](https://bo.citeo.com/sites/default/files/2024-11/CITEO_Cahier_Collecte%20s%C3%A9lective_nov%202024.pdf), [OCAPEM-2025](https://www.citeo.com/wp-content/uploads/2026/02/Synthese-du-Rapport-OCAPEM-Amelioration-du-tri-des-petits-emballages.pdf)), auxquels s'ajoutent les pertes des régénérateurs et les balles à prix plancher nul. La FNADE compte 2 738 kt de refus de tri tous gisements confondus ([FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf), p. 4).
2. **Gate fee.** Le détenteur paie aujourd'hui pour se débarrasser de ces flux. Le prix de référence à battre est l'UVE, avec une TGAP de 8 €/t seulement pour les résidus de tri performants. C'est un concurrent fort sur le prix.
3. **Part plastique.** Pour les refus de collecte sélective ménagère, la seule composition nationale trouvée donne **12 % d'emballages plastiques identifiés** et 70,9 % d'« autres ». Elle ne soutient pas `composition.part_plastique = 0,30` pour ce gisement. Les refus de régénérateurs ou les balles de mélange PE/PP/PS sont en revanche très majoritairement plastiques (88 % de teneur moyenne pour les balles PE/PP/PS). **Le choix du gisement change fortement la part plastique** ; une caractérisation propre est nécessaire avant de fixer le paramètre.
4. **Marché des exutoires sous tension.** Les capacités CSR sont utilisées à environ 20 %, l'export hors OCDE ferme le 21/11/2026, et la TGAP stockage monte à 85 €/t en 2030. Ces trois éléments soutiennent l'argument d'un nouvel exutoire thermique, sous réserve de la qualification réglementaire du procédé (voir l'interrupteur TGAP du modèle).

---

## 7. Points non vérifiés ou manquants

- Taux national de refus 2023 à 2025 ; répartition nationale actuelle des destinations des refus (dernière donnée : 2012).
- Bilan national de sortie des centres de tri par flux (seuls une projection 2019 et un exemple local existent).
- Rendements de régénération français ; destination et coût des résidus des régénérateurs.
- Texte de la directive 2018/852 (art. 6 bis) et de la décision 2019/665 sur EUR-Lex.
- Réconciliation 379,5 kt (2022) / 324 kt (2024) de plastiques recyclés chez Citeo.
- Prix récents du CSR (2024 à 2026) et prix des intrants de pyrolyse (ICIS, Platts).
- Exportations françaises par destination (Eurostat Comext, douanes).
- Rapport Plastics Europe *Circular Economy for Plastics* lu directement.
