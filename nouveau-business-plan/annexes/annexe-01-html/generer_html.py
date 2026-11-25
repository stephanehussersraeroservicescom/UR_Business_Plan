#!/usr/bin/env python3
"""Genere la version HTML de l'annexe 1 (index.html, preuves/*.html, images/*.jpg) a partir de
ANNEX-01-Process-and-Technology.md et des registres. Adapte du generateur de l'annexe 2 (decision D-023).
Les preuves deja couvertes par une fiche de l'annexe 2 renvoient a cette fiche ; les autres ont leur fiche ici.
Usage : python3 nouveau-business-plan/annexes/annexe-01-html/generer_html.py"""
import os, re, sys, subprocess, importlib.util, html as H
import yaml, markdown
sys.dont_write_bytecode = True  # pas de __pycache__ dans le depot

HERE = os.path.dirname(os.path.abspath(__file__))
ANNEXES = os.path.normpath(os.path.join(HERE, '..'))
ROOT = os.path.normpath(os.path.join(ANNEXES, '..', '..'))
WF = os.path.join(ROOT, 'working-folder')
PREUVES = os.path.join(HERE, 'preuves'); IMAGES = os.path.join(HERE, 'images')
os.makedirs(PREUVES, exist_ok=True); os.makedirs(IMAGES, exist_ok=True)

# --- generateur de l'annexe 2 (lecture seule : codes et noms de ses fiches)
spec = importlib.util.spec_from_file_location('gen2', os.path.join(ANNEXES, 'annexe-02-html', 'generer_html.py'))
g2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(g2)

ev = yaml.safe_load(open(os.path.join(WF, 'params', '_evidence.yaml'), encoding='utf-8'))
ext = yaml.safe_load(open(os.path.join(WF, 'reference', 'sources-externes', 'registre-sources.yaml'), encoding='utf-8'))
calcs = yaml.safe_load(open(os.path.join(WF, 'controle-sources', 'calculs.yaml'), encoding='utf-8'))
decs = yaml.safe_load(open(os.path.join(WF, 'params', '_decisions.yaml'), encoding='utf-8'))
MD = open(os.path.join(ANNEXES, 'ANNEX-01-Process-and-Technology.md'), encoding='utf-8').read()

# --- sources propres a l'annexe 1 : (groupe, confiance, nature, etiquette, ce que la preuve montre)
MAN = 'Manufacturer documentation (OneWorld)'
SRC1 = {
 'OW-ENG-P14-P15-PROCEDE': ('M', 95, MAN + ', English brochure, October 2019', 'CONSTRUCTEUR',
   'OneWorld\'s description of the process: superheated steam at 600 °C in an oxygen-free reactor, chlorine catalyst, condenser, separation of gas oil and heavy oil by solenoid valve, oil and water separation; a continuous plant as 7 or 4 batch-type units at fixed temperatures; temperature of each unit, 90 minutes per step, start-up of 8 batches. Also OneWorld\'s statements on mixed waste, no sorting and non-oxidised metals (p. 2).'),
 'OW-ENG-P04-P07-SPEC-PLANS': ('M', 95, MAN + ', English brochure, October 2019', 'CONSTRUCTEUR',
   'Specification sheets and site layouts of the continuous models: microcomputer control, 7 processes for the URC-2000, valves and sensors; the layouts include an input throat with a crushing function and a sorting machine.'),
 'OW-ENG-P03-P19-GAMME-DELAIS': ('M', 95, MAN + ', English brochure, October 2019', 'CONSTRUCTEUR',
   'The OneWorld range (capacity, type, buckets, size of each model), the PRIMO flue gas treatment sold as an option, the FORCE 9 residue unit, and the manufacturing lead time.'),
 'UR2000-JP-P06-P07-MODULES': ('M', 95, MAN + ', URC-2000 brochure (Japanese)', 'CONSTRUCTEUR',
   'URC-2000 made of 7 units of about 12 t built in series, carried in 7 parts by truck and assembled on site; larger plants by combining 200 t plants; buckets loaded with waste as it is.'),
 'UR2000-JP-P09-P13-PLANS': ('M', 95, MAN + ', URC-2000 brochure (Japanese)', 'CONSTRUCTEUR',
   'Site layouts of the 200 t and 1,000 t per day plants (input throat with crushing, sorting machine), 2014 general drawing with its temperature zones, and contract-to-test-run schedule.'),
 'OW-BREVETS-2022': ('M', 90, 'Manufacturer list of patents (One World Japan), not checked in patent databases', 'CONSTRUCTEUR',
   'List of 18 patents and applications of One World Japan as of 27 December 2022.'),
 'OW-STEP-TOYOHASHI-9': ('M', 90, 'Manufacturer 3D model (part names only, no performance data)', 'CONSTRUCTEUR',
   '3D assembly of a 9-unit continuous machine at Toyohashi; its parts list shows the process chain, including a combustion tower connected to the gas-liquid separator.'),
 'OW-VIDEO-ANIMATION-2024': ('M', 90, 'Manufacturer promotional animation (One World Inc.), not a measurement', 'CONSTRUCTEUR',
   'Animation of a modular continuous plant with four heating steps and a cooling step, and an oil recovery rate of 45 % to 85 %.'),
 'OW-TRANSPORT-INSTALLATION': ('M', 90, 'Table from the manufacturer files; author and date not printed', 'CONSTRUCTEUR',
   'Containers, installation days and staff, training and maintenance interval for 1 t, 100 t and 200 t machines.'),
 'IGES-AEPW-PROPOSITION': ('M', 95, 'Funding proposal using OneWorld data (IGES, about 2020)', 'CONSTRUCTEUR',
   'OneWorld lists carbide, light oil, mixed oil and off-gas as saleable resources; no life cycle assessment available.'),
 'WFD-2008-98-ART3-4': ('R', 100, 'EU legislation', 'LU',
   'Waste Framework Directive: definitions of recovery and recycling (recycling excludes reprocessing into fuels) and the waste hierarchy.'),
 'IED-2010-75-ART3-42': ('R', 100, 'EU legislation', 'LU',
   'Industrial Emissions Directive: pyrolysis and gasification plants are waste incineration plants when their products are incinerated, unless the gases are purified and emit no more than natural gas.'),
 'A4-IED-2024-1785-ART42': ('R', 100, 'EU legislation', 'LU',
   'Directive (EU) 2024/1785 amending the Industrial Emissions Directive: since 2024, the incineration chapter does not apply to a pyrolysis or gasification plant whose gases or liquids are treated before being burned so that they emit less than the least polluting fuel that could be burned in the installation.'),
 'JRC-2023-PLASTIC-RECYCLING': ('R', 90, 'EU Joint Research Centre report (page numbers to be confirmed on the PDF)', 'LU',
   'Comparison of mechanical, physical and chemical recycling and energy recovery of plastic waste: recycling preferable to energy recovery; no clear ranking between mechanical and chemical recycling.'),
}
GROUPS = [('M', 'Manufacturer documentation (OneWorld)'), ('R', 'Regulations and reference reports'), ('C', 'Calculations')]

cites = list(dict.fromkeys(re.findall(r'\[((?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+)\]', MD)))
CODE = {}; ORDER = []
letters = 'abcdefghijklmnopqrstuvwxyz'
for g, _ in GROUPS[:2]:
    n = 0
    for i in SRC1:
        if SRC1[i][0] == g and i in cites:
            CODE[i] = f'1.{g}.{letters[n]}'; ORDER.append(i); n += 1
CALC1 = [c[5:] for c in cites if c.startswith('calc:') and c[5:] not in g2.CODE]
for n, c in enumerate(CALC1):
    CODE[c] = f'1.C.{letters[n]}'; ORDER.append(c)

def esc(x): return H.escape(str(x))
def fiche(i): return ev.get(i) or ext.get(i) or {}
def conf_of(i):
    if i in SRC1: return SRC1[i][1]
    if i in g2.SRC: return g2.SRC[i][1]
    if i in g2.CODE and i in calcs: return g2.calc_conf(i)
    if i in calcs: return calc_conf(i)
    return 95
def calc_conf(c):
    cs = []
    for n, e in (calcs[c].get('entrees') or {}).items():
        cs.append(conf_of(e['calc']) if 'calc' in e else conf_of(e['source']))
    return min(min(cs) if cs else 95, 95)

def href(i, depth):
    """depth 0 : depuis index.html ; depth 1 : depuis preuves/"""
    if i in CODE:
        return ('' if depth else 'preuves/') + 'A' + CODE[i].replace('.', '-') + '.html', CODE[i]
    if i in g2.CODE:
        return ('../' * depth) + '../annexe-02-html/preuves/' + g2.fname(i), g2.CODE[i]
    return None, i
def pill(tok, depth):
    if tok.startswith('hyp:'):
        d = tok[4:]
        if d in ('D-021',):
            return f'<a href="{"../" * depth}../annexe-02-html/preuves/A2-5-0.html" title="Working assumption {d}">2.5.0</a>'
        return f'<a href="{"" if depth else "preuves/"}A1-D.html#{d}" title="Decision {d}">{d}</a>'
    k = tok[5:] if tok.startswith('calc:') else tok
    h, code = href(k, depth)
    if not h: return ''
    return f'<a href="{h}" title="{esc(k)}">{code}</a>'

def pills_in(s, depth):
    def rep(m):
        toks = re.findall(r'\[((?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+)\]', m.group(0))
        out = list(dict.fromkeys(pill(t, depth) for t in toks))
        return '<span class="ev">' + ''.join(out) + '</span>'
    return re.sub(r'(?:\s*\[(?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+\])+', rep, s)

CSS = g2.CSS + '''
figure{margin:1.6em 0;padding:0}
figure img{width:100%;height:auto;border:1px solid var(--line);border-radius:6px;background:#fff}
figcaption{font:13px/1.4 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--muted);margin-top:6px}
.key{background:var(--box);border-radius:10px;padding:4px 18px;margin:1em 0}
'''
BANNIERE = ('<!-- Fichier genere par generer_html.py a partir de ANNEX-01-Process-and-Technology.md et des registres. '
            'Ne pas modifier a la main : corriger la source, puis regenerer. -->')
def page(title, body, crumb=''):
    return f'''<!doctype html>
{BANNIERE}
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><style>{CSS}</style></head>
<body><main>{crumb}{body}</main></body></html>'''
CR = lambda: '<p class="crumb"><a href="../index.html">Annex 1. Process and Technology</a> · <a href="index.html">All evidence sheets</a></p>'

def pdf_links(chemin):
    out = []
    for part in str(chemin).split(';'):
        p = part.strip().split(' (')[0].replace('doublon probable : ', '').replace('meme texte : ', '')
        for q in [x.strip() for x in p.split(' ; ')]:
            if q.startswith('reference/'):
                out.append(f'<a href="../../../../working-folder/{esc(q)}"><code>{esc(os.path.basename(q))}</code></a>')
    return ' ; '.join(out)

def source_page(i):
    f = fiche(i); g, conf, nature, label, summ = SRC1[i]
    files = pdf_links(f.get('chemin', '')) if f.get('chemin') else ''
    if f.get('url'): files = (files + ' ; ' if files else '') + f'<a href="{esc(f["url"])}">{esc(f.get("titre", "online source"))}</a>'
    quotes = ''.join(f'<li>« {esc(v)} »' + ('' if k == 'citation' else f' <span class="small">({esc(k.replace("citation_", ""))})</span>') + '</li>' for k, v in f.items() if str(k).startswith('citation'))
    trad = f'<p class="small">Translation by Claude (marked as such in the register): {esc(f["traduction_claude"])}</p>' if f.get('traduction_claude') else ''
    vals = ''.join(f'<li>{esc(f[k])}</li>' for k in ['contenu'] + [x for x in f if str(x).startswith('valeurs')] if f.get(k))
    notes = ''.join(f'<li>{esc(f[k])}</li>' for k in ['reserve', 'note'] if f.get(k))
    lab = {'CONSTRUCTEUR': 'CONSTRUCTEUR (manufacturer statement, read in the original, not independently verified)',
           'LU': 'LU (read in the original by Claude, not yet cross-checked by a second reader)'}[label]
    body = f'''<h1>Evidence {CODE[i]}</h1>
<p class="small">{esc(f.get('titre', ''))}</p>
<div class="cards">
 <div class="card"><h4>What this evidence shows</h4><p>{esc(summ)}</p></div>
 <div class="card"><h4>Confidence</h4><div class="conf">{conf} %</div><p class="small">{esc(nature)}</p></div>
</div>
<h2>How it was obtained</h2>
<p>The facts were read directly in the source document below, at the location indicated, and recorded in the project register under <code>{esc(i)}</code>.</p>
<table><tr><th>Source document</th><td>{files}</td></tr>
<tr><th>Location in the document</th><td>{esc(f.get('emplacement', ''))}</td></tr>
<tr><th>Date</th><td>{esc(f.get('date', 'not printed'))}</td></tr>
<tr><th>Nature of the source</th><td>{esc(nature)}</td></tr>
<tr><th>Label</th><td>{lab}</td></tr></table>
{('<h2>Quotation (original language)</h2><ul>' + quotes + '</ul>' + trad) if quotes else ''}
<h2>Values and content read</h2><p class="small">As recorded in the project register (in French).</p><ul>{vals}</ul>
{('<h2>Notes</h2><ul>' + notes + '</ul>') if notes else ''}'''
    return page(f'Evidence {CODE[i]}', body, CR())

def calc_page(c):
    f = calcs[c]; conf = calc_conf(c); rows = ''
    for n, e in (f.get('entrees') or {}).items():
        k = e['calc'] if 'calc' in e else e['source']
        h, code = href(k, 1)
        val = calcs[k].get('resultat', '') if 'calc' in e else e['valeur']
        unit = calcs[k].get('unite', '') if 'calc' in e else e.get('unite', '')
        where = calcs[k].get('description', '') if 'calc' in e else e.get('emplacement', '')
        rows += f'<tr><td><code>{esc(n)}</code></td><td>{esc(val)} {esc(unit)}</td><td>{esc(where)}</td><td><span class="ev"><a href="{h}">{code}</a></span></td></tr>'
    body = f'''<h1>Evidence {CODE[c]}</h1>
<p class="small">Calculation</p>
<div class="cards">
 <div class="card"><h4>What this calculation gives</h4><p>{esc(f.get('description', ''))}</p><p class="result" style="margin-top:10px">Result: <strong>{esc(f["resultat"])}</strong> {esc(f.get("unite", ""))}</p></div>
 <div class="card"><h4>Confidence</h4><div class="conf">{conf} %</div><p class="small">Label CALCULÉ. A calculation is rated at its least reliable input, at most 95 %.</p></div>
</div>
<h2>How it was calculated</h2>
<p>The formula below is applied to the inputs listed, each taken from its own evidence sheet. The description of the calculation is recorded in the register in French.</p>
<h3>Formula</h3><pre>{esc(f["formule"])}</pre>
<h3>Inputs</h3>
<table><tr><th>Input</th><th>Value</th><th>Location or description</th><th>Evidence</th></tr>{rows}</table>
<p class="small">Register entry <code>{esc(c)}</code>. The formula is recalculated automatically by the project control script.</p>'''
    return page(f'Evidence {CODE[c]}', body, CR())

DEC_EN = {
 'D-035': 'Reactor capacity of 200 m3 per day; feed density after pressing taken at 0.7 t/m3, i.e. 140 t per day (working assumption of the project sponsor).',
 'D-016': 'OneWorld statements are admitted as a working basis when they appear in a OneWorld document cited with page or date; they are labelled CONSTRUCTEUR, attributed in the text and never presented as independently verified.',
 'D-020': 'OneWorld documentation is used as the design basis of the URC-2000, always attributed.',
 'D-021': 'Energy values of the products and basis of the energy balance (see Annex 2, sheet 2.5.0). The char value and the burner coverage are amended by D-038; the self-sufficiency on household and municipal waste is withdrawn by D-029.',
 'D-022': 'Confidence scale: 100 % for tests filed with the authorities, independent laboratories, legislation and reference data; 95 % for manufacturer documentation, peer-reviewed literature and calculations on such data; 90 % for calculations using a working assumption, manufacturer tables without printed author and patents; 80 % for secondary sources.',
 'D-025': 'The Lufthansa worksheet (Worksheet-Lufthansa-200MT.xlsx) is excluded as a source: author not identified, coefficients without source. Revenues are rebuilt from scratch in Annex 3 and the financial model.',
 'D-026': 'Annex 1 drafting choices by the project sponsor (15 October 2026): dioxins described as very low with the measured values; char positioned as a high-calorific solid fuel (for example blended with coke or coal), not as a fertiliser, with prices in Annex 3; URC-2000 as reference machine; process heat covered by the gas per Annex 2, electricity bought; PVC acceptance subject to the chlorine investigation; no revenue, price or cost figures in this annex.',
 'D-029': 'Gas from plastic, measured by difference (Chiba report, PDF p. 27), taken at 10 % of the incoming plastic mass for mixed waste (working assumption of the project sponsor, 15 October 2026). No energy self-sufficiency is claimed for household or municipal waste; their energy balance is built in Annex 5. Pure resin feeds keep the self-sufficiency shown in Annex 2.',
 'D-038': 'Gas at 37.4 MJ/kg confirmed. Char at two values by feed: 24.6 MJ/kg for char from plastic residues (Chiba factor, origin not stated) and 32.09 MJ/kg for char from household waste (Izumitec, measured on a urethane char). Burner coverage on pure plastic shown on two lines: 2.9 times with 11.5 % gas (OneWorld example) and 3.7 times with 15 % gas (rounded measured value). Amends D-021.',
}
def decisions_page():
    rows = ''.join(f'<h2 id="{d}">{d}. {esc(decs[d].get("titre", ""))}</h2><p>{esc(DEC_EN[d])}</p><p class="small">Dated {esc(decs[d].get("date", ""))}. Full text in French in <code>working-folder/params/_decisions.yaml</code>: « {esc(" ".join(str(decs[d].get("motif", "")).split()))} »</p>' for d in DEC_EN if d in decs)
    body = '''<h1>Decisions and working assumptions</h1>
<div class="cards"><div class="card"><h4>What this sheet shows</h4><p>The dated decisions of the project sponsor on which this annex relies. A figure that depends on a working assumption is capped at 90 % confidence.</p></div>
<div class="card"><h4>Confidence</h4><div class="conf">n/a</div><p class="small">Decisions, not measurements.</p></div></div>''' + rows
    return page('Annex 1. Decisions', body, CR())

def index_page():
    rows = ''
    for g, gt in GROUPS:
        rows += f'<tr><th colspan="3">1.{g} · {esc(gt)}</th></tr>'
        for i in ORDER:
            if not CODE[i].startswith(f'1.{g}.'): continue
            d = SRC1[i][4] if i in SRC1 else calcs[i].get('description', '')
            rows += f'<tr><td><a href="A{CODE[i].replace(".", "-")}.html">{CODE[i]}</a></td><td>{esc(d)}</td><td>{conf_of(i)} %</td></tr>'
    rows += '<tr><th colspan="3">Annex 2 evidence sheets cited in this annex</th></tr>'
    for t in cites:
        k = t[5:] if t.startswith('calc:') else t
        if t.startswith('hyp:') or k in CODE or k not in g2.CODE: continue
        h, code = href(k, 1)
        d = g2.SRC[k][4] if k in g2.SRC else g2.desc(k)
        rows += f'<tr><td><a href="{h}">{code}</a></td><td>{esc(d)}</td><td>{conf_of(k)} %</td></tr>'
    rows += '<tr><th colspan="3">Decisions</th></tr><tr><td><a href="A1-D.html">1.D</a></td><td>Decisions D-016, D-020, D-021, D-022, D-025, D-026, D-029 and D-038</td><td>n/a</td></tr>'
    body = f'''<h1>Annex 1. Evidence sheets</h1>
<p>Each figure or fact of Annex 1 links to one of these sheets. Sheets 1.M, 1.R and 1.C belong to this annex; sheets 2.x are the evidence sheets of Annex 2, used here without duplication.</p>
<h2>Confidence scale</h2>
<table><tr><th>Confidence</th><th>Applies to</th></tr>
<tr><td>100 %</td><td>Tests filed with the authorities, independent laboratory reports, legislation and reference data</td></tr>
<tr><td>95 %</td><td>Manufacturer documentation (OneWorld), institutional and peer-reviewed reports, calculations on data at 95 % or more</td></tr>
<tr><td>90 %</td><td>Calculations using a working assumption, manufacturer material without printed author or with no data (tables, 3D model, animation), patents, reports whose page numbers are still to be confirmed</td></tr>
<tr><td>80 %</td><td>Secondary sources</td></tr></table>
<h2>All sheets</h2><table><tr><th>Sheet</th><th>Content</th><th>Confidence</th></tr>{rows}</table>'''
    return page('Annex 1. Evidence sheets', body, '<p class="crumb"><a href="../index.html">Annex 1. Process and Technology</a></p>')

def figure(m):
    doc, p, cap = m.group(1), int(m.group(2)), m.group(3).strip()
    src = {'ow-eng': os.path.join(WF, 'reference', 'preuves', 'documents-fournis', 'Urban RIg ENG　.pdf')}[doc]
    out = os.path.join(IMAGES, f'{doc}-p{p:02d}.jpg')
    if not os.path.exists(out):
        base = out[:-4]
        subprocess.run(['pdftoppm', '-f', str(p), '-l', str(p), '-r', '90', '-jpeg', '-jpegopt', 'quality=82', '-singlefile', src, base], check=True)
    return f'\n<figure><img src="images/{doc}-p{p:02d}.jpg" alt="{esc(cap)}" loading="lazy"><figcaption>{esc(cap)}</figcaption></figure>\n'

def references_html():
    items = ''
    for t in cites:
        if t.startswith('hyp:'): continue
        k = t[5:] if t.startswith('calc:') else t
        if k in calcs: continue
        f = fiche(k); h, code = href(k, 0)
        items += f'<tr><td><span class="ev"><a href="{h}">{code}</a></span></td><td>{esc(f.get("titre", k))}</td><td>{esc(f.get("emplacement", ""))}</td><td>{conf_of(k)} %</td></tr>'
    return '<table><tr><th>Sheet</th><th>Document</th><th>Location</th><th>Confidence</th></tr>' + items + '</table>'

def main_page():
    s = MD
    s = re.sub(r'\[\[FIG ([a-z\-]+) (\d+) \| ([^\]]+)\]\]\s*nosrc', figure, s)
    s = pills_in(s, 0)
    s = s.replace('All sheets are listed in the index of evidence sheets.', 'All sheets are listed in the <a href="preuves/index.html">index of evidence sheets</a>.')
    s = s.replace('The full list of documents cited, with their location and confidence, is in the index of evidence sheets.',
                  'Documents cited in this annex, with their location and confidence. The full list of sheets is in the <a href="preuves/index.html">index of evidence sheets</a>.\n\nREFERENCES_TABLE')
    s = re.sub(r'(?m)^((?!- |\d+\. |\s|\|)[^\n]+)\n(- |\d+\. )', r'\1\n\n\2', s)
    body = markdown.markdown(s, extensions=['tables', 'sane_lists'])
    body = body.replace('<p>REFERENCES_TABLE</p>', references_html())
    left = re.findall(r'\[(?:calc:|hyp:)?[A-Z0-9][A-Z0-9\-]+\]', body)
    return page('Annex 1. Process and Technology', body), left

if __name__ == '__main__':
    mp, left = main_page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(mp)
    for i in ORDER:
        open(os.path.join(PREUVES, f'A{CODE[i].replace(".", "-")}.html'), 'w', encoding='utf-8').write(source_page(i) if i in SRC1 else calc_page(i))
    open(os.path.join(PREUVES, 'A1-D.html'), 'w', encoding='utf-8').write(decisions_page())
    open(os.path.join(PREUVES, 'index.html'), 'w', encoding='utf-8').write(index_page())
    sans = [t for t in cites if not t.startswith('hyp:') and href(t[5:] if t.startswith('calc:') else t, 0)[0] is None]
    print('fiches annexe 1 :', len(ORDER) + 2, '; renvois annexe 2 :', len([t for t in cites if (t[5:] if t.startswith('calc:') else t) in g2.CODE]),
          '; citations sans fiche :', sans, '; marqueurs non convertis :', left[:5])
