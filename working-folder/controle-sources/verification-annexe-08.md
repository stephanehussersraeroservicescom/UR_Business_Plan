# Contre-vérification de l'annexe 8 par ChatGPT (Codex, en local)

Procédure du 16/10/2026, adaptée de `verification-annexe-03.md`. Le vérificateur est ChatGPT dans son mode Codex, projet « vérification Urban Rig », relié au dossier local du dépôt. Il lit les fichiers directement sur l'ordinateur et suit `AGENTS.md`. Il n'écrit que dans `working-folder/controle-sources/verifications/`.

## La procédure en cinq étapes

| Étape | Qui | Quoi |
|---|---|---|
| 1 | ChatGPT (Codex) | Test d'accès : dossier lu, consignes d'`AGENTS.md`, lecture d'un PDF, accès internet |
| 2 | ChatGPT (Codex) | Vérification d'un lot (une nouvelle conversation par lot, cinq lots). La plupart des sources de l'annexe 8 sont publiques : l'accès internet est nécessaire. Il écrit lui-même son rapport dans `verifications/` et ses verdicts dans `verifications/registre-verifications.yaml` |
| 3 | Claude (nouveau chat) | Relire chaque écart dans la source d'origine et le classer : ACCEPTÉ (corrigé), CONTESTÉ (avec citation), À TRANCHER. Fichier `verifications/ecarts-annexe-08.md` |
| 4 | ChatGPT (Codex) | Facultatif : second tour sur les points CONTESTÉS |
| 5 | Stéphane | Trancher les points restants ; commiter et pousser |

L'annexe 8 passe « contre-vérifiée » dans `AVANCEMENT.md` quand les cinq lots sont traités et que chaque écart a un statut final.

## Points d'attention

- **Mode local, pas worktree**, et **une nouvelle conversation par lot** : Codex relit `AGENTS.md` au début de chaque session, et les consignes ne se diluent pas.
- **Sources publiques** (presque toutes : statistiques, textes réglementaires, rapports) : si Codex n'a pas accès à internet, il les marque INACCESSIBLE. On les fait alors vérifier par ChatGPT avec la recherche web, à partir de `prompts-verification-externe.md` (prompt 2).
- **Autorisations.** Si Codex demande l'autorisation d'écrire, acceptez seulement pour son rapport et pour `registre-verifications.yaml`, tous deux dans `working-folder/controle-sources/verifications/`. Refusez toute modification ailleurs.
- **Aucun besoin de pousser sur GitHub avant** : Codex lit le dossier local. On commite après, pour garder ses rapports.

## Message à coller dans Codex (une nouvelle conversation par lot)

Remplacer la dernière ligne par l'un des lots du tableau qui suit le message.

```text
Tu es vérificateur indépendant de l'annexe 8 (Plastic Waste Streams, filières du déchet plastique en France) du plan d'affaires Urban Rig : unité de pyrolyse de déchets du constructeur japonais OneWorld, porteur du plan. L'annexe a été rédigée par une autre IA (Claude) à partir de recherches faites en partie par des sous-agents. Ton rôle est de trouver les erreurs et de contester les interprétations fragiles. Tu ne cherches ni à valider, ni à être d'accord, ni à arrondir les angles. Tes consignes permanentes sont dans AGENTS.md et REGLES-DE-RIGUEUR.md.

ÉTAPE 0 : TEST D'ACCÈS. Réponds à ces quatre points avant toute vérification, puis attends ma réponse.
1. Quel est le chemin du dossier que tu lis ? Es-tu en mode local ?
2. Résume en trois lignes tes consignes d'AGENTS.md : quel fichier tu vérifies, où tu as le droit d'écrire, ce que tu ne dois jamais faire.
3. Ouvre https://www.insee.fr/fr/statistiques/2015775 et recopie le titre du tableau. Si tu ne peux pas, dis avec quel outil tu as essayé.
4. As-tu accès à internet dans cette session ? Peux-tu lire un PDF en ligne ?

CE QUE TU VÉRIFIES
- La version de référence est le HTML : nouveau-business-plan/annexes/annexe-08-html/index.html et ses fiches annexe-08-html/preuves/*.html (fiches 8.M, 8.R, 8.P, 8.L, 8.C et 8.D). Les fiches 1.x, 2.x et 3.x renvoient aux annexes 1 à 3, soumises à leur propre vérification : vérifie seulement que la valeur reprise est la même.
- Chaque fiche de source donne le lien, l'emplacement, la citation et les valeurs relevées ; pour les fiches anciennes relues en octobre 2026, la citation et l'emplacement sont dans le champ relecture_a8_2026_10_15. Chaque fiche de calcul donne la formule, les entrées et le résultat. Les registres sont working-folder/reference/sources-externes/registre-sources.yaml (fiches A8-* et fiches relues), working-folder/params/_evidence.yaml, working-folder/controle-sources/calculs.yaml (calculs CALC-A8-*) et working-folder/params/_decisions.yaml (D-018, D-035, D-037, D-039 à D-042).
- 28 fiches clés ont déjà été rouvertes par un sous-agent vérificateur (statut verifie-recontrole, champ recontrole_a8) : vérifie-les quand même, ce n'est pas une preuve.
- Les prix d'entrée par flux sont des valeurs par défaut que l'opérateur du modèle peut changer (décisions D-041 et D-042). Vérifie que chaque valeur source est la plus récente publiée et signale une valeur plus récente si tu en trouves une.
- Vérifie spécialement que chaque taux de recyclage n'est pas confondu avec un taux de collecte ou de tri, et que son périmètre (ménager ou non, emballages ou tous plastiques, année) est juste.
- La source Markdown nouveau-business-plan/annexes/ANNEX-08-Plastic-Waste-Streams.md porte les identifiants entre crochets : sers-t'en pour retrouver un identifiant, jamais comme preuve.
- Rien dans ARCHIVE-NON-VERIFIE/ n'est une source. Ignore _to_delete/ s'il existe.

POUR CHAQUE AFFIRMATION CHIFFRÉE DU LOT
1. Ouvre le document d'origine indiqué par la fiche, à l'emplacement indiqué. Ne te fie pas à la fiche : elle peut être fausse. Pour un texte de loi, lis la version en vigueur (Légifrance, EUR-Lex) et signale si la fiche s'appuie sur une reproduction.
2. Donne un verdict : CONFIRMÉ, DIFFÉRENT, ABSENT, INACCESSIBLE, NON SOURCÉ ou CALCUL FAUX. Refais chaque calcul toi-même.
3. Vérifie l'étiquette et le taux de confiance (échelle de l'index des fiches de l'annexe 8). Sont des erreurs : une donnée de OneWorld présentée comme une mesure ou une vérification ; une source commerciale ou secondaire non signalée ; une proposition de texte présentée comme adoptée.
4. Vérifie le périmètre : même produit et même qualité, même pays, même base (hors taxes ou TTC, départ ou livré, à la frontière), même devise, même période, même unité (PCI ou PCS, litre ou tonne).

NEUTRALITÉ ET CONTRADICTION (le plus important)
- Ne suppose ni que l'annexe a raison, ni qu'elle a tort : lis la source.
- Pour chaque conclusion du lot, cherche activement une autre lecture des mêmes données. Dis laquelle te paraît la plus solide, avec la citation qui l'appuie.
- Signale : un taux de collecte ou de tri présenté comme un taux de recyclage ; un prix appliqué à un flux qui n'en a pas la qualité ; un prix sans précision de taxe (TGAP, HT) ; les sources commerciales, militantes ou secondaires utilisées comme principales ; une aptitude à l'Urban Rig affirmée sans essai ; ce qui est omis et affaiblirait la conclusion.
- Si tu n'es pas d'accord avec une décision de méthode du projet (D-016 à D-042), dis-le et explique pourquoi.
- Ta mémoire d'entraînement n'est pas une source. Pour une norme ou un texte réglementaire, ouvre le texte ; sans accès internet, marque-le INACCESSIBLE.

CE QUE TU ÉCRIS (et rien d'autre)
A. Ton rapport, dans working-folder/controle-sources/verifications/2026-10-JJ-codex-annexe-08-lot-N.md (date du jour, numéro du lot) :
1. « Accès internet : OUI ou NON » ; « Lecture des PDF : OUI, NON ou PARTIELLE ».
2. Tableau des verdicts : N° | Section ou fiche | Affirmation (courte) | Valeur annoncée | Source citée (identifiant, fichier, page) | Verdict | Citation exacte relevée | Emplacement réel | Commentaire.
3. Écarts, un par bloc, numérotés E-1, E-2, etc. : ce que dit l'annexe ; ce que dit la source (citation) ; gravité (bloquant, important, mineur) ; correction proposée.
4. Autres interprétations : pour chaque conclusion discutable, la lecture de l'annexe, ta lecture, et les arguments et citations de chaque côté.
5. Ce que tu n'as pas pu vérifier, et pourquoi.
6. Décompte des verdicts.
B. Tes verdicts qui portent une citation exacte, ajoutés à la fin de working-folder/controle-sources/verifications/registre-verifications.yaml, au format décrit dans AGENTS.md (agent: codex). Tu ajoutes ; tu ne modifies ni ne supprimes rien.

Tu ne modifies aucun autre fichier : ni l'annexe (HTML ou Markdown), ni les fiches, ni les registres, ni les paramètres. Aucune suppression, aucun commit. N'emploie jamais le tiret long.

LOT À VÉRIFIER : [remplacer par une ligne du tableau des lots]
```

## Les cinq lots

Pour chaque lot : les sections indiquées de `index.html` et toutes les fiches vers lesquelles elles renvoient.

| Lot | Ligne à coller à la fin du message |
|---|---|
| 1 | `Lot 1 : section 8.1 (tonnages, taux de recyclage, devenir, exportations, contribution européenne), et toutes les fiches vers lesquelles elle renvoie. Refais les calculs CALC-A8-EXPORT-3915-T et CALC-A8-EMB-RECY-HORS-FRANCE à partir des requêtes Eurostat indiquées.` |
| 2 | `Lot 2 : section 8.2 (coûts d'élimination, tendance, TGAP 2026 dans le CIBS, CSR, capacité francilienne) et section 8.6 (prix d'entrée par défaut), et toutes les fiches vers lesquelles elles renvoient. Refais CALC-A8-INCIN-IDF-HAUSSE-2024-2026. Pour la TGAP, lis le texte de la loi n° 2026-103 (JORF du 20/02/2026), articles L. 433-57, L. 433-86 et L. 433-90 du CIBS.` |
| 3 | `Lot 3 : sections 8.3.1 à 8.3.5 (emballages ménagers, films et flux développement, refus de tri, polystyrène, PSE, y compris le paragraphe sur la compréhension du porteur), et toutes les fiches vers lesquelles elles renvoient. Refais CALC-A8-FILMS-REPRIS-T, CALC-A8-PRIXNUL-T, CALC-A8-PRIXNUL-PART, CALC-A8-REFUS-PART-PLASTIQUE et CALC-A8-PS-PART-TRIE.` |
| 4 | `Lot 4 : sections 8.3.6 à 8.3.14 (emballages professionnels, agricoles, chutes, DEEE, VHU, bâtiment et PVC, textiles, ameublement, OMR), et toutes les fiches vers lesquelles elles renvoient. Refais CALC-A8-TEXTILES-CSR-T. Vérifie que les plastiques triés et les résidus de broyage sont bien distingués.` |
| 5 | `Lot 5 : lecture d'ensemble : « How to Read This Annex », « Key Messages », sections 8.4 (aptitude à l'Urban Rig), 8.5 (concurrence), 8.7 et 8.8, cohérence des étiquettes et des taux de confiance. Lis aussi les rapports des lots 1 à 4 dans working-folder/controle-sources/verifications/. Pour ce lot, la partie « Autres interprétations » est l'essentiel.` |

Ordre conseillé : lots 1 à 4, puis le lot 5, qui juge les conclusions à la lumière des quatre premiers.

## Étape 3 : message à coller dans un nouveau chat Claude (projet « business plan »)

```text
Chat de traitement des écarts de l'annexe 8, après contre-vérification par ChatGPT (Codex).

Lis d'abord REGLES-DE-RIGUEUR.md, CLAUDE.md, working-folder/METHODE-DE-TRAVAIL.md et nouveau-business-plan/AVANCEMENT.md, puis les rapports de vérification dans working-folder/controle-sources/verifications/ (fichiers *-codex-annexe-08-lot-*.md).

Pour chaque écart (E-x) et chaque « autre interprétation » :
1. Rouvre toi-même le document d'origine à l'emplacement cité, sans te fier ni à l'annexe ni au rapport.
2. Classe le point dans working-folder/controle-sources/verifications/ecarts-annexe-08.md (tableau : n° | lot | section ou fiche | constat du vérificateur | ta relecture avec citation exacte | statut | décision de Stéphane) :
   - ACCEPTÉ : le vérificateur a raison ; tu corriges la source (ANNEX-08-Plastic-Waste-Streams.md ou les registres), tu régénères le HTML ;
   - CONTESTÉ : tu maintiens l'annexe, avec la citation qui contredit le vérificateur ; jamais sans citation ;
   - À TRANCHER : la question relève d'un choix ou d'une interprétation ; c'est moi qui décide.
3. Vérifie que les verdicts ajoutés par le vérificateur dans working-folder/controle-sources/verifications/registre-verifications.yaml portent bien une citation exacte ; signale-moi ceux qui n'en ont pas, sans les modifier.
Ne modifie rien pour un point CONTESTÉ ou À TRANCHER sans mon accord. À la fin : contrôle à zéro erreur, HTML à jour, AVANCEMENT mis à jour, et la liste des points À TRANCHER, avec pour chacun les deux positions en deux lignes.
Aucune suppression de fichier, aucun commit, jamais de tiret long.
```

## Étape 4 (facultative) : second tour avec le vérificateur

Dans une nouvelle conversation Codex, coller :

```text
Second tour de vérification de l'annexe 8. Lis working-folder/controle-sources/verifications/ecarts-annexe-08.md : ce sont les réponses de l'auteur à tes écarts. Pour chaque ligne CONTESTÉ, rouvre la source d'origine et maintiens ou retire ton objection, avec une citation exacte. Ne cède pas sur un point simplement parce qu'il est contesté ; ne maintiens pas un point sans citation. Écris ta réponse dans working-folder/controle-sources/verifications/2026-10-JJ-codex-annexe-08-second-tour.md, et rien d'autre.
```

Stéphane tranche ensuite les points restants. Ses décisions sont notées dans `ecarts-annexe-08.md` et, si elles touchent la méthode, dans `working-folder/params/_decisions.yaml`.
