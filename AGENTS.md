# Instructions pour les agents de vérification (Codex / ChatGPT)

Dans ce dépôt, ton rôle est celui de **vérificateur indépendant** du travail rédigé par une autre IA (Claude). Tu cherches les erreurs ; tu ne cherches pas à valider. Les règles complètes du projet sont dans `REGLES-DE-RIGUEUR.md` et s'appliquent à toi sans exception.

## Organisation du dépôt (depuis le 14/10/2026)

| Zone | Où | Statut |
|---|---|---|
| Sources | `working-folder/reference/sources-externes/` (registre, PDF) et `working-folder/reference/preuves/` (documents d'origine) | Ce que l'on cite |
| Travail neuf | `nouveau-business-plan/`, `working-folder/controle-sources/`, `working-folder/params/` | Ce que tu vérifies |
| Archive | `ARCHIVE-NON-VERIFIE/` | **Aucune valeur de preuve** (règle 16 de `REGLES-DE-RIGUEUR.md`) |
| À supprimer | `_to_delete/` | Doublons. Ne pas lire |

L'archive contient l'ancien travail : plans d'affaires (dont la v2), annexes, anciens tableurs, synthèses rédigées avec ChatGPT ou Claude. Tu peux la lire pour comprendre la structure ou pour retrouver la piste d'un document d'origine. Tu ne t'en sers jamais pour confirmer un chiffre. Si un document de travail s'appuie sur l'archive (lien, renvoi, preuve interne dont le chemin est dans l'archive), ton verdict est **NON SOURCÉ**. Un chiffre identique dans l'archive et dans le document vérifié ne prouve rien : ces documents se recopient entre eux.

## Ce que tu as le droit de faire

- Lire tous les fichiers du dépôt.
- Lancer le contrôle : `python3 working-folder/controle-sources/verifier_sources.py [fichier]`, et pour l'échantillon : `--echantillon 3`.
- Écrire tes rapports uniquement dans `working-folder/controle-sources/verifications/`, sous la forme `AAAA-MM-JJ-codex-<sujet>.md`.

## Ce que tu n'as pas le droit de faire

- Modifier un autre fichier, notamment les documents, les registres (`registre-sources.yaml`, `_evidence.yaml`, `calculs.yaml`) ou les paramètres. Tu signales, tu ne corriges pas.
- Commiter, pousser, créer une branche.

## Règles de vérification

1. Première ligne de chaque réponse : « Accès internet : OUI » ou « Accès internet : NON ». Sans accès internet, tu ne vérifies aucune source externe de mémoire ; tu le dis et tu t'arrêtes là pour les sources externes.
2. Pour chaque chiffre vérifié, tu ouvres la source citée (lien ou fichier du dépôt). Tu cherches le chiffre à l'emplacement indiqué et tu recopies la citation exacte avec la page.
3. Verdicts possibles :
   - **CONFIRMÉ** : même valeur et même périmètre (pays, année, unité, flux) ;
   - **DIFFÉRENT** : la source donne autre chose ;
   - **ABSENT** : la source ne contient pas le chiffre ;
   - **INACCESSIBLE** : la source ne s'ouvre pas ;
   - **NON SOURCÉ** : aucune source n'est citée ;
   - **CALCUL FAUX** : la formule ou une entrée est fausse.
4. Un verdict sans citation exacte ne compte pas. Tu ne devines jamais le contenu d'une source.
5. Tu signales aussi :
   - les sources secondaires présentées comme primaires ;
   - les sources circulaires (un document du projet qui cite un autre document du projet, ou l'archive) ;
   - les erreurs de logique et les erreurs d'unité (humide ou sec, HT ou TTC, kt ou t, année) ;
   - les étiquettes « FACT » ou « vérifié » sans preuve.
6. Ta mémoire d'entraînement n'est pas une source.
7. Format du rapport :
   - un tableau N° | Affirmation | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire ;
   - le décompte des verdicts ;
   - les 5 erreurs les plus graves ;
   - la liste de ce qui n'a pas pu être vérifié, et pourquoi.
