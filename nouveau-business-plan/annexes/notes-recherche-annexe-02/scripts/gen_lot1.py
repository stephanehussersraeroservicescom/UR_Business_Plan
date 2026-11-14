p='nouveau-business-plan/annexes/annexe-02-html/generer_html.py'; s=open(p,encoding='utf-8').read()
s=s.replace("'Independent laboratory (Japan Lubricating Oil Society)'","'Third-party laboratory (Japan Lubricating Oil Society), commissioned by Asada Shokai'")
s=s.replace("'Independent laboratory (Oosumi Co.)'","'Third-party laboratory (Oosumi Co.), commissioned by Land Brain'")
s=s.replace("'Independent laboratory (Oosumi Co.); reports marked provisional'","'Third-party laboratory (Oosumi Co.), commissioned by Land Brain; reports marked provisional'")
s=s.replace("'Independent laboratory (NKKK, Osaka), report reproduced in a OneWorld brochure'","'Third-party laboratory (NKKK, Osaka), commissioned by OneWorld; report reproduced in a OneWorld brochure'")
s=s.replace("Independent laboratories","Third-party laboratories").replace("Independent laboratory","Third-party laboratory")
s=s.replace("('2.2','Third-party laboratory reports')","('2.2','Third-party laboratory reports')")
s=s.replace("Tests filed with the authorities, independent laboratory reports, legislation and reference data</td></tr>","Tests filed with the authorities, third-party laboratory reports, legislation and reference data</td></tr>")
s=s.replace("<p class=\"small\">A calculation is never rated above its least reliable input, nor above 95 %.</p>","<p class=\"small\">A calculation is never rated above its least reliable input, nor above 95 %. The percentage measures the confidence in the reading of each document, not the independence of the test.</p>")
assert 'ndependent' not in s.replace('independence of the test',''), [s[m-40:m+40] for m in [s.find('ndependent')]]
s=s.replace("    if re.search(r'GAZDIFF',cid): return 'A2.5.a'","    if re.search(r'GAZDIFF',cid): return 'A2.5.a'\n    if re.search(r'PCI-CHAR|PCI-GAZ-CHIBA|OW16C|HUILE10|RESIDU10|NODA-0909-BRUT|NODA-0915-BRUT|BASE-NODA|CHAR-NODA-0909|GAZ-NODA-0909',cid): return 'A2.5.b' if 'NODA' in cid else 'A2.5.f'")
add="NEW_DESC={\n"+"\n".join(f"'{k}':'{v}'," for k,v in [
('CALC-A2-GAZDIFF10-MOY-POND','Gas by difference, weighted mean of the 10 pure plastic runs retained (run of 2022-07-11 excluded, decision D-034).'),
('CALC-A2-GAZDIFF10-MOY-SIMPLE','Gas by difference, simple mean of the 10 pure plastic runs retained.'),
('CALC-A2-GAZDIFF10-MEDIANE','Gas by difference, median of the 10 runs retained: mean of the 5th and 6th values (PE containers 16.8 % and mix of 2022-05-26 19.5 %).'),
('CALC-A2-GAZDIFF10-MIN','Gas by difference, lowest value of the 10 runs retained (PS moulding offcuts, 2022-03-31).'),
('CALC-A2-HUILE10-MOY-POND','Oil, weighted mean of the 10 pure plastic runs retained.'),
('CALC-A2-RESIDU10-MOY-POND','Solid residue removed, weighted mean of the 10 pure plastic runs retained.'),
('CALC-A2-BASE-NODA-0909','Input minus metals and foreign matter, municipal packaging plastics, 2022-09-09 (page 42).'),
('CALC-A2-GAZ-NODA-0909-HORSMETAUX','Gas by difference on input minus metals and foreign matter, municipal packaging plastics, 2022-09-09 (page 42).'),
('CALC-A2-CHAR-NODA-0909','Char as a share of input, municipal packaging plastics, 2022-09-09 (page 42).'),
('CALC-A2-HUILE-NODA-0909-BRUT','Oil on raw input, municipal packaging plastics, 2022-09-09.'),
('CALC-A2-HUILE-NODA-0915-BRUT','Oil on raw input, municipal non-combustible residue, 2022-09-15.'),
('CALC-A2-PCI-CHAR-PLASTIQUE','Calorific value of char from plastic residues: factor of the Chiba mass balances (5,880 kcal/kg, origin not stated) converted to MJ/kg.'),
('CALC-A2-PCI-GAZ-CHIBA','Factor applied to the off-gas in the Chiba mass balances (1,323.8 kcal/kg, origin not stated) converted to MJ/kg; not used in the annex.'),
('CALC-A2-NRJ-GAZ-PLASTIQUE15','Energy in the gas per tonne of pure plastic, with gas at 15 % of the input (working assumption D-038).'),
('CALC-A2-COUV-BRULEUR-PLASTIQUE15','Energy in the gas divided by the burner heat demand, pure plastic with gas at 15 % (working assumption D-038).'),
('CALC-A2-OW16C-ENTREE','Corrected OneWorld table (English brochure p. 16): input mass = 200 m3 per day x specific gravity 0.6.'),
('CALC-A2-OW16C-GAZOLE-T','Corrected OneWorld table: gas (diesel) oil, t per day.'),('CALC-A2-OW16C-HEATING-T','Corrected OneWorld table: heating oil, t per day.'),('CALC-A2-OW16C-HEAVY-T','Corrected OneWorld table: heavy oil, t per day.'),
('CALC-A2-OW16C-PERTE-T','Corrected OneWorld table: recovery loss, t per day.'),('CALC-A2-OW16C-CHAR-T','Corrected OneWorld table: carbide (char), t per day.'),('CALC-A2-OW16C-EAU-T','Corrected OneWorld table: water, t per day.'),
('CALC-A2-OW16C-METAUX-T','Corrected OneWorld table: metals and glass, t per day.'),('CALC-A2-OW16C-HUILE-T','Corrected OneWorld table: total oil, t per day.'),
('CALC-A2-OW16C-GAZOLE-L','Corrected OneWorld table: gas (diesel) oil at 0.8642 kg/L, L per day.'),('CALC-A2-OW16C-HEATING-L','Corrected OneWorld table: heating oil at 0.8642 kg/L, L per day.'),('CALC-A2-OW16C-HEAVY-L','Corrected OneWorld table: heavy oil at 0.8642 kg/L, L per day.'),
('CALC-A2-OW16C-HUILE-L','Corrected OneWorld table: total oil at 0.8642 kg/L, L per day.'),('CALC-A2-OW16C-SOMME','Corrected OneWorld table: sum of the products (closure check).')])
assert s.count("NEW_DESC={")==1
s=s.replace("NEW_DESC={",add,1)
open(p,'w',encoding='utf-8').write(s); print('ok')
