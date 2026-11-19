# Contre-vérification de l'annexe 4 par ChatGPT (Codex, en local)

Procédure du 19/11/2026, adaptée de `verification-annexe-09.md`. Le vérificateur est ChatGPT dans son mode Codex, projet « vérification Urban Rig », relié au dossier local du dépôt. Il lit les fichiers directement sur l'ordinateur et suit `AGENTS.md`. Il n'écrit que dans `working-folder/controle-sources/verifications/`.

## La procédure

| Étape | Qui | Quoi |
|---|---|---|
| 1 | ChatGPT (Codex) | Test d'accès : dossier lu, consignes d'`AGENTS.md`, lecture d'un PDF, accès internet |
| 2 | ChatGPT (Codex) | Vérification d'un lot (une nouvelle conversation par lot, deux lots). Il écrit son rapport dans `verifications/` et ses verdicts dans `verifications/registre-verifications.yaml` |
| 3 | Claude (nouveau chat) | Relire chaque écart dans la source d'origine et le classer : ACCEPTÉ (corrigé), CONTESTÉ (avec citation), À TRANCHER. Fichier `verifications/ecarts-annexe-04.md` |
| 4 | ChatGPT (Codex) | Facultatif : second tour sur les points CONTESTÉS |
| 5 | Stéphane | Trancher les points restants ; commiter et pousser |

## Points d'attention propres à l'annexe 4

- **Legifrance** bloque souvent les robots : utiliser la copie consolidée AIDA/INERIS en la signalant comme secondaire.
- **PDF AIDA** (brochure de la nomenclature v58, note DGPR de 2022) : vérifier p. 33, 38, 39 (brochure) et p. 57, 60, 84 (note).
- **Hypothèse D-052** (classement 2771, IED 3520 par prudence, 3532 pour le pré-traitement) : posée par Claude, pas encore tranchée. Le vérificateur la juge (fondée, fragile, à remplacer) et cherche toute doctrine ou décision contraire, en particulier sur l'article 3 (40) de la directive IED et l'assujettissement de la pyrolyse à la TGAP.

## Message à coller dans Codex (une nouvelle conversation par lot)

```text
Tu es vérificateur indépendant de l'annexe 4 (Country Study: France, réglementation, permis, fiscalité, marché et concurrence) du plan d'affaires Urban Rig : unité de pyrolyse de déchets du constructeur japonais OneWorld, porteur du plan. L'annexe a été rédigée par une autre IA (Claude). Ton rôle est de trouver les erreurs et de contester les interprétations fragiles. Tu ne cherches ni à valider, ni à être d'accord. Tes consignes permanentes sont dans AGENTS.md et REGLES-DE-RIGUEUR.md.

ÉTAPE 0 : TEST D'ACCÈS. Réponds à ces quatre points avant toute vérification, puis attends ma réponse.
1. Quel est le chemin du dossier que tu lis ? Es-tu en mode local ?
2. Résume en trois lignes tes consignes d'AGENTS.md.
3. Ouvre https://aida.ineris.fr/sites/default/files/2026-07/BrochureNom_v58.pdf et recopie le régime de la rubrique 2771 (p. 33). Si tu ne peux pas, dis avec quel outil tu as essayé.
4. As-tu accès à internet dans cette session ? Peux-tu lire un PDF en ligne ?

CE QUE TU VÉRIFIES
- La version de référence est le HTML : nouveau-business-plan/annexes/annexe-04-html/index.html et ses fiches annexe-04-html/preuves/*.html (fiches 4.R, 4.P, 4.L, 4.C et 4.D). Les fiches 1.x, 2.x, 3.x, 5.x, 7.x, 8.x et 9.x renvoient à d'autres annexes, soumises à leur propre vérification : vérifie seulement que la valeur reprise est la même.
- Registres : working-folder/reference/sources-externes/registre-sources.yaml (fiches A4-*, SDES-2022, CIBS-TGAP-2026 et les fiches A8-CST-* citées), working-folder/controle-sources/calculs.yaml (CALC-A4-*), working-folder/params/_decisions.yaml (D-052, et D-017 et D-035 citées).
- La source Markdown nouveau-business-plan/annexes/ANNEX-04-France.md porte les identifiants entre crochets : sers-t'en pour retrouver un identifiant, jamais comme preuve.
- Rien dans ARCHIVE-NON-VERIFIE/ n'est une source. Ignore _to_delete/.

POUR CHAQUE AFFIRMATION CHIFFRÉE DU LOT
1. Ouvre le document d'origine indiqué par la fiche, à l'emplacement indiqué. Ne te fie pas à la fiche.
2. Donne un verdict : CONFIRMÉ, DIFFÉRENT, ABSENT, INACCESSIBLE, NON SOURCÉ ou CALCUL FAUX. Refais chaque calcul toi-même.
3. Vérifie l'étiquette et le taux de confiance. Sont des erreurs : une donnée de OneWorld présentée comme une mesure ; une source secondaire ou ancienne non signalée ; une hypothèse présentée comme un fait.
4. Vérifie le périmètre : France ou Île-de-France, année, base humide ou sèche, PCI ou PCS, conditions de pyrolyse (température, échelle, catalyseur).

NEUTRALITÉ ET CONTRADICTION (le plus important)
- Pour chaque conclusion du lot, cherche activement une autre lecture des mêmes données. Dis laquelle te paraît la plus solide, avec la citation qui l'appuie.
- Signale : une règle appliquée à l'Urban Rig sans être présentée comme hypothèse ; un texte abrogé ou modifié depuis ; un tarif sans précision HT ou TTC, ni de périmètre ; une source plus récente ou plus solide que celle citée.
- Si tu n'es pas d'accord avec l'hypothèse D-052, dis-le et explique pourquoi.
- Ta mémoire d'entraînement n'est pas une source.

CE QUE TU ÉCRIS (et rien d'autre)
A. Ton rapport, dans working-folder/controle-sources/verifications/AAAA-MM-JJ-codex-annexe-04-lot-N.md : accès internet et lecture des PDF ; tableau des verdicts (N° | section ou fiche | affirmation | valeur annoncée | source citée | verdict | citation exacte relevée | emplacement réel | commentaire) ; écarts E-1, E-2... (ce que dit l'annexe, ce que dit la source, gravité, correction proposée) ; autres interprétations ; ce que tu n'as pas pu vérifier ; décompte des verdicts.
B. Tes verdicts qui portent une citation exacte, ajoutés à la fin de working-folder/controle-sources/verifications/registre-verifications.yaml, au format décrit dans AGENTS.md (agent: codex). Tu ajoutes ; tu ne modifies ni ne supprimes rien.

Tu ne modifies aucun autre fichier. Aucune suppression, aucun commit. N'emploie jamais le tiret long.

LOT À VÉRIFIER : [remplacer par une ligne du tableau des lots]
```

## Un seul lot

| Lot | Ligne à coller à la fin du message |
|---|---|
| 1 | `Lot unique : toute l'annexe 4. Vérifie les rubriques ICPE à leur page, les délais DRIEAT, l'article L. 541-1, les tarifs de TGAP et les données ORDIF ; refais CALC-A4-* ; cherche les projets de pyrolyse de déchets en mélange en France et les aides publiques applicables (R-051).` |

## Étape 3 : message à coller dans un nouveau chat Claude (projet « business plan »)

```text
Chat de traitement des écarts de l'annexe 4, après contre-vérification par ChatGPT (Codex).

Lis d'abord REGLES-DE-RIGUEUR.md, CLAUDE.md, working-folder/METHODE-DE-TRAVAIL.md et nouveau-business-plan/AVANCEMENT.md, puis les rapports dans working-folder/controle-sources/verifications/ (fichiers *-codex-annexe-04-lot-*.md).

Pour chaque écart (E-x) et chaque « autre interprétation » :
1. Rouvre toi-même le document d'origine à l'emplacement cité.
2. Classe le point dans working-folder/controle-sources/verifications/ecarts-annexe-04.md : ACCEPTÉ (tu corriges la source et régénères le HTML), CONTESTÉ (avec la citation qui contredit le vérificateur), À TRANCHER (c'est moi qui décide).
3. Vérifie que les verdicts ajoutés dans registre-verifications.yaml portent une citation exacte ; signale ceux qui n'en ont pas, sans les modifier.
À la fin : contrôle à zéro erreur, HTML à jour, AVANCEMENT mis à jour, et la liste des points À TRANCHER. Aucune suppression de fichier, aucun commit, jamais de tiret long.
```
