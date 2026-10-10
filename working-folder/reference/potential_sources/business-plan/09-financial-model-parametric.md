# 9. Modèle Financier Paramétrique Urban Rig

Ce document présente un modèle financier entièrement paramétrable permettant de simuler les projections financières d'un projet Urban Rig dans n'importe quel contexte géographique et économique.

---

## 9.1 Vue d'Ensemble

### Objectif du Modèle

Ce modèle permet à l'utilisateur de :
- **Ajuster tous les paramètres** selon le contexte local (prix, coûts, réglementation)
- **Visualiser l'impact financier** de chaque changement de paramètre
- **Générer les ratios financiers** scrutés par les investisseurs
- **Simuler différents scénarios** (conservateur, base, optimiste)

---

## 9.2 PARAMÈTRES D'ENTRÉE (Variables Ajustables)

### 9.2.1 Configuration de l'Installation

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| **Nombre de machines** | N_machines | unités | 1 | 1-10 | Nombre d'unités Urban Rig déployées |
| **Type de machine** | Type | - | UR-200 | UR-50/UR-100/UR-200/UR-500 | Modèle de machine |
| **Capacité journalière** | Cap_jour | tonnes/jour | 200 | 50-500 | Capacité nominale par machine |
| **Taux d'utilisation** | Util | % | 85% | 70%-95% | Disponibilité opérationnelle annuelle |
| **Jours d'opération/an** | Jours_op | jours | 350 | 300-365 | Jours de fonctionnement par an |

**Capacité Annuelle Calculée** :
```
Capacité_annuelle = N_machines × Cap_jour × Util × Jours_op
```

---

### 9.2.2 Investissement (CAPEX)

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| **Coût équipement/machine** | CAPEX_equip | €/machine | 10,000,000 | 3M-15M | Coût de l'équipement Urban Rig |
| **Génie civil & site** | CAPEX_civil | € | 5,000,000 | 2M-10M | Terrassement, bâtiments, raccordements |
| **Permis & ingénierie** | CAPEX_permis | € | 2,000,000 | 500K-4M | Études, autorisations, conception |
| **Fonds de roulement initial** | BFR_init | € | 1,000,000 | 500K-3M | Trésorerie de démarrage |
| **Contingence** | Contingence | % | 10% | 5%-20% | Provision pour imprévus |

**CAPEX Total Calculé** :
```
CAPEX_total = (N_machines × CAPEX_equip + CAPEX_civil + CAPEX_permis + BFR_init) × (1 + Contingence)
```

---

### 9.2.3 Financement

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| **Ratio dette/fonds propres** | D/E | ratio | 70/30 | 50/50 - 80/20 | Structure de financement |
| **Taux d'intérêt dette** | i_dette | %/an | 5.0% | 3%-10% | Coût de la dette senior |
| **Durée du prêt** | Durée_prêt | années | 10 | 5-15 | Maturité de la dette |
| **Période de grâce** | Grâce | années | 1 | 0-2 | Période sans remboursement principal |
| **Coût des fonds propres** | Ke | %/an | 15% | 10%-25% | Rendement exigé par actionnaires |
| **Subventions CAPEX** | Subv_CAPEX | % | 0% | 0%-40% | Aides publiques à l'investissement |

**Calculs de Financement** :
```
Montant_dette = CAPEX_total × (D / (D + E)) × (1 - Subv_CAPEX)
Fonds_propres = CAPEX_total × (E / (D + E)) × (1 - Subv_CAPEX)
Service_dette_annuel = Montant_dette × [i × (1+i)^n] / [(1+i)^n - 1]  (annuité constante)
WACC = (E/(D+E)) × Ke + (D/(D+E)) × i_dette × (1 - Taux_IS)
```

---

### 9.2.4 Revenus - Gate Fees (Tipping Fees)

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| **Gate fee MSW** | GF_MSW | €/tonne | 100 | 50-200 | Frais de traitement déchets ménagers |
| **Gate fee industriel** | GF_ind | €/tonne | 120 | 60-250 | Frais déchets industriels |
| **Gate fee aéroportuaire** | GF_aero | €/tonne | 150 | 80-300 | Frais déchets aéroportuaires |
| **Mix feedstock MSW** | Mix_MSW | % | 60% | 0%-100% | Part du MSW dans le mix |
| **Mix feedstock industriel** | Mix_ind | % | 30% | 0%-100% | Part industriel |
| **Mix feedstock aéro** | Mix_aero | % | 10% | 0%-100% | Part aéroportuaire |
| **Croissance gate fees** | g_GF | %/an | 2% | 0%-5% | Inflation des gate fees |

**Gate Fee Moyen Pondéré** :
```
GF_moyen = GF_MSW × Mix_MSW + GF_ind × Mix_ind + GF_aero × Mix_aero
Revenus_GF_an = Capacité_annuelle × GF_moyen
```

---

### 9.2.5 Revenus - Produits Valorisés

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| **HUILE DE PYROLYSE** | | | | | |
| Rendement huile | Rdt_huile | % masse input | 30% | 20%-40% | % de l'input converti en huile |
| Prix huile pyrolyse | P_huile | €/tonne | 500 | 300-800 | Prix de vente FOB |
| Croissance prix huile | g_huile | %/an | 2% | -2% à +5% | Évolution annuelle du prix |
| **BIOCHAR/CARBONE** | | | | | |
| Rendement biochar | Rdt_char | % masse input | 18% | 10%-25% | % de l'input converti en char |
| Prix biochar (agricole) | P_char_agri | €/tonne | 150 | 80-400 | Prix pour usage agricole |
| Prix biochar (industriel) | P_char_ind | €/tonne | 100 | 50-200 | Prix pour usage combustible |
| Mix biochar agricole | Mix_char_agri | % | 50% | 0%-100% | Part vendue en agricole |
| Croissance prix char | g_char | %/an | 3% | 0%-10% | Évolution annuelle |
| **MÉTAUX RÉCUPÉRÉS** | | | | | |
| Rendement métaux | Rdt_metal | % masse input | 7% | 3%-12% | % de l'input en métaux |
| Prix métaux (moyenne) | P_metal | €/tonne | 300 | 150-600 | Prix moyen pondéré |
| Croissance prix métaux | g_metal | %/an | 1% | -3% à +5% | Évolution annuelle |
| **SYNGAS (si valorisé)** | | | | | |
| Rendement syngas | Rdt_syngas | % masse input | 45% | 35%-55% | % converti en gaz |
| Part syngas autoconsommée | Syngas_auto | % | 100% | 80%-100% | Part utilisée pour le process |
| Prix syngas (si vendu) | P_syngas | €/MWh | 40 | 20-80 | Prix si injection réseau |
| PCI syngas | PCI_syngas | MWh/t | 5.5 | 4-7 | Pouvoir calorifique |

**Revenus Produits Calculés** :
```
Rev_huile = Capacité_annuelle × Rdt_huile × P_huile
Rev_char = Capacité_annuelle × Rdt_char × (P_char_agri × Mix_char_agri + P_char_ind × (1 - Mix_char_agri))
Rev_metal = Capacité_annuelle × Rdt_metal × P_metal
Rev_syngas = Capacité_annuelle × Rdt_syngas × (1 - Syngas_auto) × PCI_syngas × P_syngas
```

---

### 9.2.6 Revenus - Crédits Carbone & Environnementaux

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| **CRÉDITS CARBONE** | | | | | |
| CO₂ évité/tonne traitée | CO2_evite | tCO₂e/t input | 0.35 | 0.2-0.6 | Émissions évitées vs incinération |
| Prix carbone (ETS/volontaire) | P_CO2 | €/tCO₂e | 80 | 20-150 | Prix du crédit carbone |
| Éligibilité crédits | Elig_CO2 | % | 50% | 0%-100% | Part éligible aux crédits |
| Croissance prix CO₂ | g_CO2 | %/an | 5% | -10% à +15% | Évolution prix carbone |
| **BIOCHAR SÉQUESTRATION** | | | | | |
| Carbone séquestré/t biochar | C_seq | tCO₂e/t char | 2.5 | 2.0-3.5 | Équivalent CO₂ séquestré |
| Éligibilité séquestration | Elig_seq | % | 30% | 0%-100% | Part éligible (certification) |
| **ÉCONOMIE CIRCULAIRE** | | | | | |
| Bonus REP (si applicable) | Bonus_REP | €/tonne | 0 | 0-50 | Prime recyclage avancé |

**Revenus Carbone Calculés** :
```
Rev_CO2_evite = Capacité_annuelle × CO2_evite × Elig_CO2 × P_CO2
Rev_seq = Capacité_annuelle × Rdt_char × C_seq × Elig_seq × P_CO2
Rev_carbone_total = Rev_CO2_evite + Rev_seq
```

---

### 9.2.7 Coûts Opérationnels (OPEX)

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| **PERSONNEL** | | | | | |
| Effectif par machine | ETP_machine | ETP | 12 | 8-20 | Employés par unité |
| Coût chargé moyen | Cout_ETP | €/an | 55,000 | 25K-100K | Salaire + charges |
| Inflation salariale | g_salaire | %/an | 2.5% | 1%-5% | Hausse annuelle |
| **MAINTENANCE** | | | | | |
| Maintenance (% CAPEX équip) | Maint_pct | % | 3% | 2%-5% | Coût annuel maintenance |
| Pièces détachées | Pieces | €/an | 200,000 | 50K-500K | Consommables |
| Support technique UR | Support_UR | €/an | 150,000 | 50K-300K | Contrat de support |
| **UTILITIES** | | | | | |
| Électricité achetée | Elec_achat | MWh/an | 500 | 0-2000 | Complément si nécessaire |
| Prix électricité | P_elec | €/MWh | 150 | 50-300 | Prix du kWh |
| Eau | Eau | m³/an | 5,000 | 1K-20K | Consommation eau |
| Prix eau | P_eau | €/m³ | 3 | 1-10 | Prix du m³ |
| **AUTRES OPEX** | | | | | |
| Assurances | Assurance | €/an | 300,000 | 100K-800K | Tous risques |
| Frais généraux | FG | €/an | 200,000 | 50K-500K | Admin, bureau, IT |
| Conformité environnementale | Conformite | €/an | 100,000 | 30K-300K | Analyses, reporting |
| Transport produits | Transport | €/tonne output | 10 | 5-30 | Livraison produits |
| Inflation OPEX | g_OPEX | %/an | 2% | 1%-4% | Hausse annuelle OPEX |

**OPEX Total Calculé** :
```
OPEX_personnel = N_machines × ETP_machine × Cout_ETP
OPEX_maintenance = N_machines × CAPEX_equip × Maint_pct + Pieces + Support_UR
OPEX_utilities = Elec_achat × P_elec + Eau × P_eau
OPEX_autres = Assurance + FG + Conformite + (Capacité_annuelle × (Rdt_huile + Rdt_char + Rdt_metal) × Transport)
OPEX_total = OPEX_personnel + OPEX_maintenance + OPEX_utilities + OPEX_autres
```

---

### 9.2.8 Fiscalité & Amortissement

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| **IMPÔTS** | | | | | |
| Taux d'imposition (IS) | Taux_IS | % | 25% | 15%-35% | Impôt sur les sociétés |
| Crédit d'impôt R&D | CI_RD | €/an | 0 | 0-500K | Crédit impôt recherche |
| **AMORTISSEMENT** | | | | | |
| Durée amort. équipement | Amort_equip | années | 10 | 7-15 | Durée fiscale équipement |
| Durée amort. civil | Amort_civil | années | 20 | 15-30 | Durée fiscale bâtiments |
| Méthode amortissement | Methode | - | Linéaire | Lin/Dégr | Mode d'amortissement |
| **TAXES LOCALES** | | | | | |
| Taxe foncière | TF | €/an | 50,000 | 10K-200K | Impôts fonciers |
| CFE (France) | CFE | €/an | 30,000 | 5K-100K | Cotisation foncière entreprises |
| TGAP (si applicable) | TGAP | €/tonne | 0 | 0-25 | Taxe activités polluantes |

---

### 9.2.9 Paramètres de Projection

| Paramètre | Symbole | Unité | Valeur par Défaut | Plage Typique | Description |
|-----------|---------|-------|-------------------|---------------|-------------|
| Horizon de projection | Horizon | années | 20 | 10-30 | Durée du modèle |
| Année de démarrage | Annee_0 | année | 2026 | - | Première année opérationnelle |
| Montée en puissance | Ramp_up | années | 1 | 0.5-2 | Durée pour atteindre 100% capacité |
| Taux d'utilisation An 1 | Util_an1 | % | 60% | 40%-80% | Utilisation première année |
| Valeur résiduelle | VR | % CAPEX | 10% | 0%-20% | Valeur en fin de projet |
| Taux d'actualisation | r | % | 10% | 6%-15% | Pour calcul VAN |

---

## 9.3 FORMULES DE CALCUL - COMPTE DE RÉSULTAT

### 9.3.1 Revenus Annuels (Année n)

```
REVENUS_TOTAUX(n) = Rev_GF(n) + Rev_huile(n) + Rev_char(n) + Rev_metal(n) + Rev_syngas(n) + Rev_carbone(n)

Où :
Rev_GF(n) = Capacité(n) × GF_moyen × (1 + g_GF)^(n-1)
Rev_huile(n) = Capacité(n) × Rdt_huile × P_huile × (1 + g_huile)^(n-1)
Rev_char(n) = Capacité(n) × Rdt_char × P_char_moyen × (1 + g_char)^(n-1)
Rev_metal(n) = Capacité(n) × Rdt_metal × P_metal × (1 + g_metal)^(n-1)
Rev_carbone(n) = [Capacité(n) × CO2_evite × Elig_CO2 + Capacité(n) × Rdt_char × C_seq × Elig_seq] × P_CO2 × (1 + g_CO2)^(n-1)

Capacité(n) = Capacité_nominale × Facteur_ramp_up(n)
```

### 9.3.2 OPEX Annuels (Année n)

```
OPEX_TOTAUX(n) = [OPEX_personnel + OPEX_maintenance + OPEX_utilities + OPEX_autres] × (1 + g_OPEX)^(n-1)
```

### 9.3.3 EBITDA

```
EBITDA(n) = REVENUS_TOTAUX(n) - OPEX_TOTAUX(n)
Marge_EBITDA(n) = EBITDA(n) / REVENUS_TOTAUX(n)
```

### 9.3.4 Résultat Net

```
Amortissement(n) = (CAPEX_equip / Amort_equip) + (CAPEX_civil / Amort_civil)
EBIT(n) = EBITDA(n) - Amortissement(n)
Intérêts(n) = Dette_restante(n) × i_dette
EBT(n) = EBIT(n) - Intérêts(n)
Impôts(n) = max(0, EBT(n)) × Taux_IS - CI_RD
Résultat_Net(n) = EBT(n) - Impôts(n)
```

---

## 9.4 RATIOS FINANCIERS POUR INVESTISSEURS

### 9.4.1 Ratios de Rentabilité (Les Plus Scrutés)

#### **TRI (Taux de Rentabilité Interne) / IRR**

| Ratio | Formule | Cible Investisseur | Interprétation |
|-------|---------|-------------------|----------------|
| **TRI Projet (unlevered)** | IRR des FCF avant dette | >15% | Rendement intrinsèque du projet |
| **TRI Fonds Propres (levered)** | IRR des flux vers actionnaires | >20% | Rendement pour l'investisseur equity |
| **TRI Banque** | IRR du service de la dette | = Taux prêt | Sécurité du prêteur |

```
TRI_Projet : Σ [FCF(n) / (1 + TRI)^n] = CAPEX_total → Résoudre pour TRI
TRI_Equity : Σ [FCF_equity(n) / (1 + TRI_e)^n] = Fonds_propres → Résoudre pour TRI_e

Où FCF_equity(n) = EBITDA(n) - Impôts(n) - Service_dette(n) - CAPEX_maintenance(n)
```

**Benchmarks TRI par type d'investisseur** :

| Type d'Investisseur | TRI Equity Minimum | TRI Equity Cible |
|---------------------|-------------------|------------------|
| Infrastructure (fonds pension) | 8-10% | 10-12% |
| Private Equity infrastructure | 12-15% | 15-18% |
| Corporate (industriel) | 15-18% | 18-25% |
| Venture/Growth | 20-25% | 25-35% |
| Family Office | 10-15% | 15-20% |

---

#### **VAN (Valeur Actuelle Nette) / NPV**

```
VAN = Σ [FCF(n) / (1 + WACC)^n] - CAPEX_total + VR / (1 + WACC)^Horizon

WACC = (E / (D+E)) × Ke + (D / (D+E)) × i_dette × (1 - Taux_IS)
```

| Résultat VAN | Interprétation |
|--------------|----------------|
| VAN > 0 | Projet créateur de valeur → GO |
| VAN = 0 | Rendement = WACC → Neutre |
| VAN < 0 | Projet destructeur de valeur → NO GO |

---

#### **Payback Period (Délai de Récupération)**

| Ratio | Formule | Cible | Interprétation |
|-------|---------|-------|----------------|
| **Simple Payback** | CAPEX / EBITDA_moyen | <5 ans | Années pour récupérer l'investissement |
| **Discounted Payback** | n tel que Σ FCF_actualisé = CAPEX | <7 ans | Payback en valeur actualisée |

```
Simple_Payback = CAPEX_total / EBITDA_annuel_moyen
Discounted_Payback = n tel que Σ[FCF(i)/(1+r)^i, i=1..n] ≥ CAPEX_total
```

---

#### **Multiple de l'Investissement (MOIC)**

```
MOIC = Σ FCF_equity_totaux / Fonds_propres_investis

Cible : MOIC > 2.0× (doubler la mise sur la durée du projet)
```

---

### 9.4.2 Ratios de Couverture de Dette (Critiques pour Banques)

#### **DSCR (Debt Service Coverage Ratio)**

**LE RATIO LE PLUS IMPORTANT POUR LES PRÊTEURS**

```
DSCR(n) = CFADS(n) / Service_dette(n)

CFADS = Cash Flow Available for Debt Service
       = EBITDA - Impôts - Variation BFR - CAPEX maintenance

Service_dette = Principal(n) + Intérêts(n)
```

| DSCR | Interprétation | Décision Banque |
|------|----------------|-----------------|
| < 1.0 | Impossible de rembourser | ❌ Refus |
| 1.0-1.2 | Très risqué | ⚠️ Conditions strictes |
| 1.2-1.5 | Acceptable | ✅ Financement possible |
| 1.5-2.0 | Confortable | ✅ Conditions favorables |
| > 2.0 | Excellent | ✅ Best terms |

**Exigences typiques** :
- **Banques commerciales** : DSCR minimum 1.3×
- **Banques de développement (EIB, Bpifrance)** : DSCR minimum 1.2×
- **Project Finance** : DSCR minimum 1.4× avec covenant

---

#### **LLCR (Loan Life Coverage Ratio)**

```
LLCR = [Σ CFADS(n) / (1+r)^n + Reserve] / Dette_restante

n = années restantes jusqu'à maturité du prêt
```

| LLCR | Interprétation |
|------|----------------|
| < 1.0 | Dette non remboursable |
| 1.0-1.2 | Marginal |
| > 1.3 | Acceptable |
| > 1.5 | Confortable |

---

#### **ICR (Interest Coverage Ratio)**

```
ICR = EBIT / Intérêts

Cible : ICR > 3.0×
```

---

### 9.4.3 Ratios de Marge et Efficacité

#### **Marges Opérationnelles**

| Ratio | Formule | Benchmark Secteur | Urban Rig Typique |
|-------|---------|-------------------|-------------------|
| **Marge Brute** | (Rev - Coûts variables) / Rev | 40-60% | 70-85% |
| **Marge EBITDA** | EBITDA / Revenus | 20-35% | 60-80% |
| **Marge EBIT** | EBIT / Revenus | 15-25% | 50-70% |
| **Marge Nette** | Résultat Net / Revenus | 10-15% | 35-55% |

---

#### **Ratios d'Efficacité des Actifs**

| Ratio | Formule | Interprétation |
|-------|---------|----------------|
| **Asset Turnover** | Revenus / Actifs_totaux | Efficacité utilisation actifs |
| **CAPEX Intensity** | CAPEX / Revenus | Intensité capitalistique |
| **Rev / tonne traitée** | Revenus / Capacité_annuelle | Performance unitaire |
| **EBITDA / tonne** | EBITDA / Capacité_annuelle | Profitabilité unitaire |

---

### 9.4.4 Ratios de Retour sur Investissement

#### **ROE (Return on Equity)**

```
ROE = Résultat_Net / Fonds_Propres

Cible : ROE > Ke (coût des fonds propres)
```

#### **ROI / ROIC (Return on Invested Capital)**

```
ROIC = NOPAT / Capital_Investi
     = EBIT × (1 - Taux_IS) / (Fonds_Propres + Dette)

Cible : ROIC > WACC
```

#### **Cash-on-Cash Return**

```
Cash_on_Cash = Distribution_annuelle / Fonds_propres_investis

Important pour investisseurs cherchant du rendement courant (yield)
```

---

### 9.4.5 Ratios de Liquidité et Solvabilité

| Ratio | Formule | Cible | Usage |
|-------|---------|-------|-------|
| **Current Ratio** | Actifs CT / Passifs CT | >1.5 | Liquidité court terme |
| **Quick Ratio** | (Actifs CT - Stocks) / Passifs CT | >1.0 | Liquidité immédiate |
| **Gearing** | Dette / Fonds Propres | <3.0 | Levier financier |
| **Debt/EBITDA** | Dette_nette / EBITDA | <4.0 | Capacité de remboursement |
| **Equity Ratio** | Fonds Propres / Total Bilan | >25% | Solidité financière |

---

## 9.5 TABLEAU DE BORD - SYNTHÈSE DES KPIs

### 9.5.1 KPIs Opérationnels

| KPI | Formule | Unité | Fréquence |
|-----|---------|-------|-----------|
| Tonnage traité | Input réel | tonnes | Mensuel |
| Taux d'utilisation | Tonnage / Capacité nominale | % | Mensuel |
| Rendement huile | Huile produite / Input | % | Journalier |
| Rendement biochar | Char produit / Input | % | Journalier |
| Disponibilité technique | Heures opération / Heures totales | % | Mensuel |
| Coût / tonne traitée | OPEX / Tonnage | €/t | Mensuel |

### 9.5.2 KPIs Financiers (Tableau de Synthèse)

```
╔══════════════════════════════════════════════════════════════════╗
║                    URBAN RIG - FINANCIAL DASHBOARD                ║
╠══════════════════════════════════════════════════════════════════╣
║ CONFIGURATION                                                     ║
║ ├─ Machines: [N_machines] × [Type]                               ║
║ ├─ Capacité: [Capacité_annuelle] tonnes/an                       ║
║ └─ CAPEX Total: €[CAPEX_total]M                                  ║
╠══════════════════════════════════════════════════════════════════╣
║ REVENUS ANNUELS (Année de Croisière)                             ║
║ ├─ Gate Fees:        €[Rev_GF]M        ([%] du total)            ║
║ ├─ Huile:            €[Rev_huile]M     ([%] du total)            ║
║ ├─ Biochar:          €[Rev_char]M      ([%] du total)            ║
║ ├─ Métaux:           €[Rev_metal]M     ([%] du total)            ║
║ ├─ Carbone:          €[Rev_CO2]M       ([%] du total)            ║
║ └─ TOTAL:            €[Rev_total]M                               ║
╠══════════════════════════════════════════════════════════════════╣
║ PROFITABILITÉ                                                     ║
║ ├─ OPEX Total:       €[OPEX]M                                    ║
║ ├─ EBITDA:           €[EBITDA]M        (Marge: [%])              ║
║ ├─ EBIT:             €[EBIT]M          (Marge: [%])              ║
║ └─ Résultat Net:     €[RN]M            (Marge: [%])              ║
╠══════════════════════════════════════════════════════════════════╣
║ RATIOS INVESTISSEURS                          Valeur    Cible    ║
║ ├─ TRI Projet (IRR unlevered):               [xx.x%]    >15%     ║
║ ├─ TRI Fonds Propres (IRR levered):          [xx.x%]    >20%     ║
║ ├─ VAN (à WACC [x%]):                        €[xx]M     >0       ║
║ ├─ Payback Simple:                           [x.x] ans  <5 ans   ║
║ ├─ Payback Actualisé:                        [x.x] ans  <7 ans   ║
║ ├─ MOIC:                                     [x.x]×     >2.0×    ║
║ ├─ DSCR Minimum:                             [x.xx]     >1.3     ║
║ ├─ DSCR Moyen:                               [x.xx]     >1.5     ║
║ ├─ LLCR:                                     [x.xx]     >1.3     ║
║ ├─ ROE:                                      [xx.x%]    >15%     ║
║ └─ ROIC:                                     [xx.x%]    >WACC    ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 9.6 ANALYSE DE SENSIBILITÉ

### 9.6.1 Variables Critiques (Impact Fort)

| Variable | Variation | Impact sur TRI Projet | Impact sur VAN |
|----------|-----------|----------------------|----------------|
| Gate Fee | ±20% | ±3-5 pts | ±15-25% |
| Prix Huile | ±20% | ±4-6 pts | ±20-30% |
| Rendement Huile | ±5 pts | ±3-5 pts | ±15-25% |
| CAPEX | ±20% | ±2-4 pts | ±10-20% |
| Taux d'utilisation | ±10% | ±2-3 pts | ±10-15% |
| Prix CO₂ | ±50% | ±1-2 pts | ±5-10% |

### 9.6.2 Matrice de Scénarios

| Scénario | Gate Fee | Prix Huile | Prix CO₂ | Util% | TRI Projet | VAN |
|----------|----------|------------|----------|-------|------------|-----|
| **Pessimiste** | €70 | €350 | €50 | 75% | [calc] | [calc] |
| **Base** | €100 | €500 | €80 | 85% | [calc] | [calc] |
| **Optimiste** | €130 | €650 | €120 | 92% | [calc] | [calc] |

### 9.6.3 Break-Even Analysis

```
Tonnage Break-Even = Coûts_Fixes / (Revenus_unitaire - Coûts_Variables_unitaire)

Prix Huile Break-Even = tel que VAN = 0
Gate Fee Break-Even = tel que DSCR = 1.0
```

---

## 9.7 EXEMPLE NUMÉRIQUE - CAS CDG FRANCE

### Paramètres d'Entrée (Cas Base)

| Catégorie | Paramètre | Valeur |
|-----------|-----------|--------|
| **Configuration** | Machines | 1 × UR-200 |
| | Capacité | 70,000 t/an |
| **CAPEX** | Total | €18M |
| **Financement** | D/E | 70/30 |
| | Taux dette | 5% |
| | Durée | 10 ans |
| **Revenus** | Gate fee | €100/t |
| | Prix huile | €500/t |
| | Prix biochar | €150/t |
| | Prix CO₂ | €80/tCO₂ |
| **Rendements** | Huile | 30% |
| | Biochar | 18% |
| | Métaux | 7% |
| **OPEX** | Total | €2.3M/an |

### Résultats Calculés

| Métrique | Valeur |
|----------|--------|
| **Revenus Annuels** | €20.8M |
| - Gate fees | €7.0M (34%) |
| - Huile | €10.5M (50%) |
| - Biochar | €1.9M (9%) |
| - Métaux | €1.4M (7%) |
| **EBITDA** | €18.5M |
| **Marge EBITDA** | 89% |
| **Résultat Net** | €11.2M |
| **TRI Projet** | 52% |
| **TRI Equity** | 78% |
| **VAN (10%)** | €85M |
| **Payback Simple** | 1.0 an |
| **DSCR Moyen** | 8.5× |
| **MOIC (20 ans)** | 15× |

---

## 9.8 NOTES D'UTILISATION

### Pour les Investisseurs

1. **Focus sur le TRI Equity** : C'est votre rendement réel compte tenu du levier
2. **Vérifier le DSCR** : Assure que la dette est servie même en scénario dégradé
3. **Analyser la sensibilité** : Identifier les variables critiques et leurs impacts
4. **Comparer aux benchmarks** : Urban Rig surperforme les investissements infrastructure classiques

### Pour les Banques

1. **DSCR minimum 1.3×** : Exiger des covenants financiers
2. **Reserve account** : 6 mois de service de dette
3. **Collatéral** : Équipement + contrats d'offtake
4. **Step-in rights** : Capacité de prendre le contrôle si défaut

### Pour les Opérateurs

1. **Optimiser le mix feedstock** : Maximiser gate fees et rendement huile
2. **Sécuriser contrats long terme** : Réduire la volatilité des revenus
3. **Monitorer l'utilisation** : Chaque point d'utilisation compte
4. **Hedger le prix huile** : Si exposition significative au prix du pétrole

---

## 9.9 RÉFÉRENCES

- International Finance Corporation (IFC) - Project Finance Guidelines
- European Investment Bank - Financing Circular Economy Projects
- ADEME - Guide du Financement des Projets de Valorisation des Déchets
- Moody's/S&P - Rating Methodology for Waste-to-Energy Projects
- IRENA - Financial Instruments for Renewable Energy Projects

---

**Navigation** :

**Précédent** : [Chapter 8 - Implementation Timeline](08-implementation-timeline.md)

**Suivant** : [Chapter 10 - Risk Assessment](10-risk-assessment.md)

**Annexes** : [Annex F - Co-Pyrolysis Validation](annex-f-co-pyrolysis-scientific-validation.md)
