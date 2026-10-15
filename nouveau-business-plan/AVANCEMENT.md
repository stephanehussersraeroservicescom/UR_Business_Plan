# Avancement du plan d'affaires v3

Mémoire commune des chats. Chaque chat lit ce fichier au début et le met à jour à la fin. On ne se fie pas à l'historique des conversations.

## Périmètre (décision D-017 du 14/10/2026)

- France seule. La Corée du Sud est retirée.
- Gisements : ordures ménagères résiduelles (annexe 5), aéroport CDG (annexe 6), déchets d'activités économiques en mélange (annexe 7), déchets plastiques (annexe 8).
- Annexe 8 (décision D-018) : toutes les filières du plastique, ménagères et industrielles, en priorité celles qui sont peu ou pas recyclées. Pour chaque filière : tonnages, taux de recyclage réel, devenir de ce qui n'est pas recyclé, qui paie quoi. Exemple à vérifier, donné par Stéphane : le polystyrène, compacté ou fondu en blocs, sans débouché réel de valorisation selon sa compréhension. Les flux de plastique seul d'origine industrielle vont dans l'annexe 8, pas dans l'annexe 7.

## Statuts

`à faire` → `en cours` → `contrôle auto OK` (zéro erreur) → `contre-vérifiée` (chaque chiffre a un verdict avec citation dans `working-folder/controle-sources/verifications/registre-verifications.yaml`) → `validée` (échantillon de trois chiffres contrôlé par Stéphane ; l'annexe est alors figée).

## Tableau de bord

| Ordre | Livrable | Statut | Dernier chat (date) | Contrôle auto | Contre-vérification | Validation Stéphane | Fichier |
|---|---|---|---|---|---|---|---|
| 1 | Annexe 2, Technical Evidence | contrôle auto OK (zéro erreur sur l'annexe ; 115 affirmations chiffrées sourcées) | chat 1 (14/10/2026) | OK 14/10/2026 | à faire (message Codex : `annexes/notes-recherche-annexe-02/message-codex-contre-verification.md`) | échantillon de 3 chiffres tiré : `working-folder/out/echantillon-a-verifier.md` | lecture : `annexes/annexe-02-html/index.html` ; source : `annexes/ANNEX-02-Technical-Evidence.md` |
| 2 | Annexe 1, Process and Technology | à faire | | | | | |
| 3 | Annexe 9, Equipment Configuration and Costs | à faire | | | | | |
| 4 | Annexe 5, Municipal Solid Waste | à faire | | | | | |
| 5 | Annexe 6, Airport Waste, CDG | à faire | | | | | |
| 6 | Annexe 7, Industrial and Commercial Waste | à faire | | | | | |
| 7 | Annexe 8, Plastic Waste | à faire | | | | | |
| 8 | Annexe 3, Output Markets and Pricing | à faire | | | | | |
| 9 | Annexe 4, France | à faire | | | | | |
| 10 | Modèle financier, puis annexes 10 à 13 | à faire | | | | | `working-folder/params/` |
| 11 | Plan d'affaires | à faire | | | | | |
| 12 | Présentation interactive (application sur Hetzner) | à faire | | | | | `working-folder/app.py` |

## Décisions en attente de Stéphane

- Arbitrage des paramètres du modèle : `working-folder/params/_arbitrages.yaml` (section « Annexe 2 » ajoutée le 14/10/2026 : rendements, densité et PCI de l'huile, gaz, besoin thermique, électricité, PCI du fioul).
- Échantillon de trois chiffres de l'annexe 2 à contrôler : `working-folder/out/echantillon-a-verifier.md`.

## Demandes à OneWorld

Tenues dans `working-folder/controle-sources/a-rechercher.yaml` (statut `a_demander`, détenteur OneWorld). Chaque chat d'annexe y ajoute les siennes.

## Journal

- 14/10/2026 : réorganisation du dépôt (archive non vérifiée, sources, page blanche) ; structure extraite ; décisions D-016 (déclarations de OneWorld) et D-017 (périmètre) ; ordre de travail arrêté ; décision D-018 (périmètre de l'annexe 8, limite avec l'annexe 7).
- 14/10/2026, chat 1 annexe 2 : inventaire des preuves page par page (29 fichiers, 28 lisibles) ; 28 entrées ajoutées à `_evidence.yaml` et 6 fiches existantes annotées (sans changement de valeur ni de chemin) ; demandes R-009 à R-022 dans `a-rechercher.yaml`. Contrôle : 34 erreurs, toutes antérieures (params hérités). Point d'arrêt avant rédaction.
- 14/10/2026, chat 1 annexe 2 : décision D-019 (rapport de Chiba cité en original japonais seulement ; chemin de GC-B2002600 corrigé) ; brochure anglaise endommagée remplacée par Stéphane (copie identique) ; R-022 trouvé.
- 14/10/2026, chat 1 annexe 2 : rédaction de `ANNEX-02-Technical-Evidence.md` (anglais, orientée investisseur, plan de STRUCTURE ; sections 2.7.3 « Process Water » ajoutée) ; 25 calculs `CALC-A2-*` enregistrés ; contrôle à zéro erreur sur l'annexe ; échantillon de 3 chiffres tiré ; arbitrages proposés ; message pour Codex prêt. Prochaine étape : contre-vérification Codex, puis validation de Stéphane.
- 14/10/2026, chat 1 annexe 2 : version 2 de l'annexe après retour de Stéphane (décision D-020 : documentation OneWorld comme base de conception ; tableau par essai avec conversion huile + gaz ; déchets municipaux hors métaux ; émissions comparées à la directive 2010/75/UE et aux MTD 2019/2010). 38 calculs et 4 sources externes ajoutés. Contrôle : zéro erreur sur l'annexe (166 affirmations). Version 1 conservée dans `notes-recherche-annexe-02/ANNEX-02-version1-2026-10-14.md`.
- 14/10/2026, chat 1 annexe 2 : version 3 (décision D-021) : PCI du gaz calculé à 37,4 MJ/kg (composition B2002600 hors air, données NIST) ; char à 32 090 J/g ; huile à 46 000 J/g ; bilan énergétique sur les chiffres OneWorld de l'URC-2000 (essais en lots réservés aux coefficients) ; chlore de l'huile comparé aux références par débouché ; métaux du char comparés au règlement (UE) 2019/1009 et à l'arrêté CSR du 23/05/2016. 10 sources externes et environ 40 calculs ajoutés. Contrôle : zéro erreur sur l'annexe (203 affirmations). À trancher : électricité 600 kW ou 20 kW.
- 14/10/2026, chat 1 annexe 2 : version 4 (décision D-022) : chaque argument renvoie par lien à une fiche de preuve (`annexes/annexe-02-preuves/`, 30 fiches + index) avec nom exact du fichier source, page, citation, valeurs, et un taux de confiance (100 / 95 / 90 / 80 %). Les étiquettes LU, CALCULÉ, CONSTRUCTEUR sont dans les fiches. Contrôle : zéro erreur sur l'annexe et les 30 fiches ; 700 liens vérifiés. Version 3 conservée dans `notes-recherche-annexe-02/ANNEX-02-version3-2026-10-14.md`.
- 14/10/2026, chat 1 annexe 2 : version HTML (`annexes/annexe-02-html/index.html` + `preuves/`, 126 pages). Le texte principal ne porte plus que de petits liens ; chaque fiche montre en tête deux encarts (ce que la preuve établit ; confiance en %), puis le mode opératoire (document source, page, citation ; ou méthode, formule, entrées liées, résultat). Une fiche par source et par calcul (2.1.a à 2.4.x, 2.5.0, 2.5.a.1 à 2.5.f.x). Régénérable par `annexes/annexe-02-html/generer_html.py` à partir du Markdown et des registres. 1 075 liens vérifiés, zéro lien cassé. Le Markdown reste la référence contrôlée (zéro erreur).
- 14/10/2026 soir, chat 1 annexe 2 : questions de Stéphane traitées. (1) Chlore : la méthode JLOS n'est pas indiquée, le mot « total » est retiré ; forme du chlore (organique ou minérale) non documentée ; l'unité d'essai de Noda avait un réservoir catalytique avant le condenseur (rapport Chiba PDF p. 29). (2) Gaz KANSO : point de prélèvement non renseigné sur le bulletin. (3) Dioxines 2022 et 2023 : deux unités et deux campagnes différentes, sans correction d'O2. (4) Eaux : l'unité d'essai n'avait pas de traitement (PDF p. 39) ; SEA CORAL = option, seul un essai de dessalement d'eau de mer est documenté. (5) Nouvelle analyse GC-MS complète et lecture carburéacteur / SAF (`annexe-02-preuves/A2-4-3-oil-gcms-full-analysis.md`, calculs A2.5.g, références A2.4.e). R-010, R-011, R-013, R-016, R-017, R-021 complétés. Email à Peter : `notes-recherche-annexe-02/email-peter-2026-10-14.md`. Contrôle : zéro erreur sur l'annexe et les fiches (34 erreurs héritées des params) ; HTML régénéré, 157 pages, 1 479 liens, zéro cassé. Version 4 conservée dans `notes-recherche-annexe-02/ANNEX-02-version4-2026-10-14.md`.
- 15/10/2026 : décision D-023 (format des annexes). L'annexe 2 se lit et se contre-vérifie en HTML (`annexes/annexe-02-html/`), généré à partir de la source Markdown et des registres ; on corrige la source puis on régénère. Régénération vérifiée : HTML identique (hors bandeau « fichier généré »). Effacés à la demande de Stéphane : versions Markdown 1, 3 et 4, sauvegarde v4, et les 32 fiches Markdown que le générateur ne lit pas. Le contrôle signale désormais un HTML plus ancien que sa source.
- 15/10/2026, chat 1 annexe 2 : Key Message 6 reformulé (chlore 0,137 % et 0,526 %, sous le seuil de 1 % de la directive 2010/75/UE ; chlore venant du PVC et matières similaires selon OneWorld ; débouchés supérieurs accessibles sans PVC ou après déchloration, à confirmer par R-013). Section 2.4.1 : ligne « réaction » ajoutée (acide en 2022, neutre en 2019), explication de l'écart 2019 / 2022 (NKKK 2019 : chlore inorganique seul, titrage au nitrate d'argent, échantillon non identifié) ; seuil de 3 ppm qualifié d'« industrial threshold, not a legal limit ». Fiche NKKK complétée (méthode, réaction). HTML régénéré (157 pages, 0 lien cassé) ; contrôle : 0 erreur sur l'annexe.
- 15/10/2026, chat 1 annexe 2 : section 2.4.3 et annexe 2.4.3 complétées d'une fourchette indicative de la part de l'échantillon « drain » dans la plage carbone du kérosène : 17,69 % (bas) à 27,1 % (haut), avant traitement, sous l'hypothèse D-024 (aire GC-MS prise pour la masse, posée par Claude à la demande de Stéphane). Calculs CALC-A2-GCMS-JET-ECH-BAS et -HAUT (90 %). HTML régénéré (159 pages, 0 lien cassé) ; contrôle : 0 erreur sur l'annexe.
