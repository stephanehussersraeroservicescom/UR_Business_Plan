Chat 3 de la version 3 du plan d'affaires Urban Rig : annexe 3, Output Markets and Pricing (marchés et prix des produits, et prix de l'énergie achetée).

Contexte. Le dépôt est sur mon ordinateur : /home/steph/Documents/github/UR_Business_Plan. Les annexes 2 (Technical Evidence, chat 1) et 1 (Process and Technology, chat 2) sont rédigées ; elles attendent leur contre-vérification et ma validation. Tout l'ancien travail est dans ARCHIVE-NON-VERIFIE/ et n'a aucune valeur de preuve.

Avant toute chose, lis ces fichiers dans cet ordre, puis résume-moi en cinq lignes ce que tu en retiens :
1. REGLES-DE-RIGUEUR.md (les seize règles, sans exception)
2. CLAUDE.md
3. working-folder/METHODE-DE-TRAVAIL.md
4. nouveau-business-plan/AVANCEMENT.md
5. nouveau-business-plan/STRUCTURE-BP-ET-ANNEXES.md, partie « Annex 3 »
6. working-folder/params/_decisions.yaml, toutes les décisions à partir de D-016 (elles s'appliquent aussi à l'annexe 3)
7. Les annexes 1 et 2 en HTML (nouveau-business-plan/annexes/annexe-01-html/index.html et annexe-02-html/index.html) : elles définissent les produits et leurs propriétés mesurées
8. Dans working-folder/reference/sources-externes/registre-sources.yaml et working-folder/params/_evidence.yaml, les fiches déjà inscrites sur les prix (huile, fioul, électricité, char, métaux, carbone), et la demande R-004 de working-folder/controle-sources/a-rechercher.yaml
Lance ensuite le contrôle et donne-moi le résultat :
python3 working-folder/controle-sources/verifier_sources.py --sans-parametres

Mission. Rédiger l'annexe 3 de la v3 : ce que valent les produits de l'Urban Rig en France et en Europe, et à quel prix on achète l'énergie dont il a besoin. L'annexe est en anglais ; nos échanges sont en français. Pour chaque produit (huile et ses fractions, char, métaux récupérés), et pour le carbone :
- les débouchés possibles (par exemple, pour l'huile : combustible, charge de vapocraqueur ou de raffinerie, carburéacteur après traitement) ;
- les spécifications exigées par chaque débouché, comparées aux propriétés mesurées de l'annexe 2 (citer les mêmes fiches, pas le texte de l'annexe 2) ;
- le statut réglementaire du produit (déchet ou produit, sortie du statut de déchet, enregistrements éventuels) ;
- les prix publiés ou observables, avec leur source, leur date et leur périmètre ; quand les cotations sont payantes (ICIS, Platts, Argus), NON TROUVÉ et entrée a_demander ;
- les acheteurs possibles, nommés seulement si une source le permet ;
- ce qui n'est pas vendable et ce qu'il en coûte de s'en défaire.
Pour le carbone : les mécanismes qui pourraient s'appliquer (marché européen du carbone et incinération des déchets, standards volontaires, label bas-carbone), à quelles conditions, et le CO2 évité par rapport à l'incinération, calculé avec des facteurs d'émission sourcés. Aucun crédit n'est compté sans méthode éligible identifiée.
Ajoute une section sur les prix de l'énergie achetée en France (fioul ou GNR, électricité), utiles au modèle.
Hors champ : les gate fees, traités par gisement dans les annexes 5 à 8.

Étape 1 : collecte. On commence par là.
- Commence par le registre : ne cherche pas une donnée qui y est déjà.
- Sources primaires d'abord : séries publiques de prix (ministère de la Transition écologique, INSEE, Eurostat, Commission européenne), textes réglementaires, spécifications publiées par les acheteurs ou les organismes de normalisation, rapports annuels. Presse et sites commerciaux seulement en complément, signalés comme tels.
- Inscris chaque source au registre avec la page et la citation exacte. Ne change aucune valeur dans working-folder/params/*.yaml.
- Les déclarations de OneWorld (débouchés, acheteurs, prix obtenus au Japon) portent l'étiquette CONSTRUCTEUR (décision D-016). Les questions à leur poser vont dans a-rechercher.yaml (détenteur OneWorld), sans doublon avec R-009 à R-032.
- Notes de travail dans nouveau-business-plan/annexes/notes-recherche-annexe-03/.

Point d'arrêt. Rends-moi quatre choses, puis attends mon accord avant l'étape 2 :
- le compte rendu Trouvé / Partiel / Non trouvé ;
- un tableau provisoire produit par produit : débouché, spécification, prix trouvé (source, date, périmètre), écart avec les propriétés mesurées ;
- la liste des hypothèses de prix que je devrai trancher, avec pour chacune les sources qui l'encadrent ;
- pour les affirmations de l'ancienne annexe 3 (archive, à lire seulement pour savoir quoi vérifier : scénarios de prix de l'huile, « market tiers » du char, prime des métaux non oxydés, crédits carbone) : confirmée, contredite ou non trouvée.

Étape 2 : rédaction, après mon accord.
- Source : nouveau-business-plan/annexes/ANNEX-03-Output-Markets-and-Pricing.md, sur le plan de STRUCTURE, adapté si nécessaire (en particulier la section sur l'énergie achetée). Version de lecture : HTML généré dans nouveau-business-plan/annexes/annexe-03-html/ par un générateur adapté de ceux des annexes 1 et 2 (décision D-023). On corrige la source, jamais le HTML. Les fiches de preuve déjà présentes dans les annexes 1 et 2 sont reprises par lien, pas recopiées.
- Chaque chiffre cite [ID], [calc:ID] ou [hyp:D-xxx] et porte son étiquette : VÉRIFIÉ, LU, CALCULÉ, CONSTRUCTEUR, HYPOTHÈSE ou INCONNU. Les prix retenus pour le modèle sont des hypothèses que je tranche ; l'annexe montre les fourchettes et leurs sources.
- Contrôle : zéro erreur sur l'annexe, HTML à jour. Tire ensuite l'échantillon de trois chiffres (--echantillon 3) et copie-le sous working-folder/out/echantillon-annexe-03.md, pour ne pas écraser ceux des autres annexes.
- Propose dans working-folder/params/_arbitrages.yaml les paramètres de prix que l'annexe confirme ou contredit (prix de l'huile, du char, des métaux, du verre, du carbone, du fioul, de l'électricité). C'est moi qui tranche.
- Prépare la procédure de contre-vérification working-folder/controle-sources/verification-annexe-03.md, sur le modèle de verification-annexe-02.md (lots adaptés à l'annexe 3).
- Mets à jour nouveau-business-plan/AVANCEMENT.md.

Règles de travail.
- Aucun chiffre sans document lu. « NON TROUVÉ » est signalé tout de suite, avec ce que tu as cherché et où.
- Le mot « sûr » est réservé aux chiffres vérifiés.
- Quand deux sources divergent, montre les deux.
- Pas d'anciennes versions de l'annexe dans le dépôt. Aucune suppression de fichier sans mon accord explicite, aucun commit. Git en lecture seule, avec git --no-optional-locks.
- Jamais de tiret long.
- Si le chat devient long, écris une note de passation dans nouveau-business-plan/annexes/notes-recherche-annexe-03/, mets à jour AVANCEMENT et préviens-moi : on continuera dans un nouveau chat.
