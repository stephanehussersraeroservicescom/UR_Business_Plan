# Annex 3. Output Markets and Pricing

This annex sets out what the products of the Urban Rig are worth in France and Europe, who could buy them, under which specifications and legal status, and what the plant pays for the energy it buys. It relies on the measured product properties of Annex 2 and on the process description of Annex 1. Gate fees are covered by feedstock in Annexes 5 to 8.

## How to Read This Annex

OneWorld, the manufacturer of the Urban Rig, is the sponsor of this business plan (decision D-027). Its documentation is marked "OneWorld design data"; these are the company's own figures and have not been verified independently [hyp:D-027].

**Prices are inputs that the operator of the financial model can change** [hyp:D-030]. Each default price is the most recent published value found, shown with its basis: source, date, scope and currency. Prices linked to crude oil can be recalculated for another Brent price, for example 80 or 50 USD per barrel (Section 3.1.6) [hyp:D-030]. The ranges of earlier years are shown so that the operator can judge the default.

Each figure or fact is followed by a small link. It opens the evidence sheet: what the evidence shows, its confidence, the source document and its location, or the calculation. Sheets numbered 3.x belong to this annex; sheets numbered 2.x are those of Annex 2. All sheets are listed in the index of evidence sheets.

**A note on 2026 prices.** Oil prices are in a period of crisis: the Brent averaged 69.0 USD per barrel in 2025 and 116.8 USD in September 2026 [A3-BM-PINKSHEET-2026-10], and 128.53 USD in the week to 9 October 2026 [A3-DGEC-NPG-2026-10-09-COTATIONS]. Defaults based on the latest prices are therefore high; the sensitivity of Section 3.1.6 shows the effect of a lower oil price.

**Revision.** This version was revised after an independent check of the annex. The changes are listed, point by point, in the project's register of discrepancies for Annex 3.

## Key Messages

- **The oil is priced by fraction.** OneWorld design data split the oil into 80 % gas oil, 10 % light oil and 10 % heavy oil [calc:CALC-A1-OW16-PART-GAZOLE] [calc:CALC-A1-OW16-PART-HEATING] [calc:CALC-A1-OW16-PART-HEAVY]. Each fraction is benchmarked to its fossil equivalent: naphtha, gas oil and low-sulphur fuel oil [hyp:D-028].
- **At the latest prices, the benchmark value of the oil is 1,121 EUR/t; at a Brent of 80 USD it is 714 EUR/t, and at 50 USD 446 EUR/t** [calc:CALC-A3-HUILE-MOY-REF] [calc:CALC-A3-HUILE-MOY-BRENT80] [calc:CALC-A3-HUILE-MOY-BRENT50]. These are benchmarks before any quality discount; the discount is an operator input (Section 3.1.5).
- **As produced from municipal plastics, the oil is a hazardous waste fuel.** Its flash point is below 40 °C [CHIBA-JLOS-HUILES], and a liquid waste with a flash point below 60 °C is hazardous [A3-REG1357-2014-HP3]: it can only be delivered to a plant authorised to receive this hazardous waste for thermal treatment or co-incineration. It does not meet the gas oil or fuel oil specifications without refining, and its chlorine is 2.7 to 10.5 times the limit for use in a steam cracker without purification [calc:CALC-A3-CHLORE-TABA-BAS] [calc:CALC-A3-CHLORE-TABA-HAUT]. A French end-of-waste order exists for pyrolysis oil sent to a steam cracker, but only for sorted plastic waste [A3-ARRETE-SSD-HUILE-PYROLYSE-2024].
- **The char is a solid fuel for cement kilns.** Its energy content of 32,090 J/g [IZUMITEC-R35-339439] gives it a value of 123 to 255 EUR/t at parity with petroleum coke or coal [calc:CALC-A3-CHAR-PARITE-PETCOKE] [calc:CALC-A3-CHAR-PARITE-INSEE]. French cement plants aim to cover 80 % of their energy with alternative fuels by 2030 [A3G-FDR-DECARBONATION-CIMENT-2023]. Its chlorine content, the decisive acceptance criterion, is still to be measured.
- **Metals are priced at public scrap values:** 316.4 EUR/t for shredded steel scrap and 1,723 EUR/t for aluminium scrap, French exports in the first half of 2026 [A3H-COMEXT-MENSUEL-2025-2026].
- **On a plastic-only feed, the surplus gas can be sold, including its hydrogen** [hyp:D-031]. The gas holds about 13 kg of hydrogen per tonne of resin-rich feed [calc:CALC-A3-H2-KG-T-RESINE], worth 27 to 109 EUR per tonne before purification [calc:CALC-A3-H2-VAL-GRIS] [calc:CALC-A3-H2-VAL-HYDRIX].
- **No carbon credit is counted.** No mechanism open to the plant in France has an approved method for it today (Section 3.5) [hyp:D-028]. The CO2 avoided compared with incineration is shown for information: about 1,973 kgCO2e per tonne of resin-rich feed [calc:CALC-A3-CO2-NET-VS-INCIN].
- **Purchased energy:** electricity at 0.1212 EUR/kWh, excluding VAT [PRM-EUROSTAT-NRGPC205-ID-2025], or 8.73 EUR per tonne treated [calc:CALC-A3-ELEC-EUR-T]; fuel for start-up and for household waste feeds, where the gas does not cover the heat demand [hyp:D-029].

## 3.1 Pyrolysis Oil

### 3.1.1 Fractions and Their Outlets

According to OneWorld design data, the continuous plant has heating zones set at 150, 300, 450 and 600 °C [UR2000-JP-P08-SPEC]; separately, a solenoid valve separates gas oil and heavy oil by vapour temperature [OW-ENG-P14-P15-PROCEDE]. For a resin-rich feed, the design balance gives:

| Fraction (OneWorld) | Share of the oil | Outlet stated by OneWorld | Benchmark used here |
|---|---|---|---|
| Gas (diesel) oil | 80 % [calc:CALC-A1-OW16-PART-GAZOLE] | "Fuel for sale", or electricity sales [OW-ENG-P16-DEBOUCHES] | Gas oil, Rotterdam |
| Heating (light) oil | 10 % [calc:CALC-A1-OW16-PART-HEATING] | "Sale as heating fuel" [OW-ENG-P16-DEBOUCHES] | Naphtha, North-West Europe |
| Heavy oil | 10 % [calc:CALC-A1-OW16-PART-HEAVY] | "Sale as heating fuel" [OW-ENG-P16-DEBOUCHES] | Low-sulphur fuel oil, Rotterdam |

Why naphtha for the light fraction. In the Chiba distillations, the light fraction of each oil had a flash point of 16 to 18 °C [CHIBA-DISTILLATION], below the 38 °C minimum of jet fuel [ANCAP-JETA1-2026]. It is closer to a naphtha than to a kerosene.

Why the heavy fraction may be worth more. Plastic pyrolysis oils are often waxy. If the heavy fraction proves to be a paraffin wax, crude wax imported into the EU was worth 1,185.3 EUR/t in 2025 [A3F-COMEXT-PARAFFINES-2712-2024-2026]. The composition of the heavy fraction has not been analysed (request R-013); the fuel oil benchmark is kept as the default.

The only published precedent of fraction-by-fraction sales is the Sapporo plastic liquefaction plant (data of 2009): light oil sold at the value of imported naphtha, middle oil at 80 to 90 % of the price of A fuel oil, heavy oil at 80 to 90 % of the price of C fuel oil [A3F-SAPPORO-SPR-2009-PRIX-FRACTIONS]. The source is more than eight years old.

### 3.1.2 Specifications Compared with the Measured Oil

The measured properties are those of the two oils made from municipal waste at Noda (Annex 2, Section 2.4.1).

| Property | Urban Rig oil, municipal plastics | Gas oil (France) | Heavy fuel oil (France) | Steam cracker, end-of-waste without purification |
|---|---|---|---|---|
| Flash point | below 40 °C [CHIBA-JLOS-HUILES] | above 55 °C [A3-ARRETE-GAZOLE-1999-ANNEXE-I] | at least 70 °C [A3-ARRETE-FIOULS-LOURDS-2000] | not set [A3-ARRETE-SSD-HUILE-PYROLYSE-2024] |
| Sulphur | below 0.05 % and 0.06 % [CHIBA-JLOS-HUILES] | 10 mg/kg at most [A3-ARRETE-GAZOLE-1999-ANNEXE-I] | at most 1 %, 2 % or 4 % depending on grade [A3-ARRETE-FIOULS-LOURDS-2000] | 3,000 ppm [A3-ARRETE-SSD-HUILE-PYROLYSE-2024] |
| Density at 15 °C | 0.8642 and 0.8762 g/cm³ [CHIBA-JLOS-HUILES] | 820 to 845 kg/m³ [A3-ARRETE-GAZOLE-1999-ANNEXE-I] | not set | not set |
| Water | 0.13 % and 0.20 % [CHIBA-JLOS-HUILES] | 200 mg/kg at most [A3-ARRETE-GAZOLE-1999-ANNEXE-I] | 1.5 % at most [A3-ARRETE-FIOULS-LOURDS-2000] | not set |
| Nitrogen | 0.24 % and 0.43 %, i.e. 2,400 and 4,300 ppm [CHIBA-JLOS-HUILES] | not set | not set | 5,000 ppm; 10,000 ppm if purified [A3-ARRETE-SSD-HUILE-PYROLYSE-2024] |
| Chlorine | 0.137 % and 0.526 % [CHIBA-JLOS-HUILES] | no limit in the text read [A3-ARRETE-GAZOLE-1999-ANNEXE-I] | no limit in the text read [A3-ARRETE-FIOULS-LOURDS-2000] | sum of halogens 500 ppm; 30,000 ppm if purified [A3-ARRETE-SSD-HUILE-PYROLYSE-2024] |

Reading.

- **Gas oil and heating oil.** The oil fails the flash point, and its sulphur is up to 60 times the gas oil limit [calc:CALC-A3-SOUFRE-GAZOLE]. It needs refining (stabilisation, hydrotreatment) before it can be sold as a road or heating fuel.
- **Regulated heavy fuel oil.** The flash point is also too low for the French heavy fuel oil specification [A3-ARRETE-FIOULS-LOURDS-2000].
- **Fuel sold as a hazardous waste.** With a flash point below 40 °C [CHIBA-JLOS-HUILES], the oil is a hazardous waste (property HP 3, flash point below 60 °C) [A3-REG1357-2014-HP3]. An ordinary combustion plant cannot take it on the basis of its fuel list [ARRETE-2910-2018]; it must go to a plant authorised for the thermal treatment or co-incineration of this hazardous waste, such as a cement kiln with that authorisation, under an acceptance certificate. The 1,100 °C rule applies to hazardous waste with more than 1 % of halogenated organic substances expressed as chlorine [IED-2010-75-ART50]; the total chlorine measured, 0.137 % and 0.526 %, stays below 1 % even if all of it were organic [CHIBA-JLOS-HUILES]. This outlet is possible under conditions; no buyer has been identified.
- **Steam cracker.** Without purification, the chlorine of the municipal oils is 2.7 and 10.5 times the limit [calc:CALC-A3-CHLORE-TABA-BAS] [calc:CALC-A3-CHLORE-TABA-HAUT]; at the cracker inlet, the industrial threshold is 3 ppm [KUSENBERG-AICHE-2021]. Nitrogen was measured at 2,400 and 4,300 ppm, below the 5,000 ppm limit [CHIBA-JLOS-HUILES] [A3-ARRETE-SSD-HUILE-PYROLYSE-2024]; oxygen and metals, also limited, have not been measured (R-035).
- **Jet fuel.** No ASTM D7566 annex approving pyrolysis oil from plastics was identified in the accessible summary of the standard; the full standard has not been read [A3-ASTM-D7566-24]. Recycled carbon aviation fuels must save at least 70 % of emissions [A3-RCF-2023-1185]. This outlet is not open in the short term.

**What opens or closes each market.**

| Market | Conditions | Measured oil (municipal plastics) | Conclusion |
|---|---|---|---|
| Steam cracker, end of waste, without purification | Listed sorted plastic waste, PE + PP + PS at least 85 %, PVC at most 3 %; halogens 500 ppm, sulphur 3,000 ppm, nitrogen 5,000 ppm, oxygen 10,000 ppm, metals 500 ppm [A3-ARRETE-SSD-HUILE-PYROLYSE-2024] | Chlorine 1,370 and 5,260 ppm; nitrogen 2,400 and 4,300 ppm [CHIBA-JLOS-HUILES] | Does not pass: chlorine |
| Steam cracker, end of waste, after purification | Same feed; halogens 30,000 ppm, sulphur 5,000 ppm, nitrogen 10,000 ppm, oxygen 40,000 ppm, metals 5,000 ppm for the compounds treated [A3-ARRETE-SSD-HUILE-PYROLYSE-2024]; buyer's specification | Chlorine, sulphur and nitrogen within these limits; oxygen and metals not measured [CHIBA-JLOS-HUILES] | Possible under conditions, for a sorted plastic feed only |
| Fuel sold as a hazardous waste | Plant authorised for this hazardous waste [A3-REG1357-2014-HP3] | Flash point below 40 °C [CHIBA-JLOS-HUILES] | Possible under conditions |
| Heavy fuel oil | Flash point at least 70 °C [A3-ARRETE-FIOULS-LOURDS-2000] | Below 40 °C [CHIBA-JLOS-HUILES] | Does not pass without refining |
| Road diesel | Flash point above 55 °C, sulphur 10 mg/kg, density 820 to 845 kg/m³, water 200 mg/kg [A3-ARRETE-GAZOLE-1999-ANNEXE-I] | Fails on flash point, density, water and sulphur [CHIBA-JLOS-HUILES] | Does not pass without refining |

In short, chlorine closes the steam cracker without purification, and the flash point closes the finished fuels. Finding technical solutions to reach the better markets (removing PVC upstream, dechlorination, stabilisation) is a matter for Urban Rig.

### 3.1.3 Regulatory Status

- **The oil is a waste** until it meets end-of-waste criteria. French law sets four conditions for a waste to cease being a waste [A3-CODE-ENV-L541-4-3]. The criteria are set by the minister for the environment [A3-CENV-D541-12-4-6-2026], under a procedure revised in 2026 [A3-DECRET-2026-435-SSD]. The Code also provides that a product made from waste is not a waste if it is similar to the product made without waste and meets the four conditions [A3-CODE-ENV-L541-4-3]; this route has not been examined for the oil.
- **End-of-waste for a steam cracker (order of 19 February 2024).** It applies to pyrolysis oil used in a steam cracker or a purification unit feeding one [A3-ARRETE-SSD-HUILE-PYROLYSE-2024]. The incoming waste must be listed plastic waste with at least 85 % of PE, PP and PS and at most 3 % of PVC [A3-ARRETE-SSD-HUILE-PYROLYSE-2024]. Mixed municipal waste is not on the list; separately collected or sorted plastic waste is [A3-ARRETE-SSD-HUILE-PYROLYSE-2024]. This route is therefore open only to a plastic-only feed (Annex 8), subject to confirmation with the regional authority.
- **Fuel is not recycling.** The order states that producing fuel is not recycling [A3-ARRETE-SSD-HUILE-PYROLYSE-2024], in line with the EU definition [WFD-2008-98-ART3-4]. In the EU rules on recycled content, the share turned into fuels counts for zero, and the char is excluded [A3-SUP-DECISION-CONTENU-RECYCLE-2026].
- **REACH.** A waste is outside REACH; once it ceases to be a waste, the substance must be registered unless it is identical to a substance already registered and the safety information on that substance is available to the recovery operator [A3-REACH-ART2-2006] [A3-ECHA-GUIDE-DECHETS-2010].
- **Certification.** Buyers of recycled feedstock use mass balance certification such as ISCC PLUS [A3-ISCC-PLUS-COC-2026].

### 3.1.4 Market Benchmarks

**Most recent prices (defaults of the model).**

| Fraction | Benchmark | Price | Date and scope | Source |
|---|---|---|---|---|
| Light | Naphtha, North-West Europe | 636.8 EUR/t | August 2026, monthly average | [A3F-INSEE-NAPHTA-NWE-010002082] |
| Gas oil | Gas oil, Rotterdam | 1,406 USD/t, i.e. 1,254 EUR/t | week to 9 October 2026 | [A3-DGEC-NPG-2026-10-09-COTATIONS] [calc:CALC-A3-GAZOLE-EUR-T] |
| Heavy | Fuel oil below 1 % sulphur, Rotterdam | 541 EUR/t | week to 9 October 2026 | [A3-DGEC-NPG-2026-10-09-COTATIONS] |

Other benchmarks of the same week: heating oil 1,224 EUR/t and jet fuel 1,404 EUR/t [calc:CALC-A3-FOD-EUR-T] [calc:CALC-A3-JET-EUR-T].

**Earlier years, for comparison (annual averages, EUR/t).**

| Benchmark | 2024 | 2025 | Source |
|---|---|---|---|
| Naphtha, North-West Europe | 604.7 | 505.0 | [A3F-INSEE-NAPHTA-NWE-010002082] |
| Naphtha, French imports (unit value) | 622.8 | 621.0 | [A3F-COMEXT-NAPHTA-2710-12-2024-2026] |
| Gas oil, CIF | 690.8 | 603.1 | [A3F-INSEE-GAZOLE-CAF-010002076] |
| Gas oil, French imports (unit value) | 714.8 | 633.9 | [A3F-COMEXT-GAZOLE-2710-19-4X-2024-2026] |
| Fuel oil 0.1 to 0.5 % sulphur, French imports (unit value) | 575.4 | 443.8 | [A3F-COMEXT-FIOUL-LOURD-VGO-2710-19-5X-6X-2024-2026] |
| Heavy fuel oil, price paid by industry in France | 576 | not published | [PRM-INSEE-EACEI-2024] |

The import unit values are calculated from Eurostat trade statistics (value divided by quantity) and mix qualities. They differ from the market quotations: for naphtha in 2025, 505.0 EUR/t (quotation) against 621.0 EUR/t (French imports) [A3F-INSEE-NAPHTA-NWE-010002082] [A3F-COMEXT-NAPHTA-2710-12-2024-2026].

**Pyrolysis oil itself.** No public quotation was found; the ICIS and Argus assessments are paid services (request R-037) [PRM-ARGUS-PYRO-2024]. Three points of reference:

- Pryme (Rotterdam) sold 822 t of plastic pyrolysis oil in 2025 at about 1,300 EUR/t, ex-works, with a price formula that refers, among other things, to a plastic waste price index [A3F-PRYME-RAPPORT-ANNUEL-2025]. The oil was sold whole, to a steam cracker buyer (Shell is the partner named in other sources) [A3-SHELL-PRYME-2021]; the plant was stopped at the end of March 2026 and the auditor refused to certify the accounts [A3F-PRYME-RAPPORT-ANNUEL-2025].
- A commercial index gives 683 USD/t for pyrolysis oil in Germany in September 2026, without origin or quality (not verified) [PRM-IMARC-PYRO-2026].
- An economic study calculated a net revenue of 210 EUR/t for a pyrolysis oil used as a heavy fuel oil substitute, in its own scenario; it is a calculation, not an observed sale (secondary source) [A3F-RIEDEWALD-2020-PRIX-HUILE].

### 3.1.5 Price per Fraction for the Model

The model takes, for each fraction, the most recent benchmark of Section 3.1.4, multiplied by a quality factor set by the operator [hyp:D-030].

| Fraction | Default benchmark | Quality factor |
|---|---|---|
| Light (10 %) | 636.8 EUR/t [A3F-INSEE-NAPHTA-NWE-010002082] | set by the operator; Sapporo sold its light oil at naphtha value [A3F-SAPPORO-SPR-2009-PRIX-FRACTIONS] |
| Gas oil (80 %) | 1,254 EUR/t [calc:CALC-A3-GAZOLE-EUR-T] | set by the operator; Sapporo sold its middle oil at 80 to 90 % of A fuel oil [A3F-SAPPORO-SPR-2009-PRIX-FRACTIONS] |
| Heavy (10 %) | 541 EUR/t [A3-DGEC-NPG-2026-10-09-COTATIONS] | set by the operator; Sapporo sold its heavy oil at 80 to 90 % of C fuel oil [A3F-SAPPORO-SPR-2009-PRIX-FRACTIONS] |
| Weighted benchmark of the oil | 1,121 EUR/t [calc:CALC-A3-HUILE-MOY-REF] | |

The quality factor reflects that the oil, as produced from municipal plastics, is off-specification (Section 3.1.2). No source gives the discount actually obtained for such an oil in France; the factor is a decision of the project sponsor, proposed in the list of parameters to be decided.

### 3.1.6 Sensitivity to the Oil Price

Each benchmark is divided by the Brent price of the same period [calc:CALC-A3-RATIO-LEGERE] [calc:CALC-A3-RATIO-GAZOLE] [calc:CALC-A3-RATIO-LOURDE]. The model multiplies this ratio by the Brent price entered by the operator [hyp:D-030]:

| Brent entered | Light | Gas oil | Heavy | Weighted oil |
|---|---|---|---|---|
| Latest prices | 636.8 EUR/t [A3F-INSEE-NAPHTA-NWE-010002082] | 1,254 EUR/t [calc:CALC-A3-GAZOLE-EUR-T] | 541 EUR/t [A3-DGEC-NPG-2026-10-09-COTATIONS] | 1,121 EUR/t [calc:CALC-A3-HUILE-MOY-REF] |
| 80 USD per barrel | 560 EUR/t [calc:CALC-A3-LEGERE-BRENT80] | 781 EUR/t [calc:CALC-A3-GAZOLE-BRENT80] | 337 EUR/t [calc:CALC-A3-LOURDE-BRENT80] | 714 EUR/t [calc:CALC-A3-HUILE-MOY-BRENT80] |
| 50 USD per barrel | 350 EUR/t [calc:CALC-A3-LEGERE-BRENT50] | 488 EUR/t [calc:CALC-A3-GAZOLE-BRENT50] | 210 EUR/t [calc:CALC-A3-LOURDE-BRENT50] | 446 EUR/t [calc:CALC-A3-HUILE-MOY-BRENT50] |

Limits of the method. The ratio is held constant: refining margins and the euro to dollar rate are assumed unchanged. In 2026 the refining margin was high: 235 EUR/t in September 2026, against an average of 150 EUR/t over 2026 to date [A3-DGEC-NPG-2026-10-09-COTATIONS]. At a lower oil price the gas oil benchmark may therefore fall faster than shown.

### 3.1.7 Buyers

Buyers of plastic pyrolysis oil named by a primary source:

| Buyer | Site | What the source states | Source |
|---|---|---|---|
| ExxonMobil, with Plastic Energy | Notre-Dame-de-Gravenchon (France) | Historical precedent, not a current buyer: plant for 25,000 t per year of plastic waste announced in 2021 [A3-PLASTICENERGY-NDG-2021]; the steam cracker was shut down permanently in 2024 [A3-SDES-PETROCHIMIE-2026]; effect on the agreement not known [A3-SENAT-EXXON-NDG-2024] | [A3-PLASTICENERGY-NDG-2021] [A3-SDES-PETROCHIMIE-2026] |
| INEOS | Lavéra (France) | Steam cracker fed with pyrolysis oil from packaging waste, ISCC PLUS | [A3-INEOS-LAVERA-2025] |
| TotalEnergies, with Plastic Energy | Seville (Spain); Grandpuits (France) | 33,000 t per year in Seville; 15,000 t per year in Grandpuits | [A3-TOTAL-PLASTICENERGY-SEVILLE-2022] |
| BASF | Germany | Up to 100,000 t per year of oil (Arcus) | [A3-BASF-ARCUS-2022] |
| Shell, with Pryme | Moerdijk (Netherlands) | Oil from 60,000 t per year of plastic waste | [A3-SHELL-PRYME-2021] [A3-PRYME-SHELL-AVENANT-2024] |

All these buyers take oil made from sorted plastic waste for petrochemical use. None was found buying oil made from mixed household waste. For the fuel outlet, buyers are plants authorised to receive this oil as a hazardous waste; none is named by a source read. Letters of intent stating the accepted quality, the status of the product, the volumes and the price formula are the next step.

## 3.2 Char

### 3.2.1 Product Characteristics

The char has a gross calorific value of 32,090 J/g [IZUMITEC-R35-339439], close to petroleum coke (32 GJ/t, net) and above steam coal (26 GJ/t, net) [A3-SDES-CCE-2026-EQUIVALENCES]. Its heavy metals were measured on two municipal runs: cadmium 31 and 36 mg/kg, lead 140 and 42 mg/kg, mercury 0.06 and below 0.02 mg/kg [CHIBA-OOSUMI-CHAR]. Its chlorine, sulphur and ash have not been measured (requests R-012 and R-034).

OneWorld design data describe the char as a high-calorie powder coal mixed with heavy oil [OW-ENG-P16-DEBOUCHES] and as a coal substitute [UR2000-JP-P05-BILAN].

### 3.2.2 Outlets

**Cement kilns (main outlet).** France has 25 cement plants [A3G-FDR-DECARBONATION-CIMENT-2023]. Alternative fuels covered 44 % of their energy in 2021, with targets of 80 % in 2030 and 85 % in 2050 [A3G-FDR-DECARBONATION-CIMENT-2023]. Waste fuels used rose from 964 kt in 2015 to 1,054 kt in 2021, with 1,528 kt targeted for 2030 [A3G-FDR-DECARBONATION-CIMENT-2023]. Petroleum coke, which the char would replace, is the main fossil fuel of the sector [A3G-FDR-DECARBONATION-CIMENT-2023]. One plant, Airvault, plans up to 150,000 t per year of solid recovered fuel [A3G-HEIDELBERG-AIRVAULT-2025-2022].

**Acceptance criteria in cement plant permits.**

| Criterion | Value | Source |
|---|---|---|
| Organic chlorine | 1 % at the precalciner, 2 % at the main burner | [A3G-AP-AIRVAULT-4401-2005] |
| Chlorine for cement-grade recovered fuel | below 0.5 %, with a net calorific value above 18 MJ/kg | [A3-OBS-NORMANDIE-CSR-2021] |
| Sulphur | 4 % at most | [A3G-AP-AIRVAULT-4401-2005] |
| Mercury | 10 mg/kg | [A3G-GEORISQUES-HOLCIM-ROCHEFORT-2010] |
| Cadmium + mercury + thallium | 100 mg/kg | [A3G-GEORISQUES-HOLCIM-ROCHEFORT-2010] |
| Lead, chromium, nickel and other metals (sum) | 2,500 mg/kg | [A3G-GEORISQUES-HOLCIM-ROCHEFORT-2010] |

These are historical examples: the Airvault permit of 2005 and the Rochefort permit of 17 April 2007, reproduced in an inspection report of 2010 [A3G-AP-AIRVAULT-4401-2005] [A3G-GEORISQUES-HOLCIM-ROCHEFORT-2010]; recent permits with figures were not found online (request R-038). The measured cadmium, lead and mercury of the char are far below these limits taken one by one; the sums of metals cannot be checked because the other metals were not measured; chlorine is not known (R-034).

**Other outlets.** Boilers burning solid recovered fuel need a net calorific value of at least 12,000 kJ/kg [ARRETE-CSR-2016], but the rules apply to fuels prepared in a dedicated installation [A3-AIDA-AM-23052016-COMBUSTION-CSR], which the char is not. Blast furnace injection requires chlorine below 0.05 % (2010 source) [A3-IEACCC-PCI-PLASTIQUES-2010].

**Not an outlet.** Fertiliser and biochar uses are excluded: EU fertilising products exclude inputs from mixed municipal waste [FPR-2019-1009], and the biochar standards exclude mixed municipal waste [A3-PURO-BIOCHAR-2025] [PRM-EBC-POSLIST-V10].

### 3.2.3 Regulatory Status

The char is a waste from pyrolysis, code 19 01 17* if it contains hazardous substances or 19 01 18 otherwise [A3-FR-R541-8-LISTE-DECHETS]. A waste with an asterisk is hazardous [A3-DEC2000-532-CONSOLIDEE-2023]. On the carcinogenicity criterion (0.1 % threshold), the cadmium measured, 36 mg/kg, is 0.0036 % [A3-REG1357-2014-HP7] [CHIBA-OOSUMI-CHAR]; the other criteria have not been assessed (request R-034). No French end-of-waste criteria exist for a char or a solid recovered fuel [A3-MTE-CATEGORIES-DECHETS-SSD-2024].

### 3.2.4 Prices

**Energy parity (upper bound).**

| Benchmark | Price | Value of the char at the same price per GJ |
|---|---|---|
| Petroleum coke imported into France, first half of 2026 | 3.84 EUR/GJ [A3G-COMEXT-PETCOKE-NC27131100-FR] | 123 EUR/t [calc:CALC-A3-CHAR-PARITE-PETCOKE] |
| Steam coal imported into France, first half of 2026 | 6.32 EUR/GJ [A3G-COMEXT-CHARBON-NC27011290-FR] | 203 EUR/t [calc:CALC-A3-CHAR-PARITE-CHARBON] |
| Petroleum coke, price paid by French industry in 2024 | 7.94 EUR/GJ [calc:CALC-A3-PETCOKE-INSEE-GJ] | 255 EUR/t [calc:CALC-A3-CHAR-PARITE-INSEE] |

These values use the gross calorific value of the char against the net value of the fuels [IZUMITEC-R35-339439] [A3-SDES-CCE-2026-EQUIVALENCES]; they are an upper bound. The import price (border value) and the price paid by industry differ by a factor of about two [A3G-COMEXT-PETCOKE-NC27131100-FR] [PRM-INSEE-EACEI-2024].

**Market practice for waste fuels.** On the French market for solid recovered fuels, the producer usually pays the user. Three sources disagree on the amount:

- cement plants "buy" high-quality recovered fuel for 0 to 50 EUR/t, while boilers are paid 10 to 30 EUR/t to take it [A3-OBS-NORMANDIE-CSR-2021];
- the producer pays a gate fee of 40 to 50 EUR/t [FNADE-CSR-2023];
- in Germany, a producer pays 50 EUR/t to the cement plant in the example given [A3G-ALBA-EBS-HINTERGRUND-2023].

A recovered fuel has a net calorific value of 12 to 18 MJ/kg, or above 18 MJ/kg for cement grade [A3-OBS-NORMANDIE-CSR-2021]; the char carries about twice as much energy per tonne [IZUMITEC-R35-339439]. No published price for a pyrolysis char sold as fuel was found. In Japan, a carbonised household waste fuel of at least 16 MJ/kg is sold "at a low price" (price not readable) [A3G-KHI-GOMI-TANKA-NENRYO].

**For the model.** The char is sold [hyp:D-028]. The default price is set by the project sponsor within the range above: from a gate fee paid by the plant to the energy parity with petroleum coke (Section 3.7).

### 3.2.5 If the Char Cannot Be Sold

Treatment of waste similar to household waste cost 159 EUR/t excluding taxes in Marseille in 2025 [A3-AMP-TARIFS-TRAITEMENT-2025]. The landfill tax is 69 EUR/t in 2026 [CIBS-TGAP-2026]. The cost of a hazardous waste landfill, if the char were classified 19 01 17* [A3-FR-R541-8-LISTE-DECHETS], was not found (request R-038).

## 3.3 Recovered Metals, Glass and Inerts

### 3.3.1 Recovery and Quality

According to OneWorld design data, metals are extracted in a non-oxidised state, because the reactor contains no oxygen [OW-ENG-P14-P15-PROCEDE], and metals and glass are sold as recycled resources [OW-ENG-P16-DEBOUCHES]. Their cleanliness has not been analysed (request R-031).

To cease being a waste, steel scrap must contain at most 2 % of foreign materials, without excess iron oxide or visible oil; aluminium scrap at most 5 %, or a metal yield of at least 90 % [A3-UE-REG-333-2011]. The French packaging standard for steel requires at least 88 % of magnetic metal [A3-CITEO-GUIDE-ODQ-2024-STANDARDS].

### 3.3.2 Prices

**Public scrap prices (defaults of the model).** Unit values of French exports, calculated from Eurostat trade statistics [A3H-COMEXT-MENSUEL-2025-2026]:

| Metal | First half of 2026 (default) | 2025 | 2024 | Source |
|---|---|---|---|---|
| Shredded steel scrap (7204 49 10) | 316.4 EUR/t | 311.1 EUR/t | 352.1 EUR/t | [A3H-COMEXT-MENSUEL-2025-2026] [A3H-COMEXT-FR-ACIER-ANNUEL-2024-2025] |
| Aluminium scrap (7602 00 90) | 1,723 EUR/t | 1,456 EUR/t | 1,380 EUR/t | [A3H-COMEXT-MENSUEL-2025-2026] [A3H-COMEXT-FR-ALU-ANNUEL-2024-2025] |

These are prices of prepared scrap at the border. A French recycler sold its ferrous scrap at 305.4 EUR/t on average in the half-year to March 2026 [A3H-DERICHEBOURG-S1-2025-2026]. Secondary aluminium fragments were assessed at 1,900 to 2,000 EUR/t delivered in January 2026 [A3H-FASTMARKETS-ALU-FRAG-2026-01].

**Packaging metals taken back from French municipalities (Citeo).** These prices apply to metals recovered from household waste:

| Metal | Separate collection, 2024 | From incineration bottom ash, 2024 | From residual household waste, 2023 | Source |
|---|---|---|---|---|
| Steel | 196.7 EUR/t | 93.7 EUR/t | 172.5 EUR/t | [A3-CITEO-OBSREPRISE-2024-ACIER-CS] [A3-CITEO-OBSREPRISE-2024-ACIER-MACHEFERS] [A3-CITEO-OBSREPRISE-2023-METAUX] |
| Aluminium (rigid) | 639.5 to 831.9 EUR/t | 893.6 EUR/t (small sample) | not interpretable | [A3-CITEO-OBSREPRISE-2024-ALU-CS] [A3-CITEO-OBSREPRISE-2024-ALU-MACHEFERS] |

### 3.3.3 Value of Non-Oxidised Metals

For steel, the value of metal not passed through a furnace is visible in the Citeo data. Steel extracted from residual household waste was worth 1.83 times the steel from bottom ash in 2023 [calc:CALC-A3-ACIER-OMR-MACHEFERS], and bottom ash steel was worth 47.6 % of separately collected steel in 2024 [calc:CALC-A3-ACIER-MACHEFERS-CS-2024]. For aluminium, the data do not show such a premium: bottom ash aluminium was taken back at a higher price than rigid collected aluminium, on an 8 % sample [A3-CITEO-OBSREPRISE-2024-ALU-MACHEFERS].

### 3.3.4 Glass and Inerts

Glass and inerts (sand, stones, ceramics) are given no sale price [hyp:D-028]. According to OneWorld design data, debris, sand and stones are used as fill on site [OW-ENG-P16-DEBOUCHES]. The cost of an inert waste landfill in France was not found from a recent source; older data give 6 to 8 EUR/t (2013 to 2014) [A3-NA-DECHETS-INERTES-BTP-ETAT-DES-LIEUX]. To be costed with the feedstock in Annexes 5 to 8.

## 3.4 Surplus Gas and Hydrogen

### 3.4.1 When There Is a Surplus

On a resin-rich feed, the pyrolysis gas carries 4,299 MJ per tonne of feed [calc:CALC-A2-NRJ-GAZ-RESINE], 2.9 times the heat demand of the burner [calc:CALC-A2-COUV-BRULEUR-RESINE]. The surplus is 2,793 MJ per tonne [calc:CALC-A3-GAZ-SURPLUS-RESINE].

On household and municipal waste, self-sufficiency is not established and no surplus is counted [hyp:D-029]. The surplus gas and the hydrogen option therefore apply only to a plastic-only feed [hyp:D-031].

### 3.4.2 Hydrogen in the Gas

Hydrogen is the main component of the pyrolysis gas: 12.7 % by volume of the sample analysed, which is diluted with air [KANSO-B2002600], and about two thirds of the gas once the air is removed (Annex 2, Section 2.5.1). Because hydrogen is light, it is 11.6 % of the gas by mass [calc:CALC-A3-H2-PART-MASSE] but 37.2 % of its energy [calc:CALC-A3-H2-PART-ENERGIE].

| Per tonne of resin-rich feed | Value |
|---|---|
| Hydrogen in the gas, before purification | 13.3 kg [calc:CALC-A3-H2-KG-T-RESINE] |
| Gas energy left if all the hydrogen is removed | 2,702 MJ [calc:CALC-A3-GAZ-SANS-H2-RESINE] |
| Burner demand covered by the remaining gas | 1.8 times [calc:CALC-A3-COUV-SANS-H2-RESINE] |

The plant therefore stays self-sufficient in heat if it extracts its hydrogen, on this feed [calc:CALC-A3-COUV-SANS-H2-RESINE].

**Purification.** Pressure swing adsorption is the usual technique. A review reports 99.9913 % purity with 75.5 % recovery on a gas with 69 % hydrogen, and 80 to 95 % recovery in general (secondary source) [A3J-MDPI-ENERGIES-2025-PSA]. A manufacturer states purities up to 99.9999 % [A3J-LINDE-PSA-H2]. The pyrolysis gas also contains C2 and C3 hydrocarbons and carbon monoxide [KANSO-B2002600], which the purification must remove. The cost of a unit was not found; it belongs to Annex 9.

### 3.4.3 Status and Price of the Hydrogen

- **Status.** Hydrogen made from fossil waste that is not suitable for material recovery is a recycled carbon fuel, not a renewable fuel [A3J-UE-DIR-2018-2001-ART2-RCF]. The EU method for low-carbon hydrogen excludes recycled carbon fuels [A3J-UE-REG-DEL-2025-2359]. French public support is reserved for hydrogen from water electrolysis [A3J-CRE-2025-229-AVIS-CDC-H2]. No source establishes that this hydrogen can be sold as "green" or "low-carbon"; it is priced as conventional hydrogen.
- **Price.** Conventional hydrogen from natural gas cost a little over 2 EUR/kg in 2025; the HYDRIX market index of "green" hydrogen averaged about 8.2 EUR/kg in 2025 [A3J-ACER-H2-MARKETS-2025]. The modelled production cost of conventional hydrogen in France was 2.86 EUR/kg in 2024 [A3J-CHO-LCOH-2024-FRANCE].
- **Value per tonne of feed, before purification losses:** 27 EUR at 2 EUR/kg [calc:CALC-A3-H2-VAL-GRIS] and 109 EUR at 8.2 EUR/kg [calc:CALC-A3-H2-VAL-HYDRIX]. The conventional price is the default [hyp:D-031].

### 3.4.4 Selling the Surplus as Fuel Gas

The simplest alternative is to sell the surplus gas to a neighbouring industrial user. At the price of natural gas for large industrial users in France, 0.0470 EUR/kWh excluding VAT in the first half of 2026 [A3J-EUROSTAT-NRG-PC-203-FR], the surplus is worth 36.5 EUR per tonne of resin-rich feed [calc:CALC-A3-GAZ-SURPLUS-VAL]. Injection into the gas grid is excluded: the grid accepts less than 2 % hydrogen [A3J-NATRAN-SPEC-METHANE-SYNTHESE]. Heat bought by French industry cost 48.5 EUR/MWh excluding VAT in 2024 [A3J-SDES-BILAN-2024-PRIX-CHALEUR].

## 3.5 Carbon

### 3.5.1 Mechanisms Reviewed

No carbon revenue is counted [hyp:D-028]. The texts were checked one by one:

| Mechanism | What the text says | Credit for the Urban Rig? |
|---|---|---|
| EU emissions trading | A system of allowances to surrender; municipal waste incineration is excluded from its scope [A3I-UE-DIR-2003-87-ANNEXE-I] | No: it creates obligations, not credits |
| EU emissions trading, international credits | Use reserved to aircraft operators since the end of 2012 for fixed installations [A3I-UE-DIR-2003-87-ART11A] | No |
| EU emissions trading, projects outside the system | The Commission "may adopt measures"; no implementing act found [A3I-UE-DIR-2003-87-ART24A] | No, in practice |
| EU emissions trading, incineration | Proposal of July 2026: incineration included from 2031 above 3 t per hour, excluding chemical recycling [A3-UE-COM-2026-616-ANNEXES-FR] | No credit; possible effect on incineration gate fees after 2031 (Annexes 5 to 8) |
| EU carbon removals certification (CRCF) | Covers carbon removals and soil emission reductions only [A3I-UE-REG-2024-3012-ART1-CONSID10]; only biogenic or atmospheric carbon [A3-UE-REG-2024-3012-CRCF] | No |
| French low-carbon label | Approved method required, additionality, emissions under the EU system excluded [A3I-FR-ARRETE-LBC-2025-ART2-3]; no approved or draft method covers waste [A3I-FR-LBC-METHODES-SITE-2025] [A3I-FR-LBC-PROJETS-METHODES-2025-10] | No, until a method exists |
| Paris Agreement, Article 6 | Transfers must be authorised by the countries [A3I-ACCORD-PARIS-ART6]; the EU 2030 target is a domestic reduction [A3I-UE-REG-2021-1119-ART4] | No, without State authorisation |
| Verra (VCS) | EU countries not excluded; a method is required, and the two closest were rejected in March 2026; no double counting with an allowance system [A3I-VERRA-VCS-STANDARD-V5]; plastic credits are in tonnes of plastic, and use as fuel is not eligible [A3-VERRA-PLASTIC-STD-2021] [A3-VERRA-PWRM-2022] | Not today |
| Gold Standard | Waste methodology limited to metals, alloys and minerals [A3-GS-448-2025]; eligibility rules [A3I-GS-501-V3-2-2025] | No for the oil and the char; a route to study for the recovered metals, under conditions |
| Biochar credits (Puro) | Mixed municipal solid waste not allowed [A3-PURO-BIOCHAR-2025] | No |
| Guarantees of origin | Renewable energy only; the fossil share of waste is excluded [A3I-UE-DIR-2018-2001-ART2-GO] | No, for the fossil share |

**A risk rather than a revenue.** Combustion installations above 20 MW of thermal input fall within the EU emissions trading system, unless they incinerate hazardous or municipal waste [A3I-UE-DIR-2003-87-ANNEXE-I]; since 1 January 2024, municipal waste incinerators must nevertheless monitor and report their emissions [A3-ZWE-SEQE-ART30-2024]. The thermal input of a URC-2000 and its classification are to be confirmed (Annex 4).

**Claims.** Since 27 September 2026, a product claim based on the offsetting of emissions is prohibited in the EU [A3I-UE-DIR-2024-825-ANNEXE-4C]. The CO2 avoided below is an information for investors, not a claim for products.

### 3.5.2 CO2 Avoided Compared with Incineration

Method [hyp:D-032]: the fossil carbon of the feed ends up as CO2 in both routes. Burning one tonne of plastic emits about 2,750 kgCO2 [calc:CALC-A3-CO2-PLASTIQUE-GIEC]. The difference between the routes is what each one replaces.

| Per tonne of resin-rich feed | kgCO2e |
|---|---|
| Urban Rig: heavy fuel oil replaced by the oil (35,190 MJ at 77.4 kgCO2/GJ) | 2,724 avoided [calc:CALC-A3-CO2-SUBST-HUILE] |
| Incineration of PE: energy recovered | 747 avoided [A3-ADEME-BC-EMBALLAGES-PLASTIQUES-INCINERATION] |
| Urban Rig: electricity bought | 3.7 emitted [calc:CALC-A3-CO2-ELEC-UR] |
| **CO2 avoided compared with incineration** | **1,973** [calc:CALC-A3-CO2-NET-VS-INCIN] |

Not counted: transport, flue gas treatment, the char and surplus gas sold, and process losses [hyp:D-032]. For household waste, no calculation is made: the composition of the products is not measured [hyp:D-029]. This figure gives no credit (Section 3.5.1).

## 3.6 Purchased Energy in France

### 3.6.1 Electricity

The URC-2000 draws 600 kW [OW-CONSO-ENERGIE], or 5,256 MWh per year in continuous operation [calc:CALC-A3-ELEC-MWH-AN]. The plant therefore falls in Eurostat consumption band ID, 2,000 to 19,999 MWh per year [A3-EUROSTAT-NRG-CONS-CODELIST]. The electricity figure itself is an open point: the brochure gives 20 kW (request R-015) [UR2000-JP-P08-SPEC].

| Band ID, France, excluding VAT | EUR/kWh |
|---|---|
| 2025, first half | 0.1296 [PRM-EUROSTAT-NRGPC205-ID-2025] |
| 2025, second half (default) | 0.1212 [PRM-EUROSTAT-NRGPC205-ID-2025] |

At 72 kWh per tonne treated [calc:CALC-A3-ELEC-KWH-T], the default gives 8.73 EUR per tonne [calc:CALC-A3-ELEC-EUR-T].

Components for 2026, to update the default: the excise duty on electricity was 26.58 EUR/MWh from 1 February 2026 [A3-BOFIP-RES-EAT-000240-2025-12-31], and 26.35 EUR/MWh from 1 August 2026 according to a supplier [A3-EDF-TAXES-ELEC-2026]; the wholesale spot price averaged 61 EUR/MWh in 2025 [A3-CRE-SURVEILLANCE-2025-CP]; network tariffs (TURPE) rose by 3.04 % on 1 August 2026 [A3-CRE-TURPE7-HTA-2026-105].

### 3.6.2 Fuel

The gas covers the process heat on plastic-rich feeds (Section 3.4.1). Fuel is bought for start-up and, on household and municipal waste, for the heat that the gas does not cover [hyp:D-029]. OneWorld's consumption table states 10,000 L of fuel per day [OW-CONSO-ENERGIE].

| Fuel, France, excluding all taxes | Latest week (to 9 October 2026, default) | 2025 average | Source |
|---|---|---|---|
| Non-road diesel (GNR), deliveries below 5 m³ | 1.3405 EUR/L | 0.6855 EUR/L | [A3-DGEC-NPG-2026-10-09-PRIX-FRANCE] [A3-DGEC-PRIX-HTT-TTC-2025] |
| Heating oil, deliveries above 27 m³ | 1.3267 EUR/L | 0.7221 EUR/L | [A3-DGEC-NPG-2026-10-09-PRIX-FRANCE] [A3-DGEC-PRIX-HTT-TTC-2025] |

Including taxes, the same week: 2.0500 EUR/L for non-road diesel and 1.7920 EUR/L for heating oil [A3-DGEC-NPG-2026-10-09-PRIX-FRANCE]. The reduced tax rate on non-road diesel is being aligned with road diesel by 2030 [A3-SENAT-QE-07357-2026]; the 2026 rate was not found. Net calorific value: 42.6 GJ/t for gas oil and heating oil [A3-SDES-CCE-2026-EQUIVALENCES].

## 3.7 Price Table for the Financial Model

Each line is a default that the operator can change [hyp:D-030]. Values marked "to decide" are proposed to the project sponsor in the list of parameters to be decided.

| Item | Default | Basis | Source |
|---|---|---|---|
| Light oil, benchmark | 636.8 EUR/t | Naphtha NWE, August 2026 | [A3F-INSEE-NAPHTA-NWE-010002082] |
| Gas oil, benchmark | 1,254 EUR/t | Rotterdam, week to 9 October 2026 | [calc:CALC-A3-GAZOLE-EUR-T] |
| Heavy oil, benchmark | 541 EUR/t | Fuel oil below 1 % sulphur, Rotterdam, same week | [A3-DGEC-NPG-2026-10-09-COTATIONS] |
| Quality factor per fraction | to decide | Precedent of 80 to 90 % | [A3F-SAPPORO-SPR-2009-PRIX-FRACTIONS] |
| Brent of reference | 128.53 USD per barrel | Week to 9 October 2026 | [A3-DGEC-NPG-2026-10-09-COTATIONS] |
| Char | to decide | From a gate fee of 50 EUR/t paid by the plant to 123 EUR/t at petroleum coke parity | [A3G-ALBA-EBS-HINTERGRUND-2023] [calc:CALC-A3-CHAR-PARITE-PETCOKE] |
| Steel scrap | 316.4 EUR/t | French exports, first half of 2026 | [A3H-COMEXT-MENSUEL-2025-2026] |
| Aluminium scrap | 1,723 EUR/t | French exports, first half of 2026 | [A3H-COMEXT-MENSUEL-2025-2026] |
| Glass and inerts | no price | Decision | [hyp:D-028] |
| Carbon | no revenue | Decision | [hyp:D-028] |
| Hydrogen (plastic-only feed) | 2 EUR/kg | Conventional hydrogen, 2025 | [A3J-ACER-H2-MARKETS-2025] |
| Surplus gas as fuel (plastic-only feed) | 0.0470 EUR/kWh | Natural gas, band I4, first half of 2026 | [A3J-EUROSTAT-NRG-PC-203-FR] |
| Electricity | 0.1212 EUR/kWh | Band ID, second half of 2025, excluding VAT | [PRM-EUROSTAT-NRGPC205-ID-2025] |
| Fuel (non-road diesel) | 1.3405 EUR/L | Excluding taxes, week to 9 October 2026 | [A3-DGEC-NPG-2026-10-09-PRIX-FRANCE] |

## 3.8 Data Quality Summary

| Item | Basis | Main uncertainty |
|---|---|---|
| Oil fractions | OneWorld design data | Output of each zone not measured (R-013) |
| Oil benchmarks | Official statistics and quotations | Crisis prices in 2026; constant ratio to Brent |
| Price of the oil itself | No public quotation | Quality discount to decide; ICIS and Argus paid (R-037) |
| Steam cracker outlet | Regulation read | Plastic-only feed; oxygen and metals not measured (R-035) |
| Fuel outlet | Regulation read | Hazardous waste (flash point); acceptance by an authorised plant to obtain |
| Char value | Energy parity and market practice | Chlorine not measured; sense of payment disputed (R-012, R-034, R-038) |
| Metal prices | Trade statistics and Citeo | Cleanliness of the metals not analysed (R-031) |
| Hydrogen | Calculated from one gas analysis | Gas quantity and purification cost (R-011, Annex 9) |
| Carbon | Legislation read | Thermal input of the plant and classification under the EU system |
| Electricity | Eurostat | 600 kW [OW-CONSO-ENERGIE] or 20 kW [UR2000-JP-P08-SPEC] (R-015) |

## 3.9 Open Points

| Ref. | Subject |
|---|---|
| R-033 | Prices obtained in Japan for the oil, char and metals of the plants in operation; buyers and their specifications |
| R-034 | Char: form, chlorine, sulphur, ash, leaching, hazardous waste classification |
| R-035 | Oil from a PE, PP and PS feed analysed against table A of the end-of-waste order; ISCC PLUS certification |
| R-036 | Basis of the carbon credit statements; CO2 emissions of a URC-2000 |
| R-037 | Paid quotations: pyrolysis oil, naphtha, scrap, recovered fuels |
| R-038 | Acceptance conditions and price of the char in French cement plants and boilers |

The open points of Annexes 1 and 2 also apply, in particular R-012 (char), R-013 (oil chlorine and fractions), R-015 (energy consumption) and R-031 (metals).

## 3.10 References

The full list of documents cited, with their location and confidence, is in the index of evidence sheets.
