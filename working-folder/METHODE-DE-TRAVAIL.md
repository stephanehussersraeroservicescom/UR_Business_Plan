# Méthode de travail avec Claude sur le business plan Urban Rig

Version du 10 octobre 2026. Ce document remplace toute habitude antérieure.

## Le principe

Claude cherche, lit, calcule et rédige. **Il n'est pas la preuve.** La preuve, c'est le document source, que n'importe qui peut ouvrir et dans lequel il peut retrouver le chiffre.

Un chiffre n'existe dans le business plan que s'il remplit l'une de ces trois conditions :

1. il est **lu dans une source** inscrite au registre, avec la page et la citation exacte ;
2. il est **calculé** à partir de chiffres sourcés, et le calcul est enregistré dans `controle-sources/calculs.yaml` ;
3. c'est une **décision** de Stéphane, inscrite dans `params/_decisions.yaml`.

Tout le reste est marqué « inconnu ». Un trou visible vaut mieux qu'un chiffre inventé.

## Les cinq étiquettes

| Étiquette | Ce qu'elle veut dire |
|---|---|
| **Vérifié** | Quelqu'un a ouvert la source, trouvé le chiffre à la page indiquée et relevé la citation |
| **Lu par Claude** | Claude a lu la source, mais personne d'autre ne l'a encore recontrôlée |
| **Calculé** | Résultat d'un calcul enregistré, dont toutes les entrées sont sourcées |
| **Décision** | Choix de Stéphane, daté et motivé |
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

## L'ordre des briques

On part du bas, comme pour une maison :

1. Ce qui entre dans la machine : gisements, tonnages, composition.
2. Ce qui en sort : rendements, mesurés sur la machine quand c'est possible.
3. Les prix : gate fees, huile, char, métaux, énergie.
4. Les coûts : CAPEX et OPEX, sur devis plutôt que sur estimation.
5. Le modèle financier, qui ne lit que des briques validées.
6. Le texte du business plan et les annexes, en dernier. Ils citent les briques et ne portent aucun chiffre qui leur soit propre.

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
