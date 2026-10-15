Chat 1 de la version 3 du plan d'affaires Urban Rig : annexe 2, Technical Evidence.

**Contexte.** Le dépôt est sur mon ordinateur : `/home/steph/Documents/github/UR_Business_Plan`. Depuis le 14/10/2026, le plan d'affaires repart d'une page blanche. Tout l'ancien travail est dans `ARCHIVE-NON-VERIFIE/` et n'a aucune valeur de preuve.

**Avant toute chose**, lis ces fichiers dans cet ordre, puis résume-moi en cinq lignes ce que tu en retiens :
1. `REGLES-DE-RIGUEUR.md` (les seize règles, sans exception)
2. `CLAUDE.md`
3. `working-folder/METHODE-DE-TRAVAIL.md`
4. `nouveau-business-plan/AVANCEMENT.md`
5. `nouveau-business-plan/STRUCTURE-BP-ET-ANNEXES.md`, partie « Annex 2 »
6. `working-folder/reference/preuves/README.md` et `working-folder/params/_evidence.yaml`

Lance ensuite le contrôle et donne-moi le résultat :
`python3 working-folder/controle-sources/verifier_sources.py`

**Mission.** Rédiger l'annexe 2 de la v3 : ce que la machine produit réellement (rendements, qualité de l'huile, du gaz et du char, émissions, bilan énergétique). Elle s'appuie uniquement sur des documents d'origine. L'annexe est en anglais ; nos échanges sont en français.

**Étape 1 : inventaire des preuves. On commence par là.**
- Ouvre chaque document de `working-folder/reference/preuves/` utile à l'annexe 2 : rapports d'essais, rapports remis à la préfecture de Chiba, chromatographie, émissions et dioxines, énergie, documents de OneWorld. Lis l'original, page par page. Pour un document en japonais, donne ta traduction en la signalant comme telle.
- Pour chaque chiffre, relève :
  - le document et la page ;
  - la citation exacte, dans la langue d'origine ;
  - l'unité ;
  - les conditions de l'essai (matière, masse, date, qui a mesuré, quel laboratoire) ;
  - la nature : mesure par un tiers, mesure du constructeur, ou déclaration du constructeur.
- Consigne l'inventaire dans `nouveau-business-plan/annexes/notes-recherche-annexe-02/inventaire-preuves.md`.
- Inscris ou complète les entrées de `working-folder/params/_evidence.yaml` (chemin, page, contenu, citation). Ne change aucune valeur dans `working-folder/params/*.yaml`.
- Les déclarations de OneWorld sont admises avec l'étiquette CONSTRUCTEUR (décision D-016), à condition de figurer dans un document de OneWorld cité avec la page. Pour chacune qui n'est pas appuyée par un rapport de mesure, et pour chaque trou, ajoute une entrée `a_demander` (détenteur OneWorld) dans `working-folder/controle-sources/a-rechercher.yaml`.
- Tu peux regarder l'ancienne annexe 2 de l'archive pour savoir quoi chercher, jamais comme source.

**Point d'arrêt.** Rends-moi trois choses, puis attends mon accord avant l'étape 2 :
- le compte rendu Trouvé / Partiel / Non trouvé ;
- la liste des questions à poser à OneWorld ;
- les écarts entre ce que disent les documents et ce qu'affirmait l'ancienne annexe.

**Étape 2 : rédaction, après mon accord.**
- Fichier : `nouveau-business-plan/annexes/ANNEX-02-Technical-Evidence.md`, sur le plan de STRUCTURE.
- Chaque chiffre cite `[ID]`, `[calc:ID]` ou `[hyp:D-xxx]` et porte son étiquette : VÉRIFIÉ, LU, CALCULÉ, CONSTRUCTEUR, HYPOTHÈSE ou INCONNU.
- Une déclaration de OneWorld est toujours attribuée (« according to OneWorld »). Elle n'est jamais présentée comme une mesure indépendante.
- Lance le contrôle sur l'annexe : il faut zéro erreur. Tire ensuite l'échantillon de trois chiffres que je vérifierai (`--echantillon 3`).
- Propose dans `working-folder/params/_arbitrages.yaml` les paramètres du modèle que l'annexe confirme ou contredit. C'est moi qui tranche.
- Mets à jour `nouveau-business-plan/AVANCEMENT.md`. Prépare le message à donner à Codex pour la contre-vérification.

**Règles de travail.**
- Aucun chiffre sans document lu. « NON TROUVÉ » est signalé tout de suite, avec ce que tu as cherché et où.
- Le mot « sûr » est réservé aux chiffres vérifiés.
- Aucune suppression de fichier, aucun commit. Git en lecture seule, avec `git --no-optional-locks`.
- Jamais de tiret long.
- Si le chat devient long, écris une note de passation dans `nouveau-business-plan/annexes/notes-recherche-annexe-02/`, mets à jour AVANCEMENT et préviens-moi : on continuera dans un nouveau chat.
