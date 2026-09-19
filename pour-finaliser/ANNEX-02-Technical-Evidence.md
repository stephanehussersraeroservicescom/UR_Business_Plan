# Annex 2 — Technical Evidence

**Purpose:** Consolidates all measured test data, laboratory analyses, emission certifications, per-material pyrolysis yields, off-gas energy modelling, and the energy balance for the Urban Rig system. Every parameter is classified as FACT (measured on UR equipment), HYPOTHESIS (literature-based estimate), or ASSUMPTION (engineering judgement). Sources are cited inline throughout.

**Date:** March 2026

---

## 2.1 Test Programme Overview

All Urban Rig--specific test data originates from a controlled test campaign conducted at the Asada Shokai facility (Noda, Chiba Prefecture, Japan) between March and September 2022, supervised by Land Brain Co., Ltd. and documented in a 74-page Industrial Waste Test Research Report. Tests were performed on the Urban Rig batch unit using individual plastic types and mixed plastic batches.

**Limitations of the test programme:**

- All tests used the **batch** unit, not the continuous URC-2000 production machine. Batch-to-continuous scaling factors are manufacturer specifications, not independently verified (see §2.6).
- **No non-plastic organic feedstock** (food waste, paper, wood) was tested on the UR. All organic pyrolysis parameters are literature estimates.
- **PET, PVC, nylon, and SAP** were not tested on the UR. Their yields are derived from published pyrolysis literature.
- Two mixed-waste tests (September 2022) yielded 32.2% and 45.0% oil, but the plastic fraction of the mixed waste was not measured, making back-calculation of per-material yields impossible (Asada Shokai test report, pp. 35--36).

---

## 2.2 Pure Plastic Test Results — Measured Oil and Off-Gas Yields

### 2.2.1 Individual Polymer Tests (9 Runs)

The following data comes from single-polymer tests on the UR batch unit. Off-gas mass is calculated by mass difference (input $-$ oil $-$ residue), not directly measured (Asada Shokai test report, Section 6).

| Date | Feedstock | Input (kg) | Oil (kg) | Oil % | Off-gas (kg) | OG % | Residue (kg) | Res % |
|------|-----------|-----------|---------|-------|-------------|------|-------------|-------|
| 2022-03-02 | PE pellets | 20 | 14.8 | 74.0% | 4.9 | 24.5% | 0.3 | 1.5% |
| 2022-03-09 | PE molded offcuts | 40 | 30.7 | 76.8% | 8.8 | 22.0% | 0.5 | 1.2% |
| 2022-06-21 | PE poly containers | 50 | 40.7 | 81.4% | 8.4 | 16.8% | 0.9 | 1.8% |
| 2022-04-08 | PP pellets | 20 | 16.2 | 81.0% | 3.3 | 16.5% | 0.5 | 2.5% |
| 2022-04-16 | PP molded offcuts | 50 | 39.8 | 79.6% | 10.0 | 20.0% | 0.2 | 0.4% |
| 2022-06-28 | PP pallets | 50 | 36.5 | 73.0% | 7.4 | 14.8% | 6.1 | 12.2% |
| 2022-03-17 | PS pellets | 20 | 12.2 | 61.0% | 4.0 | 20.0% | 3.8 | 19.0% |
| 2022-03-31 | PS molded offcuts | 40 | 22.0 | 55.0% | 2.7 | 6.8% | 15.3 | 38.2% |
| 2022-07-07 | PS foam | 50 | 36.3 | 72.6% | 3.8 | 7.6% | 9.9 | 19.8% |

*Source: Asada Shokai Industrial Waste Test Research Report, Section 6 (September 2022).*

### 2.2.2 Summary by Polymer Type

| Polymer | Tests | Avg Oil % | Avg Off-gas % | OG % Range | Avg Residue % |
|---------|-------|-----------|--------------|-----------|--------------|
| PE | 3 | 77.4% | 21.1% | 16.8--24.5% | 1.5% |
| PP | 3 | 77.9% | 17.1% | 14.8--20.0% | 5.0% |
| PS | 3 | 62.9% | 11.5% | 6.8--20.0% | 25.7% |

**Key observations:**

- PE and PP (polyolefins) perform similarly: 77--78% oil yield, 17--21% off-gas, minimal residue. These are the dominant plastics in MSW at approximately 60 wt% of the plastic fraction (ADEME MODECOM 2017).
- PS produces significantly more residue (19--38%) and less oil (55--73%) than polyolefins, consistent with PS forming styrene oligomers that remain in the char.
- Mass balance closes perfectly in all nine tests (input = oil + off-gas + residue).

### 2.2.3 Mixed Plastic Energy Balance Tests (2 Runs)

Two additional tests with mixed PE/PP/PS ("3P") feedstock included detailed energy inputs and outputs (Asada Shokai test report, p. 35):

| Parameter | Test 1 (2022-05-26, 3P pellets) | Test 2 (2022-07-11, 3P offcuts) |
|-----------|--------------------------------|--------------------------------|
| Input | 60 kg | 60 kg |
| Oil output | 43.1 kg (71.8%) | 49.4 kg (82.3%) |
| Off-gas | 11.7 kg (19.5%) | 1.3 kg (2.2%) |
| Residue | 5.2 kg (8.7%) | 9.3 kg (15.5%) |
| Electricity consumed | 65 kWh (55,900 kcal) | 65 kWh (55,900 kcal) |
| Light oil consumed (heating) | 66 L (599,808 kcal) | 76 L (690,688 kcal) |
| Off-gas recycled as fuel | 15,489 kcal | 1,721 kcal |
| Water (steam generation) | 85 L | 95 L |
| **Total energy input** | **671,197 kcal** | **748,309 kcal** |

*Source: Asada Shokai energy balance test reports, p. 35.*

**Observations:**

- Oil yield ranges from 71.8% to 82.3% for mixed PE/PP/PS, supporting the **70% conservative assumption** used in the financial model.
- Off-gas mass varies enormously (11.7 kg vs 1.3 kg), likely reflecting batch startup conditions and off-gas capture variability rather than feedstock differences.
- Mass balance closes perfectly (60.0 kg out = 60.0 kg in) in both tests.

---

## 2.3 Per-Material Pyrolysis Yields — Full Polymer Set

For materials not tested on the UR, yields are estimated from published pyrolysis literature. These are required because MSW contains polymers beyond PE/PP/PS.

### 2.3.1 UR-Measured Polymers

| Polymer | Oil Yield | Off-gas Yield | Residue | Data Quality |
|---------|----------|--------------|---------|-------------|
| PE (LDPE + HDPE) | **77%** | **22%** | **1%** | FACT — Asada Shokai test #2 (PE molded, 40 kg) |
| PP | **80%** | **18%** | **2%** | FACT — Asada Shokai test #6 (PP molded, 50 kg) |
| PS | **58%** | **14%** | **28%** | FACT — Average of Asada Shokai tests #3 and #4 |

### 2.3.2 Literature-Estimated Polymers

| Polymer | Oil Yield | Off-gas Yield | Residue | Source |
|---------|----------|--------------|---------|--------|
| PET | **45%** | **17%** | **38%** | *Polymer Degradation and Stability*, 2022 (slow pyrolysis at 400°C: 46.7% oil, 39.7% solid); cross-check: PMC 7183261 |
| PVC | **32%** | **~2%** | **13%** | Two-stage dechlorination literature; 53% of mass exits as HCl (stoichiometric, captured by UR catalytic layer); net oil: 47% × 68% ≈ 32%. Sources: *Science of the Total Environment*, 2024; PMC 12096105 |
| Polyester (textile) | **45%** | **17%** | **38%** | Same as PET — clothing polyester is chemically identical to PET resin |
| Nylon (PA6/PA66) | **45%** | **20%** | **35%** | PA6 pyrolysis at 500--700°C produces 40--80% caprolactam; conservative 45% total oil accounts for secondary products |
| SAP (sodium polyacrylate) | **20%** | **30%** | **50%** | Crosslinked acrylic polymer; Na content yields ~25--30% inorganic ash (Na$_2$CO$_3$) |
| Other synthetics | **25%** | **25%** | **50%** | Blended estimate for mixed adhesives, elastics, rubber |

[!] **PET, PVC, nylon, and SAP have NOT been tested on the UR.** Validation on UR equipment is recommended.

### 2.3.3 Non-Plastic Materials

| Material | Oil Yield | Off-gas Yield | Residue/Char | Source |
|----------|----------|--------------|-------------|--------|
| Cellulose (paper, cardboard, wood, cotton) | **12%** | **20%** | **68%** | Bridgwater, *Biomass and Bioenergy*, 2012; Chen et al., *Waste Management*, 2014. Bio-oil has low CV (~17--20 MJ/kg vs ~43 MJ/kg for plastic oil) |
| Putrescibles (food/garden waste) | **10%** | **20%** | **70%** | Biomass pyrolysis literature. High moisture imposes energy penalty |
| Mineral inert | **0%** | **0%** | **100%** | Inorganic — passes through unchanged |

[!] **No non-plastic organic feedstock has been tested on the UR.** All organic yields are HYPOTHESIS.

---

## 2.4 Oil Quality — Certified Laboratory Analysis

### 2.4.1 NKKK Fuel Certification

The produced oil was tested and certified by NKKK (Nippon Kaiji Kentei Kyokai — Japan Marine Survey Association) under JIS standards:

| Parameter | Result | Comparison |
|-----------|--------|------------|
| Calorific value | **43.27 MJ/kg** | Fossil diesel: 42.6 MJ/kg |
| Flashpoint | 46°C | — |
| Sulfur content | **0.014%** | Below IMO 2020 marine fuel limit (0.5%) |
| Chlorine content | **1 ppm** | Well below problematic levels |

*Source: NKKK recycled fuel test report, JIS standards.*

### 2.4.2 Oil Fraction Distribution by Temperature Zone

The URC-2000 continuous process separates oil into four fractions by temperature-controlled condensation. The expected distribution is supported by independent laboratory distillation data.

**Oil Fraction Characteristics by URC-2000 Zone:**

| **URC-2000 Zone** | **Temperature** | **Expected %** | **Oil Type** | **Flash Point** | **Density (SG)** | **Sulfur** | **Calorific Value** | **Possible Uses** | **Sources / Justification** |
|---|---|---|---|---|---|---|---|---|---|
| Zone 1 (GET) | 150°C | **~10%** | Heating Oil (Light naphtha), C5--C8 | < 21°C | 0.70--0.76 | 19--30 ppm | ~44--46 MJ/kg | Internal fuel (machine operation); Petrochemical feedstock (naphtha); Industrial solvent | URC-2000 brochure (10%); Asada Shokai p.28: lightest Class 1 fraction (Tb <150°C); SG/S from Class 1 PE (0.756, 19 ppm) |
| Zone 2 (GET) | 300°C | **~80%** | Gas (Diesel) Oil (Kerosene + Diesel), C8--C20 | 40--55°C | 0.80--0.86 | 50--150 ppm | 43--47 MJ/kg | Recycled diesel fuel (NKKK certified); SAF co-processing feedstock (Tier 1--3); JIS Class A/B heavy fuel oil equivalent; Industrial boiler combustion | URC-2000 brochure (80%); Asada Shokai p.28: Class 2+ (52--70%) + heavy Class 1 (Tb 150--300°C); Ohsumi Tab.3-8: flash <40°C, 43--47 MJ/kg; NKKK: flash ≤40°C, S 0.014%, 43.27 MJ/kg |
| Zone 3 (GET) | 450°C | **~10%** | Heavy Oil, C20+ | > 70°C | > 0.90 | 100--200 ppm | 40--45 MJ/kg | Industrial heavy fuel oil; High-capacity boiler fuel; Bitumen/asphalt feedstock | URC-2000 brochure (10%); Asada Shokai: heavy tail of Class 2+ (Tb >300°C); Ohsumi Tab.3-9: comparable to JIS heavy fuel oil C |
| Zone 4 (GET) | 600°C | Traces | Asphaltenes (semi-solid residue) | n/a | > 1.0 | Variable | ~32 MJ/kg | Solid fuel (carbide); Soil amendment (biochar) | URC-2000 brochure; Ismitec: urethane carbide 32.09 MJ/kg |

*Source: URC-2000 product brochure (One World Japan); Asada Shokai report Section 7.2 p.28; Ohsumi Verification Report Table 3-8; NKKK certified test report; Ismitec calorific certificates.*

**Compatibility Analysis — Distillation Data vs. 10/80/10 Dispatch:**

The Asada Shokai report (Section 7.2, p.28) provides the only independent laboratory distillation of crude pyrolysis oil, separating it into Japanese petroleum Class 1 (flash point < 21°C) and Class 2+ (flash point > 21°C). The results are:

| Plastic | Class 1 Vol. | Flash | SG | % Class 1 | Class 2+ Vol. | Flash | SG | % Class 2+ | Recovery |
|---------|-------------|-------|-----|-----------|--------------|-------|-----|------------|----------|
| PE | 61 ml | 18°C | 0.756 | 30.5% | 139 ml | 55°C | 0.860 | 69.5% | 100% |
| PP | 56 ml | 18°C | 0.760 | 33% | 114 ml | 45°C | 0.820 | 67% | 85% |
| PS | 90 ml | 16°C | 0.870 | 45% | 110 ml | 53°C | 0.900 | 55% | 100% |
| 3P (mix) | 96 ml | 16°C | 0.788 | 48% | 104 ml | 52.5°C | 0.834 | 52% | 100% |

*Source: Asada Shokai Industrial Waste Test Research Report (産業廃棄物試験研究終了報告書), Section 7.2, p.28 (January 2023). Samples of 200 ml per test.*

The apparent discrepancy between 30--48% Class 1 (distillation) and the manufacturer's 10% light oil fraction is explained by the difference in separation methods. Flash point ≠ boiling point: a compound classified as "Class 1" (flash < 21°C) can have a boiling point of 100--150°C+. In the URC-2000's condensation-based system, such compounds condense in Zone 2 (300°C), not Zone 1 (150°C). Only the lightest naphtha (boiling point < 150°C) is captured in Zone 1. The heavy portion of Class 1 (boiling point 150--300°C) joins the Class 2+ diesel/kerosene fraction in Zone 2, while the heaviest tail of Class 2+ (boiling point > 300°C) moves to Zone 3. This makes the 10/80/10 distribution consistent with the measured distillation data.

[!] **The 10/80/10 distribution is a manufacturer specification for the continuous URC-2000. No independent test of the continuous machine's actual zone-by-zone output has been conducted.** The Asada Shokai distillation data confirms oil composition is compatible with this distribution but was performed on batch-produced crude oil, not on zone-separated output from the URC-2000.

### 2.4.3 GC-MS Oil Composition (Qualitative Only)

Gas chromatography--mass spectrometry analysis performed by the Osaka Institute of Industrial Science and Technology on oil from the Asada Shokai test programme identified the principal compounds in the volatile (gas oil) fraction:

- Dimethylheptane (C$_9$)
- Undecene (C$_{11}$)
- Trimethylnonane (C$_{12}$)

These are middle-distillate hydrocarbons in the C$_8$--C$_{16}$ range, confirming that the dominant oil fraction (~80% of liquid output) is in the diesel/kerosene/naphtha range — directly usable as feedstock for steam crackers or refinery co-processing (Osaka Institute GC-MS report).

[!] **The GC-MS quantitative data (54% heavy / 25% diesel) is INVALIDATED due to equipment malfunction during the test (overheating caused loss of the diesel fraction). Only the qualitative compound identification (C7--C16 chain range) is retained.** The GC-MS tested the entire mixed oil sample, not a separated fraction.

### 2.4.3 Char Calorific Value

**Literature baseline:** Published pyrolysis literature reports the following char calorific values for conventional (non-superheated-steam) pyrolysis systems:

| Char source | Literature CV (MJ/kg) | Range | Literature basis |
|-------------|----------------------|-------|-----------------|
| MSW biomass char (organic/cellulose) | 8--22 | Wide, depends on ash content and process temperature | Fazil et al., *Energies*, 2021; Ronsse et al., *Biomass Conversion and Biorefinery*, 2020 |
| Plastic-derived char | 20--32 | Higher carbon retention from incomplete polymer conversion | Malinowski et al., *Waste-Derived Chars: A Comprehensive Review*, 2023 |
| Carbon black (reference) | ~32 | Industrial benchmark for near-pure carbon residue | Standard reference |

Conservative estimates used in the financial model (Annex 5 §13):

| Char source | CV estimate (MJ/kg) | Confidence | Rationale |
|-------------|---------------------|------------|-----------|
| Organic/cellulose char | **15** | MEDIUM | Mid-range for MSW biomass char; conservative vs clean biomass (20+ MJ/kg) |
| Plastic char | **25** | MEDIUM | High carbon content from incomplete polymer conversion |
| Weighted average (combustible fraction) | **15.6** | MEDIUM | Calculated: (452.2 × 15 + 28.6 × 25) / (452.2 + 28.6) |

**UR-specific measurement:** One laboratory measurement on UR-produced char exists, and it sits at the top of the literature range:

| Sample | CV | Method | Lab |
|--------|-----|--------|-----|
| Urethane-derived char | **32.09 MJ/kg** | JIS M 8814 bomb calorimeter | Isumi Tech Co., Ltd. (Report R35-339439) |

This result — 32.09 MJ/kg on a single polymer feedstock — is notably higher than the 20--32 MJ/kg literature range for plastic char from conventional pyrolysis. While the single test is on a clean polymer (urethane, not MSW), the elevated value is consistent with a hypothesis that the Urban Rig's superheated-steam process may produce higher-energy char than conventional pyrolysis. The steam environment suppresses secondary cracking of the char matrix and may preserve more fixed carbon, resulting in a product closer to carbon black than to typical pyrolysis char. This hypothesis remains unproven and requires validation by bomb calorimetry on UR-produced MSW char across multiple feedstock compositions.

[!] **MSW-derived char CV has NOT been measured on the UR.** The financial model uses conservative literature-based estimates (15 MJ/kg organic, 25 MJ/kg plastic). These values are important for assessing the commercial viability and energy content of char as a marketable fuel product. Bomb calorimetry validation on UR-produced MSW char is recommended to support char sale quality assurance and pricing.

---

## 2.5 Off-Gas Composition and Energy

### 2.5.1 Qualitative Composition (GC Analysis)

A gas chromatography analysis was performed on an off-gas sample collected from the UR batch unit (report B2002600, 2020-12-05, Asada Shokai facility). The combustible species identified are:

| Combustible Component | Detected |
|----------------------|----------|
| Hydrogen (H$_2$) | Yes |
| Methane (CH$_4$) | Yes |
| Ethane (C$_2$H$_6$) | Yes |
| Ethylene (C$_2$H$_4$) | Yes |
| Propane (C$_3$H$_8$) | Yes |
| Propylene (C$_3$H$_6$) | Yes |
| Carbon monoxide (CO) | Yes |

*Source: GC analysis report B2002600, 2020-12-05, Asada Shokai facility.*

The sample also contained N$_2$ (~66%) and O$_2$ (~12%), most likely from the carrier gas and/or air ingress during sampling. Quantitative proportions cannot be used directly for volumetric LHV calculation. The qualitative composition confirms a typical pyrolysis gas mixture — combustible in a dedicated burner system. The presence of hydrogen provides reliable ignition and flame stability.

### 2.5.2 Off-Gas Calorific Value (Constant Factor)

Both 3P energy balance tests yield an identical off-gas energy factor (Asada Shokai test report, p. 35):

| Test | Off-gas mass | Off-gas energy | Energy per kg |
|------|-------------|---------------|--------------|
| 2022-05-26 (3P pellets) | 11.7 kg | 15,489 kcal | **1,324 kcal/kg** |
| 2022-07-11 (3P offcuts) | 1.3 kg | 1,721 kcal | **1,324 kcal/kg** |

**1,324 kcal/kg = 5.54 MJ/kg off-gas** [FACT]

This was confirmed as constant across all four feedstock types tested: 3P pellets, 3P molded, container recycling (MSW), and non-combustible residue — all returned 1,324 kcal/kg (Asada Shokai energy balance tables, pp. 35--36).

**Methodological note:** The identical value across all tests indicates this is a calorific factor applied to the mass balance, rather than an independent per-batch measurement. The same approach was used for oil (10,980 kcal/kg = 45.9 MJ/kg) and residue (5,880 kcal/kg = 24.6 MJ/kg). Cross-validation: independent lab analysis of oil from the same test campaign gave 46,000 J/g for container plastic oil and 45,000 J/g for non-combustible residue oil — consistent with the energy balance factor (Asada Shokai test report, Section 10).

### 2.5.3 Off-Gas Energy per kg of Feedstock

**From plastic feedstock (measured):**

| Parameter | Value | Source |
|-----------|-------|--------|
| Weighted off-gas yield (MSW polymer mix) | 19.3% of plastic input | Financial model cell J1: SUMPRODUCT of polymer mix × off-gas yields |
| Off-gas CV (steam-diluted) | 5.54 MJ/kg | Asada Shokai energy balance (constant across all feedstocks) |
| **Off-gas energy per kg plastic** | **1.069 MJ/kg** | 0.193 × 5.54 (financial model cell J3) |

*Note: A simplified PE/PP-only calculation gives 1.27 MJ/kg (23% off-gas × 5.54), but this overstates off-gas by 19% because it ignores the 10.3% residue from PET, PS, and PVC in the MSW mix. The weighted 1.069 MJ/kg is the correct figure for MSW modelling.*

**From organic/cellulose feedstock (literature estimate):**

| Parameter | Value | Source |
|-----------|-------|--------|
| Estimated off-gas CV (steam-diluted) | ~2.0 MJ/kg off-gas | HYPOTHESIS — lower than plastic off-gas due to high CO$_2$ and H$_2$O content |
| Off-gas mass yield | ~20% of organic input | Bridgwater, 2012; Chen et al., 2014 |
| **Off-gas energy per kg organic** | **~0.5 MJ/kg** | Conservative central estimate (range: 0.3--0.8 MJ/kg) |

*Sources for organic off-gas energy range: Bridgwater, Biomass and Bioenergy, 2012; Chen et al., Waste Management, 2014; PMC 9936530 (review of pyrolysis gas CV: 3--12 MJ/Nm$^3$ for biomass); PMC 11044251 (HHV of non-condensable gas: 14.56 MJ/m$^3$ at 600°C for clean biomass).*

[!] **The organic off-gas energy (0.5 MJ/kg) is a literature-based estimate. It has NOT been measured on the UR.** This parameter affects the total energy balance and off-gas contribution to operational understanding (see §2.6).

**Important correction log:** The original financial model contained an inverted parameter — organic off-gas energy was set at 5.0 MJ/kg instead of 0.5 MJ/kg, overstating organic off-gas by 10×. This was corrected in Session 9 based on literature review of 12 peer-reviewed sources. The correction inverts the self-sufficiency relationship: higher plastic content now **improves** (rather than hurts) off-gas coverage, which is physically correct — plastic pyrolysis produces energy-rich hydrocarbon gas while organic pyrolysis produces mostly CO$_2$ and water vapour.

---

## 2.6 Energy Balance

### 2.6.1 Plant Heating Demand

The URC-2000 manufacturer specification (UR2000-JP, p. 4; Lufthansa worksheet) specifies **10,000 litres/day** of light oil for the 200 T/day unit (140 T actual throughput at 0.7 T/m$^3$ density). Using the light oil energy density from test data (9,088 kcal/L = 38.0 MJ/L):

**Reference heating demand: 10,000 L × 38.0 MJ/L = 380,000 MJ/day (~4.4 MW continuous)**

**Thermodynamic cross-check:**

| Component | Estimate |
|-----------|---------|
| Sensible heat (140 T/day, 20°C → 600°C, $c_p$ ≈ 1.5 kJ/kg·K) | ~122,000 MJ/day |
| Latent heat for moisture evaporation (~20% moisture) | ~67,000 MJ/day |
| Endothermic pyrolysis reactions | ~2,000 MJ/day |
| Heat losses (insulation, radiation, ~25%) | ~48,000 MJ/day |
| **Thermodynamic minimum** | **~239,000 MJ/day (~2.8 MW)** |

The manufacturer figure (380,000 MJ) is ~60% above the thermodynamic minimum — plausible given real-world burner efficiency, heat distribution losses, and safety margins. **The manufacturer figure is used as the reference demand** because it comes from the equipment specification (UR2000-JP, p. 4).

[!] **The 380,000 MJ/day heating demand is a manufacturer specification for continuous operation. It has NOT been independently verified** by a third-party audit of an operating continuous UR installation. In the V2 model, this heating demand is met entirely by purchased heating oil (10,000 L/day), with all char produced allocated to commercial sale.

### 2.6.2 Off-Gas Coverage by Plastic Content

Using measured off-gas energy (1.069 MJ/kg plastic) and literature-estimated organic off-gas (0.5 MJ/kg organic), with 15% inorganic fraction removed before processing:

| Plastic % | Organic % | Off-gas (MJ/day) | Coverage | External fuel needed |
|-----------|-----------|------------------|----------|---------------------|
| 10% | 75% | 67,469 | 17.8% | Yes |
| 15% (France MSW) | 70% | 71,454 | 18.8% | Yes |
| 20% | 65% | 75,438 | 19.9% | Yes |
| 30% (model default) | 55% | 83,407 | 22.0% | Yes |
| 50% (industrial) | 35% | 99,345 | 26.1% | Yes |
| 100% (pure plastic) | 0% | 149,691 | 39.4% | Yes |

*Source: UR-Financial-Model-General.xlsx, Energy Scenarios sheet (corrected). Off-gas CV from Asada Shokai test data pp. 35--36; organic off-gas from pyrolysis literature (0.3--0.8 MJ/kg range; Bridgwater 2012, Chen et al. 2014). Inorganic fraction: 15% (glass, metals, ash — removed before reactor).*

**Key finding: off-gas alone never covers the full heating demand.** Even at 100% plastic, off-gas provides only 39% of the energy needed. At typical French MSW (15--20% plastic), coverage is approximately 19--20%.

### 2.6.3 Energy Balance: Off-Gas and Char Energy Potential

While off-gas alone is insufficient to meet the full heating demand, the **char by-product** from the organic and cellulose fractions represents a significant energy-rich commercial product. Per 1,000 kg of OMR entering the reactor, the process produces 480.8 kg of combustible char with a weighted calorific value of 15.6 MJ/kg (§2.4.3). Scaled to the 140 T/day operational throughput:

| Energy source | MJ/day | Energy content |
|---------------|--------|-----------------|
| Off-gas (plastic + organic) | 90,407 | 23.8% of heating demand |
| Char energy potential | 1,049,720 | 276.3% of heating demand |
| **Total energy in by-products** | **1,140,127** | **~300% of heating demand** |
| **Plant heating demand (purchased oil)** | **379,960** | 100% (external fuel supplied) |

*Source: Off-gas from UR-Financial-Model-General.xlsx Energy Scenarios sheet; char energy from Annex 5 §13.3 (480.8 kg/T × 15.6 MJ/kg × 140 T/day). Char CV: 15 MJ/kg organic/cellulose char, 25 MJ/kg plastic char (HYPOTHESIS — see §2.4.3).*

**V2 Operating Model:** In the current V2 operating model, all reactor heating is provided by purchased heating oil, and all char produced is sold on the commercial fuel market. The energy balance demonstrates that the char and off-gas contain significant energy content relative to the system's heating requirement, which supports the commercial viability of char as a premium fuel product:

| Parameter | Value |
|-----------|-------|
| Total char produced (combustible) | 67,312 kg/day (67.3 T/day) |
| **Char available for sale** | **~67.3 T/day (~22,095 T/year)** |
| Char energy content | 1,049,720 MJ/day |
| Off-gas energy contribution | 90,407 MJ/day |
| Plant heating supply | Purchased heating oil (10,000 L/day) |

*Source: Annex 5 §13.3; V2 operating model (March 2026).*

**Energy Content Implications:** Even under conservative char CV assumptions (10 MJ/kg instead of 15 MJ/kg), the char produced maintains substantial energy value — approximately 180% of the plant heating demand — confirming robust commercial potential. Bomb calorimetry validation on UR-produced MSW char is recommended to support market positioning and pricing strategies.

### 2.6.4 Sensitivity to Organic Off-Gas Energy Assumption

The off-gas coverage figures are moderately sensitive to the organic off-gas energy estimate. However, because off-gas provides only ~24% of the total heating demand regardless of this assumption, and because all operational heating is supplied by purchased oil in the V2 model, the sensitivity affects primarily the understanding of total energy balance and the assessment of off-gas energy recovery potential:

| Organic off-gas energy | Off-gas energy recovery | Share of total by-product energy |
|------------------------|-------------------------|--------------------------------|
| 0.3 MJ/kg (pessimistic) | ~80,500 MJ/day | 7.1% |
| 0.5 MJ/kg (central) | ~90,400 MJ/day | 7.9% |
| 0.8 MJ/kg (optimistic) | ~110,300 MJ/day | 9.6% |

Across the full literature range (0.3–0.8 MJ/kg organic off-gas), the total char availability for commercial sale remains stable at approximately 67.3 T/day. The organic off-gas energy estimate affects the relative proportions of off-gas and char energy contributions to the overall energy balance, but does not affect the V2 operating model where all char is marketed and reactor heating is sourced externally.

---

## 2.7 Exhaust Gas Emissions — Independent Laboratory Results

### 2.7.1 Air Emissions

Analysed by KANSO Technos, report 20002610, dated 2020-12-05. Samples collected 2020-11-25 at the Asada Shokai test facility (Noda, Japan).

| Pollutant | UR Measured | Analysis Method | French Incineration Limit | Factor Below Limit |
|-----------|-----------|-----------------|--------------------------|-------------------|
| Hydrogen chloride (HCl) | **< 1 ppm** | JIS K 0107 (2012) | 10 mg/m$^3$ (~7 ppm) | >7× |
| Sulfur oxides (SOx) | **< 1 ppm** | JIS K 0103 (2011) | 50 mg/m$^3$ | >50× |
| Nitrogen oxides (NOx) | **15 ppm** | JIS K 0104 (2011) | 200 mg/m$^3$ (~100 ppm) | >6× |
| Particulate matter | **< 0.002 g/m$^3$** | JIS Z 8808 (2013) | 10 mg/m$^3$ | >5× |

*Source: KANSO Technos Analysis Report 20002610. French incineration limits per Order of 20 September 2002 (Order of 20 September 2002).*

**Key result:** Emissions are 5--50× below French incineration standards across all measured pollutants. The anoxic process eliminates the chemical formation pathway for dioxins and furans entirely — they cannot form without oxygen (Urban Rig Recycling Solutions ENG, p. 14). This is fundamentally different from incineration where dioxins form during combustion and must be captured by expensive filter systems.

### 2.7.2 Odour Assessment

Analysed by Total Environment System Co., Ltd., Osaka, 2020-11-27. Method: Environmental Agency Notification No. 63 (1995-09-13).

| Measurement Point | Odour Index | Odour Concentration |
|-------------------|------------|-------------------|
| Emission source (exhaust) | 14 | 25 |
| North boundary | < 10 | < 10 |
| West boundary | < 10 | < 10 |

*Source: Total Environment System Co., Ltd. odour measurement report, 2020-11-27.*

Japanese odour regulations typically require < 15--20 at the emission source and < 10--12 at property boundaries. The UR meets these standards. French ICPE odour requirements should be compared during the permitting phase.

---

## 2.8 Batch-to-Continuous Scaling

The test data (§2.2) was collected on the batch unit. The URC-2000 production machine operates continuously. The manufacturer specifies the following scaling parameters:

| Parameter | Batch (per tonne, from tests) | Continuous (UR2000-JP / Lufthansa worksheet) | Ratio |
|-----------|------------------------------|---------------------------------------------|-------|
| Electricity | ~1,083 kWh/T | ~4.3 kWh/T (600 kW / 140 T/day) | ~250× less |
| Heating fuel | ~1,183 L/T | ~71.4 L/T (10,000 L / 140 T/day) | **~17× less** |
| Staffing | — | ~15 personnel for 200 T/day | — |

*Source: Asada Shokai batch test data vs UR2000-JP technical specification, p. 5; Lufthansa worksheet assumptions; Urban Rig Recycling Solutions ENG, p. 19.*

The 17× fuel efficiency improvement is explained by: (1) no reheat cycles — continuous reactor stays at 600°C, (2) better insulation at scale — heat loss scales as $r^2$ while throughput scales as $r^3$, (3) steady-state thermal equilibrium without temperature cycling losses, and (4) off-gas preheating of incoming feed in continuous mode.

[!] **The continuous-operation figures are manufacturer specifications. They have NOT been independently verified** by a third-party audit of an operating URC-2000 installation. The 17× improvement is physically plausible but the exact values require validation during commissioning.

---

## 2.9 Key Assumptions — Verification Status Summary

| # | Assumption | Value | Source | Status |
|---|-----------|-------|--------|--------|
| F1 | Oil yield from plastic (pure PE/PP/PS) | 70% (conservative) | Tested 71.8--82.3% (2 mixed tests, 9 individual tests) | **FACT** |
| F2 | Oil yield linearity with plastic % | Oil = plastic% × 70% | Scientific literature on superposition model (Buah et al., 2022: max ±8% deviation) | **HYPOTHESIS — supported by literature** |
| F3 | Biochar yield from organic matter | ~68--70% of organic input | Bridgwater, 2012; Chen et al., 2014 | **HYPOTHESIS — not tested on UR** |
| F4 | Oil density | 0.85 kg/L | Standard pyrolysis oil density | **REASONABLE** |
| F5 | Off-gas composition (qualitative) | H$_2$, CH$_4$, C$_2$--C$_3$ hydrocarbons, CO | GC analysis report B2002600, Asada Shokai facility | **FACT (qualitative)** |
| F6 | Off-gas mass by polymer type | PE 21%, PP 17%, PS 12% | Asada Shokai test data (9 individual tests) — mass balance | **FACT** |
| F7 | Off-gas CV (steam-diluted) | 5.54 MJ/kg | Asada Shokai energy balance tests (constant across all feedstocks) | **FACT** |
| F8 | Weighted off-gas rate (MSW plastic mix) | 19.3% of plastic input | Weighted from F6 + literature for PET/PVC | **DERIVED from FACT + HYPOTHESIS** |
| F9 | Off-gas energy from organic matter | ~0.5 MJ/kg organic input | Literature (range 0.3--0.8 MJ/kg; 12 peer-reviewed sources) | **HYPOTHESIS — critical, not tested on UR** |
| F10 | Plant heating demand (continuous) | 380,000 MJ/day | UR2000-JP specification, Lufthansa worksheet | **MANUFACTURER SPEC — not independently verified** |
| F11 | Char CV (organic/cellulose) | 15 MJ/kg | Mid-range literature (Fazil et al., 2021; Ronsse et al., 2020) | **HYPOTHESIS — not tested on UR** |
| F12 | Char CV (plastic) | 25 MJ/kg | Literature (Malinowski et al., 2023) | **HYPOTHESIS** |
| F13 | Exhaust emissions | < 1 ppm HCl, < 1 ppm SOx, 15 ppm NOx | KANSO Technos Report 20002610 | **FACT — accredited lab** |
| F14 | Oil CV | 43.27 MJ/kg | NKKK certified test report | **FACT — accredited lab** |
| F15 | Batch-to-continuous efficiency | ~17× fuel reduction | Manufacturer spec vs test data | **PLAUSIBLE — needs validation** |

**Summary:**

- **FACT** (lab/test data): F1, F5, F6, F7, F13, F14 — 6 of 15
- **DERIVED** (from verified + literature): F8 — 1 of 15
- **REASONABLE** (standard values): F4 — 1 of 15
- **HYPOTHESIS** (literature-based, not tested on UR): F2, F3, F9, F11, F12 — 5 of 15
- **MANUFACTURER SPEC** (not independently verified): F10, F15 — 2 of 15

### 2.9.1 Priority Validation Requests

The following data requests to Urban Rig / One World Corporation are recommended before commercial deployment:

1. **Off-gas flow rate and composition during continuous operation** — to validate the 5.54 MJ/kg constant at production scale and establish quantitative species proportions.
2. **Test data with non-plastic organic feedstock** (biomass, food waste, paper) — to validate the 0.5 MJ/kg organic off-gas estimate and the biochar yield assumptions.
3. **Bomb calorimetry on MSW-derived char** — to validate the 15 MJ/kg organic char and 25 MJ/kg plastic char assumptions that underpin the self-sufficiency claim.
4. **Validated energy balance for the continuous URC-2000** at different feedstock compositions — to confirm the 380,000 MJ/day heating demand and the 17× batch-to-continuous efficiency improvement.
5. **PET and PVC test runs on the UR** — to validate literature-estimated yields for the two most problematic polymer types in MSW.

---

## 2.10 Literature Sources for Off-Gas Energy Model

The off-gas energy relationship and correction (§2.5.3) is supported by 12 peer-reviewed sources:

1. ScienceDirect — "Pyrolysis gases produced from individual and mixed PE, PP, PS, PVC, and PET — Part I." PE off-gas at 86.6 MJ/m$^3$N.
2. PMC 9936530 — "A review on gasification and pyrolysis of waste plastics." Gas CV: 3--12 MJ/Nm$^3$.
3. PMC 11044251 — "Yield and Energy Modeling for Biochar and Bio-Oil Using Pyrolysis Temperature." HHV of non-condensable gas: 14.56 MJ/m$^3$ at 600°C.
4. Asada Shokai test data — Off-gas CV = 5.54 MJ/kg (steam-diluted). Energy balance tables, pp. 35--36.
5. Buah et al. (2022) — "Pyrolysis of mixed plastic waste: Predicting the product yields." Linear superposition model, max deviation 8 pp.
6. ScienceDirect — "Co-pyrolysis of waste plastic and solid biomass for synergistic production of biofuels." Plastic as hydrogen donor.
7. ScienceDirect — "Impact of plastic blends on the product yield from co-pyrolysis of lignin-rich materials." Synergy rates up to 7.78% at 500°C.
8. Nature Scientific Reports — "Co-pyrolysis of furniture wood with mixed plastics." Gas/solid yields change "almost linearly" with pine %.
9. ScienceDirect — "Co-pyrolysis and co-gasification of biomass and plastics." Blend ratio contributes 28% to gas yield model; temperature 33%.
10. ScienceDirect — "A review on municipal solid waste pyrolysis of different composition for gas production."
11. Frontiers — "Plastic regulates its co-pyrolysis process with biomass." Mass ratio is second most influential factor (28%).
12. EUBIA — "Pyrolysis" overview. Fast pyrolysis yields: ~65% liquid, ~10% gas, ~25% char; at >700°C up to 80% gas.

---

**End of Annex 2**
