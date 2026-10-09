"""
Genere une page HTML autonome : compte de resultat cliquable ET modifiable.
Chaque chiffre remonte jusqu'aux parametres, aux decisions et aux documents sources.
Chaque parametre est editable : la page recalcule tout en direct.

Le moteur JavaScript embarque (engine/moteur.js) est un port exact de modele.py.
La page verifie cette egalite au chargement et affiche un bandeau rouge si elle est rompue.

Aucune dependance, aucun serveur. Un seul fichier, ouvrable dans un navigateur.
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
    "mesure_interne": ("Mesure interne", "ok"),
    "constructeur": ("Constructeur", "moyen"),
    "litterature": ("Litterature", "moyen"),
    "aucune": ("Aucune preuve", "faible"),
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
    "fioul_litres_jour": "Fioul de secours", "fioul_annuel": "Fioul annuel",
    "energie_exportee": "Energie exportee",
    "surface_batie": "Surface batie",
    "capex_equipement": "CAPEX equipement", "capex_genie_civil": "CAPEX genie civil",
    "capex_total": "CAPEX total", "capex_par_tonne_an": "CAPEX par tonne annuelle",
    "amortissement_annuel": "Amortissement annuel",
    "dette": "Dette", "fonds_propres": "Fonds propres",
    "ebitda_an3": "EBITDA annee 3", "marge_ebitda_an3": "Marge EBITDA annee 3",
    "gate_fee_equilibre": "Gate fee d'equilibre",
    "carbone_fossile_entrant": "Carbone fossile entrant",
    "emissions_directes_site": "Emissions directes du site",
    "intensite_carbone_site": "Intensite carbone du site",
    "carbone_sortant_produits": "Carbone sortant dans les produits",
    "carbone_stocke": "Carbone stocke",
    "ecart_bouclage_carbone": "Ecart de bouclage du bilan carbone",
}

LIGNES_PL = [
    ("recettes", "RECETTES", True),
    ("rec_gate_fees", "Gate fees", False),
    ("rec_huile", "Huile", False),
    ("rec_char", "Char", False),
    ("rec_metaux", "Metaux", False),
    ("rec_verre", "Verre", False),
    ("rec_carbone", "Credits carbone", False),
    ("charges", "CHARGES", True),
    ("ch_personnel", "Personnel", False),
    ("ch_maintenance", "Maintenance", False),
    ("ch_electricite", "Electricite", False),
    ("ch_fioul_secours", "Fioul de secours", False),
    ("ch_elimination_residus", "Elimination des residus", False),
    ("ch_carbonate", "Carbonate de calcium", False),
    ("ch_concentrat", "Elimination du concentrat", False),
    ("ch_couche_catalytique", "Couche catalytique halogenes", False),
    ("ch_ceramique_seacoral", "Ceramique SEA CORAL", False),
    ("ch_charbon_actif", "Charbon actif", False),
    ("ch_assurance", "Assurance", False),
    ("ch_provision_divers", "Provision et divers", False),
    ("ebitda", "EBITDA", True),
    ("amortissement", "Amortissement", False),
    ("interets", "Interets", False),
    ("resultat_avant_impot", "Resultat avant impot", False),
    ("impot", "Impot", False),
    ("resultat_net", "RESULTAT NET", True),
    ("flux_libre", "Flux libre", False),
    ("flux_cumule", "Flux cumule", True),
]

CSS = """
*{box-sizing:border-box}
body{margin:0;font:14px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 color:#1a1a1a;background:#f6f7f9}
header{background:#1f3864;color:#fff;padding:22px 28px}
header h1{margin:0;font-size:20px;font-weight:600}
header p{margin:6px 0 0;opacity:.8;font-size:13px}
main{max-width:1180px;margin:0 auto;padding:24px 20px 80px}
section{background:#fff;border:1px solid #e2e5ea;border-radius:8px;margin-bottom:22px;overflow:hidden}
section>h2{margin:0;padding:14px 18px;font-size:15px;background:#eef1f6;border-bottom:1px solid #e2e5ea}
.inner{padding:16px 18px}
table{border-collapse:collapse;width:100%;font-size:13px}
th,td{padding:7px 10px;border-bottom:1px solid #eef0f3;text-align:right}
th:first-child,td:first-child{text-align:left}
thead th{background:#f8f9fb;font-weight:600;position:sticky;top:0}
tr.fort td{font-weight:700;background:#fafbfd}
.trace{cursor:pointer;border-bottom:1px dotted #7a8aa5}
.trace:hover{background:#fff6d6}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px}
.carte{border:1px solid #e2e5ea;border-radius:6px;padding:12px;background:#fff}
.carte .v{font-size:19px;font-weight:700;margin:4px 0}
.carte .l{font-size:12px;color:#5a6472}
.pill{display:inline-block;padding:1px 7px;border-radius:10px;font-size:11px;font-weight:600}
.ok{background:#e4f3e6;color:#1d6b2c}
.moyen{background:#fdf1dd;color:#8a5a08}
.faible{background:#fbe2e0;color:#9e2418}
#panneau{position:fixed;top:0;right:-560px;width:560px;max-width:94vw;height:100%;background:#fff;
 box-shadow:-3px 0 22px rgba(0,0,0,.18);transition:right .22s ease;overflow-y:auto;z-index:50}
#panneau.ouvert{right:0}
#panneau .tete{background:#1f3864;color:#fff;padding:16px 20px}
#panneau .tete h3{margin:0;font-size:16px}
#panneau .corps{padding:18px 20px}
#panneau h4{margin:20px 0 8px;font-size:13px;text-transform:uppercase;letter-spacing:.5px;color:#5a6472}
.fermer{position:absolute;top:14px;right:18px;color:#fff;cursor:pointer;font-size:22px;line-height:1}
.dec{border-left:3px solid #1f3864;padding:8px 12px;background:#f8f9fb;margin-bottom:10px;font-size:13px}
.pr{border-left:3px solid #9aa5b5;padding:8px 12px;background:#fafbfc;margin-bottom:10px;font-size:13px}
.res{color:#9e2418;font-style:italic}
.note{font-size:12px;color:#5a6472;margin-top:6px}
footer{text-align:center;color:#7a8492;font-size:12px;padding:20px}
.bandeau{padding:10px 18px;font-size:13px;font-weight:600}
.bandeau.vert{background:#e4f3e6;color:#1d6b2c}
.bandeau.rouge{background:#fbe2e0;color:#9e2418}
.param{border:1px solid #e2e5ea;border-radius:6px;padding:10px 12px;background:#fff}
.param.modifie{border-color:#c98a00;background:#fffdf5}
.param label{display:block;font-size:12px;color:#5a6472;margin-bottom:5px}
.param input,.param select{width:100%;padding:5px 7px;border:1px solid #cfd6e0;border-radius:4px;
 font:inherit;font-size:13px}
.param input[type=range]{padding:0;margin-top:6px}
.param .u{font-size:11px;color:#7a8492}
.ref{display:inline-block;margin:4px 4px 0 0;padding:2px 8px;font-size:11px;border-radius:10px;
 background:#eef1f6;border:1px solid #d7dde6;cursor:pointer}
.ref:hover{background:#dde6f5}
.ref.actif{background:#1f3864;color:#fff;border-color:#1f3864}
.barre{position:sticky;top:0;z-index:20;background:#fff;border-bottom:1px solid #e2e5ea;
 padding:9px 18px;display:flex;gap:12px;align-items:center;font-size:13px}
.btn{padding:5px 12px;border:1px solid #1f3864;background:#1f3864;color:#fff;border-radius:4px;
 cursor:pointer;font:inherit;font-size:13px}
.btn.sec{background:#fff;color:#1f3864}
.delta{font-size:12px;font-weight:600}
.delta.plus{color:#1d6b2c}.delta.moins{color:#9e2418}
details{margin-bottom:10px}
.arbre{margin:0;padding-left:0;list-style:none}
.arbre ul{list-style:none;padding-left:18px;margin:4px 0 4px 6px;border-left:2px solid #e2e5ea}
.arbre li{margin:5px 0}
.noeud{display:flex;gap:8px;align-items:flex-start;padding:7px 10px;border:1px solid #e2e5ea;
 border-radius:6px;background:#fff;cursor:pointer}
.noeud:hover{border-color:#1f3864}
.noeud .txt{flex:1;font-size:13px}
.noeud .base{font-size:11px;color:#5a6472;margin-top:2px}
.conf{font-weight:700;font-size:12px;padding:2px 8px;border-radius:10px;white-space:nowrap}
.c100{background:#1d6b2c;color:#fff}.c90{background:#4c9a5a;color:#fff}
.c80{background:#c98a00;color:#fff}.c60{background:#d9731a;color:#fff}
.c0{background:#9e2418;color:#fff}
.contre .noeud{border-color:#e7b0aa;background:#fdf4f3}
.feuille{font-size:12px;padding:6px 10px;border-left:3px solid #1f3864;background:#f6f8fb;
 margin:4px 0;cursor:pointer}
.discuter{font-size:11px;color:#8a5a08;font-style:italic}
.cible{font-size:12px;background:#e4f3e6;color:#1d6b2c;padding:6px 10px;border-radius:4px;margin-top:6px}
summary{cursor:pointer;font-weight:600;padding:6px 0;font-size:13px}
"""

JS_UI = """
const D = __DONNEES__;
const P0 = JSON.parse(JSON.stringify(D.params));
let P = JSON.parse(JSON.stringify(D.params));
let RES = null, PL = null, BASE = null;

const nf = (v,d=0)=> v.toLocaleString('fr-FR',{minimumFractionDigits:d,maximumFractionDigits:d});
function fmt(v,u){
  if(typeof v === 'string') return v+' '+(u||'');
  if(u==='fraction') return nf(v*100,1)+' %';
  return (Math.abs(v)>=1000 ? nf(v,0) : nf(v,2))+' '+(u||'');
}

function recalculer(){
  const r = calculer(P); RES = r.R; PL = r.pl;
  if(!BASE) BASE = JSON.parse(JSON.stringify(RES));
  peindre();
}

function peindre(){
  document.querySelectorAll('[data-res]').forEach(e=>{
    const k = e.dataset.res; if(!RES[k]) return;
    e.textContent = fmt(RES[k].valeur, RES[k].unite);
  });
  document.querySelectorAll('[data-delta]').forEach(e=>{
    const k = e.dataset.delta; const a = BASE[k].valeur, b = RES[k].valeur;
    if(typeof a !== 'number' || Math.abs(a) < 1e-12){ e.textContent=''; return; }
    const d = (b/a-1)*100;
    if(Math.abs(d) < 0.05){ e.textContent=''; e.className='delta'; return; }
    e.textContent = (d>0?'+':'')+nf(d,1)+' %';
    e.className = 'delta '+(d>0?'plus':'moins');
  });
  document.querySelectorAll('[data-pl]').forEach(e=>{
    const [c,a] = e.dataset.pl.split('|');
    e.textContent = nf(PL[+a][c],0);
  });
  let mod = 0;
  Object.keys(P).forEach(k=>{
    const chg = P[k].valeur !== P0[k].valeur;
    if(chg) mod++;
    const b = document.querySelector(`[data-box="${k}"]`);
    if(b) b.classList.toggle('modifie', chg);
  });
  const c = document.getElementById('compteur');
  if(c) c.textContent = mod ? mod+' parametre(s) modifie(s)' : 'valeurs de reference';
}

function changer(k, val){
  const q = P[k];
  if(typeof P0[k].valeur === 'number'){
    val = parseFloat(val); if(isNaN(val)) return;
    const b = D.bornes[k];
    if(b){ val = Math.min(b.haut, Math.max(b.bas, val)); }
  }
  q.valeur = val;
  const inp = document.querySelector(`[data-inp="${k}"]`);
  const sld = document.querySelector(`[data-sld="${k}"]`);
  if(inp && inp.value != val) inp.value = val;
  if(sld && sld.value != val) sld.value = val;
  document.querySelectorAll(`[data-refv="${k}"]`).forEach(e=>{
    e.classList.toggle('actif', parseFloat(e.dataset.v) === val);
  });
  recalculer();
}

function reinitialiser(){ P = JSON.parse(JSON.stringify(P0));
  Object.keys(P).forEach(k=>{
    const i = document.querySelector(`[data-inp="${k}"]`); if(i) i.value = P[k].valeur;
    const s = document.querySelector(`[data-sld="${k}"]`); if(s) s.value = P[k].valeur;
  });
  document.querySelectorAll('[data-refv]').forEach(e=>{
    e.classList.toggle('actif', parseFloat(e.dataset.v) === P[e.dataset.refv].valeur);
  });
  recalculer();
}

function ouvrir(cle){
  const r = RES[cle]; if(!r) return;
  const lab = D.libelles[cle] || cle;
  const p = document.getElementById('panneau');
  let h = `<div class="tete"><span class="fermer" onclick="fermer()">&times;</span>
    <h3>${lab}</h3><div style="opacity:.85;font-size:13px;margin-top:4px">${fmt(r.valeur,r.unite)}</div></div>
    <div class="corps">`;
  h += `<h4>Parametres consommes</h4>`;
  if(!r.depend.length){ h += `<div class="note">Grandeur derivee d'autres resultats.</div>`; }
  r.depend.slice().sort().forEach(k=>{
    const q = D.meta[k], f = D.fiab[k];
    const cf = D.confP[k];
    h += `<div class="pr"><b>${q.label}</b> ${pastilleConf(cf.c)} ${cf.instruit?'':'<span class="discuter">non instruit</span>'}
      ${q.justification?`<div class="note"><a href="#" onclick="voirJust('${q.justification}');return false;">&#9656; Voir l'arbre de justification</a></div>`:''}
      ${champ(k)}
      <div class="note">statut : ${q.statut}</div>`;
    if(q.note) h += `<div class="note">${q.note}</div>`;
    if(q.decision) h += `<div class="note">Decision : <a href="#" onclick="voirDec('${q.decision}');return false;">${q.decision}</a></div>`;
    if(q.preuves && q.preuves.length) h += `<div class="note">Preuves : ` +
      q.preuves.map(x=>`<a href="#" onclick="voirPr('${x}');return false;">${x}</a>`).join(', ') + `</div>`;
    h += `</div>`;
  });
  p.innerHTML = h + `</div>`; p.classList.add('ouvert');
  peindre();
}

function champ(k){
  const q = D.meta[k], v = P[k].valeur, b = D.bornes[k];
  if(D.choix[k]){
    return `<select data-inp="${k}" onchange="changer('${k}',this.value)">` +
      D.choix[k].map(o=>`<option value="${o}" ${o===v?'selected':''}>${o}</option>`).join('') + `</select>`;
  }
  let h = `<div style="display:flex;gap:8px;align-items:center;margin-top:6px">
    <input type="number" step="any" data-inp="${k}" value="${v}"
      oninput="changer('${k}',this.value)"><span class="u">${q.unite||''}</span></div>`;
  if(b){
    const pas = (b.haut-b.bas)/200;
    h += `<input type="range" data-sld="${k}" min="${b.bas}" max="${b.haut}" step="${pas}"
      value="${v}" oninput="changer('${k}',this.value)">
      <div class="u">${b.bas} a ${b.haut}</div>`;
  }
  if(D.refs[k]){
    h += `<div>` + D.refs[k].map(r=>
      `<span class="ref" data-refv="${k}" data-v="${r.valeur}"
        onclick="changer('${k}',${r.valeur})">${r.libelle} : ${r.valeur}</span>`).join('') + `</div>`;
  }
  return h;
}

function voirDec(id){
  const d = D.decisions[id]; const p = document.getElementById('panneau');
  p.innerHTML = `<div class="tete"><span class="fermer" onclick="fermer()">&times;</span>
    <h3>${id} — ${d.titre}</h3><div style="opacity:.85;font-size:13px;margin-top:4px">${d.date}</div></div>
    <div class="corps">
    <h4>Changement</h4><div class="dec">${d.de} &rarr; ${d.vers} ${d.unite||''}</div>
    <h4>Motif</h4><div class="dec">${d.motif}</div>
    ${d.a_verifier?`<h4>Reste a verifier</h4><div class="dec res">${d.a_verifier}</div>`:''}
    <h4>Preuves</h4>` +
    (d.preuves||[]).map(x=>`<div class="pr"><a href="#" onclick="voirPr('${x}');return false;">${x}</a></div>`).join('')
    + `</div>`;
  p.classList.add('ouvert');
}

function voirPr(id){
  const e = D.preuves[id]; const p = document.getElementById('panneau');
  const f = D.fiabPreuve[id];
  let h = `<div class="tete"><span class="fermer" onclick="fermer()">&times;</span>
    <h3>${e.titre}</h3><div style="opacity:.85;font-size:13px;margin-top:4px">${id} &middot; ${e.type}</div></div>
    <div class="corps"><h4>Fiabilite</h4><div class="pr"><span class="pill ${f.classe}">${f.libelle}</span></div>`;
  if(e.contenu) h += `<h4>Contenu</h4><div class="pr">${e.contenu}</div>`;
  if(e.chemin) h += `<h4>Emplacement</h4><div class="pr"><code>${e.chemin}</code></div>`;
  if(e.reserve) h += `<h4>Reserve</h4><div class="pr res">${e.reserve}</div>`;
  const dep = D.usage[id]||[];
  h += `<h4>Valeurs qui en dependent (${dep.length})</h4>`;
  h += dep.length ? dep.map(k=>`<div class="pr">${D.meta[k].label}</div>`).join('')
                  : `<div class="note">Aucune.</div>`;
  p.innerHTML = h + `</div>`; p.classList.add('ouvert');
}

function classeConf(c){ return c>=0.999?'c100':c>=0.9?'c90':c>=0.8?'c80':c>=0.6?'c60':'c0'; }
function pastilleConf(c){ return `<span class="conf ${classeConf(c)}">${Math.round(c*100)} %</span>`; }

function brancheHTML(aid, profondeur, vus){
  const a = D.justifs[aid]; if(!a) return '';
  if(vus.has(aid)) return `<li><div class="feuille" onclick="voirJust('${aid}')">&#8618; ${aid} (deja developpe plus haut)</div></li>`;
  vus.add(aid);
  const c = D.confJ[aid];
  let h = `<li><div class="noeud" onclick="voirJust('${aid}')">${pastilleConf(c)}
    <div class="txt">${a.enonce}<div class="base">${aid} &middot; ${a.base}${D.aDiscuter.includes(a.base)?' &middot; <span class="discuter">confiance a discuter</span>':''}${a.appuis&&a.appuis.length?' &middot; '+(a.mode==='un_suffit'?'un appui suffit':'tous les appuis requis'):''}</div></div></div>`;
  const enfants = [];
  (a.appuis||[]).forEach(x=> enfants.push(brancheHTML(x, profondeur+1, vus)));
  (a.preuves||[]).forEach(p=>{
    const e = D.preuves[p]; if(!e) return;
    enfants.push(`<li><div class="feuille" onclick="event.stopPropagation();voirPr('${p}')">&#128196; <b>${p}</b> &middot; ${e.titre} <span class="pill ${D.fiabPreuve[p].classe}">${D.fiabPreuve[p].libelle}</span></div></li>`);
  });
  if(enfants.length) h += `<ul>${enfants.join('')}</ul>`;
  if(a.contre_indications && a.contre_indications.length){
    h += `<ul class="contre"><li style="font-size:11px;color:#9e2418;font-weight:700;margin-top:6px">CONTRE-INDICATIONS</li>` +
      a.contre_indications.map(x=>brancheHTML(x, profondeur+1, vus)).join('') + `</ul>`;
  }
  return h + `</li>`;
}

function voirJust(aid){
  const a = D.justifs[aid]; const p = document.getElementById('panneau');
  const c = D.confJ[aid];
  let h = `<div class="tete"><span class="fermer" onclick="fermer()">&times;</span>
    <h3>${a.enonce}</h3><div style="margin-top:8px">${pastilleConf(c)}
    <span style="opacity:.85;font-size:12px;margin-left:6px">${aid} &middot; ${a.base}</span></div></div>
    <div class="corps">`;
  if(a.detail) h += `<h4>Detail</h4><div class="pr">${a.detail}</div>`;
  if(a.consequence) h += `<h4>Consequence</h4><div class="dec">${a.consequence}</div>`;
  if(a.pour_passer_a_1 && c < 0.999) h += `<h4>Pour atteindre 100 %</h4><div class="cible">${a.pour_passer_a_1}</div>`;
  h += `<h4>Arbre de justification</h4><ul class="arbre">${brancheHTML(aid,0,new Set())}</ul>`;
  const parents = Object.keys(D.justifs).filter(k=>(D.justifs[k].appuis||[]).includes(aid));
  const params = Object.keys(D.meta).filter(k=>D.meta[k].justification===aid);
  if(parents.length || params.length){
    h += `<h4>Utilise par</h4>`;
    params.forEach(k=> h += `<div class="pr">Parametre : <b>${D.meta[k].label}</b></div>`);
    parents.forEach(k=> h += `<div class="pr" style="cursor:pointer" onclick="voirJust('${k}')">&#8593; ${D.justifs[k].enonce}</div>`);
  }
  p.innerHTML = h + `</div>`; p.classList.add('ouvert');
}

function fermer(){ document.getElementById('panneau').classList.remove('ouvert'); }
document.addEventListener('keydown', e=>{ if(e.key==='Escape') fermer(); });

// --- autocontrole : le JS doit redonner exactement les valeurs calculees par Python
(function(){
  const r = calculer(JSON.parse(JSON.stringify(P0))).R;
  let max = 0, pire = '';
  for(const k in D.reference){
    if(!(k in r)) continue;
    const a = D.reference[k], b = r[k].valeur;
    if(typeof a !== 'number') continue;
    const e = Math.abs(a) > 1e-9 ? Math.abs(b/a - 1) : Math.abs(b - a);
    if(e > max){ max = e; pire = k; }
  }
  const el = document.getElementById('autocontrole');
  if(max < 1e-9){
    el.className = 'bandeau vert';
    el.textContent = 'Autocontrole : le calcul de cette page redonne exactement les valeurs du moteur Python.';
  } else {
    el.className = 'bandeau rouge';
    el.textContent = 'AUTOCONTROLE EN ECHEC : ecart de ' + (max*100).toFixed(4) + ' % sur ' + pire
      + '. Le moteur JavaScript et le moteur Python ont diverge. Ne pas utiliser ces chiffres.';
  }
})();

document.querySelectorAll('[data-champ]').forEach(e=>{ e.innerHTML = champ(e.dataset.champ); });
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
    donnees = {"justifs": reg.justifs, "confJ": conf_j, "confP": conf_p,
               "aDiscuter": sorted(A_DISCUTER),
               "params": valeurs, "meta": meta, "bornes": bornes, "refs": refs, "choix": choix,
               "libelles": LIBELLES, "decisions": reg.decisions, "preuves": reg.preuves,
               "fiab": fiab, "fiabPreuve": fiab_preuve, "usage": usage,
               "reference": {k: v["valeur"] for k, v in m.r.items()}}

    cles_cles = ["tonnage_annuel", "capex_total", "capex_par_tonne_an", "ebitda_an3",
                 "marge_ebitda_an3", "gate_fee_equilibre", "couverture_thermique",
                 "intensite_carbone_site", "ecart_bouclage_carbone"]
    cartes = ""
    for k in cles_cles:
        if k not in m.r:
            continue
        pires = [fiab[p]["classe"] for p in m.r[k]["depend"]]
        cl = "faible" if "faible" in pires else ("moyen" if "moyen" in pires else "ok")
        lib = {"faible": "preuve faible", "moyen": "preuve moyenne", "ok": "preuve solide"}[cl]
        cartes += (f'<div class="carte"><div class="l">{LIBELLES.get(k,k)}</div>'
                   f'<div class="v trace" data-res="{k}" onclick="ouvrir(\'{k}\')"></div>'
                   f'<span class="pill {cl}">{lib}</span> <span data-delta="{k}"></span></div>')

    edit = ""
    for domaine, cles in reg.domaines.items():
        champs = ""
        for k in cles:
            p = reg.params[k]
            f = fiab[k]
            c, inst = reg.confiance_parametre(k)
            cl = "c100" if c >= 0.999 else "c90" if c >= 0.9 else "c80" if c >= 0.8 else "c60" if c >= 0.6 else "c0"
            lien = (f' <a href="#" onclick="voirJust(\'{p["justification"]}\');return false;" '
                    f'style="font-size:11px">arbre</a>') if p.get("justification") else \
                   ' <span class="discuter">non instruit</span>'
            champs += (f'<div class="param" data-box="{k}">'
                       f'<label>{html.escape(p["label"])} '
                       f'<span class="conf {cl}">{round(c*100)} %</span>{lien}</label>'
                       f'<div data-champ="{k}"></div></div>')
        edit += (f'<details><summary>{html.escape(domaine)} ({len(cles)})</summary>'
                 f'<div class="grid" style="margin-top:8px">{champs}</div></details>')

    nb = min(10, len(m.pl))
    thead = "<tr><th>Ligne</th>" + "".join(f"<th>An {i+1}</th>" for i in range(nb)) + "</tr>"
    corps = ""
    for cle, lib, fort in LIGNES_PL:
        if cle not in m.pl[0]:
            continue
        cls = ' class="fort"' if fort else ""
        corps += f"<tr{cls}><td>{html.escape(lib)}</td>"
        for i in range(nb):
            corps += f'<td data-pl="{cle}|{i}"></td>'
        corps += "</tr>"

    mat = ""
    for k in ["huile", "char", "ferreux", "aluminium", "autres_metaux", "verre",
              "residus", "eau_procede", "eau_douce", "concentrat", "energie_exportee",
              "fioul_litres_jour", "emissions_directes_site"]:
        if k in m.r:
            mat += (f'<tr><td class="trace" onclick="ouvrir(\'{k}\')">{LIBELLES.get(k,k)}</td>'
                    f'<td data-res="{k}"></td><td data-delta="{k}"></td></tr>')

    faibles = sorted(reg.params.items(),
                     key=lambda x: (-RANG.index(_fiab(x[1].get("preuves", []), reg.preuves)),
                                    x[1]["_domaine"]))
    tf = ""
    for k, p in faibles:
        f = _fiab(p.get("preuves", []), reg.preuves)
        if RANG.index(f) < len(RANG) - 2:
            continue
        lib, cl = FIABILITE[f]
        tf += (f'<tr><td>{p["label"]}</td><td style="text-align:left">{p["_domaine"]}</td>'
               f'<td>{p["valeur"]} {p.get("unite","")}</td>'
               f'<td style="text-align:left">{p["statut"]}</td>'
               f'<td style="text-align:left"><span class="pill {cl}">{lib}</span></td></tr>')

    tdec = ""
    for did, d in reg.decisions.items():
        tdec += (f'<tr><td class="trace" onclick="voirDec(\'{did}\')">{did}</td>'
                 f'<td style="text-align:left">{d["titre"]}</td><td>{d["date"]}</td>'
                 f'<td>{d.get("de","-")}</td><td>{d.get("vers","-")}</td></tr>')

    tpr = ""
    for k, e in reg.preuves.items():
        lib, cl = FIABILITE[e["fiabilite"]]
        tpr += (f'<tr><td class="trace" onclick="voirPr(\'{k}\')">{k}</td>'
                f'<td style="text-align:left">{e["titre"]}</td>'
                f'<td style="text-align:left">{e["type"]}</td>'
                f'<td style="text-align:left"><span class="pill {cl}">{lib}</span></td>'
                f'<td>{len(usage.get(k,[]))}</td></tr>')

    utilises = set()
    for a in reg.justifs.values():
        utilises.update(a.get("appuis", []))
        utilises.update(a.get("contre_indications", []))
    racines = [aid for aid in reg.justifs if aid not in utilises]
    tj = ""
    for aid in racines:
        a = reg.justifs[aid]
        c = reg.confiance_affirmation(aid)
        cl = "c100" if c >= 0.999 else "c90" if c >= 0.9 else "c80" if c >= 0.8 else "c60" if c >= 0.6 else "c0"
        tj += (f'<tr><td class="trace" onclick="voirJust(\'{aid}\')">{html.escape(a["enonce"])}</td>'
               f'<td><span class="conf {cl}">{round(c*100)} %</span></td>'
               f'<td style="text-align:left">{a.get("base","")}</td></tr>')
    legende = ("<p class=\"note\"><b>Regles de confiance.</b> Experience interne ou industrielle, loi physique, "
               "mesure certifiee, decision commerciale, texte reglementaire : 100 %. Specification constructeur : "
               "90 %, a discuter entre 80 et 100 %. Publication scientifique : 80 %, a discuter. Declaration orale : 60 %, a discuter. Hypothese : 50 %. "
               "Un calcul prend la confiance de son appui le plus faible, sauf si un seul appui suffit.</p>")

    sur = ""
    if surcharges:
        sur = ("<p class=\"note\">Surcharges appliquees a la generation : "
               + ", ".join(f"<code>{k} = {v}</code>" for k, v in surcharges.items()) + "</p>")

    page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Urban Rig — modele tracable</title><style>{CSS}</style></head><body>
<header><h1>Urban Rig — modele tracable</h1>
<p>Genere le {date.today().isoformat()}. Cliquez sur une valeur pour remonter a ses parametres et a ses preuves, ou modifiez un parametre pour recalculer toute la page.</p></header>
<div id="autocontrole" class="bandeau"></div>
<div class="barre"><span id="compteur">valeurs de reference</span>
<button class="btn sec" onclick="reinitialiser()">Reinitialiser</button>
<span class="note">Les ecarts affiches sont relatifs aux valeurs de reference.</span></div>
<main>
<section><h2>Synthese</h2><div class="inner"><div class="grid">{cartes}</div>{sur}</div></section>
<section><h2>Arbres de justification</h2><div class="inner">
{legende}
<table><thead><tr><th>Affirmation racine</th><th>Confiance</th><th style="text-align:left">Base</th></tr></thead>
<tbody>{tj}</tbody></table></div></section>
<section><h2>Parametres — modifiables</h2><div class="inner">
<p class="note">Toute modification recalcule immediatement la page. Les pastilles indiquent la solidite de la preuve, les curseurs sont bornes par les valeurs declarees dans les fichiers YAML.</p>
{edit}</div></section>
<section><h2>Compte de resultat</h2><div class="inner" style="overflow-x:auto">
<table><thead>{thead}</thead><tbody>{corps}</tbody></table></div></section>
<section><h2>Bilan matiere et energie</h2><div class="inner">
<table><tbody>{mat}</tbody></table></div></section>
<section><h2>Parametres les plus faibles</h2><div class="inner">
<p class="note">Classes par la fiabilite de la preuve la plus solide qui les etaye. C'est la liste de travail du dossier.</p>
<table><thead><tr><th>Parametre</th><th style="text-align:left">Domaine</th><th>Valeur de reference</th>
<th style="text-align:left">Statut</th><th style="text-align:left">Preuve</th></tr></thead>
<tbody>{tf}</tbody></table></div></section>
<section><h2>Journal des decisions</h2><div class="inner">
<table><thead><tr><th>Ref</th><th style="text-align:left">Titre</th><th>Date</th><th>De</th><th>Vers</th></tr></thead>
<tbody>{tdec}</tbody></table></div></section>
<section><h2>Registre des preuves</h2><div class="inner">
<table><thead><tr><th>Cle</th><th style="text-align:left">Titre</th><th style="text-align:left">Type</th>
<th style="text-align:left">Fiabilite</th><th>Valeurs liees</th></tr></thead>
<tbody>{tpr}</tbody></table></div></section>
</main>
<div id="panneau"></div>
<footer>Genere par run.py. Aucune valeur numerique dans le code : tout vient de params/*.yaml</footer>
<script>{MOTEUR_JS}</script>
<script>{JS_UI.replace("__DONNEES__", _json(donnees))}</script>
</body></html>"""
    chemin.write_text(page, encoding="utf-8")
    return chemin
