# Urban Rig URC-2000 : sourcing des paramètres de prix

Consultation du 2026-10-10. Registre des sources : `prix.yaml` (identifiants `PRM-...`).

## Méthode et limites

- Seuls les contenus réellement lus via WebFetch sont cités. Les « citations » sont celles que l'outil de lecture a renvoyées comme verbatim. Pour les tableaux PDF dont le texte extrait était désaligné (Syctom p. 23, colonnes DGEC), il faut contrôler la valeur sur l'original avant de la figer.
- Environ 40 recherches web ont été faites, comme demandé. Les pistes restées non lues sont listées à la fin.
- **Conversion USD → EUR.** Quand une conversion était nécessaire, le taux utilisé est 1 € = 1,174 USD. Il est déduit de la note DGEC de décembre 2025, qui donne le même produit à 371 USD/t et 316 €/t (PRM-DGEC-NPG-2025-12). C'est un taux de calcul, pas une source de change officielle.
- **Informations déjà connues, contrôlées dans cette session :**
  - *Marseille 159 € HT/t* : **confirmé** (PRM-AMP-TARIFS-2025), mais **hors TGAP et hors TVA**, pour l'année 2025.
  - *Syctom 2024 (OMR 109,4 €/t, anomalies de tri 129,4 €/t)* : **confirmé** (PRM-SYCTOM-RA-2024, p. 23).
  - *ADEME référentiel 2023 (incinération 107 €/t, stockage 138 €/t)* : **non retrouvé**. La seule page ADEME lue porte sur un référentiel de données 2019, et son PDF n'était pas téléchargeable. Ne pas citer ces chiffres tant que le document n'a pas été lu.
  - *SITOM Nord-Isère 121 € HT/t* et *indices FEDEREC* : **non lus** dans cette session.

---

## 1. gate_fee : 110 €/t

### Preuves

| Source | Flux | Valeur | Année | TGAP | Fiabilité |
|---|---|---|---|---|---|
| PRM-SYCTOM-RA-2024 (p. 23) | OMr | **109,4 €/t** | 2024 | Le Syctom verse la TGAP à l'État. L'inclusion dans le tarif n'est pas écrite. | Tarif public (syndicat) |
| PRM-SYCTOM-RA-2024 (p. 23) | Anomalies de tri | **129,4 €/t** | 2024 | idem | Tarif public |
| PRM-SYCTOM-RA-2024 (p. 23) | Encombrants / tout-venant | 109,4 €/t (attribution probable) | 2024 | idem | Tarif public (lecture à confirmer) |
| PRM-AMP-TARIFS-2025 (annexe 4) | Encombrants et déchets assimilables aux OMR | **159 € HT/t** | 2025 | **Hors TGAP et hors TVA** | Tarif public (délibération) |
| PRM-AMP-TARIFS-2025 (annexe 3) | Idem, apport en centre de transfert ou plateforme | 303 € HT/t | 2025 | non précisé | Tarif public |
| PRM-BOFIP-TGAP-2025 | TGAP stockage, « autres installations autorisées » | 61 / 63 / **65 €/t** | 2023 / 2024 / 2025 | sans objet | Réglementaire |
| PRM-BOFIP-TGAP-2025 | TGAP traitement thermique, « autres installations autorisées » | 23 / 24 / **25 €/t** | 2023 / 2024 / 2025 | sans objet | Réglementaire |
| PRM-DREAL-PDL-2024 | Majoration TGAP stockage au-delà de l'objectif | 5 à 10 €/t | dès 2025 | sans objet | Administration |

Citations :
- Syctom : « Anomalies de tri : 129,4 €/t » et « Le Syctom verse à l'État une Taxe générale sur les activités polluantes (TGAP) portant sur les déchets. »
- AMP : « Les tarifs s'entendent hors toutes taxes (TVA + TGAP). »
- BOFiP : « Autres installations autorisées | Tonne | 61 | 63 | 65 » (stockage) et « Autres installations autorisées | Tonne | 23 | 24 | 25 » (traitement thermique).

### Calculs à partir des sources

AMP 2025, TGAP comprise (hors TVA). La destination (UVE ou ISDND) n'est pas précisée par AMP, d'où deux bornes :
- si les déchets sont incinérés : 159 + 25 = **184 €/t** ;
- si les déchets sont stockés : 159 + 65 = **224 €/t**.

### Lecture

- Le modèle (110 €/t) est **égal au tarif OMr du Syctom 2024 (109,4 €/t)**. C'est la référence pertinente pour les OMR d'Île-de-France, puisque le Syctom traite les déchets de 82 communes.
- Le modèle est sous le tarif « anomalies de tri » du Syctom (129,4 €/t) et nettement sous les tarifs publics de Marseille (159 € HT/t hors TGAP, soit 184 à 224 €/t TGAP comprise).
- Aucun prix de marché DAE en Île-de-France n'a été trouvé.
- Aucun tarif Syctom 2025 ou 2026 n'a pu être lu : le rapport d'activité 2025 est tronqué à l'extraction et l'infographie n'est pas lisible.
- Le barème TGAP lu s'arrête à 2025.

**Verdict : confirmé, en borne basse.** 110 €/t est cohérent avec le tarif public francilien pour les OMR. Il est prudent par rapport aux refus de tri (129,4) et aux tarifs professionnels hors Île-de-France (≥ 159 hors TGAP).

**Fiabilité :** tarifs publics et barème réglementaire (bonne). Deux limites : le statut « TGAP incluse » du tarif Syctom n'est pas écrit explicitement, et la lecture du schéma p. 23 est à confirmer.

---

## 2. prix_huile_combustible : 350 €/t

### Preuves

| Source | Contenu | Année | Fiabilité |
|---|---|---|---|
| PRM-DGEC-NPG-2025-12 | Fioul lourd TBTS (< 1 % S), cotation Rotterdam : **316 €/t** (déc. 2025, provisoire) et **326 €/t** (nov. 2025). Brent daté 457 USD/t (déc. 2025). | 2025 | Statistique publique (attribution des colonnes déduite) |
| PRM-INSEE-EACEI-2024 | Fioul lourd payé par l'industrie française : **576 €/t (2024)**, 585 (2023), 727 (2022) | 2024 | Statistique publique |
| PRM-SDES-PETROLE-2026 | Brent moyen 2025 : 69 USD/bbl d'après le texte français, 64 USD/bbl d'après la version anglaise (incohérence) | 2025 | Statistique publique |
| PRM-IMARC-PYRO-2026 | « Pyrolysis oil », Allemagne : 647 à 683 USD/t (T1 2025 à T3 2026), sans origine, qualité ni base | 2025-26 | Teaser commercial, non vérifiable |
| PRM-BESTON-PYRO-INDEX | Avant 2020 : huile de pyrolyse ≈ 60-70 % du prix du brut (paraphrase). Pic 2022 : 900 USD/t en Europe. | n.d. | Fabricant, secondaire |
| PRM-FIVGA-2018 | Substitut de fioul lourd issu de plastiques : coût de 0,87 £/kg à 100 kg/h, « 58% higher than current market prices » | 2018 | Étude académique |
| PRM-ICIS-PLASTICSTODAY-2023, PRM-ICIS-MPW-OVERVIEW, PRM-ARGUS-PYRO-2024 | Index lancés (qualités craqueur et raffinerie), **aucune valeur publique**, aucune référence au fioul | 2023-24 | Presse / indices |

Citations :
- DGEC : « Fioul lourd TBTS (< 1%) (en €/t) 316 326 -9 323 349 -26 »
- ICIS : « Pyrolysis oil prices do not track their virgin equivalents »

### Calculs à partir des sources

- **Parité avec le fioul lourd en gros (Rotterdam, LSFO < 1 % S), fin 2025 :** 316 à 326 €/t. Le modèle est **7 à 11 % au-dessus**.
- **Ratio vendeur de 60-70 % du brut** (Beston) appliqué au Brent de décembre 2025 (457 USD/t, soit 389 €/t) : 274 à 320 USD/t, soit **234 à 272 €/t**.
- **Fioul lourd livré à l'industrie** (INSEE 2024) : 576 €/t. Le modèle en représente **61 %**.
- **IMARC Allemagne**, converti : environ 551 à 582 €/t. Ce niveau correspond plutôt aux qualités pour vapocraqueur qu'à un usage combustible, car la nature du produit n'est pas précisée. Ne pas utiliser pour le cas « combustible ».

### Lecture

- **Aucune cotation publique d'huile de pyrolyse vendue comme combustible n'a été trouvée.** ICIS et Argus ne publient pas leurs valeurs en accès libre.
- Les bornes calculées pour une vente en gros vont de 234 à 326 €/t (ratio au Brent, puis parité LSFO Rotterdam). 350 €/t n'est atteignable que dans un cas : une vente directe à un industriel utilisateur final, qui substitue du fioul lourd livré (576 €/t) et partage l'économie de logistique.
- Le contexte de fin 2025 était bas (Brent autour de 61 USD/bbl en décembre). Le SDES annonce un « rebond début 2026 », mais la page lue ne donne pas de chiffre.

**Verdict : aucune source directe ; hors fourchette (au-dessus) pour une vente en gros.** 350 €/t reste dans la fourchette indirecte [316 ; 576] seulement dans l'hypothèse d'une vente à un utilisateur final.

**Fiabilité :** les bornes sur le fioul lourd sont des statistiques publiques (bonnes). Le lien entre l'huile de pyrolyse et le fioul lourd n'est étayé que par des sources faibles (fabricant, teaser commercial).

---

## 3. prix_char : 100 €/t

### Preuves

| Source | Contenu | Fiabilité |
|---|---|---|
| PRM-EMERTON-RCB-2024 (p. 6) | rCB de pneus en Europe : 250 à 550 kt/an pour environ 265 à 530 MUSD, soit **≈ 960 à 1 060 USD/t** (calcul) | Étude de conseil |
| PRM-EBC-POSLIST-V10 | « biomass from municipal collection not allowed » ; « Plastic contamination must in total not exceed 10% » | Standard de certification |
| PRM-INSEE-EACEI-2024 | Prix industriels 2024 : houille **215 €/t**, coke de pétrole **254 €/t** | Statistique publique |
| PRM-KUPPENS-2014 | Charbon actif commercial ≈ 2 000 €/t (hors sujet, données anciennes) | Étude, ancienne |
| PRM-CHHABRA-2021 | Pyrolyse d'OMR (Inde) : aucun prix de char dans le résumé | Étude |

### Lecture

- **Aucun prix de marché trouvé pour un char issu de déchets mélangés.**
- Le rCB (≈ 1 000 USD/t) concerne des pneus et un produit post-traité. Il ne s'applique pas ici.
- Un char issu de déchets municipaux riches en plastiques est **exclu de la certification EBC** (biomasse de collecte municipale non admise, contamination plastique plafonnée à 10 %). Il n'a donc pas accès aux marchés biochar ni aux crédits C-sink de l'EBC. Puro.earth et IBI n'ont pas été lus.
- **Usage combustible.** Le plafond par tonne est donné par la houille et le coke de pétrole (215 à 254 €/t en 2024). Il faut ensuite corriger par le PCI et le taux de cendres : prix_char ≤ 254 × PCI_char / PCI_coke − manutention. Les PCI ne sont pas sourcés ici ; il faut les reprendre des données de composition du modèle.
- La possibilité que le char représente un **coût d'élimination** (valeur négative) n'a pas été sourcée.

**Verdict : aucune source trouvée.** 100 €/t n'est pas contredit, puisqu'il est inférieur au plafond houille et coke de pétrole, mais il n'est étayé par aucune source.

---

## 4. prix_elec : 0,15 €/kWh

### Preuves (Eurostat nrg_pc_205, France, hors TVA et taxes récupérables, X_VAT)

| Bande | 2023-S1 | 2023-S2 | 2024-S1 | 2024-S2 | 2025-S1 | 2025-S2 | 2026-S1 |
|---|---|---|---|---|---|---|---|
| ID (2 à 20 GWh/an), PRM-EUROSTAT-NRGPC205-ID-2025 | 0,2235 | 0,2032 | 0,1409 | 0,1446 | **0,1296** | **0,1212** | non publié |
| IE (20 à 70 GWh/an), PRM-EUROSTAT-NRGPC205-IE-2026 | – | – | 0,1136 | 0,1066 | 0,0995 | 0,0853 | **0,0979** |
| IE, hors toutes taxes (X_TAX) | – | – | 0,1083 | 0,1004 | 0,0928 | 0,0782 | 0,0891 |

- Moyenne 2025 en bande ID : **0,1254 €/kWh**. Moyenne 2024 : 0,1428 €/kWh.
- En bande IE, le prix remonte de 15 % entre 2025-S2 et 2026-S1.
- Le libellé de la série est « Electricity prices for industrial consumers - bi-annual data (from 2007 onwards) ». Mises à jour Eurostat : 2026-09-24 (ID) et 2026-10-09 (IE).

**Verdict : hors fourchette (au-dessus).** 0,15 €/kWh dépasse de 20 % la moyenne 2025 de la bande ID et de 4 % le maximum 2024. L'hypothèse est donc prudente. Une valeur sourcée serait 0,125 €/kWh (2025, bande ID). Le niveau de 2026 en bande ID n'est pas encore publié.

**Fiabilité :** statistique publique officielle (très bonne). CRE, SDES et Banque de France n'ont pas été lus.

---

## 5. prix_verre : 30 €/t

| Source | Contenu | Année | Fiabilité |
|---|---|---|---|
| PRM-CITEO-OBSREPRISE-2024 (p. 8 et p. 55) | Verre ménager de collecte séparée, option filière : **24,7 €/t**, plus une aide au transport de 9,6 €/t (soit 34,3 €/t pour une collectivité, aide comprise). Options fédérations et individuelle : non renseignées. | 2024 | Éco-organisme agréé, données de reprise réelles (bonne) |
| PRM-MAIREINFO-VERRE-2006 | 19,10 €/t (barème D) | 2006 | Ancien |

Citation Citeo (p. 8) : « Verre 24,7 - - »

**Lecture :** 24,7 €/t est le prix d'un calcin **propre, issu de collecte séparée**. Aucun prix n'a été trouvé pour du verre récupéré sur des déchets mélangés ou des résidus de pyrolyse. Un tel verre est a priori de moindre qualité, mais aucune source lue ne le chiffre. L'aide au transport de 9,6 €/t est réservée aux collectivités sous contrat ; elle n'est pas transposable à un opérateur privé.

**Verdict : hors fourchette (au-dessus).** 30 €/t dépasse de 21 % le meilleur prix de reprise publié (24,7 €/t en 2024).

---

## 6. prix_carbone : 50 €/t CO2

| Source | Contenu | Date | Fiabilité |
|---|---|---|---|
| PRM-INSTRAT-ETS-2025 | Moyenne EUA 2025, pondérée par les volumes d'enchère : **73,43 €/t**. Première enchère 2026 : 86,27 €/t. | 2026-01-08 | Think tank, secondaire (données d'enchères) |
| PRM-SPGLOBAL-EUA-2026-04 | ICE : 72,85 €/t (10/04/2026). Platts, contrat déc. 2026 : **73,67 €/t** (09/04/2026). Prévision S&P : 68 €/t au T2 2026, 72 €/t au T3 2026. | 2026-04-10 | Agence de prix (Platts), secondaire |

Citations :
- Instrat : « The average CO₂ allowance price in 2025 amounted to EUR 73.43 per tCO₂ »
- S&P : « EUA prices in 2026 are likely to trade in a range-bound but slightly weaker regime. »

Piste non retenue : la page gmk.center du 10/09/2026, titrée « European carbon prices are holding above €80/t », n'a pas pu être chargée. Son titre n'est donc pas utilisé comme preuve.

**Verdict : hors fourchette (en dessous).** 50 €/t est 27 à 42 % sous les niveaux 2025-2026 (68 à 86 €/t). Une valeur sourcée serait 73 €/t (moyenne 2025 ; contrat décembre 2026 en avril 2026). Aucune projection 2027-2030 n'a été lue.

Point à vérifier dans le modèle : le carbone y est-il un coût (installation soumise à l'ETS) ou un revenu évité ? Cela conditionne le sens de l'erreur. L'applicabilité de l'ETS n'a pas été sourcée ici.

---

## 7. prix_carbonate : 120 €/t

| Source | Contenu | Année | Fiabilité |
|---|---|---|---|
| PRM-GAB22-AMENDEMENTS-2022 (p. 3) | Calcaire simple (CaO 50-54 %) : **poudre 60-80 € HT/t** ; broyé/concassé 35-40 ; compacté/granulé 150-200. Livraison incluse ou non : non précisé. | tarifs 2022 | Association agricole (moyenne) |
| PRM-INTRATEC-CACO3-2025 | Europe (export FOB Espagne) : 205 USD/t, soit ≈ **175 €/t**. Qualité non précisée, chiffres présentés comme « illustratifs ». | nov. 2025 | Teaser commercial (faible) |
| PRM-IMARC-CACO3-2026 | Allemagne 284 à 296 USD/t, Pays-Bas 237 à 248 USD/t, soit ≈ **202 à 252 €/t** | T1-T2 2026 | Teaser commercial (faible) |
| PRM-CRAB-AMENDEMENT-2011 | Coût exprimé par hectare, inexploitable | 2011 | Ancien |

**Lecture :** l'écart va de 60-80 €/t (poudre agricole, France, 2022) à 175-252 €/t (indices commerciaux européens, qualité non précisée et probablement fines ou charges minérales). Aucun prix français « qualité neutralisation, livré » n'a été trouvé.

**Verdict : confirmé, dans la fourchette large [60 ; 252] €/t.** 120 €/t se situe au milieu. **Fiabilité faible :** il faut un devis fournisseur (Omya, Carmeuse, Lhoist, Imerys) pour la granulométrie et la livraison en Île-de-France.

---

## 8. cout_concentrat : 110 €/t

| Source | Contenu | Année | Fiabilité |
|---|---|---|---|
| PRM-GISTRID-TTD-2019 | Grille de tarifs de traitement, transferts transfrontaliers (€ HT/t) : forfait déchets non dangereux **100** (120 TTC) ; 16 10 02 déchets liquides aqueux non dangereux **100** ; 19 07 03 lixiviats non dangereux **100** ; 06 03 14 « sels solides et solutions » **375** ; 19 11 03* liquides aqueux dangereux 317 ; forfait déchets dangereux 1 250 | 2019-04-15 | Grille administrative (moyenne) : référence, pas cotation de marché |
| PRM-BOAMP-26-9802 | Osmose inverse mobile de lixiviats (Syndicat Centre Hérault) : 400 000 € HT estimés, sans prix unitaire | 2026 | Marché public, inexploitable en €/t |
| PRM-FRANCE-EVAPORATION | Évapo-concentration sur site : 5 €/m³ de fonctionnement, hors élimination du concentrat | n.d. | Fabricant, non applicable |
| PRM-AERMC-2012, PRM-EIN-QUADRO-2010 | Aucun coût de centre externe | 2010-12 | Ancien |

Citation GISTRID : « Déchets non dangereux = 100 € HT (120 TTC) »

**Lecture :** 110 €/t correspond au barème de référence pour un liquide aqueux non dangereux (100 € HT/t) avec une marge de 10 %. Si la saumure de CaCl2 relève d'un code « sels et solutions », la référence passe à 375 € HT/t, soit 3,75 fois plus. Si elle relève d'un code dangereux, elle passe à 317 € HT/t ou plus. Le code déchet applicable à un concentrat de neutralisation issu de pyrolyse de déchets n'a pas été vérifié ici : il faut lire la liste européenne des déchets, rubrique 19 01. La grille date de 2019 (7 ans) et sa finalité n'est pas précisée dans l'extrait lu.

**Verdict : confirmé, avec réserve.** La valeur est dans [100 ; 375] € HT/t, en borne basse, et la classification du déchet est un risque majeur.

---

## Tableau de synthèse

| Paramètre | Valeur modèle | Valeur ou fourchette sourcée | Année | IDs sources | Verdict |
|---|---|---|---|---|---|
| gate_fee | 110 €/t | 109,4 (Syctom OMr) ; 129,4 (Syctom anomalies de tri) ; 159 € HT/t hors TGAP, soit 184-224 TGAP comprise (AMP) | 2024-2025 | PRM-SYCTOM-RA-2024, PRM-AMP-TARIFS-2025, PRM-BOFIP-TGAP-2025, PRM-DREAL-PDL-2024 | **Confirmé** (borne basse = référence OMR Île-de-France) |
| prix_huile_combustible | 350 €/t | Aucune cotation directe. Bornes indirectes : 234-272 (60-70 % Brent, calcul) ; 316-326 (LSFO Rotterdam) ; 576 (fioul lourd livré à l'industrie) | 2024-2025 | PRM-DGEC-NPG-2025-12, PRM-INSEE-EACEI-2024, PRM-BESTON-PYRO-INDEX, PRM-SDES-PETROLE-2026, PRM-IMARC-PYRO-2026 | **Aucune source directe ; hors fourchette (au-dessus) pour une vente en gros** (ne tient que pour une vente à un utilisateur final) |
| prix_char | 100 €/t | Aucun prix de char de déchets mélangés. Plafond combustible par tonne : 215-254 (houille, coke de pétrole). rCB pneus ≈ 960-1 060 USD/t (non applicable). Exclusion EBC. | 2024 | PRM-INSEE-EACEI-2024, PRM-EMERTON-RCB-2024, PRM-EBC-POSLIST-V10 | **Aucune source trouvée** |
| prix_elec | 0,15 €/kWh | 0,121-0,130 (2025) ; 0,141-0,145 (2024), bande ID, hors TVA | 2024-2025 | PRM-EUROSTAT-NRGPC205-ID-2025, PRM-EUROSTAT-NRGPC205-IE-2026 | **Hors fourchette (au-dessus, prudent)** |
| prix_verre | 30 €/t | 24,7 (verre propre de collecte séparée, filière) ; 34,3 avec aide transport réservée aux collectivités | 2024 | PRM-CITEO-OBSREPRISE-2024 | **Hors fourchette (au-dessus)** |
| prix_carbone | 50 €/t CO2 | 73,43 (moyenne 2025) ; 72,85-73,67 (avril 2026) ; prévision 68-72 (T2-T3 2026) ; 86,27 (enchère janv. 2026) | 2025-2026 | PRM-INSTRAT-ETS-2025, PRM-SPGLOBAL-EUA-2026-04 | **Hors fourchette (en dessous)** |
| prix_carbonate | 120 €/t | 60-80 (poudre agricole FR, 2022) ; ≈ 175-252 (indices commerciaux UE, 2025-2026) | 2022-2026 | PRM-GAB22-AMENDEMENTS-2022, PRM-INTRATEC-CACO3-2025, PRM-IMARC-CACO3-2026 | **Confirmé** (fourchette large, fiabilité faible) |
| cout_concentrat | 110 €/t | 100 € HT/t (liquide aqueux ou lixiviat non dangereux) à 375 € HT/t (sels et solutions) | 2019 | PRM-GISTRID-TTD-2019 | **Confirmé avec réserve** (dépend du code déchet) |

## Pistes non lues (à traiter avant de figer les valeurs)

- Syctom : sous-pages budget 2025 et 2026, et pages 64-74 du rapport d'activité 2025 (tarifs 2025 et RPQS).
- ADEME : PDF du référentiel des coûts. Les chiffres 107 et 138 €/t ne sont pas retrouvés.
- SITOM Nord-Isère, mercuriales FEDEREC.
- Eurostat : comparaison UE27 (non retournée par l'API).
- CRE : mécanisme post-ARENH 2026.
- gmk.center (EUA, septembre 2026). Banque de France.
- Puro.earth et IBI : exclusions de matières premières.
- Devis carbonate de calcium « qualité neutralisation » livré en Île-de-France.
- Liste européenne des déchets, rubrique 19 01 (code du concentrat salin).
