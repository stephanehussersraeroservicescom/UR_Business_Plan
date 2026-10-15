# Passation, chat 1 annexe 2 (14/10/2026 soir)

## État
- Annexe : `nouveau-business-plan/annexes/ANNEX-02-Technical-Evidence.md` (v5). Version 4 : `notes-recherche-annexe-02/ANNEX-02-version4-2026-10-14.md`. Fiches v4 : `notes-recherche-annexe-02/sauvegarde-preuves-v4/`.
- Fiches de preuve : `annexes/annexe-02-preuves/` (34 fichiers + README). Nouveautés : A2-3-e (SEA CORAL), A2-4-3 (GC-MS complète et lecture SAF), A2-4-e (Jet A-1, ReFuelEU), A2-5-g (calculs GC-MS et températures d'ébullition).
- HTML : `annexes/annexe-02-html/index.html`, régénérer avec `python3 nouveau-business-plan/annexes/annexe-02-html/generer_html.py`. Le Markdown reste la référence contrôlée.
- Contrôle : 0 erreur sur l'annexe et les fiches ; 34 erreurs héritées des params.
- Ajouts au registre : scripts et extraits dans `notes-recherche-annexe-02/scripts/` (*-2026-10-14b.yaml).

## En attente de Stéphane
- Envoi de l'email à Peter (`notes-recherche-annexe-02/email-peter-2026-10-14.md`).
- Électricité URC-2000 : 600 kW ou 20 kW.
- Échantillon de 3 chiffres ; arbitrages `_arbitrages.yaml` ; contre-vérification Codex.

## Non trouvé (à chercher dans une brique suivante)
- ASTM D7566 : voie d'approbation d'un kérosène de pyrolyse de plastique, teneur en aromatiques exigée.
- Directive (UE) 2018/2001 art. 2 point 35 et art. 29a(2) : définition des carburants à carbone recyclé et seuil de réduction d'émissions (EUR-Lex inaccessible le 14/10).
- Température d'ébullition du 2,4-diméthyl-1-heptène (absente du NIST WebBook).
- Forme du chlore des huiles (organique ou minérale) : aucune mesure.

## Mise à jour du 15/10/2026 (décision D-023)
- Version de lecture et de contre-vérification : le HTML (`annexes/annexe-02-html/`). Le Markdown `ANNEX-02-Technical-Evidence.md` reste la source du HTML et du contrôle automatique.
- `annexes/annexe-02-preuves/` ne contient plus que les deux fichiers lus par le générateur (A2-4-3, A2-5-0) et un README. Les 32 autres fiches Markdown, les versions 1, 3 et 4 et `sauvegarde-preuves-v4/` ont été effacées à la demande de Stéphane.
- Les liens du Markdown vers les fiches `.md` sont convertis en liens vers les fiches HTML par le générateur ; ils ne mènent plus à rien dans le Markdown lui-même, ce qui est voulu.
