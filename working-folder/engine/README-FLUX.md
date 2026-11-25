# Modele financier par flux (chat B, 25/11/2026)

Decision de methode : D-070. Valeurs : D-066 (partie A), D-067 (B1), D-068 (B2), D-069 (B3), D-073 (B4 a B17, B20, B21).
Hypotheses de Claude a trancher : D-071 (bilan des plastiques par scenario), D-072 (bruleur rapporte a 140 t/jour).
En attente : B18 (prix d'entree des DAE), B19 (cout du liquide a traiter).

## Fichiers

| Fichier | Role |
|---|---|
| `engine/flux.py` | Moteur : bilan par tonne, energie, recettes, charges, CAPEX, compte de resultat, cash-flow, TRI, retour |
| `engine/flux_bilans.yaml` | Table flux x scenario -> identifiants de calculs.yaml (aucun chiffre) ; valeurs en attente de decision |
| `engine/web_flux.py` | Pages web sous `/model` (blueprint Flask), enregistre a la fin de `app.py` |
| `controle-sources/calculs.yaml` | Bilans par tonne (CALC-A5-*, CALC-A7-*, CALC-MOD-*) lus par le moteur |
| `params/*.yaml` | Prix, couts et hypotheses, chacun avec sa decision |

L'ancien moteur (`engine/modele.py`, `run.py`, page `/`) n'est pas modifie ; il lit les memes `params/`.

## Lancer en local

Depuis `working-folder/` :

```
pip install -r requirements.txt
python3 -m engine.flux                                   # plastiques, standard
python3 -m engine.flux --flux omr --scenario pessimiste
python3 -m engine.flux --flux omr --chaleur gazole --gaz-organique
python3 -m engine.flux --flux dae --set prix_entree_dae=200
python3 -m engine.flux --flux plastiques --prix-entree prix_entree_pse_blanc --set compter_hydrogene=true
python3 -m engine.flux --json > out/flux.json            # resultats complets
python3 app.py                                           # puis http://localhost:5050/model
```

## API

- `GET /model` : page interactive.
- `GET /model/api/description` : flux, scenarios, champs (valeur, source, confiance, statut).
- `POST /model/api/calcul` : corps JSON
  `{"flux": "omr", "scenario": "standard", "surcharges": {"prix_char": 50}, "choix": {"source_chaleur": "huile", "compter_gaz_organique": false, "prix_entree": "prix_entree_omr"}}`.

## Regles appliquees

- Confiance (echelle D-022) : 100 statistique publique, reglementation, essai ou laboratoire ; 95 constructeur et litterature ; 90 hypothese de travail (D-xxx) ou declaration constructeur ; 80 source secondaire ; un calcul prend son entree la moins fiable, au plus 95.
- Statut : « contre-verifie Codex » si l'identifiant figure dans un rapport `controle-sources/verifications/*codex*.md` ; sinon « controle, non contre-verifie » ; « en attente de decision » ; « valeur heritee, non sourcee ».
- Energie : besoin = bruleur 833 kcal/s par jour / charge reelle (D-072) ; le deficit est couvert par l'huile (46 MJ/kg, PCS), le char ou le gazole (38,05 MJ/L) selon D-069 ; rendement du bruleur non applique.
- Simplifications a connaitre : montee en charge appliquee au tonnage, besoin de chaleur par tonne constant ; impot sans report des pertes ; dette amortie lineairement ; inflation de 2 % (heritee) sur tous les prix et couts ; surplus de gaz des plastiques non valorise.
