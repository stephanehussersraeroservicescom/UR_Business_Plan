# Annex 7 — Sector: Industrial Residues (France)

**Purpose:** Step-by-step derivation of expected pyrolysis product yields (oil, off-gas, residue) for sector-specific feedstock profile of French industrial/commercial waste (Commercial and Industrial Waste — DAE) sourced from the Île-de-France region, processed through the Urban Rig.

**Date:** March 2026
**Status:** DRAFT — Initial research compilation

---

## OBJECTIVE

To answer the question: **If we source waste from industrial and commercial activities in the Île-de-France region, what composition enters the Urban Rig, and what are the expected outputs?**

Industrial and commercial waste (DAE) in France represents a fundamentally different feedstock opportunity from municipal OMR (Annex 5) or airport waste (Annex 6). DAE is typically drier, more homogeneous within each source stream, and richer in packaging materials (plastic film, cardboard, wood pallets). It also has a more favourable regulatory context — DAE generators are already obligated under the "8-stream decree" (Décret 8 flux, Decree 2021-950) to sort paper/cardboard, metal, plastic, glass, wood, textiles, mineral fraction, and plaster, making pre-sorted residual streams readily available.

This annex follows the same Part 1 / Part 2 structure as Annexes 5 and 6. Every parameter is classified as: **FACT** (measured or from official sources), **HYPOTHESIS** (literature-based estimate), or **ASSUMPTION** (engineering judgment).

---

# PART 1 — WHAT GOES IN: Industrial & Commercial Waste Composition

*This part answers: of the DAE available in Île-de-France, what materials would enter the reactor, and in what proportions?*

---

## 1. INDUSTRIAL & COMMERCIAL WASTE IN ÎLE-DE-FRANCE — OVERVIEW

### 1.1 National Context

| Parameter | Value | Source |
|-----------|-------|--------|
| Total DAE produced in France | ~63 million T/year (excl. construction, mining) | ADEME Waste Key Figures 2024 (Chiffres-clés déchets 2024); Eurostat 2022 |
| Manufacturing non-hazardous waste | ~15 million T/year | INSEE Survey on Industrial Waste 2022 (Enquête déchets industrie 2022) |
| Tertiary sector non-hazardous waste | ~11 million T/year | INSEE Survey on Services Waste 2022 (Enquête déchets services 2022) |
| Total DAE to incineration or landfill | ~8–10 million T/year | ADEME 2024 estimate — residual after recycling |
| CSR (SRF) produced from DAE | 400,000 T/year (2022), capacity 1.2 MT | Senate response Q-2022-02293; ADEME |

[FACT] **FACT** — INSEE and ADEME figures from nationally representative surveys. Data quality: HIGH.

### 1.2 Île-de-France Regional Context

| Parameter | Value | Source |
|-----------|-------|--------|
| Total waste produced in IdF | ~36 million T/year | DRIEAT Île-de-France |
| IdF share of national commercial waste | ~21% | INSEE commercial waste survey 2016 |
| DAE landfilled in IdF (2022) | ~2.2 million T | ORDIF Landfill Notice 2022–2023 (Avis sur l'enfouissement ISDND 2022–2023) |
| DAE incinerated in IdF (2022) | ~3.5 million T (est.) | ORDIF Incineration Data 2022 |
| Warehouse/logistics floor area | 17 million m² | Institut Paris Région, Logistics Overview |
| Major logistics hubs | Garonor (75 ha), Gennevilliers (400 ha), Roissy-CDG cargo | Institut Paris Région |

[HYPOTHESIS] **ASSUMPTION** — IdF DAE tonnage is estimated from ORDIF landfill + incineration data plus recycled fraction. Not all DAE is tracked at regional level. MEDIUM confidence.

**Key insight for the Urban Rig:** Île-de-France generates an estimated 5–7 million tonnes per year of non-hazardous DAE (excluding construction). Of this, roughly 2–3 million tonnes are residual waste currently sent to incineration or landfill — representing a significant untapped feedstock pool. The proximity of major logistics hubs (Garonor, Roissy, Gennevilliers) to potential Urban Rig sites creates a natural supply chain.

---

## 2. DAE SOURCE STREAMS — SECTOR IDENTIFICATION

DAE waste comes from five distinct economic sectors, each with a different composition profile. We focus on sectors that generate residual waste suitable for pyrolysis (i.e., organic, cellulose, and plastic-rich streams):

| Stream | Description | Est. share of IdF DAE | Key materials |
|--------|------------|----------------------|---------------|
| **S1: Logistics & distribution** | Warehouses, distribution centres, e-commerce fulfilment | ~30% | Cardboard, plastic film (LDPE), wood pallets, strapping (PP/PET) |
| **S2: Retail & commerce** | Supermarkets, retail chains, shopping centres | ~25% | Cardboard, plastic packaging, food waste, film wrap |
| **S3: Food industry (Agri-food)** | Food processing, catering, wholesale markets (Rungis) | ~20% | Organic waste (69%), plastic packaging, cardboard, wood crates |
| **S4: Manufacturing (non-food)** | Light manufacturing, assembly, workshops | ~15% | Mixed: wood, plastic, metal, paper, rubber |
| **S5: Offices & services** | Office buildings, banks, administrations, hospitals | ~10% | Paper, cardboard, plastic cups/bottles, food waste |

[HYPOTHESIS] **ASSUMPTION** — Stream percentages are engineering estimates for Île-de-France, weighted toward the region's heavily service- and logistics-oriented economy. France nationally has a different industrial mix (more manufacturing). The IdF economy is ~75% tertiary (INSEE), which inflates S1, S2, and S5 relative to national averages. MEDIUM confidence.

**Regulatory context — 8-stream Decree (Décret 8 flux):**
Since 1 July 2016 (extended in 2021), all economic actors producing more than 1,100 litres/week of waste must sort 8 material streams: paper/cardboard, metal, plastic, glass, wood, textiles, mineral fraction, and plaster. This means that the residual waste arriving at sorting centres is already partially depleted of recyclables. The feedstock for the Urban Rig would primarily be either (a) unsorted mixed DAE from smaller producers below the threshold, or (b) sorting residues (sorting rejects/residues, refus de tri) from DAE sorting centres, which contain ~30% of input mass and are rich in mixed plastics, contaminated paper, and composite materials.

---

## 3. COMPOSITION BY STREAM — DETAILED BREAKDOWN

### 3.1 Stream S1: Logistics & Distribution (~30% of DAE)

Source: INSEE commercial waste survey (2016); CEVA Logistics sustainability report (Paris warehouse); general European logistics packaging data.

| Material | % of S1 | Per 1,000 kg S1 | Note |
|----------|---------|-----------------|------|
| Cardboard/corrugated | 40% | 400 kg | Shipping boxes, carton dividers, e-commerce packaging |
| Plastic film (LDPE/LLDPE) | 22% | 220 kg | Shrink wrap, stretch wrap, pallet covers, bubble wrap |
| Wood (pallets, crates) | 20% | 200 kg | Euro pallets, one-way pallets, wooden crates |
| Strapping (PP/PET) | 5% | 50 kg | Pallet banding, box strapping |
| EPS/foam | 3% | 30 kg | Protective packaging, electronics inserts |
| Metal (strapping, containers) | 3% | 30 kg | Steel strapping, drum remnants |
| Paper (labels, documents) | 4% | 40 kg | Delivery notes, labels, packing slips |
| Other (tape, adhesives, mixed) | 3% | 30 kg | Adhesive tape, mixed non-sortable |

[HYPOTHESIS] **HYPOTHESIS** — Based on European logistics packaging composition studies and French commercial waste surveys. Logistics waste is well-characterised because it is packaging-dominated and relatively homogeneous. HIGH confidence for material types, MEDIUM for exact percentages.

**Key advantage for pyrolysis:** Logistics waste is the driest and cleanest industrial stream — virtually zero food contamination, low moisture (<5%), high plastic content, high cellulose content. The LDPE film + PP strapping fraction is premium pyrolysis feedstock (77–80% oil yield). This is the single most attractive DAE stream for the Urban Rig.

### 3.2 Stream S2: Retail & Commerce (~25% of DAE)

Source: INSEE "Three-quarters of Commercial Waste is Sorted" (INSEE Première 1744, 2019); Citeo recycling data; European retail waste studies.

| Material | % of S2 | Per 1,000 kg S2 | Note |
|----------|---------|-----------------|------|
| Cardboard | 35% | 350 kg | Shipping and display packaging |
| Plastic packaging | 15% | 150 kg | Film, trays, bottles, blister packs |
| Food waste (organic) | 20% | 200 kg | Unsold perishables, canteen waste |
| Paper | 8% | 80 kg | Receipts, flyers, magazines |
| Wood | 5% | 50 kg | Display structures, crates |
| Glass | 5% | 50 kg | Bottles (wine, beverages) |
| Metal (cans, foil) | 4% | 40 kg | Beverage cans, food tins |
| Textiles | 3% | 30 kg | Unsold clothing (fast fashion returns) |
| Other (mixed) | 5% | 50 kg | Electronics packaging, composite materials |

[HYPOTHESIS] **HYPOTHESIS** — Based on INSEE commerce waste data: 86% ordinary waste, 13% organic. The material breakdown draws on Citeo packaging data and European retail waste studies. MEDIUM confidence — retail waste is variable by store type (supermarket vs. clothing vs. electronics).

**Caveat — France-specific:** French supermarkets (Carrefour, Leclerc, Auchan) are legally required since 2016 to donate unsold food to charities (Garot Law). This reduces the food waste fraction compared to pre-2016 data. The 20% food waste estimate accounts for this reduction.

### 3.3 Stream S3: Food Industry / Agrifood (Agroalimentaire) (~20% of DAE)

Source: ADEME — Food Industry Waste Study (2016: 3.8 MT, 69% organic); INSEE Manufacturing Waste Survey 2022; Rungis Wholesale Market Data.

| Material | % of S3 | Per 1,000 kg S3 | Note |
|----------|---------|-----------------|------|
| Organic waste (food processing) | 55% | 550 kg | Animal/vegetable processing residues, unsold food |
| Cardboard | 12% | 120 kg | Packaging, shipping boxes |
| Plastic packaging | 9% | 90 kg | Trays, film, polystyrene, containers |
| Wood (pallets, crates) | 7% | 70 kg | Wooden crates (esp. fruit/vegetables at Rungis) |
| Metal (tins, cans) | 5% | 50 kg | Food tins, aluminium lids |
| Glass | 5% | 50 kg | Jars, bottles |
| Paper | 3% | 30 kg | Labels, documents |
| Fats/oils (non-processable) | 4% | 40 kg | Used cooking oils — separate valorisation pathway |

[FACT] **FACT** — ADEME data confirms food industry waste is ~69% organic, ~31% other. INSEE 2022 confirms food industries produce ~10% of manufacturing waste. Data quality: HIGH for organic fraction, MEDIUM for sub-material breakdown.

**Caveat — Rungis Wholesale Market:** The Rungis International Market (the world's largest fresh produce wholesale market, 234 hectares, approximately 1.5 million tonnes of product traded annually) is located in Île-de-France. It generates an estimated 40,000–50,000 tonnes per year of waste (Semmaris annual report), heavily organic. If Rungis waste were specifically targeted, S3 organic fraction would increase to 65–70%.

**Note on biogas competition:** Organic food waste is increasingly diverted to anaerobic digestion under French bio-waste regulations (mandatory separate collection since 1 January 2024 for all producers). This reduces the organic fraction available for pyrolysis. The Urban Rig's value proposition for food industry waste is primarily the non-organic residual (packaging, mixed contaminated materials) that cannot be anaerobically digested.

### 3.4 Stream S4: Manufacturing (non-food) (~15% of DAE)

Source: INSEE Survey on Industrial Waste 2022 (Enquête déchets industrie 2022); INSEE Première 1745 (2019): "82% of Non-hazardous Waste is Sorted in Manufacturing Industries" (82% des déchets banals sont triés dans l'industrie manufacturière).

| Material | % of S4 | Per 1,000 kg S4 | Note |
|----------|---------|-----------------|------|
| Wood | 30% | 300 kg | Offcuts, pallets, crating — largest fraction nationally (39% of sorted mfg waste) |
| Metal | 20% | 200 kg | Scrap, offcuts, turnings — high recycling rate (93%) |
| Paper/cardboard | 15% | 150 kg | Packaging, documentation |
| Plastic | 10% | 100 kg | Packaging, offcuts, scrap parts |
| Rubber | 3% | 30 kg | Seals, gaskets, offcuts |
| Glass | 3% | 30 kg | Containers, process glass |
| Textile/leather | 2% | 20 kg | Cleaning rags, leather offcuts |
| Mixed/unsorted | 17% | 170 kg | Multi-material waste, contaminated |

[FACT] **FACT** — INSEE 2022 survey data for manufacturing establishments with 10+ employees: 15 MT non-hazardous waste, sorted waste composition: wood 39%, metals 28%, paper-cardboard 17%, glass 3%, plastics 4%. The percentages above adjust for the mixed/unsorted fraction (20% of manufacturing waste is unsorted per INSEE). Data quality: HIGH.

**Key observation:** Manufacturing waste is dominated by wood (39%) and metals (28%) — both with high existing recycling rates. The metal fraction (93% recovery) has little pyrolysis interest. The wood fraction has moderate pyrolysis value (charcoal). The most attractive fraction for the Urban Rig is the mixed/unsorted residual (17%) which contains cross-contaminated plastics, paper, and composites that cannot be easily recycled.

### 3.5 Stream S5: Offices & Services (~10% of DAE)

Source: INSEE Tertiary Waste Survey 2022; Istanbul Airport Office Data (Ozbay & Gokceviz, 2021) for cross-validation.

| Material | % of S5 | Per 1,000 kg S5 | Note |
|----------|---------|-----------------|------|
| Paper | 35% | 350 kg | Office paper, documents, envelopes — declining with digitalisation |
| Cardboard | 15% | 150 kg | Delivery boxes (e-commerce to offices) |
| Plastic | 12% | 120 kg | Cups, bottles, packaging, single-use items |
| Food waste | 20% | 200 kg | Canteen waste, vending machines, meeting catering |
| Glass | 5% | 50 kg | Bottles, glasses |
| Metal | 3% | 30 kg | Cans, cutlery |
| Other (mixed) | 10% | 100 kg | Electronics packaging, hygiene waste, mixed |

[HYPOTHESIS] **HYPOTHESIS** — Based on INSEE tertiary data (paper-cardboard 46–47% of sorted office waste) adjusted for the full waste stream including organic. Cross-validated with Istanbul Airport office data. MEDIUM confidence.

---

## 4. CONSOLIDATED DAE WASTE COMPOSITION

Weighting each stream by its share of IdF DAE:

| Material | S1 (30%) | S2 (25%) | S3 (20%) | S4 (15%) | S5 (10%) | **Weighted Total** | **% of total** |
|----------|---------|---------|---------|---------|---------|-------------------|---------------|
| Food/organic | 0 | 50 | 110 | 0 | 20 | **180** | **18.0%** |
| Plastic (all types) | 90 | 37.5 | 18 | 15 | 12 | **172.5** | **17.3%** |
| Paper/cardboard | 132 | 107.5 | 30 | 22.5 | 50 | **342** | **34.2%** |
| Wood | 60 | 12.5 | 14 | 45 | 0 | **131.5** | **13.2%** |
| Glass | 0 | 12.5 | 10 | 4.5 | 5 | **32** | **3.2%** |
| Metal | 9 | 10 | 10 | 30 | 3 | **62** | **6.2%** |
| Fats/oils (non-processable) | 0 | 0 | 8 | 0 | 0 | **8** | **0.8%** |
| Rubber/textile/other | 9 | 20.5 | 0 | 7.5 | 10 | **47** | **4.7%** |
| Mixed/unsorted | 0 | 0 | 0 | 25.5 | 0 | **25.5** | **2.6%** |
| **TOTAL** | **300** | **250** | **200** | **150** | **100** | **1,000** | **100%** |

*Values are kg per 1,000 kg of mixed IdF DAE waste.*

**Comparison with OMR (Annex 5) and CDG (Annex 6):**

| Parameter | OMR (Annex 5) | CDG Airport (Annex 6) | DAE (this annex) |
|-----------|--------------|----------------------|-------------------|
| Organic fraction | 27.0% | 26.0% | **18.0%** |
| Plastic fraction | 15.0% | 20.0% | **17.3%** |
| Paper/cardboard fraction | 14.0% | 25.4% | **34.2%** |
| Wood fraction | 1.5% | 9.7% | **13.2%** |
| Metal fraction | 3.0% | 6.3% | **6.2%** |

**Key insight:** DAE waste is radically different from OMR: half the organic content, double the paper/cardboard, nearly 9x the wood, and comparable plastic. This is a cellulose- and packaging-dominated stream — drier, less degradable, and easier to process.

---

## 5. REMOVING NON-PROCESSABLE MATERIAL

| Removed material | Mass (kg) | Removal method |
|-----------------|----------|----------------|
| Glass | 32 | Mechanical screening / optical sorting |
| Metal (ferrous + non-ferrous) | 62 | Magnetic + eddy current separation |
| Fats/oils | 8 | Separation at reception |
| Inert fraction from mixed (est. 30% of 25.5 kg) | 7.7 | Density separation |
| **Total removed** | **109.7** | |
| **Material entering reactor** | **890.3** | |

[ASSUMPTION] **ASSUMPTION** — Pre-sorting at standard MRF efficiency. Removal rate (109.7 kg/T) is very similar to OMR (109.5 kg/T) because DAE has more metal but less glass and no hygiene-related textiles.

---

## 6. CONSOLIDATED EFFECTIVE FEEDSTOCK — FINAL TABLE

### 6.1 Four-Category View (890.3 kg entering reactor)

| Category | Mass (kg) | % of reactor input | Composition |
|----------|----------|-------------------|-------------|
| **Organic** | 180 | 20.2% | Food waste from retail, food industry, offices |
| **Cellulose** | 473.5 | 53.2% | Paper 192 + cardboard 150 + wood 131.5 |
| **Plastic-like** | 219.5 | 24.7% | Plastic 172.5 + rubber/textile/composite 47 (50% is plastic-like) |
| **Mineral inert residual** | 17.3 | 1.9% | Remaining inerts from mixed fraction |
| **TOTAL** | **890.3** | **100%** | |

**Note on plastic-like classification:** The rubber/textile/other category (47 kg) contains a mix of materials. We estimate ~50% (23.5 kg) behaves as plastic-like in pyrolysis (rubber, synthetic textiles, composite plastics) and ~50% (23.5 kg) behaves as cellulose (natural textiles, leather). The 219.5 kg figure includes the 172.5 kg of pure plastic plus 23.5 kg of synthetic rubber/textile plus 23.5 kg from the mixed/unsorted fraction (estimated 50% plastic-like).

### 6.2 Adjusted Three-Category View (processable material, excl. mineral inert)

| Category | Mass (kg) | % of processable feedstock | Primary Urban Rig Output |
|----------|----------|---------------------------|--------------------------|
| **Organic (food waste)** | 180 | **20.6%** | Charcoal / biochar |
| **Cellulose (paper, cardboard, wood, natural fibre)** | 497 | **56.9%** | Charcoal + off-gas |
| **Plastic-like (polymers, synthetic rubber/textile)** | 196 | **22.4%** | Fuel oil (4 fractions) |
| **TOTAL processable** | **873** | **100%** | |

### 6.3 Comparison with French OMR (Annex 5) and CDG (Annex 6)

| Parameter | French OMR (Annex 5) | CDG Airport (Annex 6) | DAE (this annex) |
|-----------|---------------------|----------------------|-------------------|
| Plastic fraction (of processable) | 23.7% | 24.7% | **22.4%** |
| Cellulose fraction | 37.9% | 43.3% | **56.9%** |
| Organic fraction | 38.4% | 32.1% | **20.6%** |
| Material removed pre-sort | 109.5 kg/T | 189.5 kg/T | **109.7 kg/T** |
| Reactor input per tonne | 890.5 kg | 810.5 kg | **890.3 kg** |

**Key insight:** DAE waste has the highest cellulose content of all three feedstocks (57% vs 38–43%), driven by the dominance of cardboard and wood in logistics/retail/manufacturing waste. Its plastic content (22.4%) is slightly lower than OMR (23.7%), and its organic content is dramatically lower (20.6% vs 38.4%). This profile means: slightly less oil per tonne, significantly more charcoal, and the driest/easiest feedstock to process.

---

---

## 7. DAE PLASTIC POLYMER MIX

DAE plastic waste is dominated by packaging film (LDPE from logistics), rigid packaging (PET, PP, HDPE from retail), and industrial plastics. It has significantly less PVC than OMR because commercial/food-contact packaging is PVC-restricted under EU Regulation 10/2011.

### 7.1 Estimated Polymer Distribution

| Polymer | % of DAE plastic | Mass in 196 kg | Source/Basis |
|---------|-----------------|----------------|--------------|
| LDPE/LLDPE (film, shrink wrap) | 40% | 78.4 kg | Dominant in logistics (S1) — stretch wrap, pallet film |
| PP (containers, strapping, caps) | 18% | 35.3 kg | Food containers, pallet strapping, industrial containers |
| PET (bottles, trays, blisters) | 18% | 35.3 kg | Beverage bottles, food trays, blister packaging |
| HDPE (bottles, crates, drums) | 10% | 19.6 kg | Milk bottles, chemical drums, crates |
| PS/EPS (foam, trays) | 6% | 11.8 kg | Protective foam, food trays, insulation |
| PVC | 2% | 3.9 kg | Industrial piping, cable insulation (from S4) |
| Other (composites, rubber, synthetics) | 6% | 11.8 kg | Multi-layer packaging, synthetic rubber, mixed |

[HYPOTHESIS] **ASSUMPTION** — Based on European packaging waste composition (Eurostat 2022) and French commercial waste data. DAE plastic is overwhelmingly packaging (estimated >80%), with some industrial process plastic from S4. The LDPE dominance reflects the logistics sector's heavy use of stretch/shrink film. MEDIUM confidence.

**Key difference from OMR:** Polyolefin content (LDPE+LLDPE+HDPE+PP) = 68% vs 64% in OMR. This is higher because logistics film (pure LDPE) is a larger fraction. PVC is lower (2% vs 3%). Overall, DAE plastic should produce slightly higher oil yields than OMR plastic due to the polyolefin enrichment.

---

# PART 2 — WHAT COMES OUT: Pyrolysis Yields

*Applying the same per-material yields as Annex 5 (Section 10) to the DAE feedstock.*

---

## 8. WEIGHTED YIELD CALCULATION

### 8.1 Plastic-Like Fraction (196 kg)

| Material | Mass (kg) | Oil yield | Oil (kg) | Off-gas (kg) | Residue (kg) | Data quality |
|----------|----------|----------|---------|-------------|-------------|-------------|
| LDPE/LLDPE | 78.4 | 77% | 60.4 | 17.2 | 0.8 | [FACT] FACT |
| PP | 35.3 | 80% | 28.2 | 6.4 | 0.7 | [FACT] FACT |
| PET | 35.3 | 45% | 15.9 | 6.0 | 13.4 | [HYPOTHESIS] HYPOTHESIS |
| HDPE | 19.6 | 77% | 15.1 | 4.3 | 0.2 | [FACT] FACT |
| PS/EPS | 11.8 | 58% | 6.8 | 1.6 | 3.3 | [FACT] FACT |
| PVC | 3.9 | 32% | 1.2 | 0.1 | 0.6 | [HYPOTHESIS] HYPOTHESIS |
| PVC HCl | — | — | — | 2.1 | — | Stoichiometric |
| Other | 11.8 | 25% | 3.0 | 3.0 | 5.8 | [HYPOTHESIS] HYPOTHESIS |
| **SUBTOTAL** | **196** | | **130.6** | **38.6** | **24.8** | |
| **Mass check** | | | 130.6 + 38.6 + 24.8 + 2.1 = **196.1** ≈ 196 | | |
| **Weighted oil yield** | | **66.6%** | (130.6 / 196) | | | |

### 8.2 Organic + Cellulose Fraction (677 kg)

| Material | Mass (kg) | Oil yield | Oil (kg) | Off-gas (kg) | Residue (kg) | Data quality |
|----------|----------|----------|---------|-------------|-------------|-------------|
| Cellulose (paper, cardboard, wood, nat. fibre) | 497 | 12% | 59.6 | 99.4 | 338.0 | [HYPOTHESIS] HYPOTHESIS |
| Food waste (organic) | 180 | 10% | 18.0 | 36.0 | 126.0 | [HYPOTHESIS] HYPOTHESIS |
| **SUBTOTAL** | **677** | | **77.6** | **135.4** | **464.0** | |

### 8.3 Mineral Inert Residual (17.3 kg)

This fraction passes through the reactor unchanged and reports to the residue/char output.

### 8.4 TOTAL OUTPUT — 890.3 kg Entering Reactor

| Product | From plastic | From organic/cellulose | From inert | **TOTAL** | **% of 890.3 kg** |
|---------|-------------|----------------------|-----------|----------|-----------------|
| **Oil** | 130.6 | 77.6 | 0 | **208.2** | **23.4%** |
| **Off-gas** | 38.6 | 135.4 | 0 | **174.0** | **19.5%** |
| **Residue/Char** | 24.8 | 464.0 | 17.3 | **506.1** | **56.8%** |
| **HCl (filtered)** | 2.1 | 0 | 0 | **2.1** | **0.2%** |

### 8.5 Comparison with French OMR (Annex 5) and CDG (Annex 6)

| Product | French OMR | CDG Airport | DAE (this annex) |
|---------|-----------|-------------|------------------|
| Oil (% of reactor input) | 23.0% | 24.6% | **23.4%** |
| Oil (kg per 1,000 kg raw waste) | 204.7 | 199.2 | **208.2** |
| Off-gas | 19.2% | 19.8% | **19.5%** |
| Char/residue | 57.5% | 55.5% | **56.8%** |
| Plastic oil yield (weighted) | 65.1% | 65.6% | **66.6%** |

**Key finding:** DAE waste produces the highest oil yield per tonne of raw waste (208.2 kg vs 204.7 for OMR and 199.2 for CDG) because less material is removed in pre-sorting (109.7 vs 189.5 kg for CDG). The plastic oil yield is also the highest (66.6%) due to the polyolefin-enriched polymer mix. However, the char fraction is large (57%) due to the high cellulose content. **DAE is the most productive feedstock of the three on a per-tonne-raw-waste basis.**

---

## 9. ENERGY BALANCE AND CHAR ENERGY VALUE

Using the same methodology as Annex 5 §13:

| Parameter | Per 1,000 kg raw DAE waste | Per day (140 T) |
|-----------|---------------------------|-----------------|
| Combustible char | 506.1 kg | 70,854 kg (70.9 T) |
| Char energy (at 15.6 MJ/kg weighted) | 7,895 MJ | 1,105,322 MJ |
| Off-gas energy | ~408 MJ (plastic) + ~135 MJ (organic) = ~543 MJ | 76,020 MJ |
| **Total available energy** | 8,438 MJ | **1,181,342 MJ** |
| Heating demand | 2,714 MJ | 379,960 MJ |
| **Coverage** | | **311%** |

**Char energy value:** The system produces ~3.1x its energy needs from char and off-gas. Under the V2 model, all char is sold commercially to fuel buyers rather than used for reactor heating. The higher coverage (311% vs 278% for CDG, ~280% for OMR) is due to the higher cellulose content producing more char, demonstrating the substantial commercial energy value of the pyrolysis char product.

---

## 10. FINANCIAL IMPACT — DAE vs OMR vs CDG

At 140 T/day throughput (steady state, Year 3):

| Revenue stream | OMR (Annex 5) | CDG Airport (Annex 6) | DAE (this annex) | Note |
|---------------|--------------|----------------------|-------------------|------|
| Oil volume (L/year, full capacity) | 12.56M | 12.19M | **12.78M** | DAE highest due to low pre-sort removal |
| Oil revenue (€0.55/L) | €6.9M | €6.7M | **€7.0M** | |
| Gate fee (€/T) | €110 | €130–150 | **€80–100** | DAE commands lower fees — competitive market |
| Gate fee revenue | €5.1M | €6.0–6.9M | **€3.7–4.6M** | Key disadvantage of DAE |
| Metal revenue (€300/T) | €0.7M | €0.9M | **€0.9M** | Similar metal content to CDG |
| Char revenue (V2 — all char sold) | €1.7M | €1.5M | **€1.9M** | More char from high cellulose |
| Carbon credits | €2.5M | €2.5M | **€2.5M** | Similar |
| Glass revenue (€25/T) | €0.06M | €0.1M | **€0.04M** | Less glass in DAE |
| **TOTAL REVENUE** | **€17.0M** | **€17.7–18.6M** | **€16.0–16.9M** | |

**The DAE disadvantage is the gate fee.** Industrial waste treatment is a competitive market in Île-de-France with established operators (Veolia, Suez, Paprec, Séché Environnement) and significant incineration capacity. Gate fees for mixed DAE typically range from €80–120/T, below the €110/T achievable for OMR and well below the €130–150/T for airport waste. However, DAE compensates partially through higher oil volume and char production.

**Strategic consideration — Sorting centre residues (sorting rejects/residues):** If the Urban Rig targets sorting centre residues rather than raw DAE, the economics shift significantly. Sorting residues are enriched in plastics and contaminated paper (estimated 40–50% plastic, 30% paper, 20% other), with gate fees of €100–130/T because they are difficult to dispose of. This stream would be smaller in volume but significantly more profitable per tonne.

---

## 11. DAE-SPECIFIC OPERATIONAL CONSIDERATIONS

### 11.1 Feedstock Variability

DAE is more variable than OMR or airport waste. A logistics centre produces 90%+ packaging (cardboard, plastic film). A food processor produces 70%+ organic waste. An office building produces 50%+ paper. The Urban Rig would need to manage this variability through:

- **Blending:** Accepting waste from multiple sources and blending to target composition
- **Buffer storage:** Maintaining a 3–5 day buffer to smooth composition swings
- **Contractual minimum:** Long-term supply contracts with 3–5 major generators to ensure baseline volume

### 11.2 Moisture Content

DAE waste is significantly drier than OMR:

| Feedstock | Typical moisture | Impact on process |
|-----------|-----------------|-------------------|
| OMR (Annex 5) | 30–40% | Requires energy for drying |
| CDG Airport (Annex 6) | 25–35% | Moderate moisture from food waste |
| DAE (this annex) | **15–25%** | Low moisture — less drying energy needed |

The lower moisture content of DAE means less energy is consumed in the initial drying/pyrolysis phase, potentially increasing throughput or reducing fuel consumption. This is a significant operational advantage.

### 11.3 Contamination Risks

| Contaminant | Risk level | Mitigation |
|-------------|-----------|------------|
| PVC (from industrial S4) | MEDIUM | Higher than airport waste; HCl scrubbing required |
| Heavy metals (from electronics packaging) | LOW | Pre-sort removal of WEEE (Waste Electrical and Electronic Equipment) |
| Halogenated flame retardants | LOW | Present in some foam/textile waste |
| Chemical residues (from S4 manufacturing) | LOW-MEDIUM | Exclude chemical/pharma sector waste |

### 11.4 Competition for Feedstock

The DAE waste market in Île-de-France is competitive:

| Competitor | Capacity | Gate fee range |
|-----------|----------|---------------|
| UIOM (municipal incinerators) — accept some DAE | ~3.5 MT/year in IdF | €80–110/T |
| ISDND (landfills — non-hazardous waste) | ~2.2 MT/year in IdF | €70–100/T |
| SRF (Solid Recovered Fuel) production plants | Growing (1.2 MT national capacity) | €60–90/T |
| Recycling/sorting centres | ~350 nationally | Variable |

The Urban Rig competes against these established disposal routes. Its competitive advantages are: (a) higher diversion rate than landfill, (b) lower emissions than incineration, (c) produces valuable products (oil, char) versus only heat/electricity from incineration, and (d) can accept contaminated/mixed fractions that recycling rejects.

---

## 12. VOLUME AVAILABILITY IN ÎLE-DE-FRANCE

### 12.1 Estimated DAE Feedstock Pool

| Parameter | Volume (T/year) | Source |
|-----------|----------------|--------|
| Total DAE in IdF (excl. construction) | 5,000,000–7,000,000 | Estimated from ORDIF + INSEE data |
| Currently recycled | ~3,000,000–4,000,000 | 60–70% recycling rate (INSEE 2022) |
| Currently incinerated | ~1,500,000–2,000,000 | ORDIF Incineration Data 2022 |
| Currently landfilled | ~800,000–1,000,000 | ORDIF Landfill Data 2022 |
| **Residual available for pyrolysis** | **~500,000–1,000,000** | Sub-fraction of incinerated/landfilled DAE suitable for pyrolysis |

[HYPOTHESIS] **ASSUMPTION** — The pyrolysis-suitable fraction is estimated at 30–50% of the waste currently going to incineration/landfill (excluding mineral/inert, hazardous, and high-moisture waste). MEDIUM confidence.

### 12.2 Urban Rig Capacity Requirement

At 140 T/day, 330 operating days/year = ~46,200 T/year input. This represents only 5–9% of the estimated available feedstock pool. **Volume is not a constraint for DAE sourcing.**

### 12.3 Proximity to Key Sources

| Source | Distance from Roissy area | Est. DAE volume | Note |
|--------|--------------------------|-----------------|------|
| Garonor logistics hub | 5 km | 15,000–20,000 T/year | 75 ha, 350,000 m² buildings |
| Roissy-CDG cargo zone | Adjacent | 8,000–12,000 T/year | Part of CDG waste (Annex 3) |
| Paris-Nord II business park | 3 km | 10,000–15,000 T/year | 300+ companies |
| Gennevilliers port zone | 25 km | 20,000–30,000 T/year | 400 ha multimodal platform |
| Rungis wholesale market | 35 km | 40,000–50,000 T/year | World's largest fresh produce market |
| Seine-Saint-Denis industrial zones | 10–20 km | 30,000–50,000 T/year | Dense mixed commercial/industrial |

[HYPOTHESIS] **ASSUMPTION** — Volume estimates based on floor area × typical waste intensity (2–5 kg/m²/year for logistics, higher for food). MEDIUM confidence. Would require on-site waste audits to confirm.

---

## 13. DATA QUALITY SUMMARY

| Parameter | Classification | Confidence |
|-----------|---------------|------------|
| Total DAE in France (~63 MT/year) | [FACT] FACT | HIGH — ADEME/Eurostat |
| Manufacturing waste composition | [FACT] FACT | HIGH — INSEE 2022 survey |
| Tertiary waste composition | [FACT] FACT | HIGH — INSEE 2022 survey |
| IdF DAE volumes | [HYPOTHESIS] ASSUMPTION | MEDIUM — derived from ORDIF data |
| Stream percentages (S1-S5) | [HYPOTHESIS] ASSUMPTION | MEDIUM — engineering estimate for IdF economy |
| Logistics waste composition (S1) | [HYPOTHESIS] HYPOTHESIS | HIGH — well-characterised packaging stream |
| Retail waste composition (S2) | [HYPOTHESIS] HYPOTHESIS | MEDIUM — variable by store type |
| Food industry waste composition (S3) | [FACT] FACT/HYPOTHESIS | HIGH organic fraction, MEDIUM sub-materials |
| Manufacturing waste composition (S4) | [FACT] FACT | HIGH — INSEE data |
| Office waste composition (S5) | [HYPOTHESIS] HYPOTHESIS | MEDIUM — Istanbul Airport cross-validation |
| Plastic polymer mix | [HYPOTHESIS] ASSUMPTION | MEDIUM — European packaging data |
| Pyrolysis yields | Per Annex 1 | See Annex 1 §16 |
| Gate fee estimates | [HYPOTHESIS] HYPOTHESIS | MEDIUM — market data from operator websites |

---

## 14. RECOMMENDATIONS

1. **DAE waste is viable pyrolysis feedstock** with the highest oil yield per tonne of raw waste (208.2 kg vs 204.7 for OMR and 199.2 for CDG). Its lower moisture content and high packaging fraction make it operationally attractive.

2. **The logistics sector (S1) is the single most attractive DAE stream** — clean, dry, plastic/cellulose-rich, with minimal contamination and high predictability. Targeting 3–5 major logistics operators (Geodis, DHL, Kuehne+Nagel, Amazon, CEVA) near the Roissy area could secure 30,000–50,000 T/year of premium feedstock.

3. **Gate fees are the primary financial disadvantage** compared to OMR and airport waste. DAE gate fees (€80–100/T) are 10–40% below OMR (€110/T) and 40–50% below airport waste (€130–150/T). This is partially offset by higher oil production.

4. **Sorting centre residues (sorting rejects, "refus de tri") represent a premium sub-market.** These plastic-enriched residual streams command higher gate fees (€100–130/T) and produce higher oil yields. Partnering with one or two major DAE sorting operators (Paprec, Veolia, Séché) could access this stream.

5. **Blending DAE with OMR or airport waste is the optimal strategy.** A mix of 50% OMR + 30% DAE + 20% airport waste would provide: stable volume (OMR), premium gate fees (airport), high oil yield (DAE), and feedstock diversification to reduce supply risk.

6. **A waste characterisation study at 2–3 major logistics/commercial sites in IdF is essential.** All composition data in this annex is derived from national surveys and literature — not from specific site audits. A 2-week sampling campaign at Garonor, Rungis, and one manufacturing zone would dramatically increase confidence.

7. **Bio-waste diversion is a growing competitor for the organic fraction.** The mandatory separate collection of bio-waste (since 1 January 2024) will progressively reduce the organic fraction in mixed DAE. This favours the Urban Rig's long-term positioning: as organics are diverted to anaerobic digestion, the remaining residual stream becomes increasingly plastic- and cellulose-rich — which is ideal for pyrolysis.

---

## 15. SOURCES

| # | Source | Used for |
|---|--------|----------|
| 1 | ADEME — Waste Key Figures: Essentials, 2024 Edition (Chiffres-clés déchets: L'essentiel, Édition 2024) | National DAE volumes, waste production overview |
| 2 | INSEE — Waste in Industrial and Tertiary Sector Establishments in 2022 (Les déchets dans les établissements de l'industrie et du tertiaire en 2022, INSEE Première 2034) | Manufacturing + tertiary waste composition and tonnages |
| 3 | INSEE — 82% of Non-hazardous Waste is Sorted in Manufacturing Industries (82% des déchets banals sont triés dans l'industrie manufacturière, INSEE Première 1745, 2019) | Sorting rates by sector, material breakdown |
| 4 | INSEE — Three-quarters of Commercial Waste is Sorted (Les trois quarts des déchets du commerce sont triés, INSEE Première 1744, 2019) | Commercial waste composition |
| 5 | ORDIF — Landfill of Non-hazardous Waste in Île-de-France: Data 2022–2023 (Enfouissement des déchets non dangereux en Île-de-France: données 2022–2023) | IdF landfill volumes |
| 6 | ORDIF — Incineration of Non-hazardous Waste in Île-de-France: Data 2022 (Incinération des déchets non dangereux en Île-de-France: données 2022) | IdF incineration volumes |
| 7 | DRIEAT Île-de-France — 30 Million Tonnes of Waste Produced in Île-de-France (30 millions de tonnes de déchets produits en Île-de-France) | Regional waste overview |
| 8 | Institut Paris Région — Logistics Overview in Île-de-France (Logistics Landscape in Île-de-France, État des lieux de la logistique en Île-de-France) | Logistics infrastructure, warehouse floor area |
| 9 | Decree 2021-950 of July 16, 2021 (8-Stream Decree, Décret 8 flux) | Mandatory sorting obligations for DAE producers |
| 10 | Eurostat — Packaging Waste Statistics 2022 | European packaging composition (paper 40.8%, plastic 19.4%, glass 18.8%, wood 16.0%, metal 4.9%) |
| 11 | ADEME — Commercial and Industrial Waste: Know, Reduce, Master (2023) (Economic Activities Waste: Know, Reduce, Master, Les déchets d'activités économiques: connaître, réduire, maîtriser) | DAE overview and management guidance |
| 12 | Senate — Written Question No. 02293 (2022): Solid Recovered Fuels (Solid Recovered Fuels, Combustibles solides de récupération) | SRF production in France (400 kT in 2022) |
| 13 | ISPRA (2024) — SRF Average Composition | SRF: plastics 40–60%, paper/cardboard 20–30%, textiles 10–15% |
| 14 | Annex 5 — MSW Feedstock Composition and Expected Yield Model | Per-material pyrolysis yields, OMR comparison |
| 15 | Annex 6 — CDG Airport Waste Feedstock Composition and Expected Yield Model | CDG comparison data |

---

**End of Annex 7**
