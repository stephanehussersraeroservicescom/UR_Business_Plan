# Contre-vérification de l'annexe 9, lot 2

Date : 2026-11-25  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-09-html/index.html` et fiches de preuve liées  
Périmètre : sections 9.6 à 9.11, coûts manquants et lecture d'ensemble  
Accès internet : OUI  
Lecture des PDF : OUI. Les PDF BOAMP, Anaergia, db technologies et Politecnico di Milano ont été ouverts en ligne. Les autres documents originaux ont été ouverts localement ou sur leur page publique.

## Conclusion courte

Le lot 2 **passe sous conditions**.

- Les besoins de pré-traitement, les ordres de grandeur d'équipements et les calculs OREX sont correctement repris.
- Le total de 60 MEUR avant transport est arithmétiquement exact et clairement fondé sur les décisions du porteur.
- En revanche, 60 MEUR ne peut pas encore être présenté comme le besoin de financement complet d'une installation clé en main. Plusieurs postes usuels ne sont ni chiffrés ni explicitement inclus.

Il n'y a pas de blocage technique démontré. Il existe un point bloquant pour arrêter le financement : obtenir une matrice contractuelle des inclusions et exclusions, ajouter une réserve d'aléas et chiffrer les raccordements, utilités, conformité environnementale résiduelle, mise en service et fonds de roulement.

## Tableau des vérifications

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---:|---|---|---|---|---|---|---|---|
| 1 | 9.6 | OneWorld dit sans tri, mais son plan montre broyage et tri | Contradiction affichée | OW-ENG-P04-P07-SPEC-PLANS | CONFIRMÉ | « Input throat (with crushing function) ; Sorting machine » | `Urban RIg ENG　.pdf`, p. 4 | Nature : constructeur. Le périmètre reste à définir par flux. |
| 2 | 9.6 | Fraction non convertible des OMR | 11,79 % | CALC-A5-NONPROC-PCT | CONFIRMÉ | `n / total * 100` | Fiche 5.C.f ; `calculs.yaml` | 11,7944 %, correctement arrondi. Valeur reprise de l'annexe 5. |
| 3 | 9.6 | Eau des OMR | 421 kg/t | CALC-A5-EAU-KG-T | CONFIRMÉ | `(somme des parts x humidités) / 10` | Fiche 5.C.c ; `calculs.yaml` | 421,298 kg/t, correctement arrondi. |
| 4 | 9.6 | Fraction non convertible des DAE en mélange | 23 % | CALC-A7-NONCONV-PCT | CONFIRMÉ | `i + m + p` | Fiche 7.C.l ; `calculs.yaml` | 19 % d'inertes + 3 % de métaux + 1 % de plâtre. |
| 5 | 9.6, fiche 9.L.a | Trommel | 50 000 à 150 000 EUR ; jusqu'à 50 t/h | PRM-HELLOPRO-MACHINES-CDT-2026 | CONFIRMÉ | « Le prix d’un trommel est estimé entre 50 000 et 150 000 euros, avec une capacité allant jusqu’à 50 tonnes par heure. » | Hellopro, rubrique prix d'un trommel | Ordre de grandeur commercial, correctement étiqueté secondaire. |
| 6 | 9.6, fiche 9.L.b | Crible mobile avec maintenance quatre ans | 214 000 EUR | PRM-BOAMP-SMTD65-TROMMEL-2024 | CONFIRMÉ | « fourniture d'un crible rotatif sur châssis 80 km/h avec contrat d'entretien pour 4 ans » ; « Valeur de tous les contrats attribués dans cet avis : 214,000 Euro » | BOAMP, avis 24-96781, LOT-0001, section 6 | Source publique ouverte. Le marché ne donne pas la capacité. |
| 7 | 9.6, fiche 9.L.a | Séparateur magnétique | à partir de 30 000 EUR ; 20 à 50 t/h | PRM-HELLOPRO-MACHINES-CDT-2026 | CONFIRMÉ | « Le prix d’un séparateur magnétique [...] commence à partir de 30 000 euros. [...] Sa capacité va de 20 à 50 tonnes par heure. » | Hellopro, rubrique séparateur magnétique | Ordre de grandeur commercial. |
| 8 | 9.6, fiche 9.L.c | Overband 750 mm | 5 350 EUR HT EXW | PRM-MACHINESEEKER-PUTZ-OVERBAND-2026 | INACCESSIBLE | La page de l'annonce ne s'ouvre plus dans les accès disponibles | URL de la fiche 9.L.c | Petite annonce non recontrôlable. Ne pas utiliser comme devis. |
| 9 | 9.6, fiche 9.L.a | Broyeur | environ 25 000 EUR ; 5 à 20 t/h | PRM-HELLOPRO-MACHINES-CDT-2026 | CONFIRMÉ | « Le prix d’un broyeur de déchets [...] est d’environ 25 000 euros. [...] capacité de 5 à 20 tonnes par heure » | Hellopro, rubrique broyeur | Ordre de grandeur commercial. |
| 10 | 9.6, fiche 9.L.a | Ligne automatique | au moins 500 000 EUR | PRM-HELLOPRO-MACHINES-CDT-2026 | CONFIRMÉ | « Pour une ligne automatique de tri de déchets, il faut prévoir au moins 500 000 euros. » | Hellopro, rubrique prix d'une machine | Ordre de grandeur commercial, pas ligne dimensionnée pour Urban Rig. |
| 11 | 9.6, fiche 9.L.d | Dépoussiérage ATEX | 15 000 à 80 000 EUR | PRM-HELLOPRO-DEPOUSSIEREUR-2026 | CONFIRMÉ | « Dépoussiéreur pour environnement ATEX [...] Entre 15 000 € et 80 000 € » | Hellopro, tableau par secteur, lignes 119 à 128 | Ordre de grandeur commercial. La page affiche désormais novembre 2026, sans changement de fourchette. |
| 12 | 9.6, fiche 5.L.p | Presse OREX 400 | 120 kW ; 9 à 15 t/h | A9-ANAERGIA-OREX400 | CONFIRMÉ | « 120 kW average electric power consumption » ; « 9 to 15 t/h of material threated » | Fiche Anaergia OREX 400, p. 1 | Document commercial fabricant. |
| 13 | 9.6, fiche 9.L.e | Ligne CSR Baudelet | 8,5 MEUR ; 75 000 t/an à partir de 100 000 t/an | PRM-BAUDELET-CSR-2026 | CONFIRMÉ | « mise en service d'une ligne [...] 8,5 millions d'euros » ; « produire 75 000 tonnes de CSR par an à partir de 100 000 tonnes de déchets non dangereux » | La Gazette France, corps de l'article, 21/07/2026 | Benchmark plus large qu'un simple pré-traitement Urban Rig. |
| 14 | 9.6, fiche 5.L.o | Humidité de la fraction sèche OREX | 18 à 20 % | A9-DBTECH-OREX-MSW | CONFIRMÉ | « humidity: 18-20 % » | Présentation db technologies, p. 12 du PDF | Déclaration commerciale. L'entrée présentée ne contient que 25 à 30 % d'eau, contre 42,1 % pour les OMR françaises du plan. Essai requis. |
| 15 | 9.6, fiche 5.C.br | Électricité OREX au débit haut | 8,0 kWh/t | CALC-A9-OREX-KWH-T-BAS | CONFIRMÉ | `p / d` | `calculs.yaml`, 120 kW / 15 t/h | Calcul exact. |
| 16 | 9.6, fiche 5.C.bs | Électricité OREX au débit bas | 13,3 kWh/t | CALC-A9-OREX-KWH-T-HAUT | CONFIRMÉ | `p / d` | `calculs.yaml`, 120 kW / 9 t/h | Calcul exact : 13,3333 kWh/t. |
| 17 | 9.7 | Bâtiment et fondation | 4 650 m2 ; 5 t/m2 | OW-ENG-P04-P07-SPEC-PLANS + OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « Building area 4,650 m2 » ; « foundation curing of 5 Mt or more per square meter » | Brochure OneWorld anglaise, p. 4 et 19 | Nature : constructeur. Les dimensions contradictoires ont été signalées au lot 1. |
| 18 | 9.7, fiche 9.L.f | Terrassement, VRD et génie civil de Dreux | 2 695 000 EUR HT estimés | PRM-BOAMP-SITREVA-DREUX-2024 | CONFIRMÉ | « Titre : Lot 1 : Terrassement, VRD et génie civil » ; « Valeur estimée hors TVA : 2,695,000 Euro » | BOAMP, avis 24-97628, LOT-0001, section 5.1.5 | L'annexe dit bien « estimated », pas attribué. Projet différent. |
| 19 | 9.7 et 9.9 | Enveloppe bâtiment, génie civil, ingénierie et permis | 5 MEUR | D-051 | CONFIRMÉ | « batiment, genie civil, ingenierie et permis : base de 5 MEUR » | `_decisions.yaml`, D-051 | Hypothèse du porteur, correctement présentée comme telle. Le terrain n'apparaît toutefois ni dans D-051 ni dans le HTML. |
| 20 | 9.8, fiche 9.L.g | Ratios génériques de procédé | ingénierie 4 à 20 % ; bâtiments 2 à 18 % du FCI | PRM-POLIMI-PT-PLANTECON-2015 | CONFIRMÉ | « Buildings (including services) 2-18 » ; « Engineering and supervision 4-20 » | Politecnico di Milano, L8 Plant Economics, slide 8 | Source secondaire de 2015 citant un manuel de 2003, correctement donnée pour orientation seulement. |
| 21 | 9.9 et 9.11 | Total avant transport | 60 MEUR | CALC-A9-CAPEX-LIGNE | CONFIRMÉ | `m + p + b` | `calculs.yaml`, CALC-A9-CAPEX-LIGNE | 50 + 5 + 5 = 60. Calcul exact, mais périmètre incomplet pour un besoin de financement total. |
| 22 | 9.9 et 9.11 | Transport exclu | non compté | D-051 | CONFIRMÉ | « transport (100 conteneurs) non compris et non chiffre, depend du site » | `_decisions.yaml`, D-051 | L'exclusion est claire. Le cours public donne environ 10 % du coût des équipements comme simple ratio de planification, soit environ 5 MEUR sur 50 MEUR, sans valeur de devis. |
| 23 | 9.10 et 9.11 | Points ouverts déjà recensés | R-006, R-015, R-017, R-023, R-047, R-049 | Registre des recherches | CONFIRMÉ | « Quotation for a pre-sorting line » ; « Electricity [...] two contradictory figures » ; « SEA CORAL on process water » ; « Shipping cost by site » | Section 9.10 | Les principaux points techniques déjà connus sont bien repris. Les postes financiers manquants ci-dessous ne le sont pas. |
| 24 | 9.9 à 9.11 | Raccordement électrique, transformateurs et distribution | poste absent | PRM-POLIMI-PT-PLANTECON-2015 | ABSENT | « Electrical systems (installed) 2-10 » | L8 Plant Economics, slide 8 | À 60 MEUR, ordre générique de 1,2 à 6 MEUR. Ne pas additionner mécaniquement aux autres ratios. Devis Enedis et étude HTA requis. IMPORTANT. |
| 25 | 9.9 à 9.11 | Utilités, eau, air comprimé, stockage, incendie et traitement des rejets | poste absent ou périmètre non défini | PRM-POLIMI-PT-PLANTECON-2015 | ABSENT | « supply of steam, water, electricity, compressed air, fuel, waste storage and disposal, fire protection systems » ; « Service facilities (installed) 8-30 » | L8 Plant Economics, slides 8 et 20 | Ordre générique de 4,8 à 18 MEUR sur 60 MEUR, avec fort chevauchement possible avec la machine et le bâtiment. IMPORTANT. |
| 26 | 9.9 à 9.11 | Provision pour aléas | aucune | PRM-POLIMI-PT-PLANTECON-2015 | ABSENT | « Contingency 5-15 » | L8 Plant Economics, slide 8 | Ordre générique de 3 à 9 MEUR sur 60 MEUR. C'est le manque le plus net pour un budget encore sans devis. IMPORTANT. |
| 27 | 9.9 à 9.11 | Fonds de roulement | aucun | PRM-POLIMI-PT-PLANTECON-2015 | ABSENT | « TCI = FCI + WC: Total Capital Investment » ; « Available cash to purchase raw materials, pay wages, pay bills, interests » | L8 Plant Economics, slides 2 et 4 | Aucun pourcentage fiable retenu. À construire à partir des délais d'encaissement, stocks, salaires, énergie et fiscalité. IMPORTANT. |
| 28 | 9.9 à 9.11 | Assurance chantier, travaux temporaires, essais et mise en service | périmètre non indiqué | PRM-POLIMI-PT-PLANTECON-2015 | ABSENT | « expenditures occurring during the erection of the plant, up to its startup » ; « taxes, insurance » ; « 8-10% of the FCI » | L8 Plant Economics, slide 25 | Le ratio couvre une catégorie large et chevauche probablement l'installation incluse. Il montre néanmoins qu'une matrice de périmètre est indispensable. IMPORTANT. |
| 29 | 9.9 à 9.11 | Complément éventuel de traitement des fumées et des eaux | coût non chiffré | R-017 et Annexes 2/4 | NON SOURCÉ | Aucune garantie contractuelle de conformité française contrôlée dans l'annexe 9 | Sections 9.4 et 9.10 | PRIMO et SEA CORAL sont inclus, mais leur suffisant réglementaire n'est pas établi ici. Coût conditionnel, potentiellement important. |
| 30 | 9.7 et 9.9 | Terrain dans l'enveloppe de 5 MEUR | annoncé dans le mandat, absent du HTML et de D-051 | Mandat du lot 2 comparé à D-051 | ABSENT | Le mandat indique « bâtiment, génie civil, ingénierie, permis et terrain » ; D-051 s'arrête à « bâtiment, génie civil, ingénierie et permis » | Demande utilisateur ; `_decisions.yaml`, D-051 ; HTML 9.7 et 9.9 | Écart de périmètre documentaire. Il faut décider explicitement si le terrain est inclus ou ajouté séparément. IMPORTANT. |

## Écarts

### E-1, sections 9.9 et 9.11, BLOQUANT pour le financement

- Annexe : recommandation de 60 MEUR par ligne avant transport.
- Constat : le calcul est exact, mais le tableau ne couvre pas explicitement le raccordement électrique, les utilités et stockages, la protection incendie, les aléas, le fonds de roulement, certains frais de chantier et les éventuels compléments environnementaux.
- Effet : le montant de 60 MEUR peut être utilisé comme base de CAPEX, mais pas comme besoin total de financement.
- Correction proposée : conserver 60 MEUR comme « base sponsor avant transport et postes non chiffrés », puis ajouter des lignes séparées et une réserve d'aléas. Ne pas additionner aveuglément les ratios génériques, car ils se chevauchent.

### E-2, sections 9.10 et 9.11, IMPORTANT

- Annexe : les points ouverts couvrent le tri, l'électricité de la machine, SEA CORAL, la presse, le fret et la formation.
- Manque : aucun point ouvert ne demande une matrice contractuelle complète des inclusions et exclusions de la machine, de l'installation, du bâtiment, des raccordements, des utilités et de la mise en service.
- Effet : risque de double compte ou de poste oublié de plusieurs millions d'euros.
- Correction proposée : ajouter une demande unique de « battery limits and scope matrix » avec responsabilités, interfaces, essais de performance et garanties.

### E-3, sections 9.7 et 9.9, IMPORTANT

- Mandat : le terrain est annoncé dans l'enveloppe de 5 MEUR.
- Registre et HTML : D-051 et l'annexe ne mentionnent pas le terrain.
- Effet : le lecteur ne sait pas si l'acquisition foncière est incluse ou oubliée.
- Correction proposée : clarifier D-051 avec Stéphane, puis afficher soit « terrain inclus », soit une ligne foncière séparée.

### E-4, section 9.6, IMPORTANT

- Annexe : la presse OREX est présentée avec 9 à 15 t/h, 120 kW et une fraction sèche à 18 à 20 % d'humidité.
- Autre lecture : la présentation commerciale porte sur une OMR annoncée à 25 à 30 % d'eau, alors que l'OMR française du plan est à 42,1 %. À 9 t/h, une machine traite 216 t/j si elle fonctionne 24 h ; elle ne couvre 280 t/j qu'au-dessus de 11,7 t/h.
- Effet : la presse reste techniquement possible, mais une seule machine et l'humidité finale ne sont pas démontrées pour le flux français.
- Correction proposée : conserver R-047, exiger un essai sur le flux cible et dimensionner le nombre de presses, la disponibilité et le stockage tampon.

### E-5, fiche 9.L.c, MINEUR

- Annexe : annonce d'overband à 5 350 EUR HT EXW.
- Source : annonce désormais inaccessible.
- Effet : aucun effet sensible sur un projet de 60 MEUR.
- Correction proposée : conserver au mieux comme ancien indice commercial non vérifiable, ou le retirer lors de la prochaine régénération.

## Coûts manquants ou non délimités

Les ratios ci-dessous sont des ordres de grandeur génériques issus d'un cours public de génie des procédés citant un manuel de 2003. Ils ne sont ni des devis ni des montants à additionner mécaniquement.

| Poste | Ordre de grandeur public | Gravité à 60 MEUR | Lecture |
|---|---:|---|---|
| Transport de 100 conteneurs | Environ 10 % du coût équipement, soit environ 5 MEUR sur 50 MEUR | IMPORTANT | Déjà explicitement exclu. Devis par site requis. |
| Raccordement et systèmes électriques installés | 2 à 10 % du FCI, soit 1,2 à 6 MEUR sur 60 MEUR | IMPORTANT | Poste non visible dans le budget. Peut recouvrir une partie du bâtiment ou de la machine. |
| Utilités, stockage, protection incendie, eau et rejets | 8 à 30 % du FCI, soit 4,8 à 18 MEUR | IMPORTANT | Fourchette très large et chevauchante. Définir les limites de fourniture. |
| Aléas | 5 à 15 % du FCI, soit 3 à 9 MEUR | IMPORTANT | Poste absent alors que les devis ne sont pas obtenus. |
| Fonds de roulement | Pas de ratio retenu | IMPORTANT | Besoin de trésorerie distinct du CAPEX. |
| Assurance chantier, travaux temporaires et mise en service | Catégorie large donnée à 8 à 10 % du FCI | IMPORTANT | Chevauche probablement l'installation incluse. Confirmer contractuellement. |
| Traitement complémentaire des fumées ou des eaux | Aucun ordre fiable | IMPORTANT sous condition | Seulement si PRIMO ou SEA CORAL ne suffisent pas au permis et aux garanties. |
| Terrain | Aucun ordre fiable, dépend du site | IMPORTANT | Le mandat le dit inclus, D-051 et le HTML ne le disent pas. |
| Pont-bascule, laboratoire, sécurité, engins et petits équipements de site | Exemple BOAMP : pont-bascule estimé à 87 000 EUR sur le projet Dreux | MINEUR séparément | À inventorier, sans effet individuel bloquant. |

## Autres interprétations

1. **Les 5 MEUR de pré-traitement restent plausibles comme enveloppe provisoire.** Les indices unitaires publics totalisent moins que 5 MEUR, mais ils n'incluent ni intégration, convoyage complet, automatismes, génie civil, redondance, ATEX, montage ni essais. Le benchmark Baudelet à 8,5 MEUR couvre une ligne CSR plus large. Aucune de ces comparaisons ne démontre que 5 MEUR est faux.
2. **Le flux plastique peut coûter moins cher à préparer.** Le modèle applique néanmoins 5 MEUR à chaque ligne par décision. C'est prudent pour le CAPEX, mais pas une configuration technique. Un flux OMR ou DAE demande plus d'équipements et de redondance.
3. **Une OREX 400 peut suffire seulement selon le régime de marche.** À 9 à 15 t/h, elle couvre 216 à 360 t/j sur 24 h. Elle peut devenir limite si le tonnage brut atteint 280 t/j, si la ligne ne tourne qu'en journée ou si la disponibilité est déduite. Une seconde unité ou un stockage tampon peut être nécessaire.
4. **Le budget bâtiment de 5 MEUR n'est pas manifestement impossible, mais il est serré.** Le projet Dreux donne 2,695 MEUR HT de terrassement, VRD et génie civil et 1,3 MEUR HT de bâtiment pour un projet différent. Cela approche déjà 4 MEUR avant ingénierie, permis, terrain et spécificités Urban Rig.
5. **Les ratios génériques ne doivent pas être additionnés.** Certains coûts peuvent déjà être dans les 50 MEUR de machine, l'installation incluse ou les 5 MEUR de bâtiment. Ils servent à identifier les questions contractuelles, pas à produire un nouveau total artificiel.
6. **PRIMO et SEA CORAL peuvent éviter une partie des coûts additionnels.** Leur inclusion est acquise par décision, mais leur performance réglementaire sur le site français reste à démontrer. L'absence de preuve ne démontre pas une non-conformité.
7. **Le total de 60 MEUR passe comme base du modèle.** Il ne passe pas comme prix ferme « clé en main tout compris ». Il reste possible sous conditions, avec devis, interfaces contractuelles, aléas et besoin de trésorerie.

## Les cinq erreurs les plus graves

1. Absence de distinction claire entre base CAPEX de 60 MEUR et besoin total de financement.
2. Absence de matrice contractuelle des limites de fourniture et interfaces.
3. Raccordements, utilités, stockage et incendie non chiffrés ou non délimités.
4. Aucune réserve d'aléas ni fonds de roulement dans la recommandation.
5. Terrain annoncé dans le mandat mais absent de D-051 et du HTML.

## Ce qui n'a pas pu être vérifié

- Prix de l'overband : annonce inaccessible.
- Prix de la presse OREX : non publié.
- Nombre de presses et humidité finale sur OMR française : aucun essai sur le flux cible.
- Coût de raccordement électrique : site et étude réseau non disponibles.
- Suffisance réglementaire de PRIMO et SEA CORAL : pas de garantie contractuelle contrôlée ici.
- Inclusion exacte des utilités, stockages, protection incendie, instrumentation, essais et assurance dans les 50 ou 5 MEUR : aucun contrat ni matrice de périmètre.
- Terrain : contradiction entre le mandat et D-051 à arbitrer.
- Besoin de fonds de roulement : données de stocks, délais de paiement, salaires et contrats absentes.

## Décompte

- CONFIRMÉ : 22
- ABSENT : 6
- INACCESSIBLE : 1
- NON SOURCÉ : 1
- DIFFÉRENT : 0
- CALCUL FAUX : 0
- Total : 30

## Lecture d'ensemble en langage simple

- **PASSE :** les valeurs reprises, les calculs OREX, les ordres de grandeur et le calcul 50 + 5 + 5.
- **NE PASSE PAS :** présenter 60 MEUR comme financement total ferme et complet.
- **POSSIBLE SOUS CONDITIONS :** une ligne à 60 MEUR de base, si les devis confirment le pré-traitement et le bâtiment et si les autres postes sont ajoutés ou prouvés inclus.
- **À MESURER OU CONFIRMER :** performance de la presse sur le flux réel, besoin exact de tri, raccordement, traitement des fumées et des eaux, interfaces de fourniture, transport, terrain et fonds de roulement.

## Compte rendu Trouvé / Partiel / Non trouvé

| Statut | Élément | Résultat |
|---|---|---|
| Trouvé | Valeurs des sections 9.6 à 9.9 | Sources originales et pages publiques ouvertes ; calculs exacts. |
| Trouvé | Présentation des prix auxiliaires | Correctement limitée à des ordres de grandeur. |
| Trouvé | Capital fixe de base | 60 MEUR avant transport, décision et calcul correctement repris. |
| Partiel | Configuration de pré-traitement | Fonctions identifiées, mais dimensionnement et redondance non définis. |
| Partiel | Budget complet | Postes usuels identifiés, mais chevauchements et inclusions inconnus. |
| Non trouvé | Devis et garanties contractuelles | Pré-traitement, raccordements, fret, essais, conformité et limites de fourniture. |
| Non trouvé | Besoin total de financement | Fonds de roulement, aléas, frais financiers et calendrier de décaissement à construire. |
