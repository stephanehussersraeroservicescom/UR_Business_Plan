# Urban Rig: sourcing des paramètres OPEX et financement

Unité URC-2000, 200 t/j de déchets entrants, environ 330 j/an, région parisienne, ligne de pré-tri, premier de série (FOAK) en France, CAPEX d'environ 50 M EUR.

- Consulté le 2026-10-10. Budget : 40 WebSearch utilisées. Les pages ont été lues avec WebFetch.
- Les identifiants `PRM-...` renvoient à `opex_finance.yaml`.
- Règle suivie : une valeur vient d'une source lue, ou d'un calcul fait sur des valeurs sourcées. Le calcul est alors montré. Une hypothèse non sourcée est marquée **[NON SOURCÉ]**.
- **Bases de calcul communes :**
  - Tonnage annuel : 200 t/j × 330 j = **66 000 t/an**. C'est une donnée du brief, pas une source externe.
  - Change : **1,16 USD/EUR**, hypothèse technique de la BCE de septembre 2026 pour 2026-2028 (PRM-BCE-PROJ-2026-09).

---

## 1. cout_etp (modèle : 56 000 EUR/an chargé)

### Éléments lus

**Point conventionnel IDCC 2149 en 2025 (PRM-IDCC2149-AV79-2025, source primaire)**
- Avenant n°79 du 14/11/2024 : « La valeur du point est fixée à 18.67 € ».
- Ces valeurs « prendront effet à compter du 1er janvier 2025 ».

**Grille IDCC 2149 en 2026 (PRM-TRAVIND-IDCC2149-2026, source secondaire)**
- « Au 1er janvier 2026, la valeur du point est fixée à 18,90 € (revalorisation de +1,23 % sur l'ensemble de la grille). »
- Minima mensuels bruts, base 35 h :

| Niveau | Coefficient | Minimum brut mensuel |
|---|---|---|
| III-3 (conducteur d'engin) | 125 | 2 362,50 € |
| III-4 | 132 | 2 494,80 € |
| IV-1 (chef d'équipe) | 150 | 2 835,00 € |
| IV-2 | 167 | 3 156,30 € |
| V (cadre) | 170 et plus | 3 213 € et plus |

- Contrôle fait : chaque montant est égal au coefficient × 18,90 €.
- Majorations indiquées par le même site :
  - Nuit (21h-6h) : +25 %.
  - Dimanche : « + 100 % du taux horaire ».
  - Panier de nuit : 11,34 €.
- **À vérifier sur Légifrance :**
  - Le site est secondaire.
  - La majoration de dimanche de 100 % n'a pas été vérifiée dans le texte de la convention.
  - La page contient une incohérence de date sur le SMIC.

**Salaire de marché, opérateur d'unité de valorisation énergétique en Île-de-France (PRM-FT-OFFRE-UVE-DOMONT-2025)**
- Offre France Travail à Domont (95), mise à jour le 29/04/2025.
- « Salaire brut : Mensuel de 2500.0 Euros à 2900.0 Euros sur 12.0 mois ».
- 3 ans d'expérience exigés.

**Salaire débutant (PRM-CIDJ-CONDUCTEUR-UVE-2025)**
- « Salaire brut mensuel débutant : 2 000 € ». Fiche publiée le 31/07/2025.

**Coût du travail, France, secteur NACE E (eau, assainissement, déchets, dépollution) (PRM-EUROSTAT-LCLEV-E-TOTAL-2025 et PRM-EUROSTAT-LCLEV-E-D11-2025)**
- Coût total du travail (D1_D4_MD5) :

| Année | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| EUR/h | 38,6 | 38,9 | 39,7 | 41,0 | 42,5 | 43,6 |

- Salaires et traitements (D11) :

| Année | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| EUR/h | 26,9 | 27,9 | 28,8 | 29,4 |

- **Calcul :** coût total / salaires = 43,6 / 29,4 = **1,483** en 2025. Le ratio est stable : 1,470 à 1,483 entre 2022 et 2023-2025.
- Les coûts non salariaux (cotisations employeur et taxes sur l'emploi, moins les subventions) représentent donc environ **48 % du brut** dans le secteur.
- **Réserve sur l'unité :**
  - La réponse de l'API indique seulement « EUR ».
  - Les métadonnées lues (PRM-EUROSTAT-LCLEV-META-2020) définissent le coût horaire comme « (total) labour costs divided by the corresponding number of hours worked ».
  - L'unité horaire est cohérente avec le libellé du jeu de données, mais elle n'est pas écrite en toutes lettres dans la réponse.

**Cotisations patronales 2026 (PRM-BPI-CREATION-COTIS-2026 et PRM-TRAVIND-COTIS-2026, sources secondaires)**
- Part employeur : « 40 à 45 % du brut avant allègements ».
- La RGDU est « maximale au SMIC, dégressive jusqu'à 3 SMIC ».
- Les taux réduits sont « neutralisés en droit commun par la réduction générale dégressive unique depuis le 1er janvier 2026 ».
- **Incohérence entre les deux sources :** taux maladie de 13,00 % d'un côté, 13,30 % de l'autre.
- La page officielle de l'URSSAF n'a pas pu être lue (accès bloqué par robots.txt).

### Calcul du coût chargé (calcul sur valeurs sourcées)

**Hypothèses de calcul**
- Brut de base : 2 500 / 2 700 / 2 900 € × 12 mois (PRM-FT-OFFRE-UVE-DOMONT-2025).
- Majoration de nuit en 5x8 continu :
  - La plage 21h-6h couvre 9 h sur 24, soit 37,5 % des heures.
  - Surcoût : 37,5 % × 25 % = **+9,4 %**.
- Majoration de dimanche :
  - Le dimanche représente 1/7 des heures.
  - Surcoût : 1/7 × 100 % = **+14,3 %** (taux non vérifié dans la convention).
- Chargement : × 1,483 (ratio Eurostat du secteur E, 2025).

**Résultats**

| Brut mensuel | Brut annuel | + nuit | + nuit + dimanche | Chargé (+ nuit) | Chargé (+ nuit + dim.) |
|---|---|---|---|---|---|
| 2 500 | 30 000 | 32 812 | 37 098 | **48 661** | **55 016** |
| 2 700 | 32 400 | 35 438 | 40 066 | **52 554** | **59 418** |
| 2 900 | 34 800 | 38 062 | 43 034 | **56 446** | **63 819** |

**Plancher conventionnel**
- Coefficient 125 en 2026 : 2 362,50 × 12 = 28 350 €.
- Avec la majoration de nuit et × 1,483 : **45 984 €**. Avec en plus le dimanche : 51 990 €.
- Coefficient 150 (chef d'équipe) : 55 181 € (avec nuit) à 62 389 € (avec nuit et dimanche).

**Recoupement avec la moyenne du secteur E**
- 43,6 €/h × 1 600 h = 69 760 €.
- **[NON SOURCÉ]** Le nombre d'heures annuelles n'a pas été sourcé : le texte légal des 1 607 h n'a pas été consulté.
- Ce chiffre est une moyenne de tout le secteur E, encadrement et eau compris. Il donne un ordre de grandeur haut pour un ETP « moyen » de l'équipe.

### Verdict
**Confirmé (dans la fourchette).**
- 56 000 € se situe dans la fourchette calculée de 48 700 à 63 800 € pour un opérateur ou technicien en 5x8 en Île-de-France.
- Pour un ETP moyen incluant l'encadrement et la maintenance, la valeur serait plutôt dans le haut de la fourchette, entre 60 000 et 70 000 €.
- Les majorations de dimanche et les primes d'ancienneté (3 à 15 % du minimum conventionnel, source secondaire) sont à vérifier.

---

## 2. etp_coeur_base = 15 ETP et etp_tri = 7 ETP

### Repères lus

| Source | Type d'installation | Capacité | Effectif | Ratio |
|---|---|---|---|---|
| PRM-BETHUNE-RAD-CVE-2021 | Usine d'incinération en exploitation, 2 fours de 5 t/h et 10 t/h, 3x8 sept jours sur sept | 89 893 t reçues en 2021 | « l'effectif est composé de 27 personnes » | 0,30 ETP/kt |
| PRM-PRUVIA-GENDORF-2025 | Pyrolyse plastique, parc chimique de Gendorf (DE), mise en service prévue fin 2026 | 35 000 t/an | « around 30 employees » | 0,86 /kt |
| PRM-QUANTAFUEL-SUNDERLAND-2022 | Pyrolyse plastique (projet, UK) | « approximately 100,000 tonnes » | « 100 long-term jobs » | 1,0 /kt |
| PRM-PAPREC-BRIVE-CSR | Unité de production de CSR | 30 000 t de CSR produites par an | « la création d'une vingtaine de postes » | env. 0,7 /kt de CSR |
| PRM-BXM-CENTRETRI-2023 | Centre de tri d'emballages de Bègles | 65 000 t/an, « débit nominal de 17 tonnes / heure » | « 60 salariés » | 3,5 emplois par t/h |
| PRM-NORMANTRI-CP-2025 | Centre de tri d'emballages (Normandie) | 55 000 t/an | « près de 60 emplois » | 1,1 /kt |
| PRM-THERMOGREEN-LAON-2025 | Recyclage mécanique de polystyrène (pas de pyrolyse) | 11 000 t/an | « 40 emplois » | sans objet |

- L'étude Citeo/ADEME de 2019 sur l'organisation du tri (PRM-CITEO-ADEME-TRI-2019) a été lue. Elle ne contient **aucune donnée d'effectif**.

### Calculs
- **Ratio du modèle :** 22 ETP / 66 kt = 0,33 ETP/kt.
- **Mise à l'échelle des repères à 66 kt :**
  - Pruvia : 0,86 × 66 = 57 ETP.
  - Quantafuel Sunderland : 66 ETP.
  - Usine d'incinération de Béthune : 0,30 × 66 = 20 ETP.
- **Tri, à 6-9 t/h :**
  - Avec le ratio de Bègles (3,5 emplois par t/h), on obtient 21 à 32 emplois.
  - Bègles est un centre de tri de collecte sélective, avec beaucoup de tri manuel. Un pré-tri mécanique de déchets en mélange en demande moins.
- **Arithmétique des quarts :**
  - En continu à 5 équipes, 15 ETP correspondent à 3 personnes par quart.
  - Cela ne compte ni congés ni formation au-delà de ce que prévoit déjà le roulement à 5 équipes.

### Verdict
**Hors fourchette (bas) par rapport aux repères pyrolyse.**
- Le total de 22 ETP est cohérent avec une usine d'incinération mature (environ 20 ETP à l'échelle).
- Il est 2,5 à 3 fois inférieur aux deux repères pyrolyse (57 à 66 ETP).
- `etp_tri = 7` est inférieur aux repères des centres de tri d'emballages, mais ces repères ne correspondent pas au même procédé.
- **Réserves :** les chiffres de presse sont des « emplois » et non des ETP, et le repère de Sunderland est un projet de 2022.
- **Recommandation :** obtenir le plan d'armement du constructeur, ou porter l'hypothèse de base à 30-40 ETP avec une sensibilité.

---

## 3. assurance = 0,5 % du CAPEX par an

### Éléments lus
- **Incinérateur de Perham (US), PRM-PERHAM-INSURANCE-2021**
  - Prime passée de « $76,000 last year » à « about $530,000 a year ».
  - Valeur assurée : « nearly $48 million ».
  - **Calcul :** 530 / 48 000 = **1,10 %** de la valeur assurée après la hausse, contre **0,16 %** avant.
  - Raison donnée : le réassureur historique a refusé de couvrir les usines de valorisation énergétique.
  - Source ancienne (2021), contexte américain.
- **Usine de valorisation énergétique de Severnside, West London Waste Authority (PRM-LETSRECYCLE-WLWA-2023)**
  - « Insurance premiums have increased by 518% since 2016 ».
  - « insurers' appetite to risk in relation to waste facilities has continued to deteriorate ».
  - Pour une usine de tri mécano-biologique (Dumfries & Galloway), une hausse de 90 % est annoncée.
- **Sénat, rapport du 19/02/2025 (PRM-SENAT-PPL24-079-2025)**
  - « une hausse exponentielle des primes d'assurance » pour les exploitants.
  - Les batteries au lithium sont « à l'origine de 24 incendies en 2023 ».
- **Sénat, réponse ministérielle du 12/06/2025 (PRM-SENAT-QE04832-2025)**
  - Le ministère attend, à terme, « la baisse des primes et des franchises exigées par les compagnies d'assurance ». C'est une prévision, sans chiffre.
- **FEDEREC, 28/02/2025 (PRM-FEDEREC-INCENDIES-2025)**
  - « 1 incendie toutes les deux semaines dans les centres de collecte, de tri et de recyclage en France ».
  - « Des dégâts matériels estimés jusqu'à 100 millions d'euros par an pour la profession ».
- **Intratec (PRM-INTRATEC-OPEX-METHOD)**
  - Taxes foncières et assurance : « A percentage of the fixed capital per year ».
  - Aucun pourcentage n'est donné.
- **La Crau Énergies Vertes, biogaz (PRM-LCEV-RAD-2020)**
  - « Le montant de la prime d'assurance de la police dommages-bris de machines s'élève à 78 880 € en 2020 ».
  - La valeur assurée n'est pas donnée, donc aucun pourcentage ne peut être calculé.

### Verdict
**Aucune source française ne donne le taux de prime.**
- La seule donnée chiffrée (US, 2021) donne 1,1 % de la valeur assurée après la hausse.
- Le durcissement du marché de l'assurance des déchets est documenté en France (Sénat, FEDEREC) et au Royaume-Uni.
- **0,5 % est probablement sous-estimé** pour une première installation de traitement thermique de déchets.
- **Recommandation :**
  - Obtenir une cotation d'un courtier, sur la base des dommages, du bris de machine et des pertes d'exploitation.
  - Tester une sensibilité entre 0,5 et 1,1 %.

---

## 4. provision = 2 % du CAPEX par an (contenu non défini)

### Ce que recouvre une telle provision
- **GER, « gros entretien et renouvellement » (PRM-BXM-DSP-UVE-2026)**
  - Dans les concessions françaises, le concessionnaire doit « Assurer l'entretien courant, les opérations de gros entretien et grande visite ». Il assure aussi le renouvellement des ouvrages et des équipements.
  - Le tarif « inclut notamment les coûts d'exploitation, d'entretien courant et de gros entretien grandes visites (GEGV) ».
  - Travaux à moyen terme sur deux usines de valorisation énergétique et un centre de tri : « estimées entre 15 et 34 millions d'euros » pour 2028-2035.
- **Traitement comptable (PRM-LCEV-RAD-2020)**
  - « La provision GER a été donc intégralement reprise au 31.12.2019 pour le montant de 1 157 249 € ».
  - Le GER est désormais immobilisé au moment où il est réalisé. C'est la même question que celle des composants : charge provisionnée ou CAPEX de renouvellement.
- **Usine d'incinération de Béthune (PRM-BETHUNE-RAD-CVE-2021)**
  - GER de 2021 : « 1 595 731 € HT (incluant achats sur stock) ».
  - Le tableau de la p. 26 indique 1 585 023 €, ce qui ne concorde pas exactement.
  - Postes principaux : réfection des carneaux et des voûtes (427 745 €), production de vapeur (359 838 €).
  - La valeur à neuf n'est pas donnée, donc le pourcentage n'est pas calculable.

### Ordre de grandeur
- Intratec (PRM-INTRATEC-OPEX-METHOD) : la maintenance « typically ranges from 1% to 4% of plant cost per year » (contexte américain).

### Verdict
**Confirmé dans la fourchette de 1 à 4 %, mais le contenu doit être défini.**
- La provision de 2 % devrait couvrir le GER : grandes révisions, réfractaires, renouvellement des pièces d'usure et des équipements.
- **Point à contrôler :** l'absence de double comptage avec une éventuelle ligne de maintenance courante. Si le modèle n'a pas de ligne de maintenance séparée, 2 % se situe dans le bas de la fourchette d'Intratec.
- Les coûts de mise en service ne sont pas une provision. Tuin (2020) donne « range from 5 to 20 percent » du CAPEX pour la mise en service et le démarrage (PRM-TUIN-JBC-2020).

---

## 5. charbon_actif = 40 000 EUR/an

### Éléments lus
**Consommation**
- **Usine de valorisation énergétique d'Eastcroft, UK, 2019 (PRM-EASTCROFT-APR-2019)**
  - « Activated Carbon kgs 25,518 26,610 19,507 27,392 99,027 0.53 ».
  - Cela correspond à 99 t pour 188 213 t de déchets, soit **0,53 kg/t**.
  - Source ancienne (2019).
- **Lhoist, études de cas d'incinérateurs français (PRM-LHOIST-SORBACAL-2021)**
  - Adsorbant minéral « dosé à 0,3 kg par tonne de déchets incinérés ». Il s'agit du cas n°26, où il remplace du charbon actif livré « en vrac par 25 tonnes ».
  - Autre cas : « 0,9 kg de réactif par tonne de déchets ».
  - Ce n'est pas du charbon actif ; la valeur n'est qu'indicative.
- **Usine d'incinération de Béthune (PRM-BETHUNE-RAD-CVE-2021)**
  - « injection d'un mélange de bicarbonate de sodium et de charbon actif ». Aucun tonnage n'est donné.

**Prix**
- **IMARC (PRM-IMARC-AC-PRICE-2026), Allemagne :**

| Trimestre | Prix |
|---|---|
| T1 2025 | 2 298 USD/t |
| T3 2025 | 2 586 USD/t |
| T1 2026 | 2 664 USD/t |
| T3 2026 | 2 800 USD/t |

- **Intratec (PRM-INTRATEC-AC-PRICE-2025), Europe :** « reaching 1,880 USD per metric ton » en novembre 2025.
- **Conversion à 1,16 USD/EUR :** 1 621 €/t (Intratec) à 2 414 €/t (IMARC, T3 2026).

### Calculs
- Avec le repère d'Eastcroft : 66 000 t × 0,53 kg/t = 35 t/an. Coût : 35 × 1 621 à 2 414 €/t = **56 700 à 84 400 €/an**.
- Avec la valeur basse de Lhoist (0,3 kg/t) : 19,8 t/an, soit 32 100 à 47 800 €/an.
- Valeur du modèle : 40 000 € correspondent à 16,6 à 24,7 t/an, soit **0,25 à 0,37 kg/t** de déchets entrants.

### Verdict
**Hors fourchette (bas) par rapport au repère d'incinération (56 700 à 84 400 €).**
- La valeur reste plausible si la pyrolyse traite moins de fumées par tonne qu'un incinérateur classique.
- **[NON SOURCÉ]** Aucune source sur la consommation de charbon actif en pyrolyse n'a été trouvée.
- La consommation de charbon actif pour le traitement des eaux n'a pas été sourcée.
- **Recommandation :** obtenir la consommation garantie par le constructeur, ou retenir 60 000 à 85 000 €/an.

---

## 6. inflation = 2 %/an

### Éléments lus
**Banque de France, projections du 15/09/2026, France, IPCH (PRM-BDF-PROJ-2026-09)**
- « headline inflation is expected to rise to 2.3% in 2026 before falling back below the 2% target ».
- « coming in at 1.9% in 2027 and 1.6% in 2028 ».

| Indicateur | 2026 | 2027 | 2028 |
|---|---|---|---|
| IPCH total | 2,3 % | 1,9 % | 1,6 % |
| IPCH hors énergie et alimentation | 1,6 % | 2,3 % | 1,9 % |

**BCE, projections des services du 10/09/2026, zone euro (PRM-BCE-PROJ-2026-09)**
- « the baseline projections foresee HICP inflation picking up from 2.1% in 2025 to 3.0% in 2026 ».

| Indicateur | 2026 | 2027 | 2028 |
|---|---|---|---|
| IPCH total | 3,0 % | 2,5 % | 2,1 % |
| IPCH hors énergie et alimentation | 2,5 % | 2,6 % | 2,3 % |

### Verdict
**Confirmé comme hypothèse de long terme** : c'est la cible de 2 %, et la France revient sous 2 % en 2027-2028.
- Les années 2026-2027 sont au-dessus en zone euro (3,0 % et 2,5 %), et la France est à 2,3 % en 2026.
- **Option :** indexer la première année à 2,3-2,5 %, puis 2 %.

---

## 7. charge_an1 = 70 % et charge_an2 = 85 %

### Éléments lus
**Études sur les usines pionnières**
- **RAND R-2569, Merrow et al. 1981 (PRM-RAND-R2569-1981)**
  - Portait sur 44 usines de procédé.
  - Résumé : « Misestimation of the capital costs and performance of innovative energy and chemical process plants ».
  - Le PDF est scanné et n'a pas pu être lu.
- **Résultats de Merrow repris par Jenike & Johanson, revue Processing, octobre 2023, p. 22 (PRM-PROCESSING-JJ-2023), pour les usines traitant des solides :**
  - « operated at less than 80% of their name-plate (design) capacity at the end of their first year ».
  - « with a quarter failing to reach even 40% ».
  - « The average for this cohort was 64% of name-plate compared to 90-95% for the liquid and gas operations. »
  - « only 6% had no major performance issues ».
- **Bates, 2022 (PRM-BULKONLINE-BATES-2022) :** ces usines « rarely achieved their full design rating of output ».
- **Tuin 2020, citant Merrow 2011 (PRM-TUIN-JBC-2020) :** « the start-up time can be five times that when proven technology is used ».
- **NREL, usine mature (« nth plant »), 2015 (PRM-NREL-62455-2015)**
  - Démarrage de 6 mois, avec un chiffre d'affaires à 50 % du normal, puis « 90% (7,884 operating hours per year) ».
  - **Calcul :** l'année 1 représente 0,5 × 50 % + 0,5 × 100 % = 75 % du régime normal, **pour une usine mature**.

**Cas réels**
- **Quantafuel Skive, 10/01/2022 (PRM-QUANTAFUEL-SKIVE-2022)**
  - Objectif 2022 : 12 000 t traitées, pour un régime de 20 000 t/an en fin d'année. **Calcul : 60 %.**
  - « the runs were cut short by mechanical failures in the feeding systems ».
- **TotalEnergies et Plastic Energy, Grandpuits, 15 kt/an (PRM-TOTAL-GRANDPUITS-2026)**
  - Production démarrée en mars 2026. Aucune donnée de montée en charge n'est publiée.
- **Brightmark, Ashley (PRM-WASTEDIVE-BRIGHTMARK-2025)**
  - Financement bouclé en 2019 ; en 2025 l'usine fonctionne « currently only operating at 5% capacity ».
  - Faillite (Chapter 11) le 17/03/2025.
- **Fulcrum Sierra (PRM-WASTEDIVE-FULCRUM-2024)**
  - Prévue pour 175 000 t de déchets ménagers par an.
  - « shipped only a small amount of synthetic crude in late 2022 before shutting down for repairs ».
  - Arrêt total en mai 2024, faillite en septembre.

### Verdict
**Hors fourchette (optimiste).**
- 70 % en année 1 dépasse la moyenne de Merrow pour les usines de solides, qui est de 64 % **à la fin** de l'année 1 ; la moyenne de l'année est donc inférieure.
- 70 % dépasse aussi le plan de Quantafuel (60 %) et approche l'hypothèse du NREL pour une usine mature (75 %).
- **Plage sourcée ou calculée :**
  - Année 1 : environ 40 à 64 %, avec 25 % des cas sous 40 %.
  - Année 2 : 85 % n'est atteint que si le démarrage réussit.
- **Recommandation :**
  - Scénario de base : 50 à 60 % en année 1, 75 à 80 % en année 2.
  - Scénario dégradé : 40 % puis 60 %.

---

## 8. taux_interet = 12 % avec 70 % de dette, et duree_amortissement = 15 ans

### Taux d'intérêt

**Banque de France, financement des entreprises, juin 2026, publié le 10/08/2026 (PRM-BDF-FINENT-2026-06)**
- « Le taux d'intérêt moyen des nouveaux financements augmente à 3,64 % en juin. »

| Catégorie | Taux |
|---|---|
| Crédits de plus de 1 M€ | 3,61 % |
| Grandes entreprises | 3,51 % |
| ETI | 3,87 % |
| Crédit d'équipement (avril 2026, mesure TESE) | 3,57 % |

**BCE, hypothèses techniques de septembre 2026 (PRM-BCE-PROJ-2026-09)**

| Indicateur | 2026 | 2027 | 2028 |
|---|---|---|---|
| EURIBOR 3 mois | 2,4 % | 3,0 % | 3,0 % |
| Taux souverains à 10 ans (zone euro) | 3,5 % | 3,8 % | 4,0 % |

**Marges en financement de projet déchets**
- **IJGlobal, 2011, contrats PFI déchets au Royaume-Uni (PRM-IJGLOBAL-WASTE-PFI-2011), source ancienne :**
  - « priced at around 300bp over Libor ».
  - « 450bp from year 16 onwards ».
  - Les PFI sont financés à « high 80s or low 90s » de dette, avec « far more variation » pour les déchets.
- **NREL, 2015 (PRM-NREL-62455-2015) :** 60 % de dette, 8 %, 10 ans (usine mature, US, ancien).

**Calcul**
- 3,0 % (EURIBOR 2027-2028) + 300 à 450 pb = **6,0 à 7,5 %** pour une dette de projet déchets avec revenus contractés.
- 12 % représente 3,3 fois le taux moyen de la Banque de France.

**Verdict : hors fourchette (haut) pour une dette senior.**
- La combinaison « 70 % de dette à 12 % » est incohérente :
  - Une dette senior coûterait plutôt 6 à 8 %.
  - Pour une première de série, 70 % de dette senior est peu probable. **[NON SOURCÉ]** Aucune source sur le taux d'endettement des premières de série n'a été lue.
- **Recommandation :**
  - Soit modéliser une dette senior à 6-8 % avec un endettement plus faible.
  - Soit présenter 12 % comme un coût mixte incluant mezzanine ou fonds propres.
- Aucune source BPI ou BEI n'a été consultée, faute de budget de recherche.

### Durée d'amortissement

**BOFiP BOI-BIC-AMT-10-40-30, version du 23/09/2013 (PRM-BOFIP-AMT-10-40-30-2013)**, « taux usuels », « donnée à titre purement indicatif » :

| Catégorie | Taux annuel | Durée correspondante |
|---|---|---|
| Matériel | « 10 à 15 % » | 6,7 à 10 ans |
| Bâtiments industriels | 5 % | 20 ans |
| Agencements, installation | « 5 à 10 % » | 10 à 20 ans |

**BOFiP BOI-BIC-AMT-10-40-10, § 240 (PRM-BOFIP-AMT-10-40-10-2013)**
- L'administration ne remet pas en cause une durée qui s'écarte de moins de 20 % de l'usage.
- **Calcul :** pour le matériel, la durée maximale tolérée est donc de 12 ans.

**Verdict : dans la fourchette pour un taux mixte unique (entre 10 et 20 ans), mais au-dessus de l'usage fiscal pour le matériel.**
- **Recommandation :** séparer machine (10 ans, 12 ans au maximum) et bâtiments (20 ans).
- Une durée économique de 15 ans reste défendable en comptabilité (durée d'utilisation selon le PCG).

---

## Tableau final

| Paramètre | Valeur actuelle | Valeur ou plage sourcée | Sources | Verdict |
|---|---|---|---|---|
| cout_etp | 56 000 €/an | 48 700 à 63 800 € (opérateur 5x8, calculé). Plancher conventionnel de 46 000 à 52 000 €. Moyenne du secteur E d'environ 70 000 € (heures non sourcées). | PRM-IDCC2149-AV79-2025, PRM-TRAVIND-IDCC2149-2026, PRM-FT-OFFRE-UVE-DOMONT-2025, PRM-CIDJ-CONDUCTEUR-UVE-2025, PRM-EUROSTAT-LCLEV-E-TOTAL-2025, PRM-EUROSTAT-LCLEV-E-D11-2025, PRM-TRAVIND-COTIS-2026 | confirmé |
| etp_coeur_base | 15 ETP | Environ 20 ETP (incinérateur mature, mis à l'échelle). 57 à 66 ETP au total (pyrolyse, mis à l'échelle). | PRM-BETHUNE-RAD-CVE-2021, PRM-PRUVIA-GENDORF-2025, PRM-QUANTAFUEL-SUNDERLAND-2022 | hors fourchette (bas) par rapport à la pyrolyse |
| etp_tri | 7 ETP | 21 à 32 emplois à 6-9 t/h (centre de tri d'emballages, procédé différent). Unité CSR : environ 20 postes pour 30 kt. | PRM-BXM-CENTRETRI-2023, PRM-NORMANTRI-CP-2025, PRM-PAPREC-BRIVE-CSR | hors fourchette (bas), repère imparfait |
| assurance | 0,5 % du CAPEX | 1,1 % (US 2021, après la hausse). Durcissement documenté en France et au Royaume-Uni. | PRM-PERHAM-INSURANCE-2021, PRM-LETSRECYCLE-WLWA-2023, PRM-SENAT-PPL24-079-2025, PRM-FEDEREC-INCENDIES-2025 | aucune source directe (probablement sous-estimé) |
| provision | 2 % du CAPEX | Maintenance et GER de 1 à 4 % du coût de l'usine par an | PRM-INTRATEC-OPEX-METHOD, PRM-BXM-DSP-UVE-2026, PRM-BETHUNE-RAD-CVE-2021, PRM-LCEV-RAD-2020 | confirmé (contenu GER à définir) |
| charbon_actif | 40 000 €/an | 56 700 à 84 400 €/an (0,53 kg/t × 66 kt × 1 621 à 2 414 €/t) | PRM-EASTCROFT-APR-2019, PRM-LHOIST-SORBACAL-2021, PRM-IMARC-AC-PRICE-2026, PRM-INTRATEC-AC-PRICE-2025, PRM-BCE-PROJ-2026-09 | hors fourchette (bas) |
| inflation | 2 %/an | France : 2,3 / 1,9 / 1,6 % (2026-2028). Zone euro : 3,0 / 2,5 / 2,1 %. Cible : 2 %. | PRM-BDF-PROJ-2026-09, PRM-BCE-PROJ-2026-09 | confirmé (long terme) |
| charge_an1 | 70 % | Environ 40 à 64 % (solides, première de série). Plan Quantafuel : 60 %. Usine mature NREL : 75 %. | PRM-PROCESSING-JJ-2023, PRM-QUANTAFUEL-SKIVE-2022, PRM-NREL-62455-2015, PRM-RAND-R2569-1981 | hors fourchette (optimiste) |
| charge_an2 | 85 % | Atteignable seulement si le démarrage réussit. Échecs documentés : Brightmark à 5 %, Fulcrum arrêtée. | PRM-PROCESSING-JJ-2023, PRM-WASTEDIVE-BRIGHTMARK-2025, PRM-WASTEDIVE-FULCRUM-2024 | optimiste (pas de plage chiffrée pour l'année 2) |
| taux_interet | 12 % (70 % de dette) | 3,6 % (moyenne des nouveaux crédits aux entreprises en France). 6,0 à 7,5 % calculé pour une dette de projet (EURIBOR 3 % + 300 à 450 pb). | PRM-BDF-FINENT-2026-06, PRM-BCE-PROJ-2026-09, PRM-IJGLOBAL-WASTE-PFI-2011 | hors fourchette (haut), incohérent avec 70 % de dette |
| duree_amortissement | 15 ans | Matériel : 6,7 à 10 ans (12 ans avec la tolérance). Bâtiments : 20 ans. Installations : 10 à 20 ans. | PRM-BOFIP-AMT-10-40-30-2013, PRM-BOFIP-AMT-10-40-10-2013 | dans la fourchette en taux mixte ; à scinder |

## Pages consultées sans contenu exploitable (absentes du YAML)

- **Page URSSAF des taux de cotisations du secteur privé** : accès bloqué par robots.txt.
- **Grand Reims, note sur la valorisation des déchets (2023)** : page JavaScript, contenu non lu.
- **Page d'accueil Eurostat Statistics Explained** : aucune donnée.
- **LégiFiscal, durées d'amortissement** : contenu payant.
- **PDF RAND R2569** : scan sans texte.
- **Diapositives NREL fy22osti/81884** : aucun paramètre.
- **Tableau 32 du NREL 62455** : non extrait (texte du PDF limité aux premières sections).
- **Le Journal des Entreprises, article PSI Environnement** : accès bloqué par robots.txt.
- **Société Générale, article sur un projet déchets et énergie** : erreur de chargement.
