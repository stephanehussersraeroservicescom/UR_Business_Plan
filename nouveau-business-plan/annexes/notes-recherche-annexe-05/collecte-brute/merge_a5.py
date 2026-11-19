import sys, yaml, shutil, datetime
reg, nouv, rel, bak = sys.argv[1:5]
shutil.copy(reg, bak)
txt = open(reg, encoding='utf-8').read()
lines = txt.split('\n')
R = yaml.safe_load(open(rel, encoding='utf-8'))
for ident, champs in R.items():
    bloc = yaml.safe_dump(champs, allow_unicode=True, sort_keys=False, width=1000)
    bloc = '\n'.join('  ' + l if l else l for l in bloc.rstrip('\n').split('\n'))
    idx = [i for i, l in enumerate(lines) if l == ident + ':']
    assert len(idx) == 1, (ident, idx)
    lines.insert(idx[0] + 1, bloc)
out = '\n'.join(lines).rstrip('\n') + '\n' + open(nouv, encoding='utf-8').read()
d = yaml.safe_load(out)
for k in list(R) + list(yaml.safe_load(open(nouv, encoding='utf-8'))):
    assert k in d, k
open(reg, 'w', encoding='utf-8').write(out)
print('ok', len(d))
