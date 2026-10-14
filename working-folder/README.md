# Dossier de travail : sources, contrôle et modèle

Mis à jour le 14/10/2026. L'ancien README (septembre 2026) est archivé dans `ARCHIVE-NON-VERIFIE/working-folder/README-septembre-2026.md`.

## Contenu

| Dossier ou fichier | Rôle | Statut |
|---|---|---|
| `reference/sources-externes/` | Registre des sources publiques (`registre-sources.yaml`), PDF, index cliquable | Sources |
| `reference/preuves/` | Documents d'origine : constructeur, essais, rapports remis à la préfecture de Chiba, documents fournis | Sources |
| `controle-sources/` | Contrôle automatique, calculs enregistrés, liste de recherche, arbitrages des paramètres, prompts de vérification externe, rapports des vérificateurs | Outils |
| `params/` | Paramètres du modèle (un fichier par domaine), preuves internes, décisions, justifications, arbitrages | Valeurs héritées, à re-sourcer |
| `engine/`, `run.py`, `rapport.py` | Moteur de calcul et rapport HTML (aucune valeur en dur dans le code) | Outils |
| `app.py`, `Dockerfile`, `requirements.txt` | Application web du modèle, déployée par `deploy/` | Outils |
| `METHODE-DE-TRAVAIL.md` | La méthode par briques | Règle |
| `out/` | Sorties générées, non versionnées | |

## Les valeurs du modèle

Les valeurs de `params/*.yaml` sont héritées de l'ancien modèle. Elles restent en place pour que le moteur tourne, mais aucune n'entre dans le nouveau plan sans l'une de ces trois justifications :

1. une source du registre (`[ID]`) ;
2. un calcul enregistré dans `controle-sources/calculs.yaml` (`[calc:ID]`) ;
3. une décision datée de Stéphane dans `params/_decisions.yaml` (`[hyp:D-xxx]`).

Une preuve de `params/_evidence.yaml` dont le document est dans `ARCHIVE-NON-VERIFIE/` vaut « aucune », pour le moteur comme pour le contrôle (règle 16). Une valeur ne change jamais sans une décision datée.

## Commandes

Depuis la racine du dépôt :

```
python3 working-folder/controle-sources/verifier_sources.py          # contrôle des documents, registres et paramètres
python3 working-folder/run.py                                        # calcul du modèle et rapport HTML (out/)
```

Conventions de citation et procédure de relecture : `controle-sources/README.md`.
