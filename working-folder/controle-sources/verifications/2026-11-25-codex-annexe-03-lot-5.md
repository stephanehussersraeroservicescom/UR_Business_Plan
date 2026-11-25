Accès internet : OUI
Lecture des PDF : OUI

# Contre-vérification de l'annexe 3, lot 5, vérification légère

Date : 25 novembre 2026. Agent : codex. Périmètre : « How to Read This Annex », « Key Messages », sections 3.7, 3.8 et 3.9, cohérence des étiquettes et taux de confiance, et affirmations « OneWorld design data ». Les rapports des lots 1 à 4 ont été relus. Les prix et hypothèses D-xxx restent hors recalcul selon la consigne révisée.

**Conclusion : la synthèse reflète correctement les mesures, calculs et limites principales, mais elle doit intégrer trois corrections importantes. L'azote de l'huile a été mesuré et passe les plafonds cités. Une méthode Gold Standard peut être étudiée pour les métaux, même si aucun crédit n'est ouvert aujourd'hui pour l'huile ou le char. Enfin, deux fiches FNADE et loi de finances sont classées à tort comme données constructeur OneWorld. Les données réellement issues de OneWorld sont, dans l'ensemble, correctement attribuées et non présentées comme des mesures indépendantes.**

## 1. Tableau des verdicts

N° | Section ou fiche | Affirmation | Valeur annoncée | Source citée | Verdict | Citation exacte relevée | Emplacement réel | Commentaire
--- | --- | --- | --- | --- | --- | --- | --- | ---
| 1 | How to Read / 3.D | Les données OneWorld sont des chiffres internes non vérifiés indépendamment | Étiquette « OneWorld design data » | D-027 | CONFIRMÉ | « Its documentation is marked "OneWorld design data" [...] these are the company's own figures, not independent verification. » | Fiche 3.D, D-027 | La règle est claire et correctement appliquée aux principales brochures constructeur. |
| 2 | Key Messages / 1.C.b à d | Répartition de l'huile de conception | 80 % gazole, 10 % huile légère, 10 % huile lourde | CALC-A1-OW16-PART-GAZOLE, HEATING, HEAVY | CONFIRMÉ | « gazole / total * 100 » ; « heating / total * 100 » ; « heavy / total * 100 » | Fiches 1.C.b, 1.C.c et 1.C.d | 61,2 / 76,5 = 80 % et 7,65 / 76,5 = 10 %. Calculs exacts sur des données constructeur à 95 %. |
| 3 | 3.1.1 / 1.M.a et 2.3.b | Les zones à 150, 300, 450 et 600 °C sont décrites comme des zones de condensation | Quatre températures | UR2000-JP-P08-SPEC ; OW-ENG-P14-P15-PROCEDE | DIFFÉRENT | « The continuous unit process has a temperature setting for each unit. » ; « zones de chauffe 150 / 300 / 450 / 600 C » | Brochure anglaise p. 15 ; brochure japonaise p. 4 | Les sources parlent de réglages ou zones de chauffe et d'une séparation ultérieure par température de vapeur. Elles ne disent pas que ces quatre zones sont des condenseurs. |
| 4 | 3.2.1 / 3.M.a | OneWorld décrit le char comme un charbon pulvérisé à haut pouvoir calorifique mélangé à l'huile lourde | Déclaration de débouché | OW-ENG-P16-DEBOUCHES | CONFIRMÉ | « Produce high-calorie powder coal mixed with heavy oil » | Brochure OneWorld, p. 16 | Confirmé comme déclaration constructeur seulement. L'acceptation en cimenterie reste conditionnelle au chlore, aux cendres et au permis de l'acheteur. |
| 5 | 3.3.1 / 1.M.a et 3.M.a | OneWorld affirme extraire les métaux sans oxydation et les recycler | Déclaration de procédé et de débouché | OW-ENG-P14-P15-PROCEDE ; OW-ENG-P16-DEBOUCHES | CONFIRMÉ | « metals can be extracted in a non-oxidizing state » ; « Metals and glasses = Recycled resources » | Brochure OneWorld, p. 2 et p. 16 | Confirmé comme déclaration constructeur. La propreté et la sortie du statut de déchet ne sont pas démontrées. |
| 6 | Key Messages, huile | L'huile municipale produite ne respecte pas les spécifications du gazole ou du fioul lourd en l'état | Hors spécification | CHIBA-JLOS-HUILES ; textes gazole et fioul lourd | CONFIRMÉ | « eclair P.M. < 40 C » ; « Point d'éclair °C supérieur à 55,0 » ; « Point d'éclair : supérieur ou égal à 70 °C » | Rapports JLOS p. 45 et 46 ; arrêtés gazole et fioul lourd | Le point d'éclair suffit à faire échouer les deux spécifications. |
| 7 | 3.1.2 et 3.8 | L'azote de l'huile n'a pas été mesuré | Non mesuré | CHIBA-JLOS-HUILES | DIFFÉRENT | « azote 0,24 / 0,43 % » | Rapports JLOS, PDF p. 45 et 46 | L'azote vaut 2 400 et 4 300 mg/kg. Il passe les plafonds de 5 000 et 10 000 mg/kg cités dans l'annexe. |
| 8 | Key Messages, char | Pouvoir calorifique du char | 32 090 J/g | IZUMITEC-R35-339439 | CONFIRMÉ | « 発熱量 32090 J/g » | Calorie-content-UR-Carbide-1.pdf, p. 1 | Mesure retenue comme applicable. Elle démontre un potentiel énergétique, pas l'acceptation automatique par une cimenterie. |
| 9 | Key Messages, hydrogène | Hydrogène brut par tonne de charge riche en résines | Environ 13 kg/t | CALC-A3-H2-KG-T-RESINE | CONFIRMÉ | « part * 1000 * w / 100 » | calculs.yaml, CALC-A3-H2-KG-T-RESINE | Recalcul du lot 3 : 13,3178 kg/t. La vente exige encore purification et spécification d'acheteur. |
| 10 | Key Messages, carbone | Aucun mécanisme ouvert à l'usine ne possède de méthode applicable aujourd'hui | Aucun crédit possible | Section 3.5 | DIFFÉRENT | « applicable to projects that implement activities for the recovery and recycling of metals, alloys, and minerals » | Méthode Gold Standard 448 v1.0, résumé p. 2 | Correct pour l'huile et le char. Trop général pour l'ensemble de l'usine, car les métaux récupérés peuvent être étudiés sous cette méthode, avec additionnalité et absence de double comptage. |
| 11 | Key Messages, carbone | CO2 évité par rapport à l'incinération | Environ 1 973 kgCO2e/t | CALC-A3-CO2-NET-VS-INCIN | CONFIRMÉ | « subst - incin - elec » | calculs.yaml, CALC-A3-CO2-NET-VS-INCIN | 2 723,71 - 747 - 3,7368 = 1 972,9732. Correct comme scénario partiel, pas comme ACV ni crédit certifié. |
| 12 | 3.8, électricité | Deux données constructeur contradictoires sont signalées | 600 kW ou 20 kW | OW-CONSO-ENERGIE ; UR2000-JP-P08-SPEC | CONFIRMÉ | « 600kW/h » ; « 消費電力 ( 連続時 ) 20kw/h » | Tableau énergie p. 1 ; brochure URC-2000 p. 8 | La synthèse expose correctement le conflit. Aucun chiffre électrique réel n'est encore établi. |
| 13 | Index, fiche 3.M.b | Une synthèse FNADE est étiquetée comme donnée OneWorld | CONSTRUCTEUR, 95 % | FNADE-CSR-2023 | DIFFÉRENT | « Synthese modele economique filiere CSR (FNADE / SN2E, 2023) » | Fiche 3.M.b | La FNADE et le SN2E ne sont pas OneWorld. La fiche doit relever des données sectorielles et perdre l'étiquette CONSTRUCTEUR. |
| 14 | Index, fiche 3.M.c | Une loi de finances est étiquetée comme donnée OneWorld | CONSTRUCTEUR, 95 % | CIBS-TGAP-2026 | DIFFÉRENT | « Loi de finances 2026 - TGAP dechets » | Fiche 3.M.c | Un texte fiscal public doit relever des textes réglementaires, avec la confiance correspondante, et non des données constructeur. |
| 15 | 3.R.d / aviation | La fiche conclut qu'aucune annexe ASTM D7566 ne couvre l'huile de pyrolyse de plastiques | Conclusion exhaustive, confiance 100 % | A3-ASTM-D7566-24 | ABSENT | « This specification covers the manufacture of aviation turbine fuel that consists of conventional and synthetic blending components. » | Page de présentation ASTM, section Scope | La norme intégrale et ses annexes n'ont pas été lues. La page citée ne contient pas la conclusion exhaustive. Le taux de 100 % n'est pas justifié. |
| 16 | Index / 3.R.ah | L'Accord de Paris est abaissé à 90 % parce qu'il date de plus de huit ans | 90 % | A3I-ACCORD-PARIS-ART6 | DIFFÉRENT | « The use of internationally transferred mitigation outcomes [...] shall be voluntary and authorized by participating Parties. » | Accord de Paris, article 6, paragraphe 3 | L'ancienneté ne réduit pas la confiance dans un texte juridique toujours en vigueur. L'échelle de l'index attribue 100 % à la législation et à la réglementation. |

## 2. Écarts

### E-1, azote de l'huile encore présenté comme non mesuré

- Ce que dit l'annexe : « nitrogen, oxygen and metals not measured » dans la section 3.1.2 et dans le résumé de qualité.
- Ce que dit la source : « azote 0,24 / 0,43 % ».
- Gravité : **important**. Les valeurs mesurées passent les limites citées, ce qui améliore la lecture de la voie avec purification.
- Correction proposée : écrire « oxygène et métaux non mesurés ; azote mesuré à 2 400 et 4 300 mg/kg ».

### E-2, message carbone trop général

- Ce que dit l'annexe : aucun mécanisme ouvert à l'usine ne possède de méthode applicable aujourd'hui.
- Ce que dit la source : la méthode Gold Standard est « applicable to projects that implement activities for the recovery and recycling of metals, alloys, and minerals ».
- Gravité : **important**.
- Correction proposée : conserver l'absence de crédit pour l'huile et le char, et ajouter qu'une voie peut être étudiée pour les métaux sous conditions.

### E-3, deux fiches étiquetées à tort comme OneWorld

- Ce que dit l'index : 3.M.b et 3.M.c sont des « OneWorld design data » à 95 % et portent l'étiquette CONSTRUCTEUR.
- Ce que disent les titres : « FNADE / SN2E » et « Loi de finances 2026 ».
- Gravité : **important**. L'erreur brouille la nature des sources et le taux de confiance.
- Correction proposée : déplacer la synthèse FNADE vers la littérature ou les données sectorielles, et la loi de finances vers les textes réglementaires. Retirer l'étiquette CONSTRUCTEUR.

### E-4, zones de chauffe présentées comme zones de condensation

- Ce que dit l'annexe : le procédé condense les vapeurs dans des zones chauffées à 150, 300, 450 et 600 °C.
- Ce que dit la source : « The continuous unit process has a temperature setting for each unit » et la fiche japonaise parle de « zones de chauffe ».
- Gravité : **mineur**.
- Correction proposée : écrire que le procédé comporte des unités réglées à ces températures et que OneWorld déclare ensuite séparer les huiles selon la température des vapeurs.

### E-5, conclusion ASTM non démontrée

- Ce que dit l'annexe : aucune annexe ASTM D7566 n'approuve l'huile de pyrolyse de plastiques.
- Ce que dit la source accessible : « This specification covers [...] conventional and synthetic blending components. » La fiche reconnaît que la norme payante n'a pas été lue.
- Gravité : **important** pour la traçabilité, sans effet sur la prudence commerciale actuelle.
- Correction proposée : remplacer l'affirmation exhaustive par « aucune voie n'a été identifiée dans les éléments accessibles ; norme intégrale à vérifier » et réduire la confiance.

### E-6, ancienneté appliquée à un texte juridique

- Ce que dit l'index : Accord de Paris, 90 % parce que le texte a plus de huit ans.
- Ce que dit l'échelle : législation et réglementation à 100 %.
- Gravité : **mineur**.
- Correction proposée : attribuer 100 % au texte officiel en vigueur. Réserver la décote d'ancienneté aux données factuelles susceptibles d'évoluer.

## 3. Autres interprétations

### Char et cimenterie

- Lecture de l'annexe : le char est un combustible solide pour cimenterie.
- Ma lecture : le pouvoir calorifique de 32,09 GJ/t et les métaux mesurés rendent ce débouché techniquement plausible dans un cas standard. Le chlore, les cendres, l'humidité, la forme physique et le permis de l'acheteur conditionnent encore l'acceptation.
- Lecture retenue : écrire « combustible potentiel pour cimenterie, sous réserve d'essai d'acceptation ». La phrase suivante du Key Message mentionne déjà le chlore, ce qui évite de classer ce point comme écart autonome.

### Surplus de gaz et hydrogène

- Lecture de l'annexe : le surplus peut être vendu et environ 13 kg d'hydrogène sont disponibles par tonne de charge riche en résines.
- Ma lecture : la quantité calculée est correcte et le bilan thermique reste positif après retrait de l'hydrogène. La vente suppose encore un essai de purification, une pureté contractuelle, un coût de séparation et un acheteur.
- Lecture retenue : potentiel commercial réel, pas recette démontrée.

### Données OneWorld

- Lecture de l'annexe : les déclarations de conception sont utilisables à 95 %, tout en restant distinctes d'une vérification indépendante.
- Ma lecture : cette règle est appliquée correctement aux fractions 80/10/10, aux températures, aux débouchés déclarés, aux métaux et aux données de production. Elle ne transforme pas ces valeurs en mesures de performance commerciale.
- Lecture retenue : conserver l'étiquette constructeur et les demandes de confirmation. Corriger seulement les deux fiches qui ne viennent pas de OneWorld.

### Lecture générale de l'annexe

L'annexe décrit des débouchés plausibles, mais les messages doivent rester conditionnels : huile sous statut de déchet dangereux ou après purification, char après acceptation, métaux après contrôle de propreté, hydrogène après séparation. Les calculs physiques contrôlés passent. Les prix restent des champs modifiables et n'ont pas été vérifiés dans ce lot.

## 4. Autres points, une ligne chacun

- Section 3.7 : tous les prix, facteurs de qualité et valeurs « to decide » restent à confronter à des offres acheteurs, sans recalcul dans ce lot.
- Section 3.8 : ajouter la possibilité Gold Standard sur les métaux et corriger l'azote mesuré.
- Section 3.9 : les points ouverts couvrent correctement l'huile, le char, les acheteurs, l'électricité et les métaux ; ajouter un point spécifique sur l'essai PSA et un autre sur la méthode carbone des métaux.
- Confiance des standards volontaires : préciser dans l'échelle si 100 % signifie seulement que la règle du standard a été lue, sans préjuger de l'éligibilité du projet.

## 5. Ce qui n'a pas pu être vérifié

- La norme ASTM D7566 intégrale n'a pas été lue.
- Aucun essai d'acceptation en cimenterie, contrat d'achat de métaux, essai PSA ou bilan électrique garanti n'est disponible.
- Aucun dossier Gold Standard sur les métaux Urban Rig n'a été évalué par le standard.
- Aucun prix, aucune hypothèse D-xxx et aucune actualisation de marché ne sont vérifiés dans ce lot.

## 6. Décompte

Verdict | Nombre
--- | ---:
CONFIRMÉ | 9
DIFFÉRENT | 6
ABSENT | 1
INACCESSIBLE | 0
NON SOURCÉ | 0
CALCUL FAUX | 0
**Total** | **16**

16 verdicts portent une citation exacte et sont ajoutés au registre sans modifier les entrées antérieures.
