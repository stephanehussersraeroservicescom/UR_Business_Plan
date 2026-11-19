# Contre-vérification de l'annexe 5 par ChatGPT (Codex, en local)

Procédure du 19/11/2026, adaptée de `verification-annexe-08.md`. Le vérificateur est ChatGPT dans son mode Codex, projet « vérification Urban Rig », relié au dossier local du dépôt. Il lit les fichiers directement sur l'ordinateur et suit `AGENTS.md`. Il n'écrit que dans `working-folder/controle-sources/verifications/`.

## La procédure

| Étape | Qui | Quoi |
|---|---|---|
| 1 | ChatGPT (Codex) | Test d'accès : dossier lu, consignes d'`AGENTS.md`, lecture d'un PDF, accès internet |
| 2 | ChatGPT (Codex) | Vérification d'un lot (une nouvelle conversation par lot, trois lots). Il écrit son rapport dans `verifications/` et ses verdicts dans `verifications/registre-verifications.yaml` |
| 3 | Claude (nouveau chat) | Relire chaque écart dans la source d'origine et le classer : ACCEPTÉ (corrigé), CONTESTÉ (avec citation), À TRANCHER. Fichier `verifications/ecarts-annexe-05.md` |
| 4 | ChatGPT (Codex) | Facultatif : second tour sur les points CONTESTÉS |
| 5 | Stéphane | Trancher les points restants ; commiter et pousser |

## Points d'attention propres à l'annexe 5

- **Données ouvertes de l'ADEME.** `data.ademe.fr` refuse souvent les robots. Les trois jeux lus le 19/11/2026 sont copiés dans `working-folder/reference/sources-externes/pdf/` (fichiers `ADEME-MODECOM-2024-*-2026-11-19.csv`). Le vérificateur peut lire ces copies, mais doit dire s'il a pu ouvrir la version en ligne ; une copie locale n'est pas une seconde source.
- **Articles scientifiques sur PMC** (`pmc.ncbi.nlm.nih.gov`) : vérification de navigateur fréquente. Essayer le DOI chez l'éditeur.
- **Hypothèses D-043 à D-046** : posées par Claude, pas encore tranchées par Stéphane. Le vérificateur les juge (fondées, fragiles, à remplacer), il ne les traite pas comme des faits.

## Message à coller dans Codex (une nouvelle conversation par lot)

```text
Tu es vérificateur indépendant de l'annexe 5 (Municipal Solid Waste, ordures ménagères résiduelles en France) du plan d'affaires Urban Rig : unité de pyrolyse de déchets du constructeur japonais OneWorld, porteur du plan. L'annexe a été rédigée par une autre IA (Claude). Ton rôle est de trouver les erreurs et de contester les interprétations fragiles. Tu ne cherches ni à valider, ni à être d'accord. Tes consignes permanentes sont dans AGENTS.md et REGLES-DE-RIGUEUR.md.

ÉTAPE 0 : TEST D'ACCÈS. Réponds à ces quatre points avant toute vérification, puis attends ma réponse.
1. Quel est le chemin du dossier que tu lis ? Es-tu en mode local ?
2. Résume en trois lignes tes consignes d'AGENTS.md.
3. Ouvre https://data.ademe.fr/datasets/omrhum et recopie la ligne « Moyenne ». Si tu ne peux pas, dis avec quel outil tu as essayé.
4. As-tu accès à internet dans cette session ? Peux-tu lire un PDF en ligne ?

CE QUE TU VÉRIFIES
- La version de référence est le HTML : nouveau-business-plan/annexes/annexe-05-html/index.html et ses fiches annexe-05-html/preuves/*.html (fiches 5.P, 5.L, 5.C et 5.D). Les fiches 1.x, 2.x, 3.x et 8.x renvoient à d'autres annexes, soumises à leur propre vérification : vérifie seulement que la valeur reprise est la même.
- Registres : working-folder/reference/sources-externes/registre-sources.yaml (fiches A5-* ; fiches ADEME-MODECOM-2024-DATA, ADEME-MODECOM-2024-HUM, RP2-002, RP2-004 et ORDIF-DMA-2022, dont la relecture est dans le champ relecture_a5_2026_11_19), working-folder/controle-sources/calculs.yaml (CALC-A5-*), working-folder/params/_decisions.yaml (D-043 à D-046, et D-029, D-034, D-038, D-039, D-042 citées).
- La source Markdown nouveau-business-plan/annexes/ANNEX-05-Municipal-Solid-Waste.md porte les identifiants entre crochets : sers-t'en pour retrouver un identifiant, jamais comme preuve.
- Rien dans ARCHIVE-NON-VERIFIE/ n'est une source. Ignore _to_delete/.

POUR CHAQUE AFFIRMATION CHIFFRÉE DU LOT
1. Ouvre le document d'origine indiqué par la fiche, à l'emplacement indiqué. Ne te fie pas à la fiche.
2. Donne un verdict : CONFIRMÉ, DIFFÉRENT, ABSENT, INACCESSIBLE, NON SOURCÉ ou CALCUL FAUX. Refais chaque calcul toi-même.
3. Vérifie l'étiquette et le taux de confiance. Sont des erreurs : une donnée de OneWorld présentée comme une mesure ; une source secondaire ou ancienne non signalée ; une hypothèse présentée comme un fait.
4. Vérifie le périmètre : France ou Île-de-France, année, base humide ou sèche, PCI ou PCS, conditions de pyrolyse (température, échelle, catalyseur).

NEUTRALITÉ ET CONTRADICTION (le plus important)
- Pour chaque conclusion du lot, cherche activement une autre lecture des mêmes données. Dis laquelle te paraît la plus solide, avec la citation qui l'appuie.
- Signale : des rendements de laboratoire appliqués sans réserve à l'Urban Rig ; une base humide confondue avec une base sèche ; des fines comptées deux fois ou oubliées ; une source plus récente ou plus solide que celle citée (en particulier pour la composition d'une couche, les rendements de pyrolyse des déchets alimentaires et du papier, et la composition par polymère des plastiques des OMR).
- Si tu n'es pas d'accord avec une hypothèse D-043 à D-046, dis-le et explique pourquoi.
- Ta mémoire d'entraînement n'est pas une source.

CE QUE TU ÉCRIS (et rien d'autre)
A. Ton rapport, dans working-folder/controle-sources/verifications/AAAA-MM-JJ-codex-annexe-05-lot-N.md : accès internet et lecture des PDF ; tableau des verdicts (N° | section ou fiche | affirmation | valeur annoncée | source citée | verdict | citation exacte relevée | emplacement réel | commentaire) ; écarts E-1, E-2... (ce que dit l'annexe, ce que dit la source, gravité, correction proposée) ; autres interprétations ; ce que tu n'as pas pu vérifier ; décompte des verdicts.
B. Tes verdicts qui portent une citation exacte, ajoutés à la fin de working-folder/controle-sources/verifications/registre-verifications.yaml, au format décrit dans AGENTS.md (agent: codex). Tu ajoutes ; tu ne modifies ni ne supprimes rien.

Tu ne modifies aucun autre fichier. Aucune suppression, aucun commit. N'emploie jamais le tiret long.

LOT À VÉRIFIER : [remplacer par une ligne du tableau des lots]
```

## Les trois lots

| Lot | Ligne à coller à la fin du message |
|---|---|
| 1 | `Lot 1 : partie 1, sections 5.1 à 5.4 (tonnages, composition par catégorie, humidité et PCI, matières non convertibles). Refais les calculs CALC-A5-CAT01-T à CALC-A5-CAT13-PCT, CALC-A5-OMR-T et CALC-A5-NONPROC-* à partir du jeu omrcs-compo-jdd. Vérifie le traitement des fines (D-046).` |
| 2 | `Lot 2 : sections 5.5 à 5.8 (textiles sanitaires et couches, textiles, composites, plastiques, PVC, bilan d'une tonne). Refais CALC-A5-EAU-KG-T, CALC-A5-SEC-*, CALC-A5-PLAST-*, CALC-A5-COUCHE-POLYMERES-PCT et CALC-A5-PVC-CL-*. Cherche une composition de couche plus récente que 2006.` |
| 3 | `Lot 3 : partie 2, sections 5.9 à 5.17 et les Key Messages (essais Urban Rig, littérature, bilan indicatif, énergie, prix d'entrée, conflits, recommandations). Refais les calculs CALC-A5-HUILE-*, CALC-A5-GAZ-*, CALC-A5-CHAR-*, CALC-A5-LATENT-MJ-KG, CALC-A5-EAU-MJ-T, CALC-A5-COUV-* et CALC-A5-KHAN-PCS-MJ-KG. Juge les hypothèses D-043 à D-045. Pour ce lot, la partie « Autres interprétations » est l'essentiel.` |

## Étape 3 : message à coller dans un nouveau chat Claude (projet « business plan »)

```text
Chat de traitement des écarts de l'annexe 5, après contre-vérification par ChatGPT (Codex).

Lis d'abord REGLES-DE-RIGUEUR.md, CLAUDE.md, working-folder/METHODE-DE-TRAVAIL.md et nouveau-business-plan/AVANCEMENT.md, puis les rapports dans working-folder/controle-sources/verifications/ (fichiers *-codex-annexe-05-lot-*.md).

Pour chaque écart (E-x) et chaque « autre interprétation » :
1. Rouvre toi-même le document d'origine à l'emplacement cité.
2. Classe le point dans working-folder/controle-sources/verifications/ecarts-annexe-05.md : ACCEPTÉ (tu corriges la source et régénères le HTML), CONTESTÉ (avec la citation qui contredit le vérificateur), À TRANCHER (c'est moi qui décide).
3. Vérifie que les verdicts ajoutés dans registre-verifications.yaml portent une citation exacte ; signale ceux qui n'en ont pas, sans les modifier.
À la fin : contrôle à zéro erreur, HTML à jour, AVANCEMENT mis à jour, et la liste des points À TRANCHER. Aucune suppression de fichier, aucun commit, jamais de tiret long.
```
