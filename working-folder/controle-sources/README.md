# Contrôle des sources

Règle de base du projet : **tout chiffre d'un livrable renvoie à une source du registre. Ce qui n'est pas lu tel quel dans une source est un calcul enregistré, dont toutes les entrées sont sourcées.** Une hypothèse sans source reste possible, mais elle doit être documentée dans `params/_decisions.yaml` et citée comme telle.

Le script `verifier_sources.py` applique cette règle automatiquement. Il ne juge pas si une source dit vrai ; il vérifie que chaque chiffre est rattaché à quelque chose de contrôlable, et que les calculs donnent bien le résultat annoncé.

## Lancer le contrôle

Depuis la racine du dépôt :

```
python3 working-folder/controle-sources/verifier_sources.py              # documents de cibles.yaml (travail neuf)
python3 working-folder/controle-sources/verifier_sources.py nouveau-business-plan/<fichier>.md
python3 working-folder/controle-sources/verifier_sources.py --strict     # tout nombre compte, même sans unité
```

Rapport : `working-folder/out/controle-sources.md` et `.html`. Le script renvoie le code 1 tant qu'il reste une erreur : un document n'est pas publiable dans cet état.

## Comment citer dans un document

| Cas | Écriture | Exemple |
|---|---|---|
| Chiffre lu dans une source | `[ID]` ou `[ID](url)`, ID du registre externe ou de `params/_evidence.yaml` | `15,8 % des OMR [ADEME-MODECOM-2024-DATA](https://...)` |
| Lien vers une page déjà au registre | `[Titre](url)` : l'URL est reconnue | `[Citeo, rapport 2025](https://www.citeo.com/...)` |
| Chiffre calculé | `[calc:ID]`, ID défini dans `calculs.yaml` | `29,5 % [calc:CALC-TAUX-RECYCL-PLAST-MENAGER-2025]` |
| Hypothèse assumée | `[hyp:D-xxx]` ou `[hyp:AFF-xxx]` | `part plastique 0,30 [hyp:D-012]` |
| Tableau d'une seule source | la source dans la phrase qui précède le tableau, ou une ligne « Source : … » juste après | |
| Ligne sans affirmation chiffrée | `<!-- nosrc -->` en fin de ligne | numérotation, exemple de calcul fictif |

La citation doit être dans **la phrase ou la ligne de tableau** qui porte le chiffre. Une source citée seulement à la fin du paragraphe produit un avertissement.

Les marqueurs génériques `[calcul]` ou `[calc]` sans identifiant sont refusés : un calcul doit pouvoir être refait par n'importe qui.

## Ce que le script contrôle

| Contrôle | Gravité |
|---|---|
| Chiffre sans source, calcul ni hypothèse documentée | Erreur |
| `[calcul]` générique, calcul ou hypothèse inconnus | Erreur |
| Calcul dont le résultat recalculé diffère du résultat annoncé | Erreur |
| Entrée de calcul sans source, ou source absente des registres | Erreur |
| Paramètre de `params/*.yaml` sans preuve autre que `V3-MODEL`, `AUCUNE`, un document interne non sourcé ou un document de l'archive | Erreur |
| Lien vers `ARCHIVE-NON-VERIFIE/` dans un document (règle 16) | Erreur |
| Source citée dont la fiche ou la preuve interne renvoie à l'archive | Erreur |
| Chiffre qui ne cite que des documents internes non sourcés (plan d'affaires, annexes, études internes) | Erreur |
| Fiche du registre qui renvoie à l'archive | Erreur |
| Source citée seulement au niveau du paragraphe | Avertissement |
| Lien vers une URL absente du registre | Avertissement |
| **Chiffre absent de la fiche registre de la source citée** | Avertissement |
| Seules des sources de statut `secondaire`, `non-verifie` ou `ancien` | Avertissement |
| Fiche du registre « vérifiée » sans emplacement, citation ni contenu | Avertissement |

Le contrôle « chiffre absent de la fiche registre » est celui qui aurait arrêté l'annexe 8 version 1 : un lien qui ne contient pas le chiffre annoncé. Il impose de noter dans la fiche du registre (champs `contenu` et `citation`) les valeurs effectivement lues dans la source, avec leur emplacement.

## Relecture indépendante

Le script ne lit pas les sources. La vérification de fond est faite par une personne ou un agent **qui n'a pas rédigé le document** :

1. lancer le contrôle et partir de la liste des avertissements « chiffre absent de la fiche registre » ;
2. pour chaque affirmation, ouvrir la source à l'emplacement indiqué et relever la citation exacte ;
3. compléter la fiche du registre (`contenu`, `citation`, `emplacement`) et passer son statut à `verifie-recontrole`, avec la date ;
4. si la source ne contient pas le chiffre : corriger le document, jamais la fiche ;
5. relancer le contrôle jusqu'à zéro erreur.

## Fichiers

| Fichier | Rôle |
|---|---|
| `verifier_sources.py` | Le contrôle |
| `calculs.yaml` | Registre des calculs : formule, entrées sourcées, résultat attendu |
| `cibles.yaml` | Documents contrôlés par défaut : `nouveau-business-plan/` et `sources-externes/`. L'archive n'en fait jamais partie |
| `a-rechercher.yaml` | Liste de recherche : ce que Stéphane a demandé et son statut |
| `arbitrages-parametres-2026-10-10.md`, `notes-parametres-2026-10-10/` | Ce que disent les sources pour chaque paramètre à arbitrer (étiquette LU, à recontrôler) ; version machine : `params/_arbitrages.yaml` |
| `prompts-verification-externe.md` | Prompts pour la contre-vérification par ChatGPT ou DeepSeek |
| `verifications/` | Rapports des vérificateurs externes (Codex, ChatGPT, DeepSeek) |

Registres lus : `reference/sources-externes/registre-sources.yaml` (sources externes), `params/_evidence.yaml` (preuves internes), `params/_decisions.yaml` et `params/_justifications.yaml` (hypothèses).

## L'archive (règle 16)

Depuis le 14/10/2026, l'ancien travail est dans `ARCHIVE-NON-VERIFIE/`. Le contrôle ne le lit pas par défaut. On peut lancer le contrôle sur un fichier de l'archive pour inventorier ce qui pourrait être repris : le rapport le signale comme document d'archive, et un chiffre qui y paraît sourcé reste à relire dans le document d'origine avant d'entrer dans le nouveau plan.
