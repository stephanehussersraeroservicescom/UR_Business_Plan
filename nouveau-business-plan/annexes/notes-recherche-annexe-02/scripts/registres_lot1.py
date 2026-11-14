import yaml,re
# _evidence
p='working-folder/params/_evidence.yaml'; s=open(p,encoding='utf-8').read()
o='  titre: Rapport Chiba, fiches d\'essai de pyrolyse (13 essais) et definitions'
if o not in s:
    o2=[l for l in s.split('\n') if l.startswith('  titre:') and "fiches d'essai de pyrolyse (13 essais)" in l]; assert len(o2)==1,o2; o=o2[0]
s=s.replace(o,o.replace('(13 essais)','(15 essais, dont 13 avec huile mesuree)'),1)
i=s.index('\nKANSO-20002610:\n'); j=s.index('\n',s.index('  contenu:',i))
line=s[s.index('  contenu:',i):j]; assert 'VLE usuelles' in line, line
s=s[:s.index('  contenu:',i)]+'  contenu: "HCl < 1 ppm, SOx < 1 ppm, NOx 15 ppm, poussieres < 0,002 g/m3, O2 18,5 % (p. 2). Aucune comparaison aux valeurs limites dans le document (E-9, D-037)."'+s[j:]
a='\nOWJ-DEMO-2021:\n'; assert s.count(a)==1
s=s.replace(a,a+'  citation_p2: "残りの25%がオフガスもしくは水分と考えられる。触媒層からオフガスの漏れがあったため、改良する必要あり。"\n  citation_p5: "尚、今回冷却は蒸気を出さずに行った。 ; 中にはFRP素材と見られるガラス繊維も混在されていた。"\n  citation_p8: "3日目も2日目同様に冷却は蒸気を出さずに行った。 ; 油重量 248.2kg 油化率 83% オフガス他 13%"\n',1)
a='\nCHIBA-BILANS:\n'; assert s.count(a)==1
s=s.replace(a,a+'  valeurs_lues_facteurs: "Facteurs implicites (energie / masse) : off-gas 15 489 kcal / 11,7 kg = 1 323,8 kcal/kg ; char 30 576 kcal / 5,2 kg = 5 880 kcal/kg (p. 41). Origine non indiquee dans le rapport (R-011, R-012)."\n',1)
yaml.safe_load(s); open(p,'w',encoding='utf-8').write(s)
# a-rechercher
q='working-folder/controle-sources/a-rechercher.yaml'; t=open(q,encoding='utf-8').read()
add={'R-010':"15/10/2026 (D-035) : le tableau p. 16 compte une densite de 1 (1 L = 1 kg), erreur deja signalee par Stephane, tableaux non refaits par OneWorld ; corrige par nous dans l'annexe 2, section 2.8 (CALC-A2-OW16C-*). Reste a confirmer : volume journalier 200, 216 (48 bennes) ou 229,5 m3 (51 bennes) et densite par gisement.",
     'R-012':"15/10/2026 (D-038) : char de dechets menagers pris a 32,09 MJ/kg (Izumitec, char d'urethane, HYPOTHESE de Stephane) ; demander une mesure de PCI, cendres et chlore sur char de dechets menagers. Char de residus plastiques : 24,6 MJ/kg, facteur de Chiba d'origine inconnue.",
     'R-018':"15/10/2026 (D-033) : point 407 L (p. 43) / 451 L (fiches) explique (44 L des essais de Noda) et retire. Masse d'huile : jaugee (p. 29), valeur imprimee conservee. 250 / 310 kg : non bloquant."}
for k,v in add.items():
    a=f'\n{k}:\n'; assert t.count(a)==1,k
    t=t.replace(a,a+f'  complement_2026_10_15_lot1: "{v}"\n',1)
o="ecarts 250 kg declares / 310 kg sur fiches et 407 L declares / 451 L sur fiches"
if o in t: t=t.replace(o,"ecarts 250 kg declares / 310 kg sur fiches")
yaml.safe_load(t); open(q,'w',encoding='utf-8').write(t)
# arbitrages
r='working-folder/params/_arbitrages.yaml'; u=open(r,encoding='utf-8').read()
for k in ['capacite_volumetrique_annexe01','densite_dechet_annexe01']:
    a=f'\n{k}:\n'; assert u.count(a)==1,k
    u=u.replace(a,a+'  statut: "CLOS le 15/10/2026 par D-035 : capacite du reacteur 200 m3/jour ; masse = volume x 0,7 t/m3 = 140 t/jour (HYPOTHESE de Stephane : une presse remet la charge triee a 0,7) ; variable dans le modele ; LUFTHANSA-WS non utilisee (D-025). Valeurs de params/ a aligner lors de la brique du modele."\n',1)
yaml.safe_load(u); open(r,'w',encoding='utf-8').write(u); print('ok')
