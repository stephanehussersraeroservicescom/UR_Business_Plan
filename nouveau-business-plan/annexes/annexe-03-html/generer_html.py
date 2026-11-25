#!/usr/bin/env python3
"""Genere la version HTML de l'annexe 3 (index.html, preuves/*.html) a partir de
ANNEX-03-Output-Markets-and-Pricing.md et des registres. Adapte du generateur de l'annexe 1 (decision D-023).
Les fiches deja presentes dans les annexes 1 et 2 sont reprises par lien ; les autres ont leur fiche ici.
Les fiches sont construites automatiquement a partir du registre (type, statut) : groupe et taux de confiance
suivent l'echelle de D-022.
Usage : python3 nouveau-business-plan/annexes/annexe-03-html/generer_html.py"""
import os, re, sys, importlib.util, html as H
import yaml, markdown
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ANNEXES = os.path.normpath(os.path.join(HERE, '..'))
ROOT = os.path.normpath(os.path.join(ANNEXES, '..', '..'))
WF = os.path.join(ROOT, 'working-folder')
PREUVES = os.path.join(HERE, 'preuves')
os.makedirs(PREUVES, exist_ok=True)

# --- generateurs des annexes 1 et 2 (lecture seule : codes et noms de leurs fiches)
spec = importlib.util.spec_from_file_location('gen1', os.path.join(ANNEXES, 'annexe-01-html', 'generer_html.py'))
g1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(g1)
g2 = g1.g2

ev = yaml.safe_load(open(os.path.join(WF, 'params', '_evidence.yaml'), encoding='utf-8'))
ext = yaml.safe_load(open(os.path.join(WF, 'reference', 'sources-externes', 'registre-sources.yaml'), encoding='utf-8'))
calcs = yaml.safe_load(open(os.path.join(WF, 'controle-sources', 'calculs.yaml'), encoding='utf-8'))
decs = yaml.safe_load(open(os.path.join(WF, 'params', '_decisions.yaml'), encoding='utf-8'))
MD = open(os.path.join(ANNEXES, 'ANNEX-03-Output-Markets-and-Pricing.md'), encoding='utf-8').read()

GROUPS = [('M', 'OneWorld design data'), ('R', 'Legislation, regulations and standards'),
          ('P', 'Prices and official statistics'), ('L', 'Industry, literature and other sources'), ('C', 'Calculations')]
TYPE_GROUP = {'reglementaire': 'R', 'diffusion_administrative': 'R', 'norme': 'R', 'statistique_publique': 'P', 'indice_marche': 'P',
              'observatoire': 'P', 'donnees_ouvertes': 'P'}
TYPE_EN = {'reglementaire': 'Legislation or regulation', 'diffusion_administrative': 'Administrative publication (not the legal text itself)', 'norme': 'Standard', 'statistique_publique': 'Official statistics',
           'indice_marche': 'Market index (commercial source)', 'observatoire': 'Observatory (eco-organisation)',
           'donnees_ouvertes': 'Open data', 'etude_publique': 'Institutional or peer-reviewed study',
           'federation': 'Industry federation', 'entreprise': 'Company document (commercial source)',
           'presse': 'Press', 'publication': 'Scientific publication'}

def fiche(i): return ext.get(i) or ev.get(i) or {}  # 25/11/2026 : une source publique presente dans les deux registres est lue dans le registre externe

def classify(i):
    """(groupe, confiance, nature, etiquette) d'une source propre a l'annexe 3"""
    f = fiche(i)
    if i in ev and i not in ext:
        return 'M', 95, 'OneWorld documentation (company data, not independently verified)', 'CONSTRUCTEUR'
    t, st = str(f.get('type', '')), str(f.get('statut', ''))
    g = TYPE_GROUP.get(t, 'L')
    nature = TYPE_EN.get(t, t or 'Source')
    if st in ('secondaire', 'non-verifie'):
        return g, 80, nature + '; secondary or unverified reading', 'SECONDAIRE' if st == 'secondaire' else 'NON VÉRIFIÉ'
    if st == 'ancien':
        return g, 90, nature + '; data older than eight years', 'LU (ancien)'
    if t == 'presse':
        return g, 90, nature, 'LU'
    if g in ('R',) or t in ('statistique_publique', 'donnees_ouvertes', 'observatoire'):
        return g, 100, nature, 'LU'
    return g, 95, nature, 'LU'

cites = list(dict.fromkeys(re.findall(r'\[((?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+)\]', MD)))
def key(t): return t[5:] if t.startswith('calc:') else t
def elsewhere(k):
    """code et lien d'une fiche deja presente dans l'annexe 2 ou l'annexe 1"""
    if k in g2.CODE: return 'a2'
    if k in g1.CODE: return 'a1'
    return None

CODE = {}; ORDER = []; SRC3 = {}
letters = [a for a in 'abcdefghijklmnopqrstuvwxyz'] + [a + b for a in 'abcdefghijklmnopqrstuvwxyz' for b in 'abcdefghijklmnopqrstuvwxyz']
for t in cites:
    if t.startswith('hyp:') or t.startswith('calc:'): continue
    if elsewhere(t): continue
    SRC3[t] = classify(t)
for g, _ in GROUPS[:4]:
    n = 0
    for t in cites:
        if t in SRC3 and SRC3[t][0] == g:
            CODE[t] = f'3.{g}.{letters[n]}'; ORDER.append(t); n += 1
CALC3 = [key(t) for t in cites if t.startswith('calc:') and not elsewhere(key(t))]
# calculs d'entree propres a l'annexe 3 qui ne sont pas cites dans le texte
def deps(c, seen):
    for e in (calcs[c].get('entrees') or {}).values():
        if 'calc' in e and e['calc'] not in seen and not elsewhere(e['calc']):
            seen.append(e['calc']); deps(e['calc'], seen)
for c in list(CALC3): deps(c, CALC3)
CALC3 = list(dict.fromkeys(CALC3))
for n, c in enumerate(CALC3):
    CODE[c] = f'3.C.{letters[n]}'; ORDER.append(c)
# sources d'entree des calculs, non citees dans le texte
for c in CALC3:
    for e in (calcs[c].get('entrees') or {}).values():
        s = e.get('source')
        if s and s not in CODE and not elsewhere(s) and (s in ext or s in ev):
            SRC3[s] = classify(s)
            g = SRC3[s][0]; n = len([x for x in CODE.values() if x.startswith(f'3.{g}.')])
            CODE[s] = f'3.{g}.{letters[n]}'; ORDER.append(s)

def esc(x): return H.escape(str(x))
def calc_conf(c):
    cs = []
    for e in (calcs[c].get('entrees') or {}).values():
        if 'calc' in e: cs.append(conf_of(e['calc']))
        elif str(e.get('source', '')).startswith('D-'): cs.append(90)
        else: cs.append(conf_of(e['source']))
    return min(min(cs) if cs else 95, 95)
def conf_of(i):
    if i in SRC3: return SRC3[i][1]
    if i in CALC3: return calc_conf(i)
    if elsewhere(i) == 'a1': return g1.conf_of(i)
    if i in g2.SRC: return g2.SRC[i][1]
    if i in g2.CODE and i in calcs: return g2.calc_conf(i)
    return 95

def href(i, depth):
    """depth 0 : depuis index.html ; depth 1 : depuis preuves/"""
    if i in CODE:
        return ('' if depth else 'preuves/') + 'A' + CODE[i].replace('.', '-') + '.html', CODE[i]
    w = elsewhere(i)
    if w == 'a2':
        return ('../' * depth) + '../annexe-02-html/preuves/' + g2.fname(i), g2.CODE[i]
    if w == 'a1':
        return ('../' * depth) + '../annexe-01-html/preuves/A' + g1.CODE[i].replace('.', '-') + '.html', g1.CODE[i]
    return None, i

def pill(tok, depth):
    if tok.startswith('hyp:'):
        d = tok[4:]
        return f'<a href="{"" if depth else "preuves/"}A3-D.html#{d}" title="Decision {d}">{d}</a>'
    h, code = href(key(tok), depth)
    if not h: return ''
    return f'<a href="{h}" title="{esc(key(tok))}">{code}</a>'

def pills_in(s, depth):
    def rep(m):
        toks = re.findall(r'\[((?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+)\]', m.group(0))
        out = list(dict.fromkeys(pill(t, depth) for t in toks))
        return '<span class="ev">' + ''.join(out) + '</span>'
    return re.sub(r'(?:\s*\[(?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+\])+', rep, s)

CSS = g1.CSS
BANNIERE = ('<!-- Fichier genere par generer_html.py a partir de ANNEX-03-Output-Markets-and-Pricing.md et des registres. '
            'Ne pas modifier a la main : corriger la source, puis regenerer. -->')
def page(title, body, crumb=''):
    return f'''<!doctype html>
{BANNIERE}
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><style>{CSS}</style></head>
<body><main>{crumb}{body}</main></body></html>'''
CR = lambda: '<p class="crumb"><a href="../index.html">Annex 3. Output Markets and Pricing</a> · <a href="index.html">All evidence sheets</a></p>'

LABEL_EN = {'CONSTRUCTEUR': 'CONSTRUCTEUR (OneWorld design data, read in the original, not independently verified)',
            'LU': 'LU (read in the source by Claude or a research sub-agent, not yet cross-checked by a second reader)',
            'LU (ancien)': 'LU, data older than eight years',
            'SECONDAIRE': 'SECONDAIRE (read through an intermediary, or summary only)',
            'NON VÉRIFIÉ': 'NON VÉRIFIÉ (commercial or unverified source)'}

def source_page(i):
    f = fiche(i); g, conf, nature, label = SRC3[i]
    files = g1.pdf_links(f.get('chemin', '')) if f.get('chemin') else ''
    if f.get('url'): files = (files + ' ; ' if files else '') + f'<a href="{esc(f["url"])}">{esc(f.get("titre", "online source"))}</a>'
    quotes = ''.join(f'<li>« {esc(v)} »</li>' for k, v in f.items() if str(k).startswith('citation'))
    vals = ''.join(f'<li>{esc(f[k])}</li>' for k in ['contenu'] + [x for x in f if str(x).startswith('valeurs')] if f.get(k))
    notes = ''.join(f'<li>{esc(f[k])}</li>' for k in ['reserve', 'note'] if f.get(k))
    for _k in sorted(k for k in f if str(k).startswith('relecture')):
        _v = f[_k]
        for _r in ([_v] if isinstance(_v, dict) else (_v or [])):
            if isinstance(_r, dict):
                if _r.get('citation'): quotes += f'<li>« {esc(_r.get("citation"))} » <span class="small">(re-read{", " + esc(_r.get("emplacement")) if _r.get("emplacement") else ""})</span></li>'
                if _r.get('contenu'): vals += f'<li>{esc(_r.get("contenu"))}</li>'
    body = f'''<h1>Evidence {CODE[i]}</h1>
<p class="small">{esc(f.get('titre', ''))}</p>
<div class="cards">
 <div class="card"><h4>What this evidence shows</h4><p>{esc(f.get('titre', ''))}. {esc(f.get('editeur', ''))}. The values read are listed below, as recorded in the project register (in French).</p></div>
 <div class="card"><h4>Confidence</h4><div class="conf">{conf} %</div><p class="small">{esc(nature)}</p></div>
</div>
<h2>How it was obtained</h2>
<p>The facts were read in the source document below, at the location indicated, and recorded in the project register under <code>{esc(i)}</code>.</p>
<table><tr><th>Source document</th><td>{files}</td></tr>
<tr><th>Location in the document</th><td>{esc(f.get('emplacement', ''))}</td></tr>
<tr><th>Date</th><td>{esc(f.get('date', 'not printed'))}</td></tr>
<tr><th>Nature of the source</th><td>{esc(nature)}</td></tr>
<tr><th>Label</th><td>{esc(LABEL_EN.get(label, label))}</td></tr>
<tr><th>Read on</th><td>{esc(f.get('consulte', ''))}</td></tr></table>
{('<h2>Quotation (original language)</h2><ul>' + quotes + '</ul>') if quotes else ''}
<h2>Values and content read</h2><ul>{vals}</ul>
{('<h2>Notes</h2><ul>' + notes + '</ul>') if notes else ''}'''
    return page(f'Evidence {CODE[i]}', body, CR())

def calc_page(c):
    f = calcs[c]; conf = calc_conf(c); rows = ''
    for n, e in (f.get('entrees') or {}).items():
        if 'calc' in e:
            k = e['calc']; val = calcs[k].get('resultat', ''); unit = calcs[k].get('unite', ''); where = calcs[k].get('description', '')
            h, code = href(k, 1); evl = f'<a href="{h}">{code}</a>'
        else:
            k = str(e.get('source', '')); val = e['valeur']; unit = e.get('unite', ''); where = e.get('emplacement', '')
            if k.startswith('D-'):
                evl = f'<a href="A3-D.html#{k}">{k}</a>'
            else:
                h, code = href(k, 1); evl = f'<a href="{h}">{code}</a>'
        rows += f'<tr><td><code>{esc(n)}</code></td><td>{esc(val)} {esc(unit)}</td><td>{esc(where)}</td><td><span class="ev">{evl}</span></td></tr>'
    body = f'''<h1>Evidence {CODE[c]}</h1>
<p class="small">Calculation</p>
<div class="cards">
 <div class="card"><h4>What this calculation gives</h4><p>{esc(f.get('description', ''))}</p><p class="result" style="margin-top:10px">Result: <strong>{esc(f["resultat"])}</strong> {esc(f.get("unite", ""))}</p></div>
 <div class="card"><h4>Confidence</h4><div class="conf">{conf} %</div><p class="small">Label CALCULÉ. A calculation is rated at its least reliable input, at most 95 %, and at most 90 % when it uses a working assumption.</p></div>
</div>
<h2>How it was calculated</h2>
<p>The formula below is applied to the inputs listed, each taken from its own evidence sheet. The description of the calculation is recorded in the register in French.</p>
<h3>Formula</h3><pre>{esc(f["formule"])}</pre>
<h3>Inputs</h3>
<table><tr><th>Input</th><th>Value</th><th>Location or description</th><th>Evidence</th></tr>{rows}</table>
<p class="small">Register entry <code>{esc(c)}</code>. The formula is recalculated automatically by the project control script.</p>'''
    return page(f'Evidence {CODE[c]}', body, CR())

DEC_EN = dict(g1.DEC_EN)
DEC_EN.update(g1.DEC_EN_MODELE)
DEC_EN.update({
 'D-027': 'OneWorld, the manufacturer of the Urban Rig, is the sponsor of this business plan. Its documentation is marked "OneWorld design data" in the text and keeps the label CONSTRUCTEUR in the evidence sheets: these are the company\'s own figures, not independent verification.',
 'D-028': 'Choices of the project sponsor on output prices (15 October 2026): oil priced by fraction; char sold, cement plants as main outlet; steel and aluminium at public prices; no price for glass and inerts; no carbon revenue; electricity bought; process heat from the pyrolysis gas, the surplus being saleable.',
 'D-029': 'Gas from plastic taken at 10 % of the plastic input for mixed waste; energy self-sufficiency by the process gas is not asserted for household or municipal waste; resin-rich feeds keep the treatment of Annex 2.',
 'D-030': 'Each default price is the most recent published value, with its source, date and scope; the operator of the model can replace it, and prices linked to crude oil can be recalculated for a Brent price entered by the operator, the ratio of each benchmark to the Brent of the same period being held constant.',
 'D-031': 'Hydrogen is shown as a costed option only for a plastic-only feed; it is priced as conventional hydrogen, no low-carbon status being established.',
 'D-032': 'Working assumption for the CO2 avoided compared with incineration (resin-rich feed): the fossil carbon of the feed is emitted in both routes; the oil replaces heavy fuel oil at equal energy; the incinerator replaces energy as per ADEME; purchased electricity at the French average mix. Not counted: transport, flue gas treatment, char and surplus gas sold, process losses.',
})
USED_DEC = sorted({t[4:] for t in cites if t.startswith('hyp:')} | {str(e.get('source')) for c in CALC3 for e in (calcs[c].get('entrees') or {}).values() if str(e.get('source', '')).startswith('D-')} | {'D-016', 'D-022'})
def decisions_page():
    rows = ''.join(f'<h2 id="{d}">{d}. {esc(decs[d].get("titre", ""))}</h2><p>{esc(DEC_EN.get(d, ""))}</p><p class="small">Dated {esc(decs[d].get("date", ""))}. Full text in French in <code>working-folder/params/_decisions.yaml</code>: « {esc(" ".join(str(decs[d].get("motif", "")).split()))} »</p>' for d in USED_DEC if d in decs)
    body = '''<h1>Decisions and working assumptions</h1>
<div class="cards"><div class="card"><h4>What this sheet shows</h4><p>The dated decisions of the project sponsor, and the working assumptions, on which this annex relies. A figure that depends on a working assumption is capped at 90 % confidence.</p></div>
<div class="card"><h4>Confidence</h4><div class="conf">n/a</div><p class="small">Decisions, not measurements.</p></div></div>''' + rows
    return page('Annex 3. Decisions', body, CR())

def index_page():
    rows = ''
    for g, gt in GROUPS:
        items = [i for i in ORDER if CODE[i].startswith(f'3.{g}.')]
        if not items: continue
        rows += f'<tr><th colspan="3">3.{g} · {esc(gt)}</th></tr>'
        for i in items:
            d = fiche(i).get('titre', '') if i in SRC3 else calcs[i].get('description', '')
            rows += f'<tr><td><a href="A{CODE[i].replace(".", "-")}.html">{CODE[i]}</a></td><td>{esc(d)}</td><td>{conf_of(i)} %</td></tr>'
    rows += '<tr><th colspan="3">Evidence sheets of Annexes 1 and 2 cited in this annex</th></tr>'
    for t in cites:
        k = key(t)
        if t.startswith('hyp:') or k in CODE or not elsewhere(k): continue
        h, code = href(k, 1)
        d = g2.SRC[k][4] if k in g2.SRC else (calcs[k].get('description', '') if k in calcs else fiche(k).get('titre', ''))
        rows += f'<tr><td><a href="{h}">{code}</a></td><td>{esc(d)}</td><td>{conf_of(k)} %</td></tr>'
    rows += f'<tr><th colspan="3">Decisions</th></tr><tr><td><a href="A3-D.html">3.D</a></td><td>Decisions {", ".join(USED_DEC)}</td><td>n/a</td></tr>'
    body = f'''<h1>Annex 3. Evidence sheets</h1>
<p>Each figure or fact of Annex 3 links to one of these sheets. Sheets 3.M (OneWorld design data), 3.R (legislation and standards), 3.P (prices and official statistics), 3.L (industry and literature) and 3.C (calculations) belong to this annex; sheets 1.x and 2.x are those of Annexes 1 and 2, used here without duplication.</p>
<h2>Confidence scale</h2>
<table><tr><th>Confidence</th><th>Applies to</th></tr>
<tr><td>100 %</td><td>Legislation, regulations, official statistics and open data, observatories of approved eco-organisations, independent laboratory reports</td></tr>
<tr><td>95 %</td><td>OneWorld design data, company and federation documents, institutional and peer-reviewed studies, calculations on data at 95 % or more</td></tr>
<tr><td>90 %</td><td>Press, data older than eight years, calculations using a working assumption</td></tr>
<tr><td>80 %</td><td>Secondary sources and unverified commercial indices</td></tr></table>
<h2>All sheets</h2><table><tr><th>Sheet</th><th>Content</th><th>Confidence</th></tr>{rows}</table>'''
    return page('Annex 3. Evidence sheets', body, '<p class="crumb"><a href="../index.html">Annex 3. Output Markets and Pricing</a></p>')

def references_html():
    items = ''
    for t in cites:
        if t.startswith('hyp:'): continue
        k = key(t)
        if k in calcs: continue
        f = fiche(k); h, code = href(k, 0)
        items += f'<tr><td><span class="ev"><a href="{h}">{code}</a></span></td><td>{esc(f.get("titre", k))}</td><td>{esc(f.get("emplacement", ""))}</td><td>{conf_of(k)} %</td></tr>'
    return '<table><tr><th>Sheet</th><th>Document</th><th>Location</th><th>Confidence</th></tr>' + items + '</table>'

def main_page():
    s = pills_in(MD, 0)
    s = s.replace('All sheets are listed in the index of evidence sheets.', 'All sheets are listed in the <a href="preuves/index.html">index of evidence sheets</a>.')
    s = s.replace('The full list of documents cited, with their location and confidence, is in the index of evidence sheets.',
                  'Documents cited in this annex, with their location and confidence. The full list of sheets is in the <a href="preuves/index.html">index of evidence sheets</a>.\n\nREFERENCES_TABLE')
    s = re.sub(r'(?m)^((?!- |\d+\. |\s|\|)[^\n]+)\n(- |\d+\. )', r'\1\n\n\2', s)
    body = markdown.markdown(s, extensions=['tables', 'sane_lists'])
    body = body.replace('<p>REFERENCES_TABLE</p>', references_html())
    left = re.findall(r'\[(?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+\]', body)
    return page('Annex 3. Output Markets and Pricing', body), left

if __name__ == '__main__':
    mp, left = main_page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(mp)
    for i in ORDER:
        open(os.path.join(PREUVES, f'A{CODE[i].replace(".", "-")}.html'), 'w', encoding='utf-8').write(source_page(i) if i in SRC3 else calc_page(i))
    open(os.path.join(PREUVES, 'A3-D.html'), 'w', encoding='utf-8').write(decisions_page())
    open(os.path.join(PREUVES, 'index.html'), 'w', encoding='utf-8').write(index_page())
    sans = [t for t in cites if not t.startswith('hyp:') and href(key(t), 0)[0] is None]
    print('fiches annexe 3 :', len(ORDER) + 2, '; renvois annexes 1 et 2 :', len([t for t in cites if elsewhere(key(t))]),
          '; citations sans fiche :', sans, '; marqueurs non convertis :', left[:5])
