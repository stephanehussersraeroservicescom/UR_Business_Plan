# Contre-vérification de l'annexe 3 par ChatGPT (Codex, en local)

Procédure du 15/10/2026, adaptée de `verification-annexe-02.md`. Le vérificateur est ChatGPT dans son mode Codex, projet « vérification Urban Rig », relié au dossier local du dépôt. Il lit les fichiers directement sur l'ordinateur et suit `AGENTS.md`. Il n'écrit que dans `working-folder/controle-sources/verifications/`.

## La procédure en cinq étapes

| Étape | Qui | Quoi |
|---|---|---|
| 1 | ChatGPT (Codex) | Test d'accès : dossier lu, consignes d'`AGENTS.md`, lecture d'un PDF, accès internet |
| 2 | ChatGPT (Codex) | Vérification d'un lot (une nouvelle conversation par lot, cinq lots). La plupart des sources de l'annexe 3 sont publiques : l'accès internet est nécessaire. Il écrit lui-même son rapport dans `verifications/` et ses verdicts dans `verifications/registre-verifications.yaml` |
| 3 | Claude (nouveau chat) | Relire chaque écart dans la source d'origine et le classer : ACCEPTÉ (corrigé), CONTESTÉ (avec citation), À TRANCHER. Fichier `verifications/ecarts-annexe-03.md` |
| 4 | ChatGPT (Codex) | Facultatif : second tour sur les points CONTESTÉS |
| 5 | Stéphane | Trancher les points restants ; commiter et pousser |

L'annexe 3 passe « contre-vérifiée » dans `AVANCEMENT.md` quand les cinq lots sont traités et que chaque écart a un statut final.

## Points d'attention

- **Mode local, pas worktree**, et **une nouvelle conversation par lot** : Codex relit `AGENTS.md` au début de chaque session, et les consignes ne se diluent pas.
- **Sources publiques** (presque toutes : statistiques, textes réglementaires, rapports) : si Codex n'a pas accès à internet, il les marque INACCESSIBLE. On les fait alors vérifier par ChatGPT avec la recherche web, à partir de `prompts-verification-externe.md` (prompt 2).
- **Autorisations.** Si Codex demande l'autorisation d'écrire, acceptez seulement pour son rapport et pour `registre-verifications.yaml`, tous deux dans `working-folder/controle-sources/verifications/`. Refusez toute modification ailleurs.
- **Aucun besoin de pousser sur GitHub avant** : Codex lit le dossier local. On commite après, pour garder ses rapports.

## Message à coller dans Codex (une nouvelle conversation par lot)

Remplacer la dernière ligne par l'un des lots du tableau qui suit le message.

```text
Tu es vérificateur indépendant de l'annexe 3 (Output Markets and Pricing) du plan d'affaires Urban Rig : unité de pyrolyse de déchets du constructeur japonais OneWorld, porteur du plan. L'annexe a été rédigée par une autre IA (Claude) à partir de recherches faites en partie par des sous-agents. Ton rôle est de trouver les erreurs et de contester les interprétations fragiles. Tu ne cherches ni à valider, ni à être d'accord, ni à arrondir les angles. Tes consignes permanentes sont dans AGENTS.md et REGLES-DE-RIGUEUR.md. Applique aussi working-folder/controle-sources/regles-verification-legere.md (vérification légère, cas standard) : en cas de conflit avec les consignes ci-dessous, ces règles priment.

ÉTAPE 0 : TEST D'ACCÈS. Réponds à ces quatre points avant toute vérification, puis attends ma réponse.
1. Quel est le chemin du dossier que tu lis ? Es-tu en mode local ?
2. Résume en trois lignes tes consignes d'AGENTS.md : quel fichier tu vérifies, où tu as le droit d'écrire, ce que tu ne dois jamais faire.
3. Ouvre https://www.insee.fr/fr/statistiques/2015775 et recopie le titre du tableau. Si tu ne peux pas, dis avec quel outil tu as essayé.
4. As-tu accès à internet dans cette session ? Peux-tu lire un PDF en ligne ?

CE QUE TU VÉRIFIES
- La version de référence est le HTML : nouveau-business-plan/annexes/annexe-03-html/index.html et ses fiches annexe-03-html/preuves/*.html (fiches 3.M, 3.R, 3.P, 3.L, 3.C et 3.D). Les fiches 1.x et 2.x renvoient aux annexes 1 et 2, déjà soumises à leur propre vérification : vérifie seulement que la valeur reprise est la même.
- Chaque fiche de source donne le lien, l'emplacement, la citation et les valeurs relevées ; chaque fiche de calcul donne la formule, les entrées et le résultat. Les registres sont working-folder/reference/sources-externes/registre-sources.yaml (fiches A3-, A3F-, A3G-, A3H-, A3I-, A3J-), working-folder/params/_evidence.yaml, working-folder/controle-sources/calculs.yaml (calculs CALC-A3-*) et working-folder/params/_decisions.yaml (D-027 à D-032).
- Les valeurs unitaires Eurostat Comext (fiches A3F-COMEXT-*, A3G-COMEXT-*, A3H-COMEXT-*) sont des calculs : valeur en euros divisée par la quantité. Refais la requête indiquée dans la fiche et le calcul.
- Les prix sont des valeurs par défaut que l'opérateur du modèle peut changer (décision D-030) : vérifie que chaque valeur est bien la plus récente publiée par la source citée à la date de lecture (15/10/2026), et signale une valeur plus récente si tu en trouves une.
- La source Markdown nouveau-business-plan/annexes/ANNEX-03-Output-Markets-and-Pricing.md porte les identifiants entre crochets : sers-t'en pour retrouver un identifiant, jamais comme preuve.
- Rien dans ARCHIVE-NON-VERIFIE/ n'est une source. Ignore _to_delete/ s'il existe.

POUR CHAQUE AFFIRMATION CHIFFRÉE DU LOT
1. Ouvre le document d'origine indiqué par la fiche, à l'emplacement indiqué. Ne te fie pas à la fiche : elle peut être fausse. Pour un texte de loi, lis la version en vigueur (Légifrance, EUR-Lex) et signale si la fiche s'appuie sur une reproduction.
2. Donne un verdict : CONFIRMÉ, DIFFÉRENT, ABSENT, INACCESSIBLE, NON SOURCÉ ou CALCUL FAUX. Refais chaque calcul toi-même.
3. Vérifie l'étiquette et le taux de confiance (échelle de l'index des fiches de l'annexe 3). Sont des erreurs : une donnée de OneWorld présentée comme une mesure ou une vérification ; une source commerciale ou secondaire non signalée ; une proposition de texte présentée comme adoptée.
4. Vérifie le périmètre : même produit et même qualité, même pays, même base (hors taxes ou TTC, départ ou livré, à la frontière), même devise, même période, même unité (PCI ou PCS, litre ou tonne).

NEUTRALITÉ ET CONTRADICTION (le plus important)
- Ne suppose ni que l'annexe a raison, ni qu'elle a tort : lis la source.
- Pour chaque conclusion du lot, cherche activement une autre lecture des mêmes données. Dis laquelle te paraît la plus solide, avec la citation qui l'appuie.
- Signale : un prix de référence appliqué à un produit qui n'en a pas la qualité (huile hors spécification, char au chlore inconnu, métaux non analysés) ; les prix de crise présentés comme normaux ; les comparaisons PCS contre PCI ; les sources commerciales ou secondaires utilisées comme principales ; une lecture juridique trop favorable (sortie du statut de déchet, hydrogène, carbone) ; ce qui est omis et affaiblirait la conclusion.
- Si tu n'es pas d'accord avec une décision de méthode du projet (D-016 à D-032), dis-le et explique pourquoi.
- Ta mémoire d'entraînement n'est pas une source. Pour une norme ou un texte réglementaire, ouvre le texte ; sans accès internet, marque-le INACCESSIBLE.

CE QUE TU ÉCRIS (et rien d'autre)
A. Ton rapport, dans working-folder/controle-sources/verifications/2026-10-JJ-codex-annexe-03-lot-N.md (date du jour, numéro du lot) :
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
| 1 | `Lot 1 : section 3.1 (huile : fractions, spécifications comparées aux mesures, statut réglementaire, prix de référence par fraction, sensibilité au Brent, acheteurs), et toutes les fiches vers lesquelles elle renvoie. Refais les calculs CALC-A3-GAZOLE-EUR-T à CALC-A3-HUILE-MOY-BRENT50.` |
| 2 | `Lot 2 : section 3.2 (char : caractéristiques, débouchés en cimenterie, critères d'acceptation, statut, prix à parité énergétique et pratique du marché des CSR, élimination), et toutes les fiches vers lesquelles elle renvoie.` |
| 3 | `Lot 3 : sections 3.3 et 3.4 (métaux, verre et inertes ; gaz excédentaire et hydrogène : quantités, statut, prix, purification), et toutes les fiches vers lesquelles elles renvoient. Refais les calculs CALC-A3-H2-* et CALC-A3-GAZ-*.` |
| 4 | `Lot 4 : sections 3.5 et 3.6 (carbone : lecture des textes et calcul du CO2 évité ; énergie achetée : électricité et combustible), et toutes les fiches vers lesquelles elles renvoient. Pour la section 3.5.1, lis chaque texte cité en version primaire et dis si un crédit carbone est possible, impossible ou possible sous conditions.` |
| 5 | `Lot 5 : lecture d'ensemble : « How to Read This Annex », « Key Messages », sections 3.7, 3.8 et 3.9, cohérence des étiquettes et des taux de confiance, toutes les phrases « OneWorld design data ». Lis aussi les rapports des lots 1 à 4 dans working-folder/controle-sources/verifications/. Pour ce lot, la partie « Autres interprétations » est l'essentiel.` |

Ordre conseillé : lots 1 à 4, puis le lot 5, qui juge les conclusions à la lumière des quatre premiers.

## Étape 3 : message à coller dans un nouveau chat Claude (projet « business plan »)

```text
Chat de traitement des écarts de l'annexe 3, après contre-vérification par ChatGPT (Codex).

Lis d'abord REGLES-DE-RIGUEUR.md, CLAUDE.md, working-folder/METHODE-DE-TRAVAIL.md et nouveau-business-plan/AVANCEMENT.md, puis les rapports de vérification dans working-folder/controle-sources/verifications/ (fichiers *-codex-annexe-03-lot-*.md).

Pour chaque écart (E-x) et chaque « autre interprétation » :
1. Rouvre toi-même le document d'origine à l'emplacement cité, sans te fier ni à l'annexe ni au rapport.
2. Classe le point dans working-folder/controle-sources/verifications/ecarts-annexe-03.md (tableau : n° | lot | section ou fiche | constat du vérificateur | ta relecture avec citation exacte | statut | décision de Stéphane) :
   - ACCEPTÉ : le vérificateur a raison ; tu corriges la source (ANNEX-03-Output-Markets-and-Pricing.md ou les registres), tu régénères le HTML ;
   - CONTESTÉ : tu maintiens l'annexe, avec la citation qui contredit le vérificateur ; jamais sans citation ;
   - À TRANCHER : la question relève d'un choix ou d'une interprétation ; c'est moi qui décide.
3. Vérifie que les verdicts ajoutés par le vérificateur dans working-folder/controle-sources/verifications/registre-verifications.yaml portent bien une citation exacte ; signale-moi ceux qui n'en ont pas, sans les modifier.
Ne modifie rien pour un point CONTESTÉ ou À TRANCHER sans mon accord. À la fin : contrôle à zéro erreur, HTML à jour, AVANCEMENT mis à jour, et la liste des points À TRANCHER, avec pour chacun les deux positions en deux lignes.
Aucune suppression de fichier, aucun commit, jamais de tiret long.
```

## Étape 4 (facultative) : second tour avec le vérificateur

Dans une nouvelle conversation Codex, coller :

```text
Second tour de vérification de l'annexe 3. Lis working-folder/controle-sources/verifications/ecarts-annexe-03.md : ce sont les réponses de l'auteur à tes écarts. Pour chaque ligne CONTESTÉ, rouvre la source d'origine et maintiens ou retire ton objection, avec une citation exacte. Ne cède pas sur un point simplement parce qu'il est contesté ; ne maintiens pas un point sans citation. Écris ta réponse dans working-folder/controle-sources/verifications/2026-10-JJ-codex-annexe-03-second-tour.md, et rien d'autre.
```

Stéphane tranche ensuite les points restants. Ses décisions sont notées dans `ecarts-annexe-03.md` et, si elles touchent la méthode, dans `working-folder/params/_decisions.yaml`.
