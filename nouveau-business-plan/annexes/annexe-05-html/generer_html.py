#!/usr/bin/env python3
"""Genere la version HTML de l'annexe 5 (index.html, preuves/*.html) a partir de
ANNEX-05-Municipal-Solid-Waste.md et des registres. Adapte du generateur de l'annexe 8 (decision D-023).
Les fiches deja presentes dans les annexes 1, 2, 3 et 8 sont reprises par lien, sauf les sources relues pour
l'annexe 5 (LOCAL), qui ont leur fiche ici ; les autres ont leur fiche ici.
Les fiches sont construites automatiquement a partir du registre (type, statut) : groupe et taux de confiance
suivent l'echelle de D-022.
Usage : python3 nouveau-business-plan/annexes/annexe-05-html/generer_html.py"""
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
spec3 = importlib.util.spec_from_file_location('gen3', os.path.join(ANNEXES, 'annexe-03-html', 'generer_html.py'))
g3 = importlib.util.module_from_spec(spec3); spec3.loader.exec_module(g3)
spec8 = importlib.util.spec_from_file_location('gen8', os.path.join(ANNEXES, 'annexe-08-html', 'generer_html.py'))
g8 = importlib.util.module_from_spec(spec8); spec8.loader.exec_module(g8)
LOCAL = {'ADEME-MODECOM-2024-DATA', 'ADEME-MODECOM-2024-HUM', 'RP2-004', 'RP2-002', 'ORDIF-DMA-2022'}

ev = yaml.safe_load(open(os.path.join(WF, 'params', '_evidence.yaml'), encoding='utf-8'))
ext = yaml.safe_load(open(os.path.join(WF, 'reference', 'sources-externes', 'registre-sources.yaml'), encoding='utf-8'))
calcs = yaml.safe_load(open(os.path.join(WF, 'controle-sources', 'calculs.yaml'), encoding='utf-8'))
decs = yaml.safe_load(open(os.path.join(WF, 'params', '_decisions.yaml'), encoding='utf-8'))
MD = open(os.path.join(ANNEXES, 'ANNEX-05-Municipal-Solid-Waste.md'), encoding='utf-8').read()

GROUPS = [('M', 'OneWorld design data'), ('R', 'Legislation, regulations and standards'),
          ('P', 'Prices and official statistics'), ('L', 'Industry, literature and other sources'), ('C', 'Calculations')]
TYPE_GROUP = {'reglementaire': 'R', 'norme': 'R', 'statistique_publique': 'P', 'indice_marche': 'P',
              'observatoire': 'P', 'donnees_ouvertes': 'P'}
TYPE_EN = {'reglementaire': 'Legislation or regulation', 'norme': 'Standard', 'statistique_publique': 'Official statistics',
           'indice_marche': 'Market index (commercial source)', 'observatoire': 'Observatory (eco-organisation)',
           'donnees_ouvertes': 'Open data', 'etude_publique': 'Institutional or peer-reviewed study',
           'federation': 'Industry federation', 'entreprise': 'Company document (commercial source)',
           'presse': 'Press', 'publication': 'Scientific publication'}

def fiche(i): return (ext.get(i) or ev.get(i) or {}) if i in LOCAL else (ev.get(i) or ext.get(i) or {})

def classify(i):
    """(groupe, confiance, nature, etiquette) d'une source propre a l'annexe 3"""
    f = fiche(i)
    if i in ev and not (i in LOCAL and i in ext):
        return 'M', 95, 'OneWorld documentation (company data, not independently verified)', 'CONSTRUCTEUR'
    t, st = str(f.get('type', '')), str(f.get('statut', ''))
    g = TYPE_GROUP.get(t, 'L')
    nature = TYPE_EN.get(t, t or 'Source')
    if st in ('secondaire', 'non-verifie'):
        return g, 80, nature + '; secondary or unverified reading', 'SECONDAIRE' if st == 'secondaire' else 'NON VÉRIFIÉ'
    if st == 'ancien':
        return g, 90, nature + '; data older than eight years', 'LU (ancien)'
    lab = 'VÉRIFIÉ' if st == 'verifie-recontrole' else 'LU'
    if t == 'presse':
        return g, 90, nature, lab
    if g in ('R',) or t in ('statistique_publique', 'donnees_ouvertes', 'observatoire'):
        return g, 100, nature, lab
    return g, 95, nature, lab

cites = list(dict.fromkeys(re.findall(r'\[((?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+)\]', MD)))
def key(t): return t[5:] if t.startswith('calc:') else t
def elsewhere(k):
    """code et lien d'une fiche deja presente dans l'annexe 2 ou l'annexe 1"""
    if k in LOCAL: return None
    if k in g2.CODE: return 'a2'
    if k in g1.CODE: return 'a1'
    if k in g3.CODE: return 'a3'
    if k in g8.CODE: return 'a8'
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
            CODE[t] = f'5.{g}.{letters[n]}'; ORDER.append(t); n += 1
CALC3 = [key(t) for t in cites if t.startswith('calc:') and not elsewhere(key(t))]
# calculs d'entree propres a l'annexe 3 qui ne sont pas cites dans le texte
def deps(c, seen):
    for e in (calcs[c].get('entrees') or {}).values():
        if 'calc' in e and e['calc'] not in seen and not elsewhere(e['calc']):
            seen.append(e['calc']); deps(e['calc'], seen)
for c in list(CALC3): deps(c, CALC3)
CALC3 = list(dict.fromkeys(CALC3))
for n, c in enumerate(CALC3):
    CODE[c] = f'5.C.{letters[n]}'; ORDER.append(c)
# sources d'entree des calculs, non citees dans le texte
for c in CALC3:
    for e in (calcs[c].get('entrees') or {}).values():
        s = e.get('source')
        if s and s not in CODE and not elsewhere(s) and (s in ext or s in ev):
            SRC3[s] = classify(s)
            g = SRC3[s][0]; n = len([x for x in CODE.values() if x.startswith(f'5.{g}.')])
            CODE[s] = f'5.{g}.{letters[n]}'; ORDER.append(s)

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
    if elsewhere(i) == 'a3': return g3.conf_of(i)
    if elsewhere(i) == 'a8': return g8.conf_of(i)
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
    if w == 'a3':
        return ('../' * depth) + '../annexe-03-html/preuves/A' + g3.CODE[i].replace('.', '-') + '.html', g3.CODE[i]
    if w == 'a8':
        return ('../' * depth) + '../annexe-08-html/preuves/A' + g8.CODE[i].replace('.', '-') + '.html', g8.CODE[i]
    return None, i

def pill(tok, depth):
    if tok.startswith('hyp:'):
        d = tok[4:]
        return f'<a href="{"" if depth else "preuves/"}A5-D.html#{d}" title="Decision {d}">{d}</a>'
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
BANNIERE = ('<!-- Fichier genere par generer_html.py a partir de ANNEX-05-Municipal-Solid-Waste.md et des registres. '
            'Ne pas modifier a la main : corriger la source, puis regenerer. -->')
def page(title, body, crumb=''):
    return f'''<!doctype html>
{BANNIERE}
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><style>{CSS}</style></head>
<body><main>{crumb}{body}</main></body></html>'''
CR = lambda: '<p class="crumb"><a href="../index.html">Annex 5. Municipal Solid Waste</a> · <a href="index.html">All evidence sheets</a></p>'

LABEL_EN = {'CONSTRUCTEUR': 'CONSTRUCTEUR (OneWorld design data, read in the original, not independently verified)',
            'LU': 'LU (read in the source by Claude or a research sub-agent, not yet cross-checked by a second reader)',
            'LU (ancien)': 'LU, data older than eight years',
            'VÉRIFIÉ': 'VÉRIFIÉ (read in the source, then re-opened by an independent checker who found the key figures)',
            'SECONDAIRE': 'SECONDAIRE (read through an intermediary, or summary only)',
            'NON VÉRIFIÉ': 'NON VÉRIFIÉ (commercial or unverified source)'}

def source_page(i):
    f = fiche(i); g, conf, nature, label = SRC3[i]
    files = g1.pdf_links(f.get('chemin', '')) if f.get('chemin') else ''
    if f.get('url'): files = (files + ' ; ' if files else '') + f'<a href="{esc(f["url"])}">{esc(f.get("titre", "online source"))}</a>'
    r5 = f.get('relecture_a5_2026_11_19')
    rel = (f.get('relecture_a8_2026_10_15') or []) + (f.get('relecture_a8_2026_10_15_b') or []) + ([r5] if isinstance(r5, dict) else (r5 or []))
    quotes = ''.join(f'<li>« {esc(v)} »</li>' for k, v in f.items() if str(k).startswith('citation'))
    quotes += ''.join(f'<li>« {esc(r.get("citation"))} » <span class="small">(re-read{", " + esc(r.get("emplacement")) if r.get("emplacement") else ""})</span></li>' for r in rel if r.get('citation'))
    vals = ''.join(f'<li>{esc(f[k])}</li>' for k in ['contenu'] + [x for x in f if str(x).startswith('valeurs')] if f.get(k))
    vals += ''.join(f'<li>{esc(r.get("contenu"))}</li>' for r in rel if r.get('contenu'))
    vals += ''.join(f'<li><pre>{esc(r.get("valeurs_omr"))}</pre></li>' for r in rel if r.get('valeurs_omr'))
    if any(r.get('fichier') for r in rel): vals += ''.join(f'<li>Local copy: <code>{esc(r.get("fichier"))}</code></li>' for r in rel if r.get('fichier'))
    notes = ''.join(f'<li>{esc(f[k])}</li>' for k in ['reserve', 'note', 'recontrole_a8', 'recontrole_a5'] if f.get(k))
    if not f.get('emplacement') and rel:
        f = dict(f); f['emplacement'] = ' ; '.join(str(r.get('emplacement')) for r in rel if r.get('emplacement'))
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
                evl = f'<a href="A5-D.html#{k}">{k}</a>'
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
DEC_EN.update(g3.DEC_EN)
DEC_EN.update(g8.DEC_EN)
DEC_EN.update({
 'D-043': 'Working assumption posed by Claude (19 November 2026), to be confirmed by the project sponsor: in residual household waste, only the plastic category produces a saleable oil; plastic in nappies, composites and synthetic textiles is not counted; the other organic matter gives char, water and gas.',
 'D-044': 'Working assumption posed by Claude (19 November 2026), to be confirmed: the oil and gas yields of the Chiba plastic tests apply to the dry mass of the plastic of residual waste (moisture from MODECOM 2024); oil at 55 % (low), 73.07 % (central) or 81 % (high); gas at 10 % (D-029).',
 'D-045': 'Working assumption posed by Claude (19 November 2026), to be confirmed: char of the non-plastic organic matter taken at 30 % of its dry mass, range 25 to 40 %, from published laboratory data.',
 'D-046': 'Working assumption posed by Claude (19 November 2026): tonnages and shares from the MODECOM 2024 composition data set (no fines for residual waste); water and dry matter from the moisture data set (fines under 8 mm as a separate fraction of 5.4 %). The allocation method of the fines is to be read in the full technical report.',
 'D-033': 'Chiba report: page 42 (mass balance) used for the metals, char and water of the run of 9 September 2022, where the test sheet and the balance differ.',
 'D-034': 'Chiba report: the mixed plastic run of 11 July 2022 is shown but excluded from the averages; statistics of pure plastics on 10 runs.',
 'D-018': 'Scope of Annex 8: all plastic streams, household and industrial, with priority to those little or not recycled; single-plastic industrial streams belong here, mixed commercial waste to Annex 7.',
 'D-035': 'Reactor capacity of 200 m3 per day; feed density after pressing taken at 0.7 t/m3, i.e. 140 t per day (working assumption of the project sponsor).',
 'D-037': 'Shredder residues (vehicles, electronic equipment) are excluded from the plan, on the judgement of the Chiba report.',
 'D-039': 'Gate fee of plastic streams taken at 100 EUR/t by default, a value the operator can change on the website and in the spreadsheet (assumption of the project sponsor).',
 'D-040': 'Answers of the project sponsor (15 October 2026): maximum PVC share left open until OneWorld tests; brominated plastics await OneWorld tests, with the working assumption that bromine is largely removed as chlorine is; all streams retained; 2026 waste tax rates used; statuses of the re-read evidence sheets set to read.',
 'D-041': 'Entry price pre-filled according to the stream selected, always changeable by the operator.',
 'D-042': 'Default entry prices by stream and sign convention: positive when the plant is paid, negative when it buys. Sorted plastic bales bought at 249 EUR/t; clean white expanded polystyrene bought at 55 EUR/t; streams taken back at zero: 0; rejects of commercial packaging paid 188 EUR/t; household sorting rejects, residual household waste, brominated plastics, synthetic textiles, furniture foams and building plastics paid 100 EUR/t (assumption).',
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
    return page('Annex 5. Decisions', body, CR())

def index_page():
    rows = ''
    for g, gt in GROUPS:
        items = [i for i in ORDER if CODE[i].startswith(f'5.{g}.')]
        if not items: continue
        rows += f'<tr><th colspan="3">8.{g} · {esc(gt)}</th></tr>'
        for i in items:
            d = fiche(i).get('titre', '') if i in SRC3 else calcs[i].get('description', '')
            rows += f'<tr><td><a href="A{CODE[i].replace(".", "-")}.html">{CODE[i]}</a></td><td>{esc(d)}</td><td>{conf_of(i)} %</td></tr>'
    rows += '<tr><th colspan="3">Evidence sheets of Annexes 1, 2, 3 and 8 cited in this annex</th></tr>'
    for t in cites:
        k = key(t)
        if t.startswith('hyp:') or k in CODE or not elsewhere(k): continue
        h, code = href(k, 1)
        d = g2.SRC[k][4] if k in g2.SRC else (calcs[k].get('description', '') if k in calcs else fiche(k).get('titre', ''))
        rows += f'<tr><td><a href="{h}">{code}</a></td><td>{esc(d)}</td><td>{conf_of(k)} %</td></tr>'
    rows += f'<tr><th colspan="3">Decisions</th></tr><tr><td><a href="A5-D.html">5.D</a></td><td>Decisions {", ".join(USED_DEC)}</td><td>n/a</td></tr>'
    body = f'''<h1>Annex 5. Evidence sheets</h1>
<p>Each figure or fact of Annex 5 links to one of these sheets. Sheets 5.M (OneWorld design data), 5.R (legislation and standards), 5.P (prices and official statistics), 5.L (industry and literature) and 5.C (calculations) belong to this annex; sheets 1.x, 2.x, 3.x and 8.x are those of Annexes 1, 2, 3 and 8, used here without duplication.</p>
<h2>Confidence scale</h2>
<table><tr><th>Confidence</th><th>Applies to</th></tr>
<tr><td>100 %</td><td>Legislation, regulations, official statistics and open data, observatories of approved eco-organisations, independent laboratory reports</td></tr>
<tr><td>95 %</td><td>OneWorld design data, company and federation documents, institutional and peer-reviewed studies, calculations on data at 95 % or more</td></tr>
<tr><td>90 %</td><td>Press, data older than eight years, calculations using a working assumption</td></tr>
<tr><td>80 %</td><td>Secondary sources and unverified commercial indices</td></tr></table>
<h2>All sheets</h2><table><tr><th>Sheet</th><th>Content</th><th>Confidence</th></tr>{rows}</table>'''
    return page('Annex 5. Evidence sheets', body, '<p class="crumb"><a href="../index.html">Annex 5. Municipal Solid Waste</a></p>')

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
    return page('Annex 5. Municipal Solid Waste', body), left

if __name__ == '__main__':
    mp, left = main_page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(mp)
    for i in ORDER:
        open(os.path.join(PREUVES, f'A{CODE[i].replace(".", "-")}.html'), 'w', encoding='utf-8').write(source_page(i) if i in SRC3 else calc_page(i))
    open(os.path.join(PREUVES, 'A5-D.html'), 'w', encoding='utf-8').write(decisions_page())
    open(os.path.join(PREUVES, 'index.html'), 'w', encoding='utf-8').write(index_page())
    sans = [t for t in cites if not t.startswith('hyp:') and href(key(t), 0)[0] is None]
    print('fiches annexe 5 :', len(ORDER) + 2, '; renvois annexes 1, 2, 3 et 8 :', len([t for t in cites if elsewhere(key(t))]),
          '; citations sans fiche :', sans, '; marqueurs non convertis :', left[:5])
