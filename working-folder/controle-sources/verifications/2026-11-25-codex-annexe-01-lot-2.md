# Contre-vérification indépendante de l'annexe 1, lot 2

Date : 25 novembre 2026  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-01-html/index.html` et fiches liées  
Périmètre : sections 1.4 à 1.6 et cohérence d'ensemble avec l'annexe 2  
Accès internet : OUI  
Lecture des PDF : OUI, texte extrait et pages scannées contrôlées visuellement lorsque nécessaire

## Conclusion courte

Le lot 2 **passe sous conditions comme description prudente du procédé et des données de conception OneWorld**. Les contradictions importantes sur le tri, l'électricité et les délais sont visibles et l'annexe retient généralement la bonne prudence. Il n'y a pas de nouveau point bloquant démontrant que le procédé ne peut pas fonctionner.

En revanche, trois conclusions ne passent pas en l'état : la conformité des dioxines aux valeurs UE sans correction à 11 % d'oxygène, l'autonomie thermique calculée avec 11,5 % de « recovery loss » assimilé à du gaz, et la présentation de l'ancien article 42 de la directive IED comme droit actuel. La dernière ne change pas encore l'hypothèse prudente du modèle, car Urban Rig ne démontre pas les conditions de l'exemption actuelle.

Le point bloquant d'ensemble reste celui du lot 1 : la performance d'une ligne continue de 200 t/j n'est pas démontrée par les essais en lots. Avant décision d'investissement, il faut une référence continue représentative ou des garanties contractuelles de capacité, disponibilité, rendements, consommations et émissions.

## Tableau des vérifications

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---:|---|---|---|---|---|---|---|---|
| 1 | 1.4.1 | Pas de tri ni nettoyage avant chargement, après un jour de stockage | Déclaration qualitative | OW-ENG-P14-P15-PROCEDE | CONFIRMÉ | « URBAN RIG does not require to sort waste for processing » ; « This machine does not require clean such contamination and able to input after one-day storage to remove moisture. » | Brochure OneWorld anglaise, p. 2 | Nature : constructeur. Cette phrase n'exclut pas un prétraitement intégré à l'installation. |
| 2 | 1.4.1 | Les plans comprennent broyage et tri | Trémie avec broyage ; machine de tri | OW-ENG-P04-P07-SPEC-PLANS ; UR2000-JP-P09-P13-PLANS | CONFIRMÉ | « Input throat (with crushing function) ; Sorting machine » | Brochure OneWorld anglaise, p. 4 ; brochure japonaise, p. 9 et 10 | Nature : constructeur. L'annexe signale correctement la tension avec l'affirmation « sans tri ». |
| 3 | 1.4.1 | Matières effectivement testées | PE, PP, PS, deux flux municipaux, mélange avec PVC et FRP, pneus, résidu de broyage | CHIBA-ESSAIS-FICHES ; OWJ-DEMO-2021 ; OWT-DEMO-2020 | CONFIRMÉ | « 油化率 » avec séries PE, PP, PS et 3P ; « 中にはFRP素材と見られるガラス繊維も混在されていた。 » ; « The weight of each component after pyrolysis was 111 kg of wire, 133 kg of charcoal, and approximately 180 L of oil. » | Rapport Chiba, PDF p. 19 à 29 ; démonstration 2021, p. 5 et 8 ; essai pneus 2020, p. 3 | Portée correctement limitée aux unités et charges décrites. |
| 4 | 1.4.1 | Le PVC s'est arrêté au stade de la fusion | Constat qualitatif | OWJ-DEMO-2021 | CONFIRMÉ | « 塩ビに関しては融点で止まっている » | Rapport OneWorld de démonstration URT-10, p. 8 | Nature : constructeur. Cela ne valide pas l'acceptation durable d'un flux riche en PVC. |
| 5 | 1.4.1 | « Not yet tested » pour déchets ménagers bruts, papier, bois, aliments, textiles et PET | Aucun essai | Aucun renvoi sur cette phrase | NON SOURCÉ | Aucun document cité ne dit que OneWorld n'a jamais réalisé ces essais. | HTML, section 1.4.1 | La conclusion prudente est : « aucun essai de ces flux n'a été trouvé dans le dossier lu ». |
| 6 | 1.4.2 | Dioxines 2023 | 0,011 et 0,025 ng-TEQ/m3 | DIOXINES-2023 | CONFIRMÉ | « 排ガス(9/26) 0.1 0.011 基準値以下 ; 排ガス(9/27) 0.1 0.025 基準値以下 » | Rapport préliminaire Kankyo Kogai Bunseki Center, p. 1 | Mesures tierces, mais machine, charge et oxygène de référence non indiqués. |
| 7 | 1.4.2 | Dioxines 2022 | 0,067 ng-TEQ/m3 | CHIBA-OOSUMI-FUMEES | CONFIRMÉ | « ダイオキシン類（毒性等量） ng-TEQ/m³ 0.067 » | Rapport provisoire Oosumi, PDF p. 56, imprimé p. 50 | Mesure tierce, sans oxygène de référence indiqué. |
| 8 | 1.4.2 | Toutes les valeurs sont sous la limite UE | 0,1 ng/Nm3 | IED-2010-75-ANX6-P3 | DIFFÉRENT | « They are standardised at 11 % oxygen in waste gas » ; « Dioxins and furans 0,1 » | Directive 2010/75/UE, annexe VI, partie 3, points 1 et 1.4 | Les nombres bruts sont inférieurs à 0,1, mais la conformité ne peut pas être conclue sans correction à 11 % O2. |
| 9 | 1.4.2 | Les valeurs 2023 sont dans la plage MTD des installations nouvelles | 0,01 à 0,04 ng I-TEQ/Nm3 | BAT-WI-2019-2010 | DIFFÉRENT | « BAT-AEL (ng I-TEQ/Nm3) 0,01-0,04 » et conditions de référence « 11 vol-% » | Décision d'exécution (UE) 2019/2010, considérations générales et tableau MTD 30 | Possible pour une teneur en O2 assez basse, non démontré par le rapport 2023. L'annexe 2 reproduit la même conclusion trop forte. |
| 10 | 1.4.2 | OneWorld explique l'absence de dioxines par l'absence d'oxygène | Déclaration qualitative | OW-ENG-P02-P14-AFFIRMATIONS | CONFIRMÉ | « It is not necessary for fuel for operation except initial startup. ; Dioxin and CO₂ are not generated. » | Brochure OneWorld anglaise, p. 2 | Nature : constructeur. L'annexe distingue correctement le réacteur et les fumées de combustion. |
| 11 | 1.4.2 | PRIMO est une option de traitement des fumées | DeNOx, DeSOx, poussières, odeurs | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « OPTION PRIMO / Exhaust Gas Purification Facility » ; « Nox decomposition ; Sox decomposition ; Dust removal ; Odor removal » | Brochure OneWorld anglaise, p. 12 | Nature : constructeur. La performance requise en France n'est pas garantie dans ce document. |
| 12 | 1.4 à 1.6 | SEA CORAL n'est pas décrit parmi les options ou points ouverts | Option absente du texte principal | OW-ENG-P13-SEACORAL ; SEACORAL-DETAIL-ENG | ABSENT | « OPTION SEA CORAL / Specialized ceramic purifier » | Brochure OneWorld anglaise, p. 13 | Omission importante. L'annexe 2 précise qu'aucun essai sur l'eau de procédé Urban Rig n'est fourni et que la saumure reste à gérer. |
| 13 | 1.4 à 1.6 | FORCE 9 n'est pas décrit parmi les options ou points ouverts | Option absente du texte principal | OW-ENG-P03-P19-GAMME-DELAIS | ABSENT | « FORCE 9 / FIA CR-09 Far infrared catalytic reduction facility » ; « made for the stabilization of carbide residue » | Brochure OneWorld anglaise, p. 11 | Omission importante pour définir la configuration, le traitement du char et le CAPEX, sans preuve que cette option soit nécessaire au cas standard. |
| 14 | 1.4.3 | Séparation des huiles selon la température et par électrovanne | Gazole et huile lourde ; plusieurs coupes | OW-ENG-P14-P15-PROCEDE ; UR2000-JP-P08-SPEC | CONFIRMÉ | « Segregate gas-oil and heavy-oil by the temperature difference of vaporized gas through a solenoid valve. » | Brochure OneWorld anglaise, p. 14 et 15 | Nature : constructeur. Les quantités et qualités de chaque coupe continue ne sont pas mesurées. |
| 15 | 1.4.4 | Pilotage par micro-ordinateur, vannes et capteurs | Automatisation déclarée | OW-ENG-P04-P07-SPEC-PLANS | CONFIRMÉ | « Control System microcomputer control ; Safety device Valve & sensor » | Brochure OneWorld anglaise, p. 4 | Nature : constructeur. L'annexe signale correctement l'absence de logique de sécurité, interverrouillages et effectif. |
| 16 | 1.4.5 | Besoin du brûleur sur la base constructeur | 1 506,65 MJ/t | CALC-A2-BRULEUR-MJ-T | CONFIRMÉ | 833 kcal/s x 86 400 s/j x 4,1868 kJ/kcal / 1 000 / 200 t/j = 1 506,65 MJ/t | Brochure OneWorld japonaise, p. 4 ; recalcul | Arithmétique exacte. Le 833 kcal/s et le débit de 200 t/j sont des données constructeur. |
| 17 | 1.4.5 | Couverture par le gaz du cas riche en résines | 2,9 fois avec 11,5 % de gaz | CALC-A2-COUV-BRULEUR-RESINE ; OW-ENG-P16-BILAN | CALCUL FAUX | « Recovery Loss 11.5 % [...] Mainly discharged as flue gas; a very small amount will be carbide. » | Brochure OneWorld anglaise, p. 16 | Le ratio arithmétique est exact, mais 11,5 % n'est ni une mesure de gaz, ni clairement une fraction massique de l'entrée. Le qualifier de « gas » change la conclusion d'autonomie. |
| 18 | 1.4.5 | Couverture sur plastique pur sous hypothèse de 15 % de gaz | 3,7 fois | CALC-A2-COUV-BRULEUR-PLASTIQUE15 ; D-038 | CONFIRMÉ | 5 607,92 / 1 506,65 = 3,7221 | Calculs.yaml, CALC-A2-COUV-BRULEUR-PLASTIQUE15 | Exact sous l'hypothèse déclarée de 15 %. Ce n'est pas une mesure sur l'URC-2000 continu. |
| 19 | 1.4.5 | Pas de combustible après démarrage | Déclaration OneWorld | OW-ENG-P02-P14-AFFIRMATIONS | CONFIRMÉ | « It is not necessary for fuel for operation except initial startup. » | Brochure OneWorld anglaise, p. 2 | Nature : constructeur. L'annexe limite correctement cette lecture aux charges riches en résines et ne l'étend pas aux déchets ménagers. |
| 20 | 1.4.5 | Consommation électrique URC-2000 | 600 « kW/h » | OW-CONSO-ENERGIE | CONFIRMÉ | « 200t ; 10,000L/day(200t) ; 600kW/h ; 56,800kW/day(200t) » | Tableau OneWorld « UR Energy Consumption », p. 1 | Nature : constructeur. Les unités imprimées sont fautives, mais 600 est bien la valeur du tableau. |
| 21 | 1.4.5 | Electricité par tonne | 259,2 MJ/t | CALC-A2-ELEC-MJ-T | CONFIRMÉ | 600 kW x 24 h/j x 3,6 MJ/kWh / 200 t/j = 259,2 MJ/t | Calculs.yaml, CALC-A2-ELEC-MJ-T | Calcul exact si 600 kW est une puissance continue et si 200 t/j sont effectivement traitées. |
| 22 | 1.4.5 | La brochure donne une autre consommation | 20 « kw/h » | UR2000-JP-P08-SPEC | CONFIRMÉ | « 消費電力 ( 連続時 ) 20kw/h » | Brochure URC-2000 japonaise, p. 8 | Nature : constructeur. La contradiction 20 contre 600 est explicitement signalée. Le modèle doit retenir 600 kW jusqu'à garantie contractuelle. |
| 23 | 1.4.5 | Les essais Noda ont utilisé du gazole et un générateur | 61 à 76 L de gazole ; 59 à 65 kWh | CHIBA-BILANS | CONFIRMÉ | « 電力 65kwh ; 軽油 66ℓ » | Rapport Chiba, PDF p. 41 et 42 | Essais en lots, non transposables directement au continu, comme le dit l'annexe. |
| 24 | 1.4.6 | Modularité de l'URC-2000 | 7 unités d'environ 12 t ; transport en 7 parties | UR2000-JP-P06-P07-MODULES | CONFIRMÉ | « 本機処理プラント (200T) は 7 ユニットで構成。 » ; « 処理機本体を７分割しトラック搬送して現地組立方式を採用。 » | Brochure URC-2000 japonaise, p. 6 | Nature : constructeur. |
| 25 | 1.4.6 | Une installation de 1 000 t/j utilise cinq lignes | 5 x URC-2000 | UR2000-JP-P09-P13-PLANS | CONFIRMÉ | Plan « 1000t/day » composé de cinq ensembles URC-2000 | Brochure URC-2000 japonaise, p. 10 | Nature : constructeur, plan d'implantation et non preuve de fonctionnement. |
| 26 | 1.4.6 | Délais contradictoires | Environ 10 mois ; 4 mois | OW-ENG-P03-P19-GAMME-DELAIS ; UR2000-JP-P09-P13-PLANS | CONFIRMÉ | « Continuous type = about 10 months » ; calendrier du contrat à l'essai de fonctionnement sur 4 mois | Brochure anglaise, p. 19 ; brochure japonaise, p. 13 | L'annexe signale correctement la contradiction. Retenir au minimum 10 mois, puis ajouter autorisations, génie civil, transport et réception. |
| 27 | 1.4.6 | Installation et maintenance | 30 jours ; 3 jours tous les 3 mois | OW-TRANSPORT-INSTALLATION | CONFIRMÉ | « Days needed for installation onsite » avec 30 pour 200t ; « 3 months operation + 3 days maintenance » | Tableau OneWorld « Transportation, Installation and Maintenance », p. 1 | Nature : constructeur. Document sans auteur ni date imprimés. |
| 28 | 1.4.6 | Logistique de 100 conteneurs de 40 pieds non mentionnée | 100 conteneurs pour 200 t | OW-TRANSPORT-INSTALLATION | ABSENT | « How many 40' containers for shipment » avec valeur « 100 » sous 200t | Tableau OneWorld « Transportation, Installation and Maintenance », p. 1 | Peut coexister avec les sept grands modules, les conteneurs couvrant les auxiliaires et sous-ensembles. A confirmer par une liste de colisage. |
| 29 | 1.4.7 | Produits présentés comme vendables | Char, huile légère, huile mixte, off-gas | IGES-AEPW-PROPOSITION | CONFIRMÉ | « URBAN RIG can make a profit by recovering salable resources (carbide, light oil, mixed oil, off-gas). » | Proposition IGES/AEPW fondée sur la technologie OneWorld, p. 4 | Nature : constructeur ou proposition utilisant ses données. Ce n'est pas une preuve de prix, qualité ou débouché. |
| 30 | 1.5 | Hiérarchie des déchets et exclusion des combustibles du recyclage | Prévention, réemploi, recyclage, autre valorisation, élimination | WFD-2008-98-ART3-4 | CONFIRMÉ | « prevention ; preparing for re-use ; recycling ; other recovery, e.g. energy recovery ; disposal » ; « does not include energy recovery and the reprocessing into materials that are to be used as fuels » | Directive 2008/98/CE consolidée au 16 octobre 2025, art. 3(17) et 4(1) | Le texte actuel confirme la substance de la fiche, même si la fiche cite une consolidation de 2018. |
| 31 | 1.5 | Une huile vendue comme matière première compterait automatiquement comme recyclage | Recyclage | WFD-2008-98-ART3-4 | DIFFÉRENT | « enters the recycling operation whereby waste materials are actually reprocessed into products, materials or substances » | Directive 2008/98/CE consolidée au 16 octobre 2025, art. 11a(1)(c) | La vente comme matière première ne suffit pas. Il faut une re-transformation effective en produit, matière ou substance, avec règles de comptage et de statut applicables. |
| 32 | 1.5 | Les vapocraqueurs acceptent environ 3 ppm de chlore | 3 ppm | KUSENBERG-AICHE-2021 | DIFFÉRENT | « Overview of typical heteroatom specifications for fossil-based steam cracker feedstocks » ; « Chlorine 3 ppm » | Kusenberg et al., PDF p. 8, tableau 2 | Le chiffre est confirmé comme spécification industrielle typique de charges fossiles, pas comme seuil universel de tous les vapocraqueurs. L'écart avec 1 370 et 5 260 ppm reste toutefois d'un ordre de grandeur décisif. |
| 33 | 1.5 | Exemption IED décrite avec le texte ancien | Gaz rendu non-déchet et émissions au plus égales au gaz naturel | IED-2010-75-ART3-42 | DIFFÉRENT | « if the gases or liquids resulting from such thermal treatment of waste are treated prior to their incineration » ; critères d'émissions aux points (a) et (b) | Directive (UE) 2024/1785, art. 1(35), remplaçant l'art. 42(1), second alinéa | La fiche utilise le texte de 2010. Depuis 2024, l'exemption vise gaz ou liquides traités avant combustion et applique deux critères d'émissions différents. Faute de preuve de traitement et d'émissions, le modèle peut néanmoins conserver par prudence le classement incinération. |
| 34 | 1.5 | Le JRC préfère le recyclage à la valorisation énergétique et ne classe pas clairement mécanique contre chimique | Conclusion générale présentée sans restriction | JRC-2023-PLASTIC-RECYCLING | DIFFÉRENT | « Recycling (mechanical, physical or chemical) is preferable to energy recovery in all pathways analysed » ; « For some categories however [...] energy recovery can perform better » ; « a clear ranking could not be established » | JRC132067, PDF p. 9, page imprimée 4, Executive summary | La première phrase est placée sous « Climate Change ». L'annexe omet que, pour certaines autres catégories d'impact, la valorisation énergétique peut être meilleure. L'absence de classement clair mécanique contre chimique est bien confirmée. |
| 35 | Cohérence annexe 2, énergie | Même rendement et même bilan énergétique repris | 76,5 %, 11,5 %, 2,9, 3,7, 600 kW | Annexe 2, sections 2.6 et 2.8 | CONFIRMÉ | « 2.9 times on OneWorld's resin-rich design (11.5 % gas) and 3.7 times with 15 % gas » | Annexe 2 HTML, sections 2.6.2 et 2.8 | Cohérence formelle confirmée. Elle reproduit toutefois les erreurs de portée sur 76,5 % et 11,5 % déjà relevées. |
| 36 | Cohérence annexe 2, émissions | Même lecture des dioxines et même réserve sur O2 | Valeurs 2022 et 2023 | Annexe 2, section 2.7 | CONFIRMÉ | « 2022 and 2023 campaigns: oxygen was not reported » ; « The 2023 dioxin results [...] are within the BAT range » | Annexe 2 HTML, section 2.7.2 | Pas de contradiction entre annexes, mais contradiction logique interne : l'oxygène manque alors que la conclusion MTD exige une valeur normalisée à 11 % O2. |
| 37 | Contrôle HTML / source | Concordance HTML et Markdown du lot 2 | Même texte et mêmes valeurs | ANNEX-01-Process-and-Technology.md | CONFIRMÉ | « 600 kW for a 200 t plant » ; « about 10 months [...] or 4 months » ; « would count as recycling » | Markdown, sections 1.4 à 1.6 ; HTML du lot 2 | Aucun écart HTML / source Markdown trouvé. Les écarts sont présents dans les deux versions. |

## Écarts

### E-1. Preuve de la ligne continue de 200 t/j toujours absente

- Annexe : les performances et consommations servent à décrire l'URC-2000 continu.
- Source : les mesures de rendement et les bilans détaillés proviennent d'unités en lots ; les données du continu sont des données de conception OneWorld.
- Gravité : **BLOQUANT** avant décision d'investissement ou engagement irréversible, comme au lot 1. Ce n'est pas une preuve d'impossibilité technique.
- Correction proposée : référence continue représentative, essai de réception ou garanties contractuelles sur débit, disponibilité, rendements, consommations et émissions.

### E-2. Dioxines et valeurs MTD sans correction à 11 % O2

- Annexe : toutes les valeurs sont dites sous 0,1 ng/Nm3 et les valeurs 2023 dans la plage MTD de 0,01 à 0,04.
- Source : les seuils UE sont à 11 % O2, alors que les rapports 2022 et 2023 ne donnent pas l'oxygène.
- Gravité : **IMPORTANT**. Les valeurs sont basses, mais la conformité n'est pas démontrée.
- Correction proposée : « valeurs brutes inférieures numériquement aux seuils ; conformité possible sous réserve d'un rapport final à 11 % O2 ».

### E-3. Autonomie thermique fondée sur 11,5 % de « recovery loss »

- Annexe : le gaz couvrirait 2,9 fois le besoin du brûleur.
- Source : 11,5 % est une ligne de perte de récupération d'une table incohérente, non une mesure du gaz récupérable.
- Gravité : **IMPORTANT**. L'ordre de grandeur peut rester plausible, mais la conclusion d'autonomie n'est pas démontrée.
- Correction proposée : traiter 2,9 comme scénario non validé et demander quantité de gaz, PCI, routage, pertes et consommation auxiliaire sur le continu.

### E-4. Fiche IED obsolète depuis la modification de 2024

- Annexe : l'exemption repose sur un gaz devenu non-déchet et des émissions ne dépassant pas le gaz naturel.
- Source actuelle : l'article 42 vise désormais les gaz ou liquides traités avant leur combustion et deux critères d'émissions différents.
- Gravité : **IMPORTANT**. La qualification réglementaire peut influer sur permis, CAPEX et calendrier. L'hypothèse prudente d'incinération reste défendable faute de preuve d'exemption.
- Correction proposée : remplacer la fiche par la version consolidée 2024, puis faire valider le classement français actuel par le conseil réglementaire de l'annexe 4.

### E-5. SEA CORAL et FORCE 9 omis de la configuration

- Annexe : PRIMO est décrit, mais SEA CORAL et FORCE 9 ne le sont pas.
- Source : OneWorld présente SEA CORAL comme option de traitement d'eau et FORCE 9 comme traitement de stabilisation du résidu carboné.
- Gravité : **IMPORTANT** pour définir le périmètre fourni, le CAPEX, les effluents et les résidus. Aucun document ne prouve que ces options soient obligatoires dans un cas standard.
- Correction proposée : ajouter une courte ligne pour chaque option, avec statut « proposée par OneWorld, nécessité et performance non établies », et renvoyer aux essais requis.

### E-6. Logistique de 100 conteneurs absente

- Annexe : sept parties transportées par camion, 30 jours d'installation.
- Source : un autre tableau OneWorld indique 100 conteneurs de 40 pieds pour le modèle 200 t.
- Gravité : **IMPORTANT** pour transport, levage, stockage, douane et planning.
- Correction proposée : demander une liste de colisage et retenir 100 conteneurs pour le chiffrage prudent tant que la contradiction n'est pas levée.

### E-7. Comparaison JRC trop générale

- Annexe : le recyclage est présenté comme préférable à la valorisation énergétique dans toutes les voies analysées.
- Source : cette conclusion est formulée pour le changement climatique ; le rapport dit que la valorisation énergétique peut être meilleure pour certaines autres catégories.
- Gravité : **MINEUR** pour la technologie, **IMPORTANT** pour un argument environnemental ou commercial.
- Correction proposée : limiter la phrase au changement climatique et conserver la conclusion d'absence de classement clair entre recyclage mécanique et chimique.

### E-8. Vente comme matière première assimilée trop vite au recyclage

- Annexe : une huile vendue à un vapocraqueur « compterait » comme recyclage.
- Source : la directive exige une re-transformation effective en produits, matières ou substances ; la simple vente ne suffit pas.
- Gravité : **IMPORTANT** si le statut de recyclage est utilisé dans le modèle, les contrats publics ou la communication.
- Correction proposée : écrire « pourrait compter comme recyclage si elle est effectivement retransformée en matière et si les règles de statut et de comptage sont satisfaites ».

## Autres interprétations

- **Sans tri contre broyeur et machine de tri.** Les deux affirmations peuvent coexister : l'exploitant peut accepter un flux mélangé sans tri manuel préalable, tandis que l'installation réalise broyage et séparation en ligne. La lecture prudente est de budgéter le prétraitement montré sur les plans jusqu'à garantie écrite de OneWorld.
- **20 kW contre 600 kW.** Les unités « kW/h » sont incorrectes et les périmètres peuvent différer, par exemple commande seule contre auxiliaires de l'usine. Aucun document ne l'explique. Le cas prudent et l'ordre de grandeur industriel sont 600 kW continus, à remplacer uniquement par une consommation garantie.
- **10 mois contre 4 mois.** Le calendrier de quatre mois peut viser une ancienne configuration, une étape partielle ou un projet avec fabrication anticipée. Sans explication, il ne faut pas l'utiliser. Retenir au minimum dix mois de fabrication, hors autorisations, génie civil, transport et réception.
- **Sept parties contre 100 conteneurs.** Les sept parties peuvent être les grands modules, les 100 conteneurs incluant auxiliaires, structures et équipements de site. Ce n'est donc pas forcément une contradiction, mais l'ordre de grandeur logistique doit être confirmé.
- **Dioxines.** Les résultats peuvent rester sous les limites après correction si l'oxygène est assez bas. Pour la valeur 2023 de 0,025, rester sous 0,1 exige environ 18,5 % O2 ou moins ; rester sous 0,04 exige environ 14,75 % O2 ou moins. La conclusion correcte est « possible sous conditions ».
- **Article 42 IED.** Le texte actuel ouvre une exemption différente, y compris pour les liquides traités, mais Urban Rig ne fournit ni preuve de traitement répondant aux critères ni comparaison d'émissions. L'hypothèse d'une installation relevant du régime incinération reste donc la plus prudente pour le modèle.
- **Vente des huiles.** OneWorld les qualifie de vendables, mais les mesures de chlore et la fraction lourde montrent qu'un débouché matière exige probablement un traitement. Un débouché combustible est plus simple conceptuellement, mais relève de la valorisation énergétique et de contraintes de qualité propres au combustible.
- **SEA CORAL et FORCE 9.** Leur omission ne signifie pas qu'ils sont nécessaires. SEA CORAL n'est documenté que sur eau de mer et FORCE 9 par des affirmations constructeur. La bonne lecture est de les inscrire comme options à qualifier, pas comme équipements de base validés.
- **JRC.** Le rapport soutient fortement le recyclage sur le critère climat, mais ne permet ni de conclure qu'Urban Rig est du recyclage ni de le préférer à toute autre voie sans connaître la destination réelle des huiles et une ACV propre au projet. La proposition AEPW dit d'ailleurs : « Currently, no LCA data is available for URBAN RIG ».

## Manques évidents pour un investisseur

- **BLOQUANT** : preuve continue représentative ou garanties contractuelles avec essai de réception sur le flux cible.
- **IMPORTANT** : matrice d'acceptation des déchets avec humidité, densité, granulométrie, chlore, inertes, objets interdits et prétraitement requis.
- **IMPORTANT** : schéma complet des gaz et fumées, composition garantie, points de combustion, traitement PRIMO et mesures normalisées à 11 % O2.
- **IMPORTANT** : conception de sécurité, notamment HAZOP, ATEX, détection gaz, soupapes, arrêts d'urgence, interverrouillages, incendie et effectifs.
- **IMPORTANT** : traitement de l'eau de procédé, bilan d'eau, effluent final et filière des concentrats ; SEA CORAL n'est pas validé sur cet effluent.
- **IMPORTANT** : configuration contractuelle des options PRIMO, SEA CORAL et FORCE 9, performances garanties, consommables, maintenance et CAPEX inclus.
- **IMPORTANT** : liste de colisage, levage, stockage, génie civil et planning cohérent avec 100 conteneurs et dix mois de fabrication.
- **IMPORTANT** : spécifications garanties et débouchés des huiles, du char, des métaux et du gaz, avec statut de déchet ou de produit.
- **MINEUR** : ACV comparative propre à Urban Rig. Elle devient importante si l'avantage environnemental est un argument central de financement.

## Conclusion en langage simple

- **Passe** : la description du prétraitement, des options PRIMO, de la séparation des huiles, du pilotage, de la modularité et des contradictions documentaires correspond aux pièces OneWorld, avec une présentation généralement prudente.
- **Ne passe pas** : affirmer une conformité dioxines UE sans 11 % O2, une autonomie thermique démontrée par le scénario à 11,5 %, ou présenter l'ancien article 42 IED comme droit actuel.
- **Possible sous conditions** : fonctionnement sans tri externe, conformité des émissions, autonomie thermique, exemption IED, valorisation matière des huiles et délais de livraison.
- **À mesurer ou confirmer** : performance continue, consommations garanties, traitement des fumées et eaux, qualité des produits, sécurité, liste de colisage et débouchés.

## Ce qui n'a pas été vérifié dans ce lot

- Les montants de revenus, prix de vente, coûts, CAPEX et rentabilité, hors périmètre demandé.
- Le classement ICPE français complet et la transposition nationale détaillée de la directive IED 2024, traités dans l'annexe 4.
- Les contrats d'achat des huiles, du char, des métaux ou du gaz, non fournis dans le dossier lu.
- Les performances de SEA CORAL sur l'eau de procédé Urban Rig et de FORCE 9 sur le char du flux cible, non documentées par des essais pertinents.
- Les rapports finaux 2022 et 2023 avec oxygène de référence, absents du dossier.
- L'ACV Urban Rig, que la proposition AEPW déclare indisponible.

## Décompte

- CONFIRMÉ : 26
- DIFFÉRENT : 6
- ABSENT : 3
- NON SOURCÉ : 1
- CALCUL FAUX : 1
- INACCESSIBLE : 0
- Total : 37 verdicts de fond, dont 2 contrôles de cohérence avec l'annexe 2 et 1 contrôle HTML / Markdown
