# Gate Fees (Tipping Fees) - Reference Document
## Données de marché France et Europe pour le Business Plan Urban Rig

**Créé:** 2026-02-27
**Objectif:** Fournir des données de gate fees validées et sourcées pour le modèle financier
**Applicabilité:** France, Europe (business plan réplicable)

---

## Table des matières

1. [Définition et logique des gate fees](#1-definition)
2. [France - Données détaillées](#2-france)
3. [Europe - Comparaison par pays](#3-europe)
4. [Positionnement tarifaire Urban Rig](#4-positionnement)
5. [Sources](#5-sources)

---

## 1. Définition et logique des gate fees {#1-definition}

### Qu'est-ce qu'un gate fee ?

Le **gate fee** (ou tipping fee, ou tarif de traitement) est le prix payé par le producteur de déchets (municipalité, entreprise, aéroport) pour faire traiter ses déchets par une installation.

```
Producteur de déchets  ──► Paye gate fee (€/tonne) ──► Installation de traitement
(collectivité, usine)                                  (incinérateur, décharge, Urban Rig)
```

### Composition du coût total pour le producteur

```
Coût total = Gate fee (opérateur) + Taxes (TGAP en France) + Transport
```

En France :
- **Gate fee** : Prix facturé par l'installation (couvre CAPEX + OPEX + marge)
- **TGAP** : Taxe Générale sur les Activités Polluantes (payée à l'État)
- **Transport** : Variable selon distance (€10-30/tonne typiquement)

### Facteurs influençant les gate fees

| Facteur | Impact sur gate fee |
|---------|-------------------|
| Capacité de traitement disponible | Surplus = prix bas, pénurie = prix élevés |
| Réglementation (TGAP, CO2) | Taxes croissantes = prix croissants |
| Qualité du déchet | Déchet trié/homogène = moins cher |
| Contrat long-terme vs spot | Long-terme = remise, spot = premium |
| Concurrence locale | Plus de concurrence = prix bas |

---

## 2. France - Données détaillées {#2-france}

### 2.1 TGAP (Taxe Générale sur les Activités Polluantes)

La TGAP est une taxe française qui s'ajoute au gate fee pour décourager l'enfouissement et l'incinération.

#### Tarifs TGAP 2024-2025

| Mode de traitement | TGAP 2024 | TGAP 2025 | Évolution |
|-------------------|-----------|-----------|-----------|
| **Enfouissement (décharge)** | €61/t | **€65/t** | +€4/t |
| **Enfouissement (dépassement objectif)** | - | **€70/t** (+5€ majoration) | Nouveau |
| **Incinération sans valorisation** | €20/t | **€25/t** | +€5/t |
| **Incinération avec valorisation énergétique** | €12-15/t | €15-18/t | +€3/t |
| **Valorisation matière (recyclage, pyrolyse)** | **€0/t** | **€0/t** | Exempté |

**Source:** [Douanes françaises - Taux TGAP](https://www.douane.gouv.fr/fiche/taux-de-la-taxe-generale-sur-les-activites-polluantes-tgap), [UPCYCLE - TGAP 2024](https://www.upcycle.org/tgap-quest-ce-qui-change-en-2024/)

#### Avantage Urban Rig

Urban Rig est classé comme **valorisation matière** (recyclage chimique) → **Exempté de TGAP**

Cela crée un avantage compétitif de **€15-25/tonne** vs incinération et **€65/tonne** vs enfouissement.

---

### 2.2 Gate fees par type de traitement en France

#### Données SYCTOM (Île-de-France) - 2023/2024

| Type de déchet | Traitement | Gate fee (hors TGAP) | TGAP | **Coût total** |
|---------------|------------|---------------------|------|----------------|
| **Ordures ménagères (OMR)** | Incinération | €103/t | €15/t | **€118/t** |
| **Emballages triés** | Centre de tri | €19/t | €0 | **€19/t** |
| **Erreurs de tri (retour incin.)** | Incinération | €123/t | €15/t | **€138/t** |
| **Biodéchets** | Méthanisation | €35/t | €0 | **€35/t** |
| **Déchets verts** | Compostage | €65/t | €0 | **€65/t** |

**Source:** [SYCTOM - Rapport annuel 2023](https://www.syctom-paris.fr/), Denis Penouel (DG SYCTOM)

#### Données nationales ADEME/SINOE (2022)

| Mode de traitement | Gate fee moyen France | Fourchette |
|-------------------|----------------------|------------|
| **Incinération avec valorisation** | €85-110/t | €70-130/t |
| **Enfouissement (ISDND)** | €50-80/t (hors TGAP) | €40-100/t |
| **Centre de tri** | €80-120/t | €60-150/t |
| **Compostage** | €40-70/t | €30-90/t |
| **Méthanisation** | €50-90/t | €40-120/t |

**Source:** [ADEME - Référentiel des coûts](https://economie-circulaire.ademe.fr/cout-des-dechets), [SINOE](https://www.sinoe.org/)

#### Évolution Île-de-France 2019-2021

| Indicateur | 2019 | 2021 | Évolution |
|------------|------|------|-----------|
| Coût traitement OMR | Base | +20% | Hausse |
| Coût traitement encombrants | Base | +30% | Hausse forte |
| TGAP incinération | €3/t | €8/t | +167% |

**Source:** [Institut Paris Région](https://www.institutparisregion.fr/nos-travaux/publications/hausse-du-cout-du-service-public-des-dechets-en-ile-de-france-quelles-perspectives/)

---

### 2.3 Déchets spéciaux (premium pricing)

#### Déchets aéroportuaires (biosécurité)

| Type de déchet | Réglementation | Gate fee estimé | Notes |
|---------------|----------------|-----------------|-------|
| **Déchets internationaux (catering)** | IATA/ICAO - destruction obligatoire | €120-180/t | Pas de recyclage possible |
| **Déchets terminaux** | Standard | €100-130/t | Similaire MSW |
| **Déchets cargo** | Variable | €80-120/t | Dépend du contenu |

**Note:** Les déchets de vols internationaux doivent être détruits (incinération ou stérilisation) pour raisons de biosécurité (risque de transmission de maladies animales/végétales). Urban Rig avec son process thermique à 600°C répond à cette exigence.

#### DASRI (Déchets d'Activités de Soins à Risques Infectieux)

| Type | Gate fee | Notes |
|------|----------|-------|
| **DASRI non stérilisé** | €800-1200/t | Incinération spécialisée obligatoire |
| **DASRI post-stérilisation** | €150-250/t | Peut être traité comme déchet industriel |

**Source:** Estimation marché français, à valider avec collecteurs spécialisés

#### Composites (pales d'éoliennes)

| Situation | Solution actuelle | Gate fee | Urban Rig opportunity |
|-----------|------------------|----------|----------------------|
| Pales déclassées | Enfouissement ou export | €50-150/t | Alternative recyclage |
| Déchets aéronautiques composites | Enfouissement spécialisé | €100-200/t | Récupération fibre + huile |

**Source:** Études sectorielles éoliennes, à valider avec Veolia/SITA

---

## 3. Europe - Comparaison par pays {#3-europe}

### 3.1 Gate fees incinération par pays (2024)

| Pays | Gate fee (hors taxes) | Taxe CO2/incin. | **Coût total** | Tendance |
|------|----------------------|-----------------|----------------|----------|
| **Allemagne** | €70-100/t | €40-55/t (nEHS) | **€110-155/t** | ↗ Hausse (CO2) |
| **France** | €85-110/t | €15-18/t (TGAP) | **€100-128/t** | ↗ Hausse modérée |
| **Royaume-Uni** | £66-189/t (€80-220/t) | Prévu 2028 | **€80-220/t** | ↗ Hausse attendue |
| **Pays-Bas** | €80-120/t | Prévu | **€80-120/t** | → Stable |
| **Belgique** | €70-100/t | Variable | **€80-120/t** | → Stable |
| **Italie** | €80-130/t | Faible | **€85-140/t** | ↗ Hausse |
| **Espagne** | €50-80/t | Faible | **€55-90/t** | → Stable |
| **Pologne** | €40-60/t | Faible | **€45-70/t** | ↗ Hausse |

**Sources:**
- [EEA - Overview of taxes on incineration](https://www.eea.europa.eu/en/analysis/maps-and-charts/overview-of-taxes-on-the)
- [EUWID Recycling - German gate fees](https://www.euwid-recycling.com/news/markets/)
- [WRAP UK - Gate Fees Report 2024-25](https://www.wrap.ngo/resources/report/uk-gate-fees-report-2024-25)

### 3.2 Gate fees enfouissement par pays (2024)

| Pays | Gate fee (hors taxes) | Taxe landfill | **Coût total** |
|------|----------------------|---------------|----------------|
| **France** | €50-80/t | €65/t (TGAP) | **€115-145/t** |
| **Allemagne** | €80-120/t | Variable | **€100-150/t** |
| **Royaume-Uni** | €30-50/t | £126/t (€150/t) | **€180-200/t** |
| **Pays-Bas** | Interdit (sauf exceptions) | - | N/A |
| **Italie** | €40-80/t | €10-25/t | **€50-105/t** |
| **Espagne** | €30-60/t | €0-40/t | **€30-100/t** |

**Source:** [EEA - Overview of landfill taxes](https://www.eea.europa.eu/en/analysis/maps-and-charts/overview-of-landfill-taxes-on)

### 3.3 Impact EU ETS sur incinération (projection 2026-2030)

L'inclusion de l'incinération dans l'EU ETS est en discussion. Impact projeté :

| Scénario | Prix CO2 | Impact sur gate fee |
|----------|----------|-------------------|
| **Bas** | €67/t CO2 | +€40-60/t déchet |
| **Médian** | €100/t CO2 | +€60-90/t déchet |
| **Haut** | €184/t CO2 | +€125-225/t déchet |

**Source:** [Zero Waste Europe - Waste Incineration under EU ETS](https://zerowasteeurope.eu/wp-content/uploads/2025/06/CE_Delft_250247_Waste_Incineration_under_the_EU_ETS_2025-update.pdf)

**Implication pour Urban Rig:** L'inclusion de l'incinération dans l'EU ETS augmentera significativement les gate fees de l'incinération, rendant Urban Rig encore plus compétitif.

---

## 4. Positionnement tarifaire Urban Rig {#4-positionnement}

### 4.1 Logique de pricing

Urban Rig peut se positionner **à parité ou légèrement au-dessus** de l'incinération car :

1. **Exemption TGAP** : Urban Rig économise €15-18/t de taxe vs incinération
2. **Avantage environnemental** : Argument ESG pour municipalités/entreprises
3. **Conformité future EU ETS** : Pas de risque de hausse CO2
4. **Valorisation matière** : Contribution aux objectifs 65% recyclage EU

### 4.2 Grille tarifaire recommandée

#### France

| Type de déchet | Gate fee Urban Rig | Comparaison incinération | Justification |
|---------------|-------------------|-------------------------|---------------|
| **MSW municipal** | **€90-110/t** | €100-128/t (incl. TGAP) | Compétitif avec avantage TGAP |
| **Déchets industriels** | **€80-100/t** | €85-120/t | Volume, qualité plus prévisible |
| **Déchets aéroportuaires** | **€120-150/t** | €120-180/t (biosécurité) | Compliance + valorisation |
| **Plastiques industriels** | **€70-90/t** | N/A (recyclage mécanique) | Premium pour flux difficiles |
| **Composites (éoliennes)** | **€100-140/t** | €50-150/t (enfouissement) | Seule alternative recyclage |
| **EPS/Polystyrène** | **€60-80/t** | Difficile à traiter ailleurs | Volume faible, haute valeur |

#### Europe (adaptable par pays)

| Pays | Gate fee recommandé | Rationale |
|------|-------------------|-----------|
| **Allemagne** | €100-130/t | Aligné sur marché + avantage CO2 |
| **Royaume-Uni** | £80-120/t (€95-140/t) | Marché tendu, premium possible |
| **Italie** | €90-120/t | Capacité limitée au Nord |
| **Espagne** | €70-100/t | Marché plus compétitif |
| **Pologne** | €60-80/t | Marché émergent, prix bas |

### 4.3 Modèle financier - Hypothèses gate fees

#### Scénario CDG (France - Base case)

| Flux de déchets | Volume (t/an) | Gate fee | Revenu gate fees |
|----------------|---------------|----------|------------------|
| MSW Île-de-France | 35,000 | €100/t | €3,500,000 |
| Déchets aéroport CDG | 20,000 | €130/t | €2,600,000 |
| Industriel/Logistique | 10,000 | €90/t | €900,000 |
| Composites | 5,000 | €120/t | €600,000 |
| **TOTAL** | **70,000** | **€109/t moy** | **€7,600,000** |

#### Sensibilité

| Scénario | Gate fee moyen | Revenu gate fees | Impact vs base |
|----------|---------------|------------------|----------------|
| **Pessimiste** | €80/t | €5,600,000 | -26% |
| **Base** | €109/t | €7,600,000 | - |
| **Optimiste** | €130/t | €9,100,000 | +20% |

---

## 5. Sources {#5-sources}

### Sources officielles françaises

| Source | URL | Données |
|--------|-----|---------|
| ADEME - Coût des déchets | https://economie-circulaire.ademe.fr/cout-des-dechets | Référentiel coûts SPGD |
| SINOE | https://www.sinoe.org/ | Base de données déchets |
| Douanes - TGAP | https://www.douane.gouv.fr/fiche/taux-de-la-taxe-generale-sur-les-activites-polluantes-tgap | Tarifs officiels |
| SYCTOM | https://www.syctom-paris.fr/ | Tarifs IDF |
| Institut Paris Région | https://www.institutparisregion.fr/ | Études coûts IDF |
| ORDIF | https://www.ordif.fr/ | Observatoire déchets IDF |

### Sources européennes

| Source | URL | Données |
|--------|-----|---------|
| EEA - Taxes incinération | https://www.eea.europa.eu/en/analysis/maps-and-charts/overview-of-taxes-on-the | Comparaison EU |
| EEA - Taxes landfill | https://www.eea.europa.eu/en/analysis/maps-and-charts/overview-of-landfill-taxes-on | Comparaison EU |
| WRAP UK | https://www.wrap.ngo/resources/report/uk-gate-fees-report-2024-25 | Gate fees UK |
| EUWID Recycling | https://www.euwid-recycling.com/ | News marché EU |
| Zero Waste Europe | https://zerowasteeurope.eu/ | Études EU ETS |

### Sources sectorielles

| Source | Données |
|--------|---------|
| Zero Waste France | https://www.zerowastefrance.org/ | Analyses coûts incinération |
| AMORCE | https://amorce.asso.fr/ | Association collectivités |
| UPCYCLE | https://www.upcycle.org/ | Analyses TGAP |

---

## Historique du document

| Date | Modification |
|------|-------------|
| 2026-02-27 | Création initiale avec données France et Europe |

---

**Fin du document Gate Fees Reference**
