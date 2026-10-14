# Urban Rig : plan d'affaires

Dépôt réorganisé le 14/10/2026. Le plan d'affaires repart d'une page blanche. Tout ce qui est écrit doit être sourcé, calculé à partir de sources ou déclaré comme hypothèse : voir `REGLES-DE-RIGUEUR.md`.

## Les quatre zones du dépôt

| Zone | Où | Ce qu'on en fait |
|---|---|---|
| **Sources** | `working-folder/reference/sources-externes/` : registre des sources publiques, PDF, index cliquable<br>`working-folder/reference/preuves/` : documents d'origine (documentation constructeur, rapports d'essais, rapports remis à la préfecture de Chiba, autres documents fournis) | On les lit et on les cite, avec la page et la citation exacte. La confiance vient du document d'origine ; le statut de chaque fiche dit si elle a été recontrôlée |
| **Travail neuf** | `nouveau-business-plan/` : page blanche et structure à remplir<br>`working-folder/controle-sources/` : contrôle automatique, calculs enregistrés, liste de recherche, arbitrages<br>`working-folder/params/`, `engine/`, `run.py`, `app.py` : modèle financier | Ne contient que ce qui est sourcé, calculé ou décidé |
| **Archive** | `ARCHIVE-NON-VERIFIE/` : anciens plans d'affaires (dont la v2), annexes, anciens tableurs, synthèses d'IA | **Aucune valeur de preuve.** Structure et pistes de sources seulement (règle 16) |
| **À supprimer** | `_to_delete/` | Doublons exacts et fichiers temporaires. Peut être supprimé |

`deploy/` et `.github/` servent au déploiement de l'application du modèle ; ils ne contiennent aucune donnée.

## Ce qu'il faut savoir sur le modèle

Les valeurs de `working-folder/params/*.yaml` sont héritées de l'ancien modèle. Elles restent en place pour que le moteur tourne. Une valeur n'est utilisable dans le nouveau plan que si sa preuve est une source du registre, un calcul enregistré ou une décision datée. Le contrôle liste les autres :

```
python3 working-folder/controle-sources/verifier_sources.py
```

## Fichiers d'instructions

| Fichier | Pour qui |
|---|---|
| `REGLES-DE-RIGUEUR.md` | Tout le monde : les seize règles |
| `working-folder/METHODE-DE-TRAVAIL.md` | Tout le monde : la méthode par briques |
| `CLAUDE.md` | Claude |
| `AGENTS.md` | Codex et les autres agents de vérification |
| `ARCHIVE-NON-VERIFIE/README.md` | Quiconque ouvre l'archive |
