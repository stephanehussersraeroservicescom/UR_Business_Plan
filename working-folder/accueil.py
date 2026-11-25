"""
Page d'accueil et espace de lecture du plan d'affaires (chat C, 25/11/2026).

Routes de ce module (et seulement celles-ci) :
  GET /                         page d'accueil (deux espaces)
  GET /financial-model          espace du modele : echelle de confiance (D-022), etiquettes, lien vers le modele
  GET /financial-model/pending  page d'attente tant que la route du modele (chat B) n'existe pas
  GET /financial-model/current  rapport actuel du modele : appelle la vue "index" de app.py (chat B), que
                                l'accueil masque sur "/" ; rien n'est modifie dans cette vue
  GET /reports                  plan d'affaires et annexes, avec l'etat de chaque annexe
  GET /files/<chemin>           fichiers du depot servis tels quels (HTML des annexes, fiches de preuve,
                                documents sources) ; les .md autorises sont affiches en HTML

Les pages des annexes sont lues dans le depot a chaque requete : rien n'est copie (decision D-023).
L'etat de chaque annexe est lu dans working-folder/controle-sources/verifications/ecarts-annexe-*.md :
les compteurs sont des comptages des lignes du tableau du journal, aucun chiffre n'est saisi a la main.

Le blueprint doit etre enregistre juste apres la creation de l'application : pour deux regles identiques,
Flask retient la premiere enregistree (voir app.py).
"""
import html
import os
import re
from pathlib import Path

from flask import Blueprint, abort, current_app, redirect, render_template, send_file, url_for

try:
    import markdown as _markdown
except ImportError:  # pragma: no cover
    _markdown = None

bp = Blueprint("accueil", __name__)

WF = Path(__file__).resolve().parent                     # working-folder (dans le conteneur : /app)
RACINE = WF.parent                                       # racine du depot (dans le conteneur : /)
BP_DIR = Path(os.environ.get("UR_BP_DIR", RACINE / "nouveau-business-plan"))
ANNEXES = BP_DIR / "annexes"
VERIFS = WF / "controle-sources" / "verifications"

# Route du modele financier construite par le chat B. Changer ici (ou par la variable d'environnement)
# si le chat B choisit un autre chemin.
MODEL_ROUTE = os.environ.get("UR_MODEL_ROUTE", "/model")

ANNEX_LIST = [
    (1, "Process and Technology"),
    (2, "Technical Evidence"),
    (3, "Output Markets and Pricing"),
    (4, "France"),
    (5, "Municipal Solid Waste"),
    (6, "Airport Waste, CDG"),
    (7, "Industrial and Commercial Waste"),
    (8, "Plastic Waste Streams"),
    (9, "Equipment and Configuration"),
]
SET_ASIDE = {6: "Set aside by Stéphane on 19/11/2026; title and place kept."}

# Fichiers du depot que /files/ peut servir. Tout le reste renvoie 404.
_ANNEX_HTML = re.compile(r"^nouveau-business-plan/annexes/annexe-0[1-9]-html/.+")
_PREFIXES = ("working-folder/reference/preuves/", "working-folder/reference/sources-externes/")
_MD_RENDUS = re.compile(
    r"^(nouveau-business-plan/BUSINESS-PLAN\.md"
    r"|nouveau-business-plan/CRITICAL-POINTS\.md"
    r"|working-folder/controle-sources/verifications/ecarts-annexe-[0-9-]+\.md)$"
)
_INTERDITS = (".py", ".pyc", ".yaml", ".yml", ".sh")


# ---------------------------------------------------------------------------
# Outils
# ---------------------------------------------------------------------------

def _depot_vers_disque(rel: str) -> Path:
    """Chemin du depot -> fichier sur disque (local et conteneur)."""
    if rel.startswith("nouveau-business-plan/"):
        return BP_DIR / rel[len("nouveau-business-plan/"):]
    if rel.startswith("working-folder/"):
        return WF / rel[len("working-folder/"):]
    return RACINE / rel


def _route_existe(chemin: str) -> bool:
    adapter = current_app.url_map.bind("localhost")
    try:
        adapter.match(chemin, method="GET")
        return True
    except Exception:
        return False


def _md_html(texte: str) -> str:
    if _markdown is None:
        return "<pre>" + html.escape(texte) + "</pre>"
    return _markdown.markdown(texte, extensions=["tables", "fenced_code", "sane_lists"])


def _titre_html(fichier: Path) -> str | None:
    try:
        m = re.search(r"<title>([^<]*)</title>", fichier.read_text(encoding="utf-8", errors="replace")[:4000])
    except OSError:
        return None
    return html.unescape(m.group(1)).strip() if m else None


# Traitements du journal des ecarts -> libelle anglais. L'ordre compte (le plus precis d'abord).
_TRAITEMENTS = [
    ("ACCEPTÉ, À TRANCHER", "accepted, decision pending"),
    ("ACCEPTÉ EN PARTIE", "partly accepted"),
    ("ACCEPTÉ DANS LA SOURCE", "accepted"),
    ("ACCEPTÉ", "accepted"),
    ("PARTIEL", "partly accepted"),
    ("À TRANCHER", "decision pending"),
    ("À CORRIGER", "to be corrected"),
    ("CONTESTÉ", "disputed"),
    ("NON CORRIGÉ", "not corrected"),
    ("DÉJÀ", "already covered"),
    ("AUCUNE", "no correction"),
    ("CLOS", "closed"),
]


def _classer(cellule: str) -> str:
    c = cellule.strip().upper()
    for cle, libelle in _TRAITEMENTS:
        if c.startswith(cle):
            return libelle
    return "other"


def _lire_journal(fichier: Path) -> dict:
    """Lit un journal ecarts-annexe-*.md : date du titre, comptage des lignes du premier tableau
    qui porte une colonne Traitement (ou Statut), phrases de controle et NON TROUVE citees telles quelles."""
    texte = fichier.read_text(encoding="utf-8", errors="replace")
    lignes = texte.splitlines()
    titre = next((l.lstrip("# ").strip() for l in lignes if l.startswith("# ")), fichier.name)
    date = re.search(r"\((\d{2}/\d{2}/\d{4})\)", titre)

    comptes: dict[str, int] = {}
    total = 0
    col = None
    for i, l in enumerate(lignes):
        if not l.startswith("|"):
            if col is not None and total:
                break  # fin du premier tableau compte
            continue
        cellules = [c.strip() for c in l.strip().strip("|").split("|")]
        if col is None:
            for nom in ("Traitement", "Statut"):
                if nom in cellules:
                    col = cellules.index(nom)
                    break
            continue
        if set(l.replace("|", "").strip()) <= set("-: "):
            continue
        if col < len(cellules):
            libelle = _classer(cellules[col])
            comptes[libelle] = comptes.get(libelle, 0) + 1
            total += 1

    controle = [l.strip() for l in lignes if l.strip().startswith("Contrôle automatique")]
    non_trouve = []
    for l in lignes:
        if "NON TROUVÉ" in l and not l.startswith("|"):
            for phrase in re.split(r"(?<=[.;])\s+", l):
                if "NON TROUVÉ" in phrase:
                    non_trouve.append(phrase.strip())
    return {
        "fichier": fichier.name,
        "lien": "/files/working-folder/controle-sources/verifications/" + fichier.name,
        "titre": titre,
        "date": date.group(1) if date else None,
        "total": total,
        "comptes": sorted(comptes.items(), key=lambda kv: -kv[1]),
        "controle": controle[0] if controle else None,
        "non_trouve": non_trouve,
    }


def _journaux(n: int) -> list[dict]:
    if not VERIFS.is_dir():
        return []
    fichiers = sorted(VERIFS.glob(f"ecarts-annexe-{n:02d}*.md"), key=lambda p: p.name, reverse=True)
    # Le journal date du 25/11/2026 de l'annexe 2 passe avant celui d'octobre.
    fichiers.sort(key=lambda p: (0 if re.search(r"\d{4}-\d{2}-\d{2}", p.name) else 1, p.name))
    return [_lire_journal(f) for f in fichiers]


def _annexes() -> list[dict]:
    res = []
    for n, nom in ANNEX_LIST:
        d = {"n": n, "nom": nom, "set_aside": SET_ASIDE.get(n)}
        index = ANNEXES / f"annexe-{n:02d}-html" / "index.html"
        d["existe"] = index.is_file()
        if d["existe"]:
            d["titre"] = _titre_html(index) or f"Annex {n}. {nom}"
            d["lien"] = f"/files/nouveau-business-plan/annexes/annexe-{n:02d}-html/index.html"
            preuves = index.parent / "preuves"
            d["nb_fiches"] = len([p for p in preuves.glob("*.html") if p.name != "index.html"]) if preuves.is_dir() else 0
            d["lien_preuves"] = None
            for cand in ("index.html", "README.html"):
                if (preuves / cand).is_file():
                    d["lien_preuves"] = d["lien"].replace("index.html", "preuves/" + cand)
                    break
        else:
            d["titre"] = f"Annex {n}. {nom}"
        d["journaux"] = [] if d["set_aside"] else _journaux(n)
        res.append(d)
    return res


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@bp.route("/")
def home():
    return render_template("accueil/home.html")


@bp.route("/financial-model")
def financial_model():
    return render_template(
        "accueil/financial.html",
        model_route=MODEL_ROUTE,
        model_pret=_route_existe(MODEL_ROUTE),
        rapport_actuel="index" in current_app.view_functions,
    )


@bp.route("/financial-model/pending")
def financial_model_pending():
    if _route_existe(MODEL_ROUTE):
        return redirect(MODEL_ROUTE)
    return render_template("accueil/pending.html", model_route=MODEL_ROUTE,
                           rapport_actuel="index" in current_app.view_functions), 200


@bp.route("/financial-model/current")
def financial_model_current():
    vue = current_app.view_functions.get("index")
    if vue is None:
        abort(404)
    return vue()


@bp.route("/reports")
def reports():
    bp_md = BP_DIR / "BUSINESS-PLAN.md"
    return render_template(
        "accueil/reports.html",
        bp_pret=bp_md.is_file(),
        bp_lien="/files/nouveau-business-plan/BUSINESS-PLAN.md",
        annexes=_annexes(),
    )



@bp.route("/critical-points")
def critical_points():
    fichier = BP_DIR / "CRITICAL-POINTS.md"
    if not fichier.is_file():
        abort(404)
    texte = fichier.read_text(encoding="utf-8", errors="replace")
    titre = next((l.lstrip("# ").strip() for l in texte.splitlines() if l.startswith("# ")), "Critical open points")
    return render_template("accueil/page_md.html", titre=titre, corps=_md_html(texte),
                           source="nouveau-business-plan/CRITICAL-POINTS.md", retour=url_for("accueil.home"))

@bp.route("/files/<path:rel>")
def files(rel: str):
    rel = rel.replace("\\", "/")
    if ".." in rel.split("/") or rel.startswith("/") or rel.lower().endswith(_INTERDITS):
        abort(404)
    autorise = bool(_ANNEX_HTML.match(rel)) or rel.startswith(_PREFIXES) or bool(_MD_RENDUS.match(rel))
    if not autorise:
        abort(404)
    chemin = _depot_vers_disque(rel).resolve()
    base = (BP_DIR if rel.startswith("nouveau-business-plan/") else WF).resolve()
    if base not in chemin.parents or not chemin.is_file():
        abort(404)
    if _MD_RENDUS.match(rel):
        texte = chemin.read_text(encoding="utf-8", errors="replace")
        titre = next((l.lstrip("# ").strip() for l in texte.splitlines() if l.startswith("# ")), chemin.name)
        retour = url_for("accueil.reports")
        return render_template("accueil/page_md.html", titre=titre, corps=_md_html(texte),
                               source=rel, retour=retour)
    return send_file(chemin, conditional=True)
