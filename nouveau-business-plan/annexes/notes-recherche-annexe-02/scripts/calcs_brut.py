import yaml
p='working-folder/controle-sources/calculs.yaml'; t=open(p,encoding='utf-8').read()
assert 'CALC-A2-HUILE-NODA-0909-BRUT' not in t
add={'CALC-A2-HUILE-NODA-0909-BRUT':{'description':"Huile sur entree brute, plastiques d'emballage de Noda 2022-09-09",'formule':'huile / entree','entrees':{'huile':{'valeur':16.1,'unite':'kg','source':'CHIBA-ESSAIS-FICHES','emplacement':'PDF p. 26'},'entree':{'valeur':50,'unite':'kg','source':'CHIBA-ESSAIS-FICHES','emplacement':'PDF p. 26'}},'resultat':0.322,'unite':'fraction'},
'CALC-A2-HUILE-NODA-0915-BRUT':{'description':"Huile sur entree brute, residus incombustibles de Noda 2022-09-15",'formule':'huile / entree','entrees':{'huile':{'valeur':22.5,'unite':'kg','source':'CHIBA-ESSAIS-FICHES','emplacement':'PDF p. 26'},'entree':{'valeur':50,'unite':'kg','source':'CHIBA-ESSAIS-FICHES','emplacement':'PDF p. 26'}},'resultat':0.45,'unite':'fraction'}}
t=t.rstrip('\n')+'\n'+yaml.safe_dump(add,allow_unicode=True,sort_keys=False,width=4000)
yaml.safe_load(t); open(p,'w',encoding='utf-8').write(t); print('ok')
