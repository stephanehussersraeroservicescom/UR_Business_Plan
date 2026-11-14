import re,sys,importlib.util,os,yaml
ROOT=os.getcwd()
spec=importlib.util.spec_from_file_location('g',os.path.join(ROOT,'nouveau-business-plan/annexes/annexe-02-html/generer_html.py'))
g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
CALCS=yaml.safe_load(open('working-folder/controle-sources/calculs.yaml',encoding='utf-8'))
g.calcs.update(CALCS)
def anchor(t):
    a=t.strip().lower(); a=re.sub(r'[^\w\- ]','',a); return a.replace(' ','-')
def one(t):
    if t.startswith('hyp:'):
        return ('[Annex 2.5.0](annexe-02-preuves/A2-5-0-working-assumptions.md), assumption', f'[{t}]')
    if t.startswith('calc:'):
        c=t[5:]; assert c in CALCS, c
        code=g.calc_file(c); f=g.FILES[code][0]; conf=g.calc_conf(c)
        return (f'[Annex {code[1:]}](annexe-02-preuves/{f}#{anchor(c)}), {conf} %', f'[calc:{c}]')
    assert t in g.SRC, t
    code,conf=g.SRC[t][0],g.SRC[t][1]; f=g.FILES[code][0]
    return (f'[Annex {code[1:]}](annexe-02-preuves/{f}#{anchor(t)}), {conf} %', f'[{t}]')
def L(*ts):
    ps=[];ks=[]
    for t in ts:
        a,b=one(t)
        if a not in ps: ps.append(a)
        ks.append(b)
    return '('+'; '.join(ps)+')<!-- '+' '.join(ks)+' -->'
FI='CHIBA-ESSAIS-FICHES'; BIL='CHIBA-BILANS'; RAP='CHIBA-RAPPORT-2023'; OWJ='OWJ-DEMO-2021'; P16='OW-ENG-P16-BILAN'
p='nouveau-business-plan/annexes/ANNEX-02-Technical-Evidence.md'
s=open(p,encoding='utf-8').read()
def line(prefix):
    ls=[l for l in s.split('\n') if l.startswith(prefix)]
    assert len(ls)==1,(len(ls),prefix); return ls[0]
def rep(old,new,cnt=1):
    global s
    assert s.count(old)==cnt,(s.count(old),old[:100]); s=s.replace(old,new)
def repl(prefix,new):
    rep(line(prefix),new)
def links(l): return re.findall(r'\(\[Annex.*?-->',l)
# --- en-tete
repl('Version 3, draft of 14 October 2026, revision 3.','Version 3, draft of 15 October 2026, revision 4. Status: checked automatically; external cross-check of Sections 2.1 to 2.3 applied, later sections pending. <!-- nosrc -->')
# --- messages cles
repl('- In 11 batch runs on clean PE, PP and PS',f'- In 11 batch runs on PE, PP and PS filed with the Chiba prefectural government in 2022, one mixed-plastic run is excluded from the averages (Section 2.2.1) {L("hyp:D-034")}. Of the 10 runs retained, 8 produced between 72 % and 81 % of their input weight as liquid oil {L(FI)}, with a weighted average of 73.1 % {L("calc:CALC-A2-HUILE10-MOY-POND")}.')
o=line('- **Oil plus gas by difference.**')
o2=re.sub(r'On the 11 pure plastic runs, the gas by difference averaged 14\.41 % of the input, weighted by mass \(\[Annex.*?-->',f'On the 10 runs retained, the gas by difference averaged 16.3 % of the input, weighted by mass {L("calc:CALC-A2-GAZDIFF10-MOY-POND")}',o)
assert o2!=o; rep(o,o2)
o=line("- OneWorld's 2021 demonstration runs on mixed plastics")
rep(o,f"- OneWorld's 2021 demonstration runs on mixed plastics produced 83 % oil over three days (70 %, 88 % and 91 % per day) {L('calc:CALC-A2-OWJ-HUILE',OWJ)}; oil plus gas by difference, the weight reduction, reached 96 % {L(OWJ)}. The three days are not independent repetitions (Section 2.3.1).")
rep(line('- **Oil.** An independent laboratory measured'),f'- **Oil.** A third-party laboratory, the Japan Lubricating Oil Society, commissioned by Asada Shokai, reported a gross calorific value of 46,000 J/g (calculated) on oil from municipal packaging plastics, with a density of 0.8642 g/cm³ and a sulphur content below 0.05 % {L("CHIBA-JLOS-HUILES")}.')
rep(line('- **Char.** The char has a calorific value of 32,090 J/g'),f'- **Char.** Two values are used, by feed {L("hyp:D-038")}: 24.6 MJ/kg for char from plastic residues, the factor applied in the Chiba mass balances {L("calc:CALC-A2-PCI-CHAR-PLASTIQUE")}, and 32.09 MJ/kg for char from household waste, measured on a urethane char {L("IZUMITEC-R35-339439")}. Both are well above the 12,000 kJ/kg minimum for a French solid recovered fuel {L("ARRETE-CSR-2016")}.')
rep(line('- The gas alone provides 2.9 times this demand on a resin-rich feed'),f"- The gas alone provides 2.9 times this demand on OneWorld's resin-rich example, with 11.5 % gas {L('calc:CALC-A2-COUV-BRULEUR-RESINE')}, and 3.7 times on pure plastic with 15 % gas, a rounded value of the measured gas by difference {L('calc:CALC-A2-COUV-BRULEUR-PLASTIQUE15','hyp:D-038')}.")
o=line("- For a feed of 90 % resin-based waste, OneWorld design data state")
rep(o,o+" OneWorld's daily table counts 1 litre as 1 kg; Section 2.8 shows it corrected "+L("hyp:D-035")+".")
# --- How to read
rep('its documentation is marked "OneWorld design data" and has not been verified independently.','its documentation is marked "OneWorld design data" and has not been verified by a third party.')
o=line('Each argument is followed by a link to its evidence file and a confidence level')
rep(o,o+' The confidence percentage measures the confidence in the reading of each document, not the independence of the test <!-- [hyp:D-022] -->.')
rep('| 100 % | Tests filed with the authorities, independent laboratory reports, legislation, reference data |','| 100 % | Tests filed with the authorities, third-party laboratory reports, legislation, reference data |')
# --- 2.1
rep(line('The core evidence is a test programme run in 2022 at the Noda plant'),f'The core evidence is a test programme run by Asada Shokai (朝田商会) at its Noda plant, Chiba Prefecture, Japan (March to September 2022) and reported to the Governor of Chiba Prefecture {L(RAP)}. The plant was supplied and operated by OneWorld; measurements and analyses were made by Land Brain and third-party laboratories {L(RAP)}.')
rep(line('- **Machine.** An URBAN RIG batch unit manufactured and operated by OneWorld.'),f'- **Machine.** An URBAN RIG batch unit, described by the operator as a test unit {L("CHIBA-CONSTATS")}.')
o=line('| Chiba programme: oil, char, water, emissions, odour, noise |'); rep(o,o.replace('| Independent laboratories (Japan Lubricating Oil Society; Oosumi Co.) |','| Third-party laboratories: Japan Lubricating Oil Society, commissioned by Asada Shokai; Oosumi Co., commissioned by Land Brain |'))
o=line('| Off-gas composition, stack emissions, odour | 2020 |')
rep(o,'| Off-gas composition, stack emissions, odour | 2020 | Superheated steam carbonisation unit | Not stated | KANSO Technos, commissioned by OneWorld; odour measured by Total Kankyo System for KANSO | '+L('KANSO-B2002600','KANSO-20002610','TES-ODEUR-2020')+' |')
o=line('| Stack emissions, odour, dioxins | 2023 |'); rep(o,o.replace('| Tanabe; N.E. Support; Kankyo Kogai Bunseki Center (independent) |','| Third-party laboratories: Tanabe Kankyo Kogaku, N.E. Support, Kankyo Kogai Bunseki Center; client name masked |'))
o=line('| URC-2000 continuous plant specification |'); rep(o,o.replace('| 2019 to 2020 |','| 2019 (English brochure); Japanese brochure undated |'))
# --- 2.2.1
o=line('| 2022-05-26 | PE/PP/PS mix ("3P") offcuts |'); rep(o,o.replace('PE/PP/PS mix ("3P") offcuts','PE/PP/PS mix ("3P"), see note'))
o=line('| 2022-07-11 | PE/PP/PS mix ("3P") offcuts |'); rep(o,o.replace('PE/PP/PS mix ("3P") offcuts','PE/PP/PS mix ("3P"), see note; excluded from the averages'))
o=line('Source: ([Annex 2.1.a](annexe-02-preuves/A2-1-a-chiba-test-sheets.md#chiba-essais-fiches), 100 %)<!-- [CHIBA-ESSAIS-FICHES] -->, test sheets, PDF p. 19 to 24')
rep(o,o+f'\n\n**The two mixed-plastic runs.** Two runs on PE/PP/PS mixtures, described in the report as moulded-product offcuts (成型端材) {L(FI)}; according to Stéphane Husser, mixed plastic waste of unknown composition. The run of 2022-07-11 is shown but excluded from the averages {L("hyp:D-034")}: unconverted pieces are visible in the residue (photo, PDF p. 24), and it has the lowest gas (2.2 %) and the highest oil yield (82.3 %) of the 11 runs {L("calc:CALC-A2-OFFGAS-0711","calc:CALC-A2-RDT-HUILE-0711")}, a doubtful balance.')
# --- 2.2.2
o=line('| PE/PP/PS mix | 2 |'); rep(o,'| PE/PP/PS mix | 1 retained, 1 excluded | 72 % | 91.3 % |')
rep(line('- **PE and PP convert almost completely.**'),line('- **PE and PP convert almost completely.**').replace('- **PE and PP convert almost completely.** Little solid residue remains (Section 2.2.1).',f'- **PE and PP convert well.** Little solid residue remains on most runs, but the PP pallet run left 6.1 kg of residue from 50 kg {L(FI)}.'))
rep(line('- **The split between oil and gas varies from run to run.**'),f'- **The split between oil and gas varies from run to run.** On the 10 runs retained, the gas by difference ranges from 6.75 % {L("calc:CALC-A2-GAZDIFF10-MIN")} to 24.5 % {L("calc:CALC-A2-GAZDIFF-MAX")}.\n- **Batch tests and the continuous plant.** According to the project team, the internal tests carried out so far in continuous operation have shown higher yields than the batch tests. These data are not yet in this dossier. Tests on the same feed and the same basis of comparison remain to be done {L("hyp:D-036")}. The financial model starts from the batch yields.')
i=s.index('**Gas by difference on the pure plastic runs.**'); j=s.index('### 2.2.3',i)
s=s[:i]+f'''**Gas by difference on the pure plastic runs.** On the 10 runs retained {L(FI,"hyp:D-034")}:
- weighted mean 16.25 % of the input {L("calc:CALC-A2-GAZDIFF10-MOY-POND")}; simple mean 16.84 % {L("calc:CALC-A2-GAZDIFF10-MOY-SIMPLE")}; median 18.15 % {L("calc:CALC-A2-GAZDIFF10-MEDIANE")};
- range from 6.75 % {L("calc:CALC-A2-GAZDIFF10-MIN")} to 24.5 % {L("calc:CALC-A2-GAZDIFF-MAX")};
- by resin: PE 20.09 % {L("calc:CALC-A2-GAZDIFF-PE")}, PP 17.25 % {L("calc:CALC-A2-GAZDIFF-PP")}, PS 9.55 % {L("calc:CALC-A2-GAZDIFF-PS")}, PE/PP/PS mix 19.5 %, one run {L("calc:CALC-A2-OFFGAS-0526")};
- oil 73.07 % {L("calc:CALC-A2-HUILE10-MOY-POND")} and solid residue 10.65 % {L("calc:CALC-A2-RESIDU10-MOY-POND")}, weighted means.

Including the excluded run, the weighted mean of the gas on the 11 runs is 14.41 % {L("calc:CALC-A2-GAZDIFF-MOY-POND")}.

For a dry plastic, this balance is essentially gas. For pure plastic, the business plan takes the gas at 15 % of the input, a rounded value of the measured means {L("hyp:D-038")}. For mixed waste, it takes the gas produced by the plastic fraction at 10 % of the plastic input, a prudent value close to the lowest observations {L("hyp:D-029")}. The composition is taken from the analysed gas without air (Section 2.5.1); the uncertainty lies in the quantity, not the composition {L("hyp:D-029")}.

'''+s[j:]
# --- 2.2.3
rep(line('- After each run, the operator weighed separately the "metals and foreign matter"'),'- After each run, the operator weighed separately the "metals and foreign matter" (金属・異物) recovered from the reactor after treatment.')
rep(line('  - Packaging plastics: 10.5 kg of the 50 kg input'),f'  - Packaging plastics: 13.9 kg of the 50 kg input, i.e. 27.8 %, according to the mass balance (page 42) {L("calc:CALC-A2-NONPLAST-NODA-0909","hyp:D-033")}; the test sheet (page 26) gives 10.5 kg (see the box below).')
rep(line('**Yields on the convertible part of the feed.**'),f'**Yields excluding metals and foreign matter recovered after treatment.** Metals and foreign matter produce neither oil nor gas. The yield on the input minus that weight is the yield of the reactor feed after pre-sorting; the yield on the raw input gives the oil per tonne received. Both bases are shown {L("hyp:D-035")}.')
i=s.index('| | Packaging plastics, 2022-09-09 | Non-combustible residue, 2022-09-15 |'); j=s.index('**Reading for investors**',i)
old=s[i:j]
r=lambda pre: [l for l in old.split('\n') if l.startswith(pre)][0]
l1515h=links(r('| Oil yield excluding metals and foreign matter |'))[1]
l1515c=links(r('| Oil + gas by difference, excluding metals and foreign matter |'))[1]
lt=links(r('| Oil + gas by difference, on total input |'))
new=f'''| | Packaging plastics, 2022-09-09 | Non-combustible residue, 2022-09-15 |
|---|---|---|
| Input (kg) | 50 | 50 |
| Metals and foreign matter recovered after treatment (kg) | 13.9 (page 42) | 5.4 |
| Oil (kg) | 16.1 | 22.5 |
| Gas by difference (kg) | 9.5 | 10.8 |
| Char (kg) | 10.5 (page 42) | 11.3 |
| Process water in / discharged / evaporated (L) | 100 / 73 / 27 | 100 / 85 / 15 |
| Oil yield on raw input | 32.2 % {L("calc:CALC-A2-HUILE-NODA-0909-BRUT")} | 45.0 % {L("calc:CALC-A2-HUILE-NODA-0915-BRUT")} |
| Oil yield excluding metals and foreign matter recovered after treatment | 44.6 % {L("calc:CALC-A2-HUILE-NODA-0909-HORSMETAUX")} | 50.4 % {l1515h} |
| Gas by difference, excluding metals and foreign matter | 26.3 % {L("calc:CALC-A2-GAZ-NODA-0909-HORSMETAUX")} | 24 % (test sheet) {L(FI)} |
| Oil + gas by difference, excluding metals and foreign matter | 70.9 % {L("calc:CALC-A2-CONV-NODA-0909-HORSMETAUX")} | 74.7 % {l1515c} |
| Oil + gas by difference, on total input | 51.2 % {lt[0]} | 66.6 % {lt[1]} |

Source: {L(FI)}, test sheet PDF p. 26 (printed p. 20); {L(BIL)}, mass balance PDF p. 42 (printed p. 36) for the metals, char and water {L("hyp:D-033")}. The oil mass is the value printed by the operator; the oil was measured by dipstick in drums after settling, not weighed {L("CHIBA-PROCEDE-HUILE")}.

'''
s=s[:i]+new+s[j:]
o=line('- **Lower than clean plastics, as expected for a mixed and soiled stream.**')
rep(o,f'- **Lower than clean plastics, as expected for a mixed and soiled stream.** Oil plus gas by difference was 70.9 % and 74.7 % of the reactor feed after removal of metals and foreign matter {L("calc:CALC-A2-CONV-NODA-0909-HORSMETAUX")} {links(o)[0]}.')
rep(line('- **Char is a larger product.**'),f'- **Char is a larger product.** On these two runs, char represents 10.5 to 11.3 kg per 50 kg of input {L(BIL)}. Its value is discussed in Section 2.4.4 and Annex 3.')
o=line('- **Shredder residue is not a suitable feedstock.**')
rep(o,o.replace('Shredder residue is not among the business plan\'s feedstocks (decision D-017).',f'Shredder residue is excluded from the business plan, on the report\'s judgement (PDF p. 1 note ※3 and p. 43) {L(RAP,"hyp:D-037")}.'))
o=line('**One discrepancy to clarify.**')
rep(o,f'''**Inconsistencies in the source (pages 26 and 42).**
- Metals and char of the 2022-09-09 run: the test sheet (page 26) gives 10.5 kg of metals and foreign matter and 13.9 kg of char; the mass balance (page 42) gives 13.9 kg and 10.5 kg {L(FI,BIL)}. Page 42 is used, as a complete balance of inputs, products and energy {L("hyp:D-033")}. The 41 % oil yield printed on page 26 is calculated with 10.5 kg of metals {L(FI)}.
- Water: page 26 gives 52 L of drainage water for both runs; page 42 gives 100 L of water in, with 73 L discharged and 27 L evaporated on 2022-09-09, and 85 L and 15 L on 2022-09-15 {L(FI,BIL)}. Page 42 is used; the evaporated volumes are probably calculated by difference.''')
# --- 2.3.1
o=line('| Municipal packaging plastics (excluding metals and foreign matter) |')
rep(o,f'| Municipal packaging plastics (excluding metals and foreign matter recovered after treatment) | 44.6 % | 70.9 % | Calculated | {L("calc:CALC-A2-HUILE-NODA-0909-HORSMETAUX","calc:CALC-A2-CONV-NODA-0909-HORSMETAUX")} |')
o=line('| Municipal non-combustible residue (excluding metals and foreign matter) |'); rep(o,o.replace('(excluding metals and foreign matter)','(excluding metals and foreign matter recovered after treatment)'))
o=line('| Mixed plastics, mainly PP, PE and PS, URT-10 (3 runs, 299.2 kg) |')
rep(o,o.replace('| 83 % | 96 % weight reduction | Manufacturer |','| 83 % cumulated (70 %, 88 % and 91 % per day) | 96 % (weight reduction) | Manufacturer |'))
o=line('The 2021 URT-10 report also notes that oil from the second day')
rep(o,f'**Limits of the 2021 URT-10 runs.** The report notes a leak of off-gas at the catalytic layer on day 1 (p. 2) {L(OWJ)}. On days 2 and 3, the reactor was cooled without steam (p. 5 and 8) {L(OWJ)}. Oil from the second day probably included gas from the first day that condensed overnight, and glass fibre from FRP was found in the day 2 residue {L(OWJ)}. The three days are therefore not independent repetitions; only the cumulative 83 % is used.')
rep('**PET, PVC, polyamides, superabsorbent polymers: INCONNU** on Urban Rig equipment.','**PET, polyamides, superabsorbent polymers: INCONNU** on Urban Rig equipment. **PVC:** no quantified yield data; one observation only (below).')
# --- 2.4.1
rep('### 2.4.1 Independent Laboratory Analyses of the Oil','### 2.4.1 Third-Party Laboratory Analyses of the Oil')
rep('| Laboratory | Japan Lubricating Oil Society | Japan Lubricating Oil Society | NKKK (Japan Marine Survey Association), Osaka |','| Laboratory | Japan Lubricating Oil Society, commissioned by Asada Shokai | Japan Lubricating Oil Society, commissioned by Asada Shokai | NKKK (Japan Marine Survey Association), Osaka, commissioned by OneWorld |')
o=line('- **Energy content.** The oil from municipal packaging plastics reached 46,000 J/g'); rep(o,o.replace('A second independent laboratory measured','A second laboratory, Izumitec, measured'))
# --- 2.4.4
o=line('**Calorific value.** Izumitec Co. measured 32,090 J/g on a urethane char')
tail=o[o.index('According to OneWorld design data, the char from food waste'):] if 'According to OneWorld design data, the char from food waste' in o else ''
rep(o,f'''**Calorific value: two values, by feed** {L("hyp:D-038")}.
- **Char from plastic residues: 24.6 MJ/kg**, the factor applied to char in the Chiba mass balances (5,880 kcal/kg, PDF p. 41 and 42) {L("calc:CALC-A2-PCI-CHAR-PLASTIQUE")}. Its origin is not stated in the report (R-012). It also applies to the two Noda runs.
- **Char from household waste: 32.09 MJ/kg**, measured by Izumitec Co. on a urethane char with the JIS M 8814 calorimeter method {L("IZUMITEC-R35-339439")}. Working assumption of the sponsor: the organic matter, emptied of its water, acts at the end of pyrolysis as a sponge whose pores fill with heavy hydrocarbons {L("hyp:D-038")}. Ash and minerals, which lower the calorific value, remain to be measured (R-012).

{tail}''')
o=line('**Why char matters for municipal waste.**')
rep(o,f'**Why char matters for municipal waste.** On the two municipal runs, char was 10.5 to 11.3 kg per 50 kg of input {L(BIL)}. In a feed containing paper, wood or food waste, the organic fraction becomes char. At 24.6 MJ/kg, the char from one tonne of plastic packaging fed to the reactor (Noda run, page 42) carries 7,160 MJ {L("calc:CALC-A2-NRJ-CHAR-NODA")}, about a third of the energy in the oil from the same tonne, 20,515 MJ {L("calc:CALC-A2-NRJ-HUILE-NODA")}.')
o=line('| Calorific value | 32,090 J/g | 32,090 J/g |')
rep(o,f'| Calorific value | 24.6 MJ/kg (plastic residues) | 24.6 MJ/kg (plastic residues) | not applicable | at least 12,000 kJ/kg |')
o=line('Source: char analyses'); rep(o,re.sub(r'calorific value \(\[Annex.*?-->',f'calorific value {L("calc:CALC-A2-PCI-CHAR-PLASTIQUE")}',o))
# --- 2.5.1
o=line('**Reading.** The off-gas is sampled at the outlet, where it mixes with air.')
rep(o,o+f' The sample was taken at the pipe outlet, without a stated protocol, and diluted by the air of the sampling; oxygen and nitrogen are excluded, and this dilution does not change the energy per tonne of the gas produced by the feed {L("hyp:D-038")}. The Chiba mass balances apply a factor of 1,323.8 kcal/kg, i.e. 5.5 MJ/kg, to the off-gas {L("calc:CALC-A2-FACTEUR-OFFGAS","calc:CALC-A2-PCI-GAZ-CHIBA")}; its origin is unknown and it is not used here (R-011).')
# --- 2.6
o=line('The energy balance is built on OneWorld\'s figures for the continuous URC-2000')
rep(o,o+f' The financial model starts from the batch yields, without a bonus for continuous operation {L("hyp:D-036")}.')
o=line('| Resin-rich waste (OneWorld design) | 4,299')
rep(o,o.replace('| Resin-rich waste (OneWorld design) |','| Resin-rich waste (OneWorld design, 11.5 % gas) |')+f'\n| Pure plastic, 15 % gas (working assumption) | 5,608 {L("calc:CALC-A2-NRJ-GAZ-PLASTIQUE15")} | 3.7 times {L("calc:CALC-A2-COUV-BRULEUR-PLASTIQUE15")} | not calculated |')
o=line('All values calculated with the assumptions of decision D-021'); rep(o,f'All values calculated with the assumptions of decisions D-021 and D-038 {L("hyp:D-021","hyp:D-038")}.')
o=line('- **Resin-rich feeds.**'); rep(o,o.replace("2.9 times on OneWorld's resin-rich design.","2.9 times on OneWorld's resin-rich design (11.5 % gas) and 3.7 times with 15 % gas."))
o=line('| Resin-rich waste (OneWorld design) | 35,190 MJ'); rep(o,o.replace('| 1,605 MJ','| 1,231 MJ'))
o=line('All values calculated with oil at 46,000 J/g, gas at 37.4 MJ/kg and char at 32,090 J/g')
rep(o,f'All values calculated with oil at 46,000 J/g, gas at 37.4 MJ/kg and char from plastic residues at 24.6 MJ/kg {L("hyp:D-021","hyp:D-038")}.')
# --- 2.8
o=line('| Throughput | 200 t per day |')
rep(o,o+f'\n| Reactor capacity used in the business plan | 200 m³ per day; 140 t per day at 0.7 t/m³ after sorting and pressing (working assumption) | {L("hyp:D-035")} |')
o=line("**Consistency with the tests.** OneWorld's 76.5 % oil")
o2=o.replace("sits within the 72 % to 82 % measured on PE, PP and mixed plastic batches","is close to the 72 % to 81 % measured on 8 of the 10 batch runs retained, and to their weighted average of 73.1 %")
o2=o2.replace(links(o)[0],L(FI,'calc:CALC-A2-HUILE10-MOY-POND'),1)
o2+=f' According to the project team, internal tests in continuous operation have shown higher yields; these data are not yet in this dossier {L("hyp:D-036")}.'
P05='UR2000-JP-P05-BILAN'
tab=f'''

**OneWorld's daily table (English brochure p. 16), as printed.** Input "200Mt", specific gravity 0.6, 90 % resins {L(P16)}:

| Product | Share | Quantity as printed |
|---|---|---|
| Gas (diesel) oil | 61.2 % | 62,424 L (62.424 t) |
| Heating oil | 7.65 % | 7,803 L (7.803 t) |
| Heavy oil | 7.65 % | 7,803 L (7.803 t) |
| Recovery loss | 11.5 % | 11,730 L (11.73 t) |
| Carbide (char) | 5 % | 5.1 m³ (5.1 t) |
| Water | 5 % | 5,100 L (5.1 t) |
| Metals and glass | 2 % | 2.04 m³ (2.04 t) |

Source: {L(P16)}. The shares add up to 100 %, but the printed quantities add up to 102 t for an input of 200 t and count 1 litre as 1 kg {L("calc:CALC-A2-OW16-SOMME-MASSES",P16)}.

**Corrected version (calculated).** OneWorld's shares applied to 200 m³ per day at OneWorld's specific gravity of 0.6, i.e. 120 t per day {L("calc:CALC-A2-OW16C-ENTREE","hyp:D-035")}; oil volumes at 0.8642 kg/L {L("CHIBA-JLOS-HUILES")}:

| Product | Share | t per day | L per day |
|---|---|---|---|
| Gas (diesel) oil | 61.2 % | 73.44 {L("calc:CALC-A2-OW16C-GAZOLE-T")} | 84,980 {L("calc:CALC-A2-OW16C-GAZOLE-L")} |
| Heating oil | 7.65 % | 9.18 {L("calc:CALC-A2-OW16C-HEATING-T")} | 10,623 {L("calc:CALC-A2-OW16C-HEATING-L")} |
| Heavy oil | 7.65 % | 9.18 {L("calc:CALC-A2-OW16C-HEAVY-T")} | 10,623 {L("calc:CALC-A2-OW16C-HEAVY-L")} |
| Total oil | 76.5 % | 91.8 {L("calc:CALC-A2-OW16C-HUILE-T")} | 106,225 {L("calc:CALC-A2-OW16C-HUILE-L")} |
| Recovery loss | 11.5 % | 13.8 {L("calc:CALC-A2-OW16C-PERTE-T")} | |
| Carbide (char) | 5 % | 6.0 {L("calc:CALC-A2-OW16C-CHAR-T")} | |
| Water | 5 % | 6.0 {L("calc:CALC-A2-OW16C-EAU-T")} | |
| Metals and glass | 2 % | 2.4 {L("calc:CALC-A2-OW16C-METAUX-T")} | |
| Total | 100 % | 120 {L("calc:CALC-A2-OW16C-SOMME")} | |

Notes on the correction:
- The 76.5 % oil remains a statement by OneWorld on a feed with 90 % resins {L(P16)}.
- The brochure writes "200Mt". Reading it as 200 m³ per day follows the Japanese brochure ("200ton ▶ 200m3") {L(P05)} and the bucket schedule {L("UR2000-JP-P08-SPEC")}.
- The density of 0.8642 kg/L is that of the oil from Noda packaging plastics {L("CHIBA-JLOS-HUILES")}; no density is given for each OneWorld fraction.
- The business plan uses 0.7 t/m³ (140 t per day), a working assumption of the sponsor: a press brings the sorted feed back to 0.7 t/m³ {L("hyp:D-035")}.'''
rep(o,o2+tab)
# --- 2.9
o=line('| Oil yield, municipal plastics, excluding metals |')
rep(o,f'| Oil yield, municipal plastics, excluding metals and foreign matter recovered after treatment | 44.6 % and 50.4 % {L("calc:CALC-A2-HUILE-NODA-0909-HORSMETAUX","calc:CALC-A2-HUILE-NODA-0915-HORSMETAUX")}; 32.2 % and 45.0 % on raw input {L("calc:CALC-A2-HUILE-NODA-0909-BRUT","calc:CALC-A2-HUILE-NODA-0915-BRUT")} | Calculated | Tests on the French target mix (R-021) |')
o=line('| Oil + gas by difference, PE and PP |')
rep(o,o+f'\n| Gas by difference, pure plastics | 16.25 %, weighted mean of 10 runs {L("calc:CALC-A2-GAZDIFF10-MOY-POND")} | Calculated (gas not measured) | Gas measured separately (R-011) |\n| Reactor throughput | 200 m³ per day; 140 t per day at 0.7 t/m³ | Assumption {L("hyp:D-035")} | Volume per day and density by feed (R-010) |')
o=line('| Char calorific value |')
rep(o,f'| Char calorific value | 24.6 MJ/kg for plastic residues {L("calc:CALC-A2-PCI-CHAR-PLASTIQUE")}; 32.09 MJ/kg for household waste {L("IZUMITEC-R35-339439")} | Factor of unknown origin; assumption {L("hyp:D-038")} | Measurement on char from the target feed (R-012) |')
o=line('| Energy self-sufficiency, resin-rich feed |')
rep(o,f"| Energy self-sufficiency, pure plastic | gas covers the burner demand 2.9 times (OneWorld, 11.5 % gas) {L('calc:CALC-A2-COUV-BRULEUR-RESINE')} and 3.7 times (15 % gas) {L('calc:CALC-A2-COUV-BRULEUR-PLASTIQUE15')} | Calculated | Consumption guarantee (R-015, R-019); household waste in Annex 5 |")
o=line("   - the brochure's output table sums to 102.0 t for 200 t of input")
rep(o,o.replace(' for 200 t of input',' for 200 t of input, counting 1 L as 1 kg (corrected in Section 2.8)'))
assert 'ndependent' not in s.replace('independent repetitions','').replace('not independent',''), [m.start() for m in re.finditer('ndependent',s)]
if '--dry' in sys.argv: print('dry ok'); sys.exit()
open(p,'w',encoding='utf-8').write(s); print('ecrit')
