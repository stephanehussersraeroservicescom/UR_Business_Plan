# Annex 8. Plastic Waste Streams (France)

This annex describes the plastic waste streams of France, stream by stream: how much exists, how much is really recycled, what happens to the rest, who pays for it today, and which streams could feed an Urban Rig. It covers household and industrial plastics alike, with priority to the streams that are little or not recycled [hyp:D-018]. Residual household waste as a whole is covered by Annex 5, mixed commercial and industrial waste by Annex 7 and the CDG airport by Annex 6. Shredder residues are excluded from the plan [hyp:D-037].

## How to Read This Annex

OneWorld, the manufacturer of the Urban Rig, is the sponsor of this business plan [hyp:D-027]. Its documentation is marked "OneWorld design data"; these are the company's own figures and have not been verified independently.

Each figure or fact is followed by a small link. It opens the evidence sheet: what the evidence shows, its confidence, the source document and its location, or the calculation. Sheets numbered 8.x belong to this annex; sheets numbered 1.x, 2.x and 3.x are those of Annexes 1 to 3. All sheets are listed in the index of evidence sheets.

**Recycling rates are never collection or sorting rates.** Each rate below states its scope (household or not, packaging or all plastics, year) and its definition.

**Entry prices are inputs that the operator of the model can change** [hyp:D-041]. When a stream is selected, its default entry price is applied; the operator can overwrite it. A positive price means the plant is paid to take the waste; a negative price means the plant buys it [hyp:D-042]. Section 8.6 gives the defaults and their basis.

**Reading of the sources.** Most documents were read online by research sub-agents in October 2026, with short quotations. The key figures of this annex were then re-opened by an independent checker, who found them all in the documents; their sheets say so.

## Key Messages

- **France recycles about a quarter of its plastic packaging.** In 2023, 625,275 t of the 2,428,987 t of plastic packaging waste were recycled, 25.7 %; 1,213,829 t went to energy recovery [EUROSTAT-WASPAC]. The EU average was 41.7 % [A8-CAD-EUROSTAT-WASPAC-UE-2023]. About 49 % of the tonnage counted as recycled was recycled outside France [calc:CALC-A8-EMB-RECY-HORS-FRANCE].
- **Clean plastic has a price; dirty plastic has a cost.** Sorted, washed and shredded mixed plastic bales sold at 248.81 EUR/t delivered in North-West Europe in June 2025 [RP2-061], and clean white expanded polystyrene is bought from waste centres at 55 EUR/t [RP-060]. Holders pay 121 to 159 EUR/t to dispose of household sorting rejects [RP2-051] [A8-MENB-DGPR-COUTSREF-2026], but these rejects contain only about 12 % plastic [calc:CALC-A8-REFUS-PART-PLASTIQUE].
- **A large intermediate group is taken back at a price of zero.** In 2024, 164,879 t of household plastic packaging, 37 % of the tonnage taken back, had a take-back price of zero: films, the mixed "development" stream, polystyrene pots and trays, expanded polystyrene [calc:CALC-A8-PRIXNUL-T] [calc:CALC-A8-PRIXNUL-PART].
- **Polystyrene is very little recycled.** Of the 60,000 t of polystyrene pots placed on the market each year [A8-PS-CITEOAO-2022], about 5,000 t reach a sorting centre according to Citeo, as reported by the press [A8-PS-QUECHOISIR-2025]. Household expanded polystyrene, about 15,000 t, is sorted at 1,200 t per year and has no outlet of its own after sorting [A8-PS-CITEOPSE-2025].
- **Disposal costs rise.** In 2026 the landfill tax is 69 EUR/t and the incineration tax 16 or 29 EUR/t, rising to 85 and 20 or 45 EUR/t in 2030 [CIBS-TGAP-2026]. In Ile-de-France, incineration prices for commercial waste rose by about 18.6 EUR/t, excluding tax, between 2023 and 2026 [calc:CALC-A8-INCIN-IDF-HAUSSE-2024-2026].
- **Chlorine and bromine set the limits.** The oil can leave waste status for a steam cracker only from plastic waste with at least 85 % of PE, PP and PS and at most 3 % of PVC [A3-ARRETE-SSD-HUILE-PYROLYSE-2024]. PVC has not been tested on the Urban Rig beyond its melting stage [OWJ-DEMO-2021], and no OneWorld document covers bromine (requests R-021, R-039).

## 8.1 The French Plastic Waste Picture

### 8.1.1 Tonnages

The official statistics count 2,482 kt of plastic waste in France in 2022, of which 380 kt from households [SDES-2022]. This total covers only plastic collected as such: plastic collected in mixed waste is counted elsewhere [A8-CAD-EUROSTAT-META-W074]. It is not the full amount of plastic discarded.

The plastics industry federation estimates that 4,160 kt of post-consumer plastic waste were collected in France in 2024, by application [A8-CAD-PLASTICSEUROPE-NATINFO-FR-2024]:

| Application | Collected (kt, 2024) |
|---|---|
| Packaging | 2,410 |
| Building and construction | 326 |
| Electrical and electronic equipment | 285 |
| Household, leisure and sports | 210 |
| Automotive | 185 |
| Agriculture | 175 |
| Others | 569 |

Source of the table: [A8-CAD-PLASTICSEUROPE-NATINFO-FR-2024], an industry federation; the figures are rounded estimates.

No public French source gives this breakdown. The ADEME study of the plastic waste that chemical recycling could treat is available only through a registration form and has not been read (request R-001).

### 8.1.2 Recycling Rates

| Scope | Rate | Year | Definition | Evidence |
|---|---|---|---|---|
| All plastic packaging, France | 25.7 % | 2023 | Recycled tonnage over generated tonnage, EU method | [EUROSTAT-WASPAC] |
| All plastic packaging, EU | 41.7 % | 2023 | Same | [A8-CAD-EUROSTAT-WASPAC-UE-2023] |
| Household plastic packaging, France | 30 % | 2025 | Citeo estimate for the scheme | [A8-MENA-CITEOMAG-2026] |
| Plastic waste collected as such | 20 % | 2022 | Not defined in the source | [SDES-2022] |
| Post-consumer plastic waste | 23.1 % | 2024 | Industry federation estimate | [A8-CAD-PLASTICSEUROPE-NATINFO-FR-2024] |

Under the EU method, plastic packaging counts as recycled when, sorted by polymer, it enters pelletising, extrusion or moulding [A8-CAD-UE-DEC-2019-665]. Fuel production is not recycling [A8-CAD-UE-PPWR-2025].

The targets are 50 % for plastic packaging by end 2025 and 55 % by end 2030 [A8-CAD-UE-PPWR-2025]. The French law aimed to tend towards 100 % recycled plastic by 1 January 2025 [A8-CAD-AGEC-LOI-2020]. The government's interim review found that 19 % of single-use plastic packaging had no recycling route [STRAT3R-2025].

### 8.1.3 What Happens to the Rest

- **Energy recovery** takes about half of plastic packaging waste: 1,213,829 t in 2023 [EUROSTAT-WASPAC].
- **For all post-consumer plastics,** the federation estimates incineration at 49.2 % and landfill at 27.6 % in 2024 [A8-CAD-PLASTICSEUROPE-NATINFO-FR-2024].
- **Exports** of plastic waste, scraps and parings reached about 404,000 t in 2025 [calc:CALC-A8-EXPORT-3915-T], mostly to other EU countries, first Spain, Germany and Belgium [A8-CAD-COMEXT-3915-2025].

### 8.1.4 The EU Contribution on Non-Recycled Plastic Packaging

Each Member State pays the EU 0.80 EUR per kilogram of non-recycled plastic packaging waste [RP2-055]. For France this was 1.564 billion EUR in 2023 [RP2-056]. It is paid from the State budget and is not a tax charged to households or companies [RP2-056]. A tax to pass it on, proposed in the 2026 budget bill, was removed by Parliament [RP2-057]. It therefore creates no direct payment for a waste holder today.

## 8.2 What Disposal Costs Today

These are the costs that a holder of plastic waste avoids if an Urban Rig takes it. The prices found are of different kinds (price charged or cost, gross or net, with or without tax); each line states its basis.

| Basis | Value | Year | Tax included | Evidence |
|---|---|---|---|---|
| Incineration, average price to private clients, France | 120 EUR/t excl. VAT | 2023 | Not stated | [A8-PRIX-AMORCE-DT156-2023] |
| Incineration, average price to local authorities, France | 95 EUR/t excl. VAT | 2023 | Not stated | [A8-PRIX-AMORCE-DT156-2023] |
| Same survey, earlier year: private clients and local authorities | 133 and 76 EUR/t | 2021 | Not stated | [AMORCE-DT139] |
| Incineration of household waste, Ile-de-France, net cost | 46 to 115 EUR/t | 2023 | Yes | [A8-PRIX-ORDIF-REF-2023] |
| Syctom, waste of third parties incinerated | 108 EUR/t | 2026 | Not stated | [A8-CST-SYCTOM-BP-2026] |
| Landfill, private operators, transport included | 143 EUR/t | 2021 | Yes | [A8-PRIX-AMORCE-DT141-2021] |
| Household sorting rejects, incineration and transport | 159 EUR/t | 2023 | Yes | [A8-MENB-DGPR-COUTSREF-2026] |
| Rejects of commercial packaging, energy recovery | 188 EUR/t | 2024 | Not stated | [A8-PRO-NOTE-SOUTIENS-EPRO-2026] |

No average price for 2024, 2025 or 2026 was found. Two surveys four years apart do not use the same sample, and neither states whether the tax is included; they cannot be read as a trend.

**Trend.** The price indices of the recycling federation give yearly changes, excluding tax and transport. For incineration of commercial waste in Ile-de-France: plus 9.5 EUR/t at 1 January 2024 and plus 2.9 EUR/t at 1 January 2025 [A8-PRIX-PROFRECYCLEUR-INDICES-2023-2025], then plus 6.2 EUR/t at 1 January 2026 [RP-056], about 18.6 EUR/t in three years [calc:CALC-A8-INCIN-IDF-HAUSSE-2024-2026]. For landfill in Ile-de-France, the 2026 change was plus 1.8 EUR/t [FEDEREC-Q3000-2026]. A trade press article expects the inclusion of incineration in the EU emissions trading system to raise its cost by 30 to 40 % by 2028 [A8-PRIX-DECHETSINFOS-ETS-2023].

**Waste tax (TGAP), now in the tax code** [CIBS-TGAP-2026]:

| Tax per tonne of non-hazardous waste | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Landfill | 69 | 73 | 77 | 81 | 85 |
| Incineration, energy performance 65 % or more | 16 | 17 | 18 | 19 | 20 |
| Incineration, below 65 % | 29 | 33 | 37 | 41 | 45 |
| Residues of efficient sorting, plant performance 70 % or more | 8 | 8.5 | 9 | 9.5 | 10 |

Source of the table: [CIBS-TGAP-2026].

**Solid recovered fuel.** A producer of solid recovered fuel pays the boiler that burns it: a modelled 40 to 50 EUR/t [FNADE-CSR-2023]. Cement plants covered 52 % of their heat with alternative fuels and aim at 80 % in 2030 [A8-CST-FRANCECIMENT-2025].

**Ile-de-France.** The 18 incinerators of the region had an authorised capacity of 4,270,900 t per year in 2023 and burned 3,810,761 t in 2022, 93 % of the technical capacity of their furnaces [A8-CST-ORDIF-UIDND-2023].

## 8.3 Stream by Stream

### 8.3.1 Household Plastic Packaging, Overall

- **Placed on the market:** 1,165 kt in 2024 and 1,174 kt in 2025; recycled 324 kt and 346 kt [CITEO-RA-2025]. The scheme estimates the plastic recycling rate at 30 % in 2025 [A8-MENA-CITEOMAG-2026].
- **Who pays.** Producers pay Citeo per kilogram placed on the market. In 2026: 70.00 cents for clear PET bottles, 77.01 for rigid PE, 80.51 for rigid PS including expanded PS, 140.01 for complex packaging and 210.01 for PVC [RP2-045]. Local authorities receive a support of 776 EUR per tonne of plastic sorted and recycled [RP2-047], plus the take-back price.
- **Take-back prices in 2024**: clear PET bottles 347 EUR/t [A8-MENA-PRIXREPRISE-2025]; PE/PP mixed 53 EUR/t [A8-MENA-PRIXREPRISE-2025]; PE/PP/PS mixed 39 EUR/t [A8-MENA-PRIXREPRISE-2025]; films, the development stream, PS pots and trays and expanded PS 0 EUR/t [A8-MENA-PRIXREPRISE-2025]; weighted average 140 EUR/t [A8-MENA-PRIXREPRISE-2025]. For films and the development stream, the zero price is an assumption of the source, no price having been observed.
- **Main buyer.** Valorplast took back 120,500 t of household plastic packaging in 2025, 76 % recycled in France [A8-MENA-VALORPLAST-2025]. Its guaranteed floor price is 0 EUR/t for PS and the mixed streams [VALORPLAST-G-2024].
- **No recycling route.** In 2021, 66 % of household plastic packaging was considered recyclable and 17 % was PVC, complex packaging or other resins without a recycling route [RP2-036].

### 8.3.2 Household Films and the "Development" Stream

- **Tonnage:** 97,379 t of household films were taken back in 2024 [calc:CALC-A8-FILMS-REPRIS-T], and 66,005 t of the development stream, rigid mixed plastics including multilayer trays [A8-MENA-PRIXREPRISE-2025].
- **Recycling rate:** not published for France. In Europe, 18 % of flexible films placed on the market were used as input by recyclers in 2020 [PRE-FILMS-2023].
- **Price:** 0 EUR/t taken back (assumed by the source) [A8-MENA-PRIXREPRISE-2025].
- **Urban Rig:** PE and PP were tested; soiled films were not (Section 8.4).
- **Competition:** over-sorting centres and the Grandpuits chemical recycling plant (Section 8.5).

### 8.3.3 Sorting Rejects of Separate Collection

- **Tonnage:** 800,000 t in 2022, 23.0 % of the input of sorting centres [CITEO-CAHIER-CS-2024]; 750,000 t in another Citeo study [OCAPEM-2025]; 496 kt in the government cost model [A8-MENB-DGPR-COUTSREF-2026]. In Ile-de-France, 146,368 t in 2024, 27 % of the separate collection, 98 % of it incinerated [RP-034].
- **Composition:** rigid plastics 7.5 % and flexible plastics 4.5 % on average in France [OCAPEM-2025], about 12 % in total [calc:CALC-A8-REFUS-PART-PLASTIQUE]. No composition is published for Ile-de-France (request R-003); calorific value and chlorine were not found.
- **Who pays:** the local authority, 159 EUR/t including tax [A8-MENB-DGPR-COUTSREF-2026], or 121 EUR/t excluding tax in one 2024 contract [RP2-051]. The 2026 incineration tax falls to 8 EUR/t for residues of efficient sorting [CIBS-TGAP-2026], which need a calorific value of at least 9 MJ/kg [RP-071].
- **Over-sorting:** four centres of 30,000, 25,000, 15,000 and 30,000 t per year, the last one, at Thiverval-Grignon, due to open at the end of 2026 [RP-021].
- **Urban Rig:** these rejects are a mixed waste, not a plastic stream; not tested (request R-040).

### 8.3.4 Polystyrene (Compact)

- **Tonnage:** 100,000 t of household polystyrene packaging placed on the market each year, of which 60,000 t of pots [A8-PS-CITEOAO-2022].
- **Real recycling:** about 5,000 t reach a sorting centre according to Citeo, as reported by the press [A8-PS-QUECHOISIR-2025], about 8 % of the pots [calc:CALC-A8-PS-PART-TRIE]. Sorted pots were recycled in Spain into flower pots and hangers [A8-PS-CITEOMAP-2024]. Since September 2025, 80 % of the sorted tonnage goes to the Indaver plant in Antwerp, which turns it back into styrene, and 20 % to mechanical recycling in Spain [A8-PS-CITEOINDAVER-2025]. No recycled tonnage has been published.
- **Rest:** the household pots not sorted end in residual waste (Annex 5).
- **Price:** taken back at 0 EUR/t [A8-MENA-PRIXREPRISE-2025]; producers pay 80.51 cents per kilogram [RP2-045].
- **Urban Rig:** PS tested, with an oil yield of 55 % to 73 % [CHIBA-ESSAIS-FICHES].

### 8.3.5 Expanded Polystyrene

- **Household packaging:** about 15,000 t placed on the market; 1,200 t per year come out of sorting, and this degraded material has no outlet of its own; recyclers accept it only in very small proportions [A8-PS-CITEOPSE-2025].
- **Waste centres:** 15 % of French waste centres collect expanded polystyrene [A8-PS-AN14052-2026]; more than 600 t were collected at 200 sites [A8-PS-CITEOPSE-2025]. Clean white material is bought at 55 EUR/t [RP-060]; one service provider charges a local authority 8 EUR per cubic metre instead [A8-PS-POITOU-2025].
- **Commercial packaging:** 71 kt placed on the market; taken back at 284 EUR/t in April 2024 [A8-PRO-NOTE-SOUTIENS-EPRO-2026]. A study for the fisheries authority quotes recycling rates of 33 % for all expanded polystyrene packaging and 50 % for commercial packaging, figures from the industry federation [A8-PS-FAM-2023].
- **Building insulation:** above the limit set by the EU regulation on persistent organic pollutants, insulation containing the flame retardant HBCDD must be destroyed and cannot be recycled. The limit, 1,000 mg/kg in the 2019 text [A8-PS-POP2019-2019], was lowered to 500 mg/kg, with 200 mg/kg planned after a review [A8-PS-OEIL2400-2022].
- **Urban Rig:** expanded polystyrene waste tested, with 73 % oil [CHIBA-ESSAIS-FICHES]. Bromine is not documented (request R-039).

**The project sponsor's understanding, checked.** "Very little recycled": confirmed for household PS and expanded PS. "Compacted or melted into blocks": compactors and thermal densifiers are described [A8-PS-FAM-2023], but no French tonnage was found. "No real outlet": confirmed for sorted household expanded PS; contradicted for clean white expanded PS, which has a buyer, and for compact PS, recycled into styrene since 2025.

### 8.3.6 Commercial and Industrial Packaging

- **Tonnage:** 1,074 kt of non-hazardous plastic packaging placed on the market, of which 307 kt of flexible LDPE (stretch and shrink films) [A8-PRO-NOTE-SOUTIENS-EPRO-2026]. In Ile-de-France, 260,000 t per year of plastic waste from businesses, of which 17 % recycled; half of the commercial share is pallet stretch film [A8-PRO-IDF-LIVRET-2023].
- **Recycling rate:** 26 % in 2023 [A8-PRO-NOTE-SOUTIENS-EPRO-2026].
- **Who pays:** an extended producer responsibility scheme starts for this packaging, with targets of 50 % in 2028 and 55 % in 2030 for plastic [A8-PRO-CDC-EPRO-2025]; its start has been postponed by a draft order [A8-PRO-REPORT-EPRO-2026]. Clear flexible LDPE was taken back at 151 EUR/t in April 2024; sorting rejects cost 188 EUR/t in energy recovery [A8-PRO-NOTE-SOUTIENS-EPRO-2026].
- **Urban Rig:** PE and PP tested (Section 8.4).

### 8.3.7 Agricultural Films and Plastics

- **Tonnage:** 84,500 t of agricultural plastics collected in 2025, a collection rate of 75 % [A8-PRO-ADIVALOR-RA-2025]. Used films to collect are estimated at 70,000 to 85,000 t per year [A8-PRO-ADIVALOR-RA-2024].
- **Recycling:** 90 % of what is collected [A8-PRO-ADIVALOR-RA-2025].
- **Who pays:** a contribution included in the product price [A8-PRO-ADIVALOR-RA-2025].
- **Urban Rig:** PE tested. Little of this stream is in Ile-de-France.

### 8.3.8 Production Scrap

No source gives the tonnage, fate or price of plastic production scrap in France: NOT FOUND (searched: recycling federation, plastics processors' federation, ADEME). The recycling federation reports 1,024,000 t of plastics collected and recycled in 2024, 69 % of industrial origin [RP2-041]. Clean scrap is resold directly and is not a likely feed.

### 8.3.9 Plastics from Electrical and Electronic Equipment

Sorted plastics are in scope; shredder residues are excluded [hyp:D-037].

- **Tonnage:** 1,215,345 t of equipment collected in France in 2024 [A8-DEV-EUROSTAT-WEEE-2024]. One producer scheme estimated the plastic in its household equipment at about 315,000 t, 17 % of the mass [A8-DEV-ECOSYSTEM-RECYCHIM-2020].
- **Brominated plastics:** 39,301.93 t of plastics containing brominated flame retardants were extracted by that scheme in 2025 [A8-DEV-ECOSYSTEM-RA-2025]. Plastics are sorted at 2,000 ppm of bromine [A8-DEV-INERIS-BROME-2020]; the brominated fraction goes to hazardous waste incineration, at a cost the scheme calls very significant but does not quantify [A8-DEV-ECOSYSTEM-RECYCHIM-2020]. The EU waste limit for the sum of these flame retardants is 500 mg/kg, lowered to 350 mg/kg from 30 December 2025 and 200 mg/kg from 30 December 2027 [A8-DEV-POP-PBDE-2025].
- **Urban Rig:** the polymers (ABS, HIPS) are not tested; bromine is not documented [hyp:D-040].

### 8.3.10 Plastics from End-of-Life Vehicles

- **Tonnage:** 1,189,994 t of end-of-life vehicles in 2023; reuse and recycling 89 %, reuse and recovery 96.7 % [A8-DEV-EUROSTAT-ELV-2023].
- **Dismantled plastic parts:** 5,203 t recycled and 9,834 t reused in 2023 [A8-DEV-EUROSTAT-ELV-2023]. Shredder residues are excluded [hyp:D-037].
- **Polymers:** PP 37 %, PU 15 %, PA 12 %, PVC about 3 % of the plastics of current end-of-life vehicles [A8-DEV-JRC-PLASTICS-VEHICLES-2023].
- **Rules:** French target of 65 % recovery of PP and PE from 2026 and 70 % from 2028 [A8-DEV-ARRETE-CDC-VHU-2023]. The new EU regulation sets 15 % of recycled plastic in new vehicles after 72 months and 25 % after 120 months [A8-DEV-ELV-COUNCIL-6180-2026], of which 20 % from end-of-life vehicles, and allows chemical recycling [A8-DEV-ELV-REG-2026-1738].
- **Urban Rig:** PP tested.

### 8.3.11 Building Plastics and PVC

- **Recycling:** 20,282 t of plastic from building products and materials were recycled in 2024, a rate of 7.0 % against a target of 17 %; plastic is 8 % of the products placed on the market in this category [A8-BTX-ADEMEPMCB-2024]. No breakdown by polymer and no share of PVC were found.
- **PVC:** the polymer is 56.7 % chlorine [A8-BTX-INRSPVC-2026]. Europe recycled 765,972 t of PVC in 2025 [A8-BTX-VINYLPLUS-2026]. EU rules on lead limit the recycling of old rigid PVC [A8-BTX-REACHPLOMB-2023].
- **Urban Rig:** PVC not tested beyond melting [OWJ-DEMO-2021]; the share of PVC accepted in the feed is open until OneWorld tests [hyp:D-040].

### 8.3.12 Textiles

- **Tonnage:** 917,604 t of clothing, linen and footwear placed on the market in 2025, 272,479 t collected and 216,264 t sorted [A8-BTX-REFASHIONKPI-2025].
- **Fate of the sorted tonnage:** 54.47 % reused, 25.31 % sent to recycling, 11.03 % wiping cloths and 8.4 % solid recovered fuel [A8-BTX-REFASHIONKPI-2025], about 18,000 t [calc:CALC-A8-TEXTILES-CSR-T].
- **Polymers:** in non-reusable textiles, polyester 19 % and acrylic 12 % [A8-BTX-REFASHIONCARAC-2023].
- **Fibre-to-fibre recycling** is below 1 % in Europe, a secondary figure [A8-BTX-EEATEXTILES-2022].
- **Who pays:** producers, 173.61 EUR per tonne placed on the market [A8-BTX-REFASHIONKPI-2025].
- **Urban Rig:** not tested (request R-021).

### 8.3.13 Furniture and Other Producer Schemes

- **Furniture and household goods:** 1,974 kt collected in 2025 by the main scheme; across all its streams, 46 % recycled and 47 % recovered as energy; outputs included 407 kt of solid recovered fuel, 45 kt of foams and 13 kt of plastics [A8-BTX-ECOMAISON-2025].
- **Urban Rig:** foams (PU) are not tested.

### 8.3.14 Plastic in Residual Household Waste

Plastics make up 15.8 % of residual household waste, 2,329,258 t [ADEME-MODECOM-2024-DATA]. This stream is treated in Annex 5.

## 8.4 Suitability for the Urban Rig

| Polymer or stream | Tested on Urban Rig equipment | Result | Evidence |
|---|---|---|---|
| PE and PP | Yes | Oil 73 % to 81 % of the input | [CHIBA-ESSAIS-FICHES] |
| PS, including expanded PS waste | Yes | Oil 55 % to 73 % | [CHIBA-ESSAIS-FICHES] |
| Mixed plastics with some PVC and FRP | Yes, 2021 | PVC stopped at the melting stage | [OWJ-DEMO-2021] |
| PET, PA, PU, textiles, PVC alone | No | Request R-021 | |
| Sorting rejects, multilayer packaging, sorted electronic plastics | No | Request R-040 | |

Source of the table: [CHIBA-ESSAIS-FICHES] [OWJ-DEMO-2021]; details in Annex 2.

- **Chlorine.** According to OneWorld design data, the chlorine of PVC turns into dilute hydrochloric acid in the steam and is captured by a catalytic layer [UR2000-JP-P03-P04-CHLORE]. The oils made from municipal plastics contained 0.137 % and 0.526 % chlorine [CHIBA-JLOS-HUILES].
- **Outlet of the oil.** To leave waste status for a steam cracker, the oil must come from plastic waste with at least 85 % of PE, PP and PS and at most 3 % of PVC, and contain at most 500 ppm of halogens without purification [A3-ARRETE-SSD-HUILE-PYROLYSE-2024]. Otherwise the oil is a fuel for a permitted plant (Annex 3).
- **Bromine.** No OneWorld document covers bromine. The project sponsor's working assumption is that bromine is removed largely as chlorine is; it is not documented and awaits tests [hyp:D-040].

## 8.5 Competition for the Feedstock

- **Mechanical recycling:** French and European recyclers take back the valuable streams (8.3.1).
- **Chemical recycling in France:** the Grandpuits plant of TotalEnergies, 15,000 t per year, started in March 2026 [RP2-032] and is now wholly owned by TotalEnergies [A8-CST-TTE-RACHAT-2026]. Its technology partner went into administration in the United Kingdom in April 2026 [A8-CST-GAZETTE-PE-2026]. The Eastman polyester project in Normandy, more than 110,000 t per year in a first phase, is paused [A8-CST-EASTMAN-2026].
- **Chemical recycling in Europe:** Viridor closed its three plastic pyrolysis plants in 2026, citing weak demand and cheaper virgin plastic [A8-CST-VIRIDOR-2026].
- **Buyers of pyrolysis feed:** they buy sorted, washed and shredded bales with at least 86 % polyolefins and at most 1 % PVC [RP2-062], at 248.81 EUR/t in June 2025 [RP2-061].
- **Solid recovered fuel and cement plants:** see Section 8.2.
- **Incineration:** the default outlet, nearly saturated in Ile-de-France (Section 8.2).

## 8.6 Default Entry Prices for the Model

In the model, a price paid to the plant is positive and a purchase is negative. Every value can be changed by the operator [hyp:D-041] [hyp:D-042].

| Stream | Default | Basis | Evidence |
|---|---|---|---|
| Sorted plastic in bales | Buy at 249 EUR/t | Market price of mixed plastic bales, June 2025 | [RP2-061] |
| Clean white expanded PS from waste centres | Buy at 55 EUR/t | Buyer's price, 2025 | [RP-060] |
| Household films, development stream, PS pots and trays, sorted household expanded PS | 0 EUR/t | Take-back price 2024 | [A8-MENA-PRIXREPRISE-2025] |
| Rejects of commercial packaging | Paid 188 EUR/t | Energy recovery cost | [A8-PRO-NOTE-SOUTIENS-EPRO-2026] |
| Household sorting rejects | Paid 100 EUR/t | Sponsor's choice; holder's cost 159 | [hyp:D-042] [A8-MENB-DGPR-COUTSREF-2026] |
| Residual household waste | Paid 100 EUR/t | Sponsor's assumption | [hyp:D-039] |
| Brominated plastics, synthetic textiles, furniture foams and plastics, building plastics | Paid 100 EUR/t | Sponsor's assumption; real price not found | [hyp:D-042] |

## 8.7 Conflicts Between Sources

- **National sorting rejects:** 800,000 t [CITEO-CAHIER-CS-2024], 750,000 t [OCAPEM-2025] or 496 kt [A8-MENB-DGPR-COUTSREF-2026].
- **Incineration price surveys:** 133 and 76 EUR/t in 2021 [AMORCE-DT139], 120 and 95 EUR/t in 2023 [A8-PRIX-AMORCE-DT156-2023]. Different samples; not a trend.
- **HBCDD limit:** 1,000 mg/kg in the 2019 text [A8-PS-POP2019-2019]; 500 mg/kg in the amended text, read only in a summary [A8-PS-OEIL2400-2022].
- **Plastic packaging recycling 2022:** 25.2 % in the government review [STRAT3R-2025]; Eurostat gives 25.4 % for the same year [EUROSTAT-WASPAC].

## 8.8 Open Points

| Ref. | Subject | Held by |
|---|---|---|
| R-001, R-042 | ADEME reports available only on registration | Project sponsor |
| R-003 | Composition of sorting rejects in Ile-de-France | Local authorities |
| R-021, R-040 | Tests on PET, PVC, textiles, rejects, multilayer, electronic plastics, foams | OneWorld |
| R-039 | Bromine and persistent pollutants | OneWorld |
| R-041 | Physical form of a plastic feed, maximum PVC and bromine | OneWorld |
| R-044 | Disposal prices in Ile-de-France, purchase price at Grandpuits | Operators |

## 8.9 References

The full list of documents cited, with their location and confidence, is in the index of evidence sheets.
