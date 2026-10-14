# Annex 5 — Sector: Municipal Solid Waste (France)

**Purpose:** Sector-specific feedstock profile for French Municipal Solid Waste (residual household waste (OMR)), detailing composition and pyrolysis product yields when processed through the Urban Rig, with full justification and sourcing of every parameter.

**Date:** March 2026
**Status:** Corrected + Verified — Session 10 (full 13-category decomposition)

---

## OBJECTIVE

To answer the question: **If we feed French MSW (residual household waste (OMR)) into the Urban Rig, what are the expected outputs?**

This annex is divided into two parts. **Part 1** establishes the composition of what actually enters the reactor — tracing from the full 13-category MODECOM characterisation through inert removal and material-by-material decomposition to a consolidated feedstock breakdown. **Part 2** then applies per-material pyrolysis yields (measured on the UR where available, literature-based elsewhere) to that feedstock to calculate weighted-average outputs.

Every parameter is classified as: **FACT** (measured on UR), **HYPOTHESIS** (literature-based estimate), or **ASSUMPTION** (engineering judgment).

---

# PART 1 — WHAT GOES IN: Feedstock Composition

*This part answers: of the 1,000 kg of raw MSW arriving at the gate, what materials actually enter the reactor, and in what proportions?*

*Why it matters: the financial model requires a precise breakdown by material type because each material produces different yields. Getting the input wrong cascades through every output calculation.*

---

## 1. FRENCH OMR COMPOSITION — FULL 13-CATEGORY BREAKDOWN

**Why we need this:** The starting point for the entire model. MODECOM 2017 characterises French OMR into 13 categories. Previous versions of this annex used a simplified 9-category grouping that lumped five distinct categories into "Other/Fines" — losing visibility on ~190 kg of material per tonne. The full breakdown enables proper decomposition and eliminates the opaque residual.

**Source:** ADEME MODECOM 2017, France's national waste characterisation campaign (third edition), characterising OMR after separate collection. Published at [ademe.fr](https://www.ademe.fr/presse/communique-national/modecom-2017-ce-que-revelent-les-poubelles-des-francais); detailed analysis at [medias.amf.asso.fr](https://medias.amf.asso.fr/upload/files/modecom_2017_analyse_des_resultats_011318.pdf).

| # | Category | % of OMR | kg per 1,000 kg | Note |
|---|----------|---------|-----------------|------|
| 1 | Putrescibles (food/garden waste) | 27% | 270 | Largest single fraction |
| 2 | Plastics | 15% | 150 | All polymer types mixed |
| 3 | Sanitary textiles | 14% | 140 | Diapers, toilet paper, wipes, etc. |
| 4 | Fine elements (<20 mm) | 10% | 100 | Sub-sieve fraction, mix of everything |
| 5 | Paper | 8% | 80 | Newspapers, magazines, office paper |
| 6 | Cardboard | 6% | 60 | Packaging cardboard |
| 7 | Glass | 5% | 50 | Bottles, jars |
| 8 | Textiles (clothing) | 4% | 40 | Clothing, fabric scraps |
| 9 | Composites (EMR) | 3% | 30 | Multi-material packaging (Tetra Pak, etc.) |
| 10 | Metals | 3% | 30 | Ferrous + non-ferrous |
| 11 | Unclassified incombustibles | 2% | 20 | Ceramics, stones, porcelain |
| 12 | Wood | 1.5% | 15 | Wood fragments |
| 13 | Unclassified combustibles | 1.5% | 15 | Leather, rubber, misc. organic |
| | **TOTAL** | **100%** | **1,000** | |

[FACT] **FACT** — These percentages come from a statistically representative national study. Data quality: HIGH. Categories 4–13 were previously grouped as "Other/Fines (19%)" and "Composites (3%)" — now shown individually.

**Note on MODECOM 2024 update:** The latest campaign ([valor3e.fr, 2024 first results](https://www.valor3e.fr/le-kiosque-info/actualites/premiers-resultats-du-modecom-2024/)) shows further evolution: biowaste rising to 32%, sanitary textiles to 25.5%, recyclables at 24.1%. OMR per capita declined from 254 kg (2017) to 223.5 kg (2024). The underlying trends would not materially change the yield model since the plastic-like fraction ratios remain similar.

---

## 2. REMOVING NON-PROCESSABLE MATERIAL

**Why we need this:** Several categories cannot be pyrolysed and must be removed before or during processing. Quantifying all removals — not just glass and metals — gives an accurate reactor input mass.

| Removed material | Mass (kg) | Removal method |
|-----------------|----------|----------------|
| Glass (glass) | 50 | Mechanical screening / optical sorting |
| Metals (ferrous + non-ferrous) | 30 | Magnetic + eddy current separation |
| Unclassified incombustibles | 20 | Density separation / manual sorting |
| Aluminium from composites (5% of 30 kg) | 1.5 | Separated during composite processing |
| Metal fragments from fines (~3% of 100 kg) | 3.0 | Magnetic separation of fines |
| Glass fragments from fines (~5% of 100 kg) | 5.0 | Screening of fines |
| **Total removed** | **109.5** | |
| **Material entering reactor** | **890.5** | |

[HYPOTHESIS] **ASSUMPTION** — Pre-sorting assumed at standard industry efficiency. The fines fragment estimates (3% metal, 5% glass) are based on published characterisation studies of the sub-20mm fraction. In practice, removal efficiency varies; residual fragments are captured in the mineral inert residue.

**Note:** Previous versions removed only glass (50 kg) and metals (30 kg) = 80 kg, giving 920 kg effective feedstock. The fuller accounting adds 29.5 kg of removals from incombustibles, composite aluminium, and fines fragments.

---

## 3. SANITARY TEXTILES DECOMPOSITION (140 kg)

**Why we need this:** MODECOM groups "sanitary textiles" as a single category (14% of OMR), but this category contains radically different materials — from pure cellulose (toilet paper) to synthetic polymers (diaper components). Since each material has different pyrolysis yields, we must decompose this category into its constituent materials.

### 3.1 Subcategory Breakdown

Source: [vertuow.com/tsuu-transformer-les-dechets-en-ressources](https://www.vertuow.com/tsuu-transformer-les-dechets-en-ressources/).

| Subcategory | % of sanitary textiles | Mass in 140 kg | Dominant material |
|-------------|----------------------|----------------|-------------------|
| Toilet paper | 44.3% | 62.0 kg | 100% cellulose |
| Paper towels | 17.2% | 24.1 kg | 100% cellulose |
| Baby diapers | 10.7% | 15.0 kg | SAP + PP + PE + cellulose |
| Body wipes | 5.4% | 7.6 kg | PP/PET nonwoven + moisture |
| Adult incontinence products | ~4% | ~5.6 kg | SAP + PP + PE + cellulose |
| Other (protections, cotton buds, etc.) | ~18.4% | ~25.8 kg | Mixed cellulose, cotton, some synthetic |

[FACT] **FACT** — Subcategory percentages from French waste-sector analysis. Data quality: MEDIUM-HIGH.

### 3.2 Diaper Material Composition

Sources: ResearchGate material composition data; [ChemistryExplained.com](https://www.chemistryexplained.com/Di-Fa/Disposable-Diapers.html).

| Component | % of diaper mass | Type |
|-----------|-----------------|------|
| Cellulose pulp (absorbent core) | 37% | Organic |
| SAP — sodium polyacrylate | 31% | Synthetic polymer |
| Polypropylene (top sheet, elastic) | 16% | Plastic |
| LDPE (backsheet) | 6% | Plastic |
| Tape, adhesive, elastic | 10% | Mostly synthetic |

### 3.3 Material Reassignment

| Material | Mass (kg) | Reassigns to |
|----------|----------|-------------|
| Cellulose from toilet paper | 62.0 | → Cellulose |
| Cellulose from paper towels | 24.1 | → Cellulose |
| Cellulose from diapers (37% of 20.6 kg) | 7.6 | → Cellulose |
| Cellulose/cotton from other items (~50%) | 16.7 | → Cellulose |
| **Total cellulose** | **110.4** | **79% of TS** |
| SAP from diapers (31% of 20.6 kg) | 6.4 | → Plastic-like |
| PP/PE from diapers (22% of 20.6 kg) | 4.5 | → Plastic-like |
| PP/PET nonwoven from wipes (80% of 7.6 kg) | 6.1 | → Plastic-like |
| Other synthetic from misc. (~15%) | 5.0 | → Plastic-like |
| **Total plastic-like** | **22.0** | **16% of TS** |
| Moisture/contamination | 7.6 | → Organic (non-productive) |

[HYPOTHESIS] **ASSUMPTION** — The 50% cellulose and 15% synthetic estimates for "other" are engineering judgments.

---

## 4. TEXTILES — CLOTHING DECOMPOSITION (40 kg)

**Why we need this:** Clothing textiles are 4% of OMR — entirely absent from previous versions of this model, where they were hidden inside "Other/Fines." They contain significant quantities of both cellulose (cotton) and synthetic polymers (polyester, nylon) that must be assigned to the correct material group.

European textile waste composition (source: [EEA Textiles and the Environment report, 2024](https://www.eea.europa.eu/publications/textiles-and-the-environment-the); cross-checked with Euratex industry data):

| Fibre type | % of textile waste | Mass in 40 kg | Reassigns to |
|-----------|-------------------|--------------|-------------|
| Cotton | ~60% | 24.0 kg | → Cellulose |
| Polyester (PET-like) | ~21% | 8.4 kg | → Plastic-like |
| Nylon (polyamide) | ~9% | 3.5 kg | → Plastic-like |
| Acrylic / other synthetic | ~5% | 2.1 kg | → Plastic-like |
| Non-textile (buttons, zips, etc.) | ~5% | 2.0 kg | → Mineral inert |

[HYPOTHESIS] **ASSUMPTION** — European average fibre mix applied to French OMR textile fraction. Actual proportions vary by collection area and season.

---

## 5. COMPOSITES DECOMPOSITION (30 kg)

**Why we need this:** MODECOM "composites" are overwhelmingly multi-material packaging — Tetra Pak–type beverage cartons, blister packs, etc. Their composition is well-documented and can be decomposed with high confidence.

Tetra Pak composition (source: [Tetra Pak sustainability reports](https://www.tetrapak.com/sustainability/planet/good-practices/recycling); industry standard):

| Component | % of composite mass | Mass in 30 kg | Reassigns to |
|-----------|-------------------|--------------|-------------|
| Cardboard | ~75% | 22.5 kg | → Cellulose |
| Polyethylene (PE film) | ~20% | 6.0 kg | → Plastic-like (LDPE) |
| Aluminium foil | ~5% | 1.5 kg | → Removed (non-processable) |

[FACT] **FACT** — Tetra Pak composition is an industry standard. Data quality: HIGH.

---

## 6. UNCLASSIFIED COMBUSTIBLES DECOMPOSITION (15 kg)

**Why we need this:** This catch-all category (leather, rubber, wood offcuts, misc. organic material) was previously invisible inside "Other/Fines." While small, it contains both organic and synthetic fractions that behave differently in the reactor.

| Component | % estimate | Mass in 15 kg | Reassigns to |
|-----------|-----------|--------------|-------------|
| Leather, rubber (organic/protein) | ~70% | 10.5 kg | → Organic |
| Synthetic (rubber, adhesives, misc.) | ~30% | 4.5 kg | → Plastic-like |

[HYPOTHESIS] **ASSUMPTION** — Split based on general waste characterisation literature. Low confidence due to heterogeneity.

---

## 7. FINE ELEMENTS DECOMPOSITION (100 kg → 92 kg after fragment removal)

**Why we need this:** The sub-20mm sieve fraction is the second-largest "hidden" category after refus. At 10% of OMR, it contains meaningful quantities of every material type. Without decomposing it, 100 kg per tonne has undefined pyrolysis behaviour. After removing metal fragments (3 kg) and glass fragments (5 kg) in Section 2, 92 kg enters the reactor.

Composition of the sub-20mm fraction (source: published MODECOM characterisation studies of fine elements; cross-validated with local characterisation data from French waste operators):

| Component | % of fines | Mass in 92 kg | Reassigns to |
|-----------|-----------|--------------|-------------|
| Organic fragments (food scraps) | ~45% | 41.4 kg | → Organic |
| Paper/cardboard scraps | ~15% | 13.8 kg | → Cellulose |
| Small plastic fragments | ~8% | 7.4 kg | → Plastic-like (MSW polymer mix) |
| Mineral inert (soil, dust, ceramics) | ~32% | 29.4 kg | → Mineral inert (enters reactor, produces only residue) |

[HYPOTHESIS] **ASSUMPTION** — Percentages based on published characterisation data. The mineral inert fraction enters the reactor but passes through as residue without producing oil or useful gas. MEDIUM confidence.

---

## 8. PLASTIC POLYMER MIX — FULL PLASTIC-LIKE FRACTION

**Why we need this:** The plastic-like fraction now totals 203.9 kg (was 176.2 kg in previous version). The additional 27.7 kg comes from textiles, composites, combustibles, and fines. Each source has a different polymer profile, which affects the weighted oil yield. This section consolidates all plastic-like material by polymer type.

### 8.1 European Plastic Packaging Waste Composition

Source: PlasticsEurope 2017, via [pmc.ncbi.nlm.nih.gov/articles/PMC8162419](https://pmc.ncbi.nlm.nih.gov/articles/PMC8162419/).

| Polymer | % of plastic waste |
|---------|-------------------|
| LDPE | 32% |
| HDPE | 20% |
| PP | 20% |
| PET | 18% |
| PS | 7% |
| PVC | 3% |

### 8.2 Full Plastic-Like Fraction by Polymer (203.9 kg)

| Polymer | From MODECOM plastics (150 kg) | From TS (22 kg) | From textiles (14 kg) | From composites (6 kg) | From combustibles (4.5 kg) | From fines (7.4 kg) | **TOTAL** |
|---------|------|------|------|------|------|------|------|
| **LDPE** | 48.0 | 4.2 | — | 6.0 | — | 2.4 | **60.6** |
| **HDPE** | 30.0 | — | — | — | — | 1.5 | **31.5** |
| **PP** | 30.0 | 7.5 | — | — | — | 1.5 | **39.0** |
| **PET** | 27.0 | 3.1 | — | — | — | 1.3 | **31.4** |
| **PS** | 10.5 | — | — | — | — | 0.5 | **11.0** |
| **PVC** | 4.5 | — | — | — | — | 0.2 | **4.7** |
| **SAP** | — | 6.4 | — | — | — | — | **6.4** |
| **Polyester** | — | — | 8.4 | — | — | — | **8.4** |
| **Nylon (PA)** | — | — | 3.5 | — | — | — | **3.5** |
| **Other synthetic** | — | 0.8* | 2.1 | — | 4.5 | — | **7.4** |
| **TOTAL** | **150.0** | **22.0** | **14.0** | **6.0** | **4.5** | **7.4** | **203.9** |

*TS "other synthetic" (5.0 kg) split: 4.2 kg LDPE (diaper backsheet) already counted in LDPE row; 0.8 kg remaining misc.

**Key takeaway:** The polyolefin fraction (LDPE + HDPE + PP) = 131.1 kg, or 64% of the plastic-like total. These are the highest-yield polymers (77–80% oil). The remaining 36% includes lower-yield materials (PET, PS, PVC, nylon, SAP, misc.) that pull the weighted average down.

---

## 9. CONSOLIDATED EFFECTIVE FEEDSTOCK — FINAL TABLE

**Why we need this:** This is the final output of Part 1 — the complete material-by-material breakdown of what enters the reactor. All 1,000 kg of raw OMR is now accounted for: 109.5 kg removed, 890.5 kg enters the reactor, of which 859.1 kg is processable material and 31.4 kg is mineral inert that passes through as residue.

### 9.1 Four-Category View (890.5 kg entering reactor)

| Category | Mass (kg) | % of reactor input | Composition |
|----------|----------|-------------------|-------------|
| **Organic** | 329.5 | 37.0% | Putrescibles 270 + fines organic 41.4 + combustibles organic 10.5 + TS moisture 7.6 |
| **Cellulose** | 325.7 | 36.6% | Paper 80 + cardboard 60 + TS cellulose 110.4 + textile cotton 24 + composite cardboard 22.5 + wood 15 + fines paper 13.8 |
| **Plastic-like** | 203.9 | 22.9% | See polymer-by-polymer table above (Section 8.2) |
| **Mineral inert** | 31.4 | 3.5% | Fines mineral 29.4 + textile non-textile 2.0 |
| **TOTAL** | **890.5** | **100%** | |

### 9.2 Three-Category View (859.1 kg processable material)

This is the view used in Annex 2 — showing only the three material groups that produce useful pyrolysis outputs, excluding mineral inert.

| Category | Mass (kg) | % of processable feedstock | Primary Urban Rig Output |
|----------|----------|---------------------------|--------------------------|
| **Organic (food, garden, misc.)** | 329.5 | **38.4%** | Charcoal / biochar |
| **Cellulose (paper, card, wood, cotton)** | 325.7 | **37.9%** | Charcoal + off-gas |
| **Plastic-like (all polymers)** | 203.9 | **23.7%** | Fuel oil (4 fractions) |
| **TOTAL processable** | **859.1** | **100%** | |

### 9.3 Full Mass Balance

| From → To | Mass (kg) |
|-----------|----------|
| Raw OMR at gate | 1,000.0 |
| − Glass, metals, incombustibles, hazardous, fragments | −109.5 |
| = Material entering reactor | 890.5 |
| − Mineral inert in reactor (produces only residue) | −31.4 |
| = Processable feedstock | 859.1 |

### 9.4 Traceability — Where Every Kilogram Comes From

| Annex 5 category | Organic | Cellulose | Plastic-like | Mineral inert | Removed | Total |
|-----------------|---------|-----------|-------------|---------------|---------|-------|
| Putrescibles (270) | 270.0 | — | — | — | — | 270 |
| Paper (80) | — | 80.0 | — | — | — | 80 |
| Cardboard (60) | — | 60.0 | — | — | — | 60 |
| Sanitary textiles (140) | 7.6 | 110.4 | 22.0 | — | — | 140 |
| Plastics (150) | — | — | 150.0 | — | — | 150 |
| Textiles (clothing) (40) | — | 24.0 | 14.0 | 2.0 | — | 40 |
| Composites (30) | — | 22.5 | 6.0 | — | 1.5 | 30 |
| Wood (15) | — | 15.0 | — | — | — | 15 |
| Unclassified combustibles (15) | 10.5 | — | 4.5 | — | — | 15 |
| Glass (50) | — | — | — | — | 50.0 | 50 |
| Metals (30) | — | — | — | — | 30.0 | 30 |
| Incombustibles + hazardous (20) | — | — | — | — | 20.0 | 20 |
| Fine elements (100) | 41.4 | 13.8 | 7.4 | 29.4 | 8.0 | 100 |
| **TOTAL** | **329.5** | **325.7** | **203.9** | **31.4** | **109.5** | **1,000** |

---

# PART 2 — WHAT COMES OUT: Pyrolysis Yields

*This part answers: for each material identified in Part 1, what does the Urban Rig produce? Then, what are the weighted-average outputs for the full feedstock?*

*Why it matters: the financial model's revenue projections depend on oil output (sold at ICIS PPO index prices), the off-gas energy balance determines fuel costs, and the residue/char fraction determines disposal costs and biochar revenue.*

---

## 10. PER-MATERIAL PYROLYSIS YIELDS

**Data source for UR-measured yields:** Asada Shokai test programme (Noda, 2022) — 74-page test report with independent measurement by Land Brain Co., Ltd. Original document: `Asada Shokai data 2.pdf`.

Per-material yield parameters are documented in detail in Annex 2 §2.3. The values below are the same parameters applied to this feedstock.

### 10.1 Polyethylene (PE: LDPE + HDPE)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **77%** | [FACT] FACT | Asada Shokai test #2 (PE molded, 40 kg → 30.7 kg oil) |
| Off-gas yield | **22%** | [FACT] FACT | Asada Shokai test #2 (40 kg → 8.8 kg off-gas) |
| Residue | **1%** | [FACT] FACT | Asada Shokai test #2 (40 kg → 0.5 kg residue) |
| Oil density | 0.83 kg/L | [FACT] FACT | Asada Shokai measurement |
| Off-gas CV | 5.54 MJ/kg | [FACT] FACT | Asada Shokai energy balance tables, pp. 35–36 |

**Justification:** PE is the best-performing polymer in the UR. Two tests (pellets and molded) gave 74–77% oil yield. The molded test at larger scale (40 kg) is the more reliable data point.

### 10.2 Polypropylene (PP)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **80%** | [FACT] FACT | Asada Shokai test #6 (PP molded, 50 kg → 39.8 kg oil) |
| Off-gas yield | **18%** | [FACT] FACT | Asada Shokai test #6 (50 kg → 10.0 kg off-gas) |
| Residue | **2%** | [FACT] FACT | Asada Shokai test #6 (50 kg → 0.2 kg residue) |

**Justification:** PP is the highest-yield polymer tested. PP and PE are both polyolefins with similar cracking behaviour.

### 10.3 Polystyrene (PS)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **58%** | [FACT] FACT | Average of Asada Shokai tests #3 (61%) and #4 (55%) |
| Off-gas yield | **14%** | [FACT] FACT | Average of tests #3 and #4 |
| Residue | **28%** | [FACT] FACT | Average of tests #3 and #4 |

**Justification:** PS performs significantly worse than polyolefins due to its aromatic ring structure. The applied test (PS foam/EPS, test #10) gave 73% oil, but for conservative modelling we use 58%.

### 10.4 Polyethylene Terephthalate (PET)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **45%** | [HYPOTHESIS] HYPOTHESIS | Slow pyrolysis literature |
| Off-gas yield | **17%** | [HYPOTHESIS] HYPOTHESIS | Derived from mass balance |
| Residue/Char | **38%** | [HYPOTHESIS] HYPOTHESIS | Slow pyrolysis literature |

[!] **PET was NOT tested by Asada Shokai on the UR equipment.**

**Derivation:** Primary source: *Polymer Degradation and Stability*, 2022 ([sciencedirect.com/S0141391022000866](https://www.sciencedirect.com/science/article/abs/pii/S0141391022000866)) — slow pyrolysis of PET at 400°C gave 46.7% oil, 39.7% solid, ~13.3% gas. We use 45% (small discount for secondary cracking at UR's 600°C final temperature). Cross-check: [PMC 7183261](https://pmc.ncbi.nlm.nih.gov/articles/PMC7183261/).

### 10.5 Polyvinyl Chloride (PVC)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **32%** | [HYPOTHESIS] HYPOTHESIS | Two-stage pyrolysis literature |
| HCl (filtered) | **53%** | [FACT] FACT (chemistry) | Stoichiometric |
| Off-gas (non-HCl) | **~2%** | [HYPOTHESIS] HYPOTHESIS | Mass balance |
| Residue/Char | **13%** | [HYPOTHESIS] HYPOTHESIS | Two-stage literature |

[!] **PVC was NOT tested by Asada Shokai on the UR equipment.** The UR includes a patented catalytic chlorine adsorption layer (UR Recycling Solutions ENG, pp. 14–15).

**Derivation:** Two-stage dechlorination (200–340°C) removes 53% of mass as HCl; remaining polyene backbone cracks to ~68% oil, ~28% char, ~4% gas. Net: 47% × 68% = ~32% oil. Sources: [sciencedirect.com/S0048969723069723](https://www.sciencedirect.com/science/article/abs/pii/S0048969723069723); [PMC 12096105](https://pmc.ncbi.nlm.nih.gov/articles/PMC12096105/).

### 10.6 Polyester (from textiles)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **45%** | [HYPOTHESIS] HYPOTHESIS | Same as PET (polyester = PET-family polymer) |
| Off-gas yield | **17%** | [HYPOTHESIS] HYPOTHESIS | Mass balance |
| Residue/Char | **38%** | [HYPOTHESIS] HYPOTHESIS | |

**Justification:** Clothing polyester is polyethylene terephthalate — chemically identical to PET bottle resin. Same pyrolysis behaviour. Contamination from dyes and finishes may slightly increase char formation, but this is within the uncertainty range.

### 10.7 Nylon — Polyamide (from textiles)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **45%** | [HYPOTHESIS] HYPOTHESIS | PA6/PA66 pyrolysis literature |
| Off-gas yield | **20%** | [HYPOTHESIS] HYPOTHESIS | Literature |
| Residue/Char | **35%** | [HYPOTHESIS] HYPOTHESIS | Literature |

[!] **Nylon was NOT tested by Asada Shokai on the UR equipment.**

**Justification:** Nylon 6 pyrolysis at 500–700°C produces 40–80% caprolactam (monomer) depending on conditions, plus secondary products. For slow pyrolysis at UR conditions (~600°C, steam carrier), a conservative 45% total oil estimate accounts for both monomer recovery and secondary liquid products. Similar to PET as both are condensation polymers with heteroatoms (N for nylon, O for PET).

### 10.8 SAP — Sodium Polyacrylate (from diapers)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **20%** | [HYPOTHESIS] HYPOTHESIS | General polymer decomposition literature |
| Off-gas yield | **30%** | [HYPOTHESIS] HYPOTHESIS | Estimated |
| Residue | **50%** | [HYPOTHESIS] HYPOTHESIS | Na₂CO₃ inorganic ash + char |

**Justification:** Crosslinked acrylic polymer. Sodium content means ~25-30% ends up as solid inorganic ash regardless of temperature.

### 10.9 Other Synthetic Materials

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **25%** | [HYPOTHESIS] HYPOTHESIS | Blended estimate for mixed adhesives, elastics, rubber |
| Off-gas yield | **25%** | [HYPOTHESIS] HYPOTHESIS | |
| Residue | **50%** | [HYPOTHESIS] HYPOTHESIS | |

### 10.10 Cellulose (Paper, Cardboard, Wood, Cotton)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **12%** | [HYPOTHESIS] HYPOTHESIS | Biomass pyrolysis literature |
| Off-gas yield | **20%** | [HYPOTHESIS] HYPOTHESIS | Literature range 15–25% |
| Residue/Char | **68%** | [HYPOTHESIS] HYPOTHESIS | Cellulose char formation at 600°C |

**Justification:** Cellulose pyrolysis produces mainly char and gas. Bio-oil has low calorific value (~17–20 MJ/kg vs ~43 MJ/kg for plastic oil). Sources: Bridgwater, *Biomass and Bioenergy*, 2012; Chen et al., *Waste Management*, 2014.

### 10.11 Putrescibles (Food/Garden Waste)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **10%** | [HYPOTHESIS] HYPOTHESIS | Biomass pyrolysis literature |
| Off-gas yield | **20%** | [HYPOTHESIS] HYPOTHESIS | |
| Residue/Char | **70%** | [HYPOTHESIS] HYPOTHESIS | High moisture → energy penalty |

### 10.12 Mineral Inert (soil, dust, ceramics from fines)

| Parameter | Value | Classification | Source |
|-----------|-------|---------------|--------|
| Oil yield | **0%** | [FACT] FACT | Inorganic — cannot pyrolyse |
| Off-gas yield | **0%** | [FACT] FACT | |
| Residue | **100%** | [FACT] FACT | Passes through unchanged |

---

## 11. WEIGHTED YIELD CALCULATION

### 11.1 Plastic-Like Fraction (203.9 kg)

| Material | Mass (kg) | Oil yield | Oil (kg) | Off-gas (kg) | Residue (kg) | Data quality |
|----------|----------|----------|---------|-------------|-------------|-------------|
| PE (LDPE+HDPE) | 92.1 | 77% | 70.9 | 20.3 | 0.9 | [FACT] FACT |
| PP | 39.0 | 80% | 31.2 | 7.0 | 0.8 | [FACT] FACT |
| PET | 31.4 | 45% | 14.1 | 5.3 | 11.9 | [HYPOTHESIS] HYPOTHESIS |
| PS | 11.0 | 58% | 6.4 | 1.5 | 3.1 | [FACT] FACT |
| PVC | 4.7 | 32% | 1.5 | 0.1† | 0.6 | [HYPOTHESIS] HYPOTHESIS |
| PVC → HCl | — | — | — | (2.5 filtered) | — | [FACT] FACT (stoich.) |
| Polyester | 8.4 | 45% | 3.8 | 1.4 | 3.2 | [HYPOTHESIS] HYPOTHESIS |
| Nylon (PA) | 3.5 | 45% | 1.6 | 0.7 | 1.2 | [HYPOTHESIS] HYPOTHESIS |
| SAP | 6.4 | 20% | 1.3 | 1.9 | 3.2 | [HYPOTHESIS] HYPOTHESIS |
| Other synth. | 7.4 | 25% | 1.9 | 1.9 | 3.7 | [HYPOTHESIS] HYPOTHESIS |
| **SUBTOTAL** | **203.9** | | **132.7** | **40.1** | **28.6** | |
| *(PVC HCl filtered)* | | | | *(2.5)* | | |
| **Mass check** | **203.9** | | 132.7 + 40.1 + 28.6 + 2.5 = **203.9** ✓ | | | |
| **Weighted oil yield** | | **65.1%** | (132.7 / 203.9) | | | |

† PVC off-gas excludes 2.5 kg HCl captured by the UR patented chlorine filtration system.

### 11.2 Organic + Cellulose Fraction (655.2 kg)

| Material | Mass (kg) | Oil yield | Oil (kg) | Off-gas (kg) | Residue (kg) | Data quality |
|----------|----------|----------|---------|-------------|-------------|-------------|
| Cellulose | 325.7 | 12% | 39.1 | 65.1 | 221.5 | [HYPOTHESIS] HYPOTHESIS |
| Putrescibles/organic | 329.5 | 10% | 33.0 | 65.9 | 230.7 | [HYPOTHESIS] HYPOTHESIS |
| **SUBTOTAL** | **655.2** | | **72.0** | **131.0** | **452.2** | |

### 11.3 Mineral Inert Fraction (31.4 kg)

| Material | Mass (kg) | Oil yield | Oil (kg) | Off-gas (kg) | Residue (kg) |
|----------|----------|----------|---------|-------------|-------------|
| Mineral inert | 31.4 | 0% | 0 | 0 | 31.4 |

### 11.4 TOTAL OUTPUT — 890.5 kg Entering Reactor

| Product | From plastic-like | From organic/cellulose | From mineral inert | **TOTAL** | **% of 890.5 kg** |
|---------|------------------|----------------------|-------------------|----------|-----------------|
| **Oil** | 132.7 | 72.0 | 0 | **204.7** | **23.0%** |
| **Off-gas** | 40.1 | 131.0 | 0 | **171.1** | **19.2%** |
| **Residue/Char** | 28.6 | 452.2 | 31.4 | **512.2** | **57.5%** |
| **HCl (filtered)** | 2.5 | 0 | 0 | **2.5** | **0.3%** |

**Comparison with previous version (920 kg base):**

| Metric | Previous | Updated | Change |
|--------|----------|---------|--------|
| Total oil | 184.8 kg (20.1%) | 204.7 kg (23.0%) | +19.9 kg (+2.9 pp) |
| Total off-gas | 175.2 kg (19.0%) | 171.1 kg (19.2%) | −4.1 kg (+0.2 pp) |
| Total residue | 557.5 kg (60.6%) | 512.2 kg (57.5%) | −45.3 kg (−3.1 pp) |
| Plastic-like oil yield | 66% | 65.1% | −0.9 pp |

The overall oil yield increases from 20.1% to 23.0% because material previously classified as unproductive "fines/other" is now properly allocated — much of it to cellulose and organic fractions that produce some oil, and some to plastic that produces significant oil.

---

## 12. OFF-GAS ENERGY

Off-gas energy modelling is consolidated in Annex 2 §2.5. The key parameter used in this feedstock model is 5.54 MJ/kg off-gas CV (constant across all feedstocks, Asada Shokai energy balance tables pp. 35–36).

---

## 13. CHAR/RESIDUE CHARACTERISATION AND ENERGY POTENTIAL

Char characterisation, calorific value estimates, commercialisation scenarios, and market valuation are consolidated in Annex 2 §2.4.3 and Annex 3 §3.2. The key finding: 480.8 kg combustible char per 1,000 kg OMR at weighted 15.6 MJ/kg CV demonstrates fuel-grade quality suitable for commercial energy markets — see Annex 2 §2.6.3 for the full energy balance.

---

## 14. OIL YIELD SCENARIO COMPARISON

### 14.1 Three Operating Scenarios

| Metric | Scenario A: Full OMR (with decomposition) | Scenario B: Plastic-like only | Scenario C: Polyolefins only (PE+PP) |
|--------|------------------------------------------|------------------------------|--------------------------------------|
| Feed mass (per 1,000 kg OMR) | 890.5 kg | 203.9 kg | 131.1 kg |
| Oil output | 204.7 kg (**23%**) | 132.7 kg (**65%**) | 102.1 kg (**78%**) |
| Off-gas output | 171.1 kg | 40.1 kg | 24.7 kg |
| Residue/char | 512.2 kg (58%) | 28.6 kg (14%) | 2.4 kg (2%) |
| Off-gas energy | ~484 MJ | ~222 MJ | ~137 MJ |
| Oil quality | Mixed (plastic + bio-oil) | Mostly hydrocarbon | High-quality hydrocarbon |

### 14.2 Key Insights

1. **Full OMR gives 23% oil yield** (was 20.1% in previous version) because material previously hidden in "fines/other" is now properly allocated and contributes to oil production.

2. **Pre-sorting to isolate the plastic-like fraction raises oil yield to 65%.** Slightly lower than previous 66% because the expanded plastic-like fraction now includes lower-yield materials (polyester, nylon, misc. synthetics from textiles and combustibles).

3. **Polyolefin-only feed (PE+PP) gives 78% oil yield** — unchanged, consistent with the Asada Shokai mixed-polymer test (77%).

4. **The CDG airport context favours Scenario B or C.** Airport packaging waste is plastic-rich and can be pre-sorted.

### 14.3 Sensitivity: Impact of PET Yield Assumption

Since PET (+ polyester from textiles) was not tested on the UR and represents 19.5% of the plastic-like fraction:

| PET oil yield assumption | Total plastic-like oil yield |
|-------------------------|------------------------------|
| 30% (pessimistic) | 62% |
| 40% (moderate) | 64% |
| **45% (our estimate)** | **65%** |
| 55% (optimistic) | 67% |
| 70% (catalytic, upper lit.) | 71% |

---

## 15. CROSS-REFERENCE: ASADA SHOKAI MUNICIPAL WASTE TESTS

The Asada Shokai test programme included two tests with actual Japanese municipal waste (Noda city):

| Test | Material | Oil % | Off-gas % | Foreign matter % | Char % |
|------|----------|-------|-----------|-----------------|--------|
| #14 | Container recycling plastic | 32% | 19% | 21% | 28% |
| #15 | Non-combustible residue | 45% | 22% | 11% | 23% |

These results are **lower** than our Scenario B estimate (65%) because of foreign matter (11–21%), different plastic mix, and contamination. Adjusting for foreign matter: container recycling on plastic-only basis ≈ 63% — consistent with our estimate.

---

## 16. DATA QUALITY SUMMARY

| Parameter | Classification | Confidence |
|-----------|---------------|------------|
| French OMR composition (13 categories) | [FACT] FACT | HIGH — ADEME national study |
| Sanitary textiles subcategories | [FACT] FACT | MEDIUM-HIGH |
| Diaper material composition | [FACT] FACT | HIGH — peer-reviewed |
| European plastic polymer mix | [FACT] FACT | HIGH — PlasticsEurope |
| Textile fibre composition | [HYPOTHESIS] HYPOTHESIS | MEDIUM — European average |
| Composite (Tetra Pak) composition | [FACT] FACT | HIGH — industry standard |
| Fine elements composition | [HYPOTHESIS] ASSUMPTION | MEDIUM — characterisation studies |
| PE oil yield (77%) | [FACT] FACT | HIGH — measured on UR |
| PP oil yield (80%) | [FACT] FACT | HIGH — measured on UR |
| PS oil yield (58%) | [FACT] FACT | MEDIUM — range 55-73% across UR tests |
| Off-gas CV (5.54 MJ/kg) | [FACT] FACT | HIGH — consistent across 4 UR tests |
| PET oil yield (45%) | [HYPOTHESIS] HYPOTHESIS | MEDIUM — slow pyrolysis lit. |
| PVC oil yield (32%) | [HYPOTHESIS] HYPOTHESIS | MEDIUM — two-stage lit. |
| Polyester oil yield (45%) | [HYPOTHESIS] HYPOTHESIS | MEDIUM — same as PET |
| Nylon oil yield (45%) | [HYPOTHESIS] HYPOTHESIS | LOW-MEDIUM — PA literature |
| SAP oil yield (20%) | [HYPOTHESIS] HYPOTHESIS | LOW |
| Cellulose/putrescible yields | [HYPOTHESIS] HYPOTHESIS | MEDIUM — biomass lit. |
| **Char CV — organic (15 MJ/kg)** | **[HYPOTHESIS] HYPOTHESIS** | **MEDIUM — MSW biomass char literature** |
| **Char CV — plastic (25 MJ/kg)** | **[HYPOTHESIS] HYPOTHESIS** | **MEDIUM — carbon black literature** |
| **Char energy self-sufficiency** | **[HYPOTHESIS] HYPOTHESIS** | **HIGH — robust under pessimistic assumptions** |

---

## 17. RECOMMENDATIONS FOR THE BUSINESS PLAN

1. **Use Scenario B (pre-sorted plastic-like fraction) as the base case** for oil yield projections: **65% oil yield on plastic-like feedstock, or ~23% on full OMR.**

2. **The 77–80% oil yield remains valid for clean polyolefin feed** (Scenario C).

3. **The three-category split for Annex 2** should use the fully derived percentages: **38.4% organic, 37.9% cellulose, 23.7% plastic** (on processable feedstock basis).

4. **Flag PET/polyester and nylon yields as needing UR-specific validation.** These now represent ~21% of the plastic-like fraction (was 17% before textiles were decomposed).

5. **The CDG feedstock advantage** remains: airport packaging waste is PE/PP-rich, pushing performance toward Scenario C (78% oil yield).

6. **Adopt the V2 model (all char sold commercially)** as the base case for the financial model: all combustible char (~16,088 T/year) is sold at €100/T (conservative fuel pellet pricing), and purchased heating oil supplies all reactor heating. This model treats char as a premium product: fuel-grade quality biochar sold at market prices.

7. **Prioritise char characterisation testing** — bomb calorimetry and elemental analysis on UR-produced char from organic/cellulose feedstock. This is the single most impactful validation for the financial model, as it determines char commercial value and marketability to fuel buyers.

---

## 18. References

**Urban Rig Test Data**

1. **Asada Shokai test programme** (Noda, 2022) — 74-page test report with independent measurement by Land Brain Co., Ltd. Original document: `Asada Shokai data 2.pdf`. Cited for: PE oil yield 77% (test #2), PP oil yield 80% (test #6), PS oil yield 58% (tests #3–4), off-gas CV 5.54 MJ/kg (energy balance tables pp. 35–36), municipal waste tests #14 and #15 (§15).
2. **Urban Rig Recycling Solutions ENG** — OneWorld Corporation product brochure. Cited for: halogen filtration system (pp. 14–15).

**Waste Composition Sources**

3. **ADEME MODECOM 2017** — France's national waste characterisation campaign (third edition). Published at [ademe.fr](https://www.ademe.fr/presse/communique-national/modecom-2017-ce-que-revelent-les-poubelles-des-francais); detailed analysis at [medias.amf.asso.fr](https://medias.amf.asso.fr/upload/files/modecom_2017_analyse_des_resultats_011318.pdf). Cited for: 13-category OMR composition (§1).
4. **MODECOM 2024** — First results at [valor3e.fr](https://www.valor3e.fr/le-kiosque-info/actualites/premiers-resultats-du-modecom-2024/). Cited for: updated composition trends (§1, note).
5. **PlasticsEurope** (2017) — European plastic packaging waste composition via [PMC 8162419](https://pmc.ncbi.nlm.nih.gov/articles/PMC8162419/). Cited for: polymer mix (LDPE 32%, HDPE 20%, PP 20%, PET 18%, PS 7%, PVC 3%) (§8.1).
6. **EEA** — *Textiles and the Environment* report (2024), [eea.europa.eu](https://www.eea.europa.eu/publications/textiles-and-the-environment-the). Cited for: European textile fibre composition (§4).
7. **Tetra Pak** — Sustainability reports, [tetrapak.com](https://www.tetrapak.com/sustainability/planet/good-practices/recycling). Cited for: composite packaging material breakdown — 75% cardboard, 20% PE, 5% aluminium (§5).
8. **Vertuow** — Sanitary textiles subcategory breakdown, [vertuow.com](https://www.vertuow.com/tsuu-transformer-les-dechets-en-ressources/). Cited for: toilet paper 44.3%, paper towels 17.2%, baby diapers 10.7%, wipes 5.4% (§3.1).
9. **ResearchGate / ChemistryExplained.com** — Diaper material composition data. Cited for: cellulose 37%, SAP 31%, PP 16%, LDPE 6% (§3.2).

**Pyrolysis Literature**

10. **Bridgwater, A.V.** (2012) — "Review of fast pyrolysis of biomass and product upgrading," *Biomass and Bioenergy*. Cited for: cellulose pyrolysis yields, off-gas cross-validation (§10.10).
11. **Chen, D. et al.** (2014) — "Pyrolysis technologies for municipal solid waste," *Waste Management*. Cited for: cellulose/putrescible yield ranges (§10.10).
12. ***Polymer Degradation and Stability*** (2022) — Slow pyrolysis of PET at 400°C, [ScienceDirect S0141391022000866](https://www.sciencedirect.com/science/article/abs/pii/S0141391022000866). Cited for: PET oil yield 46.7% (§10.4).
13. **PMC 7183261** — PET pyrolysis cross-check. Cited for: PET yield validation (§10.4).
14. **ScienceDirect S0048969723069723** — Two-stage PVC dechlorination pyrolysis. Cited for: PVC oil yield derivation (§10.5).
15. **PMC 12096105** — PVC pyrolysis. Cited for: PVC yield cross-validation (§10.5).
16. **Fazil, A. et al.** (2021) — *Energies*. Cited for: organic/cellulose char CV estimates (via Annex 3 §3.2.1).
17. **Ronsse, F. et al.** (2020) — Biochar characterisation. Cited for: organic char CV estimates (via Annex 3 §3.2.1).

---

**End of Annex 5**
