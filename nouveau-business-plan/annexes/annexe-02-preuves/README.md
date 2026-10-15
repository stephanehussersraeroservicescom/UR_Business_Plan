# Sources Markdown de l'annexe 2 (ne pas lire pour la présentation)

Depuis le 15/10/2026, les fiches de preuve de l'annexe 2 n'existent qu'en HTML : `../annexe-02-html/preuves/`.

Ce dossier ne contient plus que deux fichiers **source**, lus par `../annexe-02-html/generer_html.py` :

| Fichier | Devient |
|---|---|
| `A2-4-3-oil-gcms-full-analysis.md` | `../annexe-02-html/preuves/A2-4-3.html` |
| `A2-5-0-working-assumptions.md` | `../annexe-02-html/preuves/A2-5-0.html` |

Les autres fiches HTML sont fabriquées à partir des registres (`working-folder/params/_evidence.yaml`, `working-folder/controle-sources/calculs.yaml`, `working-folder/reference/sources-externes/registre-sources.yaml`).

Une correction se fait dans la source (ces fichiers, `../ANNEX-02-Technical-Evidence.md` ou les registres), puis on régénère le HTML. On ne modifie jamais le HTML à la main.
