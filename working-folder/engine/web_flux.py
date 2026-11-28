"""
Pages du modele financier par flux (chat B, 25/11/2026), publiees sous /model.

Routes (toutes sous /model, aucune autre route de app.py n'est touchee) :
  GET  /model                  page interactive du modele par flux
  GET  /model/api/description  flux, scenarios, champs modifiables (valeur, source, confiance, statut)
  POST /model/api/calcul       {flux, scenario, surcharges, choix} -> resultats complets (JSON)
"""
import threading

from flask import Blueprint, Response, jsonify, request

from engine import flux as _flux
from engine.flux import Donnees, calculer, description_page

bp = Blueprint("modele_flux", __name__, url_prefix="/model")

# Donnees en cache : la lecture des registres prend environ 1,5 s, le calcul 0,1 s.
# Le cache est relu des qu'un fichier source change (date de modification).
_CACHE = {"sig": None, "d": None}
_VERROU = threading.Lock()


def _signature():
    fichiers = sorted(_flux.PARAMS.glob("*.yaml")) + [_flux.CALCULS, _flux.REG_EXT, _flux.EVIDENCE,
                                                       _flux.DECISIONS, _flux.BILANS]
    fichiers += sorted(_flux.VERIFS.glob("*codex*.md"))
    return tuple((str(f), f.stat().st_mtime) for f in fichiers if f.exists())


def _donnees():
    sig = _signature()
    with _VERROU:
        if _CACHE["sig"] != sig:
            _CACHE["d"] = Donnees()
            _CACHE["sig"] = sig
        return _CACHE["d"]


@bp.route("", strict_slashes=False)
def page():
    return Response(PAGE, mimetype="text/html")


@bp.route("/api/description")
def api_description():
    try:
        return jsonify(description_page(_donnees()))
    except Exception as e:  # noqa: BLE001
        return jsonify({"erreur": str(e)}), 500


@bp.route("/api/calcul", methods=["POST"])
def api_calcul():
    try:
        d = request.get_json(force=True) or {}
        r = calculer(d.get("flux", "plastiques"), d.get("scenario", "standard"),
                     d.get("surcharges") or {}, d.get("choix") or {}, _donnees())
        return jsonify(r)
    except Exception as e:  # noqa: BLE001
        return jsonify({"erreur": f"{type(e).__name__} : {e}"}), 400


PAGE = r"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Urban Rig : modele financier par flux</title>
<style>
:root{--bg:#f6f7f9;--card:#fff;--ink:#1c2430;--mut:#5d6878;--line:#e2e6ec;--acc:#1f5fbf;
--ok:#1d7a46;--warn:#a5650a;--bad:#b3261e;--wait:#6b4fa3}
*{box-sizing:border-box}body{margin:0;font:14px/1.45 system-ui,-apple-system,Segoe UI,sans-serif;background:var(--bg);color:var(--ink)}
header{padding:14px 22px;background:#14233b;color:#fff;display:flex;gap:18px;align-items:center;flex-wrap:wrap}
header h1{font-size:17px;margin:0;font-weight:600}header a{color:#b8cdf0;font-size:13px}
.bandeau{background:#fff4e0;border-bottom:1px solid #f0d9a8;padding:8px 22px;font-size:13px;color:#6a4a08}
main{display:grid;grid-template-columns:minmax(330px,430px) 1fr;gap:18px;padding:18px 22px}
@media(max-width:980px){main{grid-template-columns:1fr}}
main>*{min-width:0}
#etat{font-size:12px;color:var(--mut);margin:0 0 10px}#etat.run{color:var(--acc)}
.p .sanseffet{grid-column:1/3;font-size:11px;color:var(--warn)}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin-bottom:16px}
.card h2{font-size:14px;margin:0 0 10px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}
label.l{display:block;font-size:12px;color:var(--mut);margin:8px 0 3px}
select,input[type=number]{width:100%;padding:6px 8px;border:1px solid var(--line);border-radius:6px;font:inherit;background:#fff}
.seg{display:flex;gap:0;border:1px solid var(--line);border-radius:7px;overflow:hidden}
.seg button{flex:1;border:0;background:#fff;padding:7px;cursor:pointer;font:inherit}
.seg button.on{background:var(--acc);color:#fff}
.chk{display:flex;gap:8px;align-items:center;margin:6px 0}
details{border-top:1px solid var(--line);padding:6px 0}details summary{cursor:pointer;font-weight:600;padding:4px 0}
.p{display:grid;grid-template-columns:1fr 110px;gap:4px 8px;align-items:center;padding:6px 0;border-bottom:1px dashed var(--line)}
.p .lab{font-size:13px}.p .meta{grid-column:1/3;font-size:11px;color:var(--mut)}
.p.mod input{border-color:var(--acc);background:#eef4ff}
.b{display:inline-block;padding:1px 6px;border-radius:9px;font-size:11px;border:1px solid;margin-right:4px;white-space:nowrap}
.b.codex{color:var(--ok);border-color:#9fd3b4}.b.ctrl{color:var(--warn);border-color:#ecc98a}
.b.her{color:var(--bad);border-color:#efb0aa}.b.att{color:var(--wait);border-color:#c9b8e8}
.b.c{color:var(--ink);border-color:var(--line)}
.kpis{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.kpi .v{font-size:20px;font-weight:650}.kpi .n{font-size:12px;color:var(--mut)}
table{border-collapse:collapse;width:100%;font-size:12.5px}th,td{padding:5px 7px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}
th:first-child,td:first-child{text-align:left}th{color:var(--mut);font-weight:600;background:#fafbfc;position:sticky;top:0}
.scroll{overflow-x:auto}.neg{color:var(--bad)}.al li{margin:4px 0}.mut{color:var(--mut);font-size:12px}
button.reset{margin-top:10px;padding:7px 12px;border:1px solid var(--line);border-radius:6px;background:#fff;cursor:pointer}
#err{color:var(--bad);font-weight:600}
</style></head><body>
<header><h1>Urban Rig, modele financier par flux</h1><a href="/">Accueil</a>
<span class="mut" style="color:#b8cdf0">Briques en construction : chaque valeur montre sa source, sa confiance (echelle D-022) et son statut.</span></header>
<div class="bandeau">Document de travail. Les briques ne sont pas encore validees par Stephane (echantillon de trois chiffres) : ne pas presenter a un investisseur (D-070). Hors transport de la machine (D-051).</div>
<main>
<section>
 <div class="card"><h2>Flux et scenario</h2>
  <label class="l">Flux</label><select id="flux"></select>
  <div id="fluxInfo" class="mut" style="margin-top:4px"></div>
  <label class="l">Scenario (D-047)</label><div class="seg" id="scen"></div>
  <label class="l">Prix d'entree (positif = l'usine est payee ; negatif = elle achete)</label><select id="entree"></select>
  <label class="l">Chaleur manquante couverte par (D-069)</label><select id="chaleur"></select>
  <div class="chk"><input type="checkbox" id="gazorg"><label for="gazorg">Compter le gaz des matieres organiques (D-053, D-055)</label></div>
  <div id="opts"></div>
  <button class="reset" id="reset">Revenir aux valeurs par defaut</button>
 </div>
 <div class="card"><h2>Parametres modifiables</h2><div class="mut">Statuts : <span class="b codex">contre-verifie Codex</span><span class="b ctrl">controle, non contre-verifie</span><span class="b att">en attente de decision</span><span class="b her">heritee, non sourcee</span></div>
  <div id="groupes"></div></div>
</section>
<section>
 <div id="err"></div>
 <div id="etat">Calcul en cours...</div><div class="kpis" id="kpis"></div>
 <div class="card" style="margin-top:16px"><h2>Bilan par tonne entrante (lu dans calculs.yaml)</h2><div class="scroll"><table id="bilan"></table></div></div>
 <div class="card"><h2>Bilan energetique et valeurs unitaires</h2><div class="scroll"><table id="energie"></table></div></div>
 <div class="card"><h2>Compte de resultat et cash-flow, structure avec dette</h2><div class="scroll"><table id="annees"></table></div></div>
 <div class="card"><h2>Investissement</h2><div class="scroll"><table id="capex"></table></div></div>
 <div class="card"><h2>Points de vigilance</h2><ul class="al" id="alertes"></ul></div>
</section></main>
<script>
const $=id=>document.getElementById(id);
let DESC=null, etat={flux:'plastiques',scenario:'standard',surcharges:{},choix:{}}, minuterie=null, seq=0, dernier=null, champModifie=null;
const fmtM=v=>v==null?'n.d.':(v/1e6).toLocaleString('fr-FR',{minimumFractionDigits:2,maximumFractionDigits:2})+' MEUR';
const fmt=(v,d=1)=>v==null?'n.d.':Number(v).toLocaleString('fr-FR',{minimumFractionDigits:d,maximumFractionDigits:d});
const pct=v=>v==null?'n.d.':fmt(v*100,1)+' %';
function badge(s){const c=s.startsWith('contre')?'codex':s.startsWith('controle')?'ctrl':s.startsWith('en attente')?'att':'her';return `<span class="b ${c}">${s}</span>`}
function conf(c){return `<span class="b c">${c==null?'confiance : hors echelle':'confiance '+c+' %'}</span>`}
async function init(){
 DESC=await (await fetch('/model/api/description')).json();
 const fs=$('flux');
 for(const [k,f] of Object.entries(DESC.flux)){const o=new Option(f.label+(f.inactif?' (plus tard)':''),k);o.disabled=f.inactif;fs.add(o)}
 fs.value=etat.flux;
 fs.onchange=()=>{etat.flux=fs.value;etat.choix.prix_entree=null;remplirEntree();lancer(0)};
 const sc=$('scen');DESC.scenarios.forEach(s=>{const b=document.createElement('button');b.textContent=s;b.dataset.s=s;b.onclick=()=>{etat.scenario=s;majScen();lancer(0)};sc.appendChild(b)});majScen();
 for(const [k,l] of Object.entries(DESC.sources_chaleur))$('chaleur').add(new Option(l,k));
 $('chaleur').onchange=e=>{etat.choix.source_chaleur=e.target.value;lancer(0)};
 $('gazorg').onchange=e=>{etat.choix.compter_gaz_organique=e.target.checked;lancer(0)};
 $('entree').onchange=e=>{etat.choix.prix_entree=e.target.value;lancer(0)};
 const op=$('opts');DESC.options.forEach(k=>{const c=DESC.champs[k];const d=document.createElement('div');d.className='chk';
  d.innerHTML=`<input type="checkbox" id="o_${k}" ${c.valeur?'checked':''}><label for="o_${k}">${c.label} ${badge(c.statut)}</label>`;
  d.querySelector('input').onchange=e=>{etat.surcharges[k]=e.target.checked;lancer(0)};op.appendChild(d)});
 const g=$('groupes');
 for(const [nom,cles] of Object.entries(DESC.groupes)){const det=document.createElement('details');if(nom.startsWith('Prix'))det.open=true;
  det.innerHTML=`<summary>${nom}</summary>`;cles.forEach(k=>{const c=DESC.champs[k];if(!c)return;det.appendChild(ligne(k,c))});g.appendChild(det)}
 $('reset').onclick=()=>{etat.surcharges={};etat.choix={};document.querySelectorAll('.p input').forEach(i=>{i.value=i.dataset.def;i.parentElement.classList.remove('mod')});
  DESC.options.forEach(k=>$('o_'+k).checked=!!DESC.champs[k].valeur);$('gazorg').checked=false;$('chaleur').value='huile';document.querySelectorAll('.sanseffet').forEach(x=>x.remove());remplirEntree();lancer(0)};
 remplirEntree();lancer(0);
}
function ligne(k,c){const d=document.createElement('div');d.className='p';d.dataset.k=k;
 d.innerHTML=`<div class="lab">${c.label}<br><span class="mut">${c.unite||''}</span></div><input type="number" step="any" value="${c.valeur}" data-def="${c.valeur}">
 <div class="meta">${badge(c.statut)}${conf(c.confiance)} ${c.source}${c.type_decision?' ; '+c.type_decision:''}${c.note?'<br>'+c.note:''}</div>`;
 const i=d.querySelector('input');i.oninput=()=>{const v=parseFloat(String(i.value).replace(',','.'));if(isNaN(v))return;
  if(v==parseFloat(i.dataset.def)){delete etat.surcharges[k];d.classList.remove('mod')}else{etat.surcharges[k]=v;d.classList.add('mod')}champModifie=k;lancer()};
 return d}
function majScen(){document.querySelectorAll('#scen button').forEach(b=>b.classList.toggle('on',b.dataset.s==etat.scenario))}
function remplirEntree(){const f=DESC.flux[etat.flux],s=$('entree');s.innerHTML='';
 f.prix_entree.choix.forEach(k=>{const c=DESC.champs[k];s.add(new Option(`${c.label} : ${c.valeur} EUR/t`,k))});
 s.value=etat.choix.prix_entree||f.prix_entree.defaut;
 $('fluxInfo').textContent=f.annexe+'. Bilan energetique : '+(f.bilan_energie||'');
 $('chaleur').value=etat.choix.source_chaleur||'huile'}
// Recalcul automatique : 800 ms apres la derniere frappe (0 pour un choix dans une liste) ; une reponse plus ancienne
// que la derniere demande est ignoree, pour qu'un resultat perime n'ecrase jamais le bon.
function lancer(delai=800){clearTimeout(minuterie);$('etat').textContent='Recalcul...';$('etat').className='run';minuterie=setTimeout(calcul,delai)}
function empreinte(r){const s=r.structure_defaut;return JSON.stringify([r.capex.total,r.synthese_an3,s.annees.map(l=>l.cash_flow_projet),s.annees.map(l=>l.cash_flow_actionnaire)])}
async function calcul(){
 const n=++seq, k=champModifie; champModifie=null;
 let r;try{r=await (await fetch('/model/api/calcul',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(etat)})).json()}
 catch(e){if(n===seq){$('err').textContent='Erreur de connexion : '+e;$('etat').textContent=''}return}
 if(n!==seq)return;
 if(r.erreur){$('err').textContent=r.erreur;$('etat').textContent='';return}$('err').textContent='';
 const e=empreinte(r);
 if(k){const lig=document.querySelector(`.p[data-k="${k}"]`);if(lig){let m=lig.querySelector('.sanseffet');
  if(dernier!==null&&e===dernier){if(!m){m=document.createElement('div');m.className='sanseffet';lig.appendChild(m)}
   m.textContent='Sans effet sur le flux, le scenario et les options choisis (voir les alertes).'}else if(m)m.remove()}}
 dernier=e;afficher(r);
 $('etat').className='';$('etat').textContent='Recalcule a '+new Date().toLocaleTimeString('fr-FR')+(Object.keys(etat.surcharges).length?' ; '+Object.keys(etat.surcharges).length+' valeur(s) modifiee(s)':'')}
function afficher(r){
 const s=r.structure_defaut,f=r.structure_fonds_propres,a3=r.synthese_an3;
 const k=[['CAPEX (hors transport)',fmtM(r.capex.total)],['Tonnage nominal',fmt(r.tonnage_nominal,0)+' t/an'],
  ['Chiffre d affaires an 3',fmtM(a3.chiffre_affaires)],['EBITDA an 3',fmtM(a3.ebitda)],['Marge EBITDA an 3',pct(a3.marge_ebitda)],
  ['TRI projet',pct(s.tri_projet)],[`TRI fonds propres (dette ${pct(s.part_dette)})`,pct(s.tri_fonds_propres)],
  ['TRI 100 % fonds propres',pct(f.tri_fonds_propres)],['Retour sur investissement',s.retour_annees==null?'non atteint':fmt(s.retour_annees,1)+' ans'],
  [`Cash cumule / CAPEX sur ${s.annees.length} ans`,pct(s.roi_horizon)]];
 $('kpis').innerHTML=k.map(([n,v])=>`<div class="kpi"><div class="n">${n}</div><div class="v ${String(v).startsWith('-')?'neg':''}">${v}</div></div>`).join('');
 const noms={huile:'Huile d hydrocarbures',gaz_hc:'Gaz d hydrocarbures',char:'Char',liquide:'Liquide oxygene (a traiter)',gaz_org:'Gaz organique',
  eau:'Eau du dechet (a traiter)',inertes:'Inertes a eliminer',metaux:'Metaux contenus',non_alloue:'Masse non allouee',non_alloue_liq:'dont liquide',non_alloue_gaz:'dont gaz',fines:'Fines non attribuees'};
 let h='<tr><th>Produit</th><th>kg/t</th><th>Calcul</th><th>Confiance</th><th>Statut</th><th>Hypotheses</th></tr>';
 for(const [p,c] of Object.entries(r.calculs)){if(p.startsWith('_'))continue;
  h+=`<tr><td title="${c.description}">${noms[p]||p}</td><td>${fmt(c.kg_t,1)}</td><td>${c.id}</td><td>${c.confiance==null?'n.d.':c.confiance+' %'}</td><td>${badge(c.statut)}</td><td>${c.hypotheses.join(', ')}</td></tr>`}
 $('bilan').innerHTML=h;
 const e=r.energie,rv=r.recettes_eur_t,cv=r.charges_variables_eur_t;
 const lig=[['Besoin du bruleur (D-072)',fmt(e.besoin_mj_t,0)+' MJ/t'],['Gaz d hydrocarbures',fmt(e.gaz_hc_mj_t,0)+' MJ/t'],['Gaz organique (option)',fmt(e.gaz_organique_mj_t,0)+' MJ/t'],
  ['Couverture',fmt(e.couverture,2)],['Deficit',fmt(e.deficit_mj_t,0)+' MJ/t'],['Huile brulee',fmt(e.huile_brulee_kg_t,1)+' kg/t'],['Char brule',fmt(e.char_brule_kg_t,1)+' kg/t'],
  ['Gazole achete',fmt(e.gazole_l_t,1)+' L/t'],['Hydrogene recupere',fmt(e.h2_kg_t,2)+' kg/t'],['Prix de l huile vendue (apres facteur)',fmt(r.prix_huile_eur_t,1)+' EUR/t'],
  ...Object.entries(rv).map(([k,v])=>['Recette '+k,fmt(v,2)+' EUR/t entrante']),...Object.entries(cv).map(([k,v])=>['Charge '+k,fmt(v,2)+' EUR/t entrante'])];
 $('energie').innerHTML='<tr><th>Grandeur</th><th>Valeur</th></tr>'+lig.map(([a,b])=>`<tr><td>${a}</td><td>${b}</td></tr>`).join('');
 const cols=[['tonnage','Tonnage',v=>fmt(v,0)],['chiffre_affaires','CA',fmtM],['charges','Charges',fmtM],['ebitda','EBITDA',fmtM],['amortissement','Amort.',fmtM],
  ['interets','Interets',fmtM],['impot','IS',fmtM],['resultat_net','Resultat net',fmtM],['cash_flow_projet','CF projet',fmtM],['cumul_projet','Cumul projet',fmtM],
  ['cash_flow_actionnaire','CF actionnaire',fmtM],['cumul_actionnaire','Cumul actionnaire',fmtM]];
 const det=Object.keys(s.annees[0]).filter(x=>x.startsWith('rec_')||x.startsWith('ch_'));
 let t='<tr><th>Ligne</th>'+s.annees.map(l=>`<th>An ${l.annee}</th>`).join('')+'</tr>';
 cols.forEach(([c,n,fn])=>{t+=`<tr><td><b>${n}</b></td>`+s.annees.map(l=>`<td class="${l[c]<0?'neg':''}">${fn(l[c])}</td>`).join('')+'</tr>'});
 det.forEach(c=>{t+=`<tr><td class="mut">${c.replace('rec_','recette ').replace('ch_','charge ')}</td>`+s.annees.map(l=>`<td class="mut">${fmtM(l[c])}</td>`).join('')+'</tr>'});
 $('annees').innerHTML=t;
 $('capex').innerHTML='<tr><th>Poste</th><th>Montant</th></tr>'+Object.entries(r.capex.postes).map(([k,v])=>`<tr><td>${k}</td><td>${fmtM(v)}</td></tr>`).join('')
  +`<tr><td>aleas</td><td>${fmtM(r.capex.aleas)}</td></tr><tr><td><b>Total</b></td><td><b>${fmtM(r.capex.total)}</b></td></tr>`;
 const opt=k=>(k in etat.surcharges)?!!etat.surcharges[k]:!!DESC.champs[k].valeur, ex=[], hu=(r.calculs.huile||{}).kg_t;
 if(e.huile_brulee_kg_t>0&&hu!=null&&e.huile_brulee_kg_t>=hu-0.01)ex.push("Toute l'huile produite est brulee pour couvrir le deficit de chaleur (D-069) : les prix, le facteur de qualite et les parts des fractions d'huile sont sans effet sur ce flux.");
 if(!(e.gazole_l_t>0))ex.push("Aucun gazole n'est achete : le prix du fioul est sans effet.");
 if(!opt('compter_metaux'))ex.push("Option revenu des metaux desactivee : les prix de la ferraille et de l'aluminium sont sans effet sur les OMR et les DAE.");
 if(!opt('compter_hydrogene'))ex.push("Option hydrogene desactivee : prix et recuperation de l'hydrogene sans effet.");
 ex.push("Seul le prix d'entree choisi dans la liste du haut est utilise ; les prix d'entree des autres gisements sont sans effet.");
 $('alertes').innerHTML=r.alertes.map(a=>`<li>${a}</li>`).join('')+ex.map(a=>`<li class="mut">${a}</li>`).join('');
}
init();
</script></body></html>"""
