# Contre-vérification de l'annexe 9, lot 1

Date : 2026-11-25  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-09-html/index.html` et fiches de preuve liées  
Périmètre : « How to Read This Annex », « Key Messages » et sections 9.1 à 9.5  
Accès internet : OUI  
Lecture des PDF : OUI, documents originaux ouverts et pages contrôlées visuellement ou par extraction de texte.

## Conclusion courte

Le lot 1 **passe sous conditions**. Les caractéristiques, les options, la logistique et les calculs sont correctement repris comme déclarations du constructeur ou décisions du porteur. Aucun écart bloquant n'a été trouvé.

Trois corrections sont nécessaires : ne pas présenter le plan Hardin comme une transaction en USD, afficher la contradiction de délai entre 10 et 4 mois, et afficher la contradiction de dimensions entre 66 x 7 x 7 m et 62 x 10 x 7 m. Par prudence, le modèle doit retenir 600 kW et au moins 10 mois, puis obtenir un plan d'exécution et un bordereau de colisage contractuels.

## Tableau des vérifications

| N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire |
|---:|---|---|---|---|---|---|---|---|
| 1 | How to Read | OneWorld porte le plan et ses données ne sont pas indépendantes | Données constructeur | D-027 | CONFIRMÉ | « le porteur du plan est OneWorld ; les données de OneWorld sont nos données de conception » | `_decisions.yaml`, D-027 | Nature : constructeur. Présentation correcte. |
| 2 | Key Messages, 9.3, 9.4 | Prix décidé, trois options comprises, livraison exclue | 50 MEUR | D-050 | CONFIRMÉ | « 50 000 000 EUR pour une machine de 200 t/jour, options PRIMO, SEA CORAL et FORCE 9 comprises ; livraison non comprise » | `_decisions.yaml`, D-050 | Décision du porteur, pas devis. C'est clairement indiqué. |
| 3 | Key Messages, 9.3 | Prix par tonne de charge annuelle | 978 EUR/t/an | CALC-A9-PRIX-PAR-T-AN | CONFIRMÉ | `p / a` | `calculs.yaml`, CALC-A9-PRIX-PAR-T-AN | 50 000 000 / 51 100 = 978,4736. Arrondi correct. |
| 4 | Key Messages, 9.5 | Expédition | 100 conteneurs de 40 pieds | OW-TRANSPORT-INSTALLATION | CONFIRMÉ | « 200t | 100 » sous « How many 40' containers for shipment » | `transport installation and maintenance.pdf`, p. 1 | Nature : constructeur. Tableau sans émetteur ni date imprimés. |
| 5 | Key Messages, 9.5 | Installation sur site | 30 jours, 10 personnes | OW-TRANSPORT-INSTALLATION | CONFIRMÉ | « 200t | 30 | 10 » sous « Days needed for installation onsite » et « Installation staff » | même PDF, p. 1 | Nature : constructeur. |
| 6 | Key Messages, 9.5 | Formation | 30 jours, 9 formateurs | OW-TRANSPORT-INSTALLATION | CONFIRMÉ | « 200t | 30 | 9 » sous « Training days » et « Trainers » | même PDF, p. 1 | Nature : constructeur. |
| 7 | Key Messages | Deux enveloppes autour de la machine | 5 MEUR + 5 MEUR | D-051 | CONFIRMÉ | « pre-traitement : environ 5 MEUR par ligne ; batiment, genie civil, ingenierie et permis : base de 5 MEUR » | `_decisions.yaml`, D-051 | Hypothèses du porteur, correctement présentées comme estimations. |
| 8 | Key Messages | Le discours « sans tri » coexiste avec un broyeur et une machine de tri | Contradiction signalée | OW-ENG-P04-P07-SPEC-PLANS | CONFIRMÉ | « Input throat (with crushing function) ; Sorting machine » | `Urban RIg ENG　.pdf`, p. 4 | La contradiction est bien exposée. Elle sera traitée au lot 2. |
| 9 | 9.1 | URC-2000 | 200 t/j, continu | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « 200 ton 7 Continuous Process URC-2000 » | `Urban RIg ENG　.pdf`, p. 3 | Nature : constructeur. |
| 10 | 9.1 | URC-1000 | 100 t/j, continu | même source | CONFIRMÉ | « 100 ton 4 Continuous Process URC-1000 » | même PDF, p. 3 | Nature : constructeur. |
| 11 | 9.1 | URC-400 | 40 t/j, continu | même source | CONFIRMÉ | « 40 ton Continuous Process URC-400 » | même PDF, p. 3 et 5 | Nature : constructeur. |
| 12 | 9.1 | URB-50 | 5 t/j, lot | même source | CONFIRMÉ | « 5 ton 1 Batch URB-50 » | même PDF, p. 3 et 8 | Nature : constructeur. |
| 13 | 9.1 | URB-10 et URT-10 | 1 t/j, lot | même source | CONFIRMÉ | « 1 ton 1 Batch URB-10 » et « 1 ton 1 Batch URT-10 » | même PDF, p. 3 et 9 | Nature : constructeur. |
| 14 | 9.1 | Gamme annoncée comme gamme Urban Rig, mais URC-150 omis | 15 t/j, continu, absent du tableau | même source | ABSENT | « 15 ton 7 Continuous URC-150 » | même PDF, p. 7 | Omission mineure, sans effet sur le choix URC-2000. |
| 15 | 9.2 | Capacité nominale | 200 t/j | UR2000-JP-P08-SPEC | CONFIRMÉ | « 処理量 / 日 200 トン / 日 » | `UR2000-JP.pdf`, p. 8 | Nature : constructeur. |
| 16 | 9.2 | Charge retenue par le plan | 200 m3/j x 0,7 t/m3 = 140 t/j | D-035 | CONFIRMÉ | « masse = volume x 0,7 t/m3 = 140 t/jour (HYPOTHESE de Stephane) » | `_decisions.yaml`, D-035 | Hypothèse correctement distincte de la capacité nominale constructeur. |
| 17 | 9.2 | Charge annuelle sans disponibilité déduite | 51 100 t/an | CALC-A8-CAPACITE-AN | CONFIRMÉ | `j * n` | `calculs.yaml`, CALC-A8-CAPACITE-AN | 140 x 365 = 51 100. Borne haute clairement signalée. |
| 18 | 9.2 | Construction modulaire | 7 unités d'environ 12 t, 7 parties transportées | UR2000-JP-P06-P07-MODULES | CONFIRMÉ | « 本機処理プラント (200T) は 7 ユニットで構成。 ; 約 12 トン処理機 ( 1 ユニット ) ; 処理機本体を７分割しトラック搬送して現地組立方式を採用。 » | `UR2000-JP.pdf`, p. 6 | Nature : constructeur. La formulation japonaise sur les 12 t reste sommaire. |
| 19 | 9.2 | Dimensions et bâtiment selon la brochure anglaise | 66 x 7 x 7 m ; 4 650 m2 | OW-ENG-P04-P07-SPEC-PLANS | CONFIRMÉ | « Size (Processing Unit) W:66m D: 7m H: 7m » ; « Building area 4,650 m2 » | `Urban RIg ENG　.pdf`, p. 4 | Exact dans la source citée. |
| 20 | 9.2 | Dimensions comparées à la brochure japonaise | 66 x 7 x 7 m annoncé, 62 x 10 x 7 m ailleurs | UR2000-JP-P08-SPEC | DIFFÉRENT | « サイズ ( 処理機 ) W: 62m D: 10m H: 7m » | `UR2000-JP.pdf`, p. 8 | Contradiction OneWorld non signalée. La surface de bâtiment reste 4 650 m2 dans les deux plans. |
| 21 | 9.2 | Température et pression maximales | 600 °C ; 0,2 MPa | UR2000-JP-P08-SPEC | CONFIRMÉ | « 熱処理分解温度 MAX 600℃ 常圧 0.2MPa 以下 » | `UR2000-JP.pdf`, p. 8 | Nature : constructeur. |
| 22 | 9.2 | Deux valeurs d'électricité contradictoires | 20 kW et 600 kW | UR2000-JP-P08-SPEC + OW-CONSO-ENERGIE | CONFIRMÉ | « 消費電力 ( 連続時 ) 20kw/h » ; « 600kW/h » | `UR2000-JP.pdf`, p. 8 ; `consommation-electrique-et-fuel.pdf`, p. 1 | Les unités source sont incorrectes, mais le conflit est réel et correctement signalé. Retenir 600 kW par prudence. |
| 23 | 9.2 | Fioul en mode mixte | 10 000 L/j | OW-CONSO-ENERGIE | CONFIRMÉ | « 10,000L/day(200t) » | `consommation-electrique-et-fuel.pdf`, p. 1 | Nature : constructeur, sans méthode ni date imprimée. |
| 24 | 9.2 | Délai présenté comme contrat à démarrage | environ 10 mois | OW-ENG-P03-P19-GAMME-DELAIS | DIFFÉRENT | « The manufacturing period varies depending on the product. Continuous type = about 10 months » ; autre document : « １st. Month ; ２〜3th. Months ; ４th. Month » sous « 契約から製造、船積み設置までの流れ » | `Urban RIg ENG　.pdf`, p. 19 ; `UR2000-JP.pdf`, p. 13 | Le premier document parle de fabrication, pas explicitement de contrat à démarrage. Le second affiche 4 mois jusqu'à installation et essais. Utiliser au moins 10 mois avant clarification. |
| 25 | 9.2 | Fondation | 5 t/m2 | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « foundation curing of 5 Mt or more per square meter » | `Urban RIg ENG　.pdf`, p. 19 | La source écrit « Mt », vraisemblablement pour metric ton. À confirmer sur plan de génie civil. |
| 26 | 9.3 | Prix par tonne de capacité journalière nominale | 250 000 EUR par t/j | CALC-A9-PRIX-PAR-TJ | CONFIRMÉ | `p / c` | `calculs.yaml`, CALC-A9-PRIX-PAR-TJ | 50 000 000 / 200 = 250 000. |
| 27 | 9.3 | Valeurs du plan Hardin | machine 60 000 000 ; autres CAPEX 4 700 000 ; capacité 200 t | HARDIN-LOI | CONFIRMÉ | « Machine Capacity (T) 200 ; Machine cost 60,000,000 ; Initial other CAPEX 4,700,000 » | `Business-Plan-Hardin.pdf`, p. 6 | Le texte principal précise correctement que la devise n'est pas indiquée et qu'il s'agit d'une feuille de planification. |
| 28 | 9.3 | Calcul Hardin par capacité journalière | 300 000 par t/j | CALC-A9-HARDIN-PAR-TJ | CONFIRMÉ | `p / c` | `calculs.yaml`, CALC-A9-HARDIN-PAR-TJ | 60 000 000 / 200 = 300 000, devise non indiquée. |
| 29 | Fiche 9.M.a | Valeur décrite comme USD et transaction réelle | « USD 60 M » ; « seul prix de transaction réel » | HARDIN-LOI | DIFFÉRENT | « Hardin would purchase 2x 100T daily capacity waste processing pyrolysis machine » ; « Machine cost 60,000,000 » | `Business-Plan-Hardin.pdf`, p. 4 et 6 | Le PDF exprime une intention et la page financière n'indique pas la devise. Le HTML principal corrige déjà cette lecture, mais la fiche reste erronée. |
| 30 | 9.4 | Fonction PRIMO | DeNOx, DeSOx, poussières, odeurs | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « DeNOx NOx decomposition ; DeSOx SOx decomposition ; Dust removal ; Odor removal » | `Urban RIg ENG　.pdf`, p. 12 | Nature : constructeur. PRIMO est bien marqué « OPTION ». |
| 31 | 9.4 | Principe SEA CORAL | absorption, évaporation par air, récupération d'eau | OW-ENG-P13-SEACORAL | CONFIRMÉ | « This SEA CORAL ceramic absorbs water molecule from wastewater. The water molecule is vaporized by air blowing and recover pure water » | `Urban Rig Recycling Solutions ENG .pdf`, p. 13 | Déclaration constructeur, pas performance indépendante. |
| 32 | 9.4 | Essai documenté SEA CORAL | dessalement d'eau de mer | SEACORAL-DETAIL-ENG | CONFIRMÉ | « Seawater desalination Test » ; « Chloride ion mg/L 31,000 31 140,000 » | `SEA CORALdetail.pdf`, p. 5 | Aucun essai sur eau de procédé Urban Rig dans les pièces citées. |
| 33 | 9.4 | Fonction FORCE 9 | stabilisation catalytique vers 400 °C | OW-ENG-P03-P19-GAMME-DELAIS | CONFIRMÉ | « processing into a stable harmless metal by using a patented catalyst (ceramic) at a low temperature of about 400℃ » | `Urban RIg ENG　.pdf`, p. 11 | Nature : constructeur. L'efficacité indépendante n'est pas démontrée ici. |
| 34 | 9.5 | Maintenance | 3 jours tous les 3 mois | OW-TRANSPORT-INSTALLATION | CONFIRMÉ | « 3 months operation + 3 days maintenance » | `transport installation and maintenance.pdf`, p. 1 | Nature : constructeur. |
| 35 | 9.5 | Installation comprise, expédition exclue | incluse ; non chiffrée | D-051 | CONFIRMÉ | « installation sur site comprise dans les 50 MEUR ; transport (100 conteneurs) non compris et non chiffre » | `_decisions.yaml`, D-051 | Décision correctement reprise, pas devis. |
| 36 | 9.5 | Cent conteneurs comparés à sept parties | 100 contre 7 | OW-TRANSPORT-INSTALLATION + UR2000-JP-P06-P07-MODULES | CONFIRMÉ | « 200t | 100 » ; « 処理機本体を７分割しトラック搬送 » | tableau transport p. 1 ; `UR2000-JP.pdf`, p. 6 | Les deux chiffres existent. Ils ne sont pas nécessairement incompatibles : 7 peut viser le corps principal et 100 l'ensemble de la livraison. |
| 37 | 9.5 | Inclusion de la formation dans le prix | non précisée | R-049 | NON SOURCÉ | Aucune source contractuelle | Aucun devis ou contrat | L'annexe traite correctement ce point comme ouvert. Pas d'entrée au registre sans citation. |

## Écarts

### E-1, fiche 9.M.a, IMPORTANT

- Annexe : la fiche affirme « USD 60 M » et « seul prix de transaction réel du dépôt ».
- Source : le PDF montre une intention d'achat, « would purchase », et une feuille financière sans devise imprimée.
- Effet : le benchmark peut être pris à tort pour un prix de transaction ferme en dollars.
- Correction proposée : supprimer « USD » et « transaction réelle » de la fiche. Conserver « 60 000 000, devise non indiquée, scénario de planification pour 2 x URC-1000 ».

### E-2, section 9.2, IMPORTANT

- Annexe : « Lead time, contract to start-up, about 10 months ».
- Sources : la brochure anglaise dit seulement que la période de fabrication du continu est d'environ 10 mois ; la brochure japonaise présente un échéancier de 4 mois du contrat à l'installation et aux essais.
- Effet : incertitude de six mois ou plus sur le calendrier industriel, hors autorisations françaises.
- Correction proposée : afficher les deux valeurs, préciser leurs périmètres et retenir au moins 10 mois dans le modèle jusqu'à réception d'un planning contractuel. Les autorisations et travaux préparatoires doivent être planifiés séparément.

### E-3, section 9.2, IMPORTANT

- Annexe : 66 x 7 x 7 m.
- Autre source OneWorld : 62 x 10 x 7 m.
- Effet : le gabarit, les circulations et les fondations peuvent changer, même si les deux plans affichent 4 650 m2 de bâtiment.
- Correction proposée : afficher la contradiction et retenir une enveloppe provisoire de 66 x 10 x 7 m, sans la traiter comme plan d'exécution. Demander un plan général d'implantation révisé et coté.

### E-4, section 9.1, MINEUR

- Annexe : le tableau intitulé « The Urban Rig Range » omet l'URC-150.
- Source : la brochure donne « 15 ton 7 Continuous URC-150 ».
- Effet : aucun effet sur le choix URC-2000 ni sur le modèle financier.
- Correction proposée : ajouter l'URC-150 ou renommer le tableau « Main models considered ».

Il n'y a pas de cinquième erreur matérielle dans ce lot. La différence entre 100 conteneurs et 7 parties est déjà signalée et peut s'expliquer par des périmètres logistiques différents.

## Autres interprétations

1. **Électricité.** Les 20 et 600 « kW/h » peuvent provenir d'un périmètre différent ou d'une erreur de transcription. Aucune source ne permet de trancher. Retenir 600 kW pour le raccordement et les charges d'exploitation est la lecture prudente.
2. **Délai.** Les 4 mois peuvent viser une configuration, une époque ou un marché différent, tandis que les 10 mois peuvent viser une fabrication plus complète. Sans date imprimée et sans planning contractuel, la valeur prudente reste au moins 10 mois, à laquelle s'ajoutent autorisations et travaux français.
3. **Dimensions.** Les valeurs 66 x 7 x 7 m et 62 x 10 x 7 m peuvent correspondre à deux révisions ou à deux définitions de l'unité. L'égalité de la surface de bâtiment à 4 650 m2 réduit l'effet sur l'ordre de grandeur foncier, mais ne suffit pas pour le génie civil.
4. **Transport.** Les 7 parties peuvent être les sept modules du corps de traitement, tandis que les 100 conteneurs comprennent chaudières, réservoirs, traitement des fumées, convoyeurs et auxiliaires. Il faut un bordereau de colisage, pas choisir silencieusement l'un des deux chiffres.
5. **Hardin.** Une devise en dollars peut être plausible dans le contexte coréen ou financier, mais elle n'est pas imprimée sur la page contrôlée. Elle ne peut donc pas être retenue comme fait.

## Les erreurs les plus graves

1. Fiche 9.M.a : « USD » et « transaction réelle » non démontrés.
2. Délai : 10 mois présenté comme contrat à démarrage alors que la source dit fabrication et qu'un autre document affiche 4 mois.
3. Dimensions : 66 x 7 x 7 m contre 62 x 10 x 7 m, sans contradiction affichée.
4. Gamme : URC-150 de 15 t/j omis, effet mineur.
5. Aucune cinquième erreur matérielle trouvée.

## Ce qui n'a pas pu être vérifié

- Inclusion de la formation dans les 50 MEUR : aucun devis ou contrat, demande R-049 ouverte.
- Coût de transport des 100 conteneurs : site de destination non arrêté et aucune offre de fret.
- Attribution formelle et date du tableau transport, installation et maintenance : non imprimées dans le document.
- Performance industrielle de PRIMO, SEA CORAL et FORCE 9 : hors objet du lot, et aucune garantie contractuelle contrôlée ici.
- Explication des écarts 20/600 kW, 4/10 mois, 7 parties/100 conteneurs et 66 x 7/62 x 10 m : aucune note de révision ou réponse constructeur.

## Décompte

- CONFIRMÉ : 32
- DIFFÉRENT : 3
- ABSENT : 1
- NON SOURCÉ : 1
- INACCESSIBLE : 0
- CALCUL FAUX : 0
- Total : 37

## Compte rendu Trouvé / Partiel / Non trouvé

| Statut | Élément | Résultat |
|---|---|---|
| Trouvé | Données OneWorld des sections 9.1 à 9.5 | Pages originales ouvertes, valeurs recopiées ci-dessus. |
| Trouvé | Décisions D-027, D-035, D-050 et D-051 | Reprises fidèlement et présentées comme décisions ou hypothèses. |
| Trouvé | Calculs de 51 100 t/an, 978 EUR/t/an, 250 000 EUR/(t/j) et 300 000 par (t/j) | Tous recalculés, aucun calcul faux. |
| Partiel | Délai, dimensions, électricité et colisage | Valeurs présentes mais contradictoires ou de périmètre incertain. |
| Non trouvé | Devis, contrat, planning ferme, plan d'exécution et bordereau de colisage | À obtenir avant décision d'investissement et chiffrage logistique final. |
