#!/usr/bin/env python3
"""Genere la version HTML de l annexe 2 (index.html + preuves/*.html) a partir du Markdown et des registres.
Usage : python3 nouveau-business-plan/annexes/annexe-02-html/generer_html.py"""
import os, re, yaml
# ---------------- confidence and nature per source ID
SRC={
# id: (file code, confidence, nature, label, english summary)
'CHIBA-RAPPORT-2023':('A2.1.a',100,'Test report filed with the Chiba prefectural government (operator: Asada Shokai; machine built and operated by OneWorld; measurements: Land Brain)','LU',
 'Final report of the 2022 test programme on an URBAN RIG batch unit at the Noda plant of Asada Shokai, submitted to the Governor of Chiba on 2023-01-30. Defines the organisations involved and the machine tested.'),
'CHIBA-ESSAIS-FICHES':('A2.1.a',100,'Test report filed with the Chiba prefectural government','LU',
 'One test sheet per run: input weight, oil weight and volume, oil density, residue removed (metals and foreign matter, char), gas by difference, oil yield and gas yield as reported, wastewater. The operator defines the gas as input minus removed residue minus oil (PDF p. 27).'),
'CHIBA-BILANS':('A2.1.b',100,'Test report filed with the Chiba prefectural government','LU',
 'Mass and energy balances of four runs (two PE/PP/PS mixed runs, two municipal waste runs): input, oil, char, metals, gas, electricity, gas oil, water, and energy ratios computed with fixed factors.'),
'CHIBA-SYNTHESE':('A2.1.b',100,'Test report filed with the Chiba prefectural government','LU',
 'Summary chapters: points verified by the test, total oil (407 L), total char (66.3 kg), total wastewater (931 L), and the operator\'s statement on the 40 % oil criterion.'),
'CHIBA-DISTILLATION':('A2.1.c',100,'Test report filed with the Chiba prefectural government (table signed by Asada Shokai)','LU',
 'Distillation of 200 mL of oil from each virgin plastic into a light fraction (Japanese "class 1 petroleum") and a heavier fraction, with flash points, specific gravity and sulphur.'),
'CHIBA-AUTORISATION-2022':('A2.1.d',100,'Official notification of the Chiba prefectural government','LU',
 'Prefectural notification authorising the test programme from 2022-03-02 to 2022-09-30 with at most 12,000 kg of waste.'),
'CHIBA-JLOS-HUILES':('A2.2.a',100,'Independent laboratory (Japan Lubricating Oil Society)','LU',
 'Laboratory analyses of the two oils produced from Noda municipal waste: density, flash point, viscosity, pour point, carbon residue, water, ash, sulphur, nitrogen, chlorine and gross calorific value (calculated by the laboratory).'),
'CHIBA-OOSUMI-CHAR':('A2.2.b',100,'Independent laboratory (Oosumi Co., registered measurement business, Kanagawa)','LU',
 'Heavy metal contents (as received) and leaching tests of the chars from the two municipal waste runs.'),
'CHIBA-OOSUMI-EAUX':('A2.2.c',100,'Independent laboratory (Oosumi Co.)','LU',
 'Analyses of the untreated process water from the two municipal waste runs.'),
'CHIBA-OOSUMI-FUMEES':('A2.2.d',100,'Independent laboratory (Oosumi Co.); reports marked provisional','LU',
 'Exhaust gas measurements at furnace temperatures of 350, 450 and 550 °C during the two municipal waste runs: dust, sulphur oxides, nitrogen oxides, and dioxins on 2022-09-15; metals in dust.'),
'CHIBA-OOSUMI-ODEURS-BRUIT':('A2.2.e',100,'Independent laboratories (Oosumi Co.; Kazusa Environmental Research Center)','LU',
 'Odour index at the site boundary and near the exhaust outlet, odorous substances, noise and vibration during the 2022 tests.'),
'KANSO-B2002600':('A2.2.f',100,'Independent laboratory (KANSO Technos, registered measurement business, Osaka); client OneWorld','LU',
 'Gas chromatography of the off-gas of a superheated steam carbonisation unit, sampled on 2020-11-25.'),
'KANSO-20002610':('A2.2.g',100,'Independent laboratory (KANSO Technos); client OneWorld','LU',
 'Exhaust gas measurements at the outlet of the same unit on 2020-11-25: hydrogen chloride, sulphur oxides, nitrogen oxides, dust, oxygen.'),
'TES-ODEUR-2020':('A2.2.g',100,'Independent laboratory (Total Kankyo System, subcontractor of KANSO)','LU',
 'Odour index at the outlet and at the site boundary on 2020-11-25.'),
'TANABE-2023':('A2.2.h',100,'Independent laboratories (Tanabe Kankyo Kogaku; N.E. Support)','LU',
 'Exhaust gas measurements (nitrogen oxides, sulphur oxides, hydrogen cyanide, dust, gas flow) and odour on 2023-09-26 and 2023-09-27 at a waste plastic oil demonstration facility.'),
'DIOXINES-2023':('A2.2.h',100,'Independent laboratory (Kankyo Kogai Bunseki Center); preliminary results','LU',
 'Dioxins in the exhaust gas on 2023-09-26 and 2023-09-27.'),
'NKKK-ZPE8004-2019':('A2.2.i',95,'Independent laboratory (NKKK, Osaka), report reproduced in a OneWorld brochure','LU',
 'Analysis of a fuel oil sample supplied by OneWorld: flash point, viscosity, pour point, carbon residue, water, ash, sulphur, gross calorific value, inorganic chlorine.'),
'IZUMITEC-R35-339439':('A2.2.j',100,'Independent laboratory (Izumitec Co., registered measurement business, Aichi); client One World Japan','LU',
 'Calorific value of a urethane char (JIS M 8814 bomb calorimeter method).'),
'IZUMITEC-R35-339440':('A2.2.j',100,'Independent laboratory (Izumitec Co.); client One World Japan','LU',
 'Calorific value of a urethane-derived oil (JIS K 2279).'),
'ORIST-GCMS-DRAIN':('A2.2.k',100,'Public research institute (Osaka Research Institute of Industrial Science and Technology), preliminary letter','LU',
 'GC-MS analysis of a liquid "drain" sample heated to 350 °C, and its non-volatile residue.'),
'UR2000-JP-P05-BILAN':('A2.3.a',95,'Manufacturer documentation (OneWorld brochure URC-2000, Japanese)','CONSTRUCTEUR',
 'Stated output for 200 t of household waste with 10 % resins, and the products expected from resins and from organic matter.'),
'UR2000-JP-P08-SPEC':('A2.3.a',95,'Manufacturer documentation (OneWorld brochure URC-2000, Japanese)','CONSTRUCTEUR',
 'Specification of the URC-2000: 200 t/day, temperatures, burner rating, buckets, electricity consumption, steam generation.'),
'OW-ENG-P16-BILAN':('A2.3.b',95,'Manufacturer documentation (OneWorld brochure, English, October 2019)','CONSTRUCTEUR',
 'Stated daily output of the URC-2000 for a feed with 90 % resin content: oil fractions, recovery loss, char, water, metals.'),
'OW-ENG-P02-P14-AFFIRMATIONS':('A2.3.b',95,'Manufacturer documentation (OneWorld brochure, English, October 2019)','CONSTRUCTEUR',
 'OneWorld statements on operation without external fuel, exhaust treatment, water reuse, PVC, chlorine removal, dioxins, bucket size and daily throughput.'),
'OW-CONSO-ENERGIE':('A2.3.c',90,'Table from the manufacturer files; author and date not printed','CONSTRUCTEUR',
 'Fuel and electricity consumption by machine size, in two operating modes.'),
'OWJ-DEMO-2021':('A2.3.d',95,'Manufacturer test report (One World Japan)','CONSTRUCTEUR',
 'Three demonstration runs of about 100 kg of mixed plastics on the truck-mounted URT-10, 1 to 3 December 2021.'),
'OWT-DEMO-2020':('A2.3.d',95,'Manufacturer test report (One World Techno)','CONSTRUCTEUR',
 'Demonstration run on 450 kg of waste tyres in a 4.8 t batch machine on 2020-12-12.'),
'IED-2010-75-ANX6-P3':('A2.4.a',100,'EU legislation','LU','Directive 2010/75/EU on industrial emissions, Annex VI Part 3: emission limit values to air for waste incineration plants, reference conditions (11 % oxygen), and Article 42 on pyrolysis plants.'),
'BAT-WI-2019-2010':('A2.4.a',100,'EU legislation','LU','Commission Implementing Decision (EU) 2019/2010: best-available-technique emission levels (BAT-AELs) for waste incineration.'),
'WALLONIE-2003-ANX6-O2':('A2.4.a',100,'Regional legislation (Wallonia, transposition of EU incineration rules)','LU','Formula to correct a measured concentration to the standard oxygen content.'),
'DK-EPA-2002-PPM':('A2.4.a',100,'Government guidance (Danish EPA, 2002; physical conversion factors)','LU','Factors to convert concentrations from ppm to mg per normal cubic metre.'),
'KUSENBERG-AICHE-2021':('A2.4.b',95,'Scientific publication (Ghent University, AIChE meeting)','LU','Heteroatom specifications of steam cracker feedstocks, including chlorine.'),
'KUSENBERG-WM-2022':('A2.4.b',95,'Peer-reviewed scientific publication (Waste Management, 2022)','LU','Review of post-consumer plastic waste pyrolysis oils: typical chlorine content compared with the steam cracker limit.'),
'BOREALIS-EP4389855':('A2.4.b',90,'Patent (commercial source)','LU','Chlorine target of a pyrolysis oil purification process described by Borealis.'),
'ISO8217-2024-UKPI':('A2.4.b',80,'Secondary source (industry article on a paid standard)','LU','Organic chloride limit of the marine fuel standard ISO 8217:2024, as reported by the UK P&I Club.'),
'IED-2010-75-ART50':('A2.4.b',100,'EU legislation','LU','Directive 2010/75/EU, Article 50(2): combustion temperature for hazardous waste with more than 1 % halogenated organic substances.'),
'ARRETE-2910-2018':('A2.4.b',100,'French regulation','LU','Arrêté of 3 August 2018 on combustion plants below 50 MW (ICPE 2910): fuels and their maximum contents are set by the prefectural permit.'),
'FPR-2019-1009':('A2.4.c',100,'EU legislation','LU','Regulation (EU) 2019/1009 on EU fertilising products: contaminant limits for soil improvers and fertilisers, and admissible inputs for pyrolysis materials (CMC 14).'),
'ARRETE-CSR-2016':('A2.4.c',100,'French regulation','LU','Arrêté of 23 May 2016 on solid recovered fuels (CSR): minimum calorific value and limits for mercury and halogens.'),
'NIST-WEBBOOK-GAZ':('A2.4.d',100,'Reference data (NIST Chemistry WebBook)','LU','Molar masses, heats of combustion and heats of formation of the gases found in the pyrolysis gas.'),
'NIST-SP811-B9':('A2.4.d',100,'Reference data (NIST Special Publication 811)','LU','Energy unit conversion factors (kilowatt-hour, calorie).'),
}
FILES={
'A2.1.a':('A2-1-a-chiba-test-sheets.md','Chiba test programme: organisation and test sheets'),
'A2.1.b':('A2-1-b-chiba-mass-energy-balances.md','Chiba test programme: mass and energy balances, summary'),
'A2.1.c':('A2-1-c-chiba-distillation.md','Chiba test programme: oil distillation'),
'A2.1.d':('A2-1-d-chiba-permit.md','Chiba prefectural authorisation of the tests'),
'A2.2.a':('A2-2-a-jlos-oil-analyses.md','Oil analyses, Japan Lubricating Oil Society (2022)'),
'A2.2.b':('A2-2-b-oosumi-char.md','Char heavy metals and leaching, Oosumi (2022)'),
'A2.2.c':('A2-2-c-oosumi-process-water.md','Process water analyses, Oosumi (2022)'),
'A2.2.d':('A2-2-d-oosumi-exhaust-2022.md','Exhaust gas measurements, Oosumi (2022)'),
'A2.2.e':('A2-2-e-oosumi-odour-noise-2022.md','Odour, noise and vibration, Oosumi (2022)'),
'A2.2.f':('A2-2-f-kanso-gas-analysis-2020.md','Pyrolysis gas analysis, KANSO Technos (2020)'),
'A2.2.g':('A2-2-g-kanso-exhaust-odour-2020.md','Exhaust gas and odour, KANSO Technos (2020)'),
'A2.2.h':('A2-2-h-exhaust-dioxins-2023.md','Exhaust gas, odour and dioxins (2023)'),
'A2.2.i':('A2-2-i-nkkk-oil-2019.md','Fuel oil analysis, NKKK (2019)'),
'A2.2.j':('A2-2-j-izumitec-char-oil.md','Calorific values of char and oil, Izumitec (2023)'),
'A2.2.k':('A2-2-k-orist-gcms.md','GC-MS of a liquid sample, ORIST'),
'A2.3.a':('A2-3-a-oneworld-urc2000-brochure.md','OneWorld URC-2000 brochure (Japanese)'),
'A2.3.b':('A2-3-b-oneworld-english-brochure.md','OneWorld Urban Rig brochure (English, 2019)'),
'A2.3.c':('A2-3-c-oneworld-energy-table.md','Energy consumption table (manufacturer files)'),
'A2.3.d':('A2-3-d-oneworld-demonstrations.md','OneWorld demonstration runs (2020, 2021)'),
'A2.4.a':('A2-4-a-eu-emission-limits.md','EU emission limits and conversion rules'),
'A2.4.b':('A2-4-b-chlorine-references.md','Chlorine reference values by outlet'),
'A2.4.c':('A2-4-c-char-outlet-references.md','Reference values for char outlets'),
'A2.4.d':('A2-4-d-thermochemical-data.md','Thermochemical reference data (NIST)'),
'A2.5.0':('A2-5-0-working-assumptions.md','Working assumptions (decisions D-016, D-020, D-021, D-024)'),
'A2.5.a':('A2-5-a-calc-conversion-to-fuel.md','Calculation: oil and gas yields per run'),
'A2.5.b':('A2-5-b-calc-municipal-waste.md','Calculation: municipal waste runs on the convertible fraction'),
'A2.5.c':('A2-5-c-calc-gas-calorific-value.md','Calculation: pyrolysis gas composition without air and calorific value'),
'A2.5.d':('A2-5-d-calc-energy-balance.md','Calculation: energy balance of the continuous URC-2000'),
'A2.5.e':('A2-5-e-calc-emissions.md','Calculation: emission conversions and oxygen correction'),
'A2.5.f':('A2-5-f-calc-other.md','Calculation: chlorine ratios, OneWorld design figures and batch factors'),
}

def calc_file(cid):
    c=cid
    if re.search(r'CONV-(PE|PP|PS|3P)|OFFGAS-|RDT-HUILE-05|RDT-HUILE-07',c): return 'A2.5.a'
    if re.search(r'NODA|NONPLAST|BROYAGE|RDT-HUILE-09',c) and not re.search(r'NRJ|COUV',c): return 'A2.5.b'
    if re.search(r'GC-|VAP-EAU|PCI-|GAZ-PCI|GAZ-PART',c): return 'A2.5.c'
    if re.search(r'BRULEUR|FIOUL|ELEC|NRJ-|COUV-',c): return 'A2.5.d'
    if re.search(r'NOX|SO2|HCL|POUSS|O2MAX|FACTEUR-O2',c): return 'A2.5.e'
    return 'A2.5.f'

RUN={'PE-GRAN':'PE pellets, 2022-03-02','PE-CHUTES':'PE moulding offcuts, 2022-03-09','PE-BIDONS':'PE containers, 2022-06-21','PP-GRAN':'PP pellets, 2022-04-08','PP-CHUTES':'PP moulding offcuts, 2022-04-16','PP-PALETTES':'PP pallets, 2022-06-28','PS-GRAN':'PS pellets, 2022-03-17','PS-CHUTES':'PS moulding offcuts, 2022-03-31','PS-EXPANSE':'PS foam, 2022-07-07','3P-0526':'PE/PP/PS mix, 2022-05-26','3P-0711':'PE/PP/PS mix, 2022-07-11'}
CASE={'RESINE':'resin-rich feed (OneWorld design, 90 % resins)','OM':'household waste with 10 % resins (OneWorld design)','NODA':'municipal packaging plastics, per tonne of convertible material (Noda run coefficients)'}
def desc(c):
    k=c.replace('CALC-A2-','')
    m=re.match(r'CONV-(PE|PP|PS|3P)-(.+)',k)
    if m and k[5:] in RUN: return f'Conversion to fuel (oil plus gas) on input weight, {RUN[k[5:]]}.'
    d={
    'OFFGAS-0526':'Gas (by difference) as a share of input, PE/PP/PS mix, 2022-05-26.',
    'OFFGAS-0711':'Gas (by difference) as a share of input, PE/PP/PS mix, 2022-07-11.',
    'RDT-HUILE-0526':'Oil yield on total input, PE/PP/PS mix, 2022-05-26.',
    'RDT-HUILE-0711':'Oil yield on total input, PE/PP/PS mix, 2022-07-11.',
    'CONV-NODA-0909-TOTAL':'Conversion to fuel (oil plus gas) on total input, municipal packaging plastics, 2022-09-09.',
    'CONV-NODA-0909-HORSMETAUX':'Conversion to fuel (oil plus gas) on input minus metals and foreign matter, municipal packaging plastics, 2022-09-09.',
    'CONV-NODA-0915-TOTAL':'Conversion to fuel (oil plus gas) on total input, municipal non-combustible residue, 2022-09-15.',
    'CONV-NODA-0915-HORSMETAUX':'Conversion to fuel (oil plus gas) on input minus metals and foreign matter, municipal non-combustible residue, 2022-09-15.',
    'HUILE-NODA-0909-HORSMETAUX':'Oil yield on input minus metals and foreign matter, municipal packaging plastics, 2022-09-09.',
    'HUILE-NODA-0915-HORSMETAUX':'Oil yield on input minus metals and foreign matter, municipal non-combustible residue, 2022-09-15.',
    'NONPLAST-NODA-0909':'Share of metals and foreign matter in the input, municipal packaging plastics, 2022-09-09.',
    'NONPLAST-NODA-0915':'Share of metals and foreign matter in the input, municipal non-combustible residue, 2022-09-15.',
    'CONV-BROYAGE-0809':'Weight lost in the reactor (input minus residue removed), shredder residue, 2022-08-09.',
    'GC-COMBUSTIBLES':'Combustible gases (hydrogen, methane, C2 and C3 hydrocarbons, carbon monoxide) in the sample, % by volume.',
    'GC-SOMME':'Sum of the components reported in the gas analysis, % by volume.',
    'GAZ-PART-COMBUSTIBLE':'Share of combustible gases in the pyrolysis gas once oxygen and nitrogen (air) are removed.',
    'VAP-EAU':'Heat of vaporisation of water at 25 °C, as the difference between the heats of formation of liquid and gaseous water.',
    'PCI-CH4':'Net calorific value of methane: heat of combustion minus the vaporisation of the 2 moles of water formed.',
    'PCI-C2H6':'Net calorific value of ethane: heat of combustion minus the vaporisation of the 3 moles of water formed.',
    'PCI-C2H4':'Net calorific value of ethylene: heat of combustion minus the vaporisation of the 2 moles of water formed.',
    'PCI-C3H8':'Net calorific value of propane: heat of combustion minus the vaporisation of the 4 moles of water formed.',
    'PCI-C3H6':'Net calorific value of propylene: heat of combustion minus the vaporisation of the 3 moles of water formed.',
    'PCI-CO':'Net calorific value of carbon monoxide: heat of formation of CO2 minus that of CO.',
    'GAZ-PCI':'Net calorific value of the pyrolysis gas per kilogram: sum of (share x molar net calorific value) divided by sum of (share x molar mass), over hydrogen to carbon dioxide.',
    'BRULEUR-MJ-T':'Heat demand of the superheating burner per tonne treated, at 833 kcal/s continuous and 200 t/day.',
    'FIOUL-MJ-T':'Energy of the stated fuel consumption (10,000 L/day for 200 t) per tonne, if the fuel is the plant\'s own oil.',
    'ELEC-MJ-T':'Electricity (600 kW continuous) per tonne treated at 200 t/day.',
    'ELEC-ECART':'Ratio between the two electricity figures (600 and 20).',
    'FIOUL-T-CONTINU':'Fuel per tonne from the consumption table (10,000 L/day for 200 t/day).',
    'COUV-BRULEUR-RESINE':'Energy in the gas divided by the burner heat demand, '+CASE['RESINE']+'.',
    'COUV-BRULEUR-OM':'Energy in the gas divided by the burner heat demand, '+CASE['OM']+'.',
    'COUV-BRULEUR-NODA':'Energy in the gas divided by the burner heat demand, '+CASE['NODA']+'.',
    'COUV-FIOUL-RESINE':'Energy in the gas divided by the stated fuel consumption, '+CASE['RESINE']+'.',
    'COUV-FIOUL-OM':'Energy in the gas divided by the stated fuel consumption, '+CASE['OM']+'.',
    'COUV-FIOUL-NODA':'Energy in the gas divided by the stated fuel consumption, '+CASE['NODA']+'.',
    'NOX-MG-2022MAX':'Highest 2022 nitrogen oxides value (43 ppm) in mg/Nm³ of NO2, without oxygen correction.',
    'NOX-MG-2023':'2023 nitrogen oxides (30 ppm) in mg/Nm³ of NO2, without oxygen correction.',
    'NOX-MG-2020':'2020 nitrogen oxides (15 ppm) in mg/Nm³ of NO2, without oxygen correction.',
    'SO2-MG-2022MAX':'Highest 2022 sulphur oxides value (1.4 ppm) in mg/Nm³ of SO2.',
    'SO2-MG-2020':'2020 sulphur oxides (below 1 ppm) in mg/Nm³ of SO2.',
    'SO2-MG-2023':'2023 sulphur oxides (below 0.5 ppm) in mg/Nm³ of SO2.',
    'HCL-MG-2020':'2020 hydrogen chloride (below 1 ppm) in mg/Nm³.',
    'POUSS-MG-2022MAX':'Highest 2022 dust value (0.004 g/m³) in mg/Nm³.',
    'POUSS-MG-2023':'2023 dust value (below 0.005 g/m³N) in mg/Nm³.',
    'FACTEUR-O2-2020':'Correction factor to 11 % oxygen for the 2020 sample (18.5 % oxygen measured).',
    'NOX-2020-CORRIGE':'2020 nitrogen oxides corrected to 11 % oxygen.',
    'HCL-2020-CORRIGE':'2020 hydrogen chloride corrected to 11 % oxygen (upper bound).',
    'POUSS-2020-CORRIGE':'2020 dust corrected to 11 % oxygen (upper bound).',
    'O2MAX-NOX-IED':'Highest measured oxygen content for which the 2022 nitrogen oxides stay below the legal limit of 200 mg/Nm³ at 11 % oxygen.',
    'O2MAX-NOX-BAT':'Highest measured oxygen content for which the 2022 nitrogen oxides stay below 120 mg/Nm³ (top of the BAT range).',
    'O2MAX-DIOX-IED':'Highest measured oxygen content for which the 2022 dioxins stay below the legal limit of 0.1 ng/Nm³ at 11 % oxygen.',
    'O2MAX-POUSS-IED':'Highest measured oxygen content for which the 2022 dust stays below the legal limit of 10 mg/Nm³ at 11 % oxygen.',
    'JLOS-CL-EMB-PPM':'Chlorine of the oil from municipal packaging plastics, converted from % by mass to ppm.',
    'JLOS-CL-RES-PPM':'Chlorine of the oil from municipal non-combustible residue, converted from % by mass to ppm.',
    'CL-VAPO-EMB':'Chlorine of the packaging plastics oil divided by the 3 ppm steam cracker limit.',
    'CL-VAPO-RES':'Chlorine of the non-combustible residue oil divided by the 3 ppm steam cracker limit.',
    'OW16-HUILE-TOTALE':'Total oil in OneWorld\'s design output (gas oil + heating oil + heavy oil), % of input.',
    'OW16-SOMME-MASSES':'Sum of the output masses in OneWorld\'s stated daily balance for 200 t of input.',
    'OW15-CADENCE':'Daily tonnage implied by 51 buckets of 4.5 m³ at a density of 0.6.',
    'UR2000-CADENCE':'Daily tonnage implied by 48 buckets of at most 4.17 t.',
    'UR2000-NONAFFECTE-MIN':'Share of input not allocated in OneWorld\'s household waste balance, with metals and glass at 5 %.',
    'UR2000-NONAFFECTE-MAX':'Share of input not allocated in OneWorld\'s household waste balance, with metals and glass at 0 %.',
    'OWJ-HUILE':'Cumulative oil yield of the three URT-10 runs of December 2021.',
    }
    if k in d: return d[k]
    m=re.match(r'NRJ-(GAZ|HUILE|CHAR)-(\w+)',k)
    if m: return {'GAZ':'Energy in the gas','HUILE':'Energy in the oil','CHAR':'Energy in the char'}[m.group(1)]+' per tonne of feed, '+CASE[m.group(2)]+'.'
    return calcs[c].get('description','')


INTRO={
'A2.5.c':'''## Method

The gas analysis (Annex 2.2.f) was taken at the outlet of the unit, where the pyrolysis gas mixes with air. Oxygen and nitrogen do not come from the plastic; they come from the air. Following decision D-021 ([Annex 2.5.0](A2-5-0-working-assumptions.md)), the pyrolysis gas is taken as the other eight components, from hydrogen to carbon dioxide, rescaled to 100 %.

The calculation then runs in four steps:

1. **Water vaporisation.** Heat needed to vaporise the water formed (CALC-A2-VAP-EAU), from the NIST heats of formation of liquid and gaseous water (Annex 2.4.d).
2. **Net value of each gas.** Heat of combustion per mole minus the vaporisation of the water it forms. For hydrogen, the net value is the heat of formation of water vapour; for carbon monoxide, the difference between the heats of formation of CO2 and CO. Carbon dioxide does not burn (net value 0).
3. **Weighting.** Each net value is weighted by the share of the gas in the analysis. The sum is divided by the average molar mass of the mixture, carbon dioxide included, to give the net calorific value per kilogram of pyrolysis gas.
4. **Use.** This value is applied to the gas mass of each run or design case (Annex 2.5.d).

Note: the molar shares in the second table of the annex (for example hydrogen 64.5 %) are each component's share divided by their sum of 19.7 % [calc:CALC-A2-GC-SOMME] minus oxygen and nitrogen; they do not enter the calculation separately, because the weighting already uses the raw shares.

## Calculations
''',
'A2.5.d':'''## Method

The energy balance of the continuous URC-2000 uses OneWorld's figures, taken as correct by decision D-021 ([Annex 2.5.0](A2-5-0-working-assumptions.md)). Batch tests are used only for conversion coefficients.

1. **Heat demand.** Burner rating 833 kcal/s, operated 24 hours a day, divided by 200 t/day (CALC-A2-BRULEUR-MJ-T).
2. **Stated fuel.** 10,000 L/day of the plant's own oil, at the density and gross calorific value measured by JLOS, divided by 200 t/day (CALC-A2-FIOUL-MJ-T). Used as the upper value of the fuel need.
3. **Energy in the products** for three feeds:
   - resin-rich feed (OneWorld design, English brochure p. 16);
   - household waste with 10 % resins (OneWorld design, URC-2000 brochure p. 5);
   - municipal packaging plastics (Noda test coefficients, per tonne of convertible material).

   The values are 46,000 J/g for the oil, 37.4 MJ/kg for the gas (Annex 2.5.c) and 32,090 J/g for the char.
4. **Coverage.** Energy in the gas divided by the heat demand and by the stated fuel.

## Calculations
''',
}


# ---- ajouts du 14/10/2026 soir (chlore, SEA CORAL, GC-MS, carbureacteur)
NEW_SRC={
'CHIBA-PROCEDE-HUILE':('A2.1.a',100,'Test report filed with the Chiba prefecture (operator: Asada Shokai)','LU','On the Noda test unit, the gas from the pyrolysis furnace passes through a catalytic reaction tank before the condenser; oil and water are measured by dipstick after settling in drums.'),
'CHIBA-CONSTATS':('A2.1.b',100,'Test report filed with the Chiba prefecture (operator: Asada Shokai)','LU','Findings of the 2022 test programme: the Noda unit is a test unit without a wastewater treatment step; dioxins 0.067 ng-TEQ/Nm³; issues to solve before a commercial unit.'),
'UR2000-JP-P03-P04-CHLORE':('A2.3.a',95,'Manufacturer documentation (OneWorld)','CONSTRUCTEUR','OneWorld states that chlorine from PVC becomes dilute hydrochloric acid in the steam, and that the vapours pass a catalytic layer for chlorine and carbon adsorption before the condenser.'),
'OW-ENG-P13-SEACORAL':('A2.3.b',95,'Manufacturer documentation (OneWorld)','CONSTRUCTEUR','SEA CORAL ceramic water purifier, presented as an option of the Urban Rig.'),
'SEACORAL-DETAIL-ENG':('A2.3.e',95,'Manufacturer documentation (OneWorld)','CONSTRUCTEUR','SEA CORAL documentation: seawater desalination test, stated capacity per blower, patents. No test on pyrolysis process water.'),
'NIST-WEBBOOK-TEB':('A2.4.d',100,'Reference data (NIST Chemistry WebBook)','LU','Normal boiling points of 1-nonene, 1-undecene, 1-tridecene and n-hexadecane.'),
'NIST-SP811-CELSIUS':('A2.4.d',100,'Reference data (NIST Special Publication 811)','LU','Definition of the degree Celsius (T0 = 273.15 K).'),
'ANCAP-JETA1-2026':('A2.4.e',90,'Product specification of a refiner (ANCAP), aligned with the AFQRJOS check list','LU','Jet A-1 specification limits: distillation, flash point, density, freezing point, aromatics, specific energy.'),
'REFUELEU-2023-2405':('A2.4.e',95,'EU regulation, read in a reproduction','LU','ReFuelEU Aviation: definition of sustainable aviation fuels, including recycled carbon aviation fuels, and minimum shares from 2030.'),
}
NEW_FILES={
'A2.3.e':('A2-3-e-oneworld-sea-coral.md','OneWorld SEA CORAL water purifier documentation'),
'A2.4.e':('A2-4-e-jet-fuel-references.md','Jet fuel specification and SAF regulation'),
'A2.5.g':('A2-5-g-calc-gcms.md','Calculation: GC-MS composition of the oil and boiling points'),
}
NEW_DESC={
'CALC-A2-GCMS-JET-ECH-BAS':'Low estimate of the share of the sample made of hydrocarbons with 8 to 16 carbon atoms (high library match only), taking peak area as mass (working assumption D-024).',
'CALC-A2-GCMS-JET-ECH-HAUT':'High estimate of the share of the sample made of hydrocarbons with 8 to 16 carbon atoms (all named hydrocarbons), taking peak area as mass (working assumption D-024).',
'CALC-A2-GCMS-TMN':'Share of peak area of the peaks named trimethylnonene (12 carbon atoms).',
'CALC-A2-GCMS-SOMME':'Sum of the peak area shares of the 71 peaks (check of the transcription).',
'CALC-A2-GCMS-OLEF':'Share of peak area of the olefins (alkenes, cycloalkenes, dienes) in the GC-MS list.',
'CALC-A2-GCMS-JET':'Share of peak area of the named hydrocarbons with 8 to 16 carbon atoms (probable and possible identifications).',
'CALC-A2-GCMS-JET-EST':'Share of peak area of the hydrocarbons with 8 to 16 carbon atoms identified with a high library match (probable compounds only).',
'CALC-A2-GCMS-LOURD':'Share of peak area of the named hydrocarbons with more than 16 carbon atoms.',
'CALC-A2-GCMS-OXY':'Share of peak area of the possible oxygenated compounds (esters, alcohols).',
'CALC-A2-GCMS-NONID':'Share of peak area of the unidentified peaks and of the peaks only described as aliphatic hydrocarbon.',
'CALC-A2-GCMS-C9':'Share of peak area of the hydrocarbons with 9 carbon atoms.',
'CALC-A2-GCMS-C10':'Share of peak area of the hydrocarbons with 10 carbon atoms.',
'CALC-A2-GCMS-C11':'Share of peak area of the hydrocarbons with 11 carbon atoms.',
'CALC-A2-GCMS-C12':'Share of peak area of the hydrocarbons with 12 carbon atoms.',
'CALC-A2-GCMS-C13':'Share of peak area of the hydrocarbons with 13 carbon atoms.',
'CALC-A2-GCMS-NAPHT':'Share of peak area of the named cycloalkanes (naphthenes).',
'CALC-A2-GCMS-ISOPAR':'Share of peak area of the named branched alkanes.',
'CALC-A2-GCMS-VOLAT':'Share of the "drain" sample that evaporated after 5 minutes at 350 °C.',
'CALC-A2-TEB-NONENE':'Normal boiling point of 1-nonene in degrees Celsius.',
'CALC-A2-TEB-UNDECENE':'Normal boiling point of 1-undecene in degrees Celsius.',
'CALC-A2-TEB-TRIDECENE-BAS':'Normal boiling point of 1-tridecene in degrees Celsius, lowest NIST value.',
'CALC-A2-TEB-TRIDECENE-HAUT':'Normal boiling point of 1-tridecene in degrees Celsius, highest NIST value.',
'CALC-A2-TEB-HEXADECANE':'Normal boiling point of n-hexadecane in degrees Celsius.',
}

SRC.update(NEW_SRC); FILES.update(NEW_FILES)
_cf0=calc_file
def calc_file(cid):
    if re.search(r'GCMS|TEB-',cid): return 'A2.5.g'
    return _cf0(cid)
_desc0=desc
def desc(c):
    return NEW_DESC[c] if c in NEW_DESC else _desc0(c)

# =====================================================================
# Rendu HTML
# =====================================================================
import html as H, json, markdown

HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.normpath(os.path.join(HERE,'..','..','..'))           # depot
WF=os.path.join(ROOT,'working-folder')
OUTD=HERE; PREUVES=os.path.join(OUTD,'preuves')
os.makedirs(PREUVES,exist_ok=True)
ev=yaml.safe_load(open(os.path.join(WF,'params','_evidence.yaml'),encoding='utf-8'))
ext=yaml.safe_load(open(os.path.join(WF,'reference','sources-externes','registre-sources.yaml'),encoding='utf-8'))
calcs=yaml.safe_load(open(os.path.join(WF,'controle-sources','calculs.yaml'),encoding='utf-8'))
MD=open(os.path.join(ROOT,'nouveau-business-plan','annexes','ANNEX-02-Technical-Evidence.md'),encoding='utf-8').read()
FULLMD=open(os.path.join(ROOT,'nouveau-business-plan','annexes','annexe-02-preuves','A2-4-3-oil-gcms-full-analysis.md'),encoding='utf-8').read()
HYP=set(k for k in calcs if k.startswith('CALC-A2-') and re.search(r'GAZ-PCI|GAZ-PART|NRJ-|COUV-|BRULEUR-MJ|FIOUL-MJ|ELEC-MJ|JET-ECH',k))

def calc_conf(cid,seen=None):
    seen=seen or set()
    if cid in seen: return 100
    seen.add(cid); confs=[]
    for n,e in (calcs[cid].get('entrees') or {}).items():
        if 'calc' in e: confs.append(calc_conf(e['calc'],seen))
        else: confs.append(SRC[e['source']][1] if e['source'] in SRC else 95)
    base=min(confs) if confs else 95
    return min(base,90) if cid in HYP else min(base,95)

# ---- codes : une page par preuve
GROUPS=[('2.1','Test reports filed with the authorities'),('2.2','Independent laboratory reports'),('2.3','Manufacturer documentation (OneWorld)'),('2.4','Regulations and reference data'),('2.5','Calculations')]
letters='abcdefghijklmnopqrstuvwxyz'
CODE={}; ORDER=[]
for gnum,_ in GROUPS[:4]:
    ids=[i for i in SRC if SRC[i][0].startswith('A'+gnum)]
    for n,i in enumerate(ids): CODE[i]=f'{gnum}.{letters[n]}'; ORDER.append(i)
used=set(re.findall(r'\[calc:([A-Z0-9\-]+)\]',MD+FULLMD))
need=set()
def dep(c):
    if c in need or c not in calcs: return
    need.add(c)
    for n,e in (calcs[c].get('entrees') or {}).items():
        if 'calc' in e: dep(e['calc'])
for c in used: dep(c)
dep('CALC-A2-GC-SANS-AIR')
CGROUP={'A2.5.a':'a','A2.5.b':'b','A2.5.c':'c','A2.5.d':'d','A2.5.e':'e','A2.5.f':'f','A2.5.g':'g'}
order_c=['VAP-EAU','PCI-','GC-SOMME','GC-SANS','GC-COMB','GAZ-PART','GAZ-PCI']
def ckey(c):
    for n,o in enumerate(order_c):
        if o in c: return (calc_file(c),n,c)
    return (calc_file(c),99,c)
cnt={}
for c in sorted(need,key=ckey):
    g=CGROUP[calc_file(c)]; cnt[g]=cnt.get(g,0)+1
    CODE[c]=f'2.5.{g}.{cnt[g]}'; ORDER.append(c)
CODE['ASSUMPTIONS']='2.5.0'
def fname(i): return 'A'+CODE[i].replace('.','-')+'.html'

GTITLE={'A2.5.a':'Oil and gas yields per run','A2.5.b':'Municipal waste runs on the convertible fraction','A2.5.c':'Pyrolysis gas without air and its calorific value','A2.5.d':'Energy balance of the continuous URC-2000','A2.5.e':'Emission conversions and oxygen correction','A2.5.f':'Chlorine ratios, OneWorld design figures and batch factors','A2.5.g':'GC-MS composition of the oil and boiling points'}

CSS='''
:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#6b6a65;--line:#dedbd2;--accent:#1f5f8b;--box:#f1eee6;--good:#2e6b3f;}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17181a;--fg:#e9e7e1;--muted:#a3a19a;--line:#34363a;--accent:#7fb3d9;--box:#222428;--good:#7cc08f;}}
:root[data-theme="dark"]{--bg:#17181a;--fg:#e9e7e1;--muted:#a3a19a;--line:#34363a;--accent:#7fb3d9;--box:#222428;--good:#7cc08f;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,"Times New Roman",serif}
main{max-width:860px;margin:0 auto;padding:32px 16px 80px}
h1{font-size:1.9rem;line-height:1.2;margin:.2em 0 .4em}
h2{font-size:1.35rem;margin:2.2em 0 .6em;padding-top:.6em;border-top:1px solid var(--line)}
h3{font-size:1.1rem;margin:1.6em 0 .4em}
p,li{max-width:72ch}
a{color:var(--accent)}
table{border-collapse:collapse;width:100%;margin:1em 0;font:14px/1.45 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;display:block;overflow-x:auto}
th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{font-weight:600;background:var(--box)}
code,pre{font:13px/1.5 ui-monospace,Menlo,Consolas,monospace}
pre{background:var(--box);padding:10px 12px;border-radius:6px;overflow-x:auto}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
.ev{white-space:nowrap}
.ev a{display:inline-block;font:600 11px/1 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;text-decoration:none;color:var(--accent);border:1px solid var(--accent);border-radius:9px;padding:2px 6px;margin-left:3px;vertical-align:2px;opacity:.85}
.ev a:hover{opacity:1;background:var(--accent);color:var(--bg)}
.crumb{font:14px/1.4 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--muted)}
.cards{display:grid;grid-template-columns:2fr 1fr;gap:14px;margin:18px 0 26px}
@media (max-width:640px){.cards{grid-template-columns:1fr}}
.card{background:var(--box);border-radius:10px;padding:14px 16px}
.card h4{margin:0 0 6px;font:600 12px/1.2 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.card p{margin:0}
.conf{font:700 2.4rem/1 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--good);margin:4px 0 6px}
.small{font-size:.9rem;color:var(--muted)}
.result{font-size:1.15rem;background:var(--box);border-left:4px solid var(--good);padding:10px 14px;border-radius:6px}
'''
BANNIERE=('<!-- Fichier genere par generer_html.py a partir de ANNEX-02-Technical-Evidence.md, de annexe-02-preuves/ et des registres. '
          'Ne pas modifier a la main : corriger la source, puis regenerer. -->')
def page(title,body,crumb=''):
    return f'''<!doctype html>
{BANNIERE}
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)}</title><style>{CSS}</style></head>
<body><main>{crumb}{body}</main></body></html>'''

def esc(x): return H.escape(str(x))
def pdf_links(chemin, depth):
    out=[]
    for part in str(chemin).split(';'):
        p=part.strip().split(' (')[0].replace('doublon probable : ','')
        if p.startswith('reference/'):
            rel='../'*depth+'../../../working-folder/'+p
            out.append(f'<a href="{H.escape(rel)}"><code>{esc(os.path.basename(p))}</code></a>')
    return ' ; '.join(out)
def fiche(i): return ev.get(i) or ext.get(i) or {}
def link(i,depth=1):
    pre='' if depth==1 else 'preuves/'
    return f'<a href="{pre}{fname(i)}" title="{esc(i)}">{CODE[i]}</a>'

CR=lambda: '<p class="crumb"><a href="../index.html">Annex 2. Technical Evidence</a> · <a href="index.html">All evidence sheets</a></p>'

def source_page(i):
    f=fiche(i); code,conf,nature,label,summ=SRC[i]
    files=pdf_links(f.get('chemin',''),1) if f.get('chemin') else ''
    if f.get('url'): files=(files+' ; ' if files else '')+f'<a href="{esc(f["url"])}">{esc(f.get("titre","online source"))}</a>'
    quotes=''.join(f'<li>« {esc(v)} »'+('' if k=='citation' else f' <span class="small">({esc(k.replace("citation_",""))})</span>')+'</li>' for k,v in f.items() if k.startswith('citation'))
    vals=''.join(f'<li>{esc(f[k])}</li>' for k in ['contenu']+[x for x in f if str(x).startswith('valeurs_lues')] if f.get(k))
    notes=''.join(f'<li>{esc(f[k])}</li>' for k in ['reserve','note','note_inventaire_2026_10_14','correction']+[x for x in f if str(x).startswith('correction_')] if f.get(k))
    jp = 'Japanese original; the quotation below is reproduced in the original language. ' if re.search(r'[぀-ヿ一-鿿]', str(f.get('citation',''))+str(f.get('titre',''))) else ''
    body=f'''<h1>Evidence {CODE[i]}</h1>
<p class="small">{esc(f.get('titre',''))}</p>
<div class="cards">
 <div class="card"><h4>What this evidence shows</h4><p>{esc(summ)}</p></div>
 <div class="card"><h4>Confidence</h4><div class="conf">{conf} %</div><p class="small">{esc(nature)}</p></div>
</div>
<h2>How it was obtained</h2>
<p>{jp}The figures were read directly in the source document below, at the location indicated, and recorded in the project register under <code>{esc(i)}</code>.</p>
<table><tr><th>Source document</th><td>{files}</td></tr>
<tr><th>Location in the document</th><td>{esc(f.get('emplacement',''))}</td></tr>
<tr><th>Nature of the source</th><td>{esc(nature)}</td></tr>
<tr><th>Status</th><td>{esc(label)}: read in the original, not yet cross-checked by a second reader</td></tr></table>
{('<h2>Quotation (original language)</h2><ul>'+quotes+'</ul>') if quotes else ''}
<h2>Values read</h2><p class="small">As recorded in the project register (in French).</p><ul>{vals}</ul>
{('<h2>Notes</h2><ul>'+notes+'</ul>') if notes else ''}'''
    return page(f'Evidence {CODE[i]}',body,CR())

def method_text(c):
    g=calc_file(c)
    if g in INTRO:
        t=INTRO[g].split('## Calculations')[0].replace('## Method','').strip()
        t=re.sub(r'\[calc:[^\]]+\]','',t)
        t=re.sub(r'\]\([^)]*A2-5-0-working-assumptions\.md[^)]*\)','](A2-5-0.html)',t)
        t=re.sub(r'\[([^\]]+)\]\([^)]*\.md[^)]*\)',r'\1',t)
        def _fc(m):
            k=m.group(1); ids=[i for i in ORDER if i in SRC and SRC[i][0]=='A'+k]
            if ids: return '<a href="'+fname(ids[0])+'">'+CODE[ids[0]]+'</a>'
            return 'sheet group '+k
        t=re.sub(r'Annex (2\.[1-4]\.[a-z])\b',_fc,t)
        t=re.sub(r'Annex (2\.5\.[a-f])\b',lambda m:'the sheets '+m.group(1)+'.x',t)
        t=re.sub(r'\(?(CALC-A2-[A-Z0-9\-]+)\)?',lambda m:'(<a href="'+fname(m.group(1))+'">'+CODE[m.group(1)]+'</a>)' if m.group(1) in CODE else m.group(0),t)
        t=t.replace('%  minus','%, without').replace('Annex 2.5.0','sheet 2.5.0')
        return markdown.markdown(t)
    return f'<p>{esc(desc(c))} The result is obtained by applying the formula below to the inputs listed, each taken from its own evidence sheet.</p>'

def calc_page(c):
    f=calcs[c]; conf=calc_conf(c)
    rows=''
    for n,e in (f.get('entrees') or {}).items():
        if 'calc' in e:
            r=calcs[e['calc']].get('resultat','')
            rows+=f'<tr><td><code>{esc(n)}</code></td><td>{esc(r)} {esc(calcs[e["calc"]].get("unite",""))}</td><td>{esc(desc(e["calc"]))}</td><td><span class="ev">{link(e["calc"])}</span></td></tr>'
        else:
            s=e['source']
            rows+=f'<tr><td><code>{esc(n)}</code></td><td>{esc(e["valeur"])} {esc(e.get("unite",""))}</td><td>{esc(e.get("emplacement",""))}</td><td><span class="ev">{link(s)}</span></td></tr>'
    basis = 'This calculation uses a working assumption decided by the project sponsor (<a href="A2-5-0.html">sheet 2.5.0</a>), so its confidence is capped at 90 %.' if c in HYP else 'This is a direct calculation on the inputs below; its confidence is that of its least reliable input, capped at 95 %.'
    body=f'''<h1>Evidence {CODE[c]}</h1>
<p class="small">Calculation · {esc(GTITLE[calc_file(c)])}</p>
<div class="cards">
 <div class="card"><h4>What this calculation gives</h4><p>{esc(desc(c))}</p><p class="result" style="margin-top:10px">Result: <strong>{esc(f["resultat"])}</strong> {esc(f.get("unite",""))}</p></div>
 <div class="card"><h4>Confidence</h4><div class="conf">{conf} %</div><p class="small">{basis}</p></div>
</div>
<h2>How it was calculated</h2>
{method_text(c)}
<h3>Formula</h3><pre>{esc(f["formule"])}</pre>
<h3>Inputs</h3>
<table><tr><th>Input</th><th>Value</th><th>Description or location</th><th>Evidence</th></tr>{rows}</table>
<p class="small">Register entry <code>{esc(c)}</code>. The formula is recalculated automatically by the project control script.</p>'''
    return page(f'Evidence {CODE[c]}',body,CR())

def assumptions_page():
    a=open(os.path.join(ROOT,'nouveau-business-plan','annexes','annexe-02-preuves','A2-5-0-working-assumptions.md'),encoding='utf-8').read()
    a=a.split('\n',3)[3] if a.count('\n')>3 else a
    a=re.sub(r'\[Back to Annex 2\][^\n]*\n','',a)
    a=re.sub(r'\s*\[hyp:[^\]]+\]','',a); a=re.sub(r'\s*\[[A-Z0-9\-]+\]','',a)
    a=re.sub(r'\(\[Annex 2\.2\.f\]\([^)]*\)\)','(<a href="'+fname('KANSO-B2002600')+'">'+CODE['KANSO-B2002600']+'</a>)',a)
    a=re.sub(r'\[Annex 2\.5\.c\]\([^)]*\)','<a href="'+fname('CALC-A2-GAZ-PCI')+'">'+CODE['CALC-A2-GAZ-PCI']+'</a>',a)
    a=re.sub(r'\[Annex 2\.2\.j\]\([^)]*\)','<a href="'+fname('IZUMITEC-R35-339439')+'">'+CODE['IZUMITEC-R35-339439']+'</a>',a)
    a=re.sub(r'\[Annex 2\.2\.a\]\([^)]*\)','<a href="'+fname('CHIBA-JLOS-HUILES')+'">'+CODE['CHIBA-JLOS-HUILES']+'</a>',a)
    a=re.sub(r'\[Annex 2\.3\.a\]\([^)]*\)','<a href="'+fname('UR2000-JP-P08-SPEC')+'">'+CODE['UR2000-JP-P08-SPEC']+'</a>',a)
    a=re.sub(r'\[Annex 2\.3\.c\]\([^)]*\)','<a href="'+fname('OW-CONSO-ENERGIE')+'">'+CODE['OW-CONSO-ENERGIE']+'</a>',a)
    body='''<h1>Evidence 2.5.0</h1><p class="small">Working assumptions</p>
<div class="cards"><div class="card"><h4>What this sheet shows</h4><p>The working assumptions decided by the project sponsor and recorded as dated decisions. Any figure that depends on them is capped at 90 % confidence.</p></div>
<div class="card"><h4>Confidence</h4><div class="conf">n/a</div><p class="small">Assumptions, not measurements.</p></div></div>'''+markdown.markdown(a)
    return page('Evidence 2.5.0',body,CR())

GRP=re.compile(r'\((?:\[Annex[^\]]*\]\([^)]*\)(?:, (?:\d+ %|assumption))?(?:; )?)+\)<!--\s*((?:\[[^\]]+\]\s*)+)-->')
def pills(s,depth):
    def rep(m):
        toks=re.findall(r'\[((?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+)\]',m.group(1))
        out=[]
        for t in toks:
            if t.startswith('hyp:'): out.append('<a href="'+('' if depth==1 else 'preuves/')+'A2-5-0.html">2.5.0</a>')
            else:
                k=t[5:] if t.startswith('calc:') else t
                if k in CODE: out.append(link(k,depth))
        return '<span class="ev">'+''.join(dict.fromkeys(out))+'</span>'
    return GRP.sub(rep,s)

def full_page():
    s=FULLMD
    s=re.sub(r'\[Back to Annex 2\][^\n]*\n','',s)
    s=pills(s,1)
    s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    s=re.sub(r'(?m)^((?!- |\d+\. |\s|\|)[^\n]+)\n(- |\d+\. )',r'\1\n\n\2',s)
    s=re.sub(r'(?m)^ {2,3}(?=\S)','    ',s)
    s=re.sub(r'(?m)^(    [^\n]+)\n(- |\d+\. )',r'\1\n\n\2',s)
    s=re.sub(r'(?m)^((?:- |\d+\. )[^\n]+)\n(    - )',r'\1\n\n\2',s)
    body=markdown.markdown(s,extensions=['tables','sane_lists'])
    body=body.replace('<h1>Annex 2.4.3. Oil composition by GC-MS: full analysis</h1>','<h1>Annex 2.4.3</h1><p class="small">Oil composition by GC-MS: full analysis and jet fuel reading</p>',1)
    return page('Annex 2.4.3. Oil GC-MS analysis',body,CR())

def index_page():
    rows=''
    for gnum,gt in GROUPS:
        rows+=f'<tr><th colspan="3">{gnum} · {esc(gt)}</th></tr>'
        if gnum=='2.4': rows+='<tr><td><a href="A2-4-3.html">2.4.3</a></td><td>Oil composition by GC-MS: full analysis and jet fuel reading</td><td>see each figure</td></tr>'
        if gnum=='2.5': rows+=f'<tr><td><a href="A2-5-0.html">2.5.0</a></td><td>Working assumptions (decisions D-016, D-020, D-021, D-024)</td><td>n/a</td></tr>'
        for i in ORDER:
            if not CODE[i].startswith(gnum+'.'): continue
            if i in SRC: t=fiche(i).get('titre',''); c=SRC[i][1]; d=SRC[i][4]
            else: d=desc(i); c=calc_conf(i)
            rows+=f'<tr><td><a href="{fname(i)}">{CODE[i]}</a></td><td>{esc(d)}</td><td>{c} %</td></tr>'
    body=f'''<h1>Annex 2. Evidence sheets</h1>
<p>Each figure of Annex 2 links to one of these sheets. Each sheet shows what the evidence supports, its confidence, and how the figure was obtained: the source document and page, or the formula and inputs of the calculation.</p>
<h2>Confidence scale</h2>
<table><tr><th>Confidence</th><th>Applies to</th></tr>
<tr><td>100 %</td><td>Tests filed with the authorities, independent laboratory reports, legislation and reference data</td></tr>
<tr><td>95 %</td><td>Manufacturer documentation (OneWorld), peer-reviewed literature, a laboratory report read in a reproduction, calculations on data at 95 % or more</td></tr>
<tr><td>90 %</td><td>Calculations using a working assumption, a manufacturer table without printed author, patents</td></tr>
<tr><td>80 %</td><td>Secondary sources</td></tr></table>
<p class="small">A calculation is never rated above its least reliable input, nor above 95 %.</p>
<h2>All sheets</h2><table><tr><th>Sheet</th><th>Content</th><th>Confidence</th></tr>{rows}</table>'''
    return page('Annex 2. Evidence sheets',body,'<p class="crumb"><a href="../index.html">Annex 2. Technical Evidence</a></p>')

def main_page():
    s=MD
    # section "How to read"
    i=s.index('## How to Read This Annex'); j=s.index('## 2.1 Test Programme Overview')
    s=s[:i]+'''## How to Read This Annex

The manufacturer's documentation is used as the design basis of the plant (decisions D-016, D-020 and D-021). The batch tests provide the conversion coefficients and the product qualities.

Each figure is followed by a small link, for example <span class="ev"><a href="preuves/'''+fname('CHIBA-ESSAIS-FICHES')+'''">'''+CODE['CHIBA-ESSAIS-FICHES']+'''</a></span>. It opens the evidence sheet: what the evidence shows, its confidence, the source document and page, or the calculation. All sheets are listed in the <a href="preuves/index.html">index of evidence sheets</a>.

---

'''+s[j:]
    grp=re.compile(r'\((?:\[Annex[^\]]*\]\([^)]*\)(?:, (?:\d+ %|assumption))?(?:; )?)+\)<!--\s*((?:\[[^\]]+\]\s*)+)-->')
    def rep(m):
        toks=re.findall(r'\[((?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+)\]',m.group(1))
        out=[]
        for t in toks:
            if t.startswith('hyp:'): k='ASSUMPTIONS'; out.append('<a href="preuves/A2-5-0.html">2.5.0</a>')
            else:
                k=t[5:] if t.startswith('calc:') else t
                if k in CODE: out.append(link(k,0))
        out=list(dict.fromkeys(out))
        return '<span class="ev">'+''.join(out)+'</span>'
    s=grp.sub(rep,s)
    s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    s=s.replace('[index of evidence files](annexe-02-preuves/README.md)','[index of evidence sheets](preuves/index.html)')
    s=re.sub(r'\[Annex 2\.5\.0\]\(annexe-02-preuves/A2-5-0-working-assumptions\.md\)','<a href="preuves/A2-5-0.html">2.5.0</a>',s)
    s=s.replace('(annexe-02-preuves/A2-4-3-oil-gcms-full-analysis.md)','(preuves/A2-4-3.html)')
    left=re.findall(r'\[Annex [^\]]+\]\(annexe-02-preuves[^)]*\)',s)
    s=re.sub(r'(?m)^---\s*$','',s)
    s=re.sub(r'(?m)^((?!- |\d+\. |\s|\|)[^\n]+)\n(- |\d+\. )',r'\1\n\n\2',s)
    s=re.sub(r'(?m)^ {2,3}(?=\S)','    ',s)
    s=re.sub(r'(?m)^(    [^\n]+)\n(- |\d+\. )',r'\1\n\n\2',s)
    s=re.sub(r'(?m)^((?:- |\d+\. )[^\n]+)\n(    - )',r'\1\n\n\2',s)
    htmlb=markdown.markdown(s,extensions=['tables','sane_lists'])
    return page('Annex 2. Technical Evidence',htmlb), left

if __name__=='__main__':
    mp,left=main_page()
    open(os.path.join(OUTD,'index.html'),'w',encoding='utf-8').write(mp)
    for i in ORDER:
        open(os.path.join(PREUVES,fname(i)),'w',encoding='utf-8').write(source_page(i) if i in SRC else calc_page(i))
    open(os.path.join(PREUVES,'A2-5-0.html'),'w',encoding='utf-8').write(assumptions_page())
    open(os.path.join(PREUVES,'index.html'),'w',encoding='utf-8').write(index_page())
    open(os.path.join(PREUVES,'A2-4-3.html'),'w',encoding='utf-8').write(full_page())
    print('pages',len(ORDER)+3,'liens non convertis',len(left))
    for l in left[:10]: print(' ',l[:120])
