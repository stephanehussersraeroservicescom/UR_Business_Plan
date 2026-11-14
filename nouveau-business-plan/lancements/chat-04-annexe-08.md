Chat 4 de la version 3 du plan d'affaires Urban Rig : annexe 8, Plastic Waste Streams (France), les filières du déchet plastique.

Contexte. Le dépôt est sur mon ordinateur : /home/steph/Documents/github/UR_Business_Plan. Les annexes 2 (Technical Evidence), 1 (Process and Technology) et 3 (Output Markets and Pricing) sont rédigées ; elles attendent leur contre-vérification et ma validation. L'annexe 2 a déjà intégré les décisions du lot 1 de Codex (D-033 à D-038). Tout l'ancien travail est dans ARCHIVE-NON-VERIFIE/ et n'a aucune valeur de preuve.

Avant toute chose, lis ces fichiers dans cet ordre, puis résume-moi en cinq lignes ce que tu en retiens :
1. REGLES-DE-RIGUEUR.md (les seize règles, sans exception)
2. CLAUDE.md
3. working-folder/METHODE-DE-TRAVAIL.md
4. nouveau-business-plan/AVANCEMENT.md
5. nouveau-business-plan/STRUCTURE-BP-ET-ANNEXES.md, partie « Annex 8 » (périmètre v3 et deux structures possibles)
6. working-folder/params/_decisions.yaml, toutes les décisions à partir de D-016. En particulier : D-017 (périmètre), D-018 (périmètre de l'annexe 8 et limite avec l'annexe 7), D-029 et D-034 (gaz et rendements des plastiques), D-035 (capacité : 200 m³ par jour, 140 t par jour à 0,7 t/m³ après presse), D-037 (résidus de broyage exclus), D-038 (char des plastiques à 24,6 MJ/kg), D-031 (hydrogène sur charge de plastique seul)
7. Les annexes 1, 2 et 3 en HTML (nouveau-business-plan/annexes/annexe-0X-html/index.html) : rendements par polymère, chlore de l'huile, limites des débouchés (halogènes), prix des produits
8. Dans working-folder/reference/sources-externes/registre-sources.yaml, les fiches déjà inscrites sur le plastique : préfixes RP-, RP2-, PRE-, CITEO-, VALORPLAST-, COTREP-, PRM-, ainsi que ADEME-, ORDIF-, AMORCE-, FNADE-, ECOSYSTEM-, ECOMAISON-, REFASHION-, ADEME-VHU, JRC-2023-PLASTIC-RECYCLING ; et les demandes de working-folder/controle-sources/a-rechercher.yaml qui portent sur le plastique (études ADEME, Valorplast, refus de tri franciliens)
Lance ensuite le contrôle et donne-moi le résultat :
python3 working-folder/controle-sources/verifier_sources.py --sans-parametres

Mission. Rédiger l'annexe 8 de la v3 : quels déchets plastiques existent en France, ce qu'ils deviennent aujourd'hui, et lesquels peuvent alimenter un Urban Rig. L'annexe est en anglais ; nos échanges sont en français.
Périmètre (D-018) : toutes les filières du plastique, ménagères et industrielles, en priorité celles qui sont peu ou pas recyclées. Les flux de plastique seul d'origine industrielle (films, chutes de production) sont ici, pas dans l'annexe 7. Les ordures ménagères résiduelles en mélange relèvent de l'annexe 5 ; ici, on traite le plastique qu'elles contiennent seulement comme une filière parmi d'autres, sans refaire l'annexe 5.
Lecture par filière (famille de résine ou de produit) : polystyrène et polystyrène expansé, films (ménagers, industriels, agricoles), multicouches et composites, PVC, emballages souillés, refus de tri des centres de tri, plastiques des DEEE, des véhicules hors d'usage, du BTP, d'origine textile, et toute autre filière que les sources font apparaître. Pour chaque filière :
- les tonnages en France, et en Île-de-France quand une source le permet ;
- le taux de recyclage réel, distinct du taux de collecte ou de tri ;
- le devenir de ce qui n'est pas recyclé : compactage, export, combustible solide de récupération, incinération, stockage ;
- qui paie quoi : producteurs et éco-organismes (Citeo, Ecosystem, Ecomaison, Refashion et autres), collectivités, détenteurs ; coût d'élimination actuel, TGAP comprise ; prix de reprise quand le flux a une valeur ; contribution européenne sur les emballages plastiques non recyclés ;
- l'aptitude à l'Urban Rig, au seul vu des annexes 1 à 3 : polymères testés ou non (renvoyer aux fiches de l'annexe 2, sans recopier), teneur en PVC, chlore ou brome quand une source la donne, contraintes de débouché de l'huile (annexe 3) ;
- la concurrence pour le flux : recyclage mécanique, recyclage chimique, cimenteries, incinération.
Cas particuliers :
- Polystyrène : vérifier ce que je comprends, à savoir que le polystyrène, surtout expansé, est très peu recyclé, qu'il est compacté ou fondu en blocs et qu'il n'a pas de vrai débouché de valorisation. Montre ce que disent les sources, y compris si elles me contredisent.
- DEEE et véhicules hors d'usage : distinguer les plastiques triés, qui entrent dans le champ, des résidus de broyage, exclus par D-037.
- Les gate fees de cette annexe sont propres aux flux plastiques ; elles alimenteront le modèle (l'annexe 3 les a laissées aux annexes 5 à 8).
Hors champ : la composition détaillée des ordures ménagères résiduelles (annexe 5), les déchets d'activités économiques en mélange (annexe 7), l'aéroport CDG (annexe 6).

Étape 1 : collecte. On commence par là.
- Commence par le registre : ne cherche pas une donnée qui y est déjà. Vérifie le statut de chaque fiche reprise (verifie, secondaire, ancien, non-verifie) et dis-moi celles qui doivent être relues.
- Sources primaires d'abord : ADEME (dont SINOE et les études filières), ministère de la Transition écologique et SDES, éco-organismes (rapports annuels, barèmes), ORDIF pour l'Île-de-France, Eurostat, Plastics Europe et Plastics Recyclers Europe, textes réglementaires (loi AGEC, REP, TGAP, règlement européen sur les emballages). Presse et sites commerciaux seulement en complément, signalés comme tels.
- L'ancienne annexe 8 et le brouillon du 10/10/2026 (ARCHIVE-NON-VERIFIE/pour-finaliser/ANNEX-08-Sector-Plastic-Sorting-Rejects-France.md et ARCHIVE-NON-VERIFIE/working-folder/reference/sources-externes/04-devenir-plastiques-tries/) servent seulement à savoir quoi chercher, jamais de source (règle 16).
- Inscris chaque source au registre avec la page et la citation exacte. Ne change aucune valeur dans working-folder/params/*.yaml.
- Les déclarations de OneWorld sur les plastiques acceptés portent l'étiquette CONSTRUCTEUR (D-016). Les questions à leur poser vont dans a-rechercher.yaml (détenteur OneWorld), sans doublon avec les demandes existantes.
- Notes de travail dans nouveau-business-plan/annexes/notes-recherche-annexe-08/.

Point d'arrêt. Rends-moi quatre choses, puis attends mon accord avant l'étape 2 :
- le compte rendu Trouvé / Partiel / Non trouvé ;
- un tableau provisoire filière par filière : tonnage (France, Île-de-France), taux de recyclage réel, devenir du non recyclé, coût ou prix et qui paie, polymères et chlore, aptitude à l'Urban Rig, concurrence, sources ;
- la liste des hypothèses que je devrai trancher (gate fee par filière, volume accessible, part de PVC, priorité des filières), avec pour chacune les sources qui l'encadrent ;
- pour les affirmations de l'ancienne annexe 8 (archive) : confirmée, contredite ou non trouvée.

Étape 2 : rédaction, après mon accord.
- Source : nouveau-business-plan/annexes/ANNEX-08-Plastic-Waste-Streams.md, organisée par filière (la structure de STRUCTURE est à adapter, pas à suivre telle quelle). Version de lecture : HTML généré dans nouveau-business-plan/annexes/annexe-08-html/ par un générateur adapté de celui de l'annexe 3 (D-023). On corrige la source, jamais le HTML. Les fiches de preuve déjà présentes dans les annexes 1 à 3 sont reprises par lien, pas recopiées.
- Chaque chiffre cite [ID], [calc:ID] ou [hyp:D-xxx] et porte son étiquette : VÉRIFIÉ, LU, CALCULÉ, CONSTRUCTEUR, HYPOTHÈSE ou INCONNU. Les gate fees et volumes retenus pour le modèle sont des hypothèses que je tranche ; l'annexe montre les fourchettes et leurs sources.
- Contrôle : zéro erreur sur l'annexe, HTML à jour. Tire ensuite l'échantillon de trois chiffres (--echantillon 3) et copie-le sous working-folder/out/echantillon-annexe-08.md, pour ne pas écraser ceux des autres annexes.
- Propose dans working-folder/params/_arbitrages.yaml les paramètres que l'annexe confirme ou contredit (gate fees des flux plastiques, volumes accessibles, part de PVC, coût d'élimination de référence). C'est moi qui tranche.
- Prépare la procédure de contre-vérification working-folder/controle-sources/verification-annexe-08.md, sur le modèle de verification-annexe-03.md.
- Mets à jour nouveau-business-plan/AVANCEMENT.md.

Règles de travail.
- Aucun chiffre sans document lu. « NON TROUVÉ » est signalé tout de suite, avec ce que tu as cherché et où.
- Le mot « sûr » est réservé aux chiffres vérifiés.
- Quand deux sources divergent, montre les deux.
- Un taux de recyclage n'est jamais confondu avec un taux de collecte ou de tri ; précise toujours le périmètre (ménager ou non, emballages ou tous plastiques, année).
- Pas d'anciennes versions de l'annexe dans le dépôt. Aucune suppression de fichier sans mon accord explicite, aucun commit. Git en lecture seule, avec git --no-optional-locks.
- Jamais de tiret long.
- Si le chat devient long, écris une note de passation dans nouveau-business-plan/annexes/notes-recherche-annexe-08/, mets à jour AVANCEMENT et préviens-moi : on continuera dans un nouveau chat.
