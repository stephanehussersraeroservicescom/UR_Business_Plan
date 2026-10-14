# Annex 6 — Sector: Airport Waste — CDG (France)

**Purpose:** Sector-specific feedstock profile for Paris-Charles de Gaulle Airport waste processed through the Urban Rig, including step-by-step derivation of expected pyrolysis product yields (oil, off-gas, residue).

**Date:** March 2026
**Status:** DRAFT — Initial research compilation

---

## OBJECTIVE

To answer the question: **If we source waste from CDG Airport operations, what composition enters the Urban Rig, and what are the expected outputs?**

CDG Airport generates a fundamentally different waste stream from French municipal waste (Annex 5). Airport waste is richer in plastics, packaging, and food service materials, with less putrescible garden waste and fewer sanitary textiles. This shifts the yield profile significantly toward higher oil output and lower char production.

This annex follows the same Part 1 / Part 2 structure as Annex 5. Every parameter is classified as: **FACT** (measured or from official sources), **HYPOTHESIS** (literature-based estimate), or **ASSUMPTION** (engineering judgment).

---

# PART 1 — WHAT GOES IN: Airport Waste Composition

*This part answers: of the waste available at CDG, what materials would enter the reactor, and in what proportions?*

---

## 1. CDG AIRPORT — OVERVIEW AND WASTE VOLUMES

### 1.1 Airport Profile

| Parameter | Value | Source |
|-----------|-------|--------|
| Passengers (2024) | 70.3 million | Groupe ADP traffic figures, Feb 2025 |
| Passengers (2023) | 68.3 million | Groupe ADP traffic figures |
| Terminals | 3 (T1, T2A-F, T3) | Groupe ADP |
| Cargo zone | Paris-CDG Cargo City (2nd largest in Europe) | Groupe ADP |
| Waste contractor | Paprec (since Jan 2016) | Paprec Solutions / Industrial News (L'Usine Nouvelle), 2015 |

[FACT] **FACT** — Traffic figures from official Groupe ADP publications. Data quality: HIGH.

### 1.2 Total Waste Generation

| Parameter | Value | Source |
|-----------|-------|--------|
| Total non-hazardous waste (all Paris airports) | ~43,000 T/year | Paprec Solutions |
| CDG share (estimated) | ~35,000 T/year | **ASSUMPTION** — CDG handles ~80% of Groupe ADP (Paris Airports Group) passenger + cargo traffic |
| Waste per passenger (terminal) | ~0.4–0.5 kg/pax | Istanbul Airport study (Ozbay & Gokceviz, 2021): 0.39 kg/pax (2019). Cross-check: Heathrow ~1.4 kg/pax includes cabin waste. |
| Cabin waste per passenger (IATA) | 0.94 kg/pax (international average) | IATA/ASF Cabin Waste Composition Audits, 2024 |

[HYPOTHESIS] **ASSUMPTION** — CDG-specific waste tonnage is not publicly broken out from Groupe ADP totals. The 35,000 T estimate is derived from CDG's ~80% share of Groupe ADP traffic. Actual tonnage may differ due to cargo zone contribution.

**Note on waste destination today:** Of the ~43,000 T/year across Paris airports, Paprec reports that ~27,000 T are incinerated and only ~5,000 T recycled (source: Paprec Solutions). The valorization rate is ~50%, with material recovery around 12%. This represents significant untapped potential.

---

## 2. AIRPORT WASTE STREAMS — SOURCE IDENTIFICATION

CDG waste comes from five distinct operational zones, each with a different composition profile:

| Stream | Description | Est. share of CDG waste | Key materials |
|--------|------------|------------------------|---------------|
| **S1: Terminal commercial** | Shops, restaurants, lounges, passenger areas | ~30% | Food waste, plastic packaging, cups, paper, cardboard, glass |
| **S2: Cabin/catering waste** | Inflight meal trays, beverages, service items | ~25% | Food waste, plastic trays/cups, aluminium foil, paper napkins, glass miniatures |
| **S3: Cargo/freight zone** | Packaging from air freight operations | ~25% | Cardboard, shrink wrap (LDPE), wood pallets, plastic film, strapping |
| **S4: Offices/admin** | Airport offices, airline offices, ground handlers | ~10% | Paper, cardboard, plastic bottles, food packaging |
| **S5: Maintenance/operations** | Technical areas, construction, GSE maintenance | ~10% | Mixed (some hazardous — excluded), wood, plastic, metal |

[HYPOTHESIS] **ASSUMPTION** — Stream percentages are engineering estimates based on airport waste literature (Istanbul Airport study; ICAO Waste Management at Airports toolkit; Ferrovial airport waste analysis). CDG-specific breakdown not published. MEDIUM confidence.

**Critical regulatory note — International Catering Waste (ICW):**
Cabin waste from flights originating outside the EU is classified as **Category 1 (CAT1) animal by-product** under EU Regulation 1069/2009. This waste MUST be disposed of by incineration, pressure sterilisation, or authorised deep burial. It CANNOT be recycled or composted under current EU law. This represents a significant portion of S2 at CDG (an international hub). **Pyrolysis at >400°C would meet the thermal destruction requirement, but regulatory approval would be needed.** This is flagged as a critical regulatory pathway to investigate. IATA is actively lobbying for smarter regulation of ICW (joint statement, August 2022).

---

## 3. COMPOSITION BY STREAM — DETAILED BREAKDOWN

### 3.1 Stream S1: Terminal Commercial Waste (~30% of total)

Source: Istanbul Airport terminal waste characterization (Ozbay & Gokceviz, 2021, *J. Material Cycles and Waste Management*); cross-validated with Schiphol BCAM study (van der Tuin-Rademaker et al., 2024, *Frontiers in Sustainability*); adjusted for CDG commercial mix.

| Material | % of S1 | Per 1,000 kg S1 | Note |
|----------|---------|-----------------|------|
| Food waste (organic) | 35% | 350 kg | Restaurant leftovers, passenger food scraps |
| Plastic packaging | 20% | 200 kg | Cups, bottles, trays, film, clamshells |
| Paper/cardboard | 18% | 180 kg | Newspapers, magazines, receipts, boxes |
| Glass | 8% | 80 kg | Bottles (wine, spirits, water) |
| Metal (cans, foil) | 5% | 50 kg | Aluminium cans, steel food cans |
| Wood | 3% | 30 kg | Crates, pallets from retail supply |
| Textiles/other | 5% | 50 kg | Wipes, napkins, mixed |
| Liquids (non-processable) | 6% | 60 kg | Beverages, sauces — removed by drainage |

[HYPOTHESIS] **HYPOTHESIS** — Based on Istanbul Airport terminal data (56% combustible, 36% recyclable) and Schiphol BCAM priority streams. Adapted for CDG's heavy food service presence (T2E/F duty-free zones, 50+ restaurants). MEDIUM confidence.

### 3.2 Stream S2: Cabin/Catering Waste (~25% of total)

Source: LIFE Zero Cabin Waste project (IBERIA/Madrid Barajas, 2019); IATA Cabin Waste Handbook (2017); IATA/ASF Cabin Waste Composition Audits (2024); "Beyond the Runway" UK study (2025).

| Material | % of S2 | Per 1,000 kg S2 | Note |
|----------|---------|-----------------|------|
| Food waste (organic) | 54% | 540 kg | Largest fraction. 23% of total is untouched food (IATA 2024). |
| Plastic (trays, cups, film) | 14% | 140 kg | PET/PP trays, PS cups, PE film |
| Paper/cardboard | 16% | 160 kg | Napkins, cartons, meal boxes, newspapers |
| Glass | 6% | 60 kg | Miniature bottles, wine glasses |
| Aluminium | 4% | 40 kg | Foil lids, cans, meal tray covers |
| Liquids (non-processable) | 6% | 60 kg | Unconsumed beverages — drained |

[FACT] **FACT** — These percentages are from the LIFE Zero Cabin Waste characterization study: organic 54%, paper/cardboard 15.6%, plastics 14.2%, glass 6.4%, aluminium 4%. Data quality: HIGH (145 flights audited at Madrid Barajas).

**Caveat — France-specific:** CDG serves predominantly European and long-haul routes. Long-haul flights generate more waste per passenger (0.6–0.9 kg/pax vs 0.31 kg/pax short-haul) with higher food content. The "Zero Cabin Waste" data is from Iberia at Madrid — a comparable European hub but with a different route mix.

### 3.3 Stream S3: Cargo/Freight Zone (~25% of total)

Source: Airport cargo packaging literature; ICAO Waste Management at Airports toolkit; Paprec CDG operational descriptions.

| Material | % of S3 | Per 1,000 kg S3 | Note |
|----------|---------|-----------------|------|
| Cardboard/corrugated | 40% | 400 kg | Shipping boxes, dividers, corner protectors |
| Plastic film (LDPE) | 20% | 200 kg | Shrink wrap, stretch wrap, pallet covers |
| Wood (pallets, crates) | 25% | 250 kg | Pallets (often ISPM-15 treated), crates |
| Strapping (PP/PET) | 5% | 50 kg | Banding material |
| Metal (banding, containers) | 5% | 50 kg | Steel strapping, container fragments |
| Other (foam, padding) | 5% | 50 kg | EPS foam, bubble wrap (PE), air pillows |

**ASSUMPTION** — Based on general air freight packaging composition and operational descriptions (cardboard, wood, plastic film as primary streams). CDG-specific cargo waste characterization not published. MEDIUM confidence.

**Key advantage for pyrolysis:** Cargo waste is predominantly clean, dry, and plastic/cellulose-rich. Very low food contamination. The LDPE (low-density polyethylene) film + PP (polypropylene) strapping fraction is high-yield pyrolysis feedstock (77–80% oil). This is the most attractive stream for the Urban Rig.

### 3.4 Stream S4: Office/Admin Waste (~10% of total)

Source: Istanbul Airport office waste characterization (Ozbay & Gokceviz, 2021).

| Material | % of S4 | Per 1,000 kg S4 | Note |
|----------|---------|-----------------|------|
| Paper | 35% | 350 kg | Office paper, documents, envelopes |
| Cardboard | 15% | 150 kg | Delivery boxes |
| Plastic | 15% | 150 kg | Bottles, packaging, cups |
| Food waste | 20% | 200 kg | Canteen/lunch waste |
| Glass | 5% | 50 kg | |
| Metal | 5% | 50 kg | Cans |
| Other | 5% | 50 kg | |

[HYPOTHESIS] **HYPOTHESIS** — Based on Istanbul Airport office data (43% recyclable, 43% combustible, 7–23% organic depending on office type). MEDIUM confidence.

### 3.5 Stream S5: Maintenance/Operations (~10% of total)

| Material | % of S5 | Per 1,000 kg S5 | Note |
|----------|---------|-----------------|------|
| Wood | 25% | 250 kg | Construction/maintenance timber |
| Plastic (mixed) | 15% | 150 kg | Piping, sheeting, packaging |
| Metal | 20% | 200 kg | Scrap, structural offcuts |
| Cardboard | 10% | 100 kg | |
| Inert (concrete, rubble) | 20% | 200 kg | Non-processable |
| Other/hazardous | 10% | 100 kg | Excluded from pyrolysis |

[HYPOTHESIS] **ASSUMPTION** — Engineering estimate. LOW confidence. This stream is the least well-characterised and most variable.

---

## 4. CONSOLIDATED AIRPORT WASTE COMPOSITION

Weighting each stream by its share of CDG total waste:

| Material | S1 (30%) | S2 (25%) | S3 (25%) | S4 (10%) | S5 (10%) | **Weighted Total** | **% of total** |
|----------|---------|---------|---------|---------|---------|-------------------|---------------|
| Food/organic | 105 | 135 | 0 | 20 | 0 | **260** | **26.0%** |
| Plastic (all types) | 60 | 35 | 75 | 15 | 15 | **200** | **20.0%** |
| Paper/cardboard | 54 | 40 | 100 | 50 | 10 | **254** | **25.4%** |
| Wood | 9 | 0 | 62.5 | 0 | 25 | **96.5** | **9.7%** |
| Glass | 24 | 15 | 0 | 5 | 0 | **44** | **4.4%** |
| Metal | 15 | 10 | 12.5 | 5 | 20 | **62.5** | **6.3%** |
| Liquids (drained) | 18 | 15 | 0 | 0 | 0 | **33** | **3.3%** |
| Inert/non-processable | 0 | 0 | 0 | 0 | 20 | **20** | **2.0%** |
| Other/hazardous (excluded) | 15 | 0 | 0 | 5 | 10 | **30** | **3.0%** |
| **TOTAL** | **300** | **250** | **250** | **100** | **100** | **1,000** | **100%** |

*Values are kg per 1,000 kg of mixed CDG waste.*

---

## 5. REMOVING NON-PROCESSABLE MATERIAL

| Removed material | Mass (kg) | Removal method |
|-----------------|----------|----------------|
| Glass | 44 | Mechanical screening / optical sorting |
| Metal (ferrous + non-ferrous) | 62.5 | Magnetic + eddy current separation |
| Liquids | 33 | Drainage at reception |
| Inert (concrete, rubble) | 20 | Density separation |
| Hazardous / excluded | 30 | Manual sorting / pre-screening |
| **Total removed** | **189.5** | |
| **Material entering reactor** | **810.5** | |

**ASSUMPTION** — Pre-sorting at standard Materials Recovery Facility (MRF) efficiency. Higher removal rate than OMR (189.5 kg vs 109.5 kg) because airport waste has more glass, metals, and liquids.

---

## 6. CONSOLIDATED EFFECTIVE FEEDSTOCK — FINAL TABLE

### 6.1 Four-Category View (810.5 kg entering reactor)

| Category | Mass (kg) | % of reactor input | Composition |
|----------|----------|-------------------|-------------|
| **Organic** | 260 | 32.1% | Food waste from terminals, catering, offices |
| **Cellulose** | 350.5 | 43.3% | Paper 154 + cardboard 100 + wood 96.5 |
| **Plastic-like** | 200 | 24.7% | All polymer types — see §7 |
| **Mineral inert** | 0 | 0% | All removed in pre-sort |
| **TOTAL** | **810.5** | **100%** | |

### 6.2 Three-Category View (processable material)

| Category | Mass (kg) | % of processable feedstock | Primary Urban Rig Output |
|----------|----------|---------------------------|--------------------------|
| **Organic (food waste)** | 260 | **32.1%** | Charcoal / biochar |
| **Cellulose (paper, cardboard, wood)** | 350.5 | **43.3%** | Charcoal + off-gas |
| **Plastic-like (all polymers)** | 200 | **24.7%** | Fuel oil (4 fractions) |
| **TOTAL processable** | **810.5** | **100%** | |

### 6.3 Comparison with French OMR (Annex 5)

| Parameter | French OMR (Annex 5) | CDG Airport | Difference |
|-----------|---------------------|-------------|------------|
| Plastic fraction (of processable) | 23.7% | **24.7%** | +1.0 pp |
| Cellulose fraction | 37.9% | **43.3%** | +5.4 pp |
| Organic fraction | 38.4% | **32.1%** | -6.3 pp |
| Material removed pre-sort | 109.5 kg/T | **189.5 kg/T** | +80 kg |
| Reactor input per tonne | 890.5 kg | **810.5 kg** | -80 kg |

**Key insight:** CDG waste is surprisingly similar to OMR in its plastic content (~25%), but significantly richer in cellulose (paper/cardboard/wood from cargo) and leaner in putrescibles (no garden waste, less food relative to packaging). The biggest difference is the pre-sort removal: more glass and metals at the airport.

---

## 7. AIRPORT PLASTIC POLYMER MIX

Airport plastic waste has a different polymer profile from municipal waste — dominated by packaging films (LDPE), PET bottles/trays, and PP containers, with very little PVC.

### 7.1 Estimated Polymer Distribution

| Polymer | % of airport plastic | Mass in 200 kg | Source/Basis |
|---------|---------------------|----------------|--------------|
| LDPE (film, shrink wrap) | 35% | 70 kg | Dominant in cargo (shrink wrap) + terminal (bags) |
| PET (bottles, trays, clamshells) | 25% | 50 kg | Beverage bottles, meal trays, service items |
| PP (cups, lids, containers) | 20% | 40 kg | Food containers, cup lids, strapping |
| PS/EPS (foam, cups) | 8% | 16 kg | Styrofoam packaging, disposable cups |
| HDPE (bottles, containers) | 7% | 14 kg | Milk/juice bottles, cleaning product containers |
| PVC | 1% | 2 kg | Minimal in airport/food packaging context |
| Other (mixed, composites) | 4% | 8 kg | Multi-layer packaging, laminates |

**ASSUMPTION** — Based on European food service and logistics packaging composition. Airport waste is packaging-dominated (not consumer goods), so PET (polyethylene terephthalate) and LDPE are overrepresented vs municipal waste. PVC (polyvinyl chloride) is minimal (food-contact packaging is PVC-free in the EU since Regulation 10/2011 restrictions). MEDIUM confidence.

**Key difference from OMR (Municipal Solid Waste):** PET (polyethylene terephthalate) fraction is higher (25% vs 18% in OMR) due to beverage bottles and food trays. LDPE (low-density polyethylene) is similar. PVC (polyvinyl chloride) is lower (1% vs 3%). Overall polyolefin content (LDPE+HDPE+PP) = 62% vs 64% in OMR — comparable.

---

# PART 2 — WHAT COMES OUT: Pyrolysis Yields

*Applying the same per-material yields as Annex 5 (Section 10) to the airport feedstock.*

---

## 8. WEIGHTED YIELD CALCULATION

### 8.1 Plastic-Like Fraction (200 kg)

| Material | Mass (kg) | Oil yield | Oil (kg) | Off-gas (kg) | Residue (kg) | Data quality |
|----------|----------|----------|---------|-------------|-------------|-------------|
| LDPE | 70 | 77% | 53.9 | 15.4 | 0.7 | [FACT] FACT |
| PET | 50 | 45% | 22.5 | 8.5 | 19.0 | [HYPOTHESIS] HYPOTHESIS |
| PP | 40 | 80% | 32.0 | 7.2 | 0.8 | [FACT] FACT |
| PS/EPS | 16 | 58% | 9.3 | 2.2 | 4.5 | [FACT] FACT |
| HDPE | 14 | 77% | 10.8 | 3.1 | 0.1 | [FACT] FACT |
| PVC | 2 | 32% | 0.6 | 0.04 | 0.3 | [HYPOTHESIS] HYPOTHESIS |
| PVC HCl | — | — | — | 1.1 | — | Stoichiometric |
| Other | 8 | 25% | 2.0 | 2.0 | 4.0 | [HYPOTHESIS] HYPOTHESIS |
| **SUBTOTAL** | **200** | | **131.1** | **38.3** | **29.4** | |
| **Mass check** | | | 131.1 + 38.3 + 29.4 + 1.1 = **199.9** ≈ 200 | | |
| **Weighted oil yield** | | **65.6%** | (131.1 / 200) | | | |

### 8.2 Organic + Cellulose Fraction (610.5 kg)

| Material | Mass (kg) | Oil yield | Oil (kg) | Off-gas (kg) | Residue (kg) | Data quality |
|----------|----------|----------|---------|-------------|-------------|-------------|
| Cellulose (paper, card, wood) | 350.5 | 12% | 42.1 | 70.1 | 238.3 | [HYPOTHESIS] HYPOTHESIS |
| Food waste (organic) | 260 | 10% | 26.0 | 52.0 | 182.0 | [HYPOTHESIS] HYPOTHESIS |
| **SUBTOTAL** | **610.5** | | **68.1** | **122.1** | **420.3** | |

### 8.3 TOTAL OUTPUT — 810.5 kg Entering Reactor

| Product | From plastic | From organic/cellulose | **TOTAL** | **% of 810.5 kg** |
|---------|-------------|----------------------|----------|-----------------|
| **Oil** | 131.1 | 68.1 | **199.2** | **24.6%** |
| **Off-gas** | 38.3 | 122.1 | **160.4** | **19.8%** |
| **Residue/Char** | 29.4 | 420.3 | **449.7** | **55.5%** |
| **HCl (filtered)** | 1.1 | 0 | **1.1** | **0.1%** |

### 8.4 Comparison with French OMR (Annex 5)

| Product | French OMR | CDG Airport | Difference |
|---------|-----------|-------------|------------|
| Oil (% of reactor input) | 23.0% | **24.6%** | +1.6 pp |
| Oil (kg per 1,000 kg raw waste) | 204.7 | **199.2** | -5.5 kg |
| Off-gas | 19.2% | **19.8%** | +0.6 pp |
| Char/residue | 57.5% | **55.5%** | -2.0 pp |
| Plastic oil yield (weighted) | 65.1% | **65.6%** | +0.5 pp |

**Key finding:** The oil yield per kg of reactor input is slightly higher for CDG waste (24.6% vs 23.0%), but the oil yield per tonne of raw waste is slightly lower (199.2 vs 204.7 kg) because more material is removed in pre-sorting (189.5 vs 109.5 kg). The net result: **airport waste produces roughly the same amount of oil per tonne of raw waste as OMR, but with cleaner pre-sorted recyclable by-products (glass, metals) that have independent value.**

---

## 9. ENERGY BALANCE AND CHAR ENERGY VALUE

Using the same methodology as Annex 5 §13:

| Parameter | Per 1,000 kg raw CDG waste | Per day (140 T) |
|-----------|---------------------------|-----------------|
| Combustible char | 449.7 kg | 62,958 kg (63.0 T) |
| Char energy (at 15.6 MJ/kg weighted) | 7,013 MJ | 981,866 MJ |
| Off-gas energy | ~405 MJ (plastic) + ~122 MJ (organic) = ~527 MJ | 73,780 MJ |
| **Total available energy** | 7,540 MJ | **1,055,646 MJ** |
| Heating demand | 2,714 MJ | 379,960 MJ |
| **Coverage** | | **278%** |

**Char energy value:** The system produces ~2.8x its energy needs from char and off-gas. Under the V2 model, this char is sold commercially to fuel buyers rather than used for reactor heating, demonstrating the fuel-grade quality of the pyrolysis char. The 278% coverage illustrates the high energy density and commercial value of the char product.

---

## 10. FINANCIAL IMPACT — CDG vs OMR

At 140 T/day throughput (steady state, Year 3):

| Revenue stream | OMR (Annex 5) | CDG Airport | Note |
|---------------|--------------|-------------|------|
| Oil volume (L/year, full capacity) | 12.56M | 12.19M | Slightly less due to higher pre-sort removal |
| Oil revenue (€0.55/L) | €6.9M | €6.7M | |
| Gate fee (€/T) | €110 | **€130–150** | Airport waste commands premium: biosecurity compliance, consistency, single-source |
| Gate fee revenue | €5.1M | **€6.0–6.9M** | Higher gate fee compensates lower oil volume |
| Metal revenue (€300/T) | €0.7M | **€0.9M** | More metal in airport waste (6.3% vs 5%) |
| Char revenue (V2 — all char sold) | €1.7M | €1.5M | Slightly less char surplus |
| Carbon credits | €2.5M | €2.5M | Similar |
| Glass revenue (€25/T) | €0.06M | **€0.1M** | More glass at airport |
| **TOTAL REVENUE** | **€17.0M** | **€17.7–18.6M** | |

**The CDG advantage is primarily in gate fees, not oil yield.** Airport waste commands a premium because it solves a regulatory problem (ICW/CAT1 disposal) and offers consistent volume from a single counterparty (Groupe ADP / Paprec).

---

## 11. REGULATORY PATHWAY — INTERNATIONAL CATERING WASTE

### 11.1 Current Regulation

EU Regulation 1069/2009 classifies international catering waste (ICW) as **Category 1 animal by-product**. Permitted disposal methods:

- Incineration in approved plant
- Pressure sterilisation (133°C, 3 bar, 20 min) followed by incineration or landfill
- Deep burial in authorised landfill

### 11.2 Pyrolysis as Compliant Treatment

Pyrolysis at 400–600°C exceeds the thermal destruction requirements of Regulation 1069/2009. The Urban Rig operates at temperatures that would completely destroy any biological agents of concern (prions are destroyed above 600°C under prolonged exposure; bacteria and viruses are eliminated well below 400°C).

**However:** Pyrolysis is not explicitly listed as an approved method in the current regulation. Regulatory approval would require a petition to the competent authority (in France: DGAL — General Directorate for Food (General Directorate for Food)) demonstrating equivalent biosecurity. IATA has been lobbying for regulatory reform since 2018, with a joint statement in 2022 calling for smarter ICW regulation.

### 11.3 Practical Approach

Two pathways:

1. **Immediate:** Process only domestic/intra-EU cabin waste + terminal + cargo + office waste (no ICW). This represents ~60–70% of total CDG waste and avoids the CAT1 regulatory constraint entirely.

2. **Medium-term:** Seek DGAL approval for pyrolysis as equivalent thermal treatment for ICW. The thermal destruction argument is strong (>400°C vs required 133°C), but regulatory processes take 12–24 months.

---

## 12. DATA QUALITY SUMMARY

| Parameter | Classification | Confidence |
|-----------|---------------|------------|
| CDG total waste (~35,000 T/year) | [HYPOTHESIS] ASSUMPTION | MEDIUM — derived from Groupe ADP total |
| Stream percentages (S1-S5) | [HYPOTHESIS] ASSUMPTION | MEDIUM — airport waste literature, not CDG-specific |
| Terminal waste composition (S1) | [HYPOTHESIS] HYPOTHESIS | MEDIUM — Istanbul Airport study + adaptation |
| Cabin waste composition (S2) | [FACT] FACT | HIGH — LIFE Zero Cabin Waste project (145 flights) |
| Cargo waste composition (S3) | [HYPOTHESIS] ASSUMPTION | MEDIUM — packaging industry data |
| Office waste composition (S4) | [HYPOTHESIS] HYPOTHESIS | MEDIUM — Istanbul Airport study |
| Plastic polymer mix | [HYPOTHESIS] ASSUMPTION | MEDIUM — European packaging composition |
| Pyrolysis yields | Per Annex 5 | See Annex 5 §16 |

---

## 13. RECOMMENDATIONS

1. **CDG waste is viable pyrolysis feedstock** with comparable oil yield to MSW (~24.6% vs 23.0% of reactor input) and significantly higher gate fee potential (€130–150/T vs €110/T).

2. **The cargo zone (S3) is the single most attractive stream** — clean, dry, plastic/cellulose-rich, with minimal contamination. Isolating this stream alone (~8,750 T/year estimated) would provide high-yield feedstock at relatively low sorting cost.

3. **Gate fee premium is the primary financial advantage**, not yield. Airport waste commands €20–40/T above municipal rates due to regulatory compliance (International Catering Waste), single-source convenience, and waste consistency.

4. **International catering waste (Category 1 animal by-product) requires regulatory clearance** before processing. Recommend starting with non-ICW streams while pursuing DGAL (General Directorate for Food) approval for pyrolysis as equivalent thermal treatment.

5. **A CDG-specific waste characterization study is critical.** All composition data in this annex is derived from non-CDG sources (Istanbul, Madrid, Schiphol, general literature). A 2-week audit with Paprec cooperation would provide CDG-specific data and dramatically increase confidence in the financial projections.

6. **The metal and glass pre-sort yield at CDG is higher than MSW (Municipal Solid Waste)** (6.3% + 4.4% = 10.7% vs 5% + 5% = 10% for MSW), providing additional recyclable revenue streams.

---

## 14. SOURCES

| # | Source | Used for |
|---|--------|----------|
| 1 | Groupe ADP traffic figures (parisaeroport.fr, Feb 2025) | CDG passenger numbers |
| 2 | Paprec Solutions — [Behind the Scenes at Paris Airports (Behind the Scenes at Paris Airports)](https://www.mypaprecsolutions.com/paprec-aerport-paris/) | Waste tonnage, contractor info, energy recovery rates |
| 3 | Industrial News (Industrial News) — [Paprec wins waste management contract for all Paris Airports (Paprec wins waste management contract for all Paris Airports)](https://www.usinenouvelle.com/article/paprec-decroche-la-gestion-des-dechets-de-l-ensemble-des-aeroports-de-paris.N341740) (2015) | Paprec contract details |
| 4 | Ozbay & Gokceviz (2021) — Towards zero-waste airports: Istanbul Airport. *J. Material Cycles and Waste Management* (PMC8527968) | Terminal/office waste composition, waste per passenger |
| 5 | van der Tuin-Rademaker et al. (2024) — Transforming waste management methods: Dutch Airport. *Frontiers in Sustainability* (10.3389/frsus.2024.1356041) | Schiphol BCAM methodology, priority streams |
| 6 | LIFE Zero Cabin Waste project (EU LIFE15 ENV/ES/000209) — Iberia/Madrid Barajas | Cabin waste composition (organic 54%, plastic 14.2%, etc.) |
| 7 | IATA/ASF Cabin Waste Composition Audits (2024) | 0.94 kg/pax average, 25 flights at Changi |
| 8 | IATA — International Catering Waste: A Case for Smarter Regulation (2018) | CAT1 classification, regulatory framework |
| 9 | IATA — Sustainable Cabin fact sheet (Dec 2025) | 3.6M tonnes global cabin waste, plastic 17–20% |
| 10 | IATA — Joint Statement on Smarter Regulation of ICW (Aug 2022) | Regulatory reform advocacy |
| 11 | EU Regulation 1069/2009 — Animal by-products | CAT1 classification of international catering waste |
| 12 | ICAO — Waste Management at Airports toolkit | Airport waste categories and best practices |
| 13 | Annex 5 — MSW Feedstock Composition and Expected Yield Model | Per-material pyrolysis yields, OMR comparison |

---

**End of Annex 6**
