# Contre-vérification indépendante de l'annexe 8, lot 3

Date : 2026-11-25  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-08-html/index.html`  
Périmètre : introduction, messages clés, sections 8.4 à 8.8 et interprétation d'ensemble  
Accès internet : OUI  
Lecture des sources originales : OUI

## Méthode et limites

Les textes réglementaires, rapports d'essais, analyses de laboratoire et sources d'actualité industrielle ont été rouverts. Les calculs sans prix du périmètre ont été refaits. Les prix, tarifs, coûts et hypothèses D-xxx n'ont pas été recalculés, conformément aux règles de vérification légère. Ils doivent être confirmés par offre, contrat ou lettre d'intention avant décision.

Le contrôle automatique avec `--echantillon 3` a été lancé. Comme lors des lots précédents, il ne sait pas interpréter correctement les liens internes vers les fiches de preuve. Ses classements automatiques ne sont donc pas utilisés comme verdicts.

## Tableau des verdicts

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---:|---|---|---|---|---|---|---|---|
| 1 | Messages clés | Emballages plastiques France en 2023 | 2 428 987 t générées ; 625 275 t recyclées ; 25,7 % ; 1 213 829 t valorisées énergétiquement | EUROSTAT-WASPAC | CONFIRMÉ | `GEN T 2023: 2428987 ; RCY T 2023: 625275 ; RCY PC 2023: 25.7 ; RCV_E_PAC T 2023: 1213829` | API Eurostat `env_waspac`, France, W150102, 2023 | Même pays, même flux et même année. |
| 2 | Messages clés | Taux UE de recyclage des emballages plastiques | 41,7 % en 2023 | A8-CAD-EUROSTAT-WASPAC-UE-2023 | DIFFÉRENT | « In 2024, the EU recycled 42.4% [...] compared with 2023 (41.6%). » | Eurostat, actualité du 22 octobre 2026, source `env_waspac` | La base a été révisée à 41,6 %. Écart de 0,1 point. |
| 3 | Messages clés et fiche 8.C.a | Part recyclée hors de France | 49,1695 %, présenté comme environ 49 % | EUROSTAT-WASPAC | CALCUL FAUX | `RCY_EU_FOR 296981 ; RCY_NEU 10463 ; RCY 625275` | API Eurostat, France, 2023 | (296 981 + 10 463) / 625 275 x 100 = 49,169405 %, soit 49,1694 % à quatre décimales. Le texte arrondi à 49 % reste juste. |
| 4 | Messages clés et fiche 8.C.c | CALC-A8-PRIXNUL-T | 164 879 t | A8-MENA-PRIXREPRISE-2025 | CONFIRMÉ | « Films [...] 25 370 t » ; « Films [...] 72 009 t » ; « Flux développement [...] 66 005 t » ; « PS [...] 702 t » ; « PSE [...] 793 t » | PDF p. 27 | 25 370 + 72 009 + 66 005 + 702 + 793 = 164 879 t. |
| 5 | Messages clés et fiche 8.C.d | CALC-A8-PRIXNUL-PART | 37 % | A8-MENA-PRIXREPRISE-2025 | CONFIRMÉ | « Prix moyenne Plastiques [...] 445 822 t » | PDF p. 27 | 164 879 / 445 822 x 100 = 36,9832 %, correctement arrondi à 37 %. |
| 6 | Messages clés | Pots PS mis en marché et arrivant en centre de tri | 60 000 t ; environ 5 000 t | A8-PS-CITEOAO-2022 ; A8-PS-QUECHOISIR-2025 | CONFIRMÉ | « 60 000 tonnes de pots sécables » ; « seules 5 000 tonnes [...] arrivent dans les centres de tri, d'après Citeo » | Communiqué Citeo p. 1 ; Que Choisir, 1 avril 2025 | Le second chiffre est une source de presse attribuée à Citeo. |
| 7 | Messages clés | PSE ménager | environ 15 000 t ; 1 200 t/an triées ; aucun exutoire propre | A8-PS-CITEOPSE-2025 | CONFIRMÉ | « environ 15 000 tonnes » ; « seulement 1 200 T/an triées » ; « n'a pas d'exutoire en propre » | Feuille de route Citeo, p. 2-3 | Même périmètre. |
| 8 | Messages clés | TGAP stockage et incinération | Stockage 69 à 85 EUR/t ; incinération 16 à 20 ou 29 à 45 EUR/t, 2026-2030 | CIBS-TGAP-2026 | CONFIRMÉ | « Non dangereux 69 73 77 81 85 » ; « De 65 % à 100 % 16 17 18 19 20 » ; « Inférieure à 65 % 29 33 37 41 45 » | Loi n° 2026-103, CIBS, p. 58 et 60 | Tarifs légaux exacts. Les montants futurs restent soumis aux règles d'indexation du code. |
| 9 | Messages clés et 8.4 | Composition minimale de l'intrant pour la SSD de l'huile | PE + PP + PS au moins 85 % ; PVC au plus 3 % | A3-ARRETE-SSD-HUILE-PYROLYSE-2024 | CONFIRMÉ | « est au moins de 85 % en masse de matière sèche » ; « inférieure ou égale à 3 % en masse de matière sèche en PVC » | Arrêté du 19 février 2024, annexe I, points 1.2 et 1.3 | Ces deux seuils sont exacts mais ne résument pas toutes les conditions d'admission. Voir E-1. |
| 10 | 8.4 | Rendement d'huile PE et PP | 73 % à 81 % | CHIBA-ESSAIS-FICHES | CONFIRMÉ | « PE granules 74 %, PE chutes 77 % [...] PP granules 81 %, PP chutes 80 % [...] PE bidons 81 %, PP palettes 73 % » | Rapport Chiba, PDF p. 19-23 | Valeurs retrouvées sur les fiches d'essai. |
| 11 | 8.4 | Rendement d'huile PS, y compris PSE | 55 % à 73 % | CHIBA-ESSAIS-FICHES | CONFIRMÉ | « PS granules 61 %, PS chutes 55 % [...] PS expanse 73 % » | Rapport Chiba, PDF p. 20 et 23 | Même polymère et même définition du rendement. |
| 12 | 8.4 | Essai de mélange avec PVC et FRP | PVC arrêté au stade de la fusion | OWJ-DEMO-2021 | CONFIRMÉ | « 塩ビに関しては融点で止まっている » | Rapport OneWorld, p. 8 | Déclaration du constructeur issue d'un essai constructeur. Nature : constructeur. |
| 13 | 8.4 et interprétation | Périmètre des rendements présentés comme essais sur équipement Urban Rig | Cible du projet non précisée dans le tableau | CHIBA-RAPPORT-2023 ; CHIBA-ESSAIS-FICHES | DIFFÉRENT | « en lots de 20 à 60 kg » ; « Machine en lots, pas l'URC-2000 continue » | Fiche 2.1.a ; rapport Chiba p. 7 et p. 19-26 | Les rendements sont bien mesurés, mais sur une unité discontinue. La performance de l'URC-2000 continue à 51 100 t/an n'est pas démontrée. |
| 14 | 8.4 | Mécanisme annoncé de capture du chlore | HCl dilué puis couche catalytique | UR2000-JP-P03-P04-CHLORE | CONFIRMÉ | « 塩素やカーボン吸着の触媒層を通過後 » | Brochure OneWorld URC-2000, p. 3-4 | OneWorld l'affirme, mais aucune mesure de chlore en sortie de couche n'est fournie. Nature : constructeur. |
| 15 | 8.4 | Chlore dans deux huiles de plastiques municipaux | 0,137 % et 0,526 % masse | CHIBA-JLOS-HUILES | CONFIRMÉ | « 塩素分 質量% 0.137 » ; valeurs relevées « 0,137 / 0,526 % masse » | Bulletins JLOS, PDF p. 45-46 | Analyses d'un laboratoire tiers, réalisées après une étape catalytique dont l'équivalence avec l'URC-2000 reste à confirmer. |
| 16 | 8.4 | Limite d'halogènes de l'huile sans purification | 500 ppm | A3-ARRETE-SSD-HUILE-PYROLYSE-2024 | CONFIRMÉ | « Somme des halogénés : Br + Cl + F + I | 500 ppm » | Arrêté du 19 février 2024, annexe I, tableau A | Le tableau fixe aussi un maximum de 5 ppm pour le brome. |
| 17 | 8.4, 8.6 et interprétation | Périmètre des flux compatibles avec la SSD de l'huile | Les plastiques bromés, plastiques de DEEE et OMR restent présentés comme flux potentiels | A3-ARRETE-SSD-HUILE-PYROLYSE-2024 | DIFFÉRENT | « Les seuls déchets acceptés en tant qu'intrants dans l'opération de valorisation sont des déchets non dangereux de matières plastiques couverts par un des codes suivants » ; « de déchets d'équipements électriques et électroniques » ; « de déchets pouvant contenir des retardateurs de flamme bromés » | Arrêté du 19 février 2024, annexe I, points 1.1 et 1.3 | Pour la voie française de SSD citée, les DEEE et déchets pouvant contenir des retardateurs bromés sont exclus. Le code OMR 20 03 01 est absent de la liste fermée, contrairement au code 20 01 39 des plastiques collectés séparément. |
| 18 | 8.5 | Grandpuits, démarrage et capacité | Mars 2026 ; 15 000 t/an | RP2-032 | CONFIRMÉ | « d'une capacité de 15 000 tonnes par an » | Communiqué TotalEnergies du 19 mars 2026 | Capacité annoncée par l'exploitant. |
| 19 | 8.5 | Propriété de Grandpuits | TotalEnergies détient 100 % | A8-CST-TTE-RACHAT-2026 | CONFIRMÉ | « TotalEnergies has acquired Plastic Energy's 35% stake [...] becoming the sole owner » | TotalEnergies, 11 septembre 2026 | Situation actuelle confirmée par l'entreprise. |
| 20 | 8.5 | Administration du partenaire technologique | 27 avril 2026 | A8-CST-GAZETTE-PE-2026 | CONFIRMÉ | « PLASTIC ENERGY FINCO LTD | 27 April 2026 | CR-2026-003217 » | The Gazette, avis n° 5124202 | Le partenaire est bien entré en administration au Royaume-Uni. |
| 21 | 8.5 | Projet Eastman | Plus de 110 000 t/an en phase 1 ; projet en pause | A8-CST-EASTMAN-2026 | CONFIRMÉ | « planning for the project is temporarily paused » ; « more than 110,000 metric tons annually » | Page projet Eastman France | Flux polyester, différent des polyoléfines visées par pyrolyse. |
| 22 | 8.5 | Fermeture de trois sites Viridor/Quantafuel | Oslo, Skive et Malmö, fin juin 2026 | A8-CST-VIRIDOR-2026 | CONFIRMÉ | « Demand for recycled material has weakened, while cheaper virgin materials continue to undercut recycled alternatives » ; « completed by the end of June 2026 » | Communiqué Viridor du 26 juin 2026 | Motif correctement attribué à Viridor. |
| 23 | 8.5 | Spécification des balles cotées | Polyoléfines au moins 86 % ; PVC au plus 1 % | RP2-062 | CONFIRMÉ | « sorted, washed and shredded mixed plastic waste in Northwest Europe » ; spécification « polyolefins 86 % min ; PVC 1 % max » | Note méthodologique S&P Global Platts, tableau de spécification | Il s'agit d'une matière préparée de qualité, pas de déchets bruts. |
| 24 | 8.5 | Saturation de l'incinération francilienne | 93 % de la capacité technique | A8-CST-ORDIF-UIDND-2023 | CONFIRMÉ | « 93% de la capacité technique des fours » | Rapport ORDIF, p. 7 | La formule « nearly saturated » est raisonnable à cette échelle. |
| 25 | 8.7 | Estimations nationales des refus de tri | 800 000 t ; 750 000 t ; 496 kt | CITEO-CAHIER-CS-2024 ; OCAPEM-2025 ; A8-MENB-DGPR-COUTSREF-2026 | CONFIRMÉ | « 800 000 tonnes de refus » ; « TOTAL 750 000 t » ; « Refus de tri 496 kt » | Cahier Citeo ; OCAPEM p. 7 ; modèle de coûts public | L'annexe les présente bien comme estimations contradictoires, sans les fusionner. |
| 26 | 8.7 | Seuil HBCDD | 1 000 mg/kg initialement ; 500 mg/kg après modification ; 200 mg/kg seulement après réexamen éventuel | Règlement (UE) 2019/1021 ; règlement (UE) 2022/2400 | CONFIRMÉ | « Hexabromocyclododecane [...] 500 mg/kg » ; « where appropriate [...] not higher than 200 mg/kg » | Règlement 2022/2400, annexe IV | La valeur de 500 mg/kg est confirmée par le texte primaire. 200 mg/kg n'est pas automatique. |
| 27 | 8.7 | Taux France 2022 selon deux sources | 25,2 % et 25,4 % | STRAT3R-2025 ; EUROSTAT-WASPAC | CONFIRMÉ | « 25,2 % » ; `RCY PC 2022: 25.4` | Rapport gouvernemental ; API Eurostat `env_waspac` | Le conflit est réel et correctement signalé. |
| 28 | 8.8 | Liste des points ouverts | Essais sur plusieurs flux, brome, forme physique et prix | R-001 à R-044 | CONFIRMÉ | « Tests on PET, PVC, textiles, rejects, multilayer, electronic plastics, foams » ; « Bromine and persistent pollutants » | Tableau 8.8 | Les demandes listées existent, mais deux conditions structurantes manquent. Voir E-1 et E-2. |
| 29 | Contrôle HTML / source | Concordance de l'introduction et des sections 8.4 à 8.8 | Même texte et mêmes valeurs | ANNEX-08-Plastic-Waste-Streams.md | CONFIRMÉ | « Oil 73 % to 81 % » ; « at least 85 % » ; « more than 110,000 t per year » | Markdown et HTML correspondants | Aucun écart HTML / source trouvé. Les erreurs E-1 à E-4 sont présentes dans les deux versions. |

## Prix et coûts exclus du contrôle chiffré

Les prix de 249 EUR/t, 55 EUR/t, 188 EUR/t, 100 EUR/t et les autres valeurs commerciales de 8.6 n'ont pas été recalculés. L'annexe indique qu'ils sont modifiables ou issus d'hypothèses du sponsor. Avant décision, chaque flux doit être confirmé par une offre ou un contrat précisant qualité, humidité, contaminants, conditionnement, transport, volume garanti et statut juridique de l'huile produite.

Le calcul de hausse de 18,6 EUR/t est une addition correcte de 9,5, 2,9 et 6,2. Il reste exclu du contrôle économique, car ses entrées sont des indices de prix et non des mesures techniques ou des taux légaux.

## Écarts

### E-1 - La voie française de SSD exclut plusieurs flux envisagés

- Annexe : les plastiques électroniques triés et les plastiques bromés restent présentés comme flux potentiels à tester, avec l'hypothèse que le brome serait éliminé comme le chlore.
- Texte en vigueur : l'annexe I, point 1.3 de l'arrêté du 19 février 2024 exige que le lot entrant soit exempt de DEEE et de déchets pouvant contenir des retardateurs de flamme bromés. Le point 1.1 fixe en outre une liste fermée de codes déchets qui n'inclut pas les OMR 20 03 01.
- Gravité : IMPORTANT.
- Effet : une huile issue de ces flux ne peut pas bénéficier de la SSD citée sur la seule base d'une purification réussie. Elle pourrait rester un déchet combustible dans une installation autorisée, sous réserve de son acceptation et de son permis.
- Correction proposée : distinguer clairement les flux admissibles à la SSD des flux seulement envisageables pour une production de combustible sous statut de déchet.

### E-2 - Les rendements viennent d'essais en lots, pas de l'URC-2000 continue

- Annexe : le tableau 8.4 indique que PE, PP et PS ont été testés « on Urban Rig equipment », sans préciser l'échelle ni le régime.
- Source : essais sur une unité discontinue, lots de 20 à 60 kg. L'annexe 2 précise que l'URC-2000 continue n'est couverte que par des spécifications constructeur et demande une garantie de performance sur le mélange cible.
- Gravité : IMPORTANT.
- Effet : les rendements de 55 % à 81 % sont valides pour les essais, mais leur transposition à 51 100 t/an n'est pas démontrée. Cela touche directement le rendement du modèle, sans prouver que le projet est infaisable.
- Correction proposée : ajouter « essais discontinus de 20 à 60 kg » dans 8.4 et inscrire explicitement la garantie de performance continue dans 8.8.

### E-3 - La moyenne UE 2023 a été révisée

- Annexe : 41,7 %.
- Source Eurostat actuelle : 41,6 %.
- Gravité : MINEUR.
- Effet : écart de 0,1 point, aucun effet sur la décision.
- Correction proposée : remplacer 41,7 % par 41,6 % et dater la mise à jour.

### E-4 - Dernière décimale fausse dans CALC-A8-EMB-RECY-HORS-FRANCE

- Calcul enregistré : 49,1695 %.
- Recalcul : 49,169405 %, soit 49,1694 % à quatre décimales.
- Gravité : MINEUR.
- Effet : aucun sur le message « environ 49 % ».
- Correction proposée : corriger le résultat enregistré, sans changer le texte arrondi.

## Les cinq erreurs les plus graves

Seulement quatre écarts ont été retenus. Il n'existe pas de cinquième erreur suffisamment étayée à ajouter.

1. E-1 : exclusion réglementaire des DEEE et déchets pouvant contenir des retardateurs bromés, et absence des OMR 20 03 01 dans la liste d'intrants de la SSD citée.
2. E-2 : extrapolation non signalée d'essais discontinus de 20 à 60 kg vers une installation continue de 51 100 t/an.
3. E-3 : moyenne UE 2023 périmée de 0,1 point.
4. E-4 : dernière décimale fausse dans le calcul de la part recyclée hors de France.

## Autres interprétations utiles

1. **L'exclusion de la SSD n'interdit pas nécessairement toute pyrolyse.** Elle interdit la sortie du statut de déchet par l'arrêté cité. Une valorisation comme combustible sous statut de déchet peut rester possible dans une installation autorisée, mais elle doit être contractuellement et réglementairement confirmée.

2. **Le seuil de 500 ppm ne suffit pas à lui seul.** La SSD exige aussi un intrant admissible, un contrat avec une installation pétrochimique, des spécifications définies après essais, des contrôles par lot et les autres limites de composition.

3. **Les mesures de chlore ne démontrent pas la performance de la couche URC-2000.** Les deux huiles ont été analysées après une étape catalytique sur l'unité d'essai. Le rapport ne prouve pas que cette étape est identique à la couche annoncée pour l'URC-2000 continue.

4. **Les flux propres sont déjà concurrencés.** Les balles cotées exigent au moins 86 % de polyoléfines et au plus 1 % de PVC. Elles sont triées, lavées et broyées et ne représentent pas un flux brut payé pour être traité.

5. **Les fermetures concurrentes ne prouvent pas la rentabilité du projet.** Elles réduisent une partie de la concurrence, mais signalent aussi une demande faible et la concurrence du plastique vierge.

6. **Le gisement théorique reste très supérieur au besoin d'une unité.** Les deux écarts importants concernent surtout la qualité admissible, le débouché de l'huile et la garantie de rendement, pas l'existence physique de 51 100 t/an de plastiques en France.

## Conclusion en langage simple

**POSSIBLE SOUS CONDITIONS.** Les statistiques principales, les essais PE/PP/PS, les analyses de chlore et les faits de concurrence sont pour l'essentiel confirmés. Les deux calculs de prix nul sont corrects. Les prix restent des hypothèses ou données commerciales à confirmer.

**Aucun point bloquant démontré. Deux écarts importants.** Premièrement, les DEEE et déchets pouvant contenir des retardateurs bromés ne peuvent pas alimenter la voie de SSD de l'huile décrite par l'arrêté cité. Deuxièmement, les rendements proviennent d'essais discontinus de 20 à 60 kg et ne constituent pas une garantie de performance de l'URC-2000 continue.

Avant une décision d'investissement, il faut donc choisir un mélange cible admissible, obtenir une garantie constructeur sur l'unité continue, analyser chlore, brome, POP, humidité, cendres et métaux, puis sécuriser un acheteur acceptant l'huile sous le statut juridique réellement atteignable.

## Ce qui n'a pas été vérifié, et pourquoi

- Tous les prix, tarifs, coûts, droits d'entrée et valeurs par défaut : exclus du contrôle chiffré par les règles légères ; offres et contrats requis.
- Rendement de l'URC-2000 continue sur le mélange cible : aucune mesure indépendante disponible dans le dossier.
- Efficacité réelle de déchloration et de débromation de l'URC-2000 : aucune mesure entrée-sortie représentative fournie.
- Conformité d'une huile future à tous les critères SSD : dépend du mélange réel, des analyses par lot, de la purification et du contrat pétrochimique.
- Disponibilité contractuelle de 51 100 t/an : les statistiques prouvent un gisement physique, pas l'accès commercial.
- Acceptation d'une huile restant déchet comme combustible : permis de l'installation réceptrice et contrat non fournis.

## Décompte

| Verdict | Nombre |
|---|---:|
| CONFIRMÉ | 25 |
| DIFFÉRENT | 3 |
| ABSENT | 0 |
| INACCESSIBLE | 0 |
| NON SOURCÉ | 0 |
| CALCUL FAUX | 1 |
| **Total** | **29** |

## Compte rendu Trouvé / Partiel / Non trouvé

| Statut | Élément | Résultat |
|---|---|---|
| Trouvé | Textes réglementaires SSD et POP | Critères, exclusions et seuils relus dans les textes en vigueur. |
| Trouvé | Essais PE, PP, PS et analyse du chlore | Valeurs retrouvées dans les rapports et bulletins de laboratoire. |
| Trouvé | Actualité de Grandpuits, Eastman et Viridor | Capacité, démarrage, propriété, pause et fermetures confirmés. |
| Trouvé | Calculs de prix nul | 164 879 t et 36,9832 %, arithmétique correcte. |
| Partiel | Applicabilité à l'URC-2000 continue | Essais en lots disponibles, garantie continue absente. |
| Partiel | Débouché de l'huile | Critères réglementaires connus, contrat et analyses du produit futur absents. |
| Non trouvé | Essai OneWorld sur le brome | Aucun document OneWorld fourni, comme l'indique l'annexe. |
