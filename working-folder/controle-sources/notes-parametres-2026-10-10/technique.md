# Urban Rig URC-2000: sourcing the technical parameters

Consulted on 2026-10-10. About 35 web searches were used out of the shared budget of 40, plus about 45 page reads.
Every quote below was read on the page named in its URL. Quotes are verbatim and shortened, because the reader tool limits quotes to about 120 characters.
Source IDs (`PRM-...`) refer to `technique.yaml` in this folder.
Any value marked **[computed]** is my arithmetic on sourced inputs. The formula is shown next to it.
Data older than 2015 is marked **[pre-2015]**.

---

## 1. rendement_bruleur: current value 0.85

**What it means in the model:** the share of the heat released by burning the pyrolysis gas that actually reaches the retort charge.

### Evidence

| ID | Equipment / conditions | Value | Quote (verbatim) | Location |
|---|---|---|---|---|
| PRM-HONUS-2014 **[pre-2015]** | Pilot screw pyrolysis reactor, indirectly heated by 5 gas burner sections. Crushed tyres at 30 kg/h, 500–650 °C, natural gas fuel | System thermal efficiency 53.5 / 55.5 / 54.9 / 51.6 % at 500 / 550 / 600 / 650 °C. Flue gas 303–396 °C | "ranging from about 52 % to 56 % has been estimated" (abstract, p. 317). "The heat for heating the reactor up is supplied by indirect heating from five gaseous burning sections" (p. 319). "303 °C, for the process temperature 500°C" (§4.2) | Abstract p. 317; Table 4 p. 326; §4.2 |
| PRM-HTRI-UKHTC-2024 | Refinery fired heater (radiant + convection), natural draft, no air preheater | Overall fuel efficiency 84.9 % at flue outlet 327.3 °C. 94.8 % with APH (111.3 °C). 90.88 % with APH and 40 % bypass (195.1 °C) | "Overall fuel efficiency, % 84.9 94.8 90.88". "Flue gas outlet temperature, °C 327.3 111.3 195.1" | Results table |
| PRM-UOP-US11802687-2023 | Refinery fired heaters without APH (patent statement) | ">90–92 %" for current designs | "The method provides greater than 90-92% efficiency typically achieved in current designs." | Description |
| PRM-DOE-STEAMTS4-2006 **[pre-2015]** | Combustion efficiency, natural gas (boiler tip sheet) | 9.5 % excess air: 85.4 / 83.1 / 80.8 / 78.4 / 76.0 % at ΔT (flue minus air) = 200 / 300 / 400 / 500 / 600 °F | "Assumes complete combustion with no water vapor in the combustion air." | Table, Steam Tip Sheet #4 |
| PRM-DOE-PHTS10-2006 **[pre-2015]** | Process furnace exhaust losses, 10 % excess air | Exhaust loss is 42 % of input at 1400 °F (760 °C), so available heat is about 58 %. Available heat is about 80 % at 400 °F (204 °C) | "At 1400°F, the heat content of the exhaust gases (at 10% excess air) is about 42% of the heat furnace input." "the available heat at the 400°F exhaust gas temperature is approximately 80%" | Process Heating Tip Sheet #10, example |
| PRM-QASIM-2025 | Rotary kiln, 150 kW pilot, propane-fired calcination (context only) | Energy transfer efficiency 45 % (propane). Flue gas loss 29 %, surface loss 38 % | "Energy transfer efficiency for calcination was quantified at 45% for propane and 60% for electrification." | Abstract |
| PRM-FEECO-2025 | Indirect- vs direct-fired rotary kilns (manufacturer, qualitative) | No figure | "Less energy-efficient due to indirect heat transfer." | Comparison table |

### Computations from sourced inputs

- **Honus 2014, 500 °C, flue-gas loss only:** 1 − 7.99 kW (burnt gases) / 40.20 kW (natural gas input) = **0.801** [computed].
- **Honus 2014, check on the reported system efficiency:** 1 − (7.99 + 10.70 wall losses) / 40.20 = **0.535** [computed]. This matches the reported 53.5 %, which confirms the paper's definition: efficiency = 1 − (flue + wall losses) / fuel input. Wall losses are 27 % of the input on this 30 kg/h pilot. They would be proportionally much smaller at 200 t/d, but no source quantifies them at that scale.
- **DOE PHTS #10, available heat interpolated linearly between the two published points** (400 °F → 80 %, 1400 °F → 58 %) [computed, approximate]. These are the flue-gas temperatures to expect when the gases leave a 450–550 °C retort jacket with no downstream heat recovery:
  - flue at 500 °C (932 °F) gives about 68 %
  - flue at 600 °C (1112 °F) gives about 64 %
  - flue at 700 °C (1292 °F) gives about 60 %

  The source curve is for natural gas. Pyrolysis gas contains CO2 and H2O, which lowers the available heat somewhat; this is not quantified here.

### Interpretation

- 0.85 is the value of a refinery-type fired heater whose convection section cools the flue gas to about 330 °C (HTRI 84.9 %).
- In the only source found on a burner-heated pyrolysis reactor (Honus), flue-only efficiency was 0.80 even with a 303 °C flue, and overall efficiency was 0.52–0.56.
- A retort heated to 450–550 °C cannot cool its own flue gas below the charge temperature. Without a recuperator, air preheater or waste-heat use credited to the process, the DOE curve gives 0.60–0.68.
- Basis caveat: the DOE combustion-efficiency table and the HTRI / API-style values may use different heating-value bases (HHV or LHV). I could not confirm the basis in the extracted text. This may explain why DOE gives 76 % and HTRI 85 % at similar ΔT. The model's PCI convention must match.

**Verdict:** outside the range for an unrecovered retort; 0.85 is plausible only with documented flue-gas heat recovery.
- Sourced range: 0.53–0.56 (pilot system), 0.60–0.68 (computed, no recovery), up to 0.80 (flue-only, 303 °C flue), 0.85–0.95 (refinery heaters with convection section or APH).
- Suggestion: keep 0.85 only if the URC-2000 design includes an air preheater or convection-type recovery bringing the flue to about 300 °C. Otherwise use about 0.65–0.80 and cite PRM-DOE-PHTS10-2006 and PRM-HONUS-2014.

---

## 2. criblage_char (0.85) and rec_metaux_char (0.80)

### 2a. Screening efficiency (criblage_char = 0.85)

| ID | Value | Quote | Location |
|---|---|---|---|
| PRM-TF-SCREENING-ND (book not identified, metadata missing) | 85–95 % considered reasonable | "Efficiencies between 85% and 95% are considered reasonable for both scales of screening." | Chapter b11059-12 |
| PRM-911MET-2016 | About 90 % typical, about 95 % maximum | "In practice it is impossible to reach 100% efficiency. Maximum efficiency is about 95%." "In most of the cases 90% is achieved" | Section "Efficiency" |

No char-specific screening efficiency was found. Char is friable and dusty, and no source covers that behaviour.
**Verdict:** confirmed. 0.85 is the low end of 0.85–0.95, so it is conservative. Both sources are secondary (an unidentified handbook chapter and a vendor guide). An equipment supplier's guarantee would be a better source.

### 2b. Metal recovery from char (rec_metaux_char = 0.80)

No study was found on recovering metals from **pyrolysis char**. The closest documented analogue is incineration bottom ash (IBA).

| ID | Context | Value | Quote / table | Location |
|---|---|---|---|---|
| PRM-ALLEGRINI-2015 | Danish state-of-the-art IBA treatment, 2013 | Recovery efficiency: Fe 85 %, NFe 61 %, Al 62 %, heavy NFe 43 %, stainless 85 %. Content in IBA (wet basis): Fe 7.2 %, NFe 2.2 %, Al 1.4 %, SS 0.29 % | Scenario C is labelled "Danish state of the art in 2013". Table 1 values are my transcription of the table, not prose | Table 1 p. 7; Table 3 p. 8 |
| PRM-ALLEGRINI-2015 | Future scenarios (NFe recovery down to 2 / 1 / 0.5 mm) | Al 68 / 70 / 72 %; scenario K: Al 97 %, Fe 95 % | Table 3 | p. 8 |
| PRM-KUCHTA-CEWEP-2016 | German IBA plants, average | Recovery rate 82 % (all metals), 84 % (iron), 74 % (NF). The "best" plants show >100 %, so the reference basis needs checking | "82%", "84 %", "74 %" (slide 17); Germany "82" (slide 18) | Slides 17–18 |
| PRM-GISBERTZ-2013 **[pre-2015]** | German IBA, NF metals | Less than 30 % of NF metals recovered; up to 90 % lost in the fines | "Up to now less than 30 wt.-% of the contained nf-metals are separated". "In established treatment facilities up to 90 % of nf-metals are lost in the fine fraction." | Abstract p. 1; §2 p. 2 |
| PRM-THESIS-MSWIBA-ND (author and year not shown) | Wet-screened IBA, lab and pilot | Fe recovery 87 % (+6.25 mm), 71 % (0.18–6.25 mm). NF recovery 85–90 % above 6.25 mm | Summary of abstract only (tool refused a full verbatim copy) | Abstract |

**[computed] Combined metal recovery** = Σ(content × recovery) / Σ content, using Allegrini Table 1:
- Fe + NFe: (7.2 × 0.85 + 2.2 × 0.61) / 9.4 = **0.794**
- Fe + NFe + SS: (… + 0.29 × 0.85) / 9.69 = **0.796**

**Verdict:** confirmed by analogy with IBA. The computed combined value is 0.79, and Kuchta reports an average of 0.82.

**Double-counting warning:** IBA plant-level recovery rates already include the screening steps. If the model multiplies criblage_char (0.85) × rec_metaux_char (0.80), the result is 0.68, which is below the IBA plant-level values. Check whether 0.80 should be applied after screening or instead of it.

**Assumption to confirm with a source:** char from 450–550 °C pyrolysis stays below the melting point of aluminium and is non-oxidising, so Al should be less oxidised than in IBA. No source quantifying this was found.

---

## 3. rec_ferreux (0.90), rec_alu (0.75), rec_verre (0.70): sorting of mixed MSW / MBT

| ID | Context | Fe | Al / NFe | Glass | Quote / location |
|---|---|---|---|---|---|
| PRM-MONTEJO-2013 **[pre-2015]** | 8 Spanish MBT plants. Recovered / input content, wet basis | 35–84 % (mean **61.3 %** [computed], median 59 %) | Al 33–95 % (mean **62.4 %** [computed], median 66.5 %) | 4.6–49 % (manual sorting; mean 13.1 % [computed]) | Table 3 caption: "Recovery efficiencies (percent in wet basis, kg ww recovered kg-1 ww input)" |
| PRM-ALLEGRINI-2015 | IBA, Denmark 2013 | 85 % | Al 62 % / NFe 61 % | — | Table 1, Table 3 |
| PRM-KUCHTA-CEWEP-2016 | IBA, Germany, average | 84 % | NF 74 % | — | Slide 17 |
| PRM-BIGANZOLI-2013 **[pre-2015]** | 2 Italian WtE plants: Al fed to the furnace and recovered as ingot | — | 21–23 % (up to 28–38 % with better recycling) | — | "Only 21–23 % can be recovered from the bottom ash and recycled as ingots." |
| PRM-STEINERT-ATMIN-2014 **[pre-2015]** | Manufacturer, high-speed ECS | — | +20–30 % extraction compared with a 2600 rpm ECS (relative gain, not an absolute rate) | — | "increasing its extraction rate by 20 to 30 %" |
| PRM-POLOMKA-2020 | Pilot glass line on MBT stabilizate (screen, air separator, LASER, optical sorter), Marszów, PL | — | — | **68.4 ± 7.0 %** (range 49.8–74.3 %); other MBTs 58.4 ± 14.2 % | "between 49.8% and 74.3% of the glass contained in it (68.4 ± 7.0% on average)" (§4) |
| PRM-ELRABAYA-2021 | Secondary citation of Damgacioglu et al. 2019 (MRF) | — | — | 70.16 % | "which allowed only 70.16% of the mixed glass to be recovered" |

**Verdicts:**
- **rec_ferreux 0.90: outside range (optimistic).** No plant-level source exceeds 85–87 %. Fe ranges from 84–85 % in IBA down to 35–84 % in MBT. I found no manufacturer datasheet with an equipment-level recovery percentage for overband magnets. Sourced value: 0.84–0.87 at best; 0.61 is the MBT mean.
- **rec_alu 0.75: confirmed, top of range.** It lies within the MBT range of 33–95 % and is close to the German IBA NF average of 74 %. It is above the Danish IBA Al value of 62 % and the MBT mean of 62 %. Lower values exist: Gisbertz below 30 %, Biganzoli 21–23 % of Al fed. 0.60–0.65 would be the central sourced value.
- **rec_verre 0.70: confirmed only with a dedicated optical glass-sorting line** (Połomka 68.4 % mean, 74.3 % max; Damgacioglu 70.16 % via Elrabaya). With manual sorting, MBT plants reach 4.6–49 %, so 0.70 would be outside that range.

---

## 4. part_organique_eau (0.05) and rdt_huile_recyclage (0.6)

No source was found on the aqueous phase from **mixed-MSW** or **plastic** pyrolysis. Analogous feedstocks:

| ID | Feedstock / conditions | Value | Quote | Location |
|---|---|---|---|---|
| PRM-PIMENTA-2023 | Wood vinegar, slow pyrolysis (eucalyptus) | Water 85–90 %; organic fraction 10–15 % | "Around 85%–90% of the product is water, and the remaining 15%–10% is an organic fraction" | §1 Introduction |
| PRM-GILLALAGUNA-2010 **[pre-2015]** | Sewage sludge, 530 °C, conventional condensers | Aqueous layer 77.38 / 76.95 wt % water, so ≤ 23 % non-water [computed: 100 − 77] | Table 3 values as read. Phase described as "organic compounds highly oxygenated and nitrogenated" | Table 3, §3.3.1 |
| PRM-SEYEDI-2019 | Biosolids, 800 °C | Sum of identified compounds 4.96 wt % (raw APL). COD > 200 g/L | "reduced the APL COD from >200 gCOD/L for non-catalyzed APL to 32 ± 1.2 gCOD/L" | Table 2, Table 3 |
| PRM-GILARDI-2026 | Aqueous phase from stabilisation of pyrolysis oil from biomass waste | Methanol + ethanol 2–8 wt %. Distillation recovers up to 95 % of the methanol and 98 % of the ethanol | "contains mainly water, but relevant amounts of methanol and ethanol (2-8 wt%)" | Abstract |
| PRM-PIMENTA-2023 | Vacuum distillation of wood vinegar | Residue about 3–4 % of initial volume | "the residual fractions remaining at the bottom of the distillation device reached values around 3%–4% of the initial volume of liquid" | §3 |

**Verdicts:**
- **part_organique_eau 0.05: no MSW-specific source found.** The biomass analogues give 10–15 % dissolved organics (wood vinegar) and up to about 23 % non-water (sludge). Sources that count only identified compounds give about 5 %. The sourced analogue range is 0.05–0.23. 0.05 sits at the low end.
- **rdt_huile_recyclage 0.6: no source found.** None of the sources read gives the fraction of aqueous-phase organics that can be recovered as an oil. They indicate that these organics are mostly water-soluble (acids, alcohols) and are recovered by distillation, not decantation (Gilardi, Pimenta). The parameter has no evidential basis as it stands.

---

## 5. rdt_char_organique: current 0.69, marked unverified

| ID | Feedstock / conditions | Char yield | Quote | Location |
|---|---|---|---|---|
| PRM-HWANG-2007 **[pre-2015]** | Japanese residential combustible waste (RC1–RC3), rotary kiln, 500 °C, 1 h, N2 | **24.0 / 21.1 / 30.1 wt %-dry** (RC1 / without food / without plastics). Non-combustibles 47.5 %. Bulky waste 30.4–45.0 % | "Char yield (wt %-dry) 24.0 21.1 30.1 47.5". Overall range: "The yield of char was in the range of 21-86% depending on the type of raw wastes." | Table 3; §3.1 |
| PRM-OJOLO-2005 **[pre-2015]** | Household MSW, 500–650 °C | Average 24.23 % (25.2 % in the conclusions; per-run values 24.8–25.9 % [computed]) | "the average yield of char produced during the pyrolysis of MSW expressed as a percentage of feedstock was 24.23%" | §3, Table 1 |
| PRM-BUAH-2016 | Combustible MSW fractions, 700 °C | 32.00 wt % | "Other pyrolysis products were 32.00 wt% char and 44.99 wt% oil." | Abstract |
| PRM-ASSUNCAO-2022 | Organic matter + paper fraction of household MSW, 400–475 °C | 35.29–45.75 wt % | "solid phase yields between 35.29 and 45.75% (wt.)" | Abstract |
| PRM-RAO-2026 | Non-recycled MSW paper fractions, slow pyrolysis (temperature not given in abstract) | 25.6–35.6 % | "Biochar yields ranged from 25.6 % to 35.6 %" | Abstract |

**Verdict:** outside range. The sourced range is 0.21–0.46 for organic or combustible MSW fractions at 400–700 °C. The central value at 450–600 °C is about 0.25–0.35. No source supports 0.69. Values close to it appear only for high-inert or non-combustible streams (Hwang: NC 47.5 %, up to 86 % "depending on the type of raw wastes"). If 0.69 is meant to include inert ash or glass, the parameter definition should say so explicitly.

---

## 6. pci_char (15 MJ/kg) and pci_residu_plastique (25 MJ/kg)

| ID | Material | Heating value | Quote | Location |
|---|---|---|---|---|
| PRM-HWANG-2007 **[pre-2015]** | Char from residential combustibles, 500 °C, ash 39–42 % | HHV-dry 15.80 / 15.07 / 15.23 MJ/kg (RC1 / RC2 / RC3) | "High heating value (kJ/kg-dry) ... 15,802 15,065 15,229" | Table 3 |
| PRM-RAO-2026 | Biochar from MSW paper fractions | Maximum 17.4 MJ/kg | "highest energy value of 17.4 MJ kg-1" | Abstract |
| PRM-SANTOS-2024 | Review of waste-derived chars | HHV 2.5–28.4 MJ/kg | "2.5–28.4 MJ/kg" | Abstract |
| PRM-OJOLO-2005 **[pre-2015]** | Literature range cited (Barner & Gerald 1983) | 25.52–30.16 MJ/kg | "The heating value of char generally was between 25.52MJ/kg and 30.16MJ/kg" | §3 |
| PRM-MARTINLARA-2021 | Char from post-consumer mixed plastics (PP 55.7 %, PS 18.7 %, film 25.7 %), fixed-bed semi-batch, 10 °C/min, 90 min | HHV (calculated from ultimate analysis, dry) **23.94 / 10.70 / 3.69 MJ/kg** at 450 / 500 / 550 °C. Ash 35.0 / 53.8 / 67.9 %. Char yield of the mixture 4.56 / 3.19 / 2.38 % | Table 4 values as read. "Solid product yield has clear tendency to decrease as the pyrolysis temperature increases." | Tables 3–4, §3.3.1 |

**Verdicts:**
- **pci_char 15 MJ/kg: confirmed**, as a dry-basis HHV of mixed-MSW char containing about 40 % ash (Hwang 15.1–15.8). Two caveats:
  - The model uses PCI (LHV). LHV is somewhat below HHV, and the gap was not quantified in a source read.
  - Removing metals and glass changes the ash content and therefore the heating value.
- **pci_residu_plastique 25 MJ/kg: outside range.** The only measured mixed-plastic char gives 23.9 MJ/kg at 450 °C, 10.7 at 500 °C and 3.7 at 550 °C. These are HHV values, so the LHV is lower still. The URC-2000 operates at 450–600 °C, so 25 MJ/kg is above every sourced value. A sourced value would be about 10.7 MJ/kg at 500 °C, at most about 24 MJ/kg at 450 °C. The residue mass is also small (2–5 % of plastic feed).

---

## Summary table

| Parameter | Current value | Sourced value / range | Source IDs | Verdict |
|---|---|---|---|---|
| rendement_bruleur | 0.85 | 0.53–0.56 (pilot pyrolysis reactor, system); 0.80 (same, flue-only, 303 °C flue) [computed]; 0.60–0.68 (no heat recovery, flue 500–700 °C) [computed]; 0.85 (fired heater, flue 327 °C); 0.91–0.95 (with APH) | PRM-HONUS-2014, PRM-DOE-PHTS10-2006, PRM-DOE-STEAMTS4-2006, PRM-HTRI-UKHTC-2024, PRM-UOP-US11802687-2023, PRM-QASIM-2025 | **Outside range** without documented flue heat recovery; plausible upper bound with APH or convection recovery |
| criblage_char | 0.85 | 0.85–0.95 (90 % typical) | PRM-TF-SCREENING-ND, PRM-911MET-2016 | **Confirmed** (low end; secondary sources; not char-specific) |
| rec_metaux_char | 0.80 | 0.79 [computed, IBA DK]; 0.82 (IBA DE average) | PRM-ALLEGRINI-2015, PRM-KUCHTA-CEWEP-2016, PRM-GISBERTZ-2013, PRM-THESIS-MSWIBA-ND | **Confirmed** by IBA analogy. Check double counting with criblage_char |
| rec_ferreux | 0.90 | 0.84–0.87 (IBA best); 0.35–0.84, mean 0.61 (MBT) | PRM-ALLEGRINI-2015, PRM-KUCHTA-CEWEP-2016, PRM-MONTEJO-2013, PRM-THESIS-MSWIBA-ND | **Outside range** (optimistic) |
| rec_alu | 0.75 | 0.33–0.95, mean 0.62 (MBT); 0.62 (IBA DK); 0.74 (IBA DE NF); <0.30 (DE, Gisbertz); 0.21–0.23 (Al ingot, IT) | PRM-MONTEJO-2013, PRM-ALLEGRINI-2015, PRM-KUCHTA-CEWEP-2016, PRM-GISBERTZ-2013, PRM-BIGANZOLI-2013 | **Confirmed** (top of range; central about 0.62) |
| rec_verre | 0.70 | 0.684 ± 0.07 (max 0.743) optical line; 0.584 ± 0.142 (other MBT); 0.70 (MRF, secondary); 0.046–0.49 (manual MBT) | PRM-POLOMKA-2020, PRM-ELRABAYA-2021, PRM-MONTEJO-2013 | **Confirmed only with an optical glass line**; outside range otherwise |
| part_organique_eau | 0.05 | No MSW/plastic source. Analogues 0.05 (identified compounds) to 0.10–0.15 (wood vinegar) to ≤0.23 (sludge) | PRM-PIMENTA-2023, PRM-GILLALAGUNA-2010, PRM-SEYEDI-2019, PRM-GILARDI-2026 | **No source found** (MSW-specific); low end of analogues |
| rdt_huile_recyclage | 0.6 | None | (PRM-GILARDI-2026, PRM-PIMENTA-2023 context only) | **No source found** |
| rdt_char_organique | 0.69 | 0.21–0.46 (400–700 °C); about 0.25–0.35 central | PRM-HWANG-2007, PRM-OJOLO-2005, PRM-BUAH-2016, PRM-ASSUNCAO-2022, PRM-RAO-2026 | **Outside range** |
| pci_char | 15 MJ/kg | 15.1–15.8 MJ/kg HHV-dry (MSW char, about 40 % ash); 2.5–28.4 (review); max 17.4 (paper biochar) | PRM-HWANG-2007, PRM-SANTOS-2024, PRM-RAO-2026, PRM-OJOLO-2005 | **Confirmed** (HHV basis; LHV slightly lower) |
| pci_residu_plastique | 25 MJ/kg | 23.9 (450 °C), 10.7 (500 °C), 3.7 (550 °C) MJ/kg HHV | PRM-MARTINLARA-2021 | **Outside range** |

---

## Sources consulted but not retained (no usable figure)

- DOE, *Check Burner Air to Fuel Ratios*, Process Heating Tip Sheet #2 (2002 / 2007). Only gives available heat at 2400 °F (22 % / 29 %), which is not relevant.
- DOE, *Improving Process Heating System Performance: A Sourcebook*, 3rd ed. (2015). The text was truncated by the reader and no efficiency figure came back. It is worth reading manually.
- Yokogawa, *Fired Heaters in the Process Industries* (2023). Qualitative only.
- Šyc et al. 2020, J. Hazard. Mater. 393:122433. Only the abstract was readable; the BAM full text was blocked by a bot check. It is worth reading manually for IBA recovery by particle size.
- Neubert et al. 2017 (CEST). No figures.
- Holm & Simon 2017, Waste Manag. 59:229–236. BAM summary page only; no figures.
- Bin et al. 2023 (eddy current separator), TU Graz tech offer, Steinert IBA page, Eriez/Recycling Today 2024. Qualitative only.
- Świechowski et al. 2020, *Data* 5:48. Yields are in a supplementary xlsx that was not read.
- Bieniek et al. 2021 (E3S 323:00003). Woody and agricultural biomass, not MSW.
- Gracia-Monforte et al. 2026 (Energy Convers. Manag. 353:121154). Electrically heated pilot; assumes 5 % losses; gives no burner efficiency.
- Tursunov et al. 2025 (J. Ecol. Eng. 26(7)). No yields in the abstract.
- Gamboa et al. 2023 (Energies 16:7932). Abstract only: 30–50 % of the pyrolysis gas is burned for self-sufficiency, with no efficiency given.

## Recommended manual follow-up

1. Šyc et al. 2020 (full text) and Holm & Simon 2017: IBA recovery by particle size, to firm up rec_metaux_char, rec_ferreux and rec_alu.
2. The DOE Sourcebook 3rd ed. (2015), available-heat chart: replace the pre-2015 tip-sheet interpolation.
3. Świechowski 2020 supplementary xlsx: mass yield and HHV by MSW component at 300–500 °C.
4. A URC-2000 vendor guarantee or design data on flue-gas outlet temperature and heat recovery. This is the decisive input for rendement_bruleur.
