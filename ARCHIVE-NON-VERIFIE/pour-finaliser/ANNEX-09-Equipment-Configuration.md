# Annex 9 — Equipment Configuration and Sorting Requirements

**Purpose:** Product catalogue of all Urban Rig models, additional pre-processing and post-processing equipment available, and a configuration matrix mapping each deployment sector to its required equipment package and associated CAPEX implications. This annex supports the sector-specific scenario economics in Annexes 10--13.

**Date:** March 2026

---

## 9.1 Urban Rig Product Catalogue

### 9.1.1 Full Product Range

Urban Rig offers seven models spanning batch, continuous, and mobile configurations (Urban Rig Recycling Solutions ENG, pp. 4--5):

| Model | Type | Capacity | Zones | Target Application |
|-------|------|---------|-------|-------------------|
| **URC-2000** | Continuous | 200 T/day | 7-stage | Municipal and industrial scale |
| **URC-1000** | Continuous | 100 T/day | 4-stage | Mid-scale municipal |
| **URC-400** | Continuous | 40 T/day | — | Small municipal / industrial |
| **URC-150** | Continuous | 15 T/day | 7-stage | Small-scale / remote |
| **URB-50** | Batch | 5 T/batch | — | Pilot / demonstration |
| **URB-10** | Batch | 1 T/batch | — | Laboratory / R\&D |
| **URT-10** | Truck-mounted | 1 T/batch | — | Mobile / emergency deployment |

*Source: Urban Rig Recycling Solutions ENG, pp. 4--5; OneWorld Corporation product documentation.*

### 9.1.2 URC-2000 — Reference Model

The URC-2000 is the primary model for commercial deployment and the basis for all financial projections in this business plan.

| Parameter | Value | Source |
|-----------|-------|--------|
| Volumetric capacity | 200 T/day | UR2000-JP, p. 4 |
| Effective throughput (at 0.7 T/m$^3$) | 140 T/day | Lufthansa worksheet |
| Annual throughput (330 operating days) | 46,200 T/year | Financial model |
| Dimensions | W: 66 m × D: 7 m × H: 7 m | Urban Rig Recycling Solutions ENG, pp. 6--7 |
| Building requirement | 4,650 m$^2$ total (3,000 m$^2$ processing) | Urban Rig Recycling Solutions ENG, p. 7 |
| Oil storage | 5 T × 8 tanks | Urban Rig Recycling Solutions ENG, p. 7 |
| Reactor temperature | MAX 600°C normal, 0.2 MPa | Urban Rig Recycling Solutions ENG, p. 7 |
| Fuel consumption | 10,000 L/day light oil | UR2000-JP, p. 4; Lufthansa worksheet |
| Electricity | 600 kW continuous | UR2000-JP, p. 4 |
| Personnel | ~15 FTE | Urban Rig Recycling Solutions ENG, p. 19 |
| Manufacturing lead time | ~10 months | Urban Rig Recycling Solutions ENG, p. 19 |
| All-electric option | 56,800 kWh/day (replaces oil heating) | Fuel/electricity specification sheet |
| **Base equipment price** | **€50.0M** | OneWorld Corporation pricing |

**Scalability:** Each URC-2000 is a self-contained, factory-manufactured module. Multiple units can be co-located: 5 × URC-2000 yields 1,000 T/day capacity on a 28,900 m$^2$ site, sharing building infrastructure and reducing per-unit CAPEX (Urban Rig Recycling Solutions ENG, p. 19).

### 9.1.3 URC-1000 — Mid-Scale Model

| Parameter | Value | Source |
|-----------|-------|--------|
| Capacity | 100 T/day | Urban Rig Recycling Solutions ENG, p. 5 |
| Zones | 4-stage continuous | Urban Rig Recycling Solutions ENG, p. 5 |
| Fuel consumption | 5,500 L/day | Fuel/electricity specification sheet |
| Electricity | 350 kW continuous | Fuel/electricity specification sheet |
| **Estimated price** | **~€30M per unit** | Derived from Hardin LOI: USD 60M for 2 × URC-1000 = USD 30M/unit (Technical Findings Log §16.1) |
| Current status | Two units under construction | OneWorld Corporation |

**Note:** The URC-1000 is relevant for the Korea Phase 1 pilot (see Annex 4 §4B.10) and for markets where 100 T/day is a better fit than 200 T/day.

### 9.1.4 Smaller and Mobile Models

| Model | Capacity | Fuel | Electricity | Lead Time | Application |
|-------|---------|------|------------|----------|------------|
| URC-400 | 40 T/day | 2,200 L/day | 250 kW | ~10 months | Small municipal or industrial |
| URC-150 | 15 T/day | 800 L/batch | 150 kW | ~10 months | Remote or island deployments |
| URB-50 | 5 T/batch | 220 L/batch | 50 kW | ~6 months | Pilot / demonstration |
| URB-10 | 1 T/batch | 120 L/batch | 25 kW | ~6 months | Laboratory |
| URT-10 | 1 T/batch (truck) | 120 L/batch | 25 kW | ~6 months | Emergency / disaster response |

*Source: Fuel/electricity specification sheet; Urban Rig Recycling Solutions ENG, pp. 4--5, 19.*

**Pricing for smaller models** is not publicly confirmed. Scaling logic suggests approximately €8--10M per URC-400 and €3--5M per URC-150, but these are estimates only and should be verified with OneWorld Corporation.

---

## 9.2 Core System Add-Ons

These systems are designed by or for Urban Rig and can be integrated with any continuous model.

### 9.2.1 PRIMO Exhaust Gas Purification (PUREM 30.8)

**Function:** DeNOx (ammonia mist injection), DeSOx, dust removal, and deodorisation — using the same technology standard as thermal power plants (Urban Rig Recycling Solutions ENG, p. 12).

| Parameter | Detail |
|-----------|--------|
| Applicable models | URC-2000, URC-1000, URC-400, URC-150 (Type 6) |
| Purpose | Achieve near-zero atmospheric impact in sensitive environments (urban, airport) |
| When required | Deployments near residential areas; ICPE permitting with enhanced emission targets |
| Estimated CAPEX | €500k--1.5M (to be confirmed with OneWorld) |

**Note:** Base UR emissions are already 5--50× below French incineration limits (KANSO Technos — see Annex 2 §2.7). The PRIMO system is optional for sites requiring an additional margin of safety or where permitting conditions demand best-available-technology (BAT) for air quality.

### 9.2.2 SEA CORAL Water Purification

**Function:** Ceramic purification system using sea coral as catalyst and absorbent with vaporisation heat. Purifies process water, extracting pure water free of minerals including arsenic. Enables closed-loop water management — zero wastewater discharge (Urban Rig Recycling Solutions ENG, p. 13).

| Parameter | Detail |
|-----------|--------|
| Applicable models | All continuous models |
| Purpose | Closed-loop water cycle, zero liquid discharge |
| When required | All deployments (integrated water management for ICPE compliance) |
| Estimated CAPEX | Included in base package for URC-2000 (€50M) — confirm with OneWorld |

### 9.2.3 FORCE 9 (FIA CR-09) Char Stabilisation

**Function:** Far-infrared catalytic reduction for char stabilisation. Converts heavy metals in char to stable, non-water-dissolved sulphur compounds at ~400°C. Patented technology (Urban Rig Recycling Solutions ENG, pp. 10--11).

| Parameter | Detail |
|-----------|--------|
| Purpose | Ensures char output is environmentally safe for soil application or sale as fuel |
| When required | All deployments where char is sold as biochar (Tier 4--5 markets — see Annex 3 §3.2.2) |
| Estimated CAPEX | Included in base package — confirm with OneWorld |

---

## 9.3 Pre-Processing Equipment

Pre-processing equipment is required between waste reception and reactor input to remove non-processable materials and size-reduce the feedstock. Requirements vary by sector.

### 9.3.1 Mechanical Pre-Sorting Line

| Component | Function | When Required |
|-----------|----------|--------------|
| Trommel screen | Size classification, removal of oversized items | All MSW and mixed-waste deployments |
| Magnetic separator | Ferrous metal extraction (steel cans, nails, wire) | All deployments |
| Eddy-current separator | Non-ferrous metal extraction (aluminium, copper) | All deployments |
| Optical sorter (NIR) | Identification and removal of glass, specific contaminants | Optional — for high-contamination feedstocks |
| Ballistic separator | Separation of 2D (films) from 3D (containers) | Optional — for mixed packaging streams |
| Manual sorting station | Quality control, hazardous item removal | Recommended for all deployments |

**Estimated CAPEX for complete pre-sorting line:** €2--5M depending on throughput capacity and automation level. This is included in the "Building and site preparation" line of the financial model (€5M for France deployment).

### 9.3.2 Size Reduction

| Component | Function | When Required |
|-----------|----------|--------------|
| Primary shredder | Reduce waste to <300 mm | All deployments |
| Secondary shredder/granulator | Further reduction to <50 mm for reactor input | May be required for bulky or rigid waste streams |

**Note:** The URC-2000 reactor bucket is 1.5 m × 3 m × 1 m (4.5 m$^3$). Size reduction to <300 mm is sufficient for most feedstocks. The Urban Rig Recycling Solutions ENG brochure states the system accepts waste "without requiring pre-sorting or cleaning beyond basic size reduction and inert removal" (p. 6).

---

## 9.4 Post-Processing Equipment

### 9.4.1 Oil Storage and Handling

The base URC-2000 package includes 8 × 5T oil storage tanks (Urban Rig Recycling Solutions ENG, p. 7). Additional storage may be required for:

- **Separate fraction storage:** 3 tank banks (light oil, gas oil, heavy oil) to preserve price differentiation (see Annex 3 §3.1.6)
- **Tanker loading facility:** For oil dispatch to buyers

**Estimated additional CAPEX:** €200k--500k for expanded tank farm and loading.

### 9.4.2 Char Pelletisation

Required if char is sold as industrial fuel pellets (Tier 2) or charcoal briquettes (Tier 3) rather than loose material:

| Parameter | Detail |
|-----------|--------|
| Purpose | Compress char into pellets/briquettes for handling and sale |
| Throughput required | ~67 T/day (all combustible char output) |
| Estimated CAPEX | €200k--500k per unit |

*Source: Annex 5 §13.6.*

### 9.4.3 Char Combustion System

**No longer required in V2 model:** The updated V2 configuration uses purchased heating oil for all reactor heating. All char output is sold, eliminating the need for a char combustion system. This removes the associated CAPEX of €500k--1M.

---

## 9.5 Sector-Specific Configuration Matrix

The following matrix maps each deployment sector (Annexes 5--8) to its required equipment package. "Base" means included in the €50M URC-2000 package. "Add" means additional CAPEX.

| Equipment | MSW (Annex 5) | CDG Airport (Annex 6) | Industrial (Annex 7) | Plastic Rejects (Annex 8) |
|-----------|:---:|:---:|:---:|:---:|
| **Core reactor (URC-2000)** | Base | Base | Base | Base |
| **PRIMO exhaust (PUREM)** | Optional | Recommended | Optional | Optional |
| **SEA CORAL water** | Base | Base | Base | Base |
| **FORCE 9 char stabilisation** | Base | Base | Base | Base |
| **Trommel screen** | Add | Add | Add | Not needed |
| **Magnetic separator** | Add | Add | Add | Add (minimal) |
| **Eddy-current separator** | Add | Add | Add | Not needed |
| **Optical sorter (NIR)** | Optional | Optional | Optional | Not needed |
| **Primary shredder** | Add | Add | Add | Add |
| **Secondary shredder** | Optional | Optional | Optional | Optional |
| **Manual sorting station** | Add | Add | Add | Optional |
| **Expanded oil tank farm** | Add | Add | Add | Add |
| **Char pelletiser** | Add | Add | Add | Not needed |

### 9.5.1 Estimated CAPEX by Sector

| CAPEX Component | MSW | CDG Airport | Industrial | Plastic Rejects |
|----------------|-----|-------------|-----------|----------------|
| URC-2000 base package | €50.0M | €50.0M | €50.0M | €50.0M |
| Building and site preparation | €5.0M | €5.0M | €5.0M | €3.0M |
| Pre-sorting line | €3.0M | €3.5M | €2.5M | €1.0M |
| PRIMO (if selected) | — | €1.0M | — | — |
| Char pelletiser | €0.3M | €0.3M | €0.3M | — |
| Oil storage expansion | €0.3M | €0.3M | €0.3M | €0.3M |
| Installation, freight, training | €0.9M | €0.9M | €0.9M | €0.9M |
| Accessories, spares, monitoring | €2.0M | €2.0M | €2.0M | €2.0M |
| Contingency (5%) | €2.5M | €2.6M | €2.5M | €2.9M |
| **TOTAL CAPEX** | **€64.6M** | **€66.2M** | **€64.1M** | **€60.1M** |

**Notes:**

- The current financial model uses €60.8M CAPEX (UR-Financial-Model-General.xlsx, CAPEX sheet). The sector-specific estimates above show that MSW and CDG deployments may require €65--67M when pre-sorting, char combustion, and PRIMO are included. This should be reflected in the scenario economics (Annexes 10--13).
- Plastic sorting rejects require minimal pre-processing (material is already sorted and baled) — CAPEX is correspondingly lower.
- Building costs for Korea are €6M (higher land prices — see Annex 4 §4B).

---

## 9.6 Recommendations

1. **Confirm pricing for PRIMO, SEA CORAL, and FORCE 9** with OneWorld Corporation — specifically whether these are included in the €50M base package or are additional items.
2. **Obtain firm quotes for pre-sorting equipment** from European MRF equipment suppliers (TOMRA, Pellenc ST, Machinex) for integration with the site design.
3. **Request URC-1000 and URC-400 pricing** from OneWorld for Korea Phase 1 and smaller-market deployments.
4. **Consider pre-sorting as a CAPEX line item in all sector models** — the current financial model bundles it into "Building and site preparation" (€5M), which may be insufficient for MSW and airport deployments requiring a full MRF-style line.

---

## 9.7 References

**Urban Rig Technical Sources**

1. **Urban Rig Recycling Solutions ENG** — OneWorld Corporation product brochure (English edition). Cited for: full product range (pp. 4–5), URC-2000 dimensions and specifications (pp. 6–7), oil storage (p. 7), reactor temperature and pressure (p. 7), PRIMO exhaust system (p. 12), SEA CORAL water purification (p. 13), FORCE 9 char stabilisation (pp. 10–11), automation (p. 17), personnel and lead time (p. 19), multi-unit scalability (p. 19).
2. **UR2000-JP** — URC-2000 technical specification sheet (Japanese edition). Cited for: volumetric capacity 200 T/day, fuel consumption, electricity (p. 4).
3. **Fuel/electricity specification sheet** — OneWorld Corporation. Cited for: fuel and electricity consumption across all models, all-electric option 56,800 kWh/day (§9.1.2, §9.1.4).
4. **OneWorld Corporation** — Product pricing and documentation. Cited for: URC-2000 base price €50M, URC-1000 current status (§9.1.2, §9.1.3).

**Financial and Operational Sources**

5. **Lufthansa worksheet** — Operational assumptions. Cited for: effective throughput at 0.7 T/m³ density (§9.1.2).
6. **Hardin LOI** — Letter of Intent for 2 × URC-1000 at USD 60M. Via Technical Findings Log §16.1. Cited for: URC-1000 estimated price ~€30M/unit (§9.1.3).
7. **UR-Financial-Model-General.xlsx** — Working financial model (CAPEX sheet). Cited for: current model CAPEX of €60.8M (§9.5.1, Notes).

**Cross-Referenced Annexes**

8. **Annex 2 §2.6.3** — Energy balance derivation. Cited for: V2 char sales model with purchased heating oil supply (§9.4.3).
9. **Annex 2 §2.7** — KANSO Technos emission data. Cited for: base emissions 5–50× below French incineration limits (§9.2.1).
10. **Annex 3 §3.1.6** — Oil fraction storage recommendation. Cited for: separate tank banks (§9.4.1).
11. **Annex 3 §3.2.2** — Biochar market tiers. Cited for: char as fuel or biochar (§9.2.3).
12. **Annex 4 §4B** — Korea country study. Cited for: Korea building costs €6M, Phase 1 pilot with URC-1000 (§9.5.1, Notes).
13. **Annex 5 §13.6** — Char pelletisation. Cited for: pelletiser CAPEX reference (§9.4.2).
14. **Annexes 5–8** — Sector-specific feedstock profiles. Cited for: sector configuration requirements (§9.5).

---

**End of Annex 9**
