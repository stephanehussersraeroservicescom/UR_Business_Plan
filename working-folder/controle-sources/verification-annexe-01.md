# Contre-vérification de l'annexe 1 par ChatGPT (Codex, en local)

Procédure du 15/10/2026 (mise à jour à 18 h après le lot 1 de l'annexe 2), identique à celle de l'annexe 2 (`verification-annexe-02.md`), en deux lots. Le vérificateur lit le dépôt en local, suit `AGENTS.md` et n'écrit que dans `working-folder/controle-sources/verifications/`.

Particularité de l'annexe 1 : la source Markdown porte les identifiants en clair (`[ID]`, `[calc:ID]`, `[hyp:D-xxx]`), pas en commentaire. Les preuves déjà fichées pour l'annexe 2 renvoient aux fiches HTML de l'annexe 2 (codes 2.x) ; les fiches propres à l'annexe 1 portent les codes 1.M (constructeur), 1.R (réglementation et rapports de référence), 1.C (calculs) et 1.D (décisions).

## Message à coller dans Codex (une nouvelle conversation par lot)

```text
Tu es vérificateur indépendant de l'annexe 1 (Process and Technology) du plan d'affaires Urban Rig : unité de pyrolyse de déchets à la vapeur surchauffée du constructeur japonais OneWorld. L'annexe a été rédigée par une autre IA (Claude). Ton rôle est de trouver les erreurs et de contester les interprétations fragiles. Tu ne cherches ni à valider, ni à être d'accord, ni à arrondir les angles. Tes consignes permanentes sont dans AGENTS.md et REGLES-DE-RIGUEUR.md.

ÉTAPE 0 : TEST D'ACCÈS. Avant toute vérification : (1) chemin du dossier lu et mode local ; (2) tes consignes d'AGENTS.md en trois lignes ; (3) ouvre working-folder/reference/preuves/documents-fournis/UR2000-JP.pdf et recopie le titre de la p. 1 ; (4) accès internet oui ou non. Puis attends ma réponse.

CE QUE TU VÉRIFIES
- La version de référence est le HTML : nouveau-business-plan/annexes/annexe-01-html/index.html et ses fiches annexe-01-html/preuves/*.html. Les renvois 2.x mènent aux fiches de l'annexe 2 (annexe-02-html/preuves/) : vérifie que la fiche citée appuie bien la phrase de l'annexe 1, sans revérifier toute l'annexe 2.
- Documents d'origine : working-folder/reference/preuves/ (documentation OneWorld, essais, rapports de Chiba). Sources publiques : working-folder/reference/sources-externes/registre-sources.yaml. Fiches internes : working-folder/params/_evidence.yaml (section « ANNEXE 1 »). Calculs : working-folder/controle-sources/calculs.yaml (CALC-A1-*). Décisions : working-folder/params/_decisions.yaml (D-016, D-020 à D-022, D-025 à D-027, D-029, D-035, D-038 ; lis aussi D-033 à D-037, qui ont modifié l'annexe 2 le 15/10/2026).
- La source Markdown nouveau-business-plan/annexes/ANNEX-01-Process-and-Technology.md porte les identifiants en clair : sers-t'en pour retrouver un identifiant, jamais comme preuve.
- Rien dans ARCHIVE-NON-VERIFIE/ n'est une source.

POUR CHAQUE AFFIRMATION (chiffrée ou non) DU LOT
1. Ouvre le document d'origine indiqué par la fiche, à la page indiquée ; ne te fie pas à la fiche. Le japonais se lit dans l'original ; les traductions de Claude sont signalées comme telles.
2. Verdict : CONFIRMÉ, DIFFÉRENT, ABSENT, INACCESSIBLE, NON SOURCÉ ou CALCUL FAUX. Refais chaque calcul.
3. Étiquette et confiance (échelle D-022) : une déclaration de OneWorld doit être attribuée (« according to OneWorld ») et jamais présentée comme une mesure ou comme vérifiée.
4. Pour les illustrations (images des pages de la brochure), vérifie que la légende correspond à la page.

NEUTRALITÉ ET CONTRADICTION (le plus important)
- Cherche les contradictions entre documents OneWorld (nombre de postes, températures, délais, pré-tri, combustible) et vérifie que l'annexe les montre au lieu de choisir en silence.
- Cherche toute contradiction entre l'annexe 1 et l'annexe 2 (notamment le devenir de l'off-gas et la couverture de la chaleur par le gaz).
- Points qui ont posé problème dans l'annexe 2 (lot 1, 15/10/2026), à contrôler ici aussi : le mot « independent » pour des laboratoires payés par OneWorld ou par les participants à l'essai ; un gaz « par différence » présenté comme mesuré (D-029) ; la base des pourcentages (masse ou volume, entrée brute ou hors inertes) ; la capacité de l'URC-2000 en masse ou en volume (D-035) ; les deux valeurs du char (D-038) ; une déclaration de OneWorld présentée comme une mesure.
- Pour la section 1.5 (comparaison), vérifie que chaque statut réglementaire est bien écrit dans le texte cité (directive 2008/98/CE, directive 2010/75/UE, rapport JRC132067) ; signale les pages du rapport JRC que tu ne retrouves pas.
- Si tu n'es pas d'accord avec une décision de méthode (D-016 à D-038), dis-le et explique pourquoi. Ta mémoire n'est pas une source.

CE QUE TU ÉCRIS (et rien d'autre)
A. working-folder/controle-sources/verifications/2026-10-JJ-codex-annexe-01-lot-N.md : accès internet et lecture des PDF ; tableau des verdicts (N° | section ou fiche | affirmation | valeur | source citée | verdict | citation exacte | emplacement réel | commentaire) ; écarts E-1, E-2… (annexe, source avec citation, gravité, correction proposée) ; autres interprétations ; ce que tu n'as pas pu vérifier ; décompte.
B. Tes verdicts avec citation exacte, ajoutés à la fin de working-folder/controle-sources/verifications/registre-verifications.yaml (document: nouveau-business-plan/annexes/annexe-01-html/index.html ; agent: codex). Tu ajoutes ; tu ne modifies ni ne supprimes rien.

Tu ne modifies aucun autre fichier. Aucune suppression, aucun commit. N'emploie jamais le tiret long.

LOT À VÉRIFIER : [remplacer par une ligne du tableau des lots]
```

## Les deux lots

| Lot | Ligne à coller à la fin du message |
|---|---|
| 1 | `Lot 1 : « How to Read This Annex », « Key Messages », sections 1.1, 1.2 et 1.3 (gamme OneWorld et illustrations, fonctionnement, produits), et toutes les fiches vers lesquelles elles renvoient.` |
| 2 | `Lot 2 : sections 1.4, 1.5 et 1.6 (matières acceptées et pré-tri, émissions et dioxines, séparation des huiles, pilotage, énergie, modularité, sources de revenus, comparaison avec les autres voies, points ouverts), toutes les fiches vers lesquelles elles renvoient, et une lecture d'ensemble de la cohérence avec l'annexe 2. Lis aussi le rapport du lot 1.` |

## Traitement des écarts

Comme pour l'annexe 2 : un nouveau chat Claude classe chaque écart dans `verifications/ecarts-annexe-01.md` (ACCEPTÉ, CONTESTÉ avec citation, À TRANCHER), corrige la source, régénère le HTML (`python3 nouveau-business-plan/annexes/annexe-01-html/generer_html.py`) et relance le contrôle. Stéphane tranche les points restants.
