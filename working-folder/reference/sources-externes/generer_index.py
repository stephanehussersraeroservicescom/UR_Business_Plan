#!/usr/bin/env python3
"""Regenere index-sources.html depuis registre-sources.yaml. Usage : python3 generer_index.py"""
import datetime, html, yaml
from pathlib import Path

ici = Path(__file__).parent
reg = yaml.safe_load((ici / "registre-sources.yaml").read_text(encoding="utf-8"))
e = lambda s: html.escape(str(s if s is not None else ""))
lignes = []
for sid, s in reg.items():
    lien = f'<a href="{e(s.get("url",""))}" target="_blank">{e(s.get("titre",""))}</a>'
    for f in str(s.get("fichier") or "").split(";"):
        f = f.strip().split(" ")[0]
        if f:
            lien += f' <br><a href="{e(f)}">[fichier local : {e(f)}]</a>'
    st = e(s.get("statut", ""))
    lignes.append(f"<tr><td><code>{e(sid)}</code></td><td>{lien}</td><td>{e(s.get('editeur'))}</td>"
                  f"<td>{e(s.get('date'))}</td><td>{e(s.get('emplacement'))}</td><td class='s-{st}'>{st}</td></tr>")
date = datetime.date.today().strftime("%d/%m/%Y")
page = ('<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Sources externes Urban Rig</title>\n'
        '<style>body{font-family:system-ui,sans-serif;margin:24px;background:#fff;color:#222}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border-bottom:1px solid #ddd;padding:6px 8px;text-align:left;vertical-align:top}th{background:#f3f3f3;position:sticky;top:0}a{color:#0b57d0}.s-non-verifie{color:#b00}.s-ancien{color:#a60}.s-secondaire{color:#666}.s-verifie-recontrole,.s-verifie{color:#070}</style></head>\n'
        f'<body><h1>Sources externes Urban Rig</h1><p>{len(reg)} sources. Genere depuis registre-sources.yaml le {date}.</p>\n'
        '<table><tr><th>ID</th><th>Titre (lien)</th><th>Editeur</th><th>Date</th><th>Emplacement</th><th>Statut</th></tr>'
        + "".join(lignes) + "</table></body></html>\n")
(ici / "index-sources.html").write_text(page, encoding="utf-8")
print(len(reg), "sources ecrites dans index-sources.html")
