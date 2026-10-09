"""
Flask app pour Urban Rig — sert le rapport HTML avec recalcul Python a la demande.
Routes :
  GET  /          -> rapport.html (parametres par defaut)
  POST /scenario  -> rapport HTML avec surcharges JSON { "nb_unites": 5, "gate_fee": 250 }
  GET  /api/kpi   -> JSON des grandeurs calculees
"""
import json
import os
import sys
from pathlib import Path

from flask import Flask, Response, jsonify, request

sys.path.insert(0, str(Path(__file__).resolve().parent))
from engine.modele import executer
from engine.rapport import generer

app = Flask(__name__)

OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(exist_ok=True)


def _construire(surcharges: dict) -> str:
    reg, m = executer(surcharges)
    chemin = OUT / "_rapport_tmp.html"
    generer(reg, m, chemin, surcharges)
    return chemin.read_text(encoding="utf-8")


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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=False)
