# Measured stage-by-stage mass balances of household plastic packaging (collection → sorting → recycler output), France first, then EU/adjacent

Research date: 2026-10-10. Scope: complements `background-earlier-research/README.md` (Citeo refus 23 % in 2022, 15-20 % of plastics lost at sorting per Citeo ECT 2020, PRE recycler yields PET 73 %, HDPE 71 %, PP 69 %, household films ~50 %, Citeo Observatoire de la qualité 2023 bale purities). Those figures are not repeated except where verified or extended.

**Source rating legend** (applied to every finding):
- `[primary measured]` = sampling/characterisation, weighing or lab measurement by the source itself.
- `[primary declared]` = figures reported by operators or schemes (questionnaires, mass-flow declarations), not independently measured by the author.
- `[modelled]` = MFA / data reconciliation / extrapolation / assumptions, even when calibrated on some measurements.
- `[secondary]` = press release, news article or report quoting another source.
- **[calcul]** = arithmetic done by me from sourced figures; not stated by the source.

**Reading caveat.** All documents were read through a web-fetch tool that returns an extract/summary of the page. Quotes below are those returned verbatim by the tool. Page/table numbers are those the tool reported. Pages that could NOT be read:
- `pmc.ncbi.nlm.nih.gov` (Antonopoulos 2021 and Klotz et al. 2022 Swiss dataset) returned a reCAPTCHA wall. Antonopoulos was read instead via the Europe PMC full-text API. **Klotz et al. (PMC8914542, Swiss plastic flows dataset) was not read**: the Europe PMC request was rate-limited (HTTP 429).
- `mdpi.com` (Brouwer et al. 2020, *Sustainability* 12, 10021, Dutch 2017 flows): not read (access permission timed out).
- UBA Texte 156/2024 (Germany 2022): only the first ~73,000 characters (summary chapters) were extractable. Tables 69 ("Durchschnittliche Rezyklatausbeute aus Sortierfraktionen der dualen Systeme") and 70 ("Standardverlustraten") were **not** reachable.
- UBA Texte 125/2022: only the summary chapter was extractable.

---

## 1. What do peer-reviewed material flow analyses report?

### Takeaway
No peer-reviewed MFA measures the whole chain end-to-end with weighbridge data. The strongest datasets are Dutch (Wageningen: 173 sorting analyses 2010-2015, plus lab washing tests). They show that roughly **20-26 % of household plastic packaging on the market becomes washed recycled flakes**. For separately collected material, about **half of the gross collected tonnage** ends up as main recycled product [calcul]. The EU-wide JRC study (Antonopoulos 2021) relies on **operator-declared** annual averages from 5 sorting plants and 8 recyclers, several of them in France. Its medians are 37-85 % sorting recovery and 66-88 % recycler yield depending on polymer, with an EU end-of-life recycling rate of **~14 %** in 2017 (excluding exports). No French MFA with measured sorting and recycling yields was found.

### Cited Findings

**Antonopoulos, Faraca & Tonini 2021 (JRC), *Waste Management* 126, 694-705 — EU27, data 2017; plant survey June-Nov 2019** — read via [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8162419/fullTextXML) (article page [PMC8162419](https://pmc.ncbi.nlm.nih.gov/articles/PMC8162419/) blocked)
- Primary data: 5 MRFs and 8 recycling plants. "The plants were located in Germany, France, Spain, Italy, Benelux, Scandinavia and Croatia" (Sec. 2.2). No plant-level French figures are reported separately. `[primary declared]` (questionnaires to operators, annual averages)
- The authors note the data are annual averages including failures and under-capacity periods, **not controlled sampling**. Earlier studies (Eule 2013, Mastellone et al. 2017) did use controlled sampling (Sec. 3.1). Table 4 loss levels are qualitative: "level of losses is based on managers' judgements of the rejects" (Table 4 footnote).
- **Sorting rate at MRF** (share of a polymer in the input recovered into its target output), median used for 2017 (Table 2): **PET 85 %, HDPE 85 %, PP 64 %, films 59 %, PS 37 %, PVC 73 %**. 75th percentile used for 2030: PET 91 %, HDPE 91 %, PP 79 %, films 73 %, PS 65 %. Plant ranges (Sec. 3.1): PET 45-97 %, HDPE 13-95 %, PP 31-80 %. `[primary declared]`
- **Recycling-plant yield** (output/input), median (Table 2): **HDPE 88 %, PET 81 %, films 71 %, PP 66 %, PS 66 %, PVC 80 %**. Plant ranges (Sec. 3.1): HDPE 70-88 %, PET 63-90 %, PP 53-85 %. Films at one plant (REC7) 50 %, PS at REC8 75 %. `[primary declared]`
- **Output purity of sorted bales** (Table 3, operator-declared, 2019): PET 65 % (MRF4) to 98 %; HDPE 85-98 %; films 82-98 %; PP and PS 90-98 % at some MRFs, PP 80 % at REC7. "some plant operators reported that for certain output materials higher impurities are accepted by the market" (Sec. 3.1). The accepted impurity levels mentioned are about 10 % for PP and up to 20 % for films. `[primary declared]`
- **System level (modelled):** separate collection about 41 % of PPW in 2017 (Eurostat); capture rates in the MFA 20-62 % (Table S3, from Deloitte 2017). "sorting losses at the MRFs amounted to around 29 ± 12%" (Sec. 3.3). Share of PPW sent to recycling after sorting 29 ± 6 %. End-of-life recycling rate **14 ± 3 %** excluding exports, 25 ± 6 % counting exports. Exports: 37 ± 6 % of sorted material shipped outside the EU. `[modelled]`
- Uncertainty: "The standard deviation was calculated assuming a triangular distribution of the dataset" (Sec. 2.3.1). On prior literature: "Other studies use secondary data and/or best-guess estimates as input" (Sec. 1).

**Brouwer, Thoden van Velzen, Augustinus, Soethoudt, De Meester, Ragaert 2018, *Waste Management* 71, 62-85 — Netherlands, flows 2014, compositions 2010-2015** — [edepot.wur.nl/426558](https://edepot.wur.nl/426558) (accepted post-print)
- Method: MFA with STAN data reconciliation. Gross separate-collection totals are **declared** (Afvalfonds 2015); compositions are **measured** by sorting analyses (173 PPW samples 2010-2015; 37 sorting analyses of separate-collection products, 87 of MSW-derived products). Milled-goods composition was checked by NIR on 10 single samples. The paper says no standard deviations could be calculated for modelled results. `[modelled, calibrated on primary measured compositions]`
- Household plastic packaging potential **341 Gg net** (20.2 kg/cap/a). Separately collected **129.1 Gg gross (declared)**, of which **86 Gg net** packaging. Net collection response **25 %**. `[modelled / declared]`
- Separate collection → **105.4 Gg gross sorted products** containing 75.2 Gg net packaging (PET 8.8, PE 10.1, PP 12.6, film 26.5, mix 47.3 Gg gross). Sorting residue: **5.1 Gg residual waste**. The sorted products also carry **6.6 Gg non-packaging plastic and 18.7 Gg moisture and dirt** (Sec. 3). `[modelled]`
- [calcul] 105.4 / 129.1 = **82 %** of the gross separately collected mass leaves the sorter as sorted products (of which, by mass, ~18 % is moisture/dirt: 18.7 / 105.4).
- Washed milled goods, whole network: **75.2 Gg net main products, 28.1 Gg side products, 16.7 Gg process waste**. Net chain yield (main products / potential) **22 %**; 30.3 % including side products, which the authors call "not realistic". The official declared rate was 50 % on a different method (Sec. 3). `[modelled]`
- Washed product purity, NIR measured, single samples (Table 5), separate collection / mechanical recovery: PET 97.2 / 99.4 %; PE 90.6 / 94.0 %; PP 90.6 / 95.0 %; **film 76.4** / 96.8 %; **mix 32.6** / 48.0 %. `[primary measured, n = 1 per product]`
- Internal inconsistency flagged by the reading tool: the abstract and text give ~30 %, but Table 1's average row shows 21 % correctly sorted.

**Thoden van Velzen, Brouwer, Picuno 2018, WFBR Report 1823, *Verbeteropties voor de recycling van kunststofverpakkingen*** — [edepot.wur.nl/450447](https://edepot.wur.nl/450447) — same model, 2014, with error bars. `[modelled, calibrated on 173 point measurements]`
- "een steekproef van 173 punt-metingen" (a sample of 173 point measurements from sorting analyses).
- Separately collected **124 ± 10 kt gross / 85 ± 6 kt net packaging** → sorting products **104 ± 10 gross / 76 ± 3 net** → **sorting residue + moisture/dirt 21 ± 3 kt gross / 8.9 ± 0.2 kt net**, about 11 % of net packaging (Fig. 2).
- Mechanical recycling of separate-collection sorted products: **main product 59 ± 5 kt, by-product 24 ± 5 kt, process waste 11 kt**. By polymer, main product (kt): PET 6.6, PE 8.1, PP 9.4, film 18, mix 17.
- "In 2014 bedroeg het netto-materiaal-rendement van de recyclingketen 20 ± 2% en de gemiddelde polymeer-zuiverheid 91 ± 6%." The practice figure of ~40-50 % "valt hoger uit" because it includes moisture, dirt and residual waste and excludes process losses.

**Brouwer, Picuno, Thoden van Velzen, Kuchta, De Meester, Ragaert 2019, *Waste Management* 100, 112-121 — Netherlands 2017 vs 2014** — [tore.tuhh.de/handle/11420/3415](https://tore.tuhh.de/handle/11420/3415) (abstract only) `[modelled]`
- After the collection portfolio expanded to PMD (plastics + metal + drink cartons): recycled plastics (main washed milled goods) rose from **75 Gg net (2014) to 103 Gg net (2017)**. **Rejects and sorting residues rose from 19 Gg to 70 Gg gross**. Net recycling yield 2017 **26 ± 2 %**; average polymeric purity **90 ± 7 %**. Rejects and residues grew faster than recycled output.

**Thoden van Velzen, Jansen, Brouwer, Feil, Molenveld, Pretz 2017, "Efficiency of recycling post-consumer plastic packages", AIP Conf. Proc. 1914, 170002** — [edepot.wur.nl/430783](https://edepot.wur.nl/430783) — **lab-scale washing of real Dutch sorted products**, 25-50 kg samples from sorting plants, 5 kg per wash run. Washing and float-sink only, no extrusion. `[primary measured, lab]`
- Table 2, recovered mass of the main product, dry basis (SC = separate collection, MR = mechanical recovery from MSW): PET SC 83 ± 2 % (sinking); PE SC 94 ± 2 %; PP SC 90 ± 1 %; film SC 90 ± 6 %; mixed plastics SC 64 ± 12 %. MR values are lower: PP 83 %, film 83 ± 15 %.
- **Dry-matter content of sorted products** (Table 2): PET SC 93 %, PE SC 95 %, PP SC 99 %, film SC 97 %, MP SC 98 %; PET MR 87 %, PP MR 88 %, film MR 87 %. That is **1-13 % moisture by mass**. `[primary measured]`
- Loss split per product: **sludge 0.7-6 %, "dissolved" 2-10 %** (by difference). Non-target polymer side streams: PET SC 11 % floating fraction (polyolefin caps/labels); mixed plastics SC 32 ± 11 % sinking.
- "The net PE yields are close to 100% for such a standard recycling process." "Polymeric contaminants are only partially removed by this standard mechanical recycling process."

**Picuno, Alassali, Chong, Kuchta 2021, *Resources, Conservation and Recycling* 169, 105515 — Germany 2017** — [tore.tuhh.de/handle/11420/9030](https://tore.tuhh.de/handle/11420/9030) (abstract only) `[modelled, with own manual sorting data]`
- Post-consumer plastic packaging **26.3 kg/cap ± 3.0 %**. Separate collection efficiency (deposit PET + dual system) **74.8 % ± 2.9 %**. Net material recycling rate **26.4 % ± 1.3 %** excluding mixed polyolefin recycling, **37.8 % ± 2.0 %** including it. "most of the material losses occur at the sorting stage", mainly because of complex multi-material packaging. Stage-level sorting loss values were not in the abstract.

**Van Eygen 2018, TU Wien PhD thesis (includes Van Eygen, Laner, Fellner 2018, *Waste Management*, "Circular economy of plastic packaging: current practice and perspectives in Austria") — Austria 2013** — [repositum.tuwien.at PDF](https://repositum.tuwien.at/bitstream/20.500.12708/5424/2/Eygen%20Emile%20van%20-%202018%20-%20Management%20of%20plastic%20wastes%20in%20Austria%20analysis%20of%20the...pdf) `[modelled, pedigree-matrix uncertainties]`
- "The total incoming waste stream amounted to 300 kt/a±3% (35 kg/cap·a)". 58 % ± 3 % separately collected, 30 % ± 4 % in residual waste, 12 % ± 4 % in bulky/commercial waste (Ch. 5.2).
- Sorting efficiency by product type (Table 5.1): **PET bottles and large products 73-88 %, small hollow bodies 47 %, small films 34 %, "others" 12 %**. Overall sorting rate (SR) 34 % ± 3 %; recycling rate (RR) **26 % ± 7 %**. Sorting residues were "mainly sent to industrial incineration in the cement industry" (Ch. 4.2).
- [calcul] 1 − 26/34 ≈ **24 % of sorted material lost at the recyclers**. The author warns that CR, SR and RR are defined differently from common usage (all relative to total waste generated).

**Koinig, Rutrecht, Friedrich, Barretta, Vollprecht 2022, *Polymers* 14, 1553 — Austria** — [mdpi-res.com PDF](https://mdpi-res.com/d_attachment/polymers/polymers-14-01553/article_deploy/polymers-14-01553.pdf)
- Hand sorting (Q1 2021) of separately collected packaging waste: flexible 2D items **30 wt %** of the stream (~52,000 of 171,000 t). Multilayers are 20 wt % of films (n = 143 FTIR). `[primary measured]`
- "Currently, 24 wt% (12,280 tons) of small films derived from SCW are mechanically recycled" (Sec. 2.4, from Van Eygen 2018 data). Baseline packaging recycling quota 25.7 % (Table 6). `[modelled]`

**Roosen et al. 2022, *Resources, Conservation and Recycling* 178, 106025 — Belgium** — [agris.fao.org record](https://agris.fao.org/search/fr/records/669f714100eb85b7d72cff7e) (abstract only) `[modelled, with a validated sorting model]`
- Collection of plastic packaging rises from **33.6 to 64.4 m%** with the expanded P+MD portfolio. **77.3 %** of the collected material is simulated as separated into the targeted fractions. **Only 49.8 % of plastic packaging is sorted correctly overall.** Product grades: PS rigid >99 %, **PE films ~80 %**. Simpson's Diversity Index 82 % for "other films".

**Schmuck, Belé, Withoeck, Van Geem, Ragaert, De Meester 2026, *Nature*, "Analysis of trade-offs of post-sorting plastic packaging"** (DOI 10.1038/s41586-026-10606-4) — [paperity](https://paperity.org/p/371222354/analysis-of-trade-offs-of-post-sorting-plastic-packaging) (truncated)
- Samples from "one single material recovery facility". Non-packaging items are 15.7 wt % of the mixed post-sorting sample (Fig. 1a). `[primary measured]`
- Introduction, citing other work: "even these systems retain 7–30% non-target material in PMD streams owing to household misplacement". `[secondary within a primary paper]`

**Deloitte (Hestin et al.) 2017, *Blueprint for plastics packaging waste: quality sorting & recycling*, for Plastics Recyclers Europe** — [cewep.eu PDF](https://cewep.eu/wp-content/uploads/2025/04/pre-blueprint-packaging-waste-2017.pdf) `[modelled; extrapolation from 5 countries, data 2014]`
- "The estimation in the Sankey diagram assumes a refusal rate due to impurity of about 10%" (III.3.4, p. 18). This is an **assumption**, not a measurement; the authors call it low.
- **France** (Table 9, p. 23): PET + polyolefin collection 44 %, recycling 21 %. Germany: 76 % / 36 %. Italy: 55 % / 42 %. UK: 38 % / 22 %. Spain: 41 % / 31 %. EU recycling excluding extra-EU exports about 15 % (p. 17).
- PET flake contaminants (Table 10, p. 23, citing Petcore 2015): **France PVC 313.8 ppm**, Germany 16.4 ppm, Italy 387.1 ppm. `[secondary]`

### Inferences
- Across the Netherlands (2014: 20-22 %; 2017: 26 %), Germany (2017: 26-38 %), Austria (2013: 26 %) and the EU (2017: ~14 % excluding exports), the **net output of washed recyclate per tonne of household plastic packaging on the market** is about **15-30 %**. France's 29.5 % "recyclé / mis sur le marché" for 2025 (background README) sits at the top of this range. That plausibly reflects definitions (point of measurement, inclusion of exports) rather than better yields; to be verified.
- Dutch separate collection, 2014 (WUR 1823), per tonne **gross collected** [calcul]: about **840 kg** of sorted products (104/124) → about **476 kg main washed milled goods** (59/124) + 194 kg by-products (24/124, mostly mixed polyolefins and non-target polymers) + 89 kg process waste (11/124). The remaining ~240 kg is sorting residue, moisture and dirt. With the 91 % average polymer purity, target-polymer content is about **435 kg per tonne gross collected** [calcul].
- Ratio of main product to gross sorted product, NL 2014 separate collection [calcul from WUR 1823 Fig. 2 values]: PET 6.6/8.7 = **76 %**, PE 8.1/10.1 = **80 %**, PP 9.4/12 = **78 %**, film 18/26 = **69 %**, mix 17/46 = **37 %**, all products 59/104 = **57 %**. These are in the same range as the PRE yields (PET 73 %, HDPE 71 %, PP 69 %, films ~50 %), except mixed plastics, which PRE does not cover.
- Products of the Antonopoulos medians, sorting × recycling [calcul, illustrative only because they come from different plants]: PET 0.85 × 0.81 ≈ **69 %**, HDPE 0.85 × 0.88 ≈ **75 %**, PP 0.64 × 0.66 ≈ **42 %**, films 0.59 × 0.71 ≈ **42 %**, PS 0.37 × 0.66 ≈ **24 %** of each polymer entering the MRF.
- The dominant loss stage differs by stream. For bottles (PET, HDPE), losses are split between sorting and recycling. For films, small formats and mixed plastics, sorting dominates (Picuno: "most of the material losses occur at the sorting stage"; Van Eygen: small films 34 %, others 12 % sorting efficiency).

### Gaps
- **No French peer-reviewed MFA with measured sorting and recycling transfer coefficients was found.** Antonopoulos surveyed French plants but did not publish them separately.
- Stage-level values (per-polymer transfer coefficients) of Picuno 2021 and Van Eygen et al. 2018 sit in the full articles and supplements, which were not read; only abstracts or thesis chapters were.
- Klotz et al. 2022 (Swiss dataset) and Brouwer et al. 2020 (*Sustainability*, Dutch 2017 flows) were not read (access failures; see top).
- Faraca & Astrup (Denmark) was not searched within the call budget.
- No MFA reports a weighbridge-closed mass balance at a single sorting plant plus its downstream recyclers. All system-level yields are reconciled models.

---

## 2. What do official national and industry data say?

### Takeaway
Official figures are almost all **declared tonnages measured at the gate to the recycler** ("delivered for recycling" or "transferred to recovery"), corrected by sampling for non-packaging and contamination. They are not measured recycler output. Under the EU calculation point (Decision 2019/665), they fall sharply: Germany −14.3 points for plastics in 2022 (UBA); the Netherlands −22 to −30 points estimated by WUR for 2020. Measured composition data do exist: German LVP misthrows (~26 %), the Dutch non-packaging share (6-10 %), Belgian PMD misplacement (13.5 %), UK MRF sampling (input 84.8 % target; plastic output 89.4 % target) and French bale purity (Citeo ODQ). For France, the newest headline is **24 % sorting refus** for packaging (Citeo, Dec 2025, year not stated).

### Cited Findings

**France**
- Citeo infographic (Dec 2025): **"24 %"** "de taux de refus de tri en France des emballages". No data year or plastics-only figure is given. This updates the 23 % (2022) in the background README; the year must be confirmed. `[primary declared / secondary]` — [Citeo, 251218_CITEO_Infog_EMBALLAGES.pdf](https://citoyens.citeo.com/wp-content/uploads/2026/01/251218_CITEO_Infog_EMBALLAGES.pdf)
- Citeo Observatoire de la qualité 2023, English guide: method "Random selection of a bale or bulk pile to be analysed" (p. 43). Analyses run all year by V2R, Austral, Atlance and Terra in **123 sorting centres and 19 recyclers, 1,559 characterisations** (p. 8-9).
  - Per-stream analysis counts and compliance: clear PET 179 analyses (69 compliant, 70 close, 40 sub-standard); dark PET 78; **PE/PP/PS rigid 138 analyses, of which 76 sub-standard** (88.1 % average target content); PE films 6 compliant / 8 close / 33 sub-standard (82 % average).
  - **No moisture threshold or measured moisture is given for plastics**, and no recycler-side plastic measurements are reported (moisture is given only for steel, aluminium and paper). `[primary measured]` — [Citeo-Guide_ODQ_2023_English.pdf](https://bo.citeo.com/sites/default/files/2024-07/Citeo-Guide_ODQ_2023_English.pdf)
- Citeo, *Écoconception et recyclage des emballages en PET opaque 2011-2022* (May 2022):
  - About 70,000 t/yr of coloured PET packaging on the market, of which "56 % de ces emballages sont triés par les consommateurs et recyclés" (p. 13).
  - Opaque PET in coloured PET bales averaged **14 % in 2017** against a COTREP maximum of 15 %, with peaks "parfois supérieures à 20%" (p. 5, 13). Bale composition was "analysed regularly by Citeo in sorting centres".
  - **No regeneration yields are given.** `[primary measured (bale composition) / declared]` — [RAPPORT_PET_opaque_Citeo_2022.pdf](https://www.citeo.com/wp-content/uploads/2026/02/RAPPORT_PET_opaque_Citeo_2022.pdf)
- Citeo CEPOM 2020-2021: **304 characterisations** (271 of residual household waste, 56.3 t; 33 of street bins, 3.3 t) across 12 regions. 90 % of the characterised residual-waste mass is above 50 mm, "la maille moyenne de retrait des fines en centre de tri" (p. 11). Plastic packaging recycled: **13.0 kg/inhabitant/yr in extended-sorting (ECT) areas vs 15.9 kg elsewhere** (p. 23). Gains are "moindre sur les sorties, compte tenu des taux de captage des centres de tri" (p. 23), but the capture rates are not quantified. `[primary measured (residual waste); declared (tonnages)]` — [20230117_Etude_CEPOM_Citeo.pdf](https://www.citeo.com/wp-content/uploads/2025/10/20230117_Etude_CEPOM_Citeo.pdf)
- ADEME *Bilan national du recyclage 2012-2021* (published 13 March 2024), via press: plastics collected for recycling "1,3 million de tonnes en 2021" (all plastics, not only household packaging); plastic collection rate about **25 % in 2020**; recycled plastic incorporation rate "estimé à 14% en 2020". `[secondary]` — [Banque des Territoires, 18/03/2024](https://www.banquedesterritoires.fr/recyclage-des-plastiques-metaux-ou-textiles-encore-des-progres-faire-selon-un-bilan-dresse-par)

**Germany**
- ZSVR (Central Agency Packaging Register), press conference 27/01/2026, data year 2024, from dual systems' volume-flow reports "aggregated and examined by ZSVR":
  - Plastic participation volume (licensed, essentially household) **1,080,147 t**; plastic sent for mechanical recycling **764,508 t**; mechanical recycling rate **70.78 %** (2018: 42.1 %; statutory target 63 %) (p. 14). This rate is measured at transfer to the recycler, **not at the EU calculation point**. `[primary declared, ZSVR-audited]`
  - LVP share transferred for recovery: **52.55 %** of collected LVP (p. 10).
  - LVP composition (CHI cyclos-HTP basis analysis on 2.6 Mt, 2017, chart dated Dec 2025): recyclable plastic 36 %, recyclable metal/paper 25 %, non-recyclable plastic 13 %, **sorting errors (misthrows) 26 %**. The label-to-value mapping was inferred from listing order by the reading tool and **needs visual confirmation** (p. 10). `[primary measured]`
  - Practice study 2023/2024 (preliminary), "full survey of facilities receiving dual-system waste": probability of high-quality recycling for **rigid PE 93 %, rigid PP 92 %, transparent PET bottles 81 %, films 82 %, rigid PS 63 %, small flexible PE 50 %, flexible PP 27 %, PET trays 13-64 %, other plastics 0 %** (p. 15). `[primary declared]`
  - Source: [ZSVR, 20260127_PK_2026_Packaging_recycling_fact_check.pdf](https://www.verpackungsregister.org/fileadmin/files/Presse/20260127_PK_2026_Packaging_recycling_fact_check.pdf)
- ZSVR factsheet on LVP sorting: "more than 2.63 million tonnes of waste in yellow bags and bins in Germany annually", "approx. 31 kg per year and capita", 43 sorting plants, up to 17 fractions, 27-50 NIR units per plant. "For recyclable packaging, modern sorting facilities achieve sorting rates of more than 95%" (cyclos-HTP sortability chart). This is a design-for-recycling **potential**, not a plant-measured average. `[secondary/declared]` — [Factsheet_Sorting_lightweight_packaging.pdf](https://www.verpackungsregister.org/fileadmin/files/Erklaermaterialien/Factsheet_Sorting_lightweight_packaging.pdf)
- UBA Texte 125/2022 (practice of sorting and recovery, data 2020/2021): questionnaire to **40 LVP sorting plants**, with reference plants per fraction (films 21, PE 20, PP 17, PET 6, PS 3). "P(ASuV) für Kunststofffolien beträgt knapp über 80 %." PP/HDPE rigid >90 %; PS ~62 %; MPO/PO-flex ~30 %. "Für transparente PET-Flaschen beträgt die Spannbreite 73,1 % – 83,0 %." "Für sonstige formstabile PET-Verpackungen wurde eine Spannbreite von 2,6 % – 25,3 % bestimmt." EPS 0 %. Washing practice: "Bei den PET-Verwertern ist eine Heißwäsche weiterhin generelle Praxis." `[primary declared]` — [UBA Texte 125/2022](https://www.umweltbundesamt.de/sites/default/files/medien/1410/publikationen/2023-01-05_texte_125-2022_praxis_der_sortierung_und_verwertung_von_verpackungen.pdf)
- UBA Texte 156/2024 (GVM, Germany 2022, all plastic packaging, not household only):
  - "In 2022 wurden von den dualen Systemen 1.180 kt Altkunststoffe aus Verpackungen einer Verwertung zugeführt." "Insgesamt wurden 2.120 kt Kunststoffverpackungen stofflich verwertet" (65.9 %); 1,090 kt energy recovery (p. 25).
  - At the EU calculation point, plastics "-412 kt (-14,3 %-Punkte im Vergleich zur alten Methode)" (p. 29). [calcul] This gives about 51.6 %.
  - Tables 69-70 (recyclate yield per dual-system sorting fraction, standard loss rates) exist (p. 218 ff.) but were not readable. `[primary declared + modelled]` — [UBA Texte 156/2024](https://www.umweltbundesamt.de/sites/default/files/medien/11850/publikationen/156_2024_texte_verpackungsabfaelle_2022.pdf)
- Conversio, *Stoffstrombild Kunststoffe in Deutschland 2023* (short version):
  - Post-consumer plastic waste **5.58 Mt**, of which packaging 3.07 Mt and household-near packaging **1,967 kt**. Mechanical recycling of packaging 1,578 kt (51.4 %), of which household-near packaging **943 kt**.
  - Input to mechanical recycling in Germany 2.54 Mt (PCR + PIR); recyclate output 2.01 Mt, of which PCR 1.64 Mt. "Prozessverluste: Einsatz für die energetische Verwertung/EBS ~0,53 Mio. t" (p. 17).
  - Method: survey of ~50 producers, ~300 processors/recyclers responding out of 2,000+ invited, ~50 expert interviews, statistics and modelling; survey March-July 2024. `[primary declared + modelled]` — [Conversio Kurzfassung 2023](https://vci.de/ergaenzende-downloads/kurzfassung-stoffstrombild-2023.pdf)
  - [calcul] Recycler output/input, all plastics PCR + PIR in Germany: 2.01/2.54 ≈ **79 %**; process losses 0.53/2.54 ≈ **21 %**. [calcul] Household-near packaging sent to mechanical recycling: 943/1,967 ≈ **48 %** (input to recycling, not output).

**Netherlands**
- Afvalfonds Verpakkingen, *Monitoring verpakkingen 2020*:
  - Plastic placed on market 554 kt. Collected **461 kt** (395 kt source-separated + 66 kt post-separated), of which **316 kt from households** (Tables 4, 5, 5.2). **Delivered for recycling 368 kt** (Table 6). Recycling rate 66 % (2020), 54 % (2019) (Tables 7-8).
  - "het recyclingpercentage van kunststof verpakkingen moest worden bijgesteld van 57% naar 54%" after data verification (p. 6). ILT inspection of the 2019 plastics results (p. 12). 2020 includes "een incidentele groei van ca. 5 procentpunten" from 2019 stocks (p. 27).
  - Corrections: non-packaging share from sorting studies "in 2019 9,8% en in 2020 6,3%"; correction "voor het aandeel niet-verpakkingen en de gemeten afwijkingen van de gestelde DKR-norm voor vervuiling" (p. 27). Sorting studies by "Verschillende externe onderzoeksbureaus" commissioned by Nedvang (p. 34).
  - WUR estimate for the new EU measuring point: **−22 to −30 percentage points**, i.e. 46-52 % (Table 8, p. 31). `[primary declared + primary measured composition corrections]` — [Monitoren 2020](https://www.verpact.nl/sites/default/files/2022-03/Monitoren%202020.pdf)
  - [calcul] Delivered for recycling / collected = 368/461 ≈ **80 %**, i.e. about 20 % removed at sorting (residue + moisture/dirt not shipped). This is inflated by the 2019 stock effect.
- WUR presentation (Thoden van Velzen, 17/11/2022): "45% gerecycled, 55% verbrand", with no year or method stated. `[secondary]` — [edepot.wur.nl/581168](https://edepot.wur.nl/581168)
- WUR Report 2275 (beverage cartons, 2022): **378 kt PMD** collected in 2020 (CBS). PMD composition (2016 sampling): **66.4 % plastic** at object level (Table 6). `[primary measured (composition) / declared]` — [edepot.wur.nl/567789](https://edepot.wur.nl/567789)

**Belgium**
- Fost Plus 2022: plastic packaging recycling rate "rose from 52% in 2021 to 61% in 2022"; PMD collected "rose from 14.9 kg per person in 2018 to 22.8 kg per person in 2022" (new blue bag). `[primary declared]` — [Fost Plus press release](https://fostplus.prezly.com/fost-plus-recycled-95-of-all-household-packaging-in-2022)
- Fost Plus via Belga (23/09/2026): "Around 41,660 tonnes of waste are wrongly placed in Belgium's PMD bags each year", "accounting for 13.5% of the total collected". Sorting-error cost "€40 million in 2025" (~€1,000/t). Measurement method not described. `[secondary]` — [Brussels Times](https://www.brusselstimes.com/2329327/nearly-42000-tons-of-waste-incorrectly-disposed-as-pmd-annually-in-belgium)
- Fost Plus (19/02/2024): "around 35,000 tonnes of PMD waste per year from the five Fost Plus sorting centres" go to residue post-sorting (Vanheede, from 2025); the residue "still contains around 30 to 40% recyclable material". `[primary declared]` — [Fost Plus / Vanheede](https://fostplus.prezly.com/vanheede-signs-contract-with-fost-plus-for-post-sorting-35000-tonnes-of-pmd-residue)

**United Kingdom** (Materials Facility regulations: operators sample input and output; sampling "every 125 tonnes" since October 2016; data on WRAP's portal; self-reported, EA/NRW oversight)
- Q2 2018, 101 MRFs in England and Wales: plastic had the lowest target-material share in output in England, **89.4 %**. England input: 84.8 % target, **9.3 % non-recyclable, 5.9 % non-target**. Plastic was 14 % of MRF input. `[primary measured, operator self-sampling]` — [letsrecycle, 13/11/2018](https://www.letsrecycle.com/news/mrf-material-quality-continues-downward-trend/)
- Q1 2017: "The average percentage of target material of responding MFs is 90.3 % or higher for all of the four main SOM"; plastics 13.5 % of input; input non-target 5.9 %, non-recyclable 8.1 %. `[primary measured]` — [letsrecycle](https://www.letsrecycle.com/news/latest-news/mrf-quality-report-shows-little-change-on-target-material)

**Switzerland**
- KuRVe (Carbotech/UMTEC for BAFU, 13/07/2017, data 2016): Swiss households use **302,000 t** of plastic packaging; about **68,000 t** collected separately (50,000 t PET bottles, ~18,000 t other plastics). "Verwertungsquote > 80%" for PET. Mixed collections produce "grosse Mengen an Ausschüssen" that are incinerated, **but the text gives no share**; recycling and loss shares appear only in charts (Fig. 2-3, p. 7-8). Collection rates of 70 % / 35 % are assumptions. Method: MFA from literature and "ausführliche Stakeholderbefragung". `[modelled / declared]` — [KuRVe report](https://www.bafu.admin.ch/dam/bafu/de/dokumente/abfall/externe-studien-berichte/studie-kurve.pdf.download.pdf/KuRVe_Bericht_%C3%B6ffentlich_Deutsch.pdf)
- OST/UMTEC KuRVe factsheet: net cost of mixed collection "300 CHF/t bis 700 CHF/t, im Mittel rund CHF 500 pro Tonne Kunststoff", versus 250 CHF/t for municipal incineration (KVA). No yield figures. `[secondary]` — [OST factsheet](https://www.ost.ch/fileadmin/dateiliste/3_forschung_dienstleistung/institute/umtec/factsheets/rohstoffe_und_verfahrenstechnik/250304_kurve.pdf)

### Inferences
- In Germany, the 70.78 % (ZSVR) and 65.9 % (UBA) headline rates are **input-to-recycler** figures. The −14.3 points at the calculation point (UBA) imply that about **22 %** of the plastic delivered to recyclers is lost before the calculation point (14.3/65.9) [calcul]. This matches Conversio's ~21 % process losses and the ~20-30 % recycler losses in PRE and WUR.
- In the Netherlands, the WUR estimate of −22 to −30 points against a 66 % input-to-recycler rate implies **33-45 %** of what is delivered to recyclers does not reach the calculation point [calcul]. This is higher than Germany, consistent with the large Dutch mixed-plastics (DKR 350) fraction (Brouwer: mix 47 of 105 Gg sorted products).
- Measured non-target shares in the separately collected input are consistent across countries: about **6-15 %** (NL non-packaging 6-10 %; UK non-target 5.9 % + non-recyclable 8-9 %; Belgium 13.5 %), with Germany's LVP misthrows higher at about 26 % (to be confirmed).
- France's 23-24 % refus rate is in the same order as these misthrow shares plus sorting losses. It applies to a multi-material stream, however (see Q3).

### Gaps
- **France: no national measured figure for (a) plastics captured into bales / plastics entering sorting, (b) recycler yields, or (c) a declared quantity at the EU calculation point split by polymer.** Citeo's "15-20 %" plastic loss at sorting (ECT 2020) remains an estimate.
- The data year of the 24 % refus figure (Citeo Dec 2025) is unknown.
- German per-fraction recyclate yields (UBA 156/2024 Tab. 69-70) were not accessible. They are the most directly relevant official numbers and should be retrieved manually.
- UK: no recent (2022-2025) MF portal values were extracted. The [data.gov.uk dataset "Materials Facility Waste Returns Data January 2022 to December 2023"](https://ckan.publishing.service.gov.uk/dataset/51dc5123-961f-4d64-b753-13b375a4ebf3) exists but was not read.
- Austria (ARA), Italy (COREPLA), Spain (Ecoembes) and the Nordics were not covered within the call budget.
- Belgium: the Fost Plus total PMD tonnage and the plastic share of the sorting residue were not found in the pages read.

---

## 3. How do sources define and measure "sorting residue" and "recycler losses", and how comparable are they with France?

### Takeaway
Definitions differ on four points, and the differences change the results by tens of percentage points:
- **the denominator**: multi-material input, plastics only, net packaging or gross weight;
- **whether moisture and dirt are counted**;
- **the point of measurement**: delivered to recycler, or the EU calculation point;
- **how the figure is obtained**: operator annual averages, sampling, or lab tests.

French refus (23-24 %) is a share of the **whole multi-material yellow-bin input** (incl. paper/cardboard in most areas). It is not comparable with Dutch or German plastic-only residue shares or with polymer-specific sorting efficiencies. Only Citeo's "15-20 % of plastics entering" is conceptually comparable, and it is an estimate.

### Cited Findings
- **Antonopoulos 2021**: "sorting rate" = share of a polymer in MRF input that ends up in its target output; "recycling rate" at the recycling plant = output/input. Both are operator-reported annual averages. The authors explicitly contrast them with "controlled sampling" in Eule (2013) and Mastellone et al. (2017) (Sec. 3.1). — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8162419/fullTextXML) `[primary declared]`
- **WUR/Brouwer**: everything is expressed both as **gross** weight and **net packaging** (nKV, packaging polymer excluding moisture, dirt, non-packaging). Sorting residue is reported together with "moisture and dirt". Recycling outputs are split into **main product, side product and process waste**. "Net material yield" = main products / net packaging potential. The reconciled practice figure (~40-50 %) "valt hoger uit" because it counts moisture, dirt and residual waste and excludes process losses. — [WUR 1823](https://edepot.wur.nl/450447) `[modelled]`
- **Lab moisture measurements** (Dutch sorted products): dry matter 87-99 %. Moisture alone can therefore represent **1-13 %** of a bale's mass. — [Thoden van Velzen et al. 2017](https://edepot.wur.nl/430783) `[primary measured]`
- **Netherlands official**: "delivered for recycling", corrected for the non-packaging share and "gemeten afwijkingen van de gestelde DKR-norm voor vervuiling"; recycler losses deducted under the new method ("gecorrigeerd voor de productie uitval bij de recyclers"). — [Monitoren 2020](https://www.verpact.nl/sites/default/files/2022-03/Monitoren%202020.pdf) `[primary declared]`
- **Germany official**: ZSVR rate = mechanical transfer volume / participation volume (transfer to recycler). The UBA/GVM calculation-point rate deducts recycler losses with average recyclate yields per sorting fraction and standard loss rates (Tables 69-70, unread). The practice study P(ASuV) = probability that a packaging type is sorted **and** recycled, from operator questionnaires. — [ZSVR](https://www.verpackungsregister.org/fileadmin/files/Presse/20260127_PK_2026_Packaging_recycling_fact_check.pdf); [UBA 156/2024](https://www.umweltbundesamt.de/sites/default/files/medien/11850/publikationen/156_2024_texte_verpackungsabfaelle_2022.pdf); [UBA 125/2022](https://www.umweltbundesamt.de/sites/default/files/medien/1410/publikationen/2023-01-05_texte_125-2022_praxis_der_sortierung_und_verwertung_von_verpackungen.pdf)
- **Collection perimeters**:
  - Germany LVP = plastics + metals + beverage cartons, paper separately (blue bin). ZSVR composition includes "recyclable metal/paper 25 %" (p. 10).
  - Netherlands PMD since the portfolio expansion = plastics + metal + drink cartons (Brouwer 2019). PMD is 66.4 % plastic by object (WUR 2275).
  - Belgium new blue bag P+MD = plastics + metals + drink cartons.
  - UK = commingled dry recyclables including paper and often glass, with plastic **13.5-14 %** of MRF input.
  - France: yellow bin is multi-material in most areas. Plastics are only ~12 % of refus by composition (OCAPEM, background README).
  - Sources: [Brouwer 2019](https://tore.tuhh.de/handle/11420/3415); [WUR 2275](https://edepot.wur.nl/567789); [letsrecycle 2018](https://www.letsrecycle.com/news/mrf-material-quality-continues-downward-trend/)
- **UK MF regulations**: three categories are measured in the input: target, non-target (recyclable but not targeted) and non-recyclable. Output is measured as % target material per Specified Output Material. — [letsrecycle 2018](https://www.letsrecycle.com/news/mrf-material-quality-continues-downward-trend/) `[primary measured]`
- **Fines threshold, France**: about 50 mm is the "maille moyenne de retrait des fines en centre de tri" (CEPOM p. 11). Germany has shifted toward coarser 40-60 mm meshes, and no LVP plant now operates without fine screening (UBA 125/2022, p. 21-22). Everything below the mesh goes to residue by construction. — [CEPOM](https://www.citeo.com/wp-content/uploads/2025/10/20230117_Etude_CEPOM_Citeo.pdf); [UBA 125/2022](https://www.umweltbundesamt.de/sites/default/files/medien/1410/publikationen/2023-01-05_texte_125-2022_praxis_der_sortierung_und_verwertung_von_verpackungen.pdf)
- **Deloitte 2017** counted "only net resin weight" and assumed a 10 % refusal rate, while noting that large refusal volumes are exported. — [Deloitte 2017](https://cewep.eu/wp-content/uploads/2025/04/pre-blueprint-packaging-waste-2017.pdf) `[modelled]`

### Inferences
- To compare France with Germany, the Netherlands or Belgium, French refus must be converted to a plastics basis. With 23 % refus of total CS input and ~12 % plastic packaging in refus (background README, OCAPEM, fragile), plastics in refus ≈ 28 kg per tonne of CS [calcul, from background]. Converting this into "% of plastics entering" requires the plastic share of French CS input, which was not found in a measured national form. Citeo's 15-20 % estimate is the only available number.
- Dutch and German sorting residue figures (plastic-dominated streams) include misthrows (non-packaging, organics, textiles) that in France are also part of refus. On a plastics-only basis, the Dutch **~11 % of net packaging lost at sorting** (WUR 1823, 2014) is the best measured-and-reconciled analogue. Citeo's 15-20 % is higher, consistent with ECT bringing in small and flexible formats (Van Eygen: small films 34 % sorting efficiency; OCAPEM: 0 % capture under 20 mm).
- Moisture (1-13 %) and non-target material (bale purity 82-98 %) together explain much of the "recycler loss" in output/input yields. Gross-weight yields (PRE 69-73 %) and net-polymer yields (WUR lab: "close to 100%" for PE) are therefore both correct but measure different things.

### Gaps
- No French document defines the "taux de refus" denominator and mass-balance closure (weighbridge in/out, stock variation) in a way that could be checked; the background README's Citeo sources give rates but not the protocol.
- No source found measures moisture in French plastic bales (Citeo ODQ sets none for plastics).
- The text of Decision (EU) 2019/665 and of the EU guidance on the calculation point was not re-read here (see background README).

---

## 4. What is the measured overall chain yield (recycled output / plastic collected) per polymer, and what share of losses is contamination vs non-target material vs moisture vs fines?

### Takeaway
**No source gives a fully measured per-polymer chain yield (recycled output per tonne collected).** The closest are reconciled Dutch models anchored on measured compositions. For separate collection they give about **48 % main recycled product per tonne gross collected** (2014) [calcul]. Per stream, main product / gross sorted product is PET ~76 %, PE ~80 %, PP ~78 %, film ~69 % and mixed ~37 % [calcul]. The EU operator-declared medians imply about **69-75 % for PET/HDPE and ~42 % for PP and films** from MRF input to recyclate [calcul]. For the loss split, measured fragments exist:
- moisture 1-13 % of bale mass (lab, NL);
- non-target material in bales 2-18 % (FR ODQ) or 2-35 % (EU operators);
- misthrows in collection 6-15 % (NL, UK, BE), ~26 % for German LVP (to be confirmed);
- fines below 20 mm: 0 % capture, below 50 mm largely lost (FR, background).

There is no single source that splits total losses into these categories.

### Cited Findings
- **NL 2014, separate collection, per polymer** (WUR 1823 Fig. 2 values; [calcul] ratios): main washed product / gross sorted product = PET 6.6/8.7, PE 8.1/10.1, PP 9.4/12, film 18/26, mix 17/46. Average main-product polymer purity 91 ± 6 %; valuable products only 94 ± 5 %. — [edepot.wur.nl/450447](https://edepot.wur.nl/450447) `[modelled on measured compositions]`
- **NL 2014, measured purity of washed products** (NIR, n = 1 each): PET 97.2 %, PE 90.6 %, PP 90.6 %, film 76.4 %, mix 32.6 % (separate collection). — [Brouwer 2018](https://edepot.wur.nl/426558) `[primary measured]`
- **NL 2017**: net recycling yield 26 ± 2 %; rejects and sorting residues 70 Gg gross vs recycled 103 Gg net. — [Brouwer 2019](https://tore.tuhh.de/handle/11420/3415) `[modelled]`
- **Lab wash yields, NL sorted products (dry basis)**: main product 83-94 %; sludge 0.7-6 %; dissolved 2-10 %; non-target polymer side streams up to 11 % (PET SC floating) and 32 % (mixed plastics sinking). — [Thoden van Velzen 2017](https://edepot.wur.nl/430783) `[primary measured]`
- **EU medians, sorting rate × recycler yield** (Table 2): PET 85 % × 81 %, HDPE 85 % × 88 %, PP 64 % × 66 %, films 59 % × 71 %, PS 37 % × 66 %. — [Antonopoulos 2021](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8162419/fullTextXML) `[primary declared]`
- **Germany, probability of being sorted and recycled** (practice study 2023/2024, preliminary): rigid PE 93 %, rigid PP 92 %, transparent PET bottles 81 %, films 82 %, rigid PS 63 %, small flexible PE 50 %, flexible PP 27 %, PET trays 13-64 %. These are **for packaging that reached LVP**, not per tonne collected. — [ZSVR 2026](https://www.verpackungsregister.org/fileadmin/files/Presse/20260127_PK_2026_Packaging_recycling_fact_check.pdf) `[primary declared]`
- **Germany, recycler output/input, all plastics** [calcul]: 2.01/2.54 = 79 %, with ~0.53 Mt process losses to energy recovery. — [Conversio 2023](https://vci.de/ergaenzende-downloads/kurzfassung-stoffstrombild-2023.pdf) `[primary declared + modelled]`
- **Austria 2013**: sorting efficiency by format, PET bottles/large products 73-88 %, small hollow bodies 47 %, small films 34 %, others 12 %. Recycling losses ≈ 24 % of sorted material [calcul]. — [Van Eygen 2018](https://repositum.tuwien.at/bitstream/20.500.12708/5424/2/Eygen%20Emile%20van%20-%202018%20-%20Management%20of%20plastic%20wastes%20in%20Austria%20analysis%20of%20the...pdf) `[modelled]`
- **Loss components, measured fragments:**
  - **Moisture**: 1-13 % of sorted-product mass (NL lab). Brouwer 2018 model: 18.7 Gg moisture and dirt in 105.4 Gg gross sorted products (~18 %) [calcul]. — [Thoden van Velzen 2017](https://edepot.wur.nl/430783); [Brouwer 2018](https://edepot.wur.nl/426558)
  - **Non-target material in bales**, France 2023 (ODQ): PET clear 4 %, PET dark 3.1 %, PE/PP/PS 11.9 %, PE/PP films 9.9 %, PE films 18 % [calcul, 100 − target]; plus opaque PET in coloured PET bales 14 % on average in 2017. — [Citeo ODQ guide](https://bo.citeo.com/sites/default/files/2024-07/Citeo-Guide_ODQ_2023_English.pdf); [Citeo PET opaque](https://www.citeo.com/wp-content/uploads/2026/02/RAPPORT_PET_opaque_Citeo_2022.pdf) `[primary measured]`
  - **Non-target material in bales**, EU operators: PET down to 65 % purity at one MRF; films 82-98 %; PP ~10 % and films up to 20 % impurity "accepted by the market". — [Antonopoulos 2021](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8162419/fullTextXML) `[primary declared]`
  - **Misthrows / non-packaging in collection**: NL 9.8 % (2019) and 6.3 % (2020); BE 13.5 %; UK non-recyclable 8-9 % + non-target ~6 % (all-material MRF input); DE LVP "sorting errors" 26 % (mapping to be confirmed); single Belgian/Dutch MRF sample 15.7 wt % non-packaging in mixed post-sorting product. — [Monitoren 2020](https://www.verpact.nl/sites/default/files/2022-03/Monitoren%202020.pdf); [Brussels Times](https://www.brusselstimes.com/2329327/nearly-42000-tons-of-waste-incorrectly-disposed-as-pmd-annually-in-belgium); [letsrecycle](https://www.letsrecycle.com/news/mrf-material-quality-continues-downward-trend/); [ZSVR](https://www.verpackungsregister.org/fileadmin/files/Presse/20260127_PK_2026_Packaging_recycling_fact_check.pdf); [Schmuck 2026](https://paperity.org/p/371222354/analysis-of-trade-offs-of-post-sorting-plastic-packaging)
  - **Recyclable material left in residue**: Belgian PMD residue (35,000 t/yr from five centres) "still contains around 30 to 40% recyclable material". — [Fost Plus](https://fostplus.prezly.com/vanheede-signs-contract-with-fost-plus-for-post-sorting-35000-tonnes-of-pmd-residue) `[primary declared]`
  - **Fines**: France, ~50 mm average fines-screen mesh (CEPOM). Germany, 40-60 mm (UBA 125/2022). — [CEPOM](https://www.citeo.com/wp-content/uploads/2025/10/20230117_Etude_CEPOM_Citeo.pdf); [UBA 125/2022](https://www.umweltbundesamt.de/sites/default/files/medien/1410/publikationen/2023-01-05_texte_125-2022_praxis_der_sortierung_und_verwertung_von_verpackungen.pdf)

### Inferences
- **Indicative per-tonne-collected chain** (separate collection of plastic packaging, Dutch-type plastics-dominant stream, 2014 reconciled data) [calcul]:
  - about 160 kg sorting residue + moisture/dirt not shipped;
  - about 840 kg sorted products;
  - about 476 kg main recycled flakes (≈ 435 kg of target polymer at 91 % purity);
  - about 194 kg by-products (mixed polyolefins / non-target polymers, often energy use or low-grade);
  - about 89 kg process waste;
  - the balance (~80 kg) is moisture/dirt removed in washing.
- This is consistent with the background README's French scenario B (550-620 kg/t of plastic entering sorting for rigids, 400-425 kg/t for films). **The Dutch reference applies to the whole collected mix (all polymers incl. ~45 % mixed plastics), not to a single polymer**, which is why it is lower than the rigid-polymer French estimate.
- For a pyrolysis feedstock assessment, the **non-main-product fractions** per tonne gross of plastics-dominant separately collected material total about **52 %** (65 of 124 kt) [calcul, NL 2014, WUR 1823]. They break down as:
  - sorting residue + moisture/dirt not shipped: ~16 % (20 kt);
  - recycler by-products: ~19 % (24 kt; mostly polyolefin/non-target polymer fractions, i.e. plastic-rich);
  - process waste: ~9 % (11 kt);
  - unaccounted, mainly moisture/dirt removed at washing: ~8 % (10 kt).

  Only part of this is plastic, and measured French equivalents do not exist.
- Losses cannot be cleanly split into contamination, non-target material, moisture and fines from any single measured source. The best available decomposition combines NL lab data (moisture, sludge, dissolved, non-target polymers) with French ODQ bale purities and OCAPEM refus composition (background README).

### Gaps
- **No measured per-polymer chain yield per tonne collected exists for France.** No French recycler (Valorplast-contracted regenerators, Paprec, Suez, Veolia) publishes input/output mass balances. Searches for Valorplast or COTREP regeneration yields returned nothing usable.
- No EU source publishes a measured split of recycler losses by cause (labels/caps vs moisture vs fines vs non-target polymers) at industrial scale. Only lab data (NL) and qualitative PRE statements exist.
- German Tables 69-70 (UBA 156/2024: average recyclate yield per dual-system sorting fraction, standard loss rates) would provide official per-fraction yields. **Not accessed; high priority for manual retrieval.**
- Not read: Brouwer et al. 2020 (*Sustainability* 12, 10021; Dutch 2017 flows and technical-limit scenario), Klotz et al. 2022 (Swiss dataset), the full texts of Picuno 2021 and Van Eygen et al. 2018 (per-polymer transfer coefficients), and Faraca & Astrup (Denmark).
