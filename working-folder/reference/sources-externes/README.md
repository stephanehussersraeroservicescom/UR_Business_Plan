# Sources externes

Ce dossier contient les sources publiques du projet : statistiques, études, textes réglementaires, prix de marché. Les documents d'origine internes (constructeur, essais) sont dans `../preuves/`.

Mis à jour le 14/10/2026. Les synthèses rédigées à partir de ce registre le 10/10/2026 (fichiers 01 à 04, dont le brouillon d'annexe 8 v2, et la note de passation) sont archivées dans `ARCHIVE-NON-VERIFIE/working-folder/reference/sources-externes/`. Elles n'ont pas été contre-vérifiées ; leurs fiches de registre restent ici.

## Contenu

| Fichier | Rôle |
|---|---|
| `registre-sources.yaml` | Registre unique : identifiant, titre, éditeur, date, URL, emplacement (page, tableau), contenu relevé, citation exacte, statut |
| `pdf/` | Copies des documents d'origine, pour que la preuve reste disponible si le site change |
| `index-sources.html` | Toutes les fiches sous forme de liens cliquables |
| `generer_index.py` | Régénère `index-sources.html` depuis le registre |
| `telecharger-sources.sh` | Télécharge les documents dans `pdf/`, à lancer depuis un terminal ordinaire |

## Ce que vaut une fiche

Une fiche est un index : elle dit où se trouve le chiffre et ce que Claude ou un vérificateur y a lu. La preuve, c'est le document d'origine. Le statut dit jusqu'où la fiche a été contrôlée :

| Statut | Signification |
|---|---|
| `verifie-recontrole` | Chiffre lu dans le document d'origine, citation relevée, puis recontrôlé par une seconde lecture |
| `verifie` | Chiffre lu dans le document d'origine, citation relevée, pas encore recontrôlé (étiquette LU) |
| `secondaire` | Chiffre lu dans un document qui en cite un autre (presse, observatoire, entreprise) |
| `ancien` | Document d'origine, mais données de plus de huit ans |
| `non-verifie` | Recherché sans succès ; ne pas utiliser |

## Règles

- Pas d'identifiant du registre, pas de chiffre dans le plan.
- Une valeur dérivée de plusieurs sources est un calcul enregistré dans `working-folder/controle-sources/calculs.yaml`, cité `[calc:ID]`.
- Une fiche ne renvoie jamais à `ARCHIVE-NON-VERIFIE/` (règle 16) ; le contrôle automatique le refuse.
- Si le document d'origine ne contient pas le chiffre annoncé, on corrige le texte qui le cite, jamais la fiche.
