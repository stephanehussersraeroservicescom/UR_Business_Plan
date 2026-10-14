# Assumption Verification Note

**Date:** 19 September 2026
**Scope:** Urban Rig energy and electricity assumptions, checked against the source documents in this repository.
**Method:** Every figure below is traced to a named document in this repository, or explicitly marked as coming from outside it.

---

## 1. Summary of findings

| # | Assumption | Value in model | Verified value | Source of the correction |
|---|---|---|---|---|
| 1 | Off-gas calorific value | 5.54 MJ/kg | **37 MJ/kg** (18.8 MJ/Nm3) | Calculated from GC report B2002600, this repository |
| 2 | Off-gas energy per kg of plastic | 1.07 MJ/kg | **6.5 MJ/kg** | Same, applied to the Ichimura off-gas yields |
| 3 | Off-gas energy per kg of organics | 0.5 MJ/kg | **1.5 to 2.0 MJ/kg** | **Outside this repository.** Published literature only. Not measured |
| 4 | Electricity | 600 kW continuous = 103 kWh/t | **15 to 20 kWh/t measured; 25 to 30 kWh/t recommended** | Ichimura operational data, TECHNICAL-REFERENCE-VALIDATED-DATA.md |
| 5 | Heat demand | 380,000 MJ/day | **200,000 to 320,000 MJ/day useful** | All-electric option, ANNEX-09 |
| 6 | Plastic to oil conversion | 69 to 77% | **Two contradictory figures in this repository.** See section 5 | Ichimura test tables vs TECHNICAL-REFERENCE-VALIDATED-DATA.md |

---

## 2. Off-gas calorific value: corrected from the repository's own lab report

The financial model uses 5.54 MJ/kg (1,324 kcal/kg), taken from the Ichimura energy balance. That figure is the calorific value of the **diluted sample**, not of the process gas.

Gas chromatography report B2002600 (KANSO Technos, 5 December 2020), as transcribed in `supporting-documents/TECHNICAL-REFERENCE-VALIDATED-DATA.md`:

| Component | % by volume |
|---|---:|
| Nitrogen (N2) | 65.8 |
| Oxygen (O2) | 12.3 |
| Hydrogen (H2) | 12.7 |
| Methane (CH4) | 3.2 |
| Carbon dioxide (CO2) | 1.7 |
| C2 to C3 hydrocarbons | ~1.5 |
| Carbon monoxide (CO) | 0.6 |
| Hydrogen sulphide (H2S) | < 0.5 ppm |

78.1% of the sample is nitrogen and oxygen, that is, carrier gas and air drawn in during sampling. Only about 19.7% is process gas.

**Calculation, per 100 mol of sample:**

| Component | mol | LHV (kJ/mol) | Energy (kJ) | Mass (g) |
|---|---:|---:|---:|---:|
| H2 | 12.7 | 241.8 | 3,071 | 25.4 |
| CH4 | 3.2 | 802.3 | 2,567 | 51.2 |
| C2-C3 (average) | 1.5 | ~1,650 | 2,475 | 54.0 |
| CO | 0.6 | 283.0 | 170 | 16.8 |
| CO2 | 1.7 | 0 | 0 | 74.8 |
| **Process gas total** | **19.7** | | **8,283** | **222.2** |
| N2 + O2 (diluent) | 78.1 | 0 | 0 | 2,236.0 |
| **Sample total** | **97.8** | | **8,283** | **2,458.2** |

- Calorific value of the **sample as taken**: 8,283 kJ / 2.458 kg = **3.4 MJ/kg**. This is the same order as the 5.54 MJ/kg used in the model, which confirms that the model's figure describes the diluted stream.
- Calorific value of the **process gas alone**: 8,283 kJ / 0.2222 kg = **37.3 MJ/kg**, or 8,283 kJ / 0.4415 Nm3 = **18.8 MJ/Nm3**.

For reference, natural gas is about 38 MJ/Nm3. The Urban Rig process gas is about half that per unit volume, which is normal for a steam carbonisation gas containing 1.7% CO2.

**The model therefore understates the off-gas energy by a factor of about 6.7.**

Note that this value is conservative. It counts the CO2 as ballast mass. On a pure polyolefin charge, which contains no oxygen, the gas cannot contain CO2 or CO, and the calorific value would be higher still.

### Applied to the test data

Ichimura energy balance test, 26 May 2022: 60 kg of PE/PP/PS in, 43.1 kg oil, 5.2 kg residue, 11.7 kg off-gas. Mass balance closes exactly.

- Energy booked in the report: 11.7 kg x 5.54 = 64.8 MJ
- Energy recalculated: 11.7 kg x 37.3 = **436 MJ**, i.e. 7.3 MJ per kg of plastic

Using the weighted off-gas yield for a French plastic mix, 17.3% (ANNEX-02, section C.1):

**Off-gas energy = 0.173 x 37.3 = 6.5 MJ per kg of plastic input.**

---

## 3. Off-gas from organic matter: this figure is NOT in the repository

This must be stated plainly, because it is the one number in the corrected energy balance that has no source in this repository.

| Value | Where it comes from |
|---|---|
| 0.5 MJ/kg | Financial model, Assumptions tab, cell J6, marked "was 5.0 (INVERTED), corrected to 0.5". No supporting document |
| 5.0 MJ/kg | Technical annex, sections C.3.3 and C.3.4. Marked in the annex's own assumption table as "CRITICAL ASSUMPTION, NOT VERIFIED" |
| **1.5 to 2.0 MJ/kg** | **Published literature, outside this repository.** See below |

The literature basis for 1.5 to 2.0 MJ/kg:

- Neves et al., Chalmers University, *Volatile gases from biomass pyrolysis under conditions relevant for fluidized bed gasifiers*: the lower heating value of the volatile gas is about **11 MJ/kg at 600 degrees C**, rising above 17 MJ/kg at 950 degrees C.
- RSC Sustainable Energy and Fuels, 2024, fixed bed pyrolysis of forest and agroforestry biomass at 350 to 550 degrees C: permanent gas yield of **0.17 to 0.41 kg per kg of dry biomass**, with a lower heating value of 5.4 to 9.7 MJ/Nm3.

Applied: 0.20 to 0.30 kg of gas per kg of dry organic matter, at 11 MJ/kg, gives 2.2 to 3.3 MJ per kg of **dry** organic matter. Municipal organic waste as received is roughly 35% moisture, which brings this down to **1.4 to 2.1 MJ per kg as received**.

**No Urban Rig test has ever been run on an organic, non-plastic charge.** The two mixed-waste tests of September 2022 were excluded from the analysis because the plastic fraction of the charge was not measured. Until such a test is run, this parameter remains an estimate borrowed from the literature.

---

## 4. Electricity: the 600 kW figure is installed load, not consumption

This is the second significant correction, and it also comes from within the repository.

Three figures exist:

| Figure | Value | Source |
|---|---|---|
| Electricity, URC-2000 | 600 kW continuous | UR2000-JP page 4, cited in ANNEX-09 section 9.1.2 |
| All-electric option | 56,800 kWh/day, replaces oil heating | Fuel/electricity specification sheet, cited in ANNEX-09 section 9.1.2 |
| Measured consumption | **15 to 20 kWh per tonne of waste** | Ichimura operational data, TECHNICAL-REFERENCE-VALIDATED-DATA.md section 2 |

These three are consistent once read correctly:

- **600 kW is the connected load** of the machine in its oil-fired configuration, that is, the power to be subscribed from the grid. It covers motors, conveyors, fans, condensers, chiller, controls and instrumentation. It is not the average draw.
- 600 kW continuous would be 14,400 kWh/day, or **103 kWh/t**. Ichimura's operational figure of 15 to 20 kWh/t corresponds to an average draw of 88 to 117 kW, that is, a load factor of 0.15 to 0.20. This is normal for a plant whose motors are intermittent.
- The **all-electric option at 56,800 kWh/day is an alternative configuration**, not an addition. It replaces the oil burner with electric heating. It should never be added to the 600 kW figure.

**There is therefore no double counting in the model between fuel and electricity.** The model correctly carries both oil and electricity, because they describe the oil-fired configuration. What the model gets wrong is the level: it applies the connected load as if it were continuous consumption.

**Recommended working value: 25 to 30 kWh/t**, between Ichimura's measured 15 to 20 and the model's 103, pending a metered reading over a full month. The capacity charge on the subscribed 600 kW should be carried separately, at roughly 15,000 to 20,000 euros per year for an HTA connection in France.

### Financial effect

| | Model as written | Corrected |
|---|---:|---:|
| Specific consumption | 103 kWh/t | 30 kWh/t |
| Annual consumption at 46,200 t | 4,752 MWh | 1,386 MWh |
| Energy cost | 988,796 euros | ~166,000 euros |
| Capacity charge | not carried | ~20,000 euros |
| **Total** | **988,796 euros** | **~186,000 euros** |

---

## 5. Heat demand: the all-electric figure gives an independent cross-check

The model takes 380,000 MJ/day, derived from the 10,000 L/day of light oil in the Lufthansa worksheet and the UR2000-JP sheet.

The all-electric option of 56,800 kWh/day equals **204,480 MJ/day**. Electric resistance heating transfers essentially all of that to the process. An oil burner transfers 80 to 85%.

- If the true useful heat requirement is 204,000 MJ/day, then 10,000 L/day of oil (380,000 MJ) delivers 304,000 to 323,000 MJ/day of useful heat, a margin of about 50%.
- The technical annex's own thermodynamic estimate is 239,000 MJ/day, which sits between the two.

**Conclusion: the useful heat requirement is most likely between 200,000 and 320,000 MJ/day, not 380,000.** The 10,000 L/day figure is a fuel input figure that includes burner losses, start-up and design margin.

### Resulting energy balance at 20% plastic

Basis: 140 t/day, 20% plastic (28,000 kg), 65% organics (91,000 kg), 15% inert.

| | MJ/day |
|---|---:|
| Off-gas from plastic: 28,000 x 6.5 | 182,000 |
| Off-gas from organics: 91,000 x 1.75 | 159,250 |
| **Total chemical energy available** | **341,250** |
| Useful heat delivered at 85% burner efficiency | 290,000 |

| Heat demand basis | Coverage |
|---|---:|
| 380,000 MJ/day (fuel input basis, model) | 90% |
| 260,000 MJ/day (central useful demand) | **112%** |
| 204,000 MJ/day (all-electric basis) | 142% |

**At 20% plastic the plant is at or above energy break-even in the central case.** The break-even plastic content is about 17 to 18%.

One consequence changes direction. In the model as written, more plastic worsened the energy balance because organic matter was assumed to give a richer gas. With the corrected values, plastic gas gives 6.5 MJ/kg against 1.75 MJ/kg for organics, so **more plastic improves the energy balance at the same time as it improves oil yield**. The threshold above which fuel must be purchased disappears.

No capital cost is added. The condensation train, the gas separation and filtration, and the burner are already part of the installed equipment. The gas is simply not currently reintroduced in continuous mode.

**Correction required to ANNEX-01 and ANNEX-02:** both still state that "a dedicated lean-gas or regenerative burner system would be required for continuous operation". That sentence describes equipment to be bought when it already exists, and any reader will infer a capital cost that is not there.

---

## 6. Contradiction to resolve: plastic to oil conversion

Two figures in this repository are irreconcilable, and both are attributed to Ichimura.

| Source | PE | PP | PS |
|---|---:|---:|---:|
| Ichimura test tables, ANNEX-02 section C.1, 9 individual runs with full mass balance | 77.4% | 77.9% | 62.9% |
| TECHNICAL-REFERENCE-VALIDATED-DATA.md section 2 | 92% | 95% | 90% |

The test tables are the stronger evidence: nine runs, each with input, oil, off-gas and residue, and the mass balance closes. The 90 to 95% figures carry no mass balance.

The polystyrene figure settles it. The test tables show PS producing 19 to 38% residue across three runs. A 90% oil yield is arithmetically impossible against that residue.

**Recommendation:** delete the 95 to 100% conversion table from TECHNICAL-REFERENCE-VALIDATED-DATA.md, or restate it clearly as a theoretical maximum rather than measured data. It currently sits under the heading "VALIDATED data from certified laboratory reports", which it is not.

A second item in the same document needs correcting. It states that 85% energy self-sufficiency is "VALIDATED" because the off-gas contains about 18% combustibles. That does not follow: the combustible share of a diluted sample says nothing about the share of the heat demand the gas can cover. The conclusion may well be right, as section 5 above shows, but the reasoning given does not support it.

---

## 7. Revised financial effect, Year 3

Applied to the financial model at Year 3 steady state, 46,200 t.

| Line | Model as written | Corrected | Change |
|---|---:|---:|---:|
| Revenue | 16,055,538 | 16,055,538 | 0 |
| Maintenance | 2,080,800 | 2,080,800 | 0 |
| Manpower | 1,248,480 | 1,248,480 | 0 |
| Electricity | 988,796 | 186,000 | -802,796 |
| External fuel | 1,046,450 | 0 | -1,046,450 |
| Contingency / other | 1,040,400 | 1,040,400 | 0 |
| **Total OPEX** | **6,404,926** | **4,555,680** | **-1,849,246** |
| OPEX per tonne | 138.6 | 98.6 | -40.0 |
| **EBITDA** | **9,650,612** | **11,499,858** | **+1,849,246** |
| EBITDA margin | 60.1% | 71.6% | +11.5 pts |
| Depreciation | -4,053,000 | -4,053,000 | 0 |
| Interest | -4,347,660 | -4,347,660 | 0 |
| Pre-tax result | 1,249,952 | 3,099,198 | +1,849,246 |
| Project payback | 6.6 years | about 5.7 years | -0.9 years |

Removing the diesel also removes about 6,739 tCO2 per year. This raises the net carbon figure the model uses for its carbon credit line, which should be recalculated.

---

## 8. What still needs to be measured

In order of importance.

1. **Gas chromatography with flow measurement on undiluted off-gas, plus bomb calorimetry.** The 37 MJ/kg above is calculated from a sample that was 78% air and nitrogen. The calculation is sound but it is a reconstruction. A clean measurement closes it definitively. One day of work.
2. **A pyrolysis run on an organic, non-plastic charge**, with gas flow and calorific value measured. This is the only parameter in the corrected energy balance with no source in this repository.
3. **A metered electricity reading over one month of continuous operation.** This settles the 15 to 103 kWh/t range.
4. **A heat input measurement in continuous operation**, to settle whether the requirement is 204,000 or 380,000 MJ/day.
5. **A run on real French municipal solid waste** with the plastic fraction measured before the run. This is still the largest open item in the whole file: every yield in the model rests on 120 kg of tests on pure PE, PP and PS.

---

## 9. Documents consulted

Read in full:

- `pour-finaliser/ANNEX-09-Equipment-Configuration.md`
- `supporting-documents/TECHNICAL-REFERENCE-VALIDATED-DATA.md`
- Project business plan (ODT export), technical annex sections A to G, and `URFinancialModelGeneral.xlsx`

Identified but not readable as text:

- `supporting-documents/more/consommation electrique et fuel.pdf` (scanned image, Canon scanner, January 2024). Its content appears to have been transcribed into ANNEX-09 section 9.1.2 and 9.1.4, which is what has been used here.
- `supporting-documents/more/gaschromatography.pdf`
- `supporting-documents/more/Analysis Results (Off-gas Odor Index Exhaust Gas).pdf`
- `supporting-documents/more/Copy of ichimura data 2.pdf`
- `pour-finaliser/UR-Financial-Model-Restructured-V3.xlsx`
- `supporting-documents/France  CDG/Copy of Worksheet for Lufthansa-200MT.xlsx`
- `supporting-documents/more/energy balance.xlsx`

---

**End of note**
