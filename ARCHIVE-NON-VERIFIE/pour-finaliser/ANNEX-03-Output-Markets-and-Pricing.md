# Annex 3 — Output Markets and Pricing

**Purpose:** Justifies the unit prices used in the financial model for each of the four marketable output streams produced by the Urban Rig: pyrolysis oil (three fractions), biochar/carbide (five market tiers), recovered metals, and carbon credits. Each price is benchmarked against current European market data with inline sources.

**Date:** March 2026

---

## 3.1 Pyrolysis Oil — Three Fractions

### 3.1.1 The Fractional Separation Advantage

Unlike most pyrolysis technologies that produce a single crude oil stream requiring downstream distillation, the Urban Rig URC-2000 collects oil vapours at three distinct temperature points as waste moves through the 7-zone reactor. Each fraction is condensed independently via separate solenoid valves and condensation paths (Urban Rig Recycling Solutions ENG, p. 15):

| Zone | Temperature | Product | Carbon Range | Share of Liquid Oil | Daily Volume (URC-2000) |
|------|------------|---------|-------------|--------------------|-----------------------|
| 1 | ~150°C | **Light oil** (naphtha range) | C$_5$--C$_8$ | 10% | 7,803 L |
| 2 | ~300°C | **Gas (diesel) oil** | C$_8$--C$_{16}$ | **80%** | 62,424 L |
| 3 | ~450°C | **Heavy oil** (waxes/paraffins) | C$_{16}$+ | 10% | 7,803 L |

*Source: Urban Rig Recycling Solutions ENG, pp. 15--16. Volume data from URC-2000 output table at 90% resin content, 200 T/day volumetric.*

This built-in fractional distillation allows each fraction to be sold at its grade-specific market price rather than accepting the discount associated with crude, undifferentiated pyrolysis oil.

### 3.1.2 Oil Quality — Measured Data

**NKKK Fuel Certification** (Nippon Kaiji Kentei Kyokai — Japan Marine Survey Association, JIS standards):

| Parameter | Result | Comparison |
|-----------|--------|------------|
| Calorific value | **43.27 MJ/kg** | Fossil diesel: 42.6 MJ/kg |
| Flashpoint | $\leq$40°C | Contains light naphtha fractions |
| Sulfur | 0.014% (140 ppm) | Below IMO 2020 (0.5%); above Euro V diesel (10 ppm) |
| Chlorine | 0.0001% (1 ppm) | Well below problematic levels |
| Pour point | $-$20°C | Good cold-flow properties |
| Viscosity (50°C) | 1.11 mm$^2$/s | Light, low-viscosity product |
| Ash | 0.005% | Very clean |

*Source: NKKK certified test report (JIS standards). Note: sample may be light fraction only — verification with UR/OneWorld recommended.*

**GC-MS Analysis** (Osaka Institute of Industrial Science and Technology) confirmed the volatile fraction is dominated by middle-distillate hydrocarbons: dimethylheptane (C$_9$), undecene (C$_{11}$), and trimethylnonane (C$_{12}$) — the C$_8$--C$_{16}$ range directly usable as naphtha-substitute feedstock for steam crackers (Technical Findings Log §12).

### 3.1.3 Market Benchmarks (2024--2025)

**Fossil equivalents:**

| Product | Market | Price (EUR/T) | Source |
|---------|--------|--------------|--------|
| Naphtha (NWE) | ARA spot | ~€485--660 | ChemAnalyst Q4 2025; Intratec Netherlands May 2025 |
| ICE Low Sulphur Gasoil | NWE futures | ~€820 | ICE LS Gasoil futures 2025 |
| Heavy Fuel Oil (380 cst) | Rotterdam bunker | ~€415 | S&P Global Platts Feb 2025 |

**Recycled pyrolysis oil (ICIS Index):**

ICIS launched the first pyrolysis oil pricing index in 2023, covering European spot transactions. Key 2024--2025 data:

| Grade | Price Indicator | Source |
|-------|----------------|--------|
| Tire-derived pyrolysis oil (baseline) | Base reference | ICIS weekly report |
| Plastic-derived PPO, non-upgraded, ex-works NWE | **+€681/T** premium over tire-derived (2024 avg) | ICIS via PlasticsToday |
| Plastic-derived naphtha-substitute (cracker grade) | **+€1,114/T** premium over tire-derived (2024 avg) | ICIS via Tire Technology International |
| Netherlands PPO spot Q1 2025 | ~\$729/T ≈ **€670/T** | IMARC Pyrolysis Oil Price Trends 2025 |

**Recycled content premium driver:** EU regulations are creating sustained demand for recycled-content petrochemical feedstock. The PPWR (Packaging and Packaging Waste Regulation) mandates recycled content targets for plastic packaging — 30% by 2030, 65% by 2040 (EU PPWR, adopted 2024). The EU ETS makes fossil feedstock relatively more expensive. ISCC PLUS certification enables mass balance accounting, allowing refineries to attribute recycled content to downstream products. BASF ChemCycling, TotalEnergies, and Esso/ExxonMobil all have active offtake programmes for ISCC-certified pyrolysis oil (BASF press release March 2025; TotalEnergies sustainability reports).

### 3.1.4 Oil Pricing Model — Three Scenarios

**Price per fraction (EUR/T):**

| Fraction | Share | Low | Medium | High | Rationale |
|----------|-------|-----|--------|------|-----------|
| **Light oil** (C$_5$--C$_8$) | 10% | 450 | 600 | 800 | Low: discount for quality uncertainty. Medium: naphtha parity. High: + recycled premium |
| **Gas (diesel) oil** (C$_8$--C$_{16}$) | 80% | 500 | 670 | 950 | Low: crude PPO floor. Medium: ICIS spot NWE 2025. High: naphtha-sub with ISCC premium |
| **Heavy oil** (C$_{16}$+) | 10% | 350 | 450 | 550 | Low: HFO discount. Medium: marine fuel/industrial. High: hydrocracker feed + green premium |

**Weighted average oil price:**

| Scenario | Weighted EUR/T | EUR/L (at 0.85 kg/L) | Basis |
|----------|---------------|----------------------|-------|
| **Low (conservative)** | **€480/T** | **€0.41/L** | No green premium. All sold as undifferentiated crude. Floor price |
| **Medium (base case)** | **€641/T** | **€0.55/L** | Current ICIS spot. Fractions sold at grade-specific prices. **Recommended for business plan** |
| **High (optimistic)** | **€895/T** | **€0.76/L** | Full recycled premium. ISCC-certified. Long-term offtake with cracker operators |

*Calculation: Weighted price = $\sum$ (fraction share × fraction price). Example Medium: 0.10 × 600 + 0.80 × 670 + 0.10 × 450 = €641/T.*

**Note:** The original financial model used a hardcoded oil price of €0.41/L (€482/T) — corresponding to the Low scenario (floor price, zero green premium, undifferentiated crude). The Medium scenario (€641/T) is the appropriate base case given that 80% of UR output is middle distillate and the machine already separates fractions without downstream processing.

### 3.1.5 Target Buyers

| Fraction | Target buyers | Sales channel |
|----------|--------------|--------------|
| Light oil (naphtha) | Naphtha cracker operators (BASF, TotalEnergies, Esso/ExxonMobil) | ISCC PLUS certified offtake contracts |
| Gas oil (diesel) | Diesel/kerosene blenders, refinery co-processors | Spot + term contracts via ICIS-referenced pricing |
| Heavy oil | Marine fuel traders, hydrocracker feedstock buyers | Industrial spot or burn on-site for reactor heating |

### 3.1.6 Recommendations

1. **Obtain indicative offtake pricing** from at least two potential buyers (e.g., TotalEnergies Gonfreville, Esso Fos-sur-Mer) for the diesel fraction specifically. This converts the Medium scenario from hypothesis to confirmed market price.
2. **Plan ISCC PLUS certification from Day 1** — it unlocks the full recycled premium that justifies the Medium and High scenarios.
3. **Design separate storage tanks** for the three fractions to preserve the price differentiation advantage.
4. **Run the financial model at all three scenarios** (Low/Medium/High) to show investors the range of outcomes.

---

## 3.2 Biochar / Carbide

### 3.2.1 Product Characteristics

The Urban Rig produces 480.8 kg of combustible char per 1,000 kg of OMR (57.5% of reactor input after inert removal — see Annex 5 §11.4). In the V2 model, all char is sold as fuel; none is diverted for reactor heating (which is supplied by purchased heating oil). Total char available for sale is approximately **67 T/day (~22,155 T/year)**.

Char characteristics depend on source material:

| Source | Share of combustible char | Estimated CV (MJ/kg) | Carbon content | Data quality |
|--------|--------------------------|---------------------|---------------|-------------|
| Organic/cellulose char | 94% (452.2 / 480.8 kg) | 15 | ~40--50% | HYPOTHESIS — literature (Fazil et al., *Energies*, 2021; Ronsse et al., 2020) |
| Plastic char | 6% (28.6 / 480.8 kg) | 25 | ~60--80% | HYPOTHESIS — consistent with carbon black (~32 MJ/kg). One UR measurement: urethane char at 32.09 MJ/kg (Isumi Tech, JIS M 8814) |
| **Weighted average** | 100% | **15.6** | ~42--52% | |

### 3.2.2 Market Tiers

The surplus char can be sold into several markets depending on quality, certification, and form factor (loose vs compressed pellets/briquettes):

| Tier | Market | Price (EUR/T) | Basis | Annual Revenue (16,088 T) | Total Benefit (incl. €1M diesel saved) |
|------|--------|--------------|-------|--------------------------|---------------------------------------|
| T1 | Waste-to-energy fuel (RDF substitute) | 50 | Sold as-is to cement kilns or WtE plants | €804k | €1.8M |
| **T2** | **Industrial fuel pellets** | **100** | **Compressed into pellets, wholesale fuel market** | **€1.6M** | **€2.6M** |
| T3 | Charcoal briquettes | 200 | Compressed briquettes for heating/BBQ market | €3.2M | €4.2M |
| T4 | Biochar for agriculture | 350 | Soil amendment, requires EBC certification | €5.6M | €6.6M |
| T5 | Biochar + carbon credits | 350 + credit | Physical sale + CORC/EBC carbon removal certificate | €5.6M + €3.2M | €9.8M |

*Sources: Tier 1--3 pricing from European solid fuel market benchmarks. Tier 4 from European Biochar Certificate (EBC) marketplace. Tier 5 carbon credit pricing from Puro.earth CORC Carbon Removal Price Indexes (2025), CDR.fyi Biochar Carbon Removal Market Snapshot (2025), carboncredits.com biochar market analysis (2025).*

**Tier 2 (€100/T) is the recommended base case** for the financial model — conservative, does not require certification, and targets an established market for industrial fuel pellets. The current Excel model already uses €100/T (UR-Financial-Model-General.xlsx, Revenue sheet).

### 3.2.3 Carbon Credit Potential (Tier 5)

MSW-derived char has ~40--50% carbon content. Carbon sequestration potential:

| Parameter | Value |
|-----------|-------|
| Carbon content of char | ~42--52% (weighted estimate) |
| CO$_2$ equivalent per tonne of char | ~1.5 T CO$_2$ (conservative) |
| Annual surplus char | 16,088 T/year |
| Annual CO$_2$ sequestered | ~24,132 T CO$_2$/year |
| CORC price (2025) | ~€133/T CO$_2$ |
| EU ETS price (conservative) | ~€50/T CO$_2$ |
| **Revenue at CORC price** | **~€3.2M/year** |
| Revenue at EU ETS price | ~€1.2M/year |

*Sources: CORC biochar carbon removal index from Puro.earth (2025). EU ETS price from ICE EUA futures (2025).*

This revenue is **additional** to the physical sale of char (Tier 4 or 5 combined). However, biochar carbon credits require EBC or Puro.earth certification, soil application (not combustion), and chain-of-custody documentation. This pathway is best suited for Phase 2 after validating char quality.

### 3.2.4 Pelletisation CAPEX

Compressing char into pellets or briquettes requires a pelletising unit. Indicative cost for an industrial pelletiser capable of 50 T/day throughput: €200k--500k. This is a minor addition to the €50M+ CAPEX and is not separately modelled; it would appear in the "Site infrastructure" line of the CAPEX sheet (Annex 5 §13.6).

---

## 3.3 Recovered Metals

### 3.3.1 Recovery Mechanism

Metals in the waste stream — ferrous (steel) and non-ferrous (aluminium, copper) — are recovered in **non-oxidised form** because the anoxic reactor environment (superheated steam at 600°C, zero oxygen) prevents oxidation. This contrasts with incineration where metals are oxidised and must be recovered from toxic bottom ash at reduced quality and value (Urban Rig Recycling Solutions ENG, p. 13; Eurostat waste incineration guidelines).

### 3.3.2 Metal Content in MSW

Per ADEME MODECOM 2017, metals represent approximately 3% of OMR (30 kg per 1,000 kg). An additional 3 kg of metal fragments is recovered from the fine elements fraction (Annex 5 §2). Total recoverable metals: approximately **33 kg per tonne of OMR**, split roughly 70% ferrous / 30% non-ferrous (ADEME 2017 characterisation).

### 3.3.3 Pricing

| Metal type | Share | Price (EUR/T) | Source | Revenue per 1,000 kg OMR |
|-----------|-------|--------------|--------|------------------------|
| Ferrous (steel scrap) | 70% (~23 kg) | 250--350 | European steel scrap index (LKAB Minerals, S&P Global Platts, 2024--2025) | €5.75--8.05 |
| Non-ferrous (aluminium, copper mix) | 30% (~10 kg) | 1,200--2,500 | LME aluminium ~€2,200/T; LME copper ~€8,500/T; blended non-ferrous ~€1,800/T | €12.00--25.00 |
| **Total metals** | **33 kg** | — | — | **€17.75--33.05** |

*Scaling to 140 T/day × 330 days = 46,200 T/year OMR: approximately **€0.8M--1.5M/year** in metal revenue.*

The financial model uses **€0.7M/year** (UR-Financial-Model-General.xlsx, Revenue sheet) — at the conservative end of the range, reflecting sorting/cleaning losses and market variability.

### 3.3.4 Non-Oxidised Quality Premium

The non-oxidised recovery condition is a meaningful advantage. Metals recovered from incineration ash are typically oxidised, contaminated with slag, and sell at a discount of 30--50% versus clean scrap (Eurostat, CEWEP incineration benchmarks). Urban Rig metals, recovered in their original metallic form, command full scrap market prices without quality discounts.

---

## 3.4 Carbon Credits

### 3.4.1 Carbon Credit Mechanism

Carbon credits are generated by the difference between Urban Rig CO$_2$ emissions and the counterfactual emissions from the waste treatment pathway it displaces (typically incineration). Two distinct credit sources exist:

1. **CO$_2$ avoided** — less fossil carbon emitted than incineration of the same waste
2. **CO$_2$ sequestered** — carbon permanently stored in biochar applied to soil (separate from Tier 5 biochar credits in §3.2.3)

### 3.4.2 CO$_2$ Avoided vs Incineration Baseline

| Emission source | Incineration (counterfactual) | Urban Rig | Difference |
|----------------|------------------------------|-----------|-----------|
| Combustion CO$_2$ (plastic fraction) | ~1.0 T CO$_2$/T waste | ~0 (no combustion) | $-$1.0 T |
| Biogenic CO$_2$ (organic fraction) | ~0.5 T CO$_2$/T waste (considered neutral) | Stored as char (carbon-negative) | $-$0.5 T |
| Process energy CO$_2$ | ~0.15 T CO$_2$/T waste (auxiliary fuel) | ~0.10 T CO$_2$/T waste (purchased heating oil) | $-$0.05 T |
| **Net CO$_2$ reduction** | — | — | **~1.0--1.5 T CO$_2$/T waste** |

*Sources: ADEME incineration emission factors (2022); IPCC waste-sector guidelines; financial model carbon calculations.*

At 46,200 T/year throughput: approximately **46,200--69,300 T CO$_2$/year** avoided.

### 3.4.3 Carbon Credit Pricing

| Market | Price (EUR/T CO$_2$) | Source | Annual revenue estimate |
|--------|---------------------|--------|----------------------|
| EU ETS (compliance market) | ~€50--80 | ICE EUA futures (2024--2025) | €2.3M--5.5M |
| Voluntary carbon market (VCM) | ~€15--40 | Ecosystem Marketplace, MSCI Carbon Markets (2024) | €0.7M--2.8M |
| **Financial model assumption** | **€50** | Conservative (EU ETS floor) | **€2.5M** |

*Source: UR-Financial-Model-General.xlsx, Revenue sheet — uses €50/T CO$_2$ and approximately 50,000 T CO$_2$/year net reduction.*

**Eligibility note:** Carbon credits require formal methodology registration (e.g., Gold Standard, Verra VCS, or EU ETS inclusion). The UR process would need to demonstrate additionality and secure third-party verification. This is a Phase 2 revenue stream — conservatively included at €50/T but requiring regulatory and certification work.

---

## 3.5 Revenue Summary — Financial Model Reference

At the base case (URC-2000, 200 T/day, 30% plastic content, Year 3 steady state, Medium oil scenario):

| Revenue Stream | Annual Estimate | % of Total | Pricing Basis |
|---------------|----------------|-----------|--------------|
| Gate fees (waste intake) | €5.3M | 31% | €80--180/T tipping fee range (ADEME 2022); model uses blended €114/T |
| Fuel oil sales (3 fractions) | €7.1M | 41% | Medium scenario €641/T weighted (ICIS 2025; see §3.1.4) |
| Char/biochar sales (surplus) | €1.7M | 10% | Tier 2 at €100/T (fuel pellets; see §3.2.2) |
| Recovered metals | €0.7M | 4% | Conservative blend of ferrous + non-ferrous (see §3.3.3) |
| Carbon credits | €2.5M | 14% | €50/T CO$_2$ × ~50,000 T/year (see §3.4.3) |
| **TOTAL** | **€17.3M** | **100%** | |

*Source: UR-Financial-Model-General.xlsx, Revenue sheet (Year 3 steady state). 815 validated formulas, 0 circular references, 0 errors.*

### 3.5.1 Revenue Sensitivity to Oil Price

The oil price is the single most impactful assumption after machine cost:

| Oil Scenario | Oil Revenue | Total Revenue | EBITDA | Change vs Medium |
|-------------|-----------|--------------|--------|-----------------|
| Low (€480/T) | ~€5.3M | ~€15.6M | ~€10.2M | $-$€1.7M |
| **Medium (€641/T)** | **~€7.1M** | **~€17.3M** | **~€11.9M** | **Base case** |
| High (€895/T) | ~€9.9M | ~€20.1M | ~€14.7M | +€2.8M |

Moving from Low to Medium adds ~€1.7M/year; from Medium to High adds ~€2.8M/year.

---

## 3.6 Data Quality Summary

| Output | Price Used | Classification | Confidence |
|--------|-----------|---------------|------------|
| Oil — fraction split (10/80/10) | From UR spec | FACT | MEDIUM — at 90% resin; actual split may vary with MSW feedstock |
| Oil — Medium price €641/T | ICIS benchmark | FACT (market data) | MEDIUM-HIGH — 2024--2025 spot; no UR offtake contracts yet |
| Oil — NKKK quality (43.27 MJ/kg) | Certified lab | FACT | HIGH — note: may be light fraction only |
| Biochar — T2 at €100/T | Market benchmark | REASONABLE | MEDIUM — established fuel pellet market |
| Biochar — char CV 15.6 MJ/kg | Literature | HYPOTHESIS | MEDIUM — not measured on UR MSW char |
| Metals — €0.7M/year | Market indices | REASONABLE | MEDIUM — depends on sorting efficiency |
| Carbon credits — €50/T CO$_2$ | EU ETS floor | REASONABLE | MEDIUM — requires methodology + verification |
| Gate fees — €114/T blended | ADEME range | REASONABLE | HIGH — well within French tipping fee corridor |

---

## 3.7 References

**Urban Rig Technical Sources**

1. **Urban Rig Recycling Solutions ENG** — OneWorld Corporation product brochure (English edition). Cited for: fractional oil separation design (pp. 15–16), metal recovery in anoxic conditions (p. 13).
2. **NKKK (Nippon Kaiji Kentei Kyokai)** — Recycled fuel test report, JIS standards. Cited for: oil quality certification — 43.27 MJ/kg CV, 0.014% sulphur, 1 ppm chlorine (§3.1.2).
3. **Osaka Institute of Industrial Science and Technology** — GC-MS analysis of volatile oil fraction. Cited for: compound identification (dimethylheptane, undecene, trimethylnonane) in Technical Findings Log §12 (§3.1.2).

**Market Data and Pricing Sources**

4. **ICIS** — Weekly pyrolysis oil pricing index (launched 2023). Cited for: European spot PPO pricing, tire-derived baseline, plastic-derived premiums (§3.1.3, §3.1.4).
5. **ChemAnalyst** — Naphtha NWE pricing Q4 2025. Cited for: naphtha benchmark €485–660/T (§3.1.3).
6. **Intratec** — Netherlands naphtha pricing May 2025. Cited for: naphtha benchmark (§3.1.3).
7. **ICE (Intercontinental Exchange)** — Low Sulphur Gasoil NWE futures 2025; EUA futures 2024–2025. Cited for: gasoil ~€820/T (§3.1.3), EU ETS carbon price €50–80/T (§3.4.3).
8. **S&P Global Platts** — Rotterdam bunker HFO 380 cst (Feb 2025); European steel scrap index. Cited for: HFO ~€415/T (§3.1.3), ferrous scrap €250–350/T (§3.3.3).
9. **IMARC** — Pyrolysis Oil Price Trends 2025. Cited for: Netherlands PPO spot ~$729/T (§3.1.3).
10. **LME (London Metal Exchange)** — Aluminium and copper spot prices 2024–2025. Cited for: non-ferrous metal pricing (§3.3.3).

**Regulatory and Industry Sources**

11. **EU PPWR (Packaging and Packaging Waste Regulation)** — Adopted 2024. Cited for: recycled content mandates — 30% by 2030, 65% by 2040 (§3.1.3).
12. **BASF** — ChemCycling press release (March 2025). Cited for: recycled feedstock offtake programmes (§3.1.3).
13. **TotalEnergies** — Sustainability reports. Cited for: ISCC-certified pyrolysis oil offtake (§3.1.3).
14. **ISCC PLUS** — International Sustainability and Carbon Certification. Cited for: mass balance certification enabling recycled content claims (§3.1.3).

**Biochar and Carbon Credit Sources**

15. **European Biochar Certificate (EBC)** — Marketplace pricing. Cited for: Tier 4 biochar agricultural pricing (§3.2.2).
16. **Puro.earth** — CORC Carbon Removal Price Indexes (2025). Cited for: biochar carbon credit pricing ~€133/T CO$_2$ (§3.2.3).
17. **CDR.fyi** — Biochar Carbon Removal Market Snapshot (2025). Cited for: carbon removal market benchmarks (§3.2.2).
18. **carboncredits.com** — Biochar market analysis (2025). Cited for: carbon credit market context (§3.2.2).
19. **Ecosystem Marketplace** — Voluntary carbon market data (2024). Cited for: VCM pricing €15–40/T (§3.4.3).
20. **MSCI Carbon Markets** — Carbon market analysis (2024). Cited for: voluntary market benchmarks (§3.4.3).

**Institutional Sources**

21. **ADEME** — Incineration emission factors (2022); tipping fee ranges. Cited for: CO$_2$ avoided calculations (§3.4.2), gate fee corridor (§3.5).
22. **IPCC** — Waste-sector greenhouse gas guidelines. Cited for: emission factor methodology (§3.4.2).
23. **Eurostat** — Waste incineration guidelines; CEWEP benchmarks. Cited for: metal quality discount in incineration (§3.3.4).

**Internal Model References**

24. **UR-Financial-Model-General.xlsx** — Working financial model (CAPEX, Revenue, P&L sheets). Cited for: revenue assumptions, oil price baseline, steady-state projections (§3.5).

---

**End of Annex 3**
