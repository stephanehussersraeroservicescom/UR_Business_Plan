# Working Folder — modèle Urban Rig traçable

Dossier de travail. Rien ici n'est validé tant que ce n'est pas explicitement accepté.

## État au 19 septembre 2026

Structure créée. Les fichiers de paramètres, le moteur et le générateur HTML sont
à déposer depuis l'archive `urmodel.zip` produite en conversation, ou à écrire
directement ici.

## Objectif

Une présentation HTML, générée par Python, qui montre pour chaque valeur citée :

- la valeur retenue et son unité
- son statut (certifié tiers, mesuré, constructeur, calculé, littérature, hypothèse, inconnu)
- la décision qui l'a fixée, datée et motivée
- les documents sources qui l'étayent
- ce qui reste à vérifier

Autrement dit : cliquer sur un chiffre du compte de résultat et remonter jusqu'au
rapport de laboratoire.

## Arborescence prévue

```
working-folder/
  params/          paramètres en YAML, un fichier par domaine
    _evidence.yaml    registre des preuves
    _decisions.yaml   journal des décisions
    capacite.yaml  composition.yaml  rendements.yaml  energie.yaml
    eau.yaml       prix.yaml         capex.yaml       opex.yaml
    carbone.yaml   finance.yaml
  engine/
    modele.py      moteur de calcul, aucune valeur numérique
    rapport.py     générateur HTML
  run.py
  out/             sorties générées, non versionnées
```

## Règle de travail

Aucune valeur en dur dans le code. Tout paramètre cite au moins une preuve,
même `AUCUNE`. Toute valeur qui s'écarte du V3 ouvre une entrée datée dans
`_decisions.yaml`.

## Corrections déjà actées

| # | Objet | De | Vers |
|---|---|---|---|
| D-001 | PCI du gaz de procédé issu du plastique | 5,54 MJ/kg | 37,3 MJ/kg |
| D-002 | PCI du gaz de procédé issu de l'organique | 0,5 MJ/kg | 11,0 MJ/kg |
| D-003 | Fioul de chauffe en régime normal | 7 494 L/j | 0, plus provision 5 % |
| D-004 | Teneur en chlore de l'huile | 100 ppm | 1 ppm (certificat NKKK) |
| D-005 | Recette crédits carbone | 2 499 457 €/an | 0 |
| D-006 | Bâtiment | 5 M€ forfaitaires | surfaces des plans × prix marché |
| D-007 | Maintenance | 4 % dès l'année 1 | 1 % jusqu'en année 4, 4 % en année 10 |
| D-008 | Traitement de l'eau | absent | neutralisation, décantation, SEA CORAL |

## Erreur corrigée dans le tableur V4

La formule du gate fee d'équilibre comptait les gate fees deux fois. Valeur
annoncée à tort : 116 €/t. **Valeur réelle : 9,66 €/t** sur une machine, et
négative à cinq machines. Corrigée le 19 septembre 2026.

C'est la raison d'être de ce dossier : une erreur de formule dans un tableur
est invisible, une erreur dans une fonction Python se teste.
