> **Remplacée** par `analyse-approfondie-refus-plastiques.md` (10/10/2026, après-midi), qui repose sur davantage de sources mesurées et corrige ou précise plusieurs points ci-dessous.

# Vérification de l'annexe 8 (« Sector: Plastic Sorting Rejects (France) », brouillon de mars 2026)

Vérification du 10/10/2026, faite contre les sources de `README.md` (même dossier) et de `../registre-sources.yaml`.
L'annexe elle-même n'a pas été modifiée.

Légende : **OK** = confirmé ; **À CORRIGER** = contredit par une source ; **NON SOURCÉ** = aucune source trouvée ; **À NUANCER** = juste sur le fond, mais mal qualifié.

---

## 1. Synthèse

L'annexe repose sur un flux « B1a » : **670 kt/an** de plastique trié par infrarouge, pur à plus de 95 %, sans acheteur, que les centres de tri paieraient 100 à 150 €/t pour faire incinérer. **Les sources ne soutiennent pas ce flux, ni en volume, ni en pureté, ni en économie.**

1. **Volume.** Le calcul part d'un tonnage **produit** (1 085 kt) et le traite comme un tonnage **collecté**. Or environ la moitié du plastique n'atteint jamais le bac jaune. Reconstitué à partir des chiffres Citeo 2025, le plastique collecté mais non recyclé est de **210 à 280 kt/an** [calcul], dont seulement **85 à 125 kt** restent au centre de tri, dans les refus en mélange. Le reste est perdu chez les régénérateurs, en France ou à l'étranger.
2. **Pureté.** La pureté réellement mesurée sur les balles en 2023 est de 88 % pour le PE/PP/PS et de 82 % pour les films PE ; elle n'est pas de 95 % ni plus. Les 95 à 99 % sont des performances de machine annoncées par les fabricants, pas des mesures sur le terrain français.
3. **Économie (point le plus important).** Les flux « sans débouché » cités (PS, films, mélange PE/PP/PS, PET opaque, barquettes) **ont un repreneur** : Valorplast s'engage à les reprendre à un prix « positif ou nul », avec un plancher à 0 €/t, et les flux rigides vont aux centres de surtri. Le centre de tri ne paie donc pas pour s'en débarrasser. Urban Rig ne toucherait **pas de gate fee** sur ces balles. Il devrait au mieux les obtenir à 0 €/t, en concurrence avec Valorplast, les régénérateurs et des pyrolyseurs déjà sous contrat (TotalEnergies Grandpuits s'approvisionne auprès de Citeo et de Paprec).
4. **Conséquence sur le modèle.** Le revenu de 415 €/t du scénario B1a inclut une gate fee de 95 €/t qui n'existe probablement pas pour ce flux. Sans elle, on tombe à environ 320 €/t, sous réserve du rendement en huile et du prix de l'huile, qui restent non sourcés. Les flux qui paient vraiment une gate fee sont les **refus en mélange (B1b)** et les **résidus des régénérateurs et du surtri**. Leur teneur en plastique est très incertaine et doit être mesurée.

---

## 2. Vérification ligne par ligne

### Partie 1 : paysage national

| Annexe | Verdict | Ce que disent les sources |
|---|---|---|
| 3,4 Mt de déchets plastiques (2020) | **À NUANCER** | Même ordre de grandeur : 3,76 Mt en 2020 ([OPECST-2023](https://www.senat.fr/rap/r22-808/r22-8081.pdf), `secondaire`) ; 2,48 Mt de déchets plastiques en 2022 au sens SDES ([SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline)). Les périmètres diffèrent ; citer la source primaire SDES |
| Emballages plastiques : 2,35 Mt (2020) | **OK** | 2,43 Mt générés en 2023 ([EUROSTAT-WASPAC](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_waspac?geo=FR&waste=W150102)) |
| Taux de recyclage de 29 % (AEE, 2022) | **À NUANCER** | Emballages plastiques : 25,7 % en 2023 selon Eurostat ([EUROSTAT-SE-PACK](https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/10547.pdf)) ; emballages ménagers : 29,5 % en 2025 [calcul] ([CITEO-RA-2025](https://www.citeo.com/wp-content/uploads/2026/06/Rapport-dactivite-2025_Citeo.pdf)). Préciser le périmètre |
| Incinération à 116 €/t (Zero Waste France) | **À NUANCER** | Source militante et secondaire. Remplacer par la médiane ADEME 2023 des OMR, TGAP comprise : incinération 107 €/t, stockage 138 €/t ([ADEME-REFCOUTS-2023](https://librairie.ademe.fr/societe-et-politiques-publiques/8811-10587-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-hexagonale-donnees-2023.html)). Pour les refus de tri, un cas réel donne 364 € HT/t, transport compris ([SAUMUR-2024](https://www.saumurvaldeloire.fr/images/actualites/2024/DECHETS/0-Dossier_Presse_Refus-tri-CASVL_2024.pdf)) |
| TGAP « +15 à 25 €/t d'ici 2025 » | **À CORRIGER** | Barème 2026 en vigueur ([CIBS-TGAP-2026](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053508155)) : stockage 69 €/t en 2026, jusqu'à 85 €/t en 2030 ; incinération performante 16 à 20 €/t ; **résidus de tri performants en traitement thermique 8 à 10 €/t**. Ce dernier taux rend l'UVE très compétitive précisément sur les refus de tri |
| Taxe UE de 800 €/t sur les emballages non recyclés | **À CORRIGER** | Ce n'est pas un coût pour le producteur de déchets : c'est une contribution versée par l'État au budget de l'UE (ressource propre). Elle ne pèse pas sur la gate fee. À retirer du tableau des pressions sur les coûts, ou à requalifier |
| Loi AGEC « 100 % de plastique recyclé en 2025 » | **À NUANCER** | Objectif d'orientation (« tendre vers »), non contraignant. Source secondaire (site de conseil) : citer Légifrance |

### Partie 2 : flux ciblés

| Annexe | Verdict | Ce que disent les sources |
|---|---|---|
| Environ 200 centres de tri (§5.1), plus de 350 (§5.3) | **À CORRIGER** | Incohérence interne. COTREP : « 115 modern centres » ([COTREP-TRI-FR](https://www.cotrep.fr/en/plastics-sorting-and-recycling-in-france/)). Le chiffre de 350 couvre probablement tous les centres de tri, y compris ceux de déchets d'activités économiques (DAE) |
| 1 085 kt d'emballages ménagers plastiques (COTREP) | **NON SOURCÉ** | La page COTREP citée ne donne pas ce chiffre. Valeur sourcée : **1 174 kt mises sur le marché en 2025** ([CITEO-RA-2025](https://www.citeo.com/wp-content/uploads/2026/06/Rapport-dactivite-2025_Citeo.pdf), p. 13) |
| 315 kt recyclées (29 %) | **OK** | 324 kt en 2024 et 346 kt en 2025 (même source, p. 29) |
| « Collecté mais non recyclé » : 770 kt | **À CORRIGER** | Erreur de logique : 1 085 × 0,71 correspond à ce qui est **mis sur le marché** et non recyclé, pas à ce qui est collecté. Reconstitution [calcul] : plastique collecté 560 à 630 kt ; collecté mais non recyclé **210 à 280 kt** |
| Surtri : 4 centres, 100 kt/an, 70 M€ | **OK** | ([CITEO-SURTRI-2025](https://www.citeo.com/le-mag/les-centres-de-surtri-le-nouveau-maillon-de-la-chaine-du-recyclage-en-france/)). Ils reçoivent justement les balles de « flux développement rigides » ; sortie pure à plus de 90 % |
| B1a : 670 kt/an partant en incinération ou en CSR | **À CORRIGER** | Le calcul hérite de l'erreur des 770 kt. Le plastique d'emballage présent dans les refus des centres de tri est de l'ordre de **85 à 125 kt/an** [calcul, perte de 15 à 20 % selon [CITEO-ECT-2020](https://bo.citeo.com/sites/default/files/2022-06/CITEO_RAPPORT%20ECT%202020.pdf), p. 25]. Ordre de grandeur cohérent avec 12 % de 750 kt de refus = 90 kt [calcul, [OCAPEM-2025](https://www.citeo.com/wp-content/uploads/2026/02/Synthese-du-Rapport-OCAPEM-Amelioration-du-tri-des-petits-emballages.pdf)] |
| B1a = balles triées par infrarouge, pures à plus de 95 %, sans acheteur | **À CORRIGER** | 1) Pureté mesurée en 2023 : PE/PP/PS 88,1 %, films PE 82 %, flux développement 92 % ([CITEO-OBSQUAL-2023](https://bo.citeo.com/sites/default/files/2024-04/Citeo%20-%20Observatoire%20de%20la%20qualit%C3%A9%202023.pdf)). 2) Ces balles ont un repreneur : planchers Valorplast à 0 €/t pour les films, le mélange PE/PP/PS, le PS, le PET opaque et les barquettes ; prix « positif ou nul » ([VALORPLAST-G-2024](https://www.grandchambery.fr/fileadmin/mediatheque/Oxyad/DelmDec/indexdelm_20240530/Annexe34598.pdf)). Le centre de tri ne paie pas pour les évacuer |
| B1a en Île-de-France : 135 kt/an | **À CORRIGER** | Dérivé des 670 kt. À refaire, et de préférence avec des données régionales (ORDIF) plutôt qu'au prorata de 20 % |
| Composition des refus B1b : 35 à 45 % de plastiques | **NON SOURCÉ** | La seule composition nationale trouvée donne 7,5 % de plastiques rigides et 4,5 % de plastiques souples, soit 12 %, plus 70,9 % d'« autres » (fines, imbrûlés, verre, non-emballages) ([OCAPEM-2025](https://www.citeo.com/wp-content/uploads/2026/02/Synthese-du-Rapport-OCAPEM-Amelioration-du-tri-des-petits-emballages.pdf), méthode fragile). Les « autres » peuvent contenir des plastiques hors emballages. **Une caractérisation est nécessaire** |
| Taux de refus : 24,4 % en porte-à-porte, 18,4 % en apport volontaire (« ADEME ») | **À NUANCER** | Chiffres exacts, mais la source est Citeo (données 2020, [CITEO-2023](https://bo.citeo.com/sites/default/files/2023-03/2023_Citeo_Brochure%20co%C3%BBts%20et%20performances.pdf)), pas l'ADEME. Moyenne nationale 2022 : 23,0 % ([CITEO-CAHIER-CS-2024](https://bo.citeo.com/sites/default/files/2024-11/CITEO_Cahier_Collecte%20s%C3%A9lective_nov%202024.pdf)) |
| Refus B1b en Île-de-France : 300 à 500 kt/an (« 2 Mt traitées ») | **NON SOURCÉ, probablement surestimé** | Paris : 106 kt collectées en bac jaune en 2024 ([PARIS-BACJAUNE-2026](https://www.paris.fr/pages/que-devient-le-contenu-de-mon-bac-jaune-36008)). Même extrapolée à toute la région, la collecte sélective ménagère reste loin de 2 Mt. À vérifier auprès de l'ORDIF |
| CSR : environ 300 kt/an ; 80 % des refus non valorisés en CSR | **À METTRE À JOUR** | 370 kt consommées en 2021 ([FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf)) ; 510 kt en 2023, capacité de 2,5 Mt utilisée à 20 % ([SENAT-I980-2025](https://www.senat.fr/enseance/2025-2026/138/Amdt_I-980.html), `secondaire`) |
| Films agricoles : 35 kt/an (2011) | **À METTRE À JOUR** | 102 kt collectées en 2024 ([REUSSIR-2025](https://www.reussir.fr/dechets-plastiques-agricoles-une-collecte-historique-de-102-000-tonnes-pour-adivalor-en-2024)) |
| Films flexibles : 5,7 Mt collectées (2020) | **OK** | Mais seulement 2,4 Mt entrées chez les recycleurs et 1,9 Mt recyclées ([PRE-FILMS-2023](https://www.plasticsrecyclers.eu/wp-content/uploads/2023/06/2023-Flexible-Films-Market-in-Europe_State-of-Play_June-2023.pdf)) |
| Pénalité d'éco-modulation Citeo jusqu'à 1 000 €/t ; montage à trois parties | **NON VÉRIFIÉ** | Le barème Citeo n'a pas été relu. Surtout, la règle UE de comptage du recyclage chimique exclut la part transformée en combustible (« fuel use excluded », [BKV-SUPD-2026](https://bkv-gmbh.de/news-reader-4/implementing-decision-on-supd-published.html)). Si l'huile d'Urban Rig est vendue comme combustible, **aucun crédit de recyclage** n'est possible. Le montage n'est défendable que si l'huile va en vapocraquage |
| DEEE avec retardateurs de flamme bromés au-delà du seuil POP : gate fee de 200 à 400 €/t | **À NUANCER** | Ce sont alors des déchets dangereux : il faut une autorisation ICPE spécifique (rubriques 27xx), ce qui change le permis et le CAPEX. Les prix ne sont pas sourcés |
| Système d'adsorption des halogènes classé FACT HIGH | **À REQUALIFIER** | Donnée constructeur (plaquette OneWorld). Selon votre règle, confiance de 80 à 100 %, sans essai : à classer « constructeur » et non « FACT » |

### Parties 3 et 4 : prix et économie

| Annexe | Verdict | Ce que disent les sources |
|---|---|---|
| Gate fee B1a de 80 à 120 €/t | **À CORRIGER** | Pas de gate fee sur des balles reprises à 0 €/t ou plus (voir plus haut). Hypothèse prudente pour B1a : **0 €/t**, voire un prix d'achat |
| Gate fee B1b de 80 à 120 €/t | **PLAUSIBLE** | Le détenteur des refus paie bien. Mais le concurrent est l'UVE, qui ne paie que 8 €/t de TGAP sur les résidus de tri performants. Le coût médian d'incinération des OMR est de 107 €/t, TGAP comprise |
| CSR à 40–80 €/t de coût total | **À CORRIGER** | Le producteur paie environ 40 à 50 €/t de gate fee à la chaufferie ([FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf)) **en plus** d'un coût de production de 85 à 115 €/t ([NORMANDIE-CSR-2021](https://neci.normandie.fr/sites/default/files/2024-04/02%20info-dechet%20V1.0.pdf)) |
| Prix des déchets plastiques (AEE, 330 €/t pour le PE) | **À NUANCER** | Moyenne UE toutes qualités confondues. En France, les planchers sont à 0 €/t pour les mélanges ; PET clair +240 €/t et PEHD/PP +90 €/t (septembre 2023, [DOMITIENNE-2023](https://www.ladomitienne.com/wp-content/uploads/2024/02/24.010.3_Annexe_DECH_Contrats_Plastiques_lot_3.pdf)) |
| Huile de pyrolyse à 500 €/t (« indice ICIS ») | **NON VÉRIFIÉ** | Les indices ICIS et Platts sont payants. Aucun prix public trouvé |
| Rendement en huile de 62 % sur B1a | **NON VÉRIFIÉ ici** | Hors du périmètre de cette recherche. Il dépend d'une teneur en plastique de 95 %, qui n'est pas démontrée |
| Revenu B1a de 415 €/t et 19,2 M€/an | **À CORRIGER** | Sans gate fee, environ 320 €/t et 14,8 M€/an [calcul : 46 200 t × (0,62 × 500 + 10)], avant correction de la teneur en plastique et sans prix d'huile sourcé |

### Ce qui manque à l'annexe

- **Export** : interdiction des exportations de déchets plastiques hors OCDE à partir du 21/11/2026 ([EC-WSR-PLASTIC](https://environment.ec.europa.eu/topics/waste-and-recycling/waste-shipments/plastic-waste-shipments_en)). C'est un argument favorable, absent de l'annexe.
- **Concurrence en pyrolyse** : TotalEnergies Grandpuits (15 kt/an, approvisionnement auprès de Citeo et de Paprec, [TOTAL-GRANDPUITS-2026](https://totalenergies.com/system/files/documents/totalenergies_pr-totalenergies-starts-production-France-s-first-advanced-plastics-recycling-plant_2026_en.pdf)).
- **Résidus des régénérateurs** : pertes de 27 à 31 % sur les rigides et d'environ 50 % sur les films ménagers ([PRE-PET-2020](https://www.plasticsrecyclers.eu/wp-content/uploads/2022/10/pet-market-in-europe-state-of-play-2020.pdf), [PRE-HDPEPP-2025](https://plasticker.de/docs/news/HDPE_REPORT_2023_screen_spreads_VF%20(1).pdf), [PRE-FILMS-2018](https://www.plasticsrecyclers.eu/wp-content/uploads/2022/10/flexible-films-market.pdf)). C'est probablement le **vrai flux riche en plastique et à valeur négative**. Volume, composition et destination ne sont pas publiés : il faut les obtenir directement auprès des régénérateurs et des centres de surtri.

---

## 3. Recommandations

1. Remplacer B1a par deux flux distincts :
   - **B1a-bis : résidus de régénération et de surtri.** Riches en plastique, avec probablement une gate fee. Volume à établir par enquête directe.
   - **Balles à plancher nul.** À traiter comme une matière première achetée à 0 €/t ou plus, et non comme une source de gate fee.
2. Garder B1b (refus en mélange) avec une gate fee, mais fixer la teneur en plastique **après caractérisation** : 12 % selon OCAPEM, 35 à 45 % selon l'annexe, sans source.
3. Corriger les chiffres TGAP, CSR, centres de tri et films agricoles dans l'annexe.
4. Conditionner tout argument de « crédit de recyclage » à la destination de l'huile (vapocraquage et non combustible).
