# Annex 5. Municipal Solid Waste (France)

This annex describes residual household waste in France (ordures ménagères résiduelles, OMR): how much there is, what it contains, what the Urban Rig can and cannot convert, and what an Urban Rig could produce from one tonne of it. Part 1 covers what goes in; Part 2 covers what comes out. Plastic streams collected on their own are covered by Annex 8, mixed commercial waste by Annex 7 and the CDG airport by Annex 6.

## How to Read This Annex

OneWorld, the manufacturer of the Urban Rig, is the sponsor of this business plan [hyp:D-027]. Its documentation is marked "OneWorld design data"; these are the company's own figures and have not been verified independently.

Each figure or fact is followed by a small link. It opens the evidence sheet: what the evidence shows, its confidence, the source document and its location, or the calculation. Sheets numbered 5.x belong to this annex; sheets numbered 1.x, 2.x, 3.x and 8.x are those of Annexes 1, 2, 3 and 8. All sheets are listed in the index of evidence sheets.

**Composition data.** The composition comes from the national characterisation campaign of 2024 (MODECOM 2024), published by ADEME as open data and in a summary report. The full technical report is available only through a registration form and has not been read (request R-042).

**No Urban Rig test on household waste.** The Urban Rig has been tested on clean plastics and on two municipal plastic-rich streams, not on raw household waste (Annex 2). Part 2 therefore combines those tests, published literature and working assumptions. Each assumption is dated and named; the operator of the model can change it.

## Key Messages

- **Residual household waste is a large, steady stream.** France collected 14,752,013 t in 2024, 223.46 kg per inhabitant [RP2-004]. Ile-de-France collected 3.32 Mt in 2022, 268 kg per inhabitant, and sends 94 % of its residual waste to 18 incinerators [ORDIF-DMA-2022].
- **It is mostly wet organic matter.** Putrescibles make up 33.67 % of the mass [calc:CALC-A5-CAT01-PCT] and sanitary textiles, mainly paper tissues and nappies, 16.99 % [calc:CALC-A5-CAT06-PCT]. The average moisture is 42.1 % [ADEME-MODECOM-2024-HUM], about 421 kg of water per tonne [calc:CALC-A5-EAU-KG-T].
- **Plastics are 15.79 % of the mass** [calc:CALC-A5-CAT07-PCT], about 111 kg of dry plastic per tonne [calc:CALC-A5-SEC-PLAST-KG-T]. Their split by polymer is not published (request R-045).
- **11.79 % of the mass cannot be converted**: glass, metals, other minerals and hazardous items [calc:CALC-A5-NONPROC-PCT].
- **Oil comes from the plastic fraction.** On the working assumptions of this annex, one tonne of residual household waste gives 61 to 90 kg of oil, 81 kg in the central case [calc:CALC-A5-HUILE-BAS-KG-T] [calc:CALC-A5-HUILE-HAUT-KG-T] [calc:CALC-A5-HUILE-CENT-KG-T] [hyp:D-043] [hyp:D-044]. OneWorld design data state 5 % of oil for household waste with 10 % of resins [UR2000-JP-P05-BILAN].
- **Char is the main product.** The non-plastic organic fraction would give 91 to 146 kg of char per tonne, 109 kg in the central case [calc:CALC-A5-CHAR-BAS-KG-T] [calc:CALC-A5-CHAR-HAUT-KG-T] [calc:CALC-A5-CHAR-CENT-KG-T] [hyp:D-045].
- **Energy self-sufficiency is not established on this feed.** The gas from the plastic gives about 416 MJ per tonne [calc:CALC-A5-GAZ-PLAST-MJ-T], against 1,029 MJ only to evaporate the water [calc:CALC-A5-EAU-MJ-T] and 1,507 MJ of burner demand stated by OneWorld [calc:CALC-A2-BRULEUR-MJ-T]. The gap must be covered by burning part of the char or oil, or by purchased fuel [hyp:D-029].
- **Tests are the priority.** An Urban Rig test on French residual household waste, with measured moisture, gas and char, is the main request to OneWorld (R-021).

# Part 1. What Goes In

## 5.1 How Much Residual Household Waste

| Scope | Tonnage | Per inhabitant | Year | Evidence |
|---|---|---|---|---|
| France, residual household waste | 14,752,013 t | 223.46 kg | 2024 | [RP2-004] |
| Same, sum of the open data categories | 14,752,013 t | 223.54 kg | 2024 | [calc:CALC-A5-OMR-T] [ADEME-MODECOM-2024-DATA] |
| Ile-de-France | 3.32 Mt | 268 kg | 2022 | [ORDIF-DMA-2022] |

The national tonnages are extrapolated by ADEME from the 2023 collection survey [RP2-004]. The campaign characterised 95 samples of residual household waste in 50 municipalities, after 5 outliers were removed [RP2-004].

In Ile-de-France, 94 % of residual household and similar waste goes to 18 incinerators [ORDIF-DMA-2022]. The regional incinerators burned 3,810,761 t in 2022, 93 % of the technical capacity of their furnaces (Annex 8) [A8-CST-ORDIF-UIDND-2023].

## 5.2 Composition by Category

| Category (MODECOM 2024) | Tonnes, France | Share of mass | Evidence |
|---|---|---|---|
| Putrescibles (food and garden waste) | 4,966,318 | 33.67 % | [calc:CALC-A5-CAT01-T] [calc:CALC-A5-CAT01-PCT] |
| Sanitary textiles (tissues, nappies, hygiene) | 2,505,734 | 16.99 % | [calc:CALC-A5-CAT06-T] [calc:CALC-A5-CAT06-PCT] |
| Plastics | 2,329,258 | 15.79 % | [calc:CALC-A5-CAT07-T] [calc:CALC-A5-CAT07-PCT] |
| Cardboard | 973,969 | 6.60 % | [calc:CALC-A5-CAT03-T] [calc:CALC-A5-CAT03-PCT] |
| Paper | 854,481 | 5.79 % | [calc:CALC-A5-CAT02-T] [calc:CALC-A5-CAT02-PCT] |
| Glass | 739,213 | 5.01 % | [calc:CALC-A5-CAT09-T] [calc:CALC-A5-CAT09-PCT] |
| Textiles | 718,435 | 4.87 % | [calc:CALC-A5-CAT05-T] [calc:CALC-A5-CAT05-PCT] |
| Metals | 493,070 | 3.34 % | [calc:CALC-A5-CAT10-T] [calc:CALC-A5-CAT10-PCT] |
| Other minerals | 320,842 | 2.17 % | [calc:CALC-A5-CAT12-T] [calc:CALC-A5-CAT12-PCT] |
| Composites | 294,383 | 2.00 % | [calc:CALC-A5-CAT04-T] [calc:CALC-A5-CAT04-PCT] |
| Other organic matter (rubber, carpet, vacuum bags...) | 227,604 | 1.54 % | [calc:CALC-A5-CAT11-T] [calc:CALC-A5-CAT11-PCT] |
| Hazardous or specific waste | 186,789 | 1.27 % | [calc:CALC-A5-CAT13-T] [calc:CALC-A5-CAT13-PCT] |
| Wood | 141,917 | 0.96 % | [calc:CALC-A5-CAT08-T] [calc:CALC-A5-CAT08-PCT] |
| **Total** | **14,752,013** | **100 %** | [calc:CALC-A5-OMR-T] |

Each line is the sum of the sub-categories of the open data set [ADEME-MODECOM-2024-DATA]; the category names are those of the sorting grid [RP2-002].

**Fines.** The open composition data give no fines category for residual household waste [ADEME-MODECOM-2024-DATA], while the moisture data treat fines under 8 mm as a separate fraction of 5.4 % [ADEME-MODECOM-2024-HUM]. The summary report states that these fines are mostly putrescible waste [RP2-004]. How the fines were allocated to the categories above is not written in the data or in the summary; this annex uses the composition data for tonnages and the moisture data for the water balance [hyp:D-046].

**What changed since 2017.** Residual household waste fell from 252.7 to 223.5 kg per inhabitant between 2017 and 2024 [ADEME-CP-2025]. Its moisture rose from 36.9 % to 42.1 % [RP2-004].

## 5.3 Moisture and Calorific Value by Fraction

| Fraction | Share of mass | Moisture | Net calorific value, dry basis (J/g) |
|---|---|---|---|
| Garden waste | 3.0 % | 59.7 % | 16,606 |
| Other putrescibles | 26.3 % | 59.6 % | 16,975 |
| Paper | 5.7 % | 28.9 % | 14,398 |
| Cardboard | 6.6 % | 33.7 % | 15,635 |
| Composite packaging | 1.8 % | 28.3 % | 19,794 |
| Textiles | 4.9 % | 33.7 % | 18,466 |
| Sanitary textiles | 17.0 % | 60.0 % | 18,040 |
| Plastic films and bags | 8.6 % | 35.8 % | 27,808 |
| Other plastics | 7.0 % | 20.1 % | 25,616 |
| Wood (packaging / other) | 0.3 % / 0.7 % | 13.0 % / 26.0 % | 17,300 / 17,822 |
| Other organic matter | 1.4 % | 27.5 % | 16,781 |
| Glass | 4.7 % | 2.2 % | not analysed |
| Metals | 3.3 % | 13.2 % | not analysed |
| Other minerals | 2.0 % | 14.1 % | not analysed |
| Fines under 8 mm | 5.4 % | 46.3 % | 9,819 |
| **Residual household waste, average** | | **42.1 %** | **16.3 MJ/kg dry; 8.4 MJ/kg as received** |

Sources: shares and moisture [ADEME-MODECOM-2024-HUM]; calorific values [RP2-004], read on the table of the summary report.

Moisture was measured on 20 samples and the calorific value on 15 [RP2-004]. The average calorific value counts glass, metals, other minerals and hazardous waste at zero and is therefore slightly underestimated [RP2-004].

**Reading.** The plastic fractions of residual waste are not dry: 35.8 % moisture for films and 20.1 % for other plastics [ADEME-MODECOM-2024-HUM]. This is mostly water and food soiling stuck to the plastic. The calorific values show that the plastic fractions carry the most energy per dry kilogram, 27,808 and 25,616 J/g [RP2-004].

## 5.4 What the Urban Rig Cannot Convert

| Material | Share of mass | Evidence |
|---|---|---|
| Glass | 5.01 % | [calc:CALC-A5-CAT09-PCT] |
| Metals | 3.34 % | [calc:CALC-A5-CAT10-PCT] |
| Other minerals (rubble, ceramics, cat litter...) | 2.17 % | [calc:CALC-A5-CAT12-PCT] |
| Hazardous or specific waste (electronics, batteries, gas cartridges...) | 1.27 % | [calc:CALC-A5-CAT13-PCT] |
| **Total** | **11.79 %**, 1,739,914 t in France | [calc:CALC-A5-NONPROC-PCT] [calc:CALC-A5-NONPROC-T] |

Glass, metals and minerals pass through the reactor unchanged and leave with the solid residue. In the Chiba tests on municipal streams, the operator weighed "metals and foreign matter" separately after treatment: 27.8 % of the input for municipal packaging plastics [calc:CALC-A2-NONPLAST-NODA-0909]. The yields of this annex are therefore expressed per tonne received, with these materials included.

Hazardous items (batteries, gas cartridges, medicines) are a safety and permitting matter more than a yield matter. Whether they are removed before the reactor depends on the pre-sorting line chosen (Annex 9; request R-023).

## 5.5 Sanitary Textiles and Nappies

Sanitary textiles are the second category of residual waste, 16.99 % of its mass [calc:CALC-A5-CAT06-PCT]:

| Sub-category | Tonnes | Share of mass | Per inhabitant | Evidence |
|---|---|---|---|---|
| Soiled paper (tissues, kitchen paper, napkins) | 1,265,338 | 8.6 % | 19.2 kg | [ADEME-MODECOM-2024-DATA] [RP2-004] |
| Baby nappies | 859,734 | 5.8 % | 13.0 kg | [ADEME-MODECOM-2024-DATA] [RP2-004] |
| Other hygiene products (adult nappies, sanitary towels, wipes) | 380,662 | 2.6 % | 5.8 kg | [ADEME-MODECOM-2024-DATA] [RP2-004] |

Their moisture is 60.0 % [ADEME-MODECOM-2024-HUM]; their calorific value is 18,040 J/g on a dry basis [RP2-004].

**What a nappy is made of.** The only composition found is British and dates from 2006: a new nappy of 38.6 g holds 34.1 % fluff pulp, 32.4 % superabsorbent polymer, 16.6 % polypropylene, 6.0 % low-density polyethylene, 3.8 % adhesives, 2.2 % PET or polyester and 4.8 % other materials [A5-EA-2008-NAPPY-LCA]. PP, PE and PET together make 24.8 % of a new nappy [calc:CALC-A5-COUCHE-POLYMERES-PCT]. A recent European composition was not found (request R-046).

**Reading.** Nappies carry plastic that could produce oil, but it is mixed with cellulose, superabsorbent gel and, once used, a large weight of water. This plastic is not counted in the oil of this annex [hyp:D-043]. The superabsorbent polymer has no Urban Rig test (Annex 2; request R-021).

### 5.5.1 What Happens to a Nappy in the Reactor

No Urban Rig test exists on nappies (request R-021). Published work describes what each component does as the temperature rises. The URC-2000 heats its feed through zones at 150, 300, 450 and 600 °C, according to OneWorld design data [UR2000-JP-P08-SPEC].

| Temperature | What happens | Evidence |
|---|---|---|
| Up to about 230 °C | Water leaves. A used nappy is wet: sanitary textiles hold 60.0 % moisture in residual waste [ADEME-MODECOM-2024-HUM]; the superabsorbent itself loses its bound water, 14 % of its dry mass, below 360 °C [A5-MAHON-2020-SNAS-SAP] | [A5-GRABOWSKA-2013-PAANA] |
| About 230 to 550 °C | Cellulose (fluff pulp) and paper decompose; the main devolatilisation of household waste components lies between 230 and 550 °C [A5-BHATT-2026-RSCADV]. They give char, gas and a wet liquid (Section 5.10) | [A5-BHATT-2026-RSCADV] |
| From about 360 to 400 °C upwards | The superabsorbent (sodium polyacrylate) starts to break down: stable up to about 400 °C [A5-MCNEILL-1990-PAANA]; main losses between 360 and 592 °C [A5-MAHON-2020-SNAS-SAP]. It releases water, CO2, CO and methane between 300 and 500 °C [A5-GRABOWSKA-2013-PAANA] | |
| About 400 to 500 °C | Polypropylene and polyethylene (topsheet, backsheet) crack into oil and gas, as in the Chiba tests (Annex 2) | [CHIBA-ESSAIS-FICHES] |
| End | A carbon-rich residue remains. For a sodium polyacrylate binder, the residue at 1,000 °C was 11.3 %, mostly carbon, and sodium carbonate formed during the decomposition [A5-GRABOWSKA-2013-PAANA]; pure sodium polyacrylate kept 40 % of its mass at 800 °C [A5-MAHON-2020-SNAS-SAP] | |

**Results on whole nappies.**
- Microwave pyrolysis of used baby nappies gave up to 43 % oil, 29 % gas and 28 % char by mass (abstract only) [A5-LAM-2019-CHEMOSPHERE-DIAPER].
- Pyrolysis of nappies taken from the rejects of household waste plants maximised hydrogen and methane at 575 °C, up to 23 mmol of non-condensable gas per gram; at 525 °C, over 63 % of the liquid had boiling points close to heavy naphtha; the char had a low surface area, 9.7 m2/g (abstract only) [A5-CALERO-2025-CEJ-DIAPER].
- New shredded nappies held 7.5 % ash and 3.9 % fixed carbon; the cellulosic fraction of used, sterilised nappies 10.7 % ash and 1.2 % fixed carbon [A5-MALSEGNA-2021-ENERGIES-AHP].

**Sodium is the operational risk.** The superabsorbent brings 2 to 3 % sodium by mass into new nappies [A5-MALSEGNA-2021-ENERGIES-AHP]. With silicon and other minerals, sodium forms low-melting ashes between 500 and 800 °C; the authors observed agglomeration of their reactor bed [A5-MALSEGNA-2021-ENERGIES-AHP]. In an Urban Rig, this sodium would end in the char and could cause sticky deposits; it also lowers the value of the char as a fuel. This is to be checked in the OneWorld test (R-021).

**Reading.** A nappy is not mainly an oil feed: its cellulose and superabsorbent give char, water and gas, and its PP and PE a modest amount of oil. Pyrolysis destroys the superabsorbent; recovering it as a material requires separation before any thermal treatment, which is outside the Urban Rig process.

## 5.6 Textiles, Composites, Other Organic Matter and Fines

- **Textiles**, 4.87 % [calc:CALC-A5-CAT05-PCT]: mainly clothing, 443,844 t [ADEME-MODECOM-2024-DATA]. Their split between cotton and synthetic fibres in residual waste was not found (request R-046).
- **Composites**, 2.00 % [calc:CALC-A5-CAT04-PCT]: plastic-majority packaging such as coffee bags and crisp packets, 131,937 t; beverage cartons, 78,114 t; paper-majority composites, 64,087 t [ADEME-MODECOM-2024-DATA].
- **Other organic matter**, 1.54 %, 227,604 t: rubber, vacuum cleaner bags, carpet offcuts, cushions, tyres [calc:CALC-A5-CAT11-PCT] [ADEME-MODECOM-2024-DATA] [RP2-002].
- **Fines under 8 mm**, 5.4 % in the moisture data, mostly putrescible [ADEME-MODECOM-2024-HUM] [RP2-004]; dry calorific value 9,819 J/g [RP2-004].

## 5.7 Plastics in Residual Household Waste

| Plastic type | Tonnes, France | Evidence |
|---|---|---|
| Bin bags, other bags, packaging films | 1,281,445 | [calc:CALC-A5-PLAST-SOUPLES-T] |
| Rigid and other plastics | 1,047,813 | [calc:CALC-A5-PLAST-RIGIDES-T] |
| of which: tubs, trays, pots and cups | 443,885 | [ADEME-MODECOM-2024-DATA] |
| of which: other plastics (pipes, utensils, PVC panels, stretch films...) | 217,448 | [ADEME-MODECOM-2024-DATA] [RP2-002] |
| of which: PET bottles and flasks | 212,499 | [calc:CALC-A5-PLAST-PET-T] |
| of which: polyolefin bottles and flasks | 68,077 | [calc:CALC-A5-PLAST-PO-T] |
| **Total plastics** | **2,329,258** | [calc:CALC-A5-CAT07-T] |

**Polymers.** The MODECOM grid sorts plastics by use, not by polymer, except for PET bottles and polyolefin bottles [RP2-002]. The share of PE, PP, PS, PET and PVC in the plastics of residual household waste was not found (request R-045). Annex 8 describes the plastic streams that are collected separately.

**PVC and chlorine.** PVC appears in two sub-categories of the grid: other bottles and flasks, 5,461 t, and other plastics [ADEME-MODECOM-2024-DATA] [RP2-002]. Pure PVC is 56.7 % chlorine by mass [calc:CALC-A5-PVC-CL-MIN] [calc:CALC-A5-PVC-CL-MAX]. No chlorine analysis of residual household waste was found in the MODECOM summary (request R-045). The oil made from municipal streams at Chiba contained 0.137 % and 0.526 % chlorine (Annex 2) [CHIBA-JLOS-HUILES].

**Regulatory consequence.** Residual household waste is not among the waste codes from which pyrolysis oil can leave waste status in France [A3-ARRETE-SSD-HUILE-PYROLYSE-2024]. Oil made from it remains a waste-derived fuel (Annex 3).

## 5.8 One Tonne of Residual Household Waste

The table below converts the composition and moisture data into the mass of water, dry plastic, dry non-plastic organic matter and dry inert matter in one tonne received.

| Component | kg per tonne | Evidence |
|---|---|---|
| Water | 421 | [calc:CALC-A5-EAU-KG-T] |
| Dry plastic (films and other plastics) | 111 | [calc:CALC-A5-SEC-PLAST-KG-T] |
| Dry non-plastic organic matter (food, garden, paper, cardboard, composites, textiles, sanitary textiles, wood, other organics, fines) | 364 | [calc:CALC-A5-SEC-ORG-KG-T] |
| Dry inert matter (glass, metals, other minerals) | 92 | [calc:CALC-A5-SEC-INERTE-KG-T] |

The moisture data cover 98.8 % of the mass; hazardous waste has no moisture value [ADEME-MODECOM-2024-HUM]. The water figure matches the published average moisture of 42.1 % [ADEME-MODECOM-2024-HUM].

# Part 2. What Comes Out

## 5.9 Evidence on Urban Rig Equipment

**Clean plastics (Chiba, 2022).** Oil yields of 74 % to 81 % for PE, 73 % to 81 % for PP and 55 % to 73 % for PS [CHIBA-ESSAIS-FICHES]; 73.07 % on average over the 10 runs retained [calc:CALC-A2-HUILE10-MOY-POND] [hyp:D-034].

**Two municipal plastic-rich streams (Chiba, 2022).** Not raw household waste, but plastic packaging collected separately and the residue of non-combustible waste collection (Annex 2). Oil yields were 44.6 % and 50.4 % of the input after removal of metals and foreign matter [calc:CALC-A2-HUILE-NODA-0909-HORSMETAUX] [calc:CALC-A2-HUILE-NODA-0915-HORSMETAUX], and 32.2 % and 45.0 % of the raw input [calc:CALC-A2-HUILE-NODA-0909-BRUT] [calc:CALC-A2-HUILE-NODA-0915-BRUT]. The moisture of these feeds was not measured [CHIBA-ESSAIS-FICHES].

**OneWorld design data for household waste.** For household waste containing 10 % resins, OneWorld design data state 25 % char, 5 % oil and 5 % off-gas [UR2000-JP-P05-BILAN]. The same document states that food waste, leftovers, paper and wood are converted into a char that substitutes for coal [UR2000-JP-P05-BILAN]. About 60 % to 65 % of the input is not allocated in this balance; no measurement is attached [UR2000-JP-P05-BILAN].

## 5.10 Published Data for Materials Without Urban Rig Tests

Laboratory conditions differ from the Urban Rig (no superheated steam, smaller scale). These values give orders of magnitude, not design data.

| Material | Conditions | Oil or liquid | Gas | Char or solid | Evidence |
|---|---|---|---|---|---|
| Waste paper and textiles | Rotary kiln, 2 kg, 500 °C | 20 to 25 % | 45 to 48 % | 28 to 32 % | [A5-BHATT-2026-RSCADV] |
| Mixed plastics (LDPE, PP), same study | Same | 40 to 45 % | not stated | 5 to 7 % | [A5-BHATT-2026-RSCADV] |
| Food waste (simulated) | Laboratory, 500 °C | not measured | not measured | 28.45 % | [A5-KHAN-2022-POLYMERS-FOOD] |
| PET | Laboratory fast pyrolysis, 450 and 600 °C | waxes about 59.50 and 67.70 % | about 20 % | | [A5-JIA-2020-POLYMERS-PET] |
| Food waste | Fixed bed, 800 °C | 46 % | ~29 % | ~25 % | [A5-CZAJCZYNSKA-2017-REVIEW], secondary |
| Softwood / hardwood | Vacuum, 500 °C | 45.0 / 55.9 % | 24.7 / 19.9 % | 27.6 / 26.2 % | [A5-CZAJCZYNSKA-2017-REVIEW], secondary |
| Paper | Batch, 600 °C | ~19 % | ~41 % | ~40 % | [A5-CZAJCZYNSKA-2017-REVIEW], secondary |
| Cotton textile waste | Fixed bed, 450 °C | 14.00 % | 60.35 % | 25.26 % | [A5-CZAJCZYNSKA-2017-REVIEW], secondary |
| Mixed municipal solid waste | Slow pyrolysis, 550 °C | 48.0 % | 34.0 % | 18.0 % | [A5-CZAJCZYNSKA-2017-REVIEW], secondary |

**Reading.**
- **Biomass gives char and a wet, oxygenated liquid.** The liquid from paper held 8.01 % water, against 1.22 % for plastics [A5-BHATT-2026-RSCADV]. This liquid is not the hydrocarbon oil of the Chiba tests.
- **PET gives mostly waxes** (benzoic and terephthalic acids) rather than oil [A5-JIA-2020-POLYMERS-PET]; PET bottles are a small part of residual waste, 212,499 t [calc:CALC-A5-PLAST-PET-T].
- **Plastics leave almost no fixed carbon**: 0 % for PE and PP, 0.2 % for PS, 4.5 % to 4.8 % for PVC [A5-SORUM-2001-SINTEF].
- **Food waste char** at 500 °C had a gross calorific value of 5,864 kcal/kg [A5-KHAN-2022-POLYMERS-FOOD], i.e. 24.55 MJ/kg [calc:CALC-A5-KHAN-PCS-MJ-KG].

## 5.11 Indicative Mass Balance per Tonne

Working assumptions, dated and changeable by the operator:
- only the plastic category produces a saleable oil; plastic in nappies, composites and textiles is not counted [hyp:D-043];
- the oil and gas yields of plastic apply to its dry mass; oil at 55 %, 73.07 % or 81 % [hyp:D-044]; gas at 10 % of the plastic [hyp:D-029];
- char at 25 %, 30 % or 40 % of the dry non-plastic organic matter [hyp:D-045].

| Product, per tonne received | Low | Central | High | Evidence |
|---|---|---|---|---|
| Oil from the plastic fraction | 61 kg | 81 kg | 90 kg | [calc:CALC-A5-HUILE-BAS-KG-T] [calc:CALC-A5-HUILE-CENT-KG-T] [calc:CALC-A5-HUILE-HAUT-KG-T] |
| Gas from the plastic fraction | 11.1 kg | 11.1 kg | 11.1 kg | [calc:CALC-A5-GAZ-PLAST-KG-T] |
| Char from non-plastic organic matter | 91 kg | 109 kg | 146 kg | [calc:CALC-A5-CHAR-BAS-KG-T] [calc:CALC-A5-CHAR-CENT-KG-T] [calc:CALC-A5-CHAR-HAUT-KG-T] |
| Inert residue (glass, metals, minerals), dry | 92 kg | 92 kg | 92 kg | [calc:CALC-A5-SEC-INERTE-KG-T] |
| Water evaporated, then condensed | 421 kg | 421 kg | 421 kg | [calc:CALC-A5-EAU-KG-T] |
| Gas, water of reaction and liquid from non-plastic organic matter | balance, not known | | | INCONNU |

**Reading.**
- **Oil is a small share of the output.** The central case gives 81 kg of oil per tonne [calc:CALC-A5-HUILE-CENT-KG-T], against 5 % of oil in OneWorld design data for household waste with 10 % resins [UR2000-JP-P05-BILAN]. The French residual waste holds more plastic, 15.79 % [calc:CALC-A5-CAT07-PCT].
- **The low case is probably the more realistic one** until a test exists: the plastic of residual waste is dirty and mixed, and the municipal plastics of Chiba gave lower yields than clean plastics (Section 5.9).
- **The non-plastic organic matter is the unknown.** It is 364 kg of dry matter per tonne [calc:CALC-A5-SEC-ORG-KG-T]; how much of it becomes gas, liquid or char in the Urban Rig has not been measured (request R-021).

## 5.12 Energy Balance

| Item, per tonne received | MJ | Evidence |
|---|---|---|
| Energy in the gas from the plastic fraction, at 37.4 MJ/kg | 416 | [calc:CALC-A5-GAZ-PLAST-MJ-T] [hyp:D-038] |
| Heat to evaporate the water (latent heat only, 2.44 MJ/kg) | 1,029 | [calc:CALC-A5-EAU-MJ-T] [calc:CALC-A5-LATENT-MJ-KG] |
| Burner demand of the URC-2000 stated by OneWorld | 1,507 | [calc:CALC-A2-BRULEUR-MJ-T] |
| Energy in the central char, at 32.09 MJ/kg | 3,502 | [calc:CALC-A5-CHAR-MJ-T] [hyp:D-038] |

**Reading.**
- **The gas from the plastic does not cover the heat.** It covers 0.404 of the heat needed to evaporate the water [calc:CALC-A5-COUV-GAZ-EAU] and 0.276 of the burner demand stated by OneWorld [calc:CALC-A5-COUV-GAZ-BRULEUR]. Whether the evaporation is included in the burner demand is not stated by OneWorld.
- **The gas from the organic matter is not known.** Biomass pyrolysis gas is rich in carbon dioxide and its calorific value is lower than that of plastic gas; no measurement on an Urban Rig exists (request R-021).
- **The char could close the gap.** The central char carries 3,502 MJ per tonne [calc:CALC-A5-CHAR-MJ-T], more than the burner demand. Burning part of it would reduce the char sold. The value of 32.09 MJ/kg is the sponsor's assumption for household waste char [hyp:D-038]; a food waste char measured in the literature reached 24.55 MJ/kg [calc:CALC-A5-KHAN-PCS-MJ-KG]. The model must choose between burning char or oil and buying fuel (Section 5.17).
- **Consistent with Annex 2.** Self-sufficiency on household waste is not claimed [hyp:D-029].

## 5.13 Entry Price

The plant is paid to take residual household waste. The default entry price of the model is 100 EUR/t, changeable by the operator [hyp:D-039] [hyp:D-042]. For comparison (Annex 8):
- incineration cost an average of 120 EUR/t excluding VAT for private clients and 95 EUR/t for local authorities in 2023 [A8-PRIX-AMORCE-DT156-2023];
- the Syctom, the Paris area treatment authority, charges its members 109.4 EUR/t for residual household waste in 2026 [A8-CST-SYCTOM-BP-2026];
- the incineration tax is 16 or 29 EUR/t in 2026, depending on the energy performance of the plant [CIBS-TGAP-2026].

## 5.14 Conflicts Between Sources

- **Fines:** absent from the composition data, 5.4 % of the mass in the moisture data [ADEME-MODECOM-2024-DATA] [ADEME-MODECOM-2024-HUM]; the method of allocation is not written [hyp:D-046].
- **Per-inhabitant ratio:** 223.46 kg in the summary report [RP2-004], 223.54 kg as the sum of the open data [ADEME-MODECOM-2024-DATA].
- **Char of paper:** 28 to 32 % in the body of the article, 30 to 40 % in its abstract [A5-BHATT-2026-RSCADV].
- **Mixed plastics in the literature:** 40 to 45 % oil and 5 to 7 % char in the body of the article, 43 % oil and 16 % char in its abstract [A5-BHATT-2026-RSCADV]; the Chiba tests gave 73.07 % oil on clean plastics [calc:CALC-A2-HUILE10-MOY-POND].
- **Plastic pyrolysis in a review:** 65.2 % liquid in a table, 40.9 % liquid in the text, for the same reference [A5-CZAJCZYNSKA-2017-REVIEW].
- **Char energy:** 32.09 MJ/kg assumed for household waste char [hyp:D-038]; 24.55 MJ/kg measured on food waste char [calc:CALC-A5-KHAN-PCS-MJ-KG].

## 5.15 Data Quality Summary

| Item | Basis | Label |
|---|---|---|
| Tonnage and composition of residual household waste, France 2024 | ADEME open data and summary report | LU (open data previously cross-checked for plastics) |
| Moisture and calorific value by fraction | ADEME open data and summary report | LU |
| Composition of a nappy | British study, 2006 data, read on a mirror | LU, data older than eight years |
| Oil and gas of the plastic fraction | Chiba tests on clean plastics, applied to dry plastic | HYPOTHÈSE (D-043, D-044, D-029) |
| Char of the non-plastic organic matter | Literature | HYPOTHÈSE (D-045) |
| Gas and liquid of the non-plastic organic matter | None | INCONNU |
| Polymer split and chlorine of residual household waste | None | NON TROUVÉ (R-045) |
| Fibre composition of textiles in residual waste | None | NON TROUVÉ (R-046) |
| Energy balance on residual household waste | Calculation on the above | CALCULÉ, on assumptions |

## 5.16 Open Points

| Ref. | Subject | Held by |
|---|---|---|
| R-021 | Urban Rig test on French residual household waste: moisture, gas mass and calorific value, char, oil water and chlorine; separate tests on nappies (yields, sodium in the char, deposits) and food waste | OneWorld |
| R-023 | Pre-sorting line for household waste | OneWorld |
| R-042 | Full MODECOM 2024 technical report: allocation of fines, laboratory analyses | Project sponsor (ADEME registration form) |
| R-045 | Polymer split and chlorine of residual household waste | Not found in public sources |
| R-046 | Fibres of textiles in residual waste; recent nappy composition | Partly found |

## 5.17 Recommendations for the Business Plan

- Present residual household waste as a **paid feed with a modest oil yield**, not as an oil feed: per tonne received, the central case gives 81 kg of oil and 109 kg of char [calc:CALC-A5-HUILE-CENT-KG-T] [calc:CALC-A5-CHAR-CENT-KG-T].
- Use the **low oil case** by default until an Urban Rig test on French residual waste exists [hyp:D-044].
- Show the **energy balance with a purchased fuel or a char consumption line**, not as self-sufficient [hyp:D-029].
- Treat a **pre-sorting step** that recovers metals and removes hazardous items as part of the household waste configuration (Annex 9).

## 5.18 References

The full list of documents cited, with their location and confidence, is in the index of evidence sheets.
