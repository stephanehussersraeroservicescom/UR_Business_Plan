Accès internet : OUI

# Inventaire des contre-vérifications du plan Urban Rig

Date : 25 novembre 2026. Agent : Codex. Dépôt local : `/home/steph/Documents/github/UR_Business_Plan`.

## Périmètre et méthode

Inventaire documentaire uniquement : aucun chiffre du plan, aucune source externe et aucun calcul technique ou financier n'ont été vérifiés dans cette conversation. Le test d'accès internet a été réalisé à l'étape 0. Les nombres ci-dessous comptent des rapports, des entrées et des lots, pas des résultats industriels.

Corpus : les cinq rapports `*-codex-*.md`, `ecarts-annexe-02.md` et `registre-verifications.yaml` présents dans ce dossier avant création du présent rapport ; les huit procédures `verification-annexe-XX.md` ; historique et différences Git. L'archive et `_to_delete/` ne servent pas de preuve. Aucun contrôle automatique du plan n'a été relancé.

Git a été consulté uniquement par `git --no-optional-locks log`, `show` et `diff`. Comparaisons : `47ab800` (15/10/2026, révision 3), `676ce7e` (14/11/2026, premier enregistrement des rapports), puis état local au 25/11/2026, HEAD `dd4da4e` (19/11/2026). Les différences avec HEAD étaient vides pour les fichiers concernés avant écriture de ce rapport.

## Étape 1 : ce qui a déjà été vérifié

Les décomptes reprennent les lignes de verdicts des rapports et du registre. Ils ne constituent aucune nouvelle validation.

| Annexe | Lot ou sujet | Date du rapport | Nombre de verdicts | Écarts ouverts ou traités |
|---|---|---|---:|---|
| 2 | [Lot 1 initial](2026-10-15-codex-annexe-02-lot-1.md), sections 2.1 à 2.3 et 41 fiches | 15/10/2026 | 325 : 303 CONFIRMÉ, 4 DIFFÉRENT, 18 ABSENT | E-1 à E-10 déclarés CLOS dans le suivi ; conclusions remplacées par la réanalyse pour la nouvelle version |
| 2 | [Clarifications](2026-10-15-codex-annexe-02-lot-1-clarifications.md) | 15/10/2026 | 0 nouveau | Objections sur le gaz, le prétri, l'indépendance et le continu nuancées ; pas de nouvelle campagne numérique |
| 2 | [Réanalyse du lot 1](2026-10-15-codex-annexe-02-lot-1-reanalyse.md), révision 4, sections 2.1 à 2.3 et 58 fiches | 15/10/2026 | 346 : 341 CONFIRMÉ, 4 ABSENT, 1 CALCUL FAUX | Cinq réserves R-1 à R-5 ; aucune clôture consignée dans le registre des écarts |
| Transversal, lié à 2 | [Huiles chlorées : débouchés et déchloration](2026-10-17-codex-huiles-chlorees-debouches-dechloration.md) | 17/10/2026 | 13 : 12 CONFIRMÉ, 1 DIFFÉRENT | Recherche explicitement non validée pour intégration au plan ; seconde lecture indépendante manquante |
| Même sujet | [Contrôle automatique de la recherche](2026-10-17-codex-huiles-chlorees-controle.md) | 17/10/2026 | 0 nouveau | 30 erreurs de traçabilité consignées ; échantillon de relecture non coché |
| 2 | [Registre des écarts](ecarts-annexe-02.md) | Décisions du 15/10/2026 | 0 nouveau | Dix écarts E-1 à E-10 déclarés clos ; R-1 à R-5 de la réanalyse absents de ce suivi |

Le [registre des vérifications](registre-verifications.yaml) contient 684 entrées : 325 initiales, 346 de réanalyse et 13 de recherche. Ces entrées se recouvrent ; elles ne représentent pas 684 affirmations distinctes. Les verdicts initiaux restent historiques et ne doivent pas être additionnés à la réanalyse comme une couverture supplémentaire.

### Changements depuis les rapports

| Partie déjà examinée | Statut | Changements ou limite |
|---|---|---|
| Annexe 2, lot 1 initial et clarifications | MODIFIÉ | Passage à la révision 4 : gaz par différence, choix des bilans Chiba, exclusion d'un essai des moyennes, attribution des analyses, limites URT-10 et adaptation des calculs |
| Annexe 2, lot 1 après réanalyse | À REVÉRIFIER | Réserves sans clôture documentée ; identité exacte avec l'état du 15/10 non démontrable par les seuls commits disponibles |
| Annexe 2, HTML principal et fiches depuis le 14/11 | INCHANGÉ | Aucune différence entre `676ce7e` et l'état local pour le HTML et sa source Markdown |
| Calculs du lot 1 et fiches de registre associées depuis le 14/11 | INCHANGÉ | Aucun calcul préexistant modifié ; les modifications ultérieures des registres concernent d'autres sujets |
| Recherche sur les huiles chlorées et contrôle associé | INCHANGÉ depuis leur premier enregistrement Git | Aucun changement depuis `676ce7e` ; cela ne démontre pas l'identité avec leur état exact du 17/10 |

Entre `47ab800` et `676ce7e`, le dossier HTML de l'annexe 2 compte 98 fichiers modifiés ou ajoutés, dont 95 fiches de preuve. Ce nombre concerne l'annexe entière, pas seulement le lot 1. Le Markdown a changé, ainsi que les entrées `KANSO-20002610`, `CHIBA-ESSAIS-FICHES`, `CHIBA-BILANS` et `OWJ-DEMO-2021` de `_evidence.yaml`. Les calculs Noda et plusieurs calculs énergétiques ont été adaptés ; de nouveaux calculs et décisions ont été ajoutés. Ce diff regroupe les corrections du premier rapport et d'éventuels changements ultérieurs : il ne permet pas de les dater séparément.

Après le 14/11, les calculs préexistants et décisions préexistantes sont inchangés. Les ajouts concernent les annexes 4, 5, 7 et 9. `_evidence.yaml` reçoit une précision sur `HARDIN-LOI`. Les entrées publiques modifiées sont `ADEME-MODECOM-2024-DATA`, `ADEME-MODECOM-2024-HUM`, `SDES-2022`, `ORDIF-DMA-2022`, `RP2-002` et `RP2-004` ; elles ne sont pas les sources des verdicts du lot 1 recensés ici. Une modification globale d'un registre ne suffit donc pas à rendre tous ses anciens verdicts caducs.

Les rapports d'octobre ont été enregistrés le 14 novembre. La réanalyse ne publie pas les empreintes individuelles permettant de reconstituer son état exact. L'absence de changement depuis novembre ne suffit pas à classer le lot comme FAIT ET INCHANGÉ depuis octobre.

### Réserves restant à reprendre

Ces points sont ceux du rapport de réanalyse, pas des conclusions techniques nouvellement vérifiées :

1. R-1 : transfert de la composition du gaz sans qualification systématique comme hypothèse.
2. R-2 : assimilation du rendement hors inertes à un rendement obtenu après prétri.
3. R-3 : choix des essais et des pages sources, justification de l'exclusion et propagation des réserves dans la confiance affichée.
4. R-4 : base masse ou volume des pourcentages de la brochure japonaise.
5. R-5 : arrondi, liens de calcul et description des méthodes de mesure ou d'estimation.

La présence actuelle des formulations citées par R-1 et R-2 a été constatée dans le HTML, sans rouvrir les sources ni réévaluer le fond. La phrase sur l'aptitude des huiles à la combustion, signalée dans la recherche du 17/10, y figure aussi. Le statut CLOS de E-1 à E-10 ne constitue pas une clôture des réserves ultérieures R-1 à R-5.

## Étape 2 : couverture des lots

Statuts utilisés :

- FAIT ET INCHANGÉ : vérification complète du lot retrouvée et continuité documentaire suffisamment établie.
- À REVÉRIFIER : lot déjà examiné, mais réserves restantes ou continuité de version insuffisamment établie.
- JAMAIS VÉRIFIÉ : aucune contre-vérification complète du lot retrouvée dans le corpus demandé. Cela ne signifie pas qu'aucune de ses sources n'a jamais été lue.

La recherche sur les huiles chlorées ne couvre intégralement ni le lot 2 de l'annexe 2, ni le lot 1 de l'annexe 3, ni l'annexe 9. Les fiches communes déjà lues dans le lot 1 ne valident pas leur nouvelle utilisation dans une autre section. Les recontrôles de sous-agents mentionnés dans la procédure de l'annexe 8 ne remplacent pas un rapport complet de contre-vérification de ses lots.

Ordre de priorité demandé : **3 (prix), 9 (coûts), 5 (ordures ménagères), 8 (plastiques), 7 (déchets d'entreprises), 2 (preuves techniques), 1 (procédé), 4 (France)**. L'annexe 6 est exclue du périmètre.

| Annexe | Lot | Statut |
|---|---|---|
| 3 | 1 | JAMAIS VÉRIFIÉ |
| 3 | 2 | JAMAIS VÉRIFIÉ |
| 3 | 3 | JAMAIS VÉRIFIÉ |
| 3 | 4 | JAMAIS VÉRIFIÉ |
| 3 | 5 | JAMAIS VÉRIFIÉ |
| 9 | 1 | JAMAIS VÉRIFIÉ |
| 5 | 1 | JAMAIS VÉRIFIÉ |
| 5 | 2 | JAMAIS VÉRIFIÉ |
| 5 | 3 | JAMAIS VÉRIFIÉ |
| 8 | 1 | JAMAIS VÉRIFIÉ |
| 8 | 2 | JAMAIS VÉRIFIÉ |
| 8 | 3 | JAMAIS VÉRIFIÉ |
| 8 | 4 | JAMAIS VÉRIFIÉ |
| 8 | 5 | JAMAIS VÉRIFIÉ |
| 7 | 1 | JAMAIS VÉRIFIÉ |
| 7 | 2 | JAMAIS VÉRIFIÉ |
| 2 | 1 | À REVÉRIFIER |
| 2 | 2 | JAMAIS VÉRIFIÉ |
| 2 | 3 | JAMAIS VÉRIFIÉ |
| 2 | 4 | JAMAIS VÉRIFIÉ |
| 2 | 5 | JAMAIS VÉRIFIÉ |
| 1 | 1 | JAMAIS VÉRIFIÉ |
| 1 | 2 | JAMAIS VÉRIFIÉ |
| 4 | 1 | JAMAIS VÉRIFIÉ |

Bilan : **24 lots, dont 23 JAMAIS VÉRIFIÉ, 1 À REVÉRIFIER et aucun FAIT ET INCHANGÉ** selon les critères ci-dessus.

### Périmètres des lots, recopiés des procédures

Ces lignes décrivent le travail futur. Les instructions de vérification qu'elles contiennent n'ont pas été exécutées pendant cet inventaire.

#### Annexe 3

Source : [procédure de l’annexe 3](../verification-annexe-03.md). Chaque lot inclut les fiches indiquées par sa procédure.

- Lot 1 : section 3.1 (huile : fractions, spécifications comparées aux mesures, statut réglementaire, prix de référence par fraction, sensibilité au Brent, acheteurs), et toutes les fiches vers lesquelles elle renvoie. Refais les calculs CALC-A3-GAZOLE-EUR-T à CALC-A3-HUILE-MOY-BRENT50.
- Lot 2 : section 3.2 (char : caractéristiques, débouchés en cimenterie, critères d'acceptation, statut, prix à parité énergétique et pratique du marché des CSR, élimination), et toutes les fiches vers lesquelles elle renvoie.
- Lot 3 : sections 3.3 et 3.4 (métaux, verre et inertes ; gaz excédentaire et hydrogène : quantités, statut, prix, purification), et toutes les fiches vers lesquelles elles renvoient. Refais les calculs CALC-A3-H2-* et CALC-A3-GAZ-*.
- Lot 4 : sections 3.5 et 3.6 (carbone : lecture des textes et calcul du CO2 évité ; énergie achetée : électricité et combustible), et toutes les fiches vers lesquelles elles renvoient. Pour la section 3.5.1, lis chaque texte cité en version primaire et dis si un crédit carbone est possible, impossible ou possible sous conditions.
- Lot 5 : lecture d'ensemble : « How to Read This Annex », « Key Messages », sections 3.7, 3.8 et 3.9, cohérence des étiquettes et des taux de confiance, toutes les phrases « OneWorld design data ». Lis aussi les rapports des lots 1 à 4 dans working-folder/controle-sources/verifications/. Pour ce lot, la partie « Autres interprétations » est l'essentiel.

#### Annexe 9

Source : [procédure de l’annexe 9](../verification-annexe-09.md). Chaque lot inclut les fiches indiquées par sa procédure.

- Lot unique : toute l'annexe 9. Vérifie chaque donnée OneWorld à sa page (brochures, tableau transport et installation, plan Hardin p. 6), refais CALC-A9-*, et cherche des prix publics plus solides pour le pré-tri (trommel, ouvre-sacs, séparateurs, presse d'extrusion) et le fret de 100 conteneurs du Japon vers la France.

#### Annexe 5

Source : [procédure de l’annexe 5](../verification-annexe-05.md). Chaque lot inclut les fiches indiquées par sa procédure.

- Lot 1 : partie 1, sections 5.1 à 5.4 (tonnages, composition par catégorie, humidité et PCI, matières non convertibles). Refais les calculs CALC-A5-CAT01-T à CALC-A5-CAT13-PCT, CALC-A5-OMR-T et CALC-A5-NONPROC-* à partir du jeu omrcs-compo-jdd. Vérifie le traitement des fines (D-046).
- Lot 2 : sections 5.5 à 5.8 (textiles sanitaires et couches, textiles, composites, plastiques, PVC, bilan d'une tonne). Refais CALC-A5-EAU-KG-T, CALC-A5-SEC-*, CALC-A5-PLAST-*, CALC-A5-COUCHE-POLYMERES-PCT et CALC-A5-PVC-CL-*. Cherche une composition de couche plus récente que 2006.
- Lot 3 : partie 2, sections 5.9 à 5.17 et les Key Messages (essais Urban Rig, littérature, bilan indicatif, énergie, prix d'entrée, conflits, recommandations). Refais les calculs CALC-A5-HUILE-*, CALC-A5-GAZ-*, CALC-A5-CHAR-*, CALC-A5-LATENT-MJ-KG, CALC-A5-EAU-MJ-T, CALC-A5-COUV-* et CALC-A5-KHAN-PCS-MJ-KG. Juge les hypothèses D-043 à D-045. Pour ce lot, la partie « Autres interprétations » est l'essentiel.

#### Annexe 8

Source : [procédure de l’annexe 8](../verification-annexe-08.md). Chaque lot inclut les fiches indiquées par sa procédure.

- Lot 1 : section 8.1 (tonnages, taux de recyclage, devenir, exportations, contribution européenne), et toutes les fiches vers lesquelles elle renvoie. Refais les calculs CALC-A8-EXPORT-3915-T et CALC-A8-EMB-RECY-HORS-FRANCE à partir des requêtes Eurostat indiquées.
- Lot 2 : section 8.2 (coûts d'élimination, tendance, TGAP 2026 dans le CIBS, CSR, capacité francilienne) et section 8.6 (prix d'entrée par défaut), et toutes les fiches vers lesquelles elles renvoient. Refais CALC-A8-INCIN-IDF-HAUSSE-2024-2026. Pour la TGAP, lis le texte de la loi n° 2026-103 (JORF du 20/02/2026), articles L. 433-57, L. 433-86 et L. 433-90 du CIBS.
- Lot 3 : sections 8.3.1 à 8.3.5 (emballages ménagers, films et flux développement, refus de tri, polystyrène, PSE, y compris le paragraphe sur la compréhension du porteur), et toutes les fiches vers lesquelles elles renvoient. Refais CALC-A8-FILMS-REPRIS-T, CALC-A8-PRIXNUL-T, CALC-A8-PRIXNUL-PART, CALC-A8-REFUS-PART-PLASTIQUE et CALC-A8-PS-PART-TRIE.
- Lot 4 : sections 8.3.6 à 8.3.14 (emballages professionnels, agricoles, chutes, DEEE, VHU, bâtiment et PVC, textiles, ameublement, OMR), et toutes les fiches vers lesquelles elles renvoient. Refais CALC-A8-TEXTILES-CSR-T. Vérifie que les plastiques triés et les résidus de broyage sont bien distingués.
- Lot 5 : lecture d'ensemble : « How to Read This Annex », « Key Messages », sections 8.4 (aptitude à l'Urban Rig), 8.5 (concurrence), 8.7 et 8.8, cohérence des étiquettes et des taux de confiance. Lis aussi les rapports des lots 1 à 4 dans working-folder/controle-sources/verifications/. Pour ce lot, la partie « Autres interprétations » est l'essentiel.

#### Annexe 7

Source : [procédure de l’annexe 7](../verification-annexe-07.md). Chaque lot inclut les fiches indiquées par sa procédure.

- Lot 1 : partie 1, sections 7.1 à 7.3 (tonnages, secteurs, composition). Refais CALC-A7-MELANGE-*, CALC-A7-IDF-DAE-*, CALC-A7-NONCONV-PCT et CALC-A7-ORG-PCT. Vérifie la lecture de l'Insee Première 2034 après son erratum du 3/11/2026, et cherche une source d'humidité et de PCI des DAE en mélange (R-048).
- Lot 2 : partie 2, sections 7.4 à 7.9 et Key Messages. Refais CALC-A7-HUILE-*, CALC-A7-GAZ-*, CALC-A7-CHAR-* et CALC-A7-LIQ-*. Juge l'hypothèse D-049. Pour ce lot, la partie « Autres interprétations » est l'essentiel.

#### Annexe 2

Source : [procédure de l’annexe 2](../verification-annexe-02.md). Chaque lot inclut les fiches indiquées par sa procédure.

- Lot 1 : sections 2.1, 2.2 et 2.3 (programme d'essais ; rendements en huile et en gaz des essais sur plastiques purs, déchets municipaux et mélanges ; rendements par matière), et toutes les fiches vers lesquelles elles renvoient.
- Lot 2 : sections 2.4 et 2.5 (qualité de l'huile, analyses de laboratoire, fractions, GC-MS et lecture carburéacteur ; char ; composition et pouvoir calorifique du gaz), et toutes les fiches vers lesquelles elles renvoient.
- Lot 3 : sections 2.6 et 2.8 (bilan énergétique de l'URC-2000 continue ; passage des essais en lots à la machine continue), et toutes les fiches vers lesquelles elles renvoient.
- Lot 4 : section 2.7 (émissions comparées aux normes européennes, odeurs, bruit, eaux de procédé), et toutes les fiches vers lesquelles elle renvoie.
- Lot 5 : lecture d'ensemble : « Key Messages for Investors », « How to Read This Annex », sections 2.9 et 2.10, toutes les phrases « according to OneWorld », cohérence des étiquettes et des taux de confiance. Lis aussi les rapports des lots 1 à 4 dans working-folder/controle-sources/verifications/. Pour ce lot, la partie « Autres interprétations » est l'essentiel.

#### Annexe 1

Source : [procédure de l’annexe 1](../verification-annexe-01.md). Chaque lot inclut les fiches indiquées par sa procédure.

- Lot 1 : « How to Read This Annex », « Key Messages », sections 1.1, 1.2 et 1.3 (gamme OneWorld et illustrations, fonctionnement, produits), et toutes les fiches vers lesquelles elles renvoient.
- Lot 2 : sections 1.4, 1.5 et 1.6 (matières acceptées et pré-tri, émissions et dioxines, séparation des huiles, pilotage, énergie, modularité, sources de revenus, comparaison avec les autres voies, points ouverts), toutes les fiches vers lesquelles elles renvoient, et une lecture d'ensemble de la cohérence avec l'annexe 2. Lis aussi le rapport du lot 1.

#### Annexe 4

Source : [procédure de l’annexe 4](../verification-annexe-04.md). Chaque lot inclut les fiches indiquées par sa procédure.

- Lot unique : toute l'annexe 4. Vérifie les rubriques ICPE à leur page, les délais DRIEAT, l'article L. 541-1, les tarifs de TGAP et les données ORDIF ; refais CALC-A4-* ; cherche les projets de pyrolyse de déchets en mélange en France et les aides publiques applicables (R-051).

## Limites et points de préparation

- La procédure de l'annexe 9 annonce « deux lots » dans son introduction, mais son tableau « Un seul lot » définit un lot unique couvrant toute l'annexe. L'inventaire retient ce tableau explicite.
- La même procédure décrit D-050 comme non tranchée dans ses points d'attention, puis comme un prix fixé par le porteur dans le message proposé. Cette divergence de consignes est à clarifier lors de la future vérification ; aucune décision de fond n'est prise ici.
- Les statuts des écarts sont rapportés tels qu'écrits, sans valider les corrections ni rouvrir leurs sources. Les données externes n'ont pas été actualisées.
- Aucune vérification complète des autres lots n'a été retrouvée dans les rapports et le registre examinés. Une vérification éventuelle conservée ailleurs n'est pas établie par cet inventaire.
- Les futurs lots doivent être examinés dans des conversations séparées selon l'organisation demandée. Les procédures proposent une conversation par lot ; aucun de ces contrôles n'est lancé ici.

## Intégrité

Seul fichier créé : `working-folder/controle-sources/verifications/2026-11-25-codex-inventaire.md`. Aucun verdict ajouté au registre ; aucun HTML, Markdown d'annexe, paramètre ou registre modifié. Aucune suppression, aucun commit, aucune branche et aucune opération Git d'écriture.
