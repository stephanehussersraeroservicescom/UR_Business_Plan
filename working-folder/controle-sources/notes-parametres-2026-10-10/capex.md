# Urban Rig: sourcing the CAPEX parameters (URC-2000, 1 unit, 200 t/day)

- **Date of research:** 2026-10-10 (WebSearch + WebFetch only; 30 searches used).
- **Registry:** every source ID below (`PRM-...`) has an entry in `capex.yaml` with its URL, location, values and verbatim quote.
- **Model reference values (internal, not external evidence):**
  - Machine price: 50 MEUR (OneWorld quotation; `claude/etat-existant-2026-10-10.md` §5.4).
  - Total CAPEX: 64.06 MEUR (V5/V7; `claude/rapprochement-modeles-2026-10-10.md` §2).
  - Building per URC-2000: 4,650 m² (business plan §3.10).
  - Throughput: 200 t/day ÷ 24 h = 8.33 t/h.
- **Conventions:**
  - **E** = purchased-equipment cost.
  - Installation multipliers come from Peters & Timmerhaus (P&T) as reproduced in `PRM-OU-CHEDESIGN-COSTEST`:
    - installation alone: 22–55 % of E, so the multiplier is ×1.22 to ×1.55;
    - "fluid plant" Table 17: installation 47 % + instrumentation 18 % + electrical 11 % = ×1.76. I use this as the upper multiplier because the solids-plant column was not retrieved.
  - USD figures are **not converted**: no exchange-rate source was read in this batch.

> **Main caveat.** No source found gives a complete, turnkey price for a 6–9 t/h mixed-waste pre-sorting line or a 1–2 t/h char post-sorting line. The figures below are unit prices from public tenders, marketplace listings and a B2B price guide. I combine them with textbook installation factors. Marketplace prices are offers, not transactions, so they are labelled *secondaire*.

---

## 1. `pre_tri` = 1,080,000 EUR (bag opener + trommel + magnet + conveyors, 6–9 t/h)

### Evidence read

| ID | What it says | Year | Notes |
|---|---|---|---|
| PRM-BOAMP-SMTD65-TROMMEL-2024 | Mobile trommel on 80 km/h chassis **+ 4-year maintenance contract**, awarded to LHEUREUX: **214,000 EUR** ("Valeur de tous les contrats attribués dans cet avis : 214,000 Euro") | 2024 | French public award; HT/TTC not stated; capacity not stated |
| PRM-HELLOPRO-MACHINES-CDT-2026 | Trommel "Entre 50 000 et 150 000 euros" (up to 50 t/h); magnetic separator "À partir de 30 000 euros"; conveyors "À partir de 10 000 euros selon la longueur"; complete line "Au moins 500 000 euros pour une ligne automatique de tri de déchets" | Oct 2026 | B2B marketplace guide (secondary); no price for bag opener |
| PRM-TTG-DOPPSTADT-SM720-2026 | Doppstadt SM 720.2 (2025, 7 h) mobile trommel: **USD 329,000** | 2026 listing | US market, mobile diesel unit |
| PRM-BOOMBUCKET-DOPPSTADT-SM720K-2026 | Doppstadt SM720.2K (2023, 579 h): **USD 349,500** (no longer available) | 2026 listing | US market |
| PRM-MACHINESEEKER-PUTZ-OVERBAND-2026 | New Putz overband, 750 mm belt: **EUR 5,350 + VAT** EXW | 2025 unit | Small permanent overband (lower bound) |
| PRM-MACHINESEEKER-TROMMEL-2026, PRM-WERKTUIGEN-KOMPTECH-MUSTANG-2026 | Trommel listings in DE/PL/IT/SK/UK, including a static Komptech Mustang (5.5 m × 2.0 m drum) | 2026 | **No prices displayed** |
| PRM-MACHINESEEKER-BAGOPENER-2026 | No waste bag-opener listing; only powder big-bag stations | 2026 | **No bag-opener price found** |
| PRM-BAUDELET-CSR-2026 | New CSR line at Blaringhem: **8.5 MEUR**. Target 75,000 t/yr of CSR from 100,000 t/yr of waste (existing line: 25,000 t/yr) | 2026 | Full CSR line including shredding, so a much wider scope (upper bound only) |
| PRM-SIREDOM-CITD-2021 | Packaging line, 14 t/h, 55,000 t/yr, 2 trommels + 12 optical sorters | 2021 | No investment amount |
| PRM-CITEO-SEPUR-SURTRI-2025, PRM-PAPREC-RICHWILLER-2021 | MRF / re-sorting centres: 70 MEUR for 4 centres (100 kt/yr); 20 MEUR for 45 kt/yr | 2025 / 2021 | MRF scope; **not applicable** (consistent with the project's earlier decision) |
| PRM-BOAMP-SAVOIEDECHETS-CONVOYEURS-2025 | Multi-site, multi-year conveyor supply and maintenance: estimated 2.0 MEUR HT | 2025 | No unit price |

### Computation from the sourced inputs

- **Number of trommels.** The model note says 6 t/h per machine. At 8.33 t/h this gives 2 trommels. If pre-sorting runs fewer than 24 h/day the number rises; that operating assumption is not sourced.
- **Purchased equipment for the priced items (E):**
  - Low: 2 × 150,000 (Hellopro top of range) + 30,000 (magnet, Hellopro floor) = **330,000 EUR**.
  - High: 2 × 214,000 (SMTD 65 award) + 30,000 = **458,000 EUR**.
- **Installed cost:**
  - Low: 330,000 × 1.22 = **402,600 EUR**.
  - High: 458,000 × 1.76 = **806,080 EUR**.
- **Remainder for bag opener and conveyors.** The 1,080,000 EUR budget leaves **273,920 to 677,400 EUR** for these two items, which have no price source. Each conveyor costs ≥ 10,000 EUR E, i.e. ≥ 12,200 to 17,600 EUR installed.
- **Floor check.** Hellopro gives "≥ 500,000 EUR" for a complete automatic line, so 1.08 MEUR is above that floor.

**Verdict: no source found for the full scope.** The current value is compatible with the partial bottom-up above, which covers trommels and a magnet. The bag opener and the conveyor count/length remain unsourced. To close the gap, get an OEM budget quote for a bag opener plus 2 stationary trommels at 6 t/h (Komptech, Doppstadt or Terex).

---

## 2. `post_tri` = 430,000 EUR (overband + eddy-current separator + screen + conveyors, 1–2 t/h)

### Evidence read

| ID | What it says | Year |
|---|---|---|
| PRM-MACHINESEEKER-ECS-2026 | Eddy-current separators, ~1,000 mm wide: "€46,000 FCA ONO plus VAT" (BAS, new, TR); "€52,000 ONO plus VAT" (SGM EIS 1000 S, CZ); "€74,800 Fixed price VAT not applicable" (Scrappers WPS-1000 + set, new, PL); "€11,000" (Wagner Magnete, HU, old/small) | 2026 |
| PRM-GOUDSMIT-EDDYXPERT-2026 | Goudsmit EddyXpert 1,500 mm product page: **price fields empty** | 2026 |
| PRM-MACHINESEEKER-PUTZ-OVERBAND-2026 | Overband 750 mm: 5,350 EUR + VAT | 2025 |
| PRM-HELLOPRO-MACHINES-CDT-2026 | Magnetic separator "À partir de 30 000 euros"; conveyors from 10,000 EUR | 2026 |
| PRM-MACHINESEEKER-REMAV-RS1500-2026 | Rotary drum screen Remav RS1500: "€38,900", fixed price + VAT | 2026 |
| PRM-WERKTUIGEN-SCREENBEE-2026 | Static trommel Screenbee 13.26 S (2 m × 1.2 m): "€38,000", EXW + VAT | 2026 |
| PRM-ASTON-PYRO-TROMMELFINES-SI | "Sieve machine" GBP 25,000 at 200–2,000 kg/h, "Estimate provided by commercial supplier" | year n/a |

### Computation

- **Purchased equipment (E):**
  - Low: ECS 46,000 + overband 5,350 + screen 38,000 = **89,350 EUR**.
  - High: 74,800 + 30,000 + 38,900 = **143,700 EUR**.
- **Installed cost:**
  - Low: 89,350 × 1.22 = **109,007 EUR**.
  - High: 143,700 × 1.76 = **252,912 EUR**.
- **What it would take to reach 430,000 EUR.** On top of the high case you need another 177,088 EUR. At the conveyor floor that is about 10 conveyors at 17,600 EUR installed each, which is a lot for a 1–2 t/h line.

**Verdict: outside range (high).** The model is about 1.7× the high end of the sourced bottom-up (0.11–0.25 MEUR plus conveyors). Two things could justify the gap, but neither is sourced: dust-tight enclosed conveyors for char (char dust is combustible) and support structures. Next step: get one OEM budget quote for a char line (ECS + overband + screen).

---

## 3. `atex` = 650,000 EUR (ATEX compliance + dust extraction)

### Evidence read

| ID | What it says | Year |
|---|---|---|
| PRM-HELLOPRO-DEPOUSSIEREUR-2026 | ATEX dust collector "entre 15 000 € et 80 000 €"; centralised collector 15–80 kEUR; extraction ductwork 2–25 kEUR; technical study 0.5–5 kEUR; commissioning 0.5–3 kEUR | Oct 2026 (secondary) |
| PRM-CELOSIA-DDAE-VENTILATION-2024 | Comparable French CSR plant (PRAXY, Allier). General extraction: 40,000 + 40,000 + 22,000 m³/h. Point dust extraction by independent modules at 4 points (shredder outlet, trommel inlet, optical-sorter inlet, granulator inlet). Fan "protégé CAT 3D", "moteur zone 22". **No costs** | 2024 |
| PRM-INRS-COUSIN-ATEX-2020 | INRS ATEX day: explosion containment > 10 bar, minimum explosive concentration 30 g/m³. **No costs** | 2020 |

### Computation (dust extraction only, using the Celosia point count)

- Low: 4 × (15,000 + 2,000) + 500 + 500 = **69,000 EUR**.
- High: 4 × (80,000 + 25,000) + 5,000 + 3,000 = **428,000 EUR**.

This excludes the following, for which no source was found:
- ATEX-rated electrical equipment;
- gas detection and explosion isolation around the pyrolysis-gas zones;
- the ATEX zoning study / DRPCE.

**Verdict: no source found for the 650,000 EUR total.** The dust-extraction part computed from secondary prices is 0.07–0.43 MEUR. Needed: a vendor quote, or an ATEX design-office estimate based on the zoning plan.

---

## 4. `vrd_par_unite` = 400,000 EUR (site works per additional unit)

### Evidence read

| ID | What it says | Year |
|---|---|---|
| PRM-COTENTIN-QUAI-TRANSFERT-2024 | Lot 1 "Terrassements / VRD / Clôture / Portail / Espaces verts" for a waste transfer station: **1,270,961.24 EUR HT**, firm tranche (variant including confinement of spoil). Surfaces not given | 2024 |
| PRM-BOAMP-SITREVA-DREUX-2024 | Lot 1 "Terrassement, VRD et génie civil" (déchèterie + transfer station): estimated **2,695,000 EUR HT** (awarded amount per lot not published) | 2024 |
| PRM-NREL-GRIFFIN-CFP-SI-2024 | "Site Development 10.0%" of ISBL (nth-plant TEA) | 2024 (2016 USD) |
| PRM-ADEME-CDT-CONDITIONS-2022 | VRD is an eligible expense for sorting/preparation centres; no cost ratio | 2022 |

**Verdict: no source found for a per-additional-unit increment.** Available benchmarks are for whole-site VRD lots at small French waste facilities: 1.27–2.70 MEUR HT (2024). Neither gives surfaces, so no €/m² ratio could be derived. The Mercuriales note from the Réseau national des aménageurs was offline.

---

## 5. `ingenierie_base` = 750,000 EUR and `ingenierie_step` = 20 %

### Evidence read

| ID | What it says | Year |
|---|---|---|
| PRM-NETL-QGESS-COST-2021 | "The EPCM contractor services are estimated at 15 to 20 percent of BEC" (§2.3, p. 12) | 2021 |
| PRM-NREL-GRIFFIN-CFP-SI-2024 | "Home Office & Construction Fees 20.0%" of TDC; "Other Costs (Start-Up & Permits) 10.0%"; "Field Expenses 10.0%" | 2024 |
| PRM-POLIMI-PT-PLANTECON-2015 (P&T 2003) | "Engineering and supervision 4-20" % of FCI; contractor's fee 2–6 %; legal 1–3 % | 2003 ed. |
| PRM-OU-CHEDESIGN-COSTEST | Engineering 4–21 % FCI / 33 % E (fluid) / 5–30 % D | n.d. |
| PRM-EC-SWD2012-354-EIA | "The average EIA costs are estimated at 1% of the total costs of projects or around €41,000 per EIA"; average duration 11.6 months | 2012 (old) |
| PRM-BOAMP-SIECEUTOM-AMO-2024 | Owner's engineer (AMO) for the design-build-operate procurement of a sorting centre: **272,560 EUR** | 2024 |
| PRM-BOAMP-LORIENT-GPM-2025, PRM-BOAMP-VALTOM-AVIS-2026, PRM-BOAMP-VALTOM-RECTIF-2026 | French sorting-centre global contracts include design studies and the ICPE dossier inside the global price (59.0 MEUR HT; 85 MEUR HT estimate). No breakdown | 2025–2026 |
| PRM-DRIEE-EVALENV-2011 | No EIA cost; legacy 1.9 MEUR impact-study threshold | 2011 (old) |

### Computation

- **Against total CAPEX:** 750,000 / 64,060,000 = **1.2 %**.
- **Against the non-OEM part** (64.06 − 50 = 14.06 MEUR, an approximate base that itself includes engineering and contingency): **5.3 %**.
  - P&T 4–20 % of that base gives 0.56–2.81 MEUR.
  - NETL 15–20 % gives 2.11–2.81 MEUR.
  - NREL 20 % gives 2.81 MEUR.
- **Against the balance-of-plant lines in this note** (1.08 + 0.43 + 0.65 + 0.40 + 0.20 = 2.76 MEUR): **27 %**.
- **EIA alone:** the EU 2012 average is ~41 kEUR or ~1 % of project cost; 1 % × 64.06 MEUR = 0.64 MEUR.

**Verdict for `ingenierie_base`:** the outcome depends on the base.
- **Within range** (low end of P&T 4–20 %) if engineering applies only to the non-OEM scope, i.e. the OneWorld 50 MEUR price includes the process engineering. That inclusion must be confirmed in the quotation.
- **Outside range (low)** against NETL/NREL (15–20 %) or if referred to total CAPEX (1.2 %).

**Verdict for `ingenierie_step` (20 %): no source found.** None of the sources read gives an engineering factor for repeat units.

---

## 6. `taux_aleas` = 5 %

### Evidence read

| ID | What it says | Year |
|---|---|---|
| PRM-AACE-18R97-2005 | Class 5 (0–2 % definition): "-20% to -50%" / "+30% to +100%". Class 4 (1–15 %): "-15% to -30%" / "+20% to +50%". Ranges are "after application of contingency (typically at a 50% level of confidence)". No contingency % per class | 2005 (old; read via a 2019 reproduction) |
| PRM-NETL-QGESS-COST-2021 | Process contingency (AACE 16R-90), % of associated process capital: "New concept with limited data 40+"; "Small pilot plant data 20-35"; "Full-sized modules have been operated 5-20"; "Process is used commercially 0-10". Project contingency "15 percent to 30 percent of the sum of BEC, EPC fees, and process contingency" | 2021 |
| PRM-NREL-GRIFFIN-CFP-SI-2024 | "Project Contingency 10.0%" of TDC (nth-plant basis) | 2024 |
| PRM-POLIMI-PT-PLANTECON-2015 / PRM-OU-CHEDESIGN-COSTEST | Contingency 5–15 % of FCI; 10 % of (direct + engineering + construction) | 2003 ed. / n.d. |

**Verdict: outside range (low).** 5 % is the floor of the P&T range, which applies to established processes. It is below NREL's nth-plant 10 % and well below NETL's 15–30 % project contingency for a Class 4/5 estimate. For a first unit in Europe, a sourced figure would be:
- project contingency of ≥ 10–15 % (NREL/NETL), plus
- process contingency of 5–20 % if the URC-2000 counts as "full-sized modules have been operated" (Japan/China references), or 0–10 % if it counts as commercial.

---

## 7. Installation / freight / training / spares as shares of the 50 MEUR machine

| Line | Model | % of 50 MEUR | Sourced benchmark | Source IDs | Verdict |
|---|---|---|---|---|---|
| installation | 200,000 | 0.40 % | Installation 22–55 % of E (47 % fluid plant); 6–14 % of FCI; NREL installation factor 2.2× | PRM-OU-CHEDESIGN-COSTEST, PRM-POLIMI-PT-PLANTECON-2015, PRM-NREL-GRIFFIN-CFP-SI-2024 | **Outside range (low)**, unless the OneWorld price includes erection (to be confirmed in the quotation) |
| fret | 400,000 | 0.80 % | Shipping "approximately equal to 10% of the total equipment cost" (P&T course); CIF-FOB margin, all goods: world 6.2 % (1995–2014), France as importer 4.9 % (2007–2011) | PRM-POLIMI-PT-PLANTECON-2015, PRM-OECD-MIAO-CIFFOB-2017 | **Outside range (low)**. Caveat: these are value-weighted averages over all goods, and high-value, low-mass machinery (7 truckable sections, ~12 t per processing unit per the BP) has a lower freight share. No Japan→EU HS 84 figure was obtained, so a freight-forwarder quote is needed |
| formation | 300,000 | 0.60 % | No training-specific source. NETL pre-production (start-up) = "6 months operating labor" + "2% of TPC", a broader bucket | PRM-NETL-QGESS-COST-2021 | **No source found** (training alone) |
| pieces | 2,000,000 | 4.0 % | NETL inventory capital "0.5% of TPC for spare parts" (0.5 % × 64.06 MEUR = 0.32 MEUR) | PRM-NETL-QGESS-COST-2021 (PRM-HONEYWELL-SPARES-BUDGET not usable) | **Outside range (high)** against the only sourced benchmark; a 2-year operating-spares list from OneWorld would settle it |

---

## 8. Summary table

| Parameter | Current value | Sourced value / range | Source IDs | Verdict |
|---|---|---|---|---|
| pre_tri | 1,080,000 EUR | Partial bottom-up 0.40–0.81 MEUR installed (2 trommels + magnet only); complete-line floor ≥ 0.5 MEUR; full CSR line 8.5 MEUR (wider scope) | PRM-BOAMP-SMTD65-TROMMEL-2024, PRM-HELLOPRO-MACHINES-CDT-2026, PRM-TTG-DOPPSTADT-SM720-2026, PRM-BOOMBUCKET-DOPPSTADT-SM720K-2026, PRM-BAUDELET-CSR-2026, PRM-OU-CHEDESIGN-COSTEST | No source found for full scope (compatible with partial range; bag opener and conveyors unsourced) |
| post_tri | 430,000 EUR | 0.11–0.25 MEUR installed + conveyors (≥ 12–18 kEUR each installed) | PRM-MACHINESEEKER-ECS-2026, PRM-MACHINESEEKER-PUTZ-OVERBAND-2026, PRM-MACHINESEEKER-REMAV-RS1500-2026, PRM-WERKTUIGEN-SCREENBEE-2026, PRM-HELLOPRO-MACHINES-CDT-2026, PRM-OU-CHEDESIGN-COSTEST | Outside range (high) |
| atex | 650,000 EUR | Dust extraction only: 0.07–0.43 MEUR (4 points); ATEX electrical / gas zones not sourced | PRM-HELLOPRO-DEPOUSSIEREUR-2026, PRM-CELOSIA-DDAE-VENTILATION-2024 | No source found |
| vrd_par_unite | 400,000 EUR | Whole-site VRD lots, small waste facilities: 1.27–2.70 MEUR HT (2024); 10 % of ISBL (NREL) | PRM-COTENTIN-QUAI-TRANSFERT-2024, PRM-BOAMP-SITREVA-DREUX-2024, PRM-NREL-GRIFFIN-CFP-SI-2024 | No source found (per-unit increment) |
| ingenierie_base | 750,000 EUR | Engineering 4–20 % FCI (P&T); EPCM 15–20 % BEC (NETL); 20 % TDC + 10 % start-up & permits (NREL); EIA ~1 % / ~41 kEUR (EU 2012); AMO 272.6 kEUR (2024) | PRM-POLIMI-PT-PLANTECON-2015, PRM-NETL-QGESS-COST-2021, PRM-NREL-GRIFFIN-CFP-SI-2024, PRM-EC-SWD2012-354-EIA, PRM-BOAMP-SIECEUTOM-AMO-2024 | Confirmed only on a non-OEM base (5.3 %, within P&T); outside range (low) on total CAPEX (1.2 %) or against NETL/NREL |
| ingenierie_step | 20 % | none | — | No source found |
| taux_aleas | 5 % | 5–15 % FCI (P&T, established); 10 % (NREL nth-plant); 15–30 % project + 5–20 % process (NETL/AACE 16R-90) | PRM-POLIMI-PT-PLANTECON-2015, PRM-NREL-GRIFFIN-CFP-SI-2024, PRM-NETL-QGESS-COST-2021, PRM-AACE-18R97-2005 | Outside range (low) |
| installation | 200,000 EUR (0.4 %) | 22–55 % of E; factor 2.2× | PRM-OU-CHEDESIGN-COSTEST, PRM-NREL-GRIFFIN-CFP-SI-2024 | Outside range (low), unless included in OEM price |
| fret | 400,000 EUR (0.8 %) | 4.9–6.2 % (OECD CIF-FOB, all goods); ~10 % (P&T course) | PRM-OECD-MIAO-CIFFOB-2017, PRM-POLIMI-PT-PLANTECON-2015 | Outside range (low); quote needed |
| formation | 300,000 EUR (0.6 %) | none specific (NETL pre-production 2 % TPC + 6 months labour) | PRM-NETL-QGESS-COST-2021 | No source found |
| pieces | 2,000,000 EUR (4 %) | 0.5 % of TPC (NETL) | PRM-NETL-QGESS-COST-2021 | Outside range (high) |

---

## 9. Pages opened but not usable (not in the registry)

- **OECD ITIC blog, July 2024:** the article body was not retrieved.
  https://www.oecd.org/en/blogs/2024/07/recent-developments-in-international-transport-and-insurance-costs-insights-from-the-OECD-ITIC-database.html
- **TED notices 184901-2023 and 056858-2023:** empty content.
- **efis.psc.mo.gov/Document/Display/84514:** contains no 18R-97 text.
- **canadabuys AACE matrix PDF:** binary, not readable.
- **Réseau national des aménageurs, "Mercuriales" note:** page under maintenance.
- **JRC WT BREF 2018 (aida.ineris.fr, JRC113018_WTbref.pdf):** text truncated after about 108k characters (table of contents and chapters 1–4 only). The relevant "Economics" sections for dust abatement (§3.3.4.1.1, p. 320) were not reached. **This is worth a manual read.**
- **Pages that would not load:**
  - lejournaldesentreprises.com (robots blocked): Tri Ouest 5 MEUR article;
  - Machineseeker overband search pages (fetch error);
  - eBay overband listing (fetch error).

## 10. Next steps that would turn "no source" into "confirmed"

1. **OneWorld quotation.** Confirm whether the 50 MEUR includes erection/installation, process engineering, freight (Incoterm), commissioning, training and the initial spares list. This settles section 7 and the base for `ingenierie_base`.
2. **OEM budget quotes**, which outrank secondary marketplace data under the project's confidence rule (manufacturer data 80–100 %):
   - Komptech / Doppstadt / Terex: bag opener + 2 stationary trommels at 6 t/h;
   - Steinert / Goudsmit / IMRO: char line (ECS + overband + screen).
3. **ATEX design office estimate** based on the zoning plan of the URC-2000 building.
4. **Manual read of WT BREF §3.3.4.1.1 (p. 320) and §3.1.3.1.3.3 (p. 279)** for EU cost data on bag filters and deflagration management.
