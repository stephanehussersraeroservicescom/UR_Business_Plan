# Nouveau plan d'affaires : page blanche

Ce dossier accueillera le plan d'affaires et ses annexes, reconstruits à partir de zéro depuis le 14/10/2026.

## Ce qu'il contient aujourd'hui

| Fichier | Rôle |
|---|---|
| `STRUCTURE-BP-ET-ANNEXES.md` | Le plan à reprendre : titres du plan v2, des annexes 1 à 13 et du plan de mars 2026. Titres seulement, aucun chiffre |

## Règles d'écriture

1. Le texte vient en dernier. On valide d'abord les briques, dans l'ordre de `working-folder/METHODE-DE-TRAVAIL.md`.
2. Chaque chiffre cite :
   - une source du registre : `[ID]` ;
   - ou un calcul enregistré : `[calc:ID]` ;
   - ou une décision datée de Stéphane : `[hyp:D-xxx]`.
3. Ce qui n'est pas trouvé est écrit « NON TROUVÉ » ou « INCONNU ». On ne bouche pas le trou.
4. Rien n'est recopié de `ARCHIVE-NON-VERIFIE/` (règle 16 de `REGLES-DE-RIGUEUR.md`). L'archive sert à la structure et à retrouver la piste d'un document d'origine, qu'on ouvre et qu'on lit avant de le citer.
5. Avant toute livraison : `python3 working-folder/controle-sources/verifier_sources.py nouveau-business-plan/<fichier>.md` doit donner zéro erreur, puis Stéphane vérifie un échantillon de trois chiffres (`--echantillon 3`).

Langue : le plan et les annexes sont rédigés en anglais ; les notes de travail en français.
