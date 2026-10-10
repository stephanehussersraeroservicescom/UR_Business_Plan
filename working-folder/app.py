"""
Flask app pour Urban Rig — rapport HTML + assistant IA pour modifier les parametres YAML.
Routes :
  GET  /                   -> rapport.html (parametres par defaut)
  POST /scenario           -> rapport HTML avec surcharges JSON
  GET  /api/kpi            -> JSON des grandeurs calculees
  GET  /healthz            -> "ok" 200
  POST /assistant/chat     -> chat avec l'IA (modifie les YAML)
  POST /assistant/apply    -> applique une modification validee
  GET  /assistant/history  -> historique des modifications
  GET  /assistant/versions -> liste des commits git sur params/
  POST /assistant/rollback -> revient a un commit git
  POST /assistant/upload   -> upload d'un document de preuve
"""
import json
import os
import re
import sys
from pathlib import Path
from werkzeug.utils import secure_filename

from flask import Flask, Response, jsonify, request, session

sys.path.insert(0, str(Path(__file__).resolve().parent))
from engine.modele import executer
from engine.rapport import generer
from engine.assistant import (
    interroger,
    appliquer_modification,
    historique_recent,
    lister_versions_git,
    rollback_vers,
)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "ur-secret-dev-2024")

OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(exist_ok=True)

PREUVES_DIR = Path(__file__).resolve().parent / "reference" / "preuves"
PREUVES_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {"pdf", "xlsx", "xls", "docx", "doc", "csv", "png", "jpg", "jpeg"}

# Stockage en memoire de l'historique de conversation par session
# (simple dict en RAM — suffisant pour usage collaboratif leger)
_conversations: dict = {}


_ASSISTANT_INJECT = """
<style>
#ur-assistant-btn {
  position: fixed; bottom: 28px; right: 28px; z-index: 9000;
  background: #4f7cff; color: #fff; border: none; border-radius: 50%;
  width: 56px; height: 56px; font-size: 22px; cursor: pointer;
  box-shadow: 0 4px 20px rgba(79,124,255,.5);
  transition: transform .15s, box-shadow .15s;
}
#ur-assistant-btn:hover { transform: scale(1.08); box-shadow: 0 6px 28px rgba(79,124,255,.7); }
#ur-assistant-panel {
  position: fixed; bottom: 96px; right: 28px; z-index: 9000;
  width: 420px; max-width: calc(100vw - 40px);
  background: #1a1d27; border: 1px solid #2d3148; border-radius: 14px;
  box-shadow: 0 8px 40px rgba(0,0,0,.6);
  display: none; flex-direction: column; overflow: hidden;
  font-family: system-ui, sans-serif; font-size: 14px;
}
#ur-assistant-panel.open { display: flex; }
#ura-header {
  background: #252836; padding: 12px 16px;
  display: flex; align-items: center; gap: 10px;
  border-bottom: 1px solid #2d3148;
}
#ura-header span { font-weight: 600; color: #e8eaf0; flex: 1; }
#ura-header .badge { background: #4f7cff; color: #fff; padding: 2px 8px;
  border-radius: 20px; font-size: 11px; }
#ura-header input { background: #1a1d27; border: 1px solid #3d4166;
  border-radius: 6px; padding: 3px 8px; color: #e8eaf0; font-size: 12px; width: 110px; }
#ura-msgs { height: 300px; overflow-y: auto; padding: 12px; display: flex;
  flex-direction: column; gap: 8px; }
.ura-msg { padding: 8px 12px; border-radius: 8px; line-height: 1.4; max-width: 90%; }
.ura-msg.user { background: #4f7cff; color: #fff; align-self: flex-end; white-space: pre-wrap; }
.ura-msg.assistant { background: #252836; color: #e8eaf0; align-self: flex-start; white-space: pre-wrap; }
.ura-msg.system { background: #1e2235; color: #9ba3b4; align-self: center;
  font-size: 11px; border: 1px solid #2d3148; border-radius: 6px; padding: 5px 10px; }
.ura-mod-card { background: #1e2d1e; border: 1px solid #2d4a2d; border-radius: 8px;
  padding: 8px 12px; align-self: flex-start; max-width: 90%; }
.ura-mod-card .mp { color: #22c55e; font-family: monospace; font-weight: 600; }
.ura-mod-card .mv { color: #f59e0b; }
.ura-mod-card .mr { color: #9ba3b4; font-size: 11px; margin-top: 3px; }
.ura-apply-btn { margin-top: 6px; background: #22c55e; color: #000; border: none;
  border-radius: 5px; padding: 4px 12px; cursor: pointer; font-size: 12px; font-weight: 600; }
.ura-apply-btn:disabled { opacity: .4; cursor: default; }
#ura-input-row { padding: 10px 12px; background: #252836;
  border-top: 1px solid #2d3148; display: flex; gap: 6px; align-items: flex-end; }
#ura-input { flex: 1; background: #1a1d27; border: 1px solid #3d4166; border-radius: 7px;
  padding: 7px 10px; color: #e8eaf0; font-size: 13px; resize: none;
  min-height: 36px; max-height: 100px; line-height: 1.4; }
#ura-input:focus { outline: none; border-color: #4f7cff; }
#ura-voice { background: #252836; border: 1px solid #3d4166; border-radius: 7px;
  padding: 7px 10px; cursor: pointer; font-size: 14px; color: #9ba3b4; }
#ura-voice.listening { background: #ef4444; color: #fff; border-color: #ef4444; }
#ura-send { background: #4f7cff; color: #fff; border: none; border-radius: 7px;
  padding: 7px 14px; cursor: pointer; font-weight: 600; font-size: 13px; }
#ura-send:disabled { opacity: .4; }
#ura-loading { display: none; color: #9ba3b4; font-size: 12px; padding: 4px 12px; }
.ura-spinner { display: inline-block; width: 12px; height: 12px;
  border: 2px solid #9ba3b4; border-top-color: #4f7cff; border-radius: 50%;
  animation: spin .8s linear infinite; vertical-align: middle; margin-right: 5px; }
@keyframes spin { to { transform: rotate(360deg); } }
</style>

<button id="ur-assistant-btn" title="Assistant IA">🤖</button>

<div id="ur-assistant-panel">
  <div id="ura-header">
    <span>🔥 Assistant IA</span>
    <span class="badge">Urban Rig</span>
    <input id="ura-auteur" type="text" placeholder="Votre nom">
  </div>
  <div id="ura-msgs">
    <div class="ura-msg system">Bonjour. Posez-moi une question sur les parametres ou demandez une modification.<br><em>Ex: "Le taux d'interet de 12% est trop eleve, corrige-le a 6%."</em></div>
  </div>
  <div id="ura-loading"><span class="ura-spinner"></span>Analyse en cours...</div>
  <div id="ura-input-row">
    <textarea id="ura-input" rows="1" placeholder="Votre message... (Entree pour envoyer)"></textarea>
    <button id="ura-voice" title="Voix">🎤</button>
    <button id="ura-send">➤</button>
  </div>
</div>

<script>
(function() {
  const SESSION_ID = 'ur-' + Math.random().toString(36).slice(2, 8);
  let uraRec = null, uraListening = false;

  document.getElementById('ur-assistant-btn').addEventListener('click', () => {
    document.getElementById('ur-assistant-panel').classList.toggle('open');
  });

  // Voix
  const SR = window.webkitSpeechRecognition || window.SpeechRecognition;
  if (SR) {
    uraRec = new SR();
    uraRec.lang = 'fr-FR';
    uraRec.interimResults = false;
    uraRec.onresult = e => { document.getElementById('ura-input').value += e.results[0][0].transcript; };
    uraRec.onend = () => { uraListening = false; document.getElementById('ura-voice').classList.remove('listening'); };
  } else {
    document.getElementById('ura-voice').style.display = 'none';
  }
  document.getElementById('ura-voice').addEventListener('click', () => {
    if (!uraRec) return;
    if (uraListening) { uraRec.stop(); }
    else { uraRec.start(); uraListening = true; document.getElementById('ura-voice').classList.add('listening'); }
  });

  function addMsg(role, text, mods) {
    const c = document.getElementById('ura-msgs');
    const d = document.createElement('div');
    d.className = 'ura-msg ' + role;
    d.textContent = text;
    c.appendChild(d);
    if (mods && mods.length) {
      mods.forEach(mod => {
        const mc = document.createElement('div');
        mc.className = 'ura-mod-card';
        mc.innerHTML = `<div><span class="mp">${mod.parametre}</span> &rarr; <span class="mv">${mod.valeur}</span></div>
          <div class="mr">${mod.raison}</div>
          <button class="ura-apply-btn" data-p="${mod.parametre}" data-v="${mod.valeur}" data-r="${encodeURIComponent(mod.raison)}">✓ Appliquer</button>`;
        mc.querySelector('.ura-apply-btn').addEventListener('click', applyMod);
        c.appendChild(mc);
      });
    }
    c.scrollTop = c.scrollHeight;
  }

  async function applyMod(e) {
    const btn = e.currentTarget;
    const p = btn.dataset.p, v = isNaN(btn.dataset.v) ? btn.dataset.v : parseFloat(btn.dataset.v);
    const r = decodeURIComponent(btn.dataset.r);
    const auteur = document.getElementById('ura-auteur').value || 'utilisateur';
    btn.disabled = true; btn.textContent = '...';
    try {
      const res = await fetch('/assistant/apply', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({parametre:p, valeur:v, raison:r, auteur})
      });
      const d = await res.json();
      btn.textContent = d.succes ? '✓ Applique' : '✗ Erreur';
      addMsg('system', d.succes ? '✓ ' + d.message : 'Erreur: ' + d.message);
    } catch(err) { btn.textContent = '✗'; btn.disabled = false; }
  }

  async function sendMsg() {
    const inp = document.getElementById('ura-input');
    const text = inp.value.trim();
    if (!text) return;
    const auteur = document.getElementById('ura-auteur').value || 'utilisateur';
    inp.value = ''; inp.style.height = 'auto';
    addMsg('user', text);
    document.getElementById('ura-send').disabled = true;
    document.getElementById('ura-loading').style.display = 'block';
    try {
      const res = await fetch('/assistant/chat', {
        method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({message:text, session_id:SESSION_ID, auteur})
      });
      const d = await res.json();
      document.getElementById('ura-loading').style.display = 'none';
      document.getElementById('ura-send').disabled = false;
      if (d.erreur) addMsg('system', 'Erreur: ' + d.erreur);
      else addMsg('assistant', d.reponse, d.modifications);
    } catch(err) {
      document.getElementById('ura-loading').style.display = 'none';
      document.getElementById('ura-send').disabled = false;
      addMsg('system', 'Erreur reseau: ' + err.message);
    }
  }

  document.getElementById('ura-send').addEventListener('click', sendMsg);
  document.getElementById('ura-input').addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMsg(); }
    e.target.style.height = 'auto';
    e.target.style.height = Math.min(e.target.scrollHeight, 100) + 'px';
  });
})();
</script>
"""


def _construire(surcharges: dict) -> str:
    reg, m = executer(surcharges)
    chemin = OUT / "_rapport_tmp.html"
    generer(reg, m, chemin, surcharges)
    html = chemin.read_text(encoding="utf-8")
    # Injecter le panneau assistant avant </body>
    html = html.replace("</body>", _ASSISTANT_INJECT + "\n</body>")
    return html


def _allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------------------------------------------------------------------
# Routes rapport existantes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    html_content = _construire({})
    return Response(html_content, mimetype="text/html")


@app.route("/scenario", methods=["POST"])
def scenario():
    try:
        surcharges = request.get_json(force=True) or {}
        html_content = _construire(surcharges)
        return Response(html_content, mimetype="text/html")
    except Exception as e:
        return jsonify({"erreur": str(e)}), 400


@app.route("/api/kpi")
def api_kpi():
    try:
        surcharges_raw = request.args.get("surcharges", "{}")
        surcharges = json.loads(surcharges_raw)
        reg, m = executer(surcharges)
        res = {k: {"valeur": v["valeur"], "unite": v["unite"]} for k, v in m.r.items()}
        return jsonify({"resultats": res, "surcharges": surcharges})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 400


@app.route("/healthz")
def health():
    return "ok", 200


# ---------------------------------------------------------------------------
# Routes assistant IA
# ---------------------------------------------------------------------------

@app.route("/assistant/chat", methods=["POST"])
def assistant_chat():
    """
    Envoie un message a l'assistant IA.
    Body JSON: {"message": str, "session_id": str (optionnel), "auteur": str (optionnel)}
    """
    try:
        data = request.get_json(force=True) or {}
        message = data.get("message", "").strip()
        session_id = data.get("session_id", "default")
        auteur = data.get("auteur", "utilisateur")

        if not message:
            return jsonify({"erreur": "Message vide."}), 400

        # Recuperer l'historique de conversation
        historique_conv = _conversations.get(session_id, [])

        # Interroger l'IA
        resultat = interroger(message, historique_conv)

        if resultat["erreur"]:
            return jsonify({"erreur": resultat["erreur"]}), 500

        # Mettre a jour l'historique de conversation
        historique_conv.append({"role": "user", "content": message})
        historique_conv.append({"role": "assistant", "content": resultat["reponse"]})
        # Garder les 20 derniers tours max
        _conversations[session_id] = historique_conv[-40:]

        return jsonify({
            "reponse": resultat["reponse"],
            "modifications": resultat["modifications"],
            "session_id": session_id,
        })

    except Exception as e:
        return jsonify({"erreur": str(e)}), 500


@app.route("/assistant/apply", methods=["POST"])
def assistant_apply():
    """
    Applique une modification validee par l'utilisateur.
    Body JSON: {"parametre": str, "valeur": any, "raison": str, "auteur": str}
    """
    try:
        data = request.get_json(force=True) or {}
        parametre = data.get("parametre", "").strip()
        valeur = data.get("valeur")
        raison = data.get("raison", "Modification via assistant IA")
        auteur = data.get("auteur", "utilisateur")

        if not parametre or valeur is None:
            return jsonify({"erreur": "Parametre et valeur requis."}), 400

        resultat = appliquer_modification(parametre, valeur, raison, auteur)
        return jsonify(resultat)

    except Exception as e:
        return jsonify({"erreur": str(e)}), 500


@app.route("/assistant/history")
def assistant_history():
    """Retourne l'historique des modifications."""
    n = int(request.args.get("n", 20))
    return jsonify({"historique": historique_recent(n)})


@app.route("/assistant/versions")
def assistant_versions():
    """Retourne la liste des commits git sur params/."""
    n = int(request.args.get("n", 20))
    return jsonify({"versions": lister_versions_git(n)})


@app.route("/assistant/rollback", methods=["POST"])
def assistant_rollback():
    """
    Revient a un commit git specifique pour les params.
    Body JSON: {"sha": str}
    """
    try:
        data = request.get_json(force=True) or {}
        sha = data.get("sha", "").strip()
        if not sha or not re.match(r"^[0-9a-f]{7,40}$", sha):
            return jsonify({"erreur": "SHA git invalide."}), 400
        resultat = rollback_vers(sha)
        return jsonify(resultat)
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500


@app.route("/assistant/upload", methods=["POST"])
def assistant_upload():
    """
    Upload d'un document de preuve dans reference/preuves/.
    Form: file=<fichier>, code=<code_evidence>, description=<str>
    """
    try:
        if "file" not in request.files:
            return jsonify({"erreur": "Aucun fichier fourni."}), 400

        f = request.files["file"]
        code = request.form.get("code", "").strip().upper()
        description = request.form.get("description", "")

        if not f.filename:
            return jsonify({"erreur": "Nom de fichier vide."}), 400
        if not _allowed_file(f.filename):
            return jsonify({"erreur": f"Extension non autorisee. Types acceptes: {', '.join(ALLOWED_EXTENSIONS)}"}), 400

        ext = f.filename.rsplit(".", 1)[1].lower()
        if code:
            filename = secure_filename(f"{code}.{ext}")
        else:
            filename = secure_filename(f.filename)

        chemin = PREUVES_DIR / filename
        f.save(chemin)

        return jsonify({
            "succes": True,
            "fichier": filename,
            "chemin": str(chemin.relative_to(chemin.parents[3])),
            "taille": chemin.stat().st_size,
        })

    except Exception as e:
        return jsonify({"erreur": str(e)}), 500


@app.route("/assistant")
def assistant_ui():
    """Page HTML autonome de l'assistant IA (fallback si non integre dans le rapport)."""
    html = _generer_ui_assistant()
    return Response(html, mimetype="text/html")


def _generer_ui_assistant() -> str:
    """Genere la page HTML de l'assistant IA."""
    return """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Assistant IA — Urban Rig</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {
    --bg: #0f1117; --bg2: #1a1d27; --bg3: #252836;
    --fg: #e8eaf0; --fg2: #9ba3b4; --accent: #4f7cff;
    --green: #22c55e; --red: #ef4444; --yellow: #f59e0b;
    --radius: 10px; --gap: 12px;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); color: var(--fg); font-family: system-ui, sans-serif;
         font-size: 14px; display: flex; flex-direction: column; height: 100vh; }

  #header { background: var(--bg2); border-bottom: 1px solid #2d3148;
            padding: 12px 20px; display: flex; align-items: center; gap: 12px; }
  #header h1 { font-size: 16px; font-weight: 600; }
  #header .badge { background: var(--accent); color: #fff; padding: 2px 8px;
                   border-radius: 20px; font-size: 11px; }
  #auteur-input { margin-left: auto; background: var(--bg3); border: 1px solid #3d4166;
                  border-radius: 6px; padding: 4px 10px; color: var(--fg); font-size: 13px; width: 160px; }

  #main { display: flex; flex: 1; overflow: hidden; }

  #chat-panel { flex: 1; display: flex; flex-direction: column; }
  #messages { flex: 1; overflow-y: auto; padding: 16px 20px; display: flex; flex-direction: column; gap: 12px; }

  .msg { max-width: 85%; padding: 10px 14px; border-radius: var(--radius); line-height: 1.5; }
  .msg.user { background: var(--accent); color: #fff; align-self: flex-end; border-bottom-right-radius: 3px; }
  .msg.assistant { background: var(--bg3); align-self: flex-start; border-bottom-left-radius: 3px; white-space: pre-wrap; }
  .msg.system { background: #1e2235; color: var(--fg2); align-self: center; font-size: 12px;
                border: 1px solid #2d3148; border-radius: 6px; padding: 6px 12px; }

  .mod-card { background: #1e2d1e; border: 1px solid #2d4a2d; border-radius: 8px;
              padding: 10px 14px; margin-top: 8px; }
  .mod-card .mod-header { font-size: 11px; color: var(--fg2); margin-bottom: 4px; }
  .mod-card .mod-param { font-family: monospace; color: var(--green); font-weight: 600; }
  .mod-card .mod-value { color: var(--yellow); }
  .mod-card .mod-reason { font-size: 12px; color: var(--fg2); margin-top: 4px; }
  .mod-card .btn-apply { margin-top: 8px; background: var(--green); color: #000;
                          border: none; border-radius: 6px; padding: 5px 14px;
                          cursor: pointer; font-size: 12px; font-weight: 600; }
  .mod-card .btn-apply:hover { opacity: 0.85; }
  .mod-card .btn-apply:disabled { opacity: 0.4; cursor: default; }

  #input-area { padding: 12px 20px; background: var(--bg2); border-top: 1px solid #2d3148;
                display: flex; gap: 8px; align-items: flex-end; }
  #msg-input { flex: 1; background: var(--bg3); border: 1px solid #3d4166; border-radius: 8px;
               padding: 9px 12px; color: var(--fg); font-size: 14px; resize: none;
               min-height: 42px; max-height: 120px; line-height: 1.4; }
  #msg-input:focus { outline: none; border-color: var(--accent); }
  #btn-send { background: var(--accent); color: #fff; border: none; border-radius: 8px;
              padding: 9px 18px; cursor: pointer; font-weight: 600; white-space: nowrap; }
  #btn-send:hover { opacity: 0.85; }
  #btn-send:disabled { opacity: 0.4; }
  #btn-voice { background: var(--bg3); border: 1px solid #3d4166; border-radius: 8px;
               padding: 9px 12px; cursor: pointer; font-size: 16px; color: var(--fg2); }
  #btn-voice.listening { background: var(--red); color: #fff; border-color: var(--red); }

  #side-panel { width: 280px; background: var(--bg2); border-left: 1px solid #2d3148;
                display: flex; flex-direction: column; overflow: hidden; }
  #side-tabs { display: flex; border-bottom: 1px solid #2d3148; }
  .side-tab { flex: 1; padding: 10px; text-align: center; cursor: pointer; font-size: 12px;
              color: var(--fg2); border-bottom: 2px solid transparent; }
  .side-tab.active { color: var(--fg); border-bottom-color: var(--accent); }
  #side-content { flex: 1; overflow-y: auto; padding: 12px; }

  .history-item { padding: 8px; border-radius: 6px; background: var(--bg3);
                  margin-bottom: 6px; font-size: 12px; }
  .history-item .hi-param { color: var(--green); font-family: monospace; }
  .history-item .hi-ts { color: var(--fg2); font-size: 11px; }
  .history-item .hi-reason { color: var(--fg2); margin-top: 3px; }

  .version-item { padding: 7px 8px; border-radius: 6px; background: var(--bg3);
                  margin-bottom: 5px; font-size: 12px; display: flex; align-items: center; gap: 8px; }
  .version-item .vi-sha { font-family: monospace; color: var(--accent); }
  .version-item .btn-rollback { margin-left: auto; background: transparent; border: 1px solid var(--red);
                                 color: var(--red); border-radius: 4px; padding: 2px 8px;
                                 cursor: pointer; font-size: 11px; }

  #upload-area { padding: 12px; }
  #upload-area input[type=text] { width: 100%; background: var(--bg3); border: 1px solid #3d4166;
                                   border-radius: 6px; padding: 7px 10px; color: var(--fg);
                                   font-size: 13px; margin-bottom: 6px; }
  #upload-area input[type=file] { font-size: 12px; color: var(--fg2); margin-bottom: 8px; }
  #btn-upload { background: var(--accent); color: #fff; border: none; border-radius: 6px;
                padding: 7px 16px; cursor: pointer; font-size: 13px; font-weight: 600; }

  #loading { display: none; align-self: center; color: var(--fg2); font-size: 13px; }
  .spinner { display: inline-block; width: 14px; height: 14px; border: 2px solid var(--fg2);
             border-top-color: var(--accent); border-radius: 50%;
             animation: spin 0.8s linear infinite; vertical-align: middle; margin-right: 6px; }
  @keyframes spin { to { transform: rotate(360deg); } }

  @media (max-width: 600px) {
    #side-panel { display: none; }
  }
</style>
</head>
<body>

<div id="header">
  <span>🔥</span>
  <h1>Assistant IA — Urban Rig URC-2000</h1>
  <span class="badge">Phase 1</span>
  <input id="auteur-input" type="text" placeholder="Votre nom" value="">
</div>

<div id="main">
  <div id="chat-panel">
    <div id="messages">
      <div class="msg system">
        Bonjour. Je suis l'assistant IA du modele financier Urban Rig.<br>
        Posez-moi une question sur les parametres ou demandez-moi de modifier une valeur.<br>
        <em>Exemple : "Le taux d'interet de 12% avec 70% de dette n'est pas realiste, corrige-le."</em>
      </div>
    </div>
    <div id="loading"><span class="spinner"></span>L'assistant analyse...</div>
    <div id="input-area">
      <textarea id="msg-input" placeholder="Votre message... (Entree pour envoyer, Maj+Entree pour saut de ligne)" rows="1"></textarea>
      <button id="btn-voice" title="Saisie vocale">🎤</button>
      <button id="btn-send">Envoyer</button>
    </div>
  </div>

  <div id="side-panel">
    <div id="side-tabs">
      <div class="side-tab active" data-tab="history">Historique</div>
      <div class="side-tab" data-tab="versions">Versions</div>
      <div class="side-tab" data-tab="upload">Upload</div>
    </div>
    <div id="side-content">
      <div id="tab-history">Chargement...</div>
      <div id="tab-versions" style="display:none">Chargement...</div>
      <div id="tab-upload" style="display:none">
        <div id="upload-area">
          <p style="font-size:12px;color:var(--fg2);margin-bottom:8px">Ajouter un document de preuve</p>
          <input type="text" id="upload-code" placeholder="Code (ex: SEACORAL-JP)">
          <input type="text" id="upload-desc" placeholder="Description courte">
          <input type="file" id="upload-file" accept=".pdf,.xlsx,.xls,.docx,.doc,.csv,.png,.jpg">
          <button id="btn-upload">Uploader</button>
          <div id="upload-result" style="margin-top:8px;font-size:12px"></div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
const SESSION_ID = 'ur-' + Math.random().toString(36).slice(2, 9);
let recognition = null;
let isListening = false;

// --- Voix ---
function initVoice() {
  const SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
  if (!SpeechRecognition) {
    document.getElementById('btn-voice').style.display = 'none';
    return;
  }
  recognition = new SpeechRecognition();
  recognition.lang = 'fr-FR';
  recognition.interimResults = false;
  recognition.continuous = false;
  recognition.onresult = (e) => {
    const txt = e.results[0][0].transcript;
    document.getElementById('msg-input').value += txt;
  };
  recognition.onend = () => {
    isListening = false;
    document.getElementById('btn-voice').classList.remove('listening');
  };
}

document.getElementById('btn-voice').addEventListener('click', () => {
  if (!recognition) return;
  if (isListening) {
    recognition.stop();
  } else {
    recognition.lang = document.documentElement.lang || 'fr-FR';
    recognition.start();
    isListening = true;
    document.getElementById('btn-voice').classList.add('listening');
  }
});

// --- Chat ---
function addMessage(role, text, modifications) {
  const msgs = document.getElementById('messages');
  const div = document.createElement('div');
  div.className = `msg ${role}`;
  div.textContent = text;
  msgs.appendChild(div);

  if (modifications && modifications.length > 0) {
    modifications.forEach(mod => {
      const card = document.createElement('div');
      card.className = 'msg assistant';
      card.style.maxWidth = '85%';
      card.innerHTML = `
        <div class="mod-card">
          <div class="mod-header">MODIFICATION PROPOSEE</div>
          <div><span class="mod-param">${mod.parametre}</span> &rarr; <span class="mod-value">${mod.valeur}</span></div>
          <div class="mod-reason">${mod.raison}</div>
          <button class="btn-apply" data-param="${mod.parametre}" data-val="${mod.valeur}" data-raison="${encodeURIComponent(mod.raison)}">
            ✓ Appliquer
          </button>
        </div>`;
      msgs.appendChild(card);
      card.querySelector('.btn-apply').addEventListener('click', applyMod);
    });
  }
  msgs.scrollTop = msgs.scrollHeight;
}

async function applyMod(e) {
  const btn = e.currentTarget;
  const parametre = btn.dataset.param;
  const valeur = isNaN(btn.dataset.val) ? btn.dataset.val : parseFloat(btn.dataset.val);
  const raison = decodeURIComponent(btn.dataset.raison);
  const auteur = document.getElementById('auteur-input').value || 'utilisateur';
  btn.disabled = true;
  btn.textContent = '...';
  try {
    const r = await fetch('/assistant/apply', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({parametre, valeur, raison, auteur}),
    });
    const data = await r.json();
    if (data.succes) {
      btn.textContent = '✓ Applique';
      btn.style.background = '#166534';
      addMessage('system', `✓ ${data.message}\n${data.git}`);
      refreshHistory();
      refreshVersions();
    } else {
      btn.textContent = '✗ Erreur';
      btn.disabled = false;
      addMessage('system', `Erreur: ${data.message}`);
    }
  } catch(err) {
    btn.textContent = '✗';
    btn.disabled = false;
  }
}

async function sendMessage() {
  const input = document.getElementById('msg-input');
  const text = input.value.trim();
  if (!text) return;
  const auteur = document.getElementById('auteur-input').value || 'utilisateur';
  input.value = '';
  input.style.height = 'auto';
  addMessage('user', text);
  document.getElementById('btn-send').disabled = true;
  document.getElementById('loading').style.display = 'flex';
  try {
    const r = await fetch('/assistant/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: text, session_id: SESSION_ID, auteur}),
    });
    const data = await r.json();
    document.getElementById('loading').style.display = 'none';
    document.getElementById('btn-send').disabled = false;
    if (data.erreur) {
      addMessage('system', `Erreur: ${data.erreur}`);
    } else {
      addMessage('assistant', data.reponse, data.modifications);
    }
  } catch(err) {
    document.getElementById('loading').style.display = 'none';
    document.getElementById('btn-send').disabled = false;
    addMessage('system', `Erreur reseau: ${err.message}`);
  }
}

document.getElementById('btn-send').addEventListener('click', sendMessage);
document.getElementById('msg-input').addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  // Auto-resize
  e.target.style.height = 'auto';
  e.target.style.height = Math.min(e.target.scrollHeight, 120) + 'px';
});

// --- Historique ---
async function refreshHistory() {
  try {
    const r = await fetch('/assistant/history?n=20');
    const data = await r.json();
    const container = document.getElementById('tab-history');
    if (!data.historique || data.historique.length === 0) {
      container.innerHTML = '<p style="color:var(--fg2);font-size:12px;padding:8px">Aucune modification encore.</p>';
      return;
    }
    container.innerHTML = [...data.historique].reverse().map(h => `
      <div class="history-item">
        <div class="hi-ts">${h.horodatage.replace('T',' ').slice(0,16)} — ${h.auteur || ''}</div>
        <div><span class="hi-param">${h.parametre}</span>: ${h.ancienne_valeur} &rarr; ${h.nouvelle_valeur}</div>
        <div class="hi-reason">${h.raison || ''}</div>
      </div>`).join('');
  } catch(e) {}
}

// --- Versions git ---
async function refreshVersions() {
  try {
    const r = await fetch('/assistant/versions?n=15');
    const data = await r.json();
    const container = document.getElementById('tab-versions');
    if (!data.versions || data.versions.length === 0) {
      container.innerHTML = '<p style="color:var(--fg2);font-size:12px;padding:8px">Aucun commit trouvé.</p>';
      return;
    }
    container.innerHTML = data.versions.map(v => `
      <div class="version-item">
        <span class="vi-sha">${v.sha}</span>
        <span style="flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--fg2);font-size:11px">${v.message}</span>
        <button class="btn-rollback" data-sha="${v.sha}">↩ Revert</button>
      </div>`).join('');
    container.querySelectorAll('.btn-rollback').forEach(btn => {
      btn.addEventListener('click', async () => {
        if (!confirm(`Revenir au commit ${btn.dataset.sha} ?`)) return;
        const r = await fetch('/assistant/rollback', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({sha: btn.dataset.sha}),
        });
        const data = await r.json();
        addMessage('system', data.succes ? `✓ Rollback vers ${btn.dataset.sha}` : `Erreur: ${data.message}`);
        refreshVersions();
      });
    });
  } catch(e) {}
}

// --- Upload ---
document.getElementById('btn-upload').addEventListener('click', async () => {
  const file = document.getElementById('upload-file').files[0];
  if (!file) return;
  const code = document.getElementById('upload-code').value.trim();
  const desc = document.getElementById('upload-desc').value.trim();
  const fd = new FormData();
  fd.append('file', file);
  if (code) fd.append('code', code);
  if (desc) fd.append('description', desc);
  const result = document.getElementById('upload-result');
  result.textContent = 'Upload en cours...';
  try {
    const r = await fetch('/assistant/upload', {method: 'POST', body: fd});
    const data = await r.json();
    if (data.succes) {
      result.style.color = 'var(--green)';
      result.textContent = `✓ ${data.fichier} (${Math.round(data.taille/1024)} Ko)`;
    } else {
      result.style.color = 'var(--red)';
      result.textContent = `Erreur: ${data.erreur}`;
    }
  } catch(e) {
    result.style.color = 'var(--red)';
    result.textContent = `Erreur: ${e.message}`;
  }
});

// --- Tabs ---
document.querySelectorAll('.side-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.side-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    document.querySelectorAll('[id^=tab-]').forEach(c => c.style.display = 'none');
    document.getElementById(`tab-${tab.dataset.tab}`).style.display = '';
  });
});

// Init
initVoice();
refreshHistory();
refreshVersions();
</script>
</body>
</html>"""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=False)
