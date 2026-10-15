# Message pour Codex : contre-vérification de l'annexe 2

Tu es vérificateur indépendant. Tu n'as pas rédigé ce document. Ton rôle est de trouver les erreurs, pas de valider.

Dépôt : UR_Business_Plan. Lis d'abord `REGLES-DE-RIGUEUR.md` (seize règles) et `working-folder/METHODE-DE-TRAVAIL.md`. N'ouvre jamais `ARCHIVE-NON-VERIFIE/` comme source.

Document à vérifier : la version HTML, qui est la version de référence (décision D-023) : `nouveau-business-plan/annexes/annexe-02-html/index.html` et ses fiches `nouveau-business-plan/annexes/annexe-02-html/preuves/*.html` (chaque lien du texte mène à une fiche). Le HTML est généré à partir de la source `nouveau-business-plan/annexes/ANNEX-02-Technical-Evidence.md`, où les identifiants du registre figurent en commentaire `<!-- [ID] -->` : lis-la pour retrouver un identifiant, sans rien y corriger. Si le HTML et la source divergent, signale-le. Vérifie aussi que chaque taux de confiance respecte l'échelle de la décision D-022.

Pour CHAQUE affirmation chiffrée :
1. Repère l'identifiant cité ([ID] dans `working-folder/params/_evidence.yaml`, [calc:ID] dans `working-folder/controle-sources/calculs.yaml`).
2. Ouvre le document d'origine indiqué par le champ `chemin` (sous `working-folder/reference/preuves/`), à l'emplacement indiqué. Les pages sont celles du fichier PDF (rapport de Chiba : page PDF = page imprimée + 6). Les PDF scannés se lisent sur image ; le japonais se lit dans l'original.
3. Vérifie la valeur, l'unité et le périmètre (matière, date, essai, laboratoire). Pour un [calc:ID], refais le calcul à partir des entrées et vérifie chaque entrée dans sa source.
4. Vérifie l'étiquette : LU (lu dans la source), CALCULÉ, CONSTRUCTEUR (déclaration de OneWorld, attribuée « according to OneWorld »), INCONNU. Signale toute déclaration du constructeur présentée comme une mesure, et toute mesure d'exploitant présentée comme une mesure indépendante.
5. Inscris un verdict par chiffre, à la fin de `working-folder/controle-sources/verifications/registre-verifications.yaml`, au format décrit en tête de ce fichier (agent: codex ; verdict : CONFIRMÉ, DIFFÉRENT, ABSENT, INACCESSIBLE, NON SOURCÉ ou CALCUL FAUX ; citation exacte relevée ; emplacement réel). Un verdict sans citation exacte n'est pas inscrit. Ne modifie ni ne supprime aucune entrée existante.

Points à examiner en priorité :
- tableau 2.2.1 (fiches PDF p. 19 à 24) et tableau 2.2.3 (PDF p. 41 et 42) ;
- tableau 2.4.1 (JLOS PDF p. 45 et 46 ; NKKK, brochure `documents-fournis/Urban Rig Recycling Solutions ENG .pdf` p. 17) ;
- tableau 2.7.1 (KANSO p. 2 ; Oosumi PDF p. 55 et 56 ; Tanabe p. 1 et 5 ; dioxines 2023 p. 1) ;
- tableau 2.7.2 et ses conversions (sources externes IED-2010-75-ANX6-P3, BAT-WI-2019-2010, DK-EPA-2002-PPM, WALLONIE-2003-ANX6-O2 dans `working-folder/reference/sources-externes/registre-sources.yaml` : ouvre les liens) ;
- toutes les phrases « according to OneWorld ».

Interdits : modifier l'annexe (HTML ou Markdown), les paramètres (`working-folder/params/*.yaml`) ou les fiches ; supprimer un fichier ; commiter ; employer le tiret long.

À la fin, rends : le nombre de verdicts par catégorie, la liste des DIFFÉRENT, ABSENT et CALCUL FAUX avec leur ligne, et ce que tu n'as pas pu vérifier, avec la raison.
