"""
Genere une page HTML autonome avec 4 onglets :
  Tab 1 - Hypotheses     : parametres editables par domaine, sliders, valeurs de reference
  Tab 2 - Resultats      : compte de resultat par annee + KPI cles, tout recalcule en live
  Tab 3 - Bilan matiere  : flux physiques (tonnages, energie, eau, carbone)
  Tab 4 - Confiance      : parametres faibles, arbres de justification, preuves, decisions

Le moteur JavaScript embarque (engine/moteur.js) est un port exact de modele.py.
La page verifie cette egalite au chargement et affiche un bandeau rouge si elle est rompue.
Aucune dependance, aucun serveur. Un seul fichier HTML autonome.
"""
import html
import json
from datetime import date
from pathlib import Path

MOTEUR_JS = (Path(__file__).resolve().parent / "moteur.js").read_text(encoding="utf-8")


def _json(o):
    return json.dumps(o, ensure_ascii=False, default=str)


FIABILITE = {
    "certifie_tiers": ("Certifie par un tiers", "ok"),
    "mesure_interne":  ("Mesure interne", "ok"),
    "constructeur":    ("Constructeur", "moyen"),
    "litterature":     ("Litterature", "moyen"),
    "aucune":          ("Aucune preuve", "faible"),
}
RANG = list(FIABILITE)

LIBELLES = {
    "tonnage_annuel": "Tonnage annuel traite",
    "debit_massique": "Debit massique",
    "huile": "Huile produite", "char": "Char commercialisable",
    "ferreux": "Ferreux", "aluminium": "Aluminium", "autres_metaux": "Autres metaux",
    "verre": "Verre", "residus": "Residus a eliminer",
    "eau_procede": "Eau de procede", "eau_douce": "Eau douce recuperee",
    "concentrat": "Concentrat a eliminer",
    "phase_organique_decantee": "Phase organique decantee",
    "energie_gaz_disponible": "Energie du gaz de procede",
    "couverture_thermique": "Couverture thermique",
    "fioul_litres_jour": "Fioul de secours (L/j)", "fioul_annuel": "Fioul annuel",
    "energie_exportee": "Energie exportee",
    "surface_batie": "Surface batie",
    "capex_equipement": "CAPEX equipement", "capex_genie_civil": "CAPEX genie civil",
    "capex_total": "CAPEX total", "capex_par_tonne_an": "CAPEX par tonne annuelle",
    "amortissement_annuel": "Amortissement annuel",
    "dette": "Dette", "fonds_propres": "Fonds propres",
    "ebitda_an3": "EBITDA annee 3", "marge_ebitda_an3": "Marge EBITDA annee 3",
    "gate_fee_equilibre": "Gate fee d'equilibre (NPV = 0)",
    "carbone_fossile_entrant": "Carbone fossile entrant",
    "emissions_directes_site": "Emissions directes du site",
    "intensite_carbone_site": "Intensite carbone du site",
    "carbone_sortant_produits": "Carbone sortant dans les produits",
    "carbone_stocke": "Carbone stocke",
    "ecart_bouclage_carbone": "Ecart de bouclage du bilan carbone",
}

LIGNES_PL = [
    ("recettes",              "RECETTES",                   True),
    ("rec_gate_fees",         "Gate fees",                  False),
    ("rec_huile",             "Huile",                      False),
    ("rec_char",              "Char",                       False),
    ("rec_metaux",            "Metaux",                     False),
    ("rec_verre",             "Verre",                      False),
    ("rec_carbone",           "Credits carbone",            False),
    ("charges",               "CHARGES",                    True),
    ("ch_personnel",          "Personnel",                  False),
    ("ch_maintenance",        "Maintenance",                False),
    ("ch_electricite",        "Electricite",                False),
    ("ch_fioul_secours",      "Fioul de secours",           False),
    ("ch_elimination_residus","Elimination des residus",    False),
    ("ch_carbonate",          "Carbonate de calcium",       False),
    ("ch_concentrat",         "Elimination du concentrat",  False),
    ("ch_couche_catalytique", "Couche catalytique halogenes",False),
    ("ch_ceramique_seacoral", "Ceramique SEA CORAL",        False),
    ("ch_charbon_actif",      "Charbon actif",              False),
    ("ch_assurance",          "Assurance",                  False),
    ("ch_provision_divers",   "Provision et divers",        False),
    ("ebitda",                "EBITDA",                     True),
    ("amortissement",         "Amortissement",              False),
    ("interets",              "Interets",                   False),
    ("resultat_avant_impot",  "Resultat avant impot",       False),
    ("impot",                 "Impot",                      False),
    ("resultat_net",          "RESULTAT NET",               True),
    ("flux_libre",            "Flux libre",                 False),
    ("flux_cumule",           "Flux cumule",                True),
]

KPI_CLES = [
    "tonnage_annuel", "capex_total", "capex_par_tonne_an",
    "ebitda_an3", "marge_ebitda_an3", "gate_fee_equilibre",
    "couverture_thermique", "intensite_carbone_site", "ecart_bouclage_carbone",
]

FLUX_MATIERE = [
    "huile", "char", "ferreux", "aluminium", "autres_metaux", "verre",
    "residus", "eau_procede", "eau_douce", "concentrat",
    "energie_exportee", "fioul_litres_jour", "emissions_directes_site",
    "carbone_fossile_entrant", "carbone_sortant_produits", "carbone_stocke",
]

CSS = """
/* ---------- tokens ---------- */
:root {
  --bg:       #f5f6f8;
  --surface:  #ffffff;
  --border:   #e2e5ea;
  --fg:       #1a1d23;
  --fg2:      #5a6472;
  --fg3:      #8a939f;
  --accent:   #1f3864;
  --accent2:  #2d5299;
  --tab-act:  #1f3864;
  --ok-bg:    #e4f3e6; --ok-fg:    #1d6b2c;
  --warn-bg:  #fdf1dd; --warn-fg:  #8a5a08;
  --bad-bg:   #fbe2e0; --bad-fg:   #9e2418;
  --plus-c:   #1d6b2c; --moins-c:  #9e2418;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:       #0f1117;
    --surface:  #1a1d23;
    --border:   #2d3240;
    --fg:       #e8eaf0;
    --fg2:      #9aa3b2;
    --fg3:      #5a6472;
    --accent:   #2d5299;
    --accent2:  #4a7cc4;
    --tab-act:  #2d5299;
    --ok-bg:    #1a3320; --ok-fg:    #5ac87e;
    --warn-bg:  #2d2010; --warn-fg:  #d4a044;
    --bad-bg:   #2d1515; --bad-fg:   #e07070;
    --plus-c:   #5ac87e; --moins-c:  #e07070;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg:       #0f1117;
  --surface:  #1a1d23;
  --border:   #2d3240;
  --fg:       #e8eaf0;
  --fg2:      #9aa3b2;
  --fg3:      #5a6472;
  --accent:   #2d5299;
  --accent2:  #4a7cc4;
  --tab-act:  #2d5299;
  --ok-bg:    #1a3320; --ok-fg:    #5ac87e;
  --warn-bg:  #2d2010; --warn-fg:  #d4a044;
  --bad-bg:   #2d1515; --bad-fg:   #e07070;
  --plus-c:   #5ac87e; --moins-c:  #e07070;
  color-scheme: dark;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font: 14px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: var(--fg); background: var(--bg); padding-inline: 0; min-height: 100%;
}
a { color: var(--accent2); text-decoration: none; }
a:hover { text-decoration: underline; }
.app { display: flex; flex-direction: column; min-height: 100%; }
header {
  background: var(--accent); color: #fff; padding: 18px 24px 0;
  position: sticky; top: env(safe-area-inset-top, 0px); z-index: 40;
}
.header-top { display: flex; align-items: baseline; gap: 16px; flex-wrap: wrap; margin-bottom: 14px; }
header h1 { font-size: 17px; font-weight: 700; letter-spacing: -.01em; }
header .sub { font-size: 12px; opacity: .75; }
.tabs { display: flex; gap: 2px; }
.tab {
  padding: 9px 18px 10px; font-size: 13px; font-weight: 600;
  color: rgba(255,255,255,.65); border: none; background: none; cursor: pointer;
  border-bottom: 3px solid transparent; transition: color .15s, border-color .15s; white-space: nowrap;
}
.tab:hover { color: rgba(255,255,255,.9); }
.tab.actif { color: #fff; border-bottom-color: #fff; }
#autocontrole { padding: 8px 20px; font-size: 12px; font-weight: 600; display: none; }
#autocontrole.rouge { display: block; background: var(--bad-bg); color: var(--bad-fg); }
#autocontrole.vert  { display: block; background: var(--ok-bg);  color: var(--ok-fg);  }
.statusbar {
  background: var(--surface); border-bottom: 1px solid var(--border);
  padding: 7px 20px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
  font-size: 12px; color: var(--fg2); position: sticky;
  top: calc(env(safe-area-inset-top, 0px) + 96px); z-index: 30;
}
.btn {
  padding: 4px 12px; border-radius: 5px; font-size: 12px; font-weight: 600; cursor: pointer;
  border: 1px solid var(--accent); background: var(--accent); color: #fff; transition: opacity .15s;
}
.btn:hover { opacity: .85; }
.btn.sec { background: transparent; color: var(--accent); }
#compteur { font-weight: 600; color: var(--fg); }
.panel { display: none; padding: 20px; max-width: 1200px; margin: 0 auto; width: 100%; }
.panel.actif { display: block; }
.section {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 8px; margin-bottom: 18px; overflow: hidden;
}
.section > h2 {
  margin: 0; padding: 12px 16px; font-size: 13px; font-weight: 700;
  text-transform: uppercase; letter-spacing: .05em; color: var(--fg2);
  background: var(--bg); border-bottom: 1px solid var(--border);
}
.inner { padding: 16px; }
.kpi-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px,1fr)); gap: 12px; }
.kpi {
  border: 1px solid var(--border); border-radius: 7px; padding: 12px 14px;
  background: var(--surface); cursor: pointer; transition: border-color .15s;
}
.kpi:hover { border-color: var(--accent2); }
.kpi .label { font-size: 11px; color: var(--fg2); text-transform: uppercase; letter-spacing: .04em; }
.kpi .val { font-size: 22px; font-weight: 700; margin: 4px 0 2px; font-variant-numeric: tabular-nums; letter-spacing: -.02em; }
.kpi .footer { display: flex; align-items: center; gap: 8px; }
.tbl-wrap { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: 13px; font-variant-numeric: tabular-nums; }
th, td { padding: 7px 10px; border-bottom: 1px solid var(--border); text-align: right; }
th:first-child, td:first-child { text-align: left; }
thead th {
  background: var(--bg); font-weight: 700; font-size: 11px;
  text-transform: uppercase; letter-spacing: .04em; color: var(--fg2); position: sticky; top: 0;
}
tr.fort td { font-weight: 700; background: var(--bg); }
tr:last-child td { border-bottom: none; }
.cliq { cursor: pointer; border-bottom: 1px dotted var(--fg3); }
.cliq:hover { background: var(--warn-bg); }
details { margin-bottom: 10px; }
summary {
  cursor: pointer; font-size: 13px; font-weight: 700; padding: 9px 12px;
  background: var(--bg); border: 1px solid var(--border); border-radius: 6px;
  display: flex; justify-content: space-between; align-items: center;
  list-style: none; user-select: none;
}
summary::-webkit-details-marker { display: none; }
summary::after { content: "▸"; font-size: 11px; color: var(--fg3); }
details[open] summary::after { content: "▾"; }
.param-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px,1fr)); gap: 10px; padding: 12px; }
.param-card {
  border: 1px solid var(--border); border-radius: 6px; padding: 10px 12px;
  background: var(--surface); transition: border-color .2s, background .2s;
}
.param-card.modifie { border-color: #c98a00; background: var(--warn-bg); }
.param-card label { display: block; font-size: 11px; color: var(--fg2); margin-bottom: 6px; }
.param-card .label-top { display: flex; justify-content: space-between; align-items: center; gap: 4px; }
.param-card .arbre-lien { font-size: 10px; }
.param-card input[type=number], .param-card select {
  width: 100%; padding: 5px 8px; border: 1px solid var(--border); border-radius: 4px;
  background: var(--bg); color: var(--fg); font: inherit; font-size: 13px;
}
.param-card input[type=range] { width: 100%; margin-top: 6px; accent-color: var(--accent2); }
.range-bounds { display: flex; justify-content: space-between; font-size: 10px; color: var(--fg3); margin-top: 2px; }
.refs { margin-top: 6px; display: flex; flex-wrap: wrap; gap: 4px; }
.ref {
  display: inline-block; padding: 2px 8px; font-size: 10px; border-radius: 10px;
  background: var(--bg); border: 1px solid var(--border); cursor: pointer; color: var(--fg2);
}
.ref:hover { border-color: var(--accent2); color: var(--accent2); }
.ref.actif { background: var(--accent); border-color: var(--accent); color: #fff; }
.pill { display: inline-block; padding: 1px 7px; border-radius: 10px; font-size: 11px; font-weight: 700; }
.ok    { background: var(--ok-bg);   color: var(--ok-fg);   }
.moyen { background: var(--warn-bg); color: var(--warn-fg); }
.faible{ background: var(--bad-bg);  color: var(--bad-fg);  }
.conf { font-weight: 700; font-size: 11px; padding: 2px 7px; border-radius: 10px; white-space: nowrap; }
.c100 { background: #1d6b2c; color: #fff; }
.c90  { background: #4c9a5a; color: #fff; }
.c80  { background: #c98a00; color: #fff; }
.c60  { background: #d9731a; color: #fff; }
.c0   { background: #9e2418; color: #fff; }
.discuter { font-size: 10px; color: var(--warn-fg); font-style: italic; }
.delta { font-size: 11px; font-weight: 700; }
.delta.plus  { color: var(--plus-c); }
.delta.moins { color: var(--moins-c); }
.arbre { list-style: none; padding-left: 0; margin: 0; }
.arbre ul { list-style: none; padding-left: 16px; margin: 4px 0 4px 6px; border-left: 2px solid var(--border); }
.arbre li { margin: 4px 0; }
.noeud {
  display: flex; gap: 8px; align-items: flex-start; padding: 8px 10px;
  border: 1px solid var(--border); border-radius: 6px; background: var(--surface); cursor: pointer;
}
.noeud:hover { border-color: var(--accent2); }
.noeud .txt { flex: 1; min-width: 0; font-size: 13px; }
.noeud .base { font-size: 10px; color: var(--fg3); margin-top: 2px; }
.contre .noeud { border-color: var(--bad-bg); background: var(--bad-bg); }
.feuille {
  font-size: 12px; padding: 6px 10px; border-left: 3px solid var(--accent2);
  background: var(--bg); margin: 4px 0; cursor: pointer; border-radius: 0 4px 4px 0;
}
.feuille:hover { background: var(--warn-bg); }
#panneau {
  position: fixed; top: 0; right: -560px; width: 560px; max-width: 94vw;
  height: 100%; background: var(--surface); box-shadow: -4px 0 28px rgba(0,0,0,.18);
  transition: right .22s ease; overflow-y: auto; z-index: 100;
}
#panneau.ouvert { right: 0; }
.pan-tete { background: var(--accent); color: #fff; padding: 16px 20px; }
.pan-tete h3 { font-size: 15px; margin: 0; }
.pan-tete .pan-val { opacity: .85; font-size: 13px; margin-top: 4px; }
.fermer {
  position: absolute; top: 13px; right: 16px; color: #fff; cursor: pointer;
  font-size: 24px; line-height: 1; background: none; border: none; padding: 0;
}
.pan-corps { padding: 18px 20px; }
.pan-corps h4 {
  margin: 18px 0 8px; font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: var(--fg3);
}
.pan-corps h4:first-child { margin-top: 0; }
.bloc-preuve {
  border-left: 3px solid var(--border); padding: 8px 12px;
  background: var(--bg); margin-bottom: 8px; border-radius: 0 4px 4px 0; font-size: 13px;
}
.bloc-dec { border-left-color: var(--accent2); }
.note { font-size: 11px; color: var(--fg3); margin-top: 4px; }
.res { color: var(--bad-fg); font-style: italic; }
.cible { font-size: 12px; background: var(--ok-bg); color: var(--ok-fg); padding: 6px 10px; border-radius: 4px; margin-top: 6px; }
.legend { font-size: 11px; color: var(--fg3); margin-bottom: 12px; line-height: 1.6; }
@media (max-width: 600px) {
  .tabs .tab { padding: 8px 12px; font-size: 12px; }
  .kpi-grid { grid-template-columns: 1fr 1fr; }
  .kpi .val { font-size: 18px; }
}
"""

JS_UI = r"""
const D = __DONNEES__;
const P0 = JSON.parse(JSON.stringify(D.params));
let P = JSON.parse(JSON.stringify(D.params));
let RES = null, PL = null, BASE = null;

const nf = (v, d=0) => v.toLocaleString('fr-FR', {minimumFractionDigits:d, maximumFractionDigits:d});
function fmt(v, u) {
  if (typeof v === 'string') return v + ' ' + (u||'');
  if (u === 'fraction') return nf(v*100, 1) + ' %';
  return (Math.abs(v) >= 1000 ? nf(v,0) : nf(v,2)) + ' ' + (u||'');
}

function activerTab(id) {
  document.querySelectorAll('.tab').forEach(t => t.classList.toggle('actif', t.dataset.tab === id));
  document.querySelectorAll('.panel').forEach(p => p.classList.toggle('actif', p.id === 'tab-'+id));
  try { localStorage.setItem('ur_tab', id); } catch(e) {}
}
document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => activerTab(t.dataset.tab)));
(function(){
  let last; try { last = localStorage.getItem('ur_tab'); } catch(e) {}
  activerTab(last || 'hypotheses');
})();

function recalculer() {
  const r = calculer(P); RES = r.R; PL = r.pl;
  if (!BASE) BASE = JSON.parse(JSON.stringify(RES));
  peindre();
}

function peindre() {
  document.querySelectorAll('[data-res]').forEach(e => {
    const k = e.dataset.res; if (!RES[k]) return;
    e.textContent = fmt(RES[k].valeur, RES[k].unite);
  });
  document.querySelectorAll('[data-delta]').forEach(e => {
    const k = e.dataset.delta; if (!BASE[k] || !RES[k]) return;
    const a = BASE[k].valeur, b = RES[k].valeur;
    if (typeof a !== 'number' || Math.abs(a) < 1e-12) { e.textContent = ''; return; }
    const d = (b/a - 1) * 100;
    if (Math.abs(d) < 0.05) { e.textContent = ''; e.className = 'delta'; return; }
    e.textContent = (d > 0 ? '+' : '') + nf(d, 1) + ' %';
    e.className = 'delta ' + (d > 0 ? 'plus' : 'moins');
  });
  document.querySelectorAll('[data-pl]').forEach(e => {
    const [c, a] = e.dataset.pl.split('|');
    e.textContent = nf(PL[+a][c], 0);
  });
  let mod = 0;
  Object.keys(P).forEach(k => {
    const chg = P[k].valeur !== P0[k].valeur;
    if (chg) mod++;
    const b = document.querySelector(`[data-box="${k}"]`);
    if (b) b.classList.toggle('modifie', chg);
    document.querySelectorAll(`[data-refv="${k}"]`).forEach(e =>
      e.classList.toggle('actif', parseFloat(e.dataset.v) === P[k].valeur));
  });
  const c = document.getElementById('compteur');
  if (c) c.textContent = mod ? mod + ' parametre(s) modifie(s)' : 'Valeurs de reference';
}

function changer(k, val) {
  if (typeof P0[k].valeur === 'number') {
    val = parseFloat(val); if (isNaN(val)) return;
    const b = D.bornes[k]; if (b) val = Math.min(b.haut, Math.max(b.bas, val));
  }
  P[k].valeur = val;
  const inp = document.querySelector(`[data-inp="${k}"]`);
  const sld = document.querySelector(`[data-sld="${k}"]`);
  if (inp && inp.value != val) inp.value = val;
  if (sld && sld.value != val) sld.value = val;
  recalculer();
}

function reinitialiser() {
  P = JSON.parse(JSON.stringify(P0));
  Object.keys(P).forEach(k => {
    const i = document.querySelector(`[data-inp="${k}"]`); if (i) i.value = P[k].valeur;
    const s = document.querySelector(`[data-sld="${k}"]`); if (s) s.value = P[k].valeur;
  });
  recalculer();
}

function champHTML(k) {
  const q = D.meta[k], v = P[k].valeur, b = D.bornes[k];
  if (D.choix[k]) {
    return `<select data-inp="${k}" onchange="changer('${k}',this.value)">` +
      D.choix[k].map(o => `<option value="${o}" ${o===v?'selected':''}>${o}</option>`).join('') + `</select>`;
  }
  let h = `<div style="display:flex;gap:6px;align-items:center;margin-top:4px">
    <input type="number" step="any" data-inp="${k}" value="${v}"
      oninput="changer('${k}',this.value)" style="flex:1">
    <span style="font-size:11px;color:var(--fg3);white-space:nowrap">${q.unite||''}</span></div>`;
  if (b) {
    const pas = (b.haut - b.bas) / 200;
    h += `<input type="range" data-sld="${k}" min="${b.bas}" max="${b.haut}" step="${pas}"
      value="${v}" oninput="changer('${k}',this.value)">
      <div class="range-bounds"><span>${b.bas}</span><span>${b.haut}</span></div>`;
  }
  if (D.refs[k]) {
    h += `<div class="refs">` + D.refs[k].map(r =>
      `<span class="ref ${parseFloat(r.valeur)===v?'actif':''}" data-refv="${k}" data-v="${r.valeur}"
        onclick="changer('${k}',${r.valeur})">${r.libelle} : ${r.valeur}</span>`
    ).join('') + `</div>`;
  }
  return h;
}

function fermer() { document.getElementById('panneau').classList.remove('ouvert'); }
document.addEventListener('keydown', e => { if (e.key === 'Escape') fermer(); });

function ouvrir(cle) {
  const r = RES[cle]; if (!r) return;
  const lab = D.libelles[cle] || cle;
  const p = document.getElementById('panneau');
  let h = `<div class="pan-tete"><button class="fermer" onclick="fermer()">&#x2715;</button>
    <h3>${lab}</h3><div class="pan-val">${fmt(r.valeur, r.unite)}</div></div><div class="pan-corps">`;
  h += `<h4>Parametres qui entrent dans ce calcul</h4>`;
  if (!r.depend.length) { h += `<div class="note">Grandeur derivee d'autres resultats.</div>`; }
  r.depend.slice().sort().forEach(k => {
    const q = D.meta[k]; const cf = D.confP[k];
    h += `<div class="bloc-preuve"><b>${q.label}</b> ${pastilleConf(cf.c)}
      ${cf.instruit ? '' : '<span class="discuter">non instruit</span>'}
      ${q.justification ? `<div class="note"><a href="#" onclick="voirJust('${q.justification}');return false;">&#9656; Arbre de justification</a></div>` : ''}
      <div style="margin-top:6px">${champHTML(k)}</div>
      <div class="note">Statut : ${q.statut||'—'}</div>`;
    if (q.note) h += `<div class="note">${q.note}</div>`;
    if (q.decision) h += `<div class="note">Decision : <a href="#" onclick="voirDec('${q.decision}');return false;">${q.decision}</a></div>`;
    if (q.preuves && q.preuves.length)
      h += `<div class="note">Preuves : ` + q.preuves.map(x =>
        `<a href="#" onclick="voirPr('${x}');return false;">${x}</a>`).join(', ') + `</div>`;
    h += `</div>`;
  });
  p.innerHTML = h + `</div>`; p.classList.add('ouvert');
  document.querySelectorAll('[data-champ]').forEach(e => { e.innerHTML = champHTML(e.dataset.champ); });
  peindre();
}

function voirDec(id) {
  const d = D.decisions[id]; const p = document.getElementById('panneau');
  p.innerHTML = `<div class="pan-tete"><button class="fermer" onclick="fermer()">&#x2715;</button>
    <h3>${id} — ${d.titre}</h3><div class="pan-val">${d.date}</div></div><div class="pan-corps">
    <h4>Changement</h4><div class="bloc-preuve bloc-dec">${d.de} &rarr; ${d.vers} ${d.unite||''}</div>
    <h4>Motif</h4><div class="bloc-preuve">${d.motif}</div>
    ${d.a_verifier ? `<h4>Reste a verifier</h4><div class="bloc-preuve res">${d.a_verifier}</div>` : ''}
    <h4>Preuves</h4>` +
    (d.preuves||[]).map(x => `<div class="bloc-preuve"><a href="#" onclick="voirPr('${x}');return false;">${x}</a></div>`).join('')
    + `</div>`;
  p.classList.add('ouvert');
}

function voirPr(id) {
  const e = D.preuves[id]; const p = document.getElementById('panneau');
  const f = D.fiabPreuve[id];
  let h = `<div class="pan-tete"><button class="fermer" onclick="fermer()">&#x2715;</button>
    <h3>${e.titre}</h3><div class="pan-val">${id} &middot; ${e.type}</div></div>
    <div class="pan-corps"><h4>Fiabilite</h4>
    <div class="bloc-preuve"><span class="pill ${f.classe}">${f.libelle}</span></div>`;
  if (e.contenu) h += `<h4>Contenu</h4><div class="bloc-preuve">${e.contenu}</div>`;
  if (e.chemin) h += `<h4>Emplacement</h4><div class="bloc-preuve"><code>${e.chemin}</code></div>`;
  if (e.reserve) h += `<h4>Reserve</h4><div class="bloc-preuve res">${e.reserve}</div>`;
  const dep = D.usage[id]||[];
  h += `<h4>Valeurs qui en dependent (${dep.length})</h4>`;
  h += dep.length ? dep.map(k => `<div class="bloc-preuve">${D.meta[k].label}</div>`).join('')
                  : `<div class="note">Aucune.</div>`;
  p.innerHTML = h + `</div>`; p.classList.add('ouvert');
}

function classeConf(c) { return c>=0.999?'c100':c>=0.9?'c90':c>=0.8?'c80':c>=0.6?'c60':'c0'; }
function pastilleConf(c) { return `<span class="conf ${classeConf(c)}">${Math.round(c*100)}&nbsp;%</span>`; }

function brancheHTML(aid, profondeur, vus) {
  const a = D.justifs[aid]; if (!a) return '';
  if (vus.has(aid)) return `<li><div class="feuille" onclick="voirJust('${aid}')">&#8618; ${aid} (deja developpe)</div></li>`;
  vus.add(aid);
  const c = D.confJ[aid];
  let h = `<li><div class="noeud" onclick="voirJust('${aid}')">
    ${pastilleConf(c)}
    <div class="txt">${a.enonce}
    <div class="base">${aid} &middot; ${a.base}
      ${D.aDiscuter.includes(a.base) ? ' &middot; <span class="discuter">a discuter</span>' : ''}
      ${a.appuis&&a.appuis.length ? ' &middot; ' + (a.mode==='un_suffit'?'un appui suffit':'tous requis') : ''}
    </div></div></div>`;
  const enfants = [];
  (a.appuis||[]).forEach(x => enfants.push(brancheHTML(x, profondeur+1, vus)));
  (a.preuves||[]).forEach(pp => {
    const ev = D.preuves[pp]; if (!ev) return;
    enfants.push(`<li><div class="feuille" onclick="event.stopPropagation();voirPr('${pp}')">
      &#128196; <b>${pp}</b> &middot; ${ev.titre}
      <span class="pill ${D.fiabPreuve[pp].classe}">${D.fiabPreuve[pp].libelle}</span>
    </div></li>`);
  });
  if (enfants.length) h += `<ul>${enfants.join('')}</ul>`;
  if (a.contre_indications && a.contre_indications.length) {
    h += `<ul class="contre"><li style="font-size:10px;color:var(--bad-fg);font-weight:700;margin:6px 0 2px">CONTRE-INDICATIONS</li>` +
      a.contre_indications.map(x => brancheHTML(x, profondeur+1, vus)).join('') + `</ul>`;
  }
  return h + `</li>`;
}

function voirJust(aid) {
  const a = D.justifs[aid]; const p = document.getElementById('panneau');
  const c = D.confJ[aid];
  let h = `<div class="pan-tete"><button class="fermer" onclick="fermer()">&#x2715;</button>
    <h3>${a.enonce}</h3>
    <div style="margin-top:8px">${pastilleConf(c)}
    <span style="opacity:.8;font-size:11px;margin-left:6px">${aid} &middot; ${a.base}</span></div></div>
    <div class="pan-corps">`;
  if (a.detail) h += `<h4>Detail</h4><div class="bloc-preuve">${a.detail}</div>`;
  if (a.consequence) h += `<h4>Consequence</h4><div class="bloc-preuve bloc-dec">${a.consequence}</div>`;
  if (a.pour_passer_a_1 && c < 0.999) h += `<h4>Pour atteindre 100 %</h4><div class="cible">${a.pour_passer_a_1}</div>`;
  h += `<h4>Arbre de justification</h4><ul class="arbre">${brancheHTML(aid, 0, new Set())}</ul>`;
  const parents = Object.keys(D.justifs).filter(k => (D.justifs[k].appuis||[]).includes(aid));
  const params = Object.keys(D.meta).filter(k => D.meta[k].justification === aid);
  if (parents.length || params.length) {
    h += `<h4>Utilise par</h4>`;
    params.forEach(k => h += `<div class="bloc-preuve">Parametre : <b>${D.meta[k].label}</b></div>`);
    parents.forEach(k => h += `<div class="bloc-preuve" style="cursor:pointer" onclick="voirJust('${k}')">&#8593; ${D.justifs[k].enonce}</div>`);
  }
  p.innerHTML = h + `</div>`; p.classList.add('ouvert');
}

(function(){
  const r = calculer(JSON.parse(JSON.stringify(P0))).R;
  let max = 0, pire = '';
  for (const k in D.reference) {
    if (!(k in r)) continue;
    const a = D.reference[k], b = r[k].valeur;
    if (typeof a !== 'number') continue;
    const e = Math.abs(a) > 1e-9 ? Math.abs(b/a - 1) : Math.abs(b - a);
    if (e > max) { max = e; pire = k; }
  }
  const el = document.getElementById('autocontrole');
  if (max < 1e-9) {
    el.className = 'vert';
    el.textContent = 'Autocontrole OK : le moteur JS reproduit exactement le moteur Python.';
  } else {
    el.className = 'rouge';
    el.textContent = 'AUTOCONTROLE EN ECHEC : ecart de ' + (max*100).toFixed(4) + ' % sur ' + pire + '. Ne pas utiliser ces chiffres.';
  }
})();

document.querySelectorAll('[data-champ]').forEach(e => { e.innerHTML = champHTML(e.dataset.champ); });
recalculer();
"""


def _fiab(preuves, registre):
    if not preuves:
        return "aucune"
    rangs = [RANG.index(registre[p]["fiabilite"]) for p in preuves if p in registre]
    return RANG[min(rangs)] if rangs else "aucune"


def generer(reg, m, chemin, surcharges=None):
    usage = {}
    meta, bornes, refs, choix, valeurs = {}, {}, {}, {}, {}
    for k, p in reg.params.items():
        meta[k] = {kk: p.get(kk) for kk in
                   ("label", "unite", "statut", "note", "decision", "preuves", "justification")}
        meta[k]["domaine"] = p["_domaine"]
        valeurs[k] = {"valeur": p["valeur"]}
        if p.get("bornes"):
            bornes[k] = p["bornes"]
        if p.get("valeurs_reference"):
            refs[k] = p["valeurs_reference"]
        if isinstance(p["valeur"], str):
            choix[k] = ["craqueur", "combustible"] if k == "qualite_huile" else [p["valeur"]]
        for pr in p.get("preuves", []):
            usage.setdefault(pr, []).append(k)

    fiab = {k: dict(zip(("libelle", "classe"), FIABILITE[_fiab(p.get("preuves", []), reg.preuves)]))
            for k, p in reg.params.items()}
    fiab_preuve = {k: dict(zip(("libelle", "classe"), FIABILITE[e["fiabilite"]]))
                   for k, e in reg.preuves.items()}
    conf_j = {aid: reg.confiance_affirmation(aid) for aid in reg.justifs}
    conf_p = {}
    for k in reg.params:
        c, inst = reg.confiance_parametre(k)
        conf_p[k] = {"c": c, "instruit": inst}
    from engine.modele import A_DISCUTER
    donnees = {
        "justifs": reg.justifs, "confJ": conf_j, "confP": conf_p,
        "aDiscuter": sorted(A_DISCUTER),
        "params": valeurs, "meta": meta, "bornes": bornes, "refs": refs, "choix": choix,
        "libelles": LIBELLES, "decisions": reg.decisions, "preuves": reg.preuves,
        "fiab": fiab, "fiabPreuve": fiab_preuve, "usage": usage,
        "reference": {k: v["valeur"] for k, v in m.r.items()},
    }

    tab_hypotheses = ""
    for domaine, cles in reg.domaines.items():
        champs = ""
        for k in cles:
            p = reg.params[k]
            c, inst = reg.confiance_parametre(k)
            cl = ("c100" if c >= 0.999 else "c90" if c >= 0.9 else
                  "c80" if c >= 0.8 else "c60" if c >= 0.6 else "c0")
            lien = (f'<a class="arbre-lien" href="#" onclick="voirJust(\'{p["justification"]}\');return false;">arbre</a>'
                    if p.get("justification") else
                    '<span class="discuter">non instruit</span>')
            champs += (
                f'<div class="param-card" data-box="{k}">'
                f'<label><div class="label-top">'
                f'<span>{html.escape(p["label"])}</span>'
                f'<div style="display:flex;gap:4px;align-items:center">'
                f'<span class="conf {cl}">{round(c*100)}&nbsp;%</span>{lien}</div></div></label>'
                f'<div data-champ="{k}"></div></div>'
            )
        nb = len(cles)
        tab_hypotheses += (
            f'<details><summary>{html.escape(domaine)}'
            f'<span style="font-size:11px;font-weight:400;color:var(--fg3)">{nb} parametre(s)</span>'
            f'</summary><div class="param-grid">{champs}</div></details>'
        )

    kpi_html = ""
    for k in KPI_CLES:
        if k not in m.r:
            continue
        pires = [fiab[q]["classe"] for q in m.r[k]["depend"] if q in fiab]
        cl = "faible" if "faible" in pires else ("moyen" if "moyen" in pires else "ok")
        lib = {"faible": "preuve faible", "moyen": "preuve moyenne", "ok": "preuve solide"}[cl]
        kpi_html += (
            f'<div class="kpi" onclick="ouvrir(\'{k}\')">'
            f'<div class="label">{LIBELLES.get(k,k)}</div>'
            f'<div class="val" data-res="{k}"></div>'
            f'<div class="footer"><span class="pill {cl}">{lib}</span>'
            f'<span class="delta" data-delta="{k}"></span></div></div>'
        )

    nb = min(10, len(m.pl))
    thead_pl = "<tr><th>Ligne</th>" + "".join(f"<th>An {i+1}</th>" for i in range(nb)) + "</tr>"
    corps_pl = ""
    for cle, lib, fort in LIGNES_PL:
        if cle not in m.pl[0]:
            continue
        cls = ' class="fort"' if fort else ""
        corps_pl += f"<tr{cls}><td>{html.escape(lib)}</td>"
        for i in range(nb):
            corps_pl += f'<td data-pl="{cle}|{i}"></td>'
        corps_pl += "</tr>"

    bilan_html = ""
    for k in FLUX_MATIERE:
        if k not in m.r:
            continue
        bilan_html += (
            f'<tr><td class="cliq" onclick="ouvrir(\'{k}\')">{LIBELLES.get(k,k)}</td>'
            f'<td data-res="{k}"></td><td data-delta="{k}"></td></tr>'
        )

    faibles_html = ""
    for k, p in sorted(reg.params.items(),
                        key=lambda x: (-RANG.index(_fiab(x[1].get("preuves",[]), reg.preuves)),
                                       x[1]["_domaine"])):
        f = _fiab(p.get("preuves", []), reg.preuves)
        if RANG.index(f) < len(RANG) - 2:
            continue
        lib, cl = FIABILITE[f]
        faibles_html += (
            f'<tr><td>{html.escape(p["label"])}</td>'
            f'<td style="text-align:left">{html.escape(p["_domaine"])}</td>'
            f'<td>{p["valeur"]} {p.get("unite","")}</td>'
            f'<td style="text-align:left">{html.escape(p.get("statut",""))}</td>'
            f'<td style="text-align:left"><span class="pill {cl}">{lib}</span></td></tr>'
        )

    utilises = set()
    for a in reg.justifs.values():
        utilises.update(a.get("appuis", []))
        utilises.update(a.get("contre_indications", []))
    racines = [aid for aid in reg.justifs if aid not in utilises]
    arbres_html = ""
    for aid in racines:
        a = reg.justifs[aid]
        c = reg.confiance_affirmation(aid)
        cl = classeConf_py(c)
        arbres_html += (
            f'<tr><td class="cliq" onclick="voirJust(\'{aid}\')">{html.escape(a["enonce"])}</td>'
            f'<td><span class="conf {cl}">{round(c*100)}&nbsp;%</span></td>'
            f'<td style="text-align:left">{html.escape(a.get("base",""))}</td></tr>'
        )

    dec_html = ""
    for did, d in reg.decisions.items():
        dec_html += (
            f'<tr><td class="cliq" onclick="voirDec(\'{did}\')">{html.escape(did)}</td>'
            f'<td style="text-align:left">{html.escape(d["titre"])}</td>'
            f'<td>{html.escape(str(d["date"]))}</td>'
            f'<td>{html.escape(str(d.get("de","-")))}</td>'
            f'<td>{html.escape(str(d.get("vers","-")))}</td></tr>'
        )

    preuves_html = ""
    for k, e in reg.preuves.items():
        lib, cl = FIABILITE[e["fiabilite"]]
        preuves_html += (
            f'<tr><td class="cliq" onclick="voirPr(\'{k}\')">{html.escape(k)}</td>'
            f'<td style="text-align:left">{html.escape(e["titre"])}</td>'
            f'<td style="text-align:left">{html.escape(e["type"])}</td>'
            f'<td style="text-align:left"><span class="pill {cl}">{lib}</span></td>'
            f'<td>{len(usage.get(k,[]))}</td></tr>'
        )

    legende = (
        '<p class="legend"><b>Regles de confiance.</b> '
        'Experience interne ou industrielle, loi physique, mesure certifiee, '
        'decision commerciale, texte reglementaire : 100 %. '
        'Specification constructeur : 90 % (a discuter). '
        'Publication scientifique : 80 % (a discuter). '
        'Declaration orale : 60 % (a discuter). Hypothese : 50 %. '
        'Un calcul prend la confiance de son appui le plus faible, '
        'sauf si un seul appui suffit.</p>'
    )
    sur = ""
    if surcharges:
        sur = ('<p class="legend">Surcharges appliquees : ' +
               ", ".join(f"<code>{k} = {v}</code>" for k, v in surcharges.items()) + "</p>")

    page = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Urban Rig — modele tracable</title>
<style>{CSS}</style>
</head>
<body>
<div class="app">
<header>
  <div class="header-top">
    <h1>Urban Rig — modele tracable</h1>
    <span class="sub">Genere le {date.today().isoformat()}{' &middot; surcharges actives' if surcharges else ''}</span>
  </div>
  <nav class="tabs">
    <button class="tab" data-tab="hypotheses">Hypotheses</button>
    <button class="tab" data-tab="resultats">Resultats financiers</button>
    <button class="tab" data-tab="matiere">Bilan matiere</button>
    <button class="tab" data-tab="confiance">Confiance &amp; preuves</button>
  </nav>
</header>
<div id="autocontrole"></div>
<div class="statusbar">
  <span id="compteur">Valeurs de reference</span>
  <button class="btn sec" onclick="reinitialiser()">Reinitialiser</button>
  <span style="color:var(--fg3)">Cliquez sur un chiffre pour remonter a ses preuves. Modifiez un parametre pour recalculer la page.</span>
</div>
<div class="panel" id="tab-hypotheses">
  <div class="section"><h2>Parametres editables</h2><div class="inner">
    <p class="legend">Les pastilles indiquent le taux de confiance dans chaque parametre. Les curseurs sont bornes par les valeurs declarees dans les fichiers YAML. Tout changement recalcule la page instantanement.</p>
    {sur}{tab_hypotheses}
  </div></div>
</div>
<div class="panel" id="tab-resultats">
  <div class="section"><h2>Indicateurs cles</h2><div class="inner">
    <div class="kpi-grid">{kpi_html}</div>
  </div></div>
  <div class="section"><h2>Compte de resultat (k EUR)</h2><div class="inner">
    <div class="tbl-wrap"><table>
      <thead>{thead_pl}</thead><tbody>{corps_pl}</tbody>
    </table></div>
  </div></div>
</div>
<div class="panel" id="tab-matiere">
  <div class="section"><h2>Flux physiques — cliquez sur une ligne pour remonter aux hypotheses</h2><div class="inner">
    <div class="tbl-wrap"><table>
      <thead><tr><th>Grandeur</th><th>Valeur</th><th>Delta vs reference</th></tr></thead>
      <tbody>{bilan_html}</tbody>
    </table></div>
  </div></div>
</div>
<div class="panel" id="tab-confiance">
  {legende}
  <div class="section"><h2>Affirmations racines — taux de confiance global</h2><div class="inner">
    <div class="tbl-wrap"><table>
      <thead><tr><th>Affirmation</th><th>Confiance</th><th style="text-align:left">Base</th></tr></thead>
      <tbody>{arbres_html}</tbody>
    </table></div>
  </div></div>
  <div class="section"><h2>Parametres a renforcer (preuve faible ou absente)</h2><div class="inner">
    <div class="tbl-wrap"><table>
      <thead><tr><th>Parametre</th><th style="text-align:left">Domaine</th><th>Valeur</th><th style="text-align:left">Statut</th><th style="text-align:left">Preuve</th></tr></thead>
      <tbody>{faibles_html}</tbody>
    </table></div>
  </div></div>
  <div class="section"><h2>Journal des decisions</h2><div class="inner">
    <div class="tbl-wrap"><table>
      <thead><tr><th>Ref</th><th style="text-align:left">Titre</th><th>Date</th><th>De</th><th>Vers</th></tr></thead>
      <tbody>{dec_html}</tbody>
    </table></div>
  </div></div>
  <div class="section"><h2>Registre des preuves</h2><div class="inner">
    <div class="tbl-wrap"><table>
      <thead><tr><th>Cle</th><th style="text-align:left">Titre</th><th style="text-align:left">Type</th><th style="text-align:left">Fiabilite</th><th>Valeurs liees</th></tr></thead>
      <tbody>{preuves_html}</tbody>
    </table></div>
  </div></div>
</div>
</div>
<div id="panneau"></div>
<script>{MOTEUR_JS}</script>
<script>{JS_UI.replace("__DONNEES__", _json(donnees))}</script>
</body>
</html>"""
    chemin.write_text(page, encoding="utf-8")
    return chemin


def classeConf_py(c):
    return "c100" if c >= 0.999 else "c90" if c >= 0.9 else "c80" if c >= 0.8 else "c60" if c >= 0.6 else "c0"
