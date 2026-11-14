Chat 2 de la version 3 du plan d'affaires Urban Rig : annexe 1, Process and Technology.

Contexte. Le dépôt est sur mon ordinateur : /home/steph/Documents/github/UR_Business_Plan. L'annexe 2 (Technical Evidence) a été rédigée dans le chat 1 ; elle est en attente de contre-vérification par Codex et de ma validation. Tout l'ancien travail est dans ARCHIVE-NON-VERIFIE/ et n'a aucune valeur de preuve.

Avant toute chose, lis ces fichiers dans cet ordre, puis résume-moi en cinq lignes ce que tu en retiens :
1. REGLES-DE-RIGUEUR.md (les seize règles, sans exception)
2. CLAUDE.md
3. working-folder/METHODE-DE-TRAVAIL.md
4. nouveau-business-plan/AVANCEMENT.md
5. nouveau-business-plan/STRUCTURE-BP-ET-ANNEXES.md, partie « Annex 1 »
6. working-folder/params/_decisions.yaml, décisions D-016 à D-023 (elles s'appliquent aussi à l'annexe 1)
7. nouveau-business-plan/annexes/notes-recherche-annexe-02/passation-chat1-2026-10-14-soir.md, inventaire-preuves.md et le dossier releves/
Lance ensuite le contrôle et donne-moi le résultat :
python3 working-folder/controle-sources/verifier_sources.py --sans-parametres

Mission. Rédiger l'annexe 1 de la v3 : ce qu'est l'Urban Rig et comment il fonctionne (réacteur, vapeur surchauffée, zones de température, recyclage des gaz, fonctionnement continu), ce qui en sort (huile et ses fractions, char, métaux, gaz), ses caractéristiques (matières acceptées et besoin de pré-tri, traitement des fumées et dioxines, séparation des fractions, pilotage, énergie, modularité, sources de revenus) et sa comparaison avec les autres voies de traitement. L'annexe est en anglais ; nos échanges sont en français.

Cohérence avec l'annexe 2. L'annexe 1 décrit ; l'annexe 2 prouve les performances. L'annexe 1 cite les mêmes documents d'origine que l'annexe 2 (identifiants du registre et de _evidence.yaml), jamais le texte de l'annexe 2 comme source. Quand une fiche de preuve de l'annexe 2 couvre déjà une source ou un calcul, l'annexe 1 renvoie à cette fiche au lieu d'en créer une seconde. Si un document semble contredire l'annexe 2, tu me le signales ; tu ne tranches pas en silence.

Étape 1 : collecte. On commence par là.
- Pars de l'inventaire du chat 1 (inventaire-preuves.md et releves/) : ne relis un document que si l'inventaire ne suffit pas.
- Lis les documents de working-folder/reference/preuves/ utiles à l'annexe 1 que le chat 1 n'a pas exploités (par exemple « transport installation and maintenance.pdf », « patent list.xlsx », la présentation « Urban RIg ENG », la documentation SEA CORAL). Pour un document en japonais, donne ta traduction en la signalant comme telle.
- Pour la comparaison avec les autres voies (incinération, gazéification, recyclage mécanique, autres pyrolyses), uniquement des sources primaires ou réglementaires, inscrites au registre avec page et citation exacte.
- Inscris ou complète les entrées de working-folder/params/_evidence.yaml et du registre. Ne change aucune valeur dans working-folder/params/*.yaml.
- Les déclarations de OneWorld portent l'étiquette CONSTRUCTEUR (décision D-016). Pour chacune sans rapport de mesure, et pour chaque trou, ajoute une entrée a_demander (détenteur OneWorld) dans working-folder/controle-sources/a-rechercher.yaml, sans doublon avec R-009 à R-022 ni avec l'email à Peter (notes-recherche-annexe-02/email-peter-2026-10-14.md).
- Notes de travail dans nouveau-business-plan/annexes/notes-recherche-annexe-01/.

Point d'arrêt. Rends-moi trois choses, puis attends mon accord avant l'étape 2 :
- le compte rendu Trouvé / Partiel / Non trouvé ;
- les nouvelles questions à poser à OneWorld ;
- pour chaque affirmation de l'ancienne annexe 1 (archive, à lire seulement pour savoir quoi vérifier) : confirmée par un document, déclaration de OneWorld seulement, contredite, ou non trouvée. En particulier : « accepts all waste types without pre-sorting », « zero dioxins », « energy self-sufficiency », « four revenue streams », « 7-zone continuous reactor ».

Étape 2 : rédaction, après mon accord.
- Source : nouveau-business-plan/annexes/ANNEX-01-Process-and-Technology.md, sur le plan de STRUCTURE. Version de lecture : HTML généré dans nouveau-business-plan/annexes/annexe-01-html/ (index.html et preuves/), par un générateur adapté de celui de l'annexe 2 (décision D-023). On corrige la source, jamais le HTML.
- Chaque chiffre cite [ID], [calc:ID] ou [hyp:D-xxx] et porte son étiquette : VÉRIFIÉ, LU, CALCULÉ, CONSTRUCTEUR, HYPOTHÈSE ou INCONNU. Une déclaration de OneWorld est toujours attribuée (« according to OneWorld »).
- Contrôle : zéro erreur sur l'annexe, HTML à jour (pas d'avertissement « HTML plus ancien que sa source »), puis l'échantillon de trois chiffres pour moi (--echantillon 3).
- Propose dans working-folder/params/_arbitrages.yaml les paramètres du modèle que l'annexe confirme ou contredit. C'est moi qui tranche.
- Mets à jour nouveau-business-plan/AVANCEMENT.md et prépare le message pour Codex (contre-vérification sur le HTML).

Règles de travail.
- Aucun chiffre sans document lu. « NON TROUVÉ » est signalé tout de suite, avec ce que tu as cherché et où.
- Le mot « sûr » est réservé aux chiffres vérifiés.
- Pas d'anciennes versions de l'annexe dans le dépôt. Aucune suppression de fichier sans mon accord explicite, aucun commit. Git en lecture seule, avec git --no-optional-locks.
- Jamais de tiret long.
- Si le chat devient long, écris une note de passation dans nouveau-business-plan/annexes/notes-recherche-annexe-01/, mets à jour AVANCEMENT et préviens-moi : on continuera dans un nouveau chat.
