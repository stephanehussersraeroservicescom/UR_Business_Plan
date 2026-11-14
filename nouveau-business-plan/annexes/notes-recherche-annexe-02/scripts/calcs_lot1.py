import yaml,re,math,sys
p='working-folder/controle-sources/calculs.yaml'
txt=open(p,encoding='utf-8').read()
C=yaml.safe_load(txt)
def val(cid):
    f=C[cid]; env={}
    for n,e in f['entrees'].items():
        env[n]=val(e['calc']) if 'calc' in e else e['valeur']
    return eval(f['formule'],{'__builtins__':{}},env)
B=lambda v,u,src,emp:{'valeur':v,'unite':u,'source':src,'emplacement':emp}
P42=lambda v,u='kg':B(v,u,'CHIBA-BILANS','PDF p. 42, essai du 09/09/2022')
mods={}; new={}
mods['CALC-A2-HUILE-NODA-0909-HORSMETAUX']={'description':"Huile hors metaux et corps etrangers, plastiques d'emballage de Noda 2022-09-09, metaux selon la page 42 (decision E-3)",'formule':'huile / (entree - metaux)','entrees':{'entree':P42(50),'huile':P42(16.1),'metaux':P42(13.9)},'unite':'fraction'}
mods['CALC-A2-CONV-NODA-0909-HORSMETAUX']={'description':"Huile + gaz par difference hors metaux et corps etrangers, plastiques d'emballage de Noda 2022-09-09, metaux selon la page 42 (decision E-3)",'formule':'(huile + gaz) / (entree - metaux)','entrees':{'entree':P42(50),'gaz':P42(9.5),'huile':P42(16.1),'metaux':P42(13.9)},'unite':'fraction'}
mods['CALC-A2-NONPLAST-NODA-0909']={'description':"Part de metaux et corps etrangers dans la charge, plastiques d'emballage de Noda 2022-09-09, selon la page 42 (decision E-3)",'formule':'metaux / entree','entrees':{'entree':P42(50),'metaux':P42(13.9)},'unite':'fraction'}
new['CALC-A2-BASE-NODA-0909']={'description':"Base hors metaux et corps etrangers, plastiques d'emballage de Noda 2022-09-09, page 42",'formule':'entree - metaux','entrees':{'entree':P42(50),'metaux':P42(13.9)},'unite':'kg'}
new['CALC-A2-GAZ-NODA-0909-HORSMETAUX']={'description':"Gaz par difference hors metaux et corps etrangers, plastiques d'emballage de Noda 2022-09-09, page 42",'formule':'gaz / (entree - metaux)','entrees':{'entree':P42(50),'gaz':P42(9.5),'metaux':P42(13.9)},'unite':'fraction'}
new['CALC-A2-CHAR-NODA-0909']={'description':"Part de char dans la charge, plastiques d'emballage de Noda 2022-09-09, page 42",'formule':'char / entree','entrees':{'char':P42(10.5),'entree':P42(50)},'unite':'fraction'}
new['CALC-A2-PCI-CHAR-PLASTIQUE']={'description':"Pouvoir calorifique du char de residus plastiques : facteur des bilans de Chiba (5 880 kcal/kg, origine inconnue) converti en MJ/kg (decision E-10)",'formule':'facteur * kcal / 1000','entrees':{'facteur':{'calc':'CALC-A2-FACTEUR-CHAR'},'kcal':B(4.1868,'kJ/kcal','NIST-SP811-B9','Appendix B.9, calorie IT')},'unite':'MJ/kg'}
new['CALC-A2-PCI-GAZ-CHIBA']={'description':"Facteur applique a l'off-gas dans les bilans de Chiba (1 323,8 kcal/kg, origine inconnue) converti en MJ/kg ; non utilise dans l'annexe",'formule':'facteur * kcal / 1000','entrees':{'facteur':{'calc':'CALC-A2-FACTEUR-OFFGAS'},'kcal':B(4.1868,'kJ/kcal','NIST-SP811-B9','Appendix B.9, calorie IT')},'unite':'MJ/kg'}
mods['CALC-A2-NRJ-HUILE-NODA']={'description':"Energie de l'huile par tonne de matiere convertible, plastiques d'emballage de Noda 2022-09-09, page 42",'formule':'huile / (entree - metaux) * 1000 * pcs','entrees':{'entree':P42(50),'huile':P42(16.1),'metaux':P42(13.9),'pcs':B(46,'MJ/kg','CHIBA-JLOS-HUILES','PDF p. 45')},'unite':'MJ/t'}
mods['CALC-A2-NRJ-GAZ-NODA']={'description':"Energie du gaz par difference par tonne de matiere convertible, plastiques d'emballage de Noda 2022-09-09, page 42 (humidite comprise)",'formule':'gaz / (entree - metaux) * 1000 * pci','entrees':{'entree':P42(50),'gaz':P42(9.5),'metaux':P42(13.9),'pci':{'calc':'CALC-A2-GAZ-PCI'}},'unite':'MJ/t'}
mods['CALC-A2-NRJ-CHAR-NODA']={'description':"Energie du char par tonne de matiere convertible, plastiques d'emballage de Noda 2022-09-09, page 42, char de residus plastiques a 24,6 MJ/kg (decision E-10)",'formule':'char / (entree - metaux) * 1000 * pci','entrees':{'char':P42(10.5),'entree':P42(50),'metaux':P42(13.9),'pci':{'calc':'CALC-A2-PCI-CHAR-PLASTIQUE'}},'unite':'MJ/t'}
mods['CALC-A2-NRJ-CHAR-RESINE']={'description':"Energie du char par tonne de charge, charge riche en resines (bilan OneWorld, brochure p. 16), char de residus plastiques a 24,6 MJ/kg (decision E-10)",'formule':'part * 1000 * pci','entrees':{'part':B(0.05,'fraction','OW-ENG-P16-BILAN','p. 16'),'pci':{'calc':'CALC-A2-PCI-CHAR-PLASTIQUE'}},'unite':'MJ/t'}
new['CALC-A2-NRJ-GAZ-PLASTIQUE15']={'description':"Energie du gaz par tonne de plastique pur, gaz pris a 15 % de la masse entrante (hypothese de Stephane du 15/10/2026, arrondi des moyennes mesurees par difference)",'formule':'0.15 * 1000 * pci','entrees':{'pci':{'calc':'CALC-A2-GAZ-PCI'}},'unite':'MJ/t'}
new['CALC-A2-COUV-BRULEUR-PLASTIQUE15']={'description':"Energie du gaz rapportee au besoin du bruleur, plastique pur avec gaz a 15 % (hypothese de Stephane)",'formule':'gaz / besoin','entrees':{'besoin':{'calc':'CALC-A2-BRULEUR-MJ-T'},'gaz':{'calc':'CALC-A2-NRJ-GAZ-PLASTIQUE15'}},'unite':'rapport'}
R=[('PE-GRAN','PE granules 2022-03-02',4.9,14.8,0.3,20,19),('PE-CHUTES','PE chutes 2022-03-09',8.8,30.7,0.5,40,19),('PE-BIDONS','PE bidons 2022-06-21',8.4,40.7,0.8,50,22),
   ('PP-GRAN','PP granules 2022-04-08',3.3,16.2,0.5,20,21),('PP-CHUTES','PP chutes 2022-04-16',10.0,39.8,0.2,50,21),('PP-PALETTES','PP palettes 2022-06-28',7.4,36.5,6.1,50,23),
   ('3P-0526','3P 2022-05-26',11.7,43.1,5.2,60,22),('PS-EXPANSE','PS expanse 2022-07-07',3.8,36.3,9.9,50,23),('PS-GRAN','PS granules 2022-03-17',4.0,12.2,3.8,20,20),('PS-CHUTES','PS chutes 2022-03-31',2.7,22.0,15.3,40,20)]
F=lambda v,run,p: B(v,'kg','CHIBA-ESSAIS-FICHES',f'PDF p. {p}, {run}')
def pond(cid,descr,idx,pre):
    e={}
    for row in R:
        k,run,i,p=row[0],row[1],row[5],row[6]; n=k.replace('-','_').lower()
        e[f'{pre}_{n}']=F(row[idx],run,p); e['e_'+n]=F(i,run,p)
    num=' + '.join(x for x in e if not x.startswith('e_')); den=' + '.join(x for x in e if x.startswith('e_'))
    new[cid]={'description':descr,'formule':f'({num}) / ({den}) * 100','entrees':e,'unite':'%'}
pond('CALC-A2-GAZDIFF10-MOY-POND',"Gaz par difference, moyenne ponderee des 10 essais de plastiques purs retenus (essai 3P du 11/07 ecarte, decision E-4)",2,'g')
pond('CALC-A2-HUILE10-MOY-POND',"Huile, moyenne ponderee des 10 essais de plastiques purs retenus (essai 3P du 11/07 ecarte, decision E-4)",3,'h')
pond('CALC-A2-RESIDU10-MOY-POND',"Residu solide retire, moyenne ponderee des 10 essais de plastiques purs retenus (decision E-4)",4,'r')
e={}
for row in R:
    n=row[0].replace('-','_').lower(); e['g_'+n]=F(row[2],row[1],row[6]); e['e_'+n]=F(row[5],row[1],row[6])
terms=' + '.join(f'g_{r[0].replace("-","_").lower()} / e_{r[0].replace("-","_").lower()}' for r in R)
new['CALC-A2-GAZDIFF10-MOY-SIMPLE']={'description':"Gaz par difference, moyenne simple des 10 essais de plastiques purs retenus (decision E-4)",'formule':f'({terms}) / 10 * 100','entrees':e,'unite':'%'}
new['CALC-A2-GAZDIFF10-MEDIANE']={'description':"Gaz par difference, mediane des 10 essais retenus : moyenne des 5e et 6e valeurs classees (PE bidons 16,8 % et 3P du 26/05 19,5 %)",'formule':'(g_pe_bidons / e_pe_bidons + g_3p_0526 / e_3p_0526) / 2 * 100','entrees':{'g_pe_bidons':F(8.4,'PE bidons 2022-06-21',22),'e_pe_bidons':F(50,'PE bidons 2022-06-21',22),'g_3p_0526':F(11.7,'3P 2022-05-26',22),'e_3p_0526':F(60,'3P 2022-05-26',22)},'unite':'%'}
new['CALC-A2-GAZDIFF10-MIN']={'description':"Gaz par difference, valeur la plus basse des 10 essais retenus (PS chutes 2022-03-31)",'formule':'g / e * 100','entrees':{'g':F(2.7,'PS chutes 2022-03-31',20),'e':F(40,'PS chutes 2022-03-31',20)},'unite':'%'}
OW=lambda v,u: B(v,u,'OW-ENG-P16-BILAN','p. 16')
new['CALC-A2-OW16C-ENTREE']={'description':"Tableau OneWorld p. 16 corrige : masse entrante = 200 (lu comme m3 par jour, decision E-2/E-6) x densite 0,6 de la brochure",'formule':'volume * densite','entrees':{'volume':OW(200,'m3/jour'),'densite':OW(0.6,'t/m3')},'unite':'t/jour'}
for code,lab,pct in [('GAZOLE','gas (diesel) oil',61.2),('HEATING','heating oil',7.65),('HEAVY','heavy oil',7.65),('PERTE','recovery loss',11.5),('CHAR','carbide (char)',5),('EAU','water',5),('METAUX','metals and glass',2)]:
    new[f'CALC-A2-OW16C-{code}-T']={'description':f"Tableau OneWorld p. 16 corrige : {lab}, t/jour",'formule':'part / 100 * entree','entrees':{'part':OW(pct,'%'),'entree':{'calc':'CALC-A2-OW16C-ENTREE'}},'unite':'t/jour'}
new['CALC-A2-OW16C-HUILE-T']={'description':"Tableau OneWorld p. 16 corrige : huile totale (gazole, heating oil, heavy oil), t/jour",'formule':'(p1 + p2 + p3) / 100 * entree','entrees':{'p1':OW(61.2,'%'),'p2':OW(7.65,'%'),'p3':OW(7.65,'%'),'entree':{'calc':'CALC-A2-OW16C-ENTREE'}},'unite':'t/jour'}
D8642=B(0.8642,'kg/L','CHIBA-JLOS-HUILES','PDF p. 45')
for code in ['GAZOLE','HEATING','HEAVY','HUILE']:
    new[f'CALC-A2-OW16C-{code}-L']={'description':f"Tableau OneWorld p. 16 corrige : volume ({code.lower()}) a 0,8642 kg/L (densite de l'huile d'emballages de Noda, JLOS), L/jour",'formule':'masse * 1000 / densite','entrees':{'masse':{'calc':f'CALC-A2-OW16C-{code}-T'},'densite':D8642},'unite':'L/jour'}
new['CALC-A2-OW16C-SOMME']={'description':"Tableau OneWorld p. 16 corrige : somme des produits (controle de fermeture du bilan)",'formule':'a + b + c + d + e + f + g','entrees':{k:{'calc':f'CALC-A2-OW16C-{c}-T'} for k,c in zip('abcdefg',['GAZOLE','HEATING','HEAVY','PERTE','CHAR','EAU','METAUX'])},'unite':'t/jour'}
assert not any(k in C for k in new), [k for k in new if k in C]
C.update(mods); C.update(new)
for k in list(mods)+list(new):
    C[k]['resultat']=round(val(k),4 if C[k]['unite'] in ('fraction','rapport') else 2)
    print(k,C[k]['resultat'])
if '--dry' in sys.argv: sys.exit()
for k,v in mods.items():
    blk=yaml.safe_dump({k:v},allow_unicode=True,sort_keys=False,width=4000)
    pat=re.compile(r'^'+re.escape(k)+r':\n(?:[ \t].*\n)*',re.M)
    assert len(pat.findall(txt))==1,k
    txt=pat.sub(lambda m: blk,txt)
txt=txt.rstrip('\n')+'\n\n# === ANNEXE 2 : application du lot 1 de Codex (E-3, E-4, E-6, E-10), 15/10/2026 ===\n\n'+yaml.safe_dump(new,allow_unicode=True,sort_keys=False,width=4000)
yaml.safe_load(txt)
open(p,'w',encoding='utf-8').write(txt); print('ecrit')
