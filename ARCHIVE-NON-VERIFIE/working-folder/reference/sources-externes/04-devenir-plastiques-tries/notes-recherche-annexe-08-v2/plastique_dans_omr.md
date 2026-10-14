# Plastic in French residual household waste (OMR): tonnages, split, fate and cost (France and Île-de-France)

Reading notes, session of 10/10/2026. Status labels: `mesuré`, `déclaré`, `modélisé`, `secondaire`, `ancien` (data before 2018). **[calcul]** marks a figure derived by me, with its inputs shown. Page numbers come from text extraction and may be off by one.

**Access limits in this session (they affect what was verified):**
- The WebSearch budget ran out after about 10 queries.
- These sources were blocked by an unanswered permission prompt, so I did **not** re-read them: INSEE Première 2055, the Eurostat API env_waspac, the ADEME "indicateurs clés DMA" page, the Commission "plastics own resource" page, and the MODECOM 2017 report (AMF mirror).
- The full MODECOM 2024 report (cycl-op.org mirror) was blocked by robots.txt. I read the **synthèse** (obdec-normandie mirror) and the **ADEME open data** instead.
- Where I use a figure from the project's earlier source register (`/home/claude/background-earlier-research/registre-sources.yaml`, verified by an earlier session on 10/10/2026), it is labelled "**registre, non relu ici**".

---

## Q1. MODECOM 2024: plastic categories and shares in OMR, kg/hab and tonnes, compared with 2017

### Takeaway
The ADEME open data give plastics as **2,329,258 t (15.8 % of OMR, 35.28 kg/hab/yr)** in mainland France (2024 campaign, extrapolated to 2023 OMR tonnage). This total splits into 14 sub-categories:
- **Films: 1.28 Mt** (55 % of OMR plastics). Bin bags alone are 0.50 Mt.
- **Rigids: 1.05 Mt**.
- **Packaging: about 1.60 Mt** (68.5 %), counting shopping bags as packaging, which is how ADEME's own Figure 12 counts them. Non-packaging is **about 0.73 Mt**, mostly bin bags.

The figures are wet weights as collected. Measured moisture (35.8 % for films, 20.1 % for other plastics) brings the total to **about 1.66 Mt dry** [calcul]. The 2017 values were 14.7 % to 15 %, about 37 kg/hab and about 2.4 Mt. Plastic per inhabitant has therefore fallen slightly, while plastic's share has risen slightly because the OMR total fell faster.

### Cited Findings

**Campaign and base (synthèse)**
- MODECOM 2024 is ADEME's 4th national campaign, after 1993, 2007 and 2017. Publication ref. **013089**, put online 19/12/2025. The library page lists rapport, résumé, synthèse and an infographic — [ADEME librairie](https://librairie.ademe.fr/economie-circulaire-et-dechets/8784-modecom-2024-campagne-nationale-de-caracterisation-des-dechets-menagers-et-assimiles.html) (`déclaré`).
- Methodology, from the synthèse:
  - OMR: 100 samples planned in 50 communes (2 per commune); 5 removed as outliers, so **95 analysed**.
  - CSM: 50 samples.
  - Moisture measured on 20 OMR samples, PCI on 15.
  - Standards NF X30-413 and NF X30-408; fieldwork in 2024; confidence intervals given as ±½ IC 95 %.
  - Source: [ADEME, MODECOM 2024 synthèse, p. 11, 14, 25](https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf) (`mesuré`).
- Extrapolation base (synthèse p. 39 table, "DMA SPGD", France métropolitaine):
  - OMR **14,752,013 t = 223.46 kg/hab/yr** in 2023.
  - 2017: 16,337,249 t = 252.75 kg/hab.
  - Multimatériaux (packaging + paper) collected separately: 3,488,675 t (52.84 kg/hab) in 2023.
  - Source: [synthèse p. 39](https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf) (`déclaré`, from the Enquête Collecte 2023).
  - The implied population is about 66.0 M **[calcul: 14,752,013 / 223.46]**.
- Unlike 2007 and 2017, the 2024 campaign characterises household and assimilated (business) waste collected by the public service **together**: "A key change … household waste and business-type waste collected through the public service will be characterized together rather than as separate streams" (paraphrase of the article) — [Déchets Infos, 13/03/2024](https://dechets-infos.com/modecom-national-la-campagne-2024-est-lancee-4930699.html) (`secondaire`). ADEME attributes 80 % of OMR to households and 20 % to activities (Figure 24, p. 27, MODECOM 2017 basis) — [ADEME, Déchets chiffres-clés 2023 (copy)](https://www.ecologic-france.com/images/medias/document/21269/dechetsdeeechiffres-cles-2023ademe.pdf) (`déclaré`).

**Open-data composition (dataset `omrcs-compo-jdd`; labels from grid `omrcs-grille`)**
- Category 07 = "Plastiques" in the grid (14 categories in all; 07 has 14 sub-categories) — [ADEME open data, grille](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-grille/lines?format=csv&size=200) (`déclaré`).
- Values, read from the CSV columns `pourcentage_OMR`, `tonnage_OMR`, `IC_tonnage_OMR`, `ratio_OMR` and `tonnage_CSM` — [ADEME open data, omrcs-compo-jdd](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv&size=100) (`mesuré`, 2024 campaign):

| Code | Grid label (verbatim) | % OMR | OMR t (± ½ IC) | kg/hab/yr | Same item in CS multimatériaux (t) |
|---|---|---|---|---|---|
| 07.01 | « Sacs poubelles » | 3,4 % | 496 503 (± 51 719) | 7.52 | 18 462 |
| 07.02 | « Autres sacs plastiques » (sacs de courses…) | 1,1 % | 165 000 (± 46 301) | 2.50 | 19 574 |
| 07.03 | « Films plastiques d'emballage » | 4,2 % | 619 942 (± 99 068) | 9.39 | 135 773 |
| 07.04 | « Bouteilles et flacons pour boissons en PET » | 1,1 % | 160 966 (± 29 153) | 2.44 | 174 077 |
| 07.05 | « Bouteilles et flacons en PET (autres que boissons) » | 0,3 % | 51 533 (± 19 020) | 0.78 | 28 408 |
| 07.06 | « Bouteilles et flacons en polyoléfines pour boissons » | 0,2 % | 23 899 (± 6 704) | 0.36 | 26 843 |
| 07.07 | « Bouteilles et flacons en polyoléfines (autres que boissons) » | 0,3 % | 44 178 (± 11 698) | 0.67 | 54 959 |
| 07.08 | « Boites, caisses, casiers, pots, barquettes, gobelets » | 3,0 % | 443 885 (± 44 509) | 6.73 | 135 705 |
| 07.09 | « Autres bouteilles, flacons, bonbonnes » (PVC, PAN…) | 0,0 % | 5 461 (± 4 384) | 0.08 | 2 867 |
| 07.10 | « Bouchons, couvercles, capsules » | 0,3 % | 40 401 (± 47 340) | 0.61 | 8 087 |
| 07.11 | « Autres emballages plastiques » (calages, PSE, blisters…) | 0,3 % | 40 123 (± 15 086) | 0.61 | 11 921 |
| 07.12 | « Jouets composés majoritairement de plastique » | 0,1 % | 14 665 (± 6 983) | 0.22 | 4 621 |
| 07.13 | « Articles de sport et de loisirs composés majoritairement de plastiques » | 0,0 % | 5 254 (± 4 928) | 0.08 | 498 |
| 07.14 | « Autres plastiques » (tuyaux, brosses, boîtes hermétiques…) | 1,5 % | 217 448 (± 32 113) | 3.29 | 69 292 |
| **07** | **Total plastics** | **15,8 %** | **2 329 258** | **35.28** | **691 087 [calcul]** |

- The sub-category sum equals 2,329,258 t and 35.28 kg/hab **[calcul]**. This matches the background figure (15.8 %, 2,329,258 t).
- Aggregates **[calcul from the table above]**:

| Group | Codes | OMR t | kg/hab | Share of OMR plastics | Share of OMR |
|---|---|---|---|---|---|
| Films (all) | 07.01-07.03 | 1,281,445 | 19.41 | 55.0 % | 8.7 % |
| — of which bin bags (non-packaging) | 07.01 | 496,503 | 7.52 | 21.3 % | 3.4 % |
| — packaging films (incl. shopping/carrier bags) | 07.02-07.03 | 784,942 | 11.89 | 33.7 % | 5.3 % |
| Rigids (all) | 07.04-07.14 | 1,047,813 | 15.87 | 45.0 % | 7.1 % |
| — rigid packaging | 07.04-07.11 | 810,446 | 12.28 | 34.8 % | 5.5 % |
| — bottles and flasks (PET + polyolefin) | 07.04-07.07 | 280,576 | 4.25 | 12.0 % | 1.9 % |
| — PET bottles and flasks | 07.04-07.05 | 212,499 | 3.22 | 9.1 % | 1.4 % |
| — polyolefin bottles and flasks | 07.06-07.07 | 68,077 | 1.03 | 2.9 % | 0.5 % |
| — pots, trays, boxes, cups | 07.08 | 443,885 | 6.73 | 19.1 % | 3.0 % |
| **Packaging total** | 07.02-07.11 | **1,595,388** | **24.17** | **68.5 %** | **10.8 %** |
| **Non-packaging** (bin bags, toys, sport, other) | 07.01, 07.12-07.14 | **733,870** | **11.11** | **31.5 %** | **5.0 %** |

- The synthèse confirms how ADEME groups packaging. Figure 12, p. 20 (CSM materials in OMR, kg/hab/yr, 2017 → 2024) gives:
  - « Bouteilles plastiques » 4.5 → **4.3**;
  - « Autres emballages plastiques » 21.4 → **19.9**;
  - « Emballages cartons » 15.6 → 13.9; « Papiers » 18.8 → 10.6; total CSM-type material in OMR 71.7 → 59.4.
  - Source: [synthèse p. 20](https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf) (`mesuré`).
  - 4.3 = 07.04-07.07 (4.25), and 19.9 = 07.02 + 07.03 + 07.08-07.11 (19.92) **[calcul]**. **ADEME therefore counts carrier bags (07.02) as packaging**, which gives 24.2 kg/hab of plastic packaging in OMR.
- Quote from the synthèse: "Les quantités d'emballages ménagers jetés avec les OMR ont également diminué (- 4,1 kg/hab./an soit une baisse de 8 %)" (p. 20). Also: CSM-type material is "26 % des OMR (soit 59 kg/hab./an)", and "69,1 % des déchets collectés au sein des OMR n'y ont pas leur place" (p. 17) — [synthèse](https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf) (`mesuré`).

**Moisture and PCI of the plastic fractions (dataset `omrhum`)**
- Films fraction S09 (07.01-07.03) = 8.6 % of OMR, moisture **35.8 %** (± 4.81).
- Other plastics fraction S10 (07.04-07.14) = 7.0 % of OMR, moisture **20.1 %** (± 2.77).
- Mean OMR moisture: 42.1 % (± 5.78).
- Source: [ADEME open data, omrhum](https://data.ademe.fr/data-fair/api/v1/datasets/omrhum/lines?format=csv&size=100) (`mesuré`, n = 20).
- The synthèse (Tableau 1, p. 23) gives the 2017 values: films 27.9 % ± 2.0; other plastics 18.0 % ± 1.8. The authors warn the results should be read "avec beaucoup de prudence" — [synthèse p. 23](https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf) (`mesuré`).
- Dry-basis plastics **[calcul: wet tonnage × (1 − moisture)]**:
  - films 1,281,445 × 0.642 ≈ **823 kt**;
  - rigids 1,047,813 × 0.799 ≈ **837 kt**;
  - total **≈ 1.66 Mt dry**;
  - packaging only (07.02-07.03 at 35.8 %, 07.04-07.11 at 20.1 %) ≈ **1.15 Mt dry**;
  - non-packaging ≈ 0.51 Mt dry.
  - "Dry" still includes adhering non-water soiling.
- PCI: films 27,808 J/g dry matter ± 2,940 (2024), versus 35,489 J/g in 2007 (Tableau 2, p. 24) — [synthèse](https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf) (`mesuré`). The 2024 "autres fractions plastiques" PCI came out garbled ("2,641") and must be checked on the PDF.

**Comparison with 2017**
- An ADEME presentation of MODECOM 2017 results reads: "Plastiques : 15 %" of OMR (p. 19). It warns that falling shares of other materials raise the plastics share, which "ne signifie pas nécessairement une augmentation des gisements associés" (p. 21) — [ADEME, R. Desplats, 04/07/2019, via SINOE](https://www.sinoe.org/documents/consult-and-count-doc/doc/1263/rubrique/7) (`mesuré`, `ancien` for 2017 data).
- MODECOM 2017 report (ref. 011318), Tableau 2 p. 13: "Plastiques 14,7 % des OMR, 37,3 kg/hab, 2 410 kt ; humidite 36,9 %" — [registre, non relu ici; URL medias.amf.asso.fr/upload/files/modecom_2017_analyse_des_resultats_011318.pdf] (`mesuré`, `ancien`).
- Cross-check: 14.7 % × 16,337,249 t ≈ 2.40 Mt, and 14.7 % × 252.75 ≈ 37.2 kg/hab **[calcul]**. Both are consistent with the register.
- Change 2017 → 2024 **[calcul]**:
  - total plastics: about 37.3 → 35.3 kg/hab (−5 %), about 2.41 → 2.33 Mt;
  - plastic packaging: 25.9 → 24.2 kg/hab (Fig. 12).
  - Caveat: the household and assimilated perimeter was merged in 2024 (see above).
- Press coverage of the 2024 results gives no plastic-specific figures; it reports only "une diminution des papiers et emballages (-17%)" — [Localtis, 07/01/2026](https://www.banquedesterritoires.fr/tri-des-dechets-menagers-du-mieux-mais-les-marges-de-progression-restent-importantes) (`secondaire`).
- The ORDIF presentation (ADEME, 23/06/2026), slide 14, says: "27 % correspondent à des déchets qui auraient dû être triés dans le bac jaune". It gives no plastic split. Slide 13 says: "Des TV composés de 18% de plastiques & de 23,5% de matières minérales" (déchèterie tout-venant, not OMR) — [ADEME at ORDIF, 23/06/2026](https://www.ordif.fr/fileadmin/DataStorageKit/ORDIF/Event/2026_06_23/2026_01.3_ADEME_MODECOM_2024_VF.pdf) (`mesuré`). The synthèse gives 17.6 % plastics in tout-venant (Figure 25, p. 35).
- From 2026 to 2028, ADEME will run three campaigns (60 communes and 60 déchèteries per year, results averaged over three rolling years). The 2026 programme is 40 OMR samples in 20 communes (slides 16-18) — [ADEME at ORDIF](https://www.ordif.fr/fileadmin/DataStorageKit/ORDIF/Event/2026_06_23/2026_01.3_ADEME_MODECOM_2024_VF.pdf) (`déclaré`).

### Inferences
- Bin bags are **21 % of the plastic mass in OMR** (0.50 Mt). They are non-packaging and cannot be recycled. Any project that counts "plastics in OMR" as a recyclable or pyrolysable resource should treat them separately. Their 35.8 % moisture belongs to the whole film fraction, and bags are probably soiled by contents.
- Plastic packaging alone in OMR is about 1.60 Mt wet and about 1.15 Mt dry. That is about 68 % of OMR plastics by wet mass.
- Films dominate the mass (55 %) but carry the most water and soiling. Rigid packaging (0.81 Mt wet) is the cleaner part of the resource.
- The 2024 "assimilés included" perimeter means the 2.33 Mt is plastic in the public-service grey bin, households and small businesses together. It is not household plastic only.
- No polymer split exists beyond PET and polyolefin bottles (about 212 kt PET and 68 kt PO). Pots, trays and films are not split by resin.

### Gaps
- The full MODECOM 2024 report (19.7 MB) was not read; robots.txt blocked the mirror. Its Figure 8 values (1993/2007/2017/2024 plastics in kg/hab) and any typology breakdown (urban/rural, ECT) are therefore missing.
- No polymer split (PE/PP/PS/PET/PVC/multilayer) of films or pots and trays in French OMR was found. The UBA Restmüllanalyse (Germany) was not reached because of the search budget, so I have no foreign proxy either.
- The MODECOM 2017 sub-category split (films vs rigids vs packaging) was not re-read; the AMF mirror was blocked.

---

## Q2. Plastic packaging that "escapes" sorting (CEPOM, Citeo), and the recyclable share

### Takeaway
- Citeo's CEPOM study (2020-2021, 271 OMR characterisations) found about **14 kg/hab/yr of plastic packaging in OMR on a dry basis** (19 kg wet, against 24 kg in MODECOM 2017). It found **13.0 kg/hab in areas with extended sorting instructions (ECT) and 15.9 kg/hab outside them**.
- MODECOM 2024 measures 24.2 kg/hab wet, about 1.6 Mt (about 1.15 Mt dry) **[calcul]**. All plastic packaging falls under the sorting instruction since ECT became national.
- MODECOM-implied capture rates into separate collection are **about 50 % for bottles but only about 19 % for other plastic packaging** (ADEME p. 31, reproduced by my calculation). So about 80 % of non-bottle plastic packaging, by mass, goes to the grey bin.
- No source splits OMR plastic packaging into "recyclable in practice" and "non-recyclable".

### Cited Findings
- **CEPOM method:** "a été réalisée sur l'ensemble du territoire français métropolitain (hormis la Corse"; February 2020 to August 2021 (no measurements March-September 2020); **304 characterisations (271 OMR, 33 street bins), about 60 t sorted** (56.3 t OMR); 77 packaging and paper categories, 71 sorted above 50 mm and 6 between 20 and 50 mm (p. 2-4) — [Citeo, étude CEPOM](https://www.citeo.com/wp-content/uploads/2025/10/20230117_Etude_CEPOM_Citeo.pdf) (`mesuré`).
- **CEPOM results:**
  - Packaging and paper in OMR: "54 kg par habitant et par an" (dry, excluding moisture), about 25 % of OMR weight, out of 262 kg/hab of OMR. Nationally, "3,5 millions de tonnes" could additionally be sorted (p. 9).
  - Plastic packaging about **14 kg/hab dry**; wet, **19 kg (CEPOM) against 24 kg (MODECOM 2017)** (charts p. 12-15).
  - ECT vs non-ECT territories: plastic packaging **13.0 vs 15.9 kg/hab**; the text says "13 kg/hab/an d'emballages plastiques encore à trier" (p. 22-23).
  - Packaging and paper not capturable at the sorting centre (< 50 mm): 2.1 vs 2.8 kg/hab. "90 % du contenu des OMr caractérisées sont des éléments supérieurs à 50 mm" (p. 10-11).
  - Source: [CEPOM](https://www.citeo.com/wp-content/uploads/2025/10/20230117_Etude_CEPOM_Citeo.pdf) (`mesuré`, 2020-2021).
  - Caveat: a chart label reads "Dont emballages plastiques : 0,4 %", which conflicts with 14 kg/hab. It is probably a sub-fraction (fines) and must be checked on the PDF.
- CEPOM scaled to France: 14 kg × 66.0 M ≈ 0.92 Mt dry; 19 kg wet ≈ 1.25 Mt **[calcul, population implied by MODECOM]**.
- **MODECOM 2024 capture rates (synthèse p. 31):** « bouteilles plastiques 50 % ; autres emballages plastiques 19 % » — [synthèse](https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf) (`mesuré`/`modélisé`).
- These rates can be reproduced from the open data as CSM / (CSM + OMR) **[calcul]**:

| Item | Captured in CSM | Left in OMR | Capture rate |
|---|---|---|---|
| Bottles 07.04-07.07 | 284,287 t | 280,576 t | 50 % |
| Other plastic packaging 07.02-07.03 + 07.08-07.11 | 313,927 t | 1,314,812 t | 19 % |
| PET beverage bottles 07.04 | 174,077 t | 160,966 t | 52 % |
| Pots and trays 07.08 | 135,705 t | 443,885 t | 23 % |
| Packaging films 07.02-07.03 | 155,347 t | 784,942 t | 17 % |

  Source data: [ADEME open data](https://data.ademe.fr/data-fair/api/v1/datasets/omrcs-compo-jdd/lines?format=csv&size=100).
- MODECOM separate collection (CSM): 52.8 kg/hab, of which 42.7 kg conforming and 10.2 kg non-conforming. The non-conforming share was 19 % in 2024 against 12.4 % in 2017. Footnote 19 says: "Ce taux peut différer du taux de refus des centres de tri" (20 mm mesh against about 50 mm at sorting centres). Conforming plastics in CSM: bottles 4.3 kg, other plastic packaging 4.8 kg (2017: 4.6 and 2.1) — [synthèse p. 27-28](https://obdec-normandie.org/sites/obdec/files/2026-01/ADEME-MODECOM-2024-caracterisation-dechet-synthese.pdf) (`mesuré`).
- **Citeo statements:**
  - "99% des emballages sont captés par les différents dispositifs de collecte, de tri et de ramassage" (p. 6). This means captured by some collection system, including the grey bin; it is not a sorting rate.
  - Household plastic packaging placed on the market: 1,165 kt (2024) and 1,174 kt (2025). Recycled from separate collection: 324 kt (2024) and 346 kt (2025) (p. 13, 29).
  - Recyclability of plastic packaging rose from 65 % to 75 % between 2020 and 2025 (p. 5).
  - Citeo pays a support for "valorisation énergétique des emballages restés dans les OMR" (SVE OMR) of **15.0 M€ (2024) and 9.9 M€ (2025)**, and 12.3 / 12.0 M€ for packaging in sorting rejects (p. 28).
  - Source: [Citeo, Rapport d'activité 2025](https://www.citeo.com/wp-content/uploads/2026/06/Rapport-dactivite-2025_Citeo.pdf) (`déclaré`).
- Household plastic packaging not recycled: 1,174 − 346 = **828 kt (2025)** **[calcul from Citeo]**.

### Inferences
- **Recyclable vs non-recyclable split:**
  - By the sorting instruction, essentially all 1.60 Mt of plastic packaging in OMR "should" have gone to the yellow bin: ECT has been national since 2023, and ADEME counts carrier bags as packaging.
  - By technical recyclability, the defensible "escaped recyclable" core is:
    - bottles and flasks, 0.28 Mt wet (established PET/PEHD outlets);
    - part of pots and trays (0.44 Mt, PP/PE/PS/PET mix; PS and PET trays depend on surtri);
    - the larger PE films.
  - Small films, multilayers and PVC are recyclable mainly on paper. Applying Citeo's 75 % recyclability-by-design rate (a placed-on-market metric) to the 1.60 Mt would give about 1.2 Mt **[calcul, crude, not a measured split]**.
- **Mass-balance tension:** MODECOM's dry packaging (about 1.15 Mt) is larger than Citeo's household plastic packaging not recycled (828 kt). Plausible reasons:
  - (a) MODECOM 2024 includes assimilated business waste (about 20 % of OMR);
  - (b) "dry" still includes food residues;
  - (c) ±½ IC of ±99 kt on films alone;
  - (d) perimeter differences (carrier bags and non-household packaging).
  - CEPOM's 0.92 Mt dry (households, 2020-21) sits between the two.
- The SVE OMR support fell 34 % between 2024 and 2025. That may reflect a scale change rather than fewer tonnes; no tonnage basis is published.

### Gaps
- No Citeo or ADEME figure states "X kt of plastic packaging in the grey bin, of which Y kt recyclable". No study was found that splits OMR plastic packaging into recyclable and non-recyclable fractions.
- The CEPOM breakdown of plastic packaging by type (bottles, pots, films) in OMR could not be extracted from the PDF text.

---

## Q3. Île-de-France: characterisations, OMR tonnage, UVE treatment, cost per tonne

### Takeaway
- Île-de-France collected **3.2 Mt of OMR in 2024 (258 kg/hab)**. About **90 % of residual waste goes to 18 incinerators (17 UVE)**, which have 4.28 Mt/yr of authorised capacity.
- **No recent region-wide characterisation exists** (ORDIF). Regional plastic figures are therefore estimates: applying MODECOM 2024 gives **about 0.44 Mt (per-capita basis) to 0.51 Mt (percentage basis) of plastic in Île-de-France OMR**, about 0.40-0.46 Mt of it incinerated **[calcul]**.
- For the Syctom alone (1.68 Mt of OMR), plastic is about 0.27 Mt **[calcul]**.
- Cost: Syctom charges 109.4 €/t of OMR (2024). The ORDIF regional average treatment cost was 115 €/t (2022). Net UVE costs were 44-97 €/t, TGAP included (2022).

### Cited Findings

**Regional totals (ORDIF)**
- 2024 data:
  - Population 12,419,961.
  - "Le tonnage atteint 3,2 millions de tonnes, contre 3,17 millions de tonnes en 2023"; 258 kg/hab, about 59 % of DMA.
  - "Les déchets résiduels de l'Île-de-France sont à 90 % acheminés vers 18 unités d'incinération", of which "17 d'entres elles présentent une performance permettant de les qualifier d'unité de valorisation énergétique (UVE)".
  - Authorised incineration capacity 4,275,900 t (about 80 % used).
  - DMA treatment: incineration 63.2 % (3,419,422 t); ISDND 7.1 % (382,433 t); other (methanisation, CSR) 1.4 %.
  - "Il n'existe pas de caractérisation récente représentative de l'ensemble de l'ile-de-France" (slide 18).
  - Source: [ORDIF, Bilan DMA 2024, slides 2, 9, 11, 15-16, 18, 26](https://www.ordif.fr/fileadmin/DataStorage/user_upload/00-home/Bilan_DMA_2024%40.pdf) (`déclaré`).
- ORDIF summary page: OMR reached 258 kg/hab, up 2 kg/hab. Residual waste with refus and bulky waste reaches 303 kg/hab. Capacity is 4.3 Mt, falling to 4.07 Mt with the new Ivry plant and a third furnace at Créteil — [ORDIF, DMA 2024 page](https://www.ordif.fr/nos-ressources/publications/les-dechets-menagers-assimiles-en-ile-de-france-2024/) (`déclaré`).
- **Only regional composition (old):** ORDIF's 2022 report says OMR contain "plus de 55 %" recyclable materials. Its chart shows « Plastiques recyclables 3% », with putrescibles 27 %, paper 11 %, cardboard 8 % and non-recyclable residue 45 %. These come from a **2014 characterisation "corroborated" by MODECOM 2017**. Same report: "avec 3,32 Mt d'Omr (268 kg/hab)" in 2022, and residual flows "à 94 % acheminé vers 18 unités d'incinération" (p. 19-21) — [ORDIF, Rapport DMA 2022](https://www.ordif.fr/fileadmin/DataStorage/user_upload/ORDIF_Rapp_DMA_2022_V1b.pdf) (`déclaré`, `ancien` for the 2014 composition).
- On that basis, 3 % "recyclable plastics" × 3.2 Mt ≈ 96 kt **[calcul]**. This covers recyclable plastic only (under the pre-ECT definition), not all plastic.

**Syctom (Paris and 81 communes)**
- 2024:
  - OMR "1 683 105 t" (+0.62 %), 5,692,272 inhabitants, 296 kg/hab (p. 16, 20-21).
  - UVE tonnages incinerated: **Saint-Ouen (L'Étoile Verte) 547,463 t** (capacity 650,000); **Ivry/Paris XIII 627,290 t** (730,000); **Isséane 536,000 t** (536,000). Total 1,710,753 t **[calcul]** (p. 10).
  - "112 218 t" of OMR, rejects and sorting refusals went to storage, not split by category (p. 17).
  - Tariff to members: **OMR 109,4 €/t**; encombrants 109.4; collecte sélective 25.4; "anomalies de tri" 129.4. The report says Syctom pays TGAP to the State but **not whether the tariffs include it** (p. 23).
  - CO2: 615,236 t CO2e from UVE and external centres (p. 17).
  - OMR composition chart p. 22 (garbled in extraction): "73,8 % du contenu d'une poubelle d'OMr pourraient être détournés de l'incinération"; no plastic share legible.
  - Source: [Syctom, Rapport d'activité 2024](https://www.syctom-paris.fr/fileadmin/user_upload/RA_Syctom_2024_exe_BD_Pap_VERSION_FINALE.pdf) (`déclaré`).
- 2025:
  - OMR "1 671 121 t" (−0.71 %), "293,7 kg/an par habitant.e".
  - OMR composition chart headed "Ordures ménagères résiduelles (OMr) Moyenne des caractérisations 2020-2025": "35% papiers et emballages légers"; "24% déchets organiques"; "6% emballages en verre"; "6% déchets avec filière de reprise"; "29% déchets sans filière de reprise". **No separate plastic figure.**
  - "71 % du contenu d'une poubelle d'OMr pourrait être détourné de l'incinération".
  - "Le Syctom évalue ainsi son besoin de traitement externe à 270 000 tonnes" (forward-looking).
  - Treatment of all Syctom waste: 60.5 % energy recovery, 29.3 % material and organic recovery, 10.1 % landfill.
  - Footprint 758,971 t CO2e, of which 724,311 t from treatment (p. 28-31).
  - Source: [Syctom, Rapport d'activité 2025](https://www.syctom-paris.fr/fileadmin/user_upload/SYCTOM_RA_exe_2026_DEF_WEB.pdf) (`déclaré`; the composition is `mesuré` with undescribed method).

**Costs (Île-de-France)**
- ORDIF cost reference (2022 data, published October 2024):
  - "le coût aidé hors taxes moyen en Île-de-France des OMR était de 52 € par habitant et 191 € par tonne";
  - "le 1er poste de dépense est le traitement avec un coût moyen de 115 € par tonne";
  - incineration: "Si les coûts complets d'incinérations vont de 85 € à 149 € par tonne", net costs "de 44 € à 97 € par tonne (y compris TGAP)" (p. 14, 17).
  - Source: [ORDIF, Notice référentiel des coûts](https://www.ordif.fr/fileadmin/DataStorageKit/ORDIF/Etudes/pdf/Notice_reference_couts_VF.pdf) (`déclaré`).

**Plastic in Île-de-France OMR, estimates [calcul, `modélisé`]**

| Basis | Inputs | Result |
|---|---|---|
| National % applied | 3.2 Mt × 15.8 % | ≈ 506 kt |
| National kg/hab applied | 35.28 kg × 12,419,961 hab | ≈ 438 kt |
| Syctom, % basis | 1,683,105 t × 15.8 % | ≈ 266 kt |
| Plastic packaging only, kg/hab basis | 24.17 kg × 12.42 M | ≈ 300 kt |
| Plastic packaging only, % basis | 10.8 % × 3.2 Mt | ≈ 346 kt |
| Incinerated share | 90 % of the total-plastic range | ≈ 0.39-0.46 Mt/yr |

### Inferences
- Île-de-France OMR per capita (258 kg; Syctom 294-296 kg) is well above the national 223 kg. Paris-area OMR probably include more assimilated waste, and the yellow-bin performance is weak: Citeo ranks Île-de-France last, per the background report. The percentage basis (about 0.5 Mt) is therefore probably closer than the per-capita basis, but no measurement confirms this.
- Syctom's 1.71 Mt incinerated in 2024 implies about 0.27 Mt of plastic burnt in its three UVEs, if the OMR plastic share applies to all inputs **[calcul: 1,710,753 × 15.8 %]**. UVE inputs also include refus and encombrants, which may be more plastic-rich.
- A plastic tonne in Syctom OMR costs member authorities 109.4 €/t, the same as any OMR tonne. Plastic carries no specific price signal.

### Gaps
- No public characterisation of Île-de-France OMR since 2014. The Syctom's 2020-2025 average gives no plastic line.
- I found no tonnage list for the 15 non-Syctom UVEs in Île-de-France (Créteil, Argenteuil-Azalys, Carrières-sur-Seine, Massy, Sarcelles, Rungis, Vaux-le-Pénil, Saint-Thibault, Monthyon, Montereau, Thiverval, etc.). It was not found in ORDIF's 2022 or 2024 documents.
- I could not find whether the Syctom's 109.4 €/t includes TGAP.

---

## Q4. Fate of plastic in OMR nationally (incineration, landfill, MBT, CSR) and fossil-CO2 cross-check

### Takeaway
Nationally, about two-thirds of OMR are incinerated (almost all with energy recovery), about a quarter landfilled and about 7-8 % sent to MBT. Applying these shares to MODECOM's 2.33 Mt gives about **1.58 Mt of plastic incinerated, 0.54 Mt landfilled and 0.17 Mt through MBT/organic treatment** each year **[calcul]**. MBT rejects end in landfill or incineration; no tonnage was found. No French source states plastic's share of UVE fossil CO2. The EU-wide fossil share of municipal incineration CO2 is 47 %, and AMORCE says "half" of UVE energy is biogenic.

### Cited Findings
- **OMR destinations:**
  - ADEME: "67% sont orientés vers la valorisation énergétique ou l'incinération," "24% directement vers le stockage," "8% vers le traitement mécano-biologique (TMB) suivi de compostage ou méthanisation." The section is headed "OÙ VONT NOS DÉCHETS?…"; the block is not explicitly labelled OMR and has no year (2021 collection data are nearby). Same document: "« poubelle grise » 246kg/hab" (2021) (p. 18-19). "Le nombre d'UIOM avec production d'énergie est passé de 109 en 2000 à 117 en 2022"; 12.4 Mt incinerated with energy recovery in 2022 (provisional); 497 kt diverted to landfill or other plants in 2022 because of stoppages and saturation (p. 35). Source: [ADEME, Déchets chiffres-clés 2024, synthèse (copy)](https://batisseurs-outremer.com/wp-content/uploads/2025/01/ChiffresclesDechets-Synthese2024-012515.pdf) (`déclaré`).
  - INSEE: "En 2021, 67,9 % des ordures ménagères résiduelles sont destinées à l'incinération, 23,1 % au stockage, 7,2 % à la valorisation organique" — Insee Première 2055, figures 2-3 [registre, non relu ici; URL insee.fr/fr/statistiques/8574484] (`déclaré`). This confirms the ADEME 67/24/8 split refers to OMR.
- **Plastic in OMR by route [calcul: 2,329,258 t × INSEE 2021 shares, assuming the same plastic share on every route]:**

| Route | All OMR plastics | Packaging only (1,595,388 t × same shares) |
|---|---|---|
| Incineration (67.9 %) | ≈ 1.58 Mt | ≈ 1.08 Mt |
| Landfill (23.1 %) | ≈ 0.54 Mt | ≈ 0.37 Mt |
| Organic recovery / MBT (7.2 %) | ≈ 0.17 Mt | ≈ 0.11 Mt |

  Plastics passing through MBT are mostly screened out as rejects (destination not quantified).
- **SDES:** "Les déchets ménagers et assimilés, en raison de leur composition hétérogène, et les résidus de tri ne sont pas recyclés." Plastic waste counted separately is 2,482 kt in 2022 (380 kt from households), and "Le taux de recyclage des plastiques est de 20 %" (Tableau 2). This 2,482 kt does not include plastic inside mixed household waste (category "Déchets ménagers et similaires", 20,835 kt) — [SDES, Bilan 2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline) (`déclaré`).
- **UVE fleet:**
  - AMORCE: 2020 tonnage "pour un tonnage total incinéré de 14,57 Mt", stable "autour de 14,5 Mt depuis une dizaine d'années"; 118 installations in Table 1 (17 electricity, 15 heat, 84 cogeneration, 2 without recovery) (p. 8-10).
  - AMORCE: "le tri des plastiques notamment engendre une tendance à la baisse du PCI des ordures résiduelles" (p. 8, note 7), and "la moitié de l'énergie issue de l'incinération des ordures ménagères et assimilées" comes from the biodegradable fraction (p. 8).
  - Source: [AMORCE, DT139](https://amorce.asso.fr/publications/performances-recettes-et-couts-des-unites-de-traitement-thermique-des-dechets-donnees-2020-2021-dt139/download) (`déclaré`).
  - ADEME: 14.5 Mt of non-hazardous, non-mineral waste incinerated and 17.4 Mt landfilled in 2020 (ITOM) (p. 4) — [ADEME, Déchets chiffres-clés 2023](https://www.ecologic-france.com/images/medias/document/21269/dechetsdeeechiffres-cles-2023ademe.pdf) (`déclaré`).
- **Fossil CO2:**
  - EU municipal incineration emitted 85 Mt CO2e in 2024 (ETS monitoring), of which **39.4 Mt fossil (47 %)** and 45.6 Mt biogenic.
  - CEWEP's own estimate: 42.431 Mt of fossil CO2 for 81.32 Mt of waste treated (EU27), about 0.52 t fossil CO2 per tonne **[calcul]**.
  - France on the CEWEP map: 116 plants, 14.0 Mt thermally treated (pairing uncertain in the jumbled extraction). No France fossil split; no plastic attribution.
  - Source: [CEWEP/ESWET, 26/03/2026](https://www.cewep.eu/wp-content/uploads/2026/04/FULL-Slides_CEWEPESWET-Event-WasteEUETS_26-3-26.pdf) (`modélisé`/`déclaré`).
- Syctom reports 615,236 t CO2e (2024) and 724,311 t CO2e (2025) from treatment, without a fossil/biogenic split (see Q3).

### Inferences
- **Fossil-CO2 cross-check (order of magnitude only):**
  - Plastics incinerated from OMR: about 1.58 Mt wet, about 1.13 Mt dry **[calcul: 1.58 × 1.66/2.33]**.
  - With an assumed carbon content of about 75 % of dry mass (a common default for plastics, **not re-read in this session**), that is about 3.1 Mt fossil CO2 per year **[calcul]**.
  - At the EU-average 0.52 t/t, French incineration (about 14-14.5 Mt) would emit about 7.3-7.5 Mt fossil CO2 **[calcul, EU factor applied to France]**.
  - OMR plastics would then be roughly 40 % of French UVE fossil CO2. The rest would come from plastics in other inputs (DAE, refus, encombrants), synthetic textiles and the fossil share of composites.
  - This is plausible but rests on unverified factors. It cannot validate the 1.58 Mt more tightly than ±30-50 %.
- **CSR:** no source quantifies CSR made directly from OMR. CSR in France is made mainly from DAE and sorting refus (background report: 370-510 kt consumed in 2021-2023). OMR plastic going to CSR is probably negligible today.
- **Landfilled plastic (about 0.5 Mt/yr)** is the share most exposed to the rising ISDND TGAP (background: 69 €/t in 2026). It is also the share that can be diverted without competing with UVE heat contracts.

### Gaps
- No French source (ADEME, FNADE, AMORCE, CITEPA) quantifying plastic's share of UVE input or of UVE fossil CO2 was read.
- No national tonnage of OMR-derived MBT rejects or OMR-derived CSR was found.
- The INSEE 2021 split and the ADEME "indicateurs clés DMA" (15.2 Mt OMR, 2023) were not re-read; the permission prompt timed out.

---

## Q5. Indirect national indicators: EU plastic own resource and Eurostat env_waspac

### Takeaway
The EU own resource charges **0.80 €/kg of non-recycled plastic packaging waste** (generated minus recycled, all packaging, household and commercial). **France receives no lump-sum reduction.** With Eurostat's 2023 French figures (2.43 Mt generated, 0.63 Mt recycled, from the project register), the non-recycled base is **about 1.80 Mt**, implying **about €1.44 bn for 2023** **[calcul]**. I could not read a French budget document or Commission table that states the actual amount.

### Cited Findings
- **Council Decision (EU, Euratom) 2020/2053, Art. 2(1)(c):** the resource applies "au poids des déchets d'emballages en plastique non recyclés produits dans chaque État membre"; "Le taux d'appel uniforme est de 0,80 EUR par kilogramme." Art. 2(2) lists annual lump-sum reductions for 17 Member States: Spain 142 M€, Italy 184.048 M€, Poland 117 M€, Romania 60 M€, and others. **France is not listed** — [EUR-Lex, CELEX 32020D2053](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32020D2053) (`déclaré`, official text).
- **Eurostat env_waspac, France, W150102 (plastic packaging), 2023:** "2 428 987 t generees ; 625 275 t recyclees (25,7 %) ; 1 213 829 t valorisees en energie" — [registre, non relu ici; URL ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_waspac?geo=FR&waste=W150102] (`déclaré`).
- The 25.7 % rate is confirmed: "France (25.7%)", among the lowest in the EU in 2023 (Figure 6) — [Eurostat, Packaging waste statistics](https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/10547.pdf) (`déclaré`).
- Derived figures **[calcul]**:
  - Non-recycled = 2,428,987 − 625,275 = **1,803,712 t**, × 0.80 €/kg = **≈ €1.443 bn** (2023 base).
  - Neither recycled nor energy-recovered = 2,428,987 − 625,275 − 1,213,829 = **589,883 t**, presumably landfill or other disposal.

### Inferences
- The two indirect national indicators bracket the OMR measurement consistently:
  - all non-recycled plastic packaging (household and commercial), about 1.80 Mt;
  - of which energy-recovered, about 1.21 Mt, and landfilled or other, about 0.59 Mt;
  - against MODECOM plastic packaging in public-service OMR of about 1.60 Mt wet (about 1.15 Mt dry);
  - against Citeo household plastic packaging not recycled, 0.83 Mt.
- The Eurostat landfill remainder (0.59 Mt) is close to my OMR-based landfill estimate for packaging (0.37 Mt) plus landfilled packaging in DAE and refus. The orders of magnitude agree.
- The €1.44 bn is paid from the State budget (within the "prélèvement sur recettes au profit de l'UE"). It is not charged to producers or to local authorities. Each extra tonne recycled saves the State €800, an incentive that does not reach the waste holder. This is an inference about the mechanism; I did not read a budget document confirming the accounting line.

### Gaps
- **The actual French plastic own-resource amount (€/yr)** was not found. The Commission page, the PLF "jaune budgétaire" (Relations financières avec l'UE), Sénat budget reports and Cour des comptes were all unreachable (search budget exhausted, permission timeouts). The €1.44 bn is a calculation from register data.
- Eurostat 2018-2022 and 2024 values for France were not re-read; the API was blocked.

---

## Q6. Cost per tonne paid for treating OMR (and hence the plastic it contains)

### Takeaway
The waste holder (the local authority) pays the OMR rate for plastic in the grey bin:
- **109.4 €/t at the Syctom (2024)**;
- **115 €/t average treatment cost in Île-de-France (2022)**;
- national medians of **107 €/t for incineration and 138 €/t for landfill (2023, TGAP included)**.

At the national median, the 2.33 Mt of OMR plastic costs about **€250-270 M per year** to treat **[calcul]**, on top of collection costs.

### Cited Findings
- Syctom: OMR **109,4 €/t** (2024); TGAP inclusion not stated (p. 23) — [Syctom RA 2024](https://www.syctom-paris.fr/fileadmin/user_upload/RA_Syctom_2024_exe_BD_Pap_VERSION_FINALE.pdf) (`déclaré`).
- ORDIF (2022 data): OMR treatment 115 €/t on average; net incineration cost 44-97 €/t including TGAP; full incineration cost 85-149 €/t; OMR "coût aidé" 191 €/t all items, 52 €/hab — [ORDIF notice](https://www.ordif.fr/fileadmin/DataStorageKit/ORDIF/Etudes/pdf/Notice_reference_couts_VF.pdf) (`déclaré`).
- National ADEME cost reference, 2023 data: median net cost of OMR treatment 107 €/t for incineration (n = 306), 138 €/t for landfill (n = 197), 156 €/t for MBT-composting (n = 44); € HT/t, TGAP included — [ADEME, Référentiel des coûts, données 2023](https://librairie.ademe.fr/societe-et-politiques-publiques/8811-10587-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-hexagonale-donnees-2023.html) (`déclaré`; figure 33 p. 36 per the background report; landfill and MBT values from the register, not re-read here).
- AMORCE: average UVE gate fee in 2021 of 76 €/t for public clients (range 36-128) and **133 €/t for private clients**, excluding transport. Operating charges about 55 €/t, by-product disposal 12 €/t, taxes 11 €/t (p. 32-33). TGAP on incineration at 1/1/2022: "18 € si A ou B, 14 € si C" — [AMORCE DT139](https://amorce.asso.fr/publications/performances-recettes-et-couts-des-unites-de-traitement-thermique-des-dechets-donnees-2020-2021-dt139/download) (`déclaré`).
- ADEME: TGAP on landfill of non-hazardous waste 52-61 €/t in 2023, 65 €/t from 2025; incineration 6-20 €/t in 2023 (p. 36-37) — [ADEME chiffres-clés 2024](https://batisseurs-outremer.com/wp-content/uploads/2025/01/ChiffresclesDechets-Synthese2024-012515.pdf) (`déclaré`).

### Inferences
- Plastic in OMR treatment cost **[calcul]**:
  - 1.58 Mt incinerated × 107 €/t ≈ €169 M;
  - 0.54 Mt landfilled × 138 €/t ≈ €74 M;
  - 0.17 Mt in MBT × 156 €/t ≈ €26 M;
  - total ≈ **€270 M/yr**, treatment only, at median costs, assuming uniform plastic share by route.
- In Île-de-France, about 0.44-0.51 Mt × about 110-115 €/t ≈ **€50-60 M/yr** **[calcul]**.
- These are costs of the mixed waste that contains the plastic. Treating plastic separately would avoid them only if the residual service were priced per tonne. The Syctom's 109.4 €/t is such a per-tonne price.

### Gaps
- No contract-level UVE gate fee for Île-de-France non-Syctom plants was found.
- I found no statement of whether the Syctom's 109.4 €/t includes TGAP.

---

## Q7. Foreign fallback data (Germany, Netherlands, Belgium, UK)

### Takeaway
Not researched in this session; the search budget was exhausted before I could reach the UBA Restmüllanalyse or Dutch, Belgian or UK residual-waste composition studies. French data cover the main sub-questions (total, films/rigids, packaging/non-packaging, bottles by PET/PO). Only the **polymer split of films and pots/trays** remains without a source, French or foreign.

### Cited Findings
- None read in this session for residual-waste composition abroad. The background report covers German, Dutch and Belgian **sorting residues**, not residual household waste.

### Inferences
- A polymer split for OMR films and trays would have to come from a German or Dutch residual-waste study, or from Citeo placed-on-market data by resin. This needs a follow-up search.

### Gaps
- UBA Texte (Siedlungsrestabfall-Zusammensetzung 2018-2020), the Dutch Rijkswaterstaat "samenstelling huishoudelijk restafval", the Flemish OVAM residual-waste analyses and the WRAP/Defra national compositional estimates were not reached. A new search turn is needed.
