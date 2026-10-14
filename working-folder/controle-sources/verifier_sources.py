#!/usr/bin/env python3
"""Controle des sources du business plan Urban Rig.

Regle : tout chiffre d'un livrable renvoie a une source du registre, ou a un
calcul enregistre dont toutes les entrees sont sourcees. Ce qui n'est ni l'un
ni l'autre est signale.

Usage (depuis la racine du depot ou n'importe ou) :
    python3 working-folder/controle-sources/verifier_sources.py
    python3 working-folder/controle-sources/verifier_sources.py nouveau-business-plan/<fichier>.md
    python3 working-folder/controle-sources/verifier_sources.py --strict

Sorties : working-folder/out/controle-sources.md et controle-sources.html.
Code retour : 1 s'il reste au moins une erreur, 0 sinon.

Conventions de citation reconnues dans un document Markdown :
    [ID] ou [ID](url)          ID du registre externe ou de _evidence.yaml
    [Titre](url)               accepte si l'URL figure dans le registre
    [calc:ID]                  calcul enregistre dans calculs.yaml
    [hyp:ID]                   hypothese documentee (D-xxx de _decisions.yaml
                               ou AFF-xxx de _justifications.yaml)
    <!-- nosrc -->             a placer en fin de ligne pour une ligne sans
                               affirmation chiffree (ex. numerotation)

Archive (regle 16) : rien dans ARCHIVE-NON-VERIFIE/ n'est une source. Un lien vers
l'archive, une fiche du registre qui y renvoie, ou une preuve interne de
_evidence.yaml dont le chemin est dans l'archive sont comptes comme des erreurs.
Un document de l'archive peut etre controle a la main pour inventaire : un chiffre
qui y parait source reste a relire dans le document d'origine.
"""
from __future__ import annotations

import argparse
import ast
import fnmatch
import glob
import html
import math
import operator
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ICI = Path(__file__).resolve().parent
WF = ICI.parent                      # working-folder
RACINE = WF.parent                   # depot
REG_EXT = WF / "reference" / "sources-externes" / "registre-sources.yaml"
REG_INT = WF / "params" / "_evidence.yaml"
DECISIONS = WF / "params" / "_decisions.yaml"
JUSTIFS = WF / "params" / "_justifications.yaml"
CALCULS = ICI / "calculs.yaml"
ARBITRAGES = WF / "params" / "_arbitrages.yaml"
A_RECHERCHER = ICI / "a-rechercher.yaml"
STATUTS_RECHERCHE = {"a_chercher", "trouve", "partiel", "introuvable", "a_demander"}
CIBLES = ICI / "cibles.yaml"
SORTIE = WF / "out"

STATUTS_FAIBLES = {"secondaire", "non-verifie", "ancien"}
ARCHIVE = "ARCHIVE-NON-VERIFIE"     # regle 16 : aucune valeur de preuve
RE_LIEN_ARCHIVE = re.compile(r"\]\(([^)\s]*" + ARCHIVE + r"[^)\s]*)\)")


def dans_archive(fiche) -> bool:
    """Vrai si la fiche (registre ou preuve interne) renvoie a l'archive non verifiee."""
    if not isinstance(fiche, dict):
        return False
    return any(ARCHIVE in str(fiche.get(c, "")) for c in ("chemin", "fichier", "url"))
AFFIRMATIONS_SOURCEES: list = []   # (fichier, ligne, extrait, ids) pour l'echantillon de verification manuelle

# ---------------------------------------------------------------------------
# Chargement des registres
# ---------------------------------------------------------------------------

def charger_yaml(p: Path) -> dict:
    if not p.exists():
        return {}
    d = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    return {k: v for k, v in d.items() if not str(k).startswith("_")}


@dataclass
class Registres:
    ext: dict
    int_: dict
    decisions: dict
    justifs: dict
    calculs: dict
    url_vers_id: dict = field(default_factory=dict)

    @classmethod
    def charger(cls) -> "Registres":
        r = cls(charger_yaml(REG_EXT), charger_yaml(REG_INT), charger_yaml(DECISIONS),
                charger_yaml(JUSTIFS), charger_yaml(CALCULS))
        for k, v in r.ext.items():
            if isinstance(v, dict):
                for champ in ("url", "url_fiche", "url_page", "url_2020"):
                    u = v.get(champ)
                    if u:
                        r.url_vers_id[norm_url(str(u))] = k
        return r

    def source(self, ident: str):
        if ident in self.ext:
            return "ext", self.ext[ident]
        if ident in self.int_:
            return "int", self.int_[ident]
        return None, None


def norm_url(u: str) -> str:
    u = u.strip().strip("<>").replace("&amp;", "&")
    u = re.sub(r"^https?://(www\.)?", "", u)
    u = u.replace("%20", " ").replace("%28", "(").replace("%29", ")")
    return u.rstrip("/")

# ---------------------------------------------------------------------------
# Nombres
# ---------------------------------------------------------------------------

UNITES = (r"%|‰|€|\$|£|CHF|EUR|USD|GBP|k€|M€|Md€|Mds?€|bn|billion|million|milliards?|millions?|"
          r"Gt|Mt|kt|t|tonnes?|tons?|kg|g|mg|µg|ng|MJ|GJ|kJ|kcal|Wh|kWh|MWh|GWh|TWh|kW|MW|GW|"
          r"MWe|MWth|MWh/t|°C|K|ppm|ppb|mg/L|g/L|m²|m2|m³|m3|Nm3|Nm³|km|m|mm|cm|ha|bar|"
          r"hab|inhabitants?|habitants?|ans?|years?|yr|mois|months?|jours?|days?|h|heures?|hours?|"
          r"x|×|t/an|t/yr|t/j|t/h|pts?|points?")
RE_NOMBRE = re.compile(r"(?<![\w.,/])[-−+]?\d{1,3}(?:[   ]\d{3})+(?:[.,]\d+)?(?![\d])"
                       r"|(?<![\w.,/])[-−+]?\d+(?:[.,]\d+)?(?![\d])")
RE_UNITE_APRES = re.compile(r"^\s?(?:" + UNITES + r")(?![A-Za-zÀ-ÿ])")
RE_DEVISE_AVANT = re.compile(r"(?:€|\$|£|EUR|USD|GBP|CHF)\s?$")

# Numerotation de plan en debut de ligne de liste : "- 10.1 Technology Risk", "11. Annexes".
# Hierarchique (10.1, 4A.3) ou suivie d'un point (11.), puis un mot en majuscule qui n'est pas
# une unite : "- 10.5 Mt ..." reste une affirmation chiffree.
RE_NUMEROTATION = re.compile(r"(?m)^(\s*(?:[-*+]\s+)?(?:\*\*)?)"
                             r"(\d{1,2}[A-Z]?(?:\.\d{1,2}){1,3}\.?|\d{1,2}\.)"
                             r"(?=(?:\*\*)?\s+(?:\*\*)?[A-ZÀ-Ý(]|(?:\*\*)?\s*$)")
RE_UNITE_I = re.compile(r"^(?:" + UNITES + r")(?![A-Za-zÀ-ÿ])", re.I)


def _numerotation(m: re.Match) -> str:
    suite = m.string[m.end():m.end() + 20].lstrip("* ")
    if not suite.strip() and not re.search(r"[-*+]", m.group(1)):
        return m.group(0)          # "10." seul hors liste : on ne presume pas une numerotation
    return m.group(0) if RE_UNITE_I.match(suite) else m.group(1) + " "


# Tout ce qui n'est pas une affirmation chiffree
NETTOYAGES = [
    (RE_NUMEROTATION, _numerotation),
    (re.compile(r"```.*?```", re.S), " "),
    (re.compile(r"`[^`]*`"), " "),
    (re.compile(r"<!--.*?-->", re.S), " "),
    (re.compile(r"\]\([^)]*\)"), "]"),                       # cibles de liens
    (re.compile(r"https?://\S+"), " "),
    (re.compile(r"\[(?:calc|calcul|hyp)\s*:[^\]]*\]", re.I), " "),
    (re.compile(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b"), " "),       # dates
    (re.compile(r"(?i)\b\d{1,2}(?:er)?\s+(?:janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre|January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\\b\\.?"), " "),
    (re.compile(r"\b(?:19|20)\d{2}-\d{2}(?:-\d{2})?\b"), " "),
    (re.compile(r"\b(?:19[5-9]\d|20[0-6]\d)(?:\s?[-–/]\s?(?:19|20)?\d{2})?\b"), " "),  # annees et periodes
    (re.compile(r"(?i)\b(?:p|pp|page|pages|slide|slides|diapo|diapos|diapositives?|tableau|tableaux|table|tables|"
                r"tab|fig|figure|figures|art|article|articles|annex|annexe|annexes|section|sections|chapitre|chapter|"
                r"part|partie|n°|no|nr|§|al|alinéa|point|ligne|line|row|version|étape|step|scénario|"
                r"scenario|lot|lots|zone|zones|edition|édition|ref|réf|ed|vol|issue)\.?\s?\d+[a-z]?"
                r"(?:\s?(?:[-–,/]|à|et|and|to)\s?\d+[a-z]?)*"), " "),
    (re.compile(r"§\s?\d+(?:\.\d+)*"), " "),
    (re.compile(r"\b[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ_\-]*\d[\w\-.]*"), " "),   # identifiants, formules, codes
    (re.compile(r"\b\d+(?:er|e|ème|eme|st|nd|rd|th)\b"), " "),     # ordinaux
]


def nettoyer(txt: str) -> str:
    for rx, rep in NETTOYAGES:
        txt = rx.sub(rep, txt)
    return txt


def valeur(tok: str) -> float | None:
    t = tok.replace("−", "-").replace(" ", " ").replace(" ", " ")
    if re.search(r"\d[ ]\d{3}", t):
        t = t.replace(" ", "")
    t = t.replace(" ", "")
    if "," in t and "." in t:
        t = t.replace(",", "")
    elif t.count(",") == 1 and len(t.split(",")[1]) != 3:
        t = t.replace(",", ".")
    elif t.count(",") >= 1:
        t = t.replace(",", "")
    try:
        return float(t)
    except ValueError:
        return None


def chiffres_affirmes(txt: str, strict: bool) -> list[str]:
    propre = nettoyer(txt)
    trouves = []
    for m in RE_NOMBRE.finditer(propre):
        tok = m.group(0)
        apres = propre[m.end():m.end() + 12]
        avant = propre[max(0, m.start() - 4):m.start()]
        v = valeur(tok)
        if v is None:
            continue
        a_unite = bool(RE_UNITE_APRES.match(apres) or RE_DEVISE_AVANT.search(avant))
        if strict or a_unite or abs(v) >= 10:
            trouves.append(tok.strip())
    return trouves


def ensemble_valeurs(txt: str) -> set[float]:
    out = set()
    for m in RE_NOMBRE.finditer(txt or ""):
        v = valeur(m.group(0))
        if v is not None:
            out.add(round(v, 6))
    return out


def present_dans(v: float, valeurs: set[float]) -> bool:
    if v in valeurs:
        return True
    for w in valeurs:
        if w == 0:
            continue
        for facteur in (1, 100, 0.01, 1000, 0.001, 1e6, 1e-6):
            if math.isclose(v, w * facteur, rel_tol=0.006):
                return True
    return False

# ---------------------------------------------------------------------------
# Citations
# ---------------------------------------------------------------------------

RE_LIEN = re.compile(r"\[([^\]\n]{1,300})\]\((\S+?)\)")
RE_CROCHET = re.compile(r"\[([A-Za-z0-9][\w\-.]*)\](?!\()")
RE_BACKTICK = re.compile(r"`([A-Za-z0-9][\w\-.]*)`")
RE_CALC = re.compile(r"\[calc(?:ul)?\s*:\s*([\w\-.]+)\]", re.I)
RE_HYP = re.compile(r"\[hyp\s*:\s*([\w\-.]+)\]", re.I)
RE_CALC_GENERIQUE = re.compile(r"\[(?:calc|calcul)(?:\s*[:;,][^\]]*)?\]", re.I)
RE_HYPOTHESE_TEXTE = re.compile(r"\b(?:ASSUMPTION|HYPOTHESIS|hypothèse|hypothese|Judgement|jugement)\b")


@dataclass
class Citations:
    sources: list = field(default_factory=list)      # IDs resolus
    hors_registre: list = field(default_factory=list)  # URL non enregistrees
    calculs: list = field(default_factory=list)
    hypotheses: list = field(default_factory=list)
    calc_generique: bool = False
    hyp_texte: bool = False

    @property
    def vide(self) -> bool:
        return not (self.sources or self.hors_registre or self.calculs or self.hypotheses)


def lire_citations(txt: str, reg: Registres) -> Citations:
    c = Citations()
    for m in RE_CALC.finditer(txt):
        c.calculs.append(m.group(1))
    for m in RE_HYP.finditer(txt):
        c.hypotheses.append(m.group(1))
    sans_calc = RE_CALC.sub(" ", RE_HYP.sub(" ", txt))
    if RE_CALC_GENERIQUE.search(sans_calc):
        c.calc_generique = True
    if RE_HYPOTHESE_TEXTE.search(txt):
        c.hyp_texte = True
    for m in RE_LIEN.finditer(txt):
        texte, url = m.group(1), m.group(2)
        if not url.startswith("http"):
            continue
        cle = norm_url(url)
        if texte in reg.ext or texte in reg.int_:
            c.sources.append(texte)
        elif cle in reg.url_vers_id:
            c.sources.append(reg.url_vers_id[cle])
        else:
            c.hors_registre.append(url)
    for rx in (RE_CROCHET, RE_BACKTICK):
        for m in rx.finditer(txt):
            ident = m.group(1)
            if ident in reg.ext or ident in reg.int_:
                c.sources.append(ident)
    c.sources = list(dict.fromkeys(c.sources))
    return c

# ---------------------------------------------------------------------------
# Decoupage d'un document en unites d'affirmation
# ---------------------------------------------------------------------------

@dataclass
class Unite:
    ligne: int
    texte: str
    paragraphe: str
    nature: str          # phrase | tableau | titre


RE_PHRASE = re.compile(r"(?<=[.!?;])\s+(?=[A-ZÀ-Ý«\"(\[*])")


def unites(doc: str):
    lignes = doc.splitlines()
    i, dans_code = 0, False
    bloc: list[tuple[int, str]] = []
    legende = ""

    def vider(bloc):
        if not bloc:
            return
        par = " ".join(t for _, t in bloc)
        # une puce = un sous-paragraphe
        courant, debut = [], bloc[0][0]
        for n, t in bloc:
            if re.match(r"^\s*(?:[-*+]|\d+[.)])\s", t) and courant:
                yield from phrases(debut, " ".join(courant), par)
                courant, debut = [], n
            courant.append(t)
        if courant:
            yield from phrases(debut, " ".join(courant), par)

    def phrases(n, txt, par):
        for ph in RE_PHRASE.split(txt):
            if ph.strip():
                yield Unite(n, ph.strip(), par, "phrase")

    while i < len(lignes):
        l = lignes[i]
        if l.strip().startswith("```"):
            dans_code = not dans_code
            yield from vider(bloc); bloc = []
            i += 1
            continue
        if dans_code:
            i += 1
            continue
        if "nosrc" in l:
            i += 1
            continue
        if l.lstrip().startswith("|"):
            if bloc:
                legende = " ".join(t for _, t in bloc)
            yield from vider(bloc); bloc = []
            # note de source juste apres le tableau
            j = i
            while j < len(lignes) and lignes[j].lstrip().startswith("|"):
                j += 1
            k = j
            while k < len(lignes) and not lignes[k].strip():
                k += 1
            note = lignes[k] if k < len(lignes) and re.match(r"^\s*[*_]*\s*(?:Sources?|Note|Lecture)\b", lignes[k], re.I) else ""
            contexte = (legende + " " + note).strip()
            if not re.fullmatch(r"\s*\|[\s:|-]*\|?\s*", l):
                yield Unite(i + 1, l, contexte, "tableau")
        elif l.lstrip().startswith("#"):
            yield from vider(bloc); bloc = []
            legende = ""
            yield Unite(i + 1, re.sub(r"^#+\s*(?:\d+(?:\.\d+)*\.?\s)?", "", l), l, "titre")
        elif not l.strip():
            if bloc:
                legende = " ".join(t for _, t in bloc)
            yield from vider(bloc); bloc = []
        else:
            bloc.append((i + 1, l))
        i += 1
    yield from vider(bloc)

# ---------------------------------------------------------------------------
# Controles
# ---------------------------------------------------------------------------

@dataclass
class Constat:
    gravite: str     # ERREUR | AVERTISSEMENT | INFO
    fichier: str
    ligne: int
    message: str
    extrait: str = ""


def texte_fiche(fiche: dict) -> str:
    if not isinstance(fiche, dict):
        return str(fiche)
    return " ".join(str(v) for k, v in fiche.items() if k not in ("url", "url_fiche", "url_page", "url_2020"))


def controler_document(chemin: Path, reg: Registres, strict: bool, stats: dict) -> list[Constat]:
    rel = str(chemin.relative_to(RACINE)) if chemin.is_relative_to(RACINE) else str(chemin)
    doc = chemin.read_text(encoding="utf-8", errors="replace")
    out: list[Constat] = []
    s = stats.setdefault(rel, {"affirmations": 0, "sourcees": 0, "calculees": 0, "hypotheses": 0,
                               "paragraphe": 0, "tableau": 0, "sans_source": 0})
    if rel.startswith(ARCHIVE):
        out.append(Constat("INFO", rel, 0, "Document d'archive : controle pour inventaire seulement. Un chiffre "
                                           "source ici reste a relire dans le document d'origine (regle 16)."))
    for n, ligne in enumerate(doc.splitlines(), 1):
        for m in RE_LIEN_ARCHIVE.finditer(ligne):
            out.append(Constat("ERREUR", rel, n, f"Renvoi vers l'archive non verifiee : {m.group(1)[:120]}. "
                                                 "L'archive n'est pas une source (regle 16) : citer le document d'origine.",
                               ligne.strip()[:220]))
    for u in unites(doc):
        nombres = chiffres_affirmes(u.texte, strict)
        if not nombres:
            continue
        s["affirmations"] += 1
        c = lire_citations(u.texte, reg)
        extrait = re.sub(r"\s+", " ", u.texte)[:220]
        if u.nature == "titre":
            s["affirmations"] -= 1
            out.append(Constat("INFO", rel, u.ligne, "Titre chiffre : verifier que la section le source", extrait))
            continue
        herite = False
        if c.vide:
            cp = lire_citations(u.paragraphe, reg)
            if not cp.vide:
                if u.nature == "tableau":
                    s.setdefault("tableau", 0)
                    s["tableau"] += 1
                else:
                    s["paragraphe"] += 1
                    out.append(Constat("AVERTISSEMENT", rel, u.ligne,
                                       "Source seulement au niveau du paragraphe : la rattacher a la phrase", extrait))
                c = cp
                herite = True
            elif c.calc_generique or cp.calc_generique:
                s["calculees"] += 1
                out.append(Constat("ERREUR", rel, u.ligne,
                                   "Calcul non enregistre : remplacer [calcul] par [calc:ID] defini dans calculs.yaml", extrait))
                continue
            elif c.hyp_texte:
                s["hypotheses"] += 1
                out.append(Constat("ERREUR", rel, u.ligne,
                                   "Hypothese non documentee : la rattacher a [hyp:D-xxx] ou la sourcer", extrait))
                continue
            else:
                s["sans_source"] += 1
                out.append(Constat("ERREUR", rel, u.ligne,
                                   f"Chiffre sans source ({', '.join(nombres[:4])})", extrait))
                continue
        if c.sources:
            AFFIRMATIONS_SOURCEES.append((rel, u.ligne, re.sub(r"\s+", " ", u.texte)[:300], list(c.sources)))
        if herite:
            pass
        elif c.sources:
            s["sourcees"] += 1
        elif c.calculs:
            s["calculees"] += 1
        elif c.hypotheses:
            s["hypotheses"] += 1
        for url in c.hors_registre:
            out.append(Constat("AVERTISSEMENT", rel, u.ligne, f"Lien hors registre : {url[:120]}", extrait))
        if c.hors_registre and not (c.sources or c.calculs or c.hypotheses) and not herite:
            s["sourcees"] += 1
        for ident in c.calculs:
            if ident not in reg.calculs:
                out.append(Constat("ERREUR", rel, u.ligne, f"Calcul inconnu : {ident}", extrait))
        for ident in c.hypotheses:
            if ident not in reg.decisions and ident not in reg.justifs:
                out.append(Constat("ERREUR", rel, u.ligne, f"Hypothese inconnue : {ident}", extrait))
        # le chiffre affirme figure-t-il dans la fiche de la source ?
        if c.sources:
            archivees = [i for i in c.sources if dans_archive(reg.source(i)[1])]
            for i in archivees:
                out.append(Constat("ERREUR", rel, u.ligne, f"{i} renvoie a l'archive non verifiee : ce n'est pas une "
                                                           "source (regle 16)", extrait))
            internes = [i for i in c.sources if reg.source(i)[0] == "int" and not preuve_reelle(i, reg)]
            if internes and len(internes) == len(c.sources) and not archivees:
                out.append(Constat("ERREUR", rel, u.ligne, "Ne cite que des documents internes non sources "
                                                           f"({', '.join(internes[:3])}) : circularite", extrait))
            valeurs = set()
            faibles = []
            for ident in c.sources:
                _, fiche = reg.source(ident)
                valeurs |= ensemble_valeurs(texte_fiche(fiche))
                if isinstance(fiche, dict) and str(fiche.get("statut", "")) in STATUTS_FAIBLES:
                    faibles.append(f"{ident} ({fiche.get('statut')})")
            vals = [valeur(n) for n in nombres]
            if not any(v is not None and present_dans(v, valeurs) for v in vals):
                out.append(Constat("AVERTISSEMENT", rel, u.ligne,
                                   "Chiffre absent de la fiche registre : recontroler la source ou completer la fiche "
                                   f"({', '.join(c.sources[:3])})", extrait))
            if faibles and len(faibles) == len(c.sources):
                out.append(Constat("AVERTISSEMENT", rel, u.ligne,
                                   f"Source de statut faible uniquement : {', '.join(faibles[:3])}", extrait))
    return out

# ---------------------------------------------------------------------------
# Calculs enregistres
# ---------------------------------------------------------------------------

OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
       ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos}
FONCTIONS = {"min": min, "max": max, "round": round, "abs": abs, "sum": lambda *a: sum(a)}


def evaluer(expr: str, env: dict) -> float:
    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value
        if isinstance(n, ast.Name):
            return env[n.id]
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            return OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and type(n.op) in OPS:
            return OPS[type(n.op)](ev(n.operand))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in FONCTIONS:
            return FONCTIONS[n.func.id](*[ev(a) for a in n.args])
        raise ValueError(f"expression non autorisee : {ast.dump(n)[:60]}")
    return ev(ast.parse(str(expr), mode="eval"))


def controler_calculs(reg: Registres) -> tuple[list[Constat], dict]:
    out, resultats = [], {}
    rel = str(CALCULS.relative_to(RACINE))

    def resoudre(ident, pile=()):
        if ident in resultats:
            return resultats[ident]
        if ident in pile:
            raise ValueError(f"calcul circulaire : {' -> '.join(pile + (ident,))}")
        fiche = reg.calculs[ident]
        env = {}
        for nom, e in (fiche.get("entrees") or {}).items():
            if "calc" in e:
                env[nom] = resoudre(e["calc"], pile + (ident,))
            else:
                env[nom] = float(e["valeur"])
        v = evaluer(fiche["formule"], env)
        resultats[ident] = v
        return v

    for ident, fiche in reg.calculs.items():
        try:
            v = resoudre(ident)
        except Exception as exc:  # noqa: BLE001
            out.append(Constat("ERREUR", rel, 0, f"{ident} : calcul impossible ({exc})"))
            continue
        attendu = fiche.get("resultat")
        tol = float(fiche.get("tolerance", 0.005))
        if attendu is None:
            out.append(Constat("ERREUR", rel, 0, f"{ident} : champ 'resultat' manquant (valeur calculee {v:.6g})"))
        elif not math.isclose(v, float(attendu), rel_tol=tol, abs_tol=1e-12):
            out.append(Constat("ERREUR", rel, 0, f"{ident} : resultat annonce {attendu} different du calcul {v:.6g}"))
        for nom, e in (fiche.get("entrees") or {}).items():
            if "calc" in e:
                if e["calc"] not in reg.calculs:
                    out.append(Constat("ERREUR", rel, 0, f"{ident}.{nom} : calcul d'entree inconnu {e['calc']}"))
                continue
            src = e.get("source")
            if not src:
                out.append(Constat("ERREUR", rel, 0, f"{ident}.{nom} : entree sans source"))
                continue
            sources = src if isinstance(src, list) else [src]
            for s_id in sources:
                kind, f = reg.source(s_id)
                if kind is None:
                    if s_id in reg.decisions or s_id in reg.justifs:
                        out.append(Constat("AVERTISSEMENT", rel, 0, f"{ident}.{nom} : repose sur une hypothese ({s_id})"))
                    else:
                        out.append(Constat("ERREUR", rel, 0, f"{ident}.{nom} : source inconnue {s_id}"))
                    continue
                if not present_dans(round(float(e["valeur"]), 6), ensemble_valeurs(texte_fiche(f))):
                    out.append(Constat("AVERTISSEMENT", rel, 0,
                                       f"{ident}.{nom} = {e['valeur']} absent de la fiche {s_id} : completer la fiche"))
                if isinstance(f, dict) and str(f.get("statut", "")) in STATUTS_FAIBLES:
                    out.append(Constat("AVERTISSEMENT", rel, 0, f"{ident}.{nom} : source de statut {f.get('statut')} ({s_id})"))
    return out, resultats

# ---------------------------------------------------------------------------
# Registres et parametres du modele
# ---------------------------------------------------------------------------

def controler_registres(reg: Registres) -> list[Constat]:
    out = []
    rel = str(REG_EXT.relative_to(RACINE))
    vues = {}
    for k, f in reg.ext.items():
        if not isinstance(f, dict):
            continue
        if not f.get("url") and not f.get("fichier"):
            out.append(Constat("ERREUR", rel, 0, f"{k} : ni url ni fichier"))
        if not f.get("statut"):
            out.append(Constat("ERREUR", rel, 0, f"{k} : statut manquant"))
        if dans_archive(f):
            out.append(Constat("ERREUR", rel, 0, f"{k} : renvoie a l'archive non verifiee (regle 16)"))
        if str(f.get("statut", "")).startswith("verifie") and not (f.get("emplacement") or f.get("citation") or f.get("contenu")):
            out.append(Constat("AVERTISSEMENT", rel, 0, f"{k} : statut verifie sans emplacement, citation ni contenu"))
        u = norm_url(str(f.get("url", "")))
        if u and u in vues:
            out.append(Constat("INFO", rel, 0, f"{k} : meme URL que {vues[u]}"))
        vues.setdefault(u, k)
    return out


BASES_SANS_PREUVE = {"loi_physique", "decision_commerciale"}
PREUVES_VIDES = {"V3-MODEL", "AUCUNE"}
# documents internes eux-memes non sources : les citer ne prouve rien (circularite)
TYPES_CIRCULAIRES = {"modele_interne", "annexe_plan_affaires", "plan_affaires", "etude_marche_interne", "aucune"}


def preuve_reelle(ident: str, reg: Registres) -> bool:
    kind, f = reg.source(ident)
    if kind is None or ident in PREUVES_VIDES:
        return False
    if dans_archive(f):
        return False
    if kind == "int" and isinstance(f, dict):
        if str(f.get("type")) in TYPES_CIRCULAIRES or str(f.get("fiabilite")) == "aucune":
            return False
    return True


def appuis_parametre(f: dict, reg: Registres) -> tuple[set, set, list]:
    """Preuves et bases atteintes depuis un parametre, via le graphe _justifications.yaml."""
    preuves, bases, inconnues = set(f.get("preuves") or []), set(), []
    a_voir, vus = [f.get("justification")] if f.get("justification") else [], set()
    while a_voir:
        aff = a_voir.pop()
        if not aff or aff in vus:
            continue
        vus.add(aff)
        j = reg.justifs.get(aff)
        if j is None:
            inconnues.append(aff)
            continue
        bases.add(str(j.get("base", "")))
        preuves |= set(j.get("preuves") or [])
        a_voir += list(j.get("appuis") or [])
    return preuves, bases, inconnues


def controler_parametres(reg: Registres) -> list[Constat]:
    out = []
    arbitrages = charger_yaml(ARBITRAGES)
    for p in sorted((WF / "params").glob("*.yaml")):
        if p.name.startswith("_"):
            continue
        rel = str(p.relative_to(RACINE))
        d = charger_yaml(p)
        for nom, f in d.items():
            if not isinstance(f, dict) or "valeur" not in f:
                continue
            if nom in arbitrages:
                a = arbitrages[nom] or {}
                out.append(Constat("INFO", rel, 0,
                                   f"{nom} : A ARBITRER ({a.get('verdict', 'decision attendue')}) : {a.get('question', '')} "
                                   f"Sources : {', '.join(a.get('sources') or []) or 'aucune'}"))
            preuves, bases, aff_inconnues = appuis_parametre(f, reg)
            for a in aff_inconnues:
                out.append(Constat("ERREUR", rel, 0, f"{nom} : justification inconnue {a}"))
            inconnues = [x for x in preuves if not reg.source(x)[0]]
            if inconnues:
                out.append(Constat("ERREUR", rel, 0, f"{nom} : preuve inconnue {sorted(inconnues)}"))
            reelles = {x for x in preuves if preuve_reelle(x, reg)}
            circulaires = {x for x in preuves if reg.source(x)[0] and not preuve_reelle(x, reg)} - PREUVES_VIDES
            decision = f.get("decision")
            if reelles:
                if str(f.get("statut")) in ("hypothese", "inconnu"):
                    out.append(Constat("AVERTISSEMENT", rel, 0,
                                       f"{nom} : statut {f.get('statut')} malgre des preuves {sorted(reelles)}"))
                continue
            if decision and decision in reg.decisions:
                out.append(Constat("INFO", rel, 0, f"{nom} : choix documente par {decision}"))
                continue
            if bases & BASES_SANS_PREUVE:
                out.append(Constat("INFO", rel, 0, f"{nom} : justifie par {sorted(bases & BASES_SANS_PREUVE)}"))
                continue
            precision = f" ; ne cite que des documents internes non sources {sorted(circulaires)}" if circulaires else ""
            out.append(Constat("ERREUR", rel, 0,
                               f"{nom} = {f.get('valeur')} {f.get('unite', '')} : aucune source externe ou interne "
                               f"(statut {f.get('statut')}, justification {f.get('justification', 'aucune')}){precision}"))
    return out


# ---------------------------------------------------------------------------
# Rapport
# ---------------------------------------------------------------------------

def cibles_par_defaut() -> list[Path]:
    conf = charger_yaml(CIBLES) if CIBLES.exists() else {}
    motifs = conf.get("inclure") or ["nouveau-business-plan/**/*.md",
                                     "working-folder/reference/sources-externes/**/*.md"]
    exclure = conf.get("exclure") or [ARCHIVE + "/**", "_to_delete/**", "**/_to_delete/**",
                                      "**/notes-recherche*/**", "**/README.md", "**/PASSATION-*.md"]
    fichiers = []
    for m in motifs:
        fichiers += [Path(x) for x in glob.glob(str(RACINE / m), recursive=True)]
    garde = []
    for f in sorted(set(fichiers)):
        rel = str(f.relative_to(RACINE))
        if any(fnmatch.fnmatch(rel, e) for e in exclure):
            continue
        garde.append(f)
    return garde


def ecrire_rapport(constats: list[Constat], stats: dict, resultats: dict, strict: bool) -> tuple[Path, Path]:
    SORTIE.mkdir(parents=True, exist_ok=True)
    n = {g: sum(1 for c in constats if c.gravite == g) for g in ("ERREUR", "AVERTISSEMENT", "INFO")}
    lignes = ["# Controle des sources", "",
              f"Mode {'strict' if strict else 'standard'}. Erreurs : **{n['ERREUR']}** ; avertissements : "
              f"{n['AVERTISSEMENT']} ; informations : {n['INFO']}.", "",
              "## Synthese par document", "",
              "| Document | Affirmations chiffrees | Sourcees | Source du tableau | Calcul enregistre | Hypothese | Source au paragraphe | **Sans source** | Taux sourcé |",
              "|---|---|---|---|---|---|---|---|---|"]
    for doc, s in sorted(stats.items()):
        a = s["affirmations"] or 1
        ok = s["sourcees"] + s["paragraphe"] + s["tableau"] + s["calculees"]
        lignes.append(f"| {doc} | {s['affirmations']} | {s['sourcees']} | {s['tableau']} | {s['calculees']} | {s['hypotheses']} | "
                      f"{s['paragraphe']} | **{s['sans_source']}** | {100 * ok / a:.0f} % |")
    if resultats:
        lignes += ["", "## Calculs enregistres", "", "| ID | Valeur recalculee |", "|---|---|"]
        lignes += [f"| {k} | {v:.6g} |" for k, v in resultats.items()]
    par_fichier: dict[str, list[Constat]] = {}
    for c in constats:
        par_fichier.setdefault(c.fichier, []).append(c)
    for f, cs in sorted(par_fichier.items()):
        lignes += ["", f"## {f}", ""]
        for c in sorted(cs, key=lambda c: ({"ERREUR": 0, "AVERTISSEMENT": 1, "INFO": 2}[c.gravite], c.ligne)):
            pos = f"l. {c.ligne}" if c.ligne else ""
            ex = f" : « {c.extrait} »" if c.extrait else ""
            lignes.append(f"- **{c.gravite}** {pos} {c.message}{ex}")
    md = SORTIE / "controle-sources.md"
    md.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    corps, dans_table = [], False
    for l in lignes:
        est_ligne = l.startswith("|")
        if dans_table and not est_ligne:
            corps.append("</table>"); dans_table = False
        if est_ligne:
            if re.fullmatch(r"\|[-| ]+\|", l):
                continue
            if not dans_table:
                corps.append("<table>"); dans_table = True
            cel = [html.escape(x.strip().replace("**", "")) for x in l.strip("|").split("|")]
            corps.append("<tr>" + "".join(f"<td>{x}</td>" for x in cel) + "</tr>")
        elif l.startswith("# "):
            corps.append(f"<h1>{html.escape(l[2:])}</h1>")
        elif l.startswith("## "):
            corps.append(f"<h2>{html.escape(l[3:])}</h2>")
        elif l.startswith("- "):
            g = "err" if "ERREUR" in l[:20] else "avert" if "AVERTISSEMENT" in l[:25] else "info"
            corps.append(f"<p class='{g}'>{html.escape(l[2:].replace('**', ''))}</p>")
        elif l.strip():
            corps.append(f"<p>{html.escape(l.replace('**', ''))}</p>")
    if dans_table:
        corps.append("</table>")
    page = ("<!doctype html><html lang='fr'><head><meta charset='utf-8'><title>Controle des sources</title><style>"
            "body{font-family:system-ui,sans-serif;margin:24px;max-width:1200px;color:#222;background:#fff}"
            "table{border-collapse:collapse}td{border-bottom:1px solid #ddd;padding:4px 8px;font-size:14px}"
            "p{margin:4px 0;font-size:14px}.err{color:#b00}.avert{color:#a60}.info{color:#666}</style></head><body>"
            + "\n".join(corps) + "</body></html>")
    hp = SORTIE / "controle-sources.html"
    hp.write_text(page, encoding="utf-8")
    return md, hp


def controler_recherche(reg: Registres) -> tuple[list[Constat], dict]:
    """Liste de recherche : chaque element a un statut coherent ; les trous sont signales."""
    out, compte = [], {}
    if not A_RECHERCHER.exists():
        return out, compte
    rel = str(A_RECHERCHER.relative_to(RACINE))
    for ident, e in charger_yaml(A_RECHERCHER).items():
        e = e or {}
        st = str(e.get("statut", ""))
        compte[st] = compte.get(st, 0) + 1
        q = str(e.get("question", ""))[:140]
        if st not in STATUTS_RECHERCHE:
            out.append(Constat("ERREUR", rel, 0, f"{ident} : statut inconnu '{st}'"))
            continue
        for s_id in e.get("sources") or []:
            if not reg.source(s_id)[0]:
                out.append(Constat("ERREUR", rel, 0, f"{ident} : source inconnue {s_id}"))
        if st in ("trouve", "partiel") and not e.get("sources"):
            out.append(Constat("ERREUR", rel, 0, f"{ident} : statut {st} sans source"))
        if st in ("introuvable", "partiel") and not e.get("cherche"):
            out.append(Constat("ERREUR", rel, 0, f"{ident} : statut {st} sans dire ou l'on a cherche"))
        if st == "a_demander" and not e.get("detenteur"):
            out.append(Constat("ERREUR", rel, 0, f"{ident} : a demander, mais detenteur non precise"))
        if st in ("introuvable", "a_demander", "partiel", "a_chercher"):
            detail = e.get("manque") or e.get("detenteur") or e.get("cherche") or ""
            out.append(Constat("AVERTISSEMENT", rel, 0, f"A SIGNALER A STEPHANE : {ident} ({st}) {q}. {detail}"[:400]))
    return out, compte


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fichiers", nargs="*", help="documents Markdown a controler (defaut : cibles.yaml)")
    ap.add_argument("--strict", action="store_true", help="tout nombre compte comme une affirmation")
    ap.add_argument("--sans-parametres", action="store_true", help="ne pas controler params/*.yaml")
    ap.add_argument("--echantillon", type=int, default=0, metavar="N",
                    help="tirer au hasard N affirmations sourcees a verifier a la main")
    a = ap.parse_args()
    reg = Registres.charger()
    fichiers = [Path(f).resolve() for f in a.fichiers] if a.fichiers else cibles_par_defaut()
    constats, stats = [], {}
    for f in fichiers:
        constats += controler_document(f, reg, a.strict, stats)
    c_calc, resultats = controler_calculs(reg)
    constats += c_calc + controler_registres(reg)
    if not a.sans_parametres:
        constats += controler_parametres(reg)
    c_rech, compte_rech = controler_recherche(reg)
    constats += c_rech
    md, hp = ecrire_rapport(constats, stats, resultats, a.strict)
    if a.echantillon and AFFIRMATIONS_SOURCEES:
        import random
        tirage = random.sample(AFFIRMATIONS_SOURCEES, min(a.echantillon, len(AFFIRMATIONS_SOURCEES)))
        lignes = ["# Echantillon a verifier a la main", "",
                  "Pour chaque ligne : ouvrir le lien, aller a l'emplacement indique, et verifier que le chiffre",
                  "y figure bien. Noter OK ou FAUX. Un seul FAUX suffit a bloquer la validation de la brique.", ""]
        for n, (f, l, ex, ids) in enumerate(tirage, 1):
            lignes += [f"## {n}. {f}, ligne {l}", "", f"> {ex}", ""]
            for i in ids:
                _, fiche = reg.source(i)
                fiche = fiche if isinstance(fiche, dict) else {}
                lignes.append(f"- **{i}** : {fiche.get('titre', '')}")
                lignes.append(f"  - lien : {fiche.get('url') or fiche.get('chemin', '')}")
                lignes.append(f"  - emplacement : {fiche.get('emplacement', 'non renseigne')}")
                if fiche.get("citation"):
                    lignes.append(f"  - citation relevee : « {fiche['citation']} »")
            lignes += ["", "Resultat : [ ] OK   [ ] FAUX", ""]
        ech = SORTIE / "echantillon-a-verifier.md"
        ech.write_text("\n".join(lignes), encoding="utf-8")
        print(f"Echantillon de {len(tirage)} affirmations : {ech.relative_to(RACINE)}")
    n_err = sum(1 for c in constats if c.gravite == "ERREUR")
    print(f"{len(fichiers)} documents, {sum(s['affirmations'] for s in stats.values())} affirmations chiffrees.")
    for doc, s in sorted(stats.items()):
        print(f"  {doc}: {s['affirmations']} affirmations, {s['sans_source']} sans source")
    if compte_rech:
        print("Liste de recherche : " + ", ".join(f"{k} {v}" for k, v in sorted(compte_rech.items())))
    print(f"Erreurs : {n_err}. Rapport : {md.relative_to(RACINE)} et {hp.relative_to(RACINE)}")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
