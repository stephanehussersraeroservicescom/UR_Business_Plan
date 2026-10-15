# Méthode de travail avec Claude sur le business plan Urban Rig

Version du 10 octobre 2026. Ce document remplace toute habitude antérieure.

## Le principe

Claude cherche, lit, calcule et rédige. **Il n'est pas la preuve.** La preuve, c'est le document source, que n'importe qui peut ouvrir et dans lequel il peut retrouver le chiffre.

Un chiffre n'existe dans le business plan que s'il remplit l'une de ces trois conditions :

1. il est **lu dans une source** inscrite au registre, avec la page et la citation exacte ;
2. il est **calculé** à partir de chiffres sourcés, et le calcul est enregistré dans `controle-sources/calculs.yaml` ;
3. c'est une **décision** de Stéphane, inscrite dans `params/_decisions.yaml`.

Tout le reste est marqué « inconnu ». Un trou visible vaut mieux qu'un chiffre inventé.

## Les six étiquettes

| Étiquette | Ce qu'elle veut dire |
|---|---|
| **Vérifié** | Quelqu'un a ouvert la source, trouvé le chiffre à la page indiquée et relevé la citation |
| **Lu par Claude** | Claude a lu la source, mais personne d'autre ne l'a encore recontrôlée |
| **Calculé** | Résultat d'un calcul enregistré, dont toutes les entrées sont sourcées |
| **Décision** | Choix de Stéphane, daté et motivé |
| **Constructeur** | Déclaration de OneWorld, lue dans un document de OneWorld (brochure, présentation, rapport, courriel) avec la page ou la date. Admise comme base de travail (décision D-016), toujours attribuée dans le texte (« according to OneWorld »), jamais présentée comme vérifiée de façon indépendante. Le rapport de mesure correspondant est demandé à OneWorld |
| **Inconnu** | Aucune source trouvée. On ne bouche pas le trou |

Le mot « sûr » n'est jamais employé pour un chiffre qui n'est pas « Vérifié ».

## Avancer par briques

Une brique, c'est **une question précise**, par exemple : « Combien de plastique contiennent les OMR d'Île-de-France ? ». On ne construit jamais sur une brique qui n'est pas validée.

Chaque brique passe par cinq étapes :

1. **La question.** Stéphane la pose en une phrase. Claude dit ce qu'il va chercher et où.
2. **La collecte.** Claude trouve les sources et les inscrit au registre (lien, page, citation exacte). Quand c'est possible, le PDF est déposé dans `reference/sources-externes/pdf/`, pour que la preuve ne disparaisse pas si le site change.
3. **Le contrôle automatique.** Claude lance `verifier_sources.py` sur la brique. Il faut **zéro erreur** pour passer à l'étape suivante.
4. **La contre-vérification.** Un second agent, qui n'a pas rédigé la brique, rouvre chaque source et confirme les chiffres.
5. **Le contrôle de Stéphane, 10 minutes.** Le script tire au hasard 3 chiffres :
   `python3 working-folder/controle-sources/verifier_sources.py <fichier> --echantillon 3`
   Stéphane ouvre les trois liens et coche OK ou FAUX. **Un seul FAUX bloque la brique** : on cherche pourquoi, et on revérifie toute la brique.

Une brique validée est **figée**. On ne la modifie plus sans ouvrir une décision datée.

## L'ordre de travail de la version 3 (décidé le 14/10/2026)

On commence par ce que la machine fait réellement, puis ce qu'on lui donne, puis ce que ça rapporte :

1. Annexe 2, preuves techniques : rendements, qualité des produits, émissions, énergie. Première étape : inventaire page par page des documents de `reference/preuves/`.
2. Annexe 1, procédé.
3. Annexe 9, équipement et coûts.
4. Annexes 5 à 8, gisements : ordures ménagères, CDG, déchets d'activités économiques, déchets plastiques.
5. Annexe 3, marchés et prix des produits.
6. Annexe 4, France : statistiques, réglementation, marché.
7. Modèle financier, qui ne lit que des briques validées ; les annexes 10 à 13 (économie par gisement) en sortent.
8. Plan d'affaires, qui résume les annexes et le modèle, sans chiffre qui lui soit propre.
9. Présentation interactive (application du modèle sur Hetzner).

Périmètre (décision D-017) : France seule ; la Corée du Sud est retirée.

## Un chat par annexe

- Chaque annexe est traitée dans un chat dédié du projet « business plan ».
- Le chat commence par lire `nouveau-business-plan/AVANCEMENT.md` et la dernière note de passation de l'annexe, et termine en les mettant à jour. C'est la mémoire commune ; on ne se fie pas à l'historique des conversations.
- Si le chat devient long, il écrit une note de passation (`nouveau-business-plan/annexes/notes-recherche-annexe-XX/PASSATION-AAAA-MM-JJ.md`) et le travail continue dans un nouveau chat.
- Une donnée n'est cherchée qu'une fois : avant toute recherche, on consulte le registre et `_evidence.yaml`.
- Format (décision D-023) : l'annexe se lit et se contre-vérifie en HTML (`annexes/annexe-XX-html/`), généré à partir de sa source Markdown et des registres par `generer_html.py`. On corrige la source, jamais le HTML, puis on régénère. Pas d'anciennes versions dans le dépôt : l'historique git suffit.
- Un chat d'annexe ne change aucune valeur du modèle. Il propose les changements dans `params/_arbitrages.yaml` ; Stéphane tranche par une décision datée.
- Les contre-vérifications (Codex, ChatGPT, DeepSeek, Stéphane) sont consignées dans `controle-sources/verifications/registre-verifications.yaml`. Une annexe est « contre-vérifiée » quand chaque chiffre y a un verdict avec citation.

## Au début de chaque session

Stéphane commence par une phrase de ce type : « On travaille sur la brique X. Lance d'abord le contrôle des sources. »

Claude doit alors :

- lancer le contrôle et dire où en est la brique ;
- ne s'appuyer que sur ce qui est validé ;
- signaler tout de suite une source introuvable, au lieu de la remplacer par une estimation.

## Ce qui doit alerter Stéphane

- Un chiffre sans lien ou sans page.
- Un lien vers la page d'accueil d'un site, ou vers un article qui cite une autre source.
- « Industry estimates », « études de caractérisation » ou « selon les experts », sans référence précise.
- Un chiffre très arrondi et commode, ou qui arrange beaucoup le résultat.
- Une conclusion trop belle : quand tout va dans le même sens, c'est souvent qu'on n'a rien contre-vérifié.
- Une longue session où l'on enchaîne beaucoup de sujets différents sans repasser par le contrôle.

## Ce qu'on garde du travail précédent (organisation du 14/10/2026)

- **Les documents d'origine restent des preuves** : essais, rapports remis à la préfecture de Chiba, documentation constructeur, documents fournis (`reference/preuves/`), et les sources publiques du registre (`reference/sources-externes/`). Ils sont cités avec la page et la citation exacte. Un document constructeur reste une source commerciale (règle 12).
- **Tout le reste est archivé** dans `ARCHIVE-NON-VERIFIE/` : plans d'affaires, annexes, présentations, anciens tableurs, synthèses rédigées avec ChatGPT ou Claude, y compris celles du 10/10/2026. L'archive n'a aucune valeur de preuve (règle 16). On y reprend la structure, déjà extraite dans `nouveau-business-plan/STRUCTURE-BP-ET-ANNEXES.md`, et des pistes de documents d'origine, qu'on ouvre et qu'on lit avant de les citer.
- **La cotation OneWorld** n'est connue que par le texte de l'annexe 9, archivée. Elle redevient une preuve quand le document de cotation lui-même est versé dans `reference/preuves/` (recherche R-005).
- **Les valeurs du modèle** (`params/`) sont héritées de l'ancien modèle. Chacune repasse par une brique : source, calcul enregistré ou décision datée.
- Le texte du business plan et les annexes sont reconstruits à partir des briques validées, dans `nouveau-business-plan/`.
