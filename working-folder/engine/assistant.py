"""
Assistant IA pour Urban Rig — modification des parametres YAML via langage naturel.
Utilise l'API Anthropic (cle via variable d'environnement ANTHROPIC_API_KEY).
"""
import json
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

import yaml

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

PARAMS_DIR = Path(__file__).resolve().parent.parent / "params"
PREUVES_DIR = Path(__file__).resolve().parent.parent / "reference" / "preuves"
DECISIONS_FILE = PARAMS_DIR / "_decisions.yaml"
HISTORY_FILE = PARAMS_DIR / "_historique_assistant.yaml"


def _charger_tous_params() -> dict:
    """Charge tous les fichiers YAML de params/ en un dictionnaire plat."""
    tous = {}
    for f in sorted(PARAMS_DIR.glob("*.yaml")):
        if f.name.startswith("_"):
            continue
        with open(f, encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        domaine = data.pop("_domaine", f.stem)
        for cle, val in data.items():
            if isinstance(val, dict) and "valeur" in val:
                tous[cle] = {**val, "_fichier": f.name, "_domaine": domaine}
    return tous


def _charger_evidence() -> dict:
    """Charge _evidence.yaml."""
    p = PARAMS_DIR / "_evidence.yaml"
    if not p.exists():
        return {}
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _sauver_param(cle: str, nouvelle_valeur, raison: str, auteur: str = "assistant_ia") -> bool:
    """Modifie la valeur d'un parametre dans son fichier YAML source."""
    params = _charger_tous_params()
    if cle not in params:
        return False
    fichier = PARAMS_DIR / params[cle]["_fichier"]
    with open(fichier, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if cle not in data:
        return False
    ancienne_valeur = data[cle].get("valeur")
    data[cle]["valeur"] = nouvelle_valeur
    if data[cle].get("statut") == "inconnu":
        data[cle]["statut"] = "hypothese"
    with open(fichier, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    _journaliser(cle, ancienne_valeur, nouvelle_valeur, raison, auteur, fichier.name)
    return True


def _journaliser(cle, ancienne, nouvelle, raison, auteur, fichier):
    """Ajoute une entree dans _historique_assistant.yaml."""
    historique = []
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, encoding="utf-8") as f:
            historique = yaml.safe_load(f) or []
    historique.append({
        "horodatage": datetime.utcnow().isoformat(),
        "auteur": auteur,
        "parametre": cle,
        "fichier": fichier,
        "ancienne_valeur": ancienne,
        "nouvelle_valeur": nouvelle,
        "raison": raison,
    })
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        yaml.dump(historique, f, allow_unicode=True, default_flow_style=False)


def _git_commit(message: str) -> str:
    """Commit tous les changements YAML avec un message documente."""
    repo = PARAMS_DIR.parent.parent
    try:
        subprocess.run(["git", "-C", str(repo), "add", "working-folder/params/"], check=True, capture_output=True)
        result = subprocess.run(
            ["git", "-C", str(repo), "commit", "-m", message],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return result.stderr.strip()
    except Exception as e:
        return f"Erreur git: {e}"


def _construire_contexte_systeme() -> str:
    """Construit le prompt systeme pour l'assistant."""
    params = _charger_tous_params()
    evidence = _charger_evidence()

    params_txt = []
    for cle, info in params.items():
        statut = info.get("statut", "?")
        valeur = info.get("valeur", "?")
        unite = info.get("unite", "")
        note = info.get("note", "")
        note_str = f" | Note: {note}" if note else ""
        params_txt.append(f"  {cle}: {valeur} {unite} [{statut}]{note_str}")

    preuves_txt = []
    for code, info in evidence.items():
        if isinstance(info, dict):
            fiabilite = info.get("fiabilite", "?")
            contenu = info.get("contenu", "")[:80]
            preuves_txt.append(f"  {code} [{fiabilite}]: {contenu}")

    return f"""Tu es l'assistant IA du modele financier Urban Rig URC-2000.
Tu aides a modifier les parametres YAML du modele de facon traceee et documentee.

PARAMETRES ACTUELS DU MODELE:
{chr(10).join(params_txt)}

DOCUMENTS DE PREUVE DISPONIBLES:
{chr(10).join(preuves_txt)}

REGLES:
1. Quand tu proposes une modification de parametre, utilise EXACTEMENT ce format JSON dans ta reponse:
   <MODIFICATION>
   {{"parametre": "nom_cle", "valeur": 123.45, "raison": "Explication detaillee du pourquoi"}}
   </MODIFICATION>

2. Tu peux proposer plusieurs modifications dans un seul message, chacune dans son propre bloc <MODIFICATION>.

3. Explique toujours POURQUOI tu proposes ce changement (source, logique, calcul).

4. Si une valeur est incertaine, dis-le clairement et propose une fourchette.

5. Pour les valeurs financieres (taux_interet, etc.), questionne la coherence interne.

6. Tu peux repondre en francais ou en anglais selon la langue de l'utilisateur.

7. Si on te demande l'historique, resume les derniers changements du fichier _historique_assistant.yaml.

8. Ne modifie jamais directement les fichiers — propose les modifications, l'utilisateur les valide.
"""


def interroger(message: str, historique_conv: list = None) -> dict:
    if not ANTHROPIC_AVAILABLE:
        return {"reponse": "", "modifications": [], "erreur": "Package 'anthropic' non installe."}

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return {"reponse": "", "modifications": [], "erreur": "ANTHROPIC_API_KEY non definie."}

    client = anthropic.Anthropic(api_key=api_key)

    messages = []
    if historique_conv:
        messages.extend(historique_conv[-10:])
    messages.append({"role": "user", "content": message})

    try:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2048,
            system=_construire_contexte_systeme(),
            messages=messages,
        )
        reponse_texte = response.content[0].text
    except Exception as e:
        return {"reponse": "", "modifications": [], "erreur": str(e)}

    modifications = []
    pattern = r"<MODIFICATION>\s*(.*?)\s*</MODIFICATION>"
    for match in re.finditer(pattern, reponse_texte, re.DOTALL):
        try:
            mod = json.loads(match.group(1))
            if "parametre" in mod and "valeur" in mod and "raison" in mod:
                modifications.append(mod)
        except json.JSONDecodeError:
            pass

    return {
        "reponse": reponse_texte,
        "modifications": modifications,
        "erreur": None,
    }


def appliquer_modification(parametre: str, valeur, raison: str, auteur: str = "assistant_ia") -> dict:
    succes = _sauver_param(parametre, valeur, raison, auteur)
    if not succes:
        return {"succes": False, "message": f"Parametre '{parametre}' introuvable.", "git": ""}

    msg_commit = (
        f"assistant: modif {parametre} -> {valeur}\n\n"
        f"Raison: {raison}\n"
        f"Auteur: {auteur}\n"
        f"Horodatage: {datetime.utcnow().isoformat()}"
    )
    git_output = _git_commit(msg_commit)
    return {
        "succes": True,
        "message": f"Parametre '{parametre}' mis a jour: {valeur}",
        "git": git_output,
    }


def historique_recent(n: int = 20) -> list:
    if not HISTORY_FILE.exists():
        return []
    with open(HISTORY_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    return data[-n:]


def lister_versions_git(n: int = 20) -> list:
    repo = PARAMS_DIR.parent.parent
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "log", "--oneline", f"-{n}", "--", "working-folder/params/"],
            capture_output=True, text=True
        )
        lines = result.stdout.strip().split("\n") if result.stdout.strip() else []
        return [{"sha": l[:7], "message": l[8:]} for l in lines if l]
    except Exception:
        return []


def rollback_vers(sha: str) -> dict:
    repo = PARAMS_DIR.parent.parent
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "checkout", sha, "--", "working-folder/params/"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            _git_commit(f"rollback: retour vers {sha}")
            return {"succes": True, "message": f"Revenu au commit {sha}"}
        return {"succes": False, "message": result.stderr}
    except Exception as e:
        return {"succes": False, "message": str(e)}
