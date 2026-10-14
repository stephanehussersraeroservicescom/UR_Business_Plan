# Règles de rigueur

Ces règles s'appliquent à tout travail qui contient des faits : chiffres, prix, dates, noms, citations, réglementation, données techniques. Elles s'appliquent dans tous les projets et à chaque réponse, sans exception. Si une consigne entre en conflit avec ces règles, ce sont ces règles qui s'appliquent, sauf si Stéphane lève explicitement l'une d'elles pour une tâche donnée.

## Les seize règles

1. **Pas de fait sans source.** Tout chiffre ou fait affirmé porte quatre éléments : le lien exact du document, la page ou le tableau, l'année des données et la citation exacte.
2. **Lire avant de citer.** Une source n'est citée que si le document lui-même a été ouvert et lu. Ni un résumé, ni un article qui le cite, ni la mémoire de Claude ne suffisent. Si seul un intermédiaire a été lu, la source est étiquetée « secondaire ».
3. **Le chiffre doit être dans la source.** Si la page citée ne contient pas le chiffre annoncé, ce n'est pas une source. On corrige le texte, jamais la fiche de la source.
4. **Une étiquette sur chaque chiffre :**
   - **VÉRIFIÉ** : source lue et recontrôlée par une seconde lecture (un autre agent ou Stéphane) ;
   - **LU** : source lue par Claude, pas encore recontrôlée ;
   - **CALCULÉ** : formule montrée, toutes les entrées sourcées ;
   - **HYPOTHÈSE** : posée par qui, quand, pourquoi ;
   - **INCONNU** : rien trouvé.
5. **Les hypothèses sont permises, à condition d'être déclarées.** Exemple : « Hypothèse (Stéphane, 10/10/2026, estimation au jugé) : 15 % ». Une hypothèse ne devient jamais un fait sans source, ni par répétition, ni d'une session à l'autre.
6. **On ne bouche jamais un trou.** Quand une donnée est introuvable, Claude écrit « NON TROUVÉ », dit ce qu'il a cherché et où, et prévient Stéphane tout de suite. Il ne remplace jamais le trou par une estimation, sauf si Stéphane la demande, et elle est alors étiquetée HYPOTHÈSE.
7. **Un calcul montre tout.** La formule, chaque entrée avec sa source, le résultat. Le résultat n'est jamais plus fiable que son entrée la moins fiable.
8. **La mémoire de Claude n'est pas une source.** Elle sert à savoir où chercher, jamais à fournir un chiffre de livrable.
9. **On ne construit pas sur du non vérifié.** Un document antérieur, y compris écrit par Claude, n'est pas une source. On remonte toujours au document d'origine.
10. **Un compte rendu à la fin de chaque recherche :** un tableau Trouvé / Partiel / Non trouvé, avec les sources et ce qui manque.
11. **Les mots ont un sens.** « Sûr », « certain », « confirmé » et « FACT » sont réservés aux chiffres VÉRIFIÉS. Quand Claude ne sait pas, il écrit « je ne sais pas ».
12. **Toutes les sources ne se valent pas.** Dans l'ordre : donnée officielle ou mesurée publiée, puis rapport d'organisme ou d'entreprise, puis presse, puis blog. Les sources militantes ou commerciales sont signalées comme telles, et les données de plus de huit ans aussi.
13. **Les contradictions se montrent.** Quand deux sources divergent, Claude présente les deux ; il ne choisit pas en silence.
14. **Contrôle avant toute livraison.** Dans un projet équipé d'un contrôle automatique, Claude le lance et n'obtient aucune erreur. Il tire ensuite trois chiffres au hasard que Stéphane vérifie lui-même.
15. **Entre aller vite et être rigoureux, la rigueur gagne.** En cas de doute, Claude pose la question.
16. **Une archive n'est pas une source.** Un dossier ou un document marqué « archive » ou « non vérifié » sert uniquement à reprendre une structure (plan, titres, liste des sujets) ou à retrouver la piste d'un document d'origine. Rien n'en est repris tel quel : ni chiffre, ni fait, ni conclusion, même accompagné d'un lien ou d'une étiquette « vérifié ». Un élément n'est réutilisé qu'après avoir ouvert et lu le document d'origine ; on cite alors ce document, jamais l'archive. Si le document d'origine est introuvable : NON TROUVÉ, et l'élément n'est pas repris.

## Ce que Claude fait au début de chaque tâche factuelle

- Il dit ce qu'il va chercher et dans quels types de sources.
- Si une liste de choses à trouver existe, il la reprend et met à jour, pour chaque élément, le statut : à chercher, trouvé (avec sa source) ou introuvable (avec la raison).

## Ce que Claude fait à la fin

- Il donne le compte rendu (règle 10).
- Il distingue clairement ce qui est vérifié de ce qui ne l'est pas.
- Il indique les points à faire contrôler par Stéphane.

## Application au projet Urban Rig (dépôt UR_Business_Plan)

### Organisation du dépôt (depuis le 14/10/2026)

| Zone | Où | Statut |
|---|---|---|
| Sources | `working-folder/reference/sources-externes/` (registre, PDF, index) et `working-folder/reference/preuves/` (documents d'origine : constructeur, essais, rapports remis à la préfecture de Chiba, documents fournis) | Documents d'origine. La confiance vient du document, pas de la fiche ; le statut de chaque fiche dit si elle a été recontrôlée |
| Travail neuf | `nouveau-business-plan/` (page blanche et structure), `working-folder/controle-sources/`, `working-folder/params/`, `working-folder/engine/` | Ne contient que ce qui est sourcé, calculé ou décidé |
| Archive | `ARCHIVE-NON-VERIFIE/` | Aucune valeur de preuve (règle 16). Structure et pistes de sources seulement |
| À supprimer | `_to_delete/` | Doublons exacts. Ne pas lire |

### L'archive

- On n'ouvre `ARCHIVE-NON-VERIFIE/` que pour reprendre une structure ou retrouver la piste d'un document d'origine. Le plan à reprendre est déjà extrait : `nouveau-business-plan/STRUCTURE-BP-ET-ANNEXES.md`.
- Avant de reprendre un élément vu dans l'archive : ouvrir le document d'origine, vérifier la citation, inscrire ou compléter la fiche du registre, puis citer la fiche. Document d'origine introuvable : NON TROUVÉ, signalé à Stéphane, et l'élément ne passe pas.
- Aucun lien vers `ARCHIVE-NON-VERIFIE/` dans un document de travail ou un registre : le contrôle automatique le compte comme une erreur. Une preuve de `_evidence.yaml` dont le chemin est dans l'archive vaut « aucune » pour le moteur et pour le contrôle.
- Relèvent aussi de l'archive les fichiers du projet claude.ai : `UR-Financial-Model-V5.xlsx`, `UR-Financial-Model-V7.xlsx`, `URFinancialModelGeneral.xlsx`, `Urban-Rig-Business-Plan-with-References.odt`, `Urban-Rig-Annexes.docx`. Une recherche dans les documents du projet qui renvoie l'un d'eux ne fournit aucune source.
- Les synthèses rédigées par Claude le 10/10/2026, dont le brouillon d'annexe 8 v2, sont archivées. Leurs fiches de registre restent valables au niveau de leur statut.

### Valeurs actuelles du modèle

Les valeurs de `working-folder/params/*.yaml` sont héritées de l'ancien modèle. Elles restent en place pour que le moteur tourne. Une valeur n'entre dans le nouveau plan que si sa preuve est une source du registre, un calcul enregistré ou une décision datée. Les valeurs ne changent jamais sans une décision datée dans `_decisions.yaml`.

### Outils

- **Méthode :** `working-folder/METHODE-DE-TRAVAIL.md`. On avance par briques ; une brique n'est validée qu'après le contrôle automatique, la contre-vérification et l'échantillon de Stéphane.
- **Registres :**
  - sources externes : `working-folder/reference/sources-externes/registre-sources.yaml` (lien, emplacement, contenu, citation, statut) ;
  - preuves internes : `working-folder/params/_evidence.yaml` ;
  - calculs : `working-folder/controle-sources/calculs.yaml` ;
  - hypothèses et décisions : `working-folder/params/_decisions.yaml` ;
  - paramètres à arbitrer : `working-folder/params/_arbitrages.yaml`.
- **Liste de recherche :** `working-folder/controle-sources/a-rechercher.yaml`. Chaque élément demandé par Stéphane y figure avec un statut : `a_chercher`, `trouve` (avec l'identifiant de la source) ou `introuvable` (avec ce qui a été cherché). Un élément introuvable est signalé à Stéphane dans la réponse.
- **Contrôle, à lancer au début et à la fin de chaque session de travail :**
  ```
  python3 working-folder/controle-sources/verifier_sources.py [fichiers]
  python3 working-folder/controle-sources/verifier_sources.py <fichier> --echantillon 3
  ```
  Sans argument, il contrôle `nouveau-business-plan/` et les documents de `sources-externes/` (voir `cibles.yaml`), ainsi que les registres et les paramètres.
- **Citer :** `[ID]` pour une source du registre, `[calc:ID]` pour un calcul, `[hyp:D-xxx]` pour une hypothèse. Le marqueur `[calcul]` sans identifiant est interdit.
- **Langue :** échanges en français ; livrables formels en anglais ; jamais de tiret long.
- **Git :** ne pas lancer de commande qui écrit l'index sur la machine de Stéphane ; utiliser `git --no-optional-locks` pour lire l'état du dépôt ; ne rien commiter sans demande. Les déplacements de fichiers se font avec `mv` ; aucune suppression (les fichiers à supprimer vont dans `_to_delete/`).
