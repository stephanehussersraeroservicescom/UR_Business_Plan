# Comparaison V3 / V4, parametre par parametre

Genere le 19/09/2026. Le V4 est le modele de reference (decision D-013). Le V3 est conserve pour comparaison.
Le moteur Python reproduit le V4 a l'euro pres sur 15 ans.

Colonne **Decision** : renvoie au journal `params/_decisions.yaml`. Colonne **Confiance** : resultat de l'arbre de justification.

## Parametres modifies entre V3 et V4 (17)

| Domaine | Parametre | V3 | V4 | Unite | Decision | Confiance |
|---|---|---:|---:|---|---|---|
| Bilan energetique | Consommation electrique par unite | 4800 | 3000 | kWh/j |  | 60 % |
| Bilan energetique | PCI du gaz de procede issu de l'organique | 0.5 | 11.0 | MJ/kg | D-002 | 80 % |
| Bilan energetique | PCI du gaz de procede issu du plastique | 5.54 | 37.3 | MJ/kg | D-001 | 100 % |
| Bilan energetique | Provision de fioul de secours | absent (fioul plein : 7 495 L/j) | 0.05 | fraction du besoin | D-003 | 30 % (non instruit) |
| Bilan energetique | Rendement du bruleur | absent (100% implicite) | 0.85 | fraction |  | 90 % |
| Charges d'exploitation | Annee d'atteinte du regime etabli | sans objet (4% fixe) | 10 | annee |  | 30 % (non instruit) |
| Charges d'exploitation | Derniere annee au taux bas | sans objet (4% fixe) | 4 | annee |  | 30 % (non instruit) |
| Charges d'exploitation | ETP coeur par unite supplementaire | absent (compteur d'unites inactif) | 3 | ETP |  | 30 % (non instruit) |
| Charges d'exploitation | Taux de maintenance, annees 1 a N | 4% des l'annee 1 (pas de rampe) | 0.01 | fraction | D-007 | 100 % |
| Investissement | Majoration ingenierie par unite | absent (compteur d'unites inactif) | 0.2 | fraction |  | 30 % (non instruit) |
| Investissement | Prix bureaux | absent (batiment forfaitaire 5 MEUR) | 1300 | EUR/m2 |  | 100 % |
| Investissement | Prix stockage | absent (batiment forfaitaire 5 MEUR) | 500 | EUR/m2 |  | 100 % |
| Investissement | Prix usine de traitement | absent (batiment forfaitaire 5 MEUR) | 900 | EUR/m2 | D-006 | 100 % |
| Investissement | VRD, fondations, raccordements, 1re unite | absent (inclus dans le forfait batiment) | 1300000 | EUR |  | 80 % (non instruit) |
| Prix de vente et d'achat | Prix du fioul (GNR) | 0.4 | 0.95 | EUR/L |  | 100 % |
| Prix de vente et d'achat | Prix huile qualite combustible | absent (scenario bas 480) | 350 | EUR/T |  | 50 % |
| Prix de vente et d'achat | Reduction carbone certifiee | 1,04 T CO2/T calcule (base incineration 1,80) | 0.0 | T CO2/T traitee | D-005 | 30 % (non instruit) |

## Parametres ajoutes dans le V4 (absents du V3) (28)

| Domaine | Parametre | V3 | V4 | Unite | Decision | Confiance |
|---|---|---:|---:|---|---|---|
| Bilan carbone de l'installation | CO2 par tonne d'huile brulee | — | 3.1 | T CO2/T |  | 100 % |
| Bilan carbone de l'installation | PCI de l'huile | — | 43 | GJ/T |  | 100 % |
| Bilan carbone de l'installation | Teneur en carbone de la fraction organique | — | 0.45 | fraction |  | 100 % |
| Bilan carbone de l'installation | Teneur en carbone des plastiques | — | 0.857 | fraction |  | 100 % |
| Bilan carbone de l'installation | Teneur en carbone du char | — | 0.5 | fraction |  | 80 % |
| Bilan carbone de l'installation | Teneur en carbone du gaz de procede | — | 0.8 | fraction |  | 100 % (non instruit) |
| Bilan carbone de l'installation | Teneur en carbone du residu plastique | — | 0.8 | fraction |  | 80 % |
| Charges d'exploitation | Ceramique SEA CORAL | — | 15000 | EUR/an/unite |  | 80 % (non instruit) |
| Charges d'exploitation | Charbon actif, affinage eau | — | 40000 | EUR/an/unite |  | 30 % (non instruit) |
| Charges d'exploitation | Couche catalytique halogenes | — | 150000 | EUR/an/unite |  | 80 % (non instruit) |
| Investissement | Cuve de neutralisation et decantation | — | 250000 | EUR | D-008 | 30 % (non instruit) |
| Investissement | Surface bureaux, 1re unite | — | 200 | m2 |  | 90 % |
| Investissement | Surface stockage dechets, 1re unite | — | 640 | m2 |  | 90 % |
| Investissement | Surface stockage produits, 1re unite | — | 810 | m2 |  | 90 % |
| Investissement | Surface usine de traitement, 1re unite | — | 3000 | m2 |  | 90 % |
| Investissement | VRD par unite ajoutee | — | 400000 | EUR |  | 30 % (non instruit) |
| Investissement | Variation par unite ajoutee | — | -38.5 | m2 |  | 90 % |
| Investissement | Variation par unite ajoutee | — | -30 | m2 |  | 90 % |
| Investissement | Variation par unite ajoutee | — | -18 | m2 |  | 90 % |
| Investissement | Variation par unite ajoutee | — | 12.5 | m2 |  | 90 % |
| Prix de vente et d'achat | Qualite d'huile retenue (combustible / craqueur) | — | craqueur | - | D-004 | 90 % |
| Traitement de l'eau de procede | Carbonate de calcium | — | 2.5 | kg/T traitee | D-008 | 100 % |
| Traitement de l'eau de procede | Cout d'elimination du concentrat | — | 110 | EUR/T |  | 30 % (non instruit) |
| Traitement de l'eau de procede | Part de la phase organique recyclee en benne | — | 0.0 | fraction | D-008 | 30 % (non instruit) |
| Traitement de l'eau de procede | Prix du carbonate | — | 120 | EUR/T |  | 30 % (non instruit) |
| Traitement de l'eau de procede | Rendement huile au recyclage | — | 0.6 | fraction |  | 30 % (non instruit) |
| Traitement de l'eau de procede | Taux de recuperation d'eau du SEA CORAL | — | 0.78 | fraction |  | 90 % |
| Traitement de l'eau de procede | Teneur en phase organique de l'eau | — | 0.05 | fraction |  | 30 % (non instruit) |

## Parametres identiques (63)

| Domaine | Parametre | V3 | V4 | Unite | Decision | Confiance |
|---|---|---:|---:|---|---|---|
| Bilan carbone de l'installation | CO2 par litre de fioul | 2.68 | 2.68 | kg/L |  | 100 % |
| Bilan energetique | Besoin thermique | 2714 | 2714 | MJ/T |  | 90 % |
| Bilan energetique | PCI du char organique | 15 | 15 | MJ/kg |  | 80 % |
| Bilan energetique | PCI du fioul | 38 | 38 | MJ/L |  | 100 % |
| Bilan energetique | PCI du residu plastique | 25 | 25 | MJ/kg |  | 80 % |
| Capacite et disponibilite | Capacite nominale par unite | 200 | 200 | T/j |  | 90 % |
| Capacite et disponibilite | Jours d'exploitation par an | 330 | 330 | j/an | D-011 | 90 % |
| Capacite et disponibilite | Masse volumique des dechets en benne | 0.7 | 0.7 | T/m3 | D-010 | 90 % |
| Capacite et disponibilite | Nombre d'unites URC-2000 | 1 | 1 | unites |  | 30 % (non instruit) |
| Charges d'exploitation | Assurance | 0.005 | 0.005 | fraction du CAPEX |  | 50 % |
| Charges d'exploitation | Cout charge par ETP | 56000 | 56000 | EUR/an |  | 50 % |
| Charges d'exploitation | ETP coeur, premiere unite | 15 | 15 | ETP |  | 90 % |
| Charges d'exploitation | ETP tri par unite | 7 | 7 | ETP |  | 30 % (non instruit) |
| Charges d'exploitation | Provision et divers | 0.02 | 0.02 | fraction du CAPEX |  | 30 % (non instruit) |
| Charges d'exploitation | Taux de maintenance en regime etabli | 0.04 | 0.04 | fraction |  | 100 % |
| Composition du gisement | Humidite | 0.08 | 0.08 | fraction |  | 50 % |
| Composition du gisement | Part aluminium des metaux | 0.15 | 0.15 | fraction |  | 50 % |
| Composition du gisement | Part ferreuse des metaux | 0.8 | 0.8 | fraction |  | 50 % |
| Composition du gisement | Part inertes mineraux | 0.02 | 0.02 | fraction |  | 100 % |
| Composition du gisement | Part metaux | 0.05 | 0.05 | fraction |  | 50 % |
| Composition du gisement | Part organique et cellulose | 0.47 | 0.47 | fraction |  | 50 % |
| Composition du gisement | Part plastique | 0.3 | 0.3 | fraction |  | 50 % |
| Composition du gisement | Part verre | 0.055 | 0.055 | fraction |  | 100 % |
| Composition du gisement | Taux de refus a l'entree | 0.02 | 0.02 | fraction |  | 50 % |
| Financement et fiscalite | Duree d'amortissement | 15 | 15 | ans |  | 100 % |
| Financement et fiscalite | Duree du pret | 10 | 10 | ans |  | 100 % |
| Financement et fiscalite | Horizon du modele | 15 | 15 | ans |  | 30 % (non instruit) |
| Financement et fiscalite | Impot sur les societes | 0.25 | 0.25 | fraction |  | 100 % |
| Financement et fiscalite | Inflation | 0.02 | 0.02 | fraction |  | 30 % (non instruit) |
| Financement et fiscalite | Part de dette | 0.7 | 0.7 | fraction |  | 100 % |
| Financement et fiscalite | Taux d'interet | 0.12 | 0.12 | fraction |  | 100 % |
| Financement et fiscalite | Taux de charge annee 1 | 0.7 | 0.7 | fraction |  | 50 % |
| Financement et fiscalite | Taux de charge annee 2 | 0.85 | 0.85 | fraction |  | 50 % |
| Investissement | ATEX et depoussierage | 650000 | 650000 | EUR |  | 60 % |
| Investissement | Accessoires et pieces de rechange | 2000000 | 2000000 | EUR |  | 100 % |
| Investissement | Formation | 300000 | 300000 | EUR |  | 100 % |
| Investissement | Fret depuis le Japon | 400000 | 400000 | EUR |  | 100 % |
| Investissement | Ingenierie, ICPE, MOE, 1re unite | 750000 | 750000 | EUR |  | 60 % |
| Investissement | Installation et mise en service | 200000 | 200000 | EUR |  | 100 % |
| Investissement | Ligne de post-tri | 430000 | 430000 | EUR |  | 60 % |
| Investissement | Ligne de pre-tri | 1080000 | 1080000 | EUR |  | 50 % |
| Investissement | Machine URC-2000 | 50000000 | 50000000 | EUR |  | 100 % |
| Investissement | Taux d'aleas | 0.05 | 0.05 | fraction |  | 50 % |
| Prix de vente et d'achat | Cout d'elimination des residus | 110 | 110 | EUR/T |  | 100 % |
| Prix de vente et d'achat | Gate fee moyen | 110 | 110 | EUR/T |  | 100 % |
| Prix de vente et d'achat | Prix aluminium | 1400 | 1400 | EUR/T |  | 100 % |
| Prix de vente et d'achat | Prix autres metaux | 500 | 500 | EUR/T |  | 100 % |
| Prix de vente et d'achat | Prix de l'electricite | 0.15 | 0.15 | EUR/kWh |  | 30 % (non instruit) |
| Prix de vente et d'achat | Prix du char | 100 | 100 | EUR/T |  | 60 % |
| Prix de vente et d'achat | Prix du credit carbone | 50 | 50 | EUR/T CO2 |  | 100 % |
| Prix de vente et d'achat | Prix du verre | 30 | 30 | EUR/T |  | 30 % (non instruit) |
| Prix de vente et d'achat | Prix ferreux | 250 | 250 | EUR/T |  | 100 % |
| Prix de vente et d'achat | Prix huile specification craqueur | 641 | 641 | EUR/T |  | 90 % |
| Rendements du procede | Criblage du char au post-tri | 0.85 | 0.85 | fraction |  | 50 % |
| Rendements du procede | Masse volumique de l'huile | 0.85 | 0.85 | kg/L |  | 100 % |
| Rendements du procede | Metaux recuperes du char | 0.8 | 0.8 | fraction |  | 50 % |
| Rendements du procede | Recuperation aluminium au pre-tri | 0.75 | 0.75 | fraction |  | 80 % |
| Rendements du procede | Recuperation ferreux au pre-tri | 0.9 | 0.9 | fraction |  | 80 % |
| Rendements du procede | Recuperation verre au pre-tri | 0.7 | 0.7 | fraction |  | 80 % |
| Rendements du procede | Rendement char sur fraction organique | 0.69 | 0.69 | fraction |  | 80 % |
| Rendements du procede | Rendement gaz sur plastique | 0.193 | 0.193 | fraction |  | 80 % |
| Rendements du procede | Rendement huile sur fraction plastique | 0.69315 | 0.69315 | fraction |  | 80 % |
| Rendements du procede | Rendement residu solide sur plastique | 0.10325 | 0.10325 | fraction |  | 80 % |

## Resultats, une machine, annee 3

| Grandeur | V3 | V4 |
|---|---:|---:|
| CAPEX total | 63 780 500 | 64 059 750 |
| Recettes | 16 127 319 | 13 884 998 |
| dont credits carbone | 2 499 457 | 0 |
| Charges | 7 269 259 | 4 775 823 |
| dont fioul de chauffe | 1 029 265 | 191 842 |
| EBITDA | 8 858 061 | 9 109 175 |
| Gate fee d'equilibre | non calcule | 9,66 EUR/T |

## Fichiers de reference

Deposer dans ce dossier, pour que les chemins du registre de preuves soient valides :

- `UR-Financial-Model-V4.xlsx` : derniere version, telechargee depuis la conversation du 19/09/2026
- `UR-Financial-Model-Restructured-V3.xlsx` : copie de `pour-finaliser/UR-Financial-Model-Restructured-V3.xlsx`
