# Coûts de traitement (gate fees) des déchets ménagers et assimilés en France, et TGAP

Recherche du 10/10/2026. Identifiants : voir `registre-sources.yaml`.

## Avertissement de lecture

1. **Aucune source nationale récente ne publie un prix d'entrée hors TGAP.** Les références disponibles sont TGAP comprise. Les valeurs « hors TGAP » ci-dessous sont des **[calcul]** et ne doivent pas être citées comme données publiées.
2. **Les définitions diffèrent :** coût net médian (référentiel ADEME), médiane des charges (déclinaisons régionales), prix facturé (AMORCE). Les valeurs ne sont pas strictement comparables.
3. Tous les montants sont en € HT par tonne entrante, sauf mention contraire.

---

## 1. Synthèse par mode de traitement

| Mode | Coût publié (€ HT/t) | Base | TGAP 2026 (€/t) | Tonnage France | Sources | Statut |
|---|---|---|---|---|---|---|
| **Stockage ISDND** | **138** (médiane nationale, coût net, 2023) ; 122 (2022) ; 118 (médiane AURA 2022) ; 131 (moyenne PACA 2020-21) | TGAP comprise | **69**, puis 73, 77, 81, 85 de 2027 à 2030 | 14,2 Mt reçues dans 165 ISDND (2022) | [ADEME-REFCOUTS-2023](https://librairie.ademe.fr/societe-et-politiques-publiques/8811-10587-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-hexagonale-donnees-2023.html), [ADEME-REFCOUTS-2022](https://librairie.ademe.fr/societe-et-politiques-publiques/7932-9578-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-metropolitaine.html), [ANNMINES-2026](https://waga-energy.com/wp-content/uploads/2026/03/La-valorisation-energetique.pdf), [ADEME-AURA-2022](https://www.ordec-auvergne-rhone-alpes.fr/api/fileadmin/mediatheque_ordec/publications/Referentiel_des_couts_2022_Edition2025.pdf), [ADEME-PACA-2021](https://www.ordeec.org/fileadmin/user_upload/REF_COUTS_PACA_2021.pdf), [CIBS-TGAP-2026](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053508155) | `verifie` (référentiels ADEME 2022 et 2023, texte de loi) |
| **Incinération avec valorisation (UVE)** | **107** (médiane nationale, coût net, 2023) ; 106 (2022) ; 127 en coût complet (2022) ; 119 (médiane AURA 2022) ; Île-de-France 44 à 97 (net) | TGAP comprise | **16** (performance énergétique ≥ 65 %) ; **29** (< 65 %) ; 8 (résidus de tri performants, installation ≥ 70 %) | 14,6 Mt de DMA dans 117 UVE (2022) | [ADEME-REFCOUTS-2023](https://librairie.ademe.fr/societe-et-politiques-publiques/8811-10587-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-hexagonale-donnees-2023.html), [ADEME-REFCOUTS-2022](https://librairie.ademe.fr/societe-et-politiques-publiques/7932-9578-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-metropolitaine.html), [ANNMINES-2026](https://waga-energy.com/wp-content/uploads/2026/03/La-valorisation-energetique.pdf), [ADEME-AURA-2022](https://www.ordec-auvergne-rhone-alpes.fr/api/fileadmin/mediatheque_ordec/publications/Referentiel_des_couts_2022_Edition2025.pdf), [ORDIF-COUTS-2022](https://www.ordif.fr/fileadmin/DataStorageKit/ORDIF/Etudes/pdf/Notice_reference_couts_VF.pdf), [CIBS-TGAP-2026](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053508155) | `verifie` (référentiels ADEME 2022 et 2023, texte de loi) |
| UVE, prix facturé 2021 | moyenne 76 (clients publics, 36 à 128) ; **133 (clients privés, 83 à 262)** | Hors transport ; TGAP et HT non précisés | | | [AMORCE-DT139](https://amorce.asso.fr/publications/performances-recettes-et-couts-des-unites-de-traitement-thermique-des-dechets-donnees-2020-2021-dt139/download), p. 33, fig. 21 | `verifie` |
| Incinération sans valorisation | non trouvé | | 29 | 13 unités, 319 kt (2012) | [SINOE-ITOM2012](https://www.sinoe.org/documents/consult-and-count-doc/doc/1200/rubrique/6) | `non-verifie` |
| **Tri des collectes sélectives** | 179 à 254 (tri + refus, 2020) ; Île-de-France 223 (2022) ; médiane AURA 187 (2022) | Refus compris | TGAP sur les refus seulement | | [CITEO-2023](https://bo.citeo.com/sites/default/files/2023-03/2023_Citeo_Brochure%20co%C3%BBts%20et%20performances.pdf), [ORDIF-COUTS-2022](https://www.ordif.fr/fileadmin/DataStorageKit/ORDIF/Etudes/pdf/Notice_reference_couts_VF.pdf), [ADEME-AURA-2022](https://www.ordec-auvergne-rhone-alpes.fr/api/fileadmin/mediatheque_ordec/publications/Referentiel_des_couts_2022_Edition2025.pdf) | `verifie` |
| **TMB** | **156** (TMB compostage, médiane nationale 2023) ; 150 (TMB compostage) et 152 (TMB méthanisation) en 2022 | TGAP comprise, coût net | TGAP sur les refus (46 % des entrants en IdF, 2020) | IdF : 103 kt (2020) | [ADEME-REFCOUTS-2023](https://librairie.ademe.fr/societe-et-politiques-publiques/8811-10587-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-hexagonale-donnees-2023.html), [ADEME-REFCOUTS-2022](https://librairie.ademe.fr/societe-et-politiques-publiques/7932-9578-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-metropolitaine.html), [ADEME-REF-2016](https://www.ordeec.org/fileadmin/user_upload/rapport-referentiel-cout-service-public-dechets_2019_v1.pdf), [ORDIF-TMB-2022](https://www.ordif.fr/fileadmin/DataStorage/user_upload/ORDIF_Notice_TMB_2020-2021_vf.pdf) | `verifie` |
| **Compostage** | 41 à 76 (modèle) ; déchets verts IdF : 40 (2022) | | Non soumis | IdF : 336 kt (2022) | [CME-BIODECH-2022](https://www.fnade.org/ressources/_pdf/publications/4263/Synthe%CC%80se-biode%CC%81chets-des-m%C3%A9nages.pdf), [ORDIF-COUTS-2022](https://www.ordif.fr/fileadmin/DataStorageKit/ORDIF/Etudes/pdf/Notice_reference_couts_VF.pdf) | `verifie` |
| **Méthanisation des biodéchets** | 83 à 162 (modèle) | | Non soumis | 16 unités, 341 kt (2022) | [CME-BIODECH-2022](https://www.fnade.org/ressources/_pdf/publications/4263/Synthe%CC%80se-biode%CC%81chets-des-m%C3%A9nages.pdf), [ANNMINES-2026](https://waga-energy.com/wp-content/uploads/2026/03/La-valorisation-energetique.pdf) | `verifie` |
| **CSR, gate fee en chaufferie** | 50 (chaufferie 19,9 MW) ; 40 (50 MW) | Payé par le producteur de CSR (modèle FNADE) | Régime non vérifié | 13 unités de préparation, 367 kt/an (2022) ; 370 kt consommées (2021) | [FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf), p. 5 | `verifie` (modélisation) |
| CSR, marché observé | accueil en chaufferie 10 à 30 ; vente en cimenterie 0 à 50 ; coût de production 85 à 115 | | | | [NORMANDIE-CSR-2021](https://neci.normandie.fr/sites/default/files/2024-04/02%20info-dechet%20V1.0.pdf), p. 6 | `verifie` |

**Ordres de grandeur 2026 [calcul]** (médianes 2023 moins TGAP 2023, plus TGAP 2026, sans inflation ni hausse des prix hors taxe) :
- stockage : 138 €/t en 2023 avec une TGAP 2023 de 51 à 61 €/t, soit environ **145 à 155 €/t** en 2026 avec une TGAP de 69 €/t. La FNADE retenait **160 €/t** pour 2025 ([FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf), hypothèse de modèle) ;
- UVE performante : 107 €/t en 2023 avec une TGAP 2023 de 12 à 14 €/t, soit environ **110 €/t** en 2026 (TGAP 16 €/t). Une UVE de performance inférieure à 65 % paie 29 €/t, soit environ +15 €/t.

À utiliser comme fourchette de positionnement, pas comme chiffre publié.

---

## 2. Citations clés

**Source primaire : référentiels nationaux des coûts ADEME** ([ADEME-REFCOUTS-2022](https://librairie.ademe.fr/societe-et-politiques-publiques/7932-9578-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-metropolitaine.html), [ADEME-REFCOUTS-2023](https://librairie.ademe.fr/societe-et-politiques-publiques/8811-10587-referentiel-des-couts-du-service-public-de-gestion-des-dechets-en-france-hexagonale-donnees-2023.html))
- Données 2022, Figure 66, p. 63 (coûts nets médians de traitement des OMR, € HT/t) : incinération 106 (n = 342), stockage 122 (n = 212), TMB compostage 150 (n = 45), TMB méthanisation 152 (n = 15) ; incinération en coût complet 127 (n = 118).
- Données 2023, Figure 33, p. 36 : incinération **107** (n = 306), stockage **138** (n = 197), TMB compostage **156** (n = 44).
- Les deux éditions, p. 9 : « Les coûts sont présentés en euros HT (sauf indication contraire) et comprennent la TGAP ».
- Données 2023, p. 36 : « le différentiel entre coût net d’incinération et de stockage (31 euros par tonne) se situe dans le bas de la fourchette du différentiel de TGAP entre ces deux types de traitement. En effet ce dernier se situait en 2023 entre 31 et 40 euros la tonne selon les configurations. »
- Synthèse 2023 : coût aidé moyen de 127 € HT/hab, en hausse de 11 €/hab entre 2022 et 2023.

**Stockage et incinération, médianes nationales 2022**
- [ANNMINES-2026](https://waga-energy.com/wp-content/uploads/2026/03/La-valorisation-energetique.pdf), p. 96 : « le coût net médian du traitement des DMA en France est de 106 €/t pour l'incinération et de 122 €/t pour l'enfouissement ». Les auteurs citent le Référentiel des coûts ADEME, données 2022.
- [ADEME-AURA-2022](https://www.ordec-auvergne-rhone-alpes.fr/api/fileadmin/mediatheque_ordec/publications/Referentiel_des_couts_2022_Edition2025.pdf), p. 28 : « Sur l'incinération, il est de 119 € par tonne et 118 € par tonne pour le stockage. » Et p. 6 : « Les coûts sont présentés en euros HT […] et comprennent la TGAP. »
- Même source, p. 50 : « l'augmentation entre 2022 et 2025 sera de +20 €/tonne à +25 €/tonne sur le stockage ».

**Tension sur le stockage**
- `AdlC-20A09` (Autorité de la concurrence, avis 20-A-09) :
  - taux de saturation des ISDND : 99,1 % en 2018 (§ 35) ;
  - capacité autorisée passée de 26,3 Mt (2010) à 19,2 Mt (2018) (§ 36) ;
  - hausse des prix d'entrée des refus de tri de 7,3 % à 25,4 % selon les régions entre octobre 2019 et janvier 2020 (§ 41).

**Prix facturé en UVE**
- [AMORCE-DT139](https://amorce.asso.fr/publications/performances-recettes-et-couts-des-unites-de-traitement-thermique-des-dechets-donnees-2020-2021-dt139/download), p. 33 : « Sur l'année 2021, le prix moyen de la tonne de déchets ménagers traitée […] hors coûts de transport ». Moyenne de 76 €/t pour les clients publics (n = 32) et de 133 €/t pour les clients privés (n = 26). Recettes énergétiques : 5 à 46 €/t (p. 17).

**CSR**
- [FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf), p. 5 : « le gate-fee calculé est de 50 € pour une chaufferie de 19,9 MW et de 40 € lorsqu'on alimente une chaufferie de 50 MW ».
- Même source : « un coût de traitement en ISDND à horizon 2025 de 160€/t […] intégrant une TGAP […] à hauteur de 65€/t ».

**Biodéchets**
- [CME-BIODECH-2022](https://www.fnade.org/ressources/_pdf/publications/4263/Synthe%CC%80se-biode%CC%81chets-des-m%C3%A9nages.pdf), p. 4 : « Le coût de compostage est compris entre 41 et 76 €/T » ; « Le coût de méthanisation est compris entre 83 et 162 €/T ».

**Coût global du service public**
- DMA, France, 2022 : 266 €/t et 144 €/hab (ADEME, repris par [ORDEEC-COUTS](https://www.ordeec.org/indicateurs/dechets-menagers-et-assimiles-dma/couts-et-financement)). Statut : `secondaire`.

---

## 3. TGAP déchets : barèmes officiels

### 3.1 Stockage des déchets non dangereux (€/t)

Sources : [BOFIP-BAREME-2024](https://bofip.impots.gouv.fr/bofip/12765-PGP.html/identifiant=BOI-BAREME-000039-20240221) (2021 à 2024) et [BOFIP-BAREME-2025](https://bofip.impots.gouv.fr/bofip/12765-PGP.html/identifiant=BOI-BAREME-000039-20250723) (2025, `verifie-recontrole`).

| Catégorie d'installation | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|
| Valorisation énergétique de plus de 75 % du biogaz capté | 37 | 45 | 52 | 59 | 65 |
| Bioréacteur avec valorisation du biogaz | 47 | 53 | 58 | 61 | 65 |
| Les deux | 30 | 40 | 51 | 58 | 65 |
| Autres installations autorisées | 54 | 58 | 61 | 63 | 65 |
| Majoration au-delà de l'objectif annuel | | | | | +5 |

### 3.2 Traitement thermique des déchets non dangereux (€/t)

| Catégorie d'installation | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|
| A : ISO 50001 | 17 | 18 | 20 | 22 | 25 |
| B : NOx < 80 mg/Nm³ | 17 | 18 | 20 | 22 | 25 |
| C : rendement énergétique ≥ 0,65 | 14 | 14 | 14 | 14 | 15 |
| A et B | 14 | 14 | 17 | 20 | 25 |
| A et C | 11 | 12 | 13 | 14 | 15 |
| B et C | 10 | 11 | 12 | 14 | 15 |
| A, B et C | 8 | 11 | 12 | 14 | 15 |
| Rendement ≥ 0,70 et résidus de tri à haut PCI | 4 | 5,5 | 6 | 7 | 7,5 |
| Autres installations autorisées | 20 | 22 | 23 | 24 | 25 |

### 3.3 À partir de 2026

- **Cadre :** loi n° 2026-103 du 19 février 2026 de finances pour 2026 (article 81). La TGAP déchets passe du Code des douanes (art. 266 sexies et 266 nonies) au Code des impositions sur les biens et services (stockage : art. L. 433-57 ; incinération : art. L. 433-86). Source : [BOFIP-RES-259](https://bofip.impots.gouv.fr/bofip/15018-PGP.html/identifiant=BOI-RES-TCA-000259-20260311). Montants également fixés par arrêté du 27 janvier 2026 ([FNTP-2026](https://www.fntp.fr/tgap-2026-les-montants-sont-publies/)).
Tarifs vérifiés dans le texte de loi ([CIBS-TGAP-2026](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053508155), JORF du 20/02/2026, texte 1 ; fichier `pdf/joe_20260220_0043_0001.pdf`), en €/t :

| Article CIBS | Catégorie | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---:|---:|---:|---:|---:|
| L. 433-57 (stockage) | Non dangereux | 69 | 73 | 77 | 81 | 85 |
| L. 433-57 (stockage) | Dangereux | 30,36 | indexé | indexé | indexé | indexé |
| L. 433-86 (traitement thermique) | Non dangereux, performance 65 à 100 % | 16 | 17 | 18 | 19 | 20 |
| L. 433-86 (traitement thermique) | Non dangereux, performance < 65 % | 29 | 33 | 37 | 41 | 45 |
| L. 433-86 (traitement thermique) | Dangereux | 15,18 | indexé | indexé | indexé | indexé |
| L. 433-90 | Résidus de tri performant, installation ≥ 70 % | 8 | 8,5 | 9 | 9,5 | 10 |

- Opération irrégulière : majoration de 200 €/t en 2026 (art. L. 433-58 et L. 433-88).
- Majoration communale possible, 2 €/t au maximum, pour les installations qui traitent des déchets ménagers (art. L. 433-59 et L. 433-91).
- Indexation sur l'inflation à partir de 2027 (art. L. 433-56 et L. 433-85).
- Du 1er janvier au 28 février 2026 : 66,20 €/t en stockage, tarif 2025 indexé (source unique : [CPTAONLINE-2026](https://www.compta-online.com/la-tgap-taxe-generale-sur-les-activites-polluantes-ao3403)).
- **Date d'effet :** 19 février 2026 (FNTP, Réglementation-environnement) ou 1er mars 2026 (Déchets Infos, Compta-Online). Non tranché dans les extraits lus.
- **Régions :** pas de taux différencié en Île-de-France ([BOFIP-BAREME-2025](https://bofip.impots.gouv.fr/bofip/12765-PGP.html/identifiant=BOI-BAREME-000039-20250723), § 60). Réfactions en Corse (20 %, 2025 à 2029) et outre-mer.

### 3.4 Objectifs réglementaires qui soutiennent la hausse des prix

- LTECV (loi n° 2015-992) : -50 % de déchets non dangereux non inertes stockés en 2025 par rapport à 2010.
- AGEC (loi n° 2020-105) : au plus 10 % des DMA mis en stockage en 2035 ([SDES-2021](https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/economie-circulaire/11-evolution-des-tonnages-de-dechetsmis)).
- Trajectoire réelle : 19,5 Mt stockées (2010), 15,1 Mt (2022), 13,9 Mt (2023) ; cible 2025 : 9,7 Mt ([ADEME-IND-DMA](https://economie-circulaire.ademe.fr/indicateurs-cles-dma)).

---

## 4. Lacunes à combler

1. Fait le 10/10/2026 : référentiels ADEME 2022 et 2023 lus, tarifs TGAP 2026-2030 lus dans la loi.
2. Prix de l'incinération sans valorisation, tonnages nationaux du tri et du compostage, régime TGAP des chaufferies CSR.
3. Date d'effet exacte des tarifs 2026.
