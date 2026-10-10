# Filières de déchets spécialisées en France : tonnages, modes de traitement, coûts

Recherche du 10/10/2026. Identifiants : voir `registre-sources.yaml`.

## Avertissement de lecture

- Aucune source publique nationale récente (2022 à 2026) ne publie de prix d'entrée par filière pour les DAE ou les déchets dangereux. Les prix trouvés sont souvent **anciens** (ADEME 2007-2008 ou 2012), **locaux** (barèmes de déchèteries, budgets de syndicats) ou **d'entreprise**. Le statut est indiqué pour chaque prix.
- **[calcul]** = valeur dérivée par nous de chiffres sourcés.

---

## Synthèse

| Filière | Tonnage/an | Modes de traitement | Coût par mode (€/t) | Statut des prix |
|---|---|---|---|---|
| **DASRI** | ≈ 170 kt | incinération 81 % ; prétraitement par désinfection 19 % (2019) | **500 à 1 000** (contre 150 à 250 pour les déchets non dangereux) | `ancien` (ADEME 2007-2008, repris tel quel en 2026) |
| **DAE non dangereux non minéraux** | ≈ 65 Mt [calcul] (2022) | recyclage 43 % (2020, tous non dangereux non minéraux) | ISDND ≈ 160 avec TGAP (hypothèse 2025) ; CSR 40 à 50 ; DIB 245 (collecte comprise, 2023) | `secondaire` ou modèle |
| Refus de tri stockés | 2,74 Mt (2020) | stockage | voir ISDND | |
| **Plastiques** | 3,76 Mt (2020) ; 2,48 Mt triés (2022) | recyclage 20 % (2022) | reprise : PET clair +240, PEHD/PP +90 (sept. 2023) ; refus en mélange : non trouvé | `verifie` (un contrat) |
| Plastiques agricoles | 102 kt collectés (2024) | recyclage ≈ 90 % | non publié | |
| **Déchets dangereux** | 11,39 Mt (2022) | valorisation matière 32 % ; ISDD 32 % ; incinération sans énergie 22 % ; avec énergie 14 % | incinération 265 à 450 ; ISDD 130 à 350 ; cimenterie 50 à 70 (hors TGAP) | `ancien` (2012) |
| Pneus usagés | 533 kt (2023) | énergie 48 % ; matière 38,4 % ; réutilisation 13,6 % | non trouvé | |
| VHU | 1,17 M véhicules (2022) | réutilisation et valorisation 96 % | non trouvé | |
| DEEE ménagers | 695 kt (2024) | recyclage 79,2 % | non trouvé | |
| Mobilier (Ecomaison) | 1 749 kt (2024) | recyclage 44 % ; énergie 48 % (340 kt de CSR) | non trouvé | |
| Textiles | 289 kt collectés (2024) | CSR 8 % | appel d'offres CSR, prix non publiés | |
| **Boues de STEP** | ≈ 1 Mt de matière sèche (2016) | épandage 44 % ; compostage 36 % ; incinération 17 % ; ISDND 1 % | co-incinération en UIOM 75 €/t de matière brute | `ancien` (2012) |
| Biodéchets non ménagers | ≈ 7,2 Mt [calcul] (2022, périmètre large) | non disponible | compostage sur plateforme 25 à 45 hors transport | `ancien` (2011) |
| BTP | 247 Mt (construction, 2022) | valorisation ≈ 70 % (bâtiment) | ISDI 3 à 40 ; ISDND 24 à 150 | `ancien` (2012) |
| Huiles usagées | ≈ 260 kt | régénération (objectif 75 puis 90 %) | non trouvé | |
| Aéroports / ICW | > 43 kt (aéroports franciliens) | ICW : incinération ou co-incinération **obligatoire** | non trouvé | |

---

## 1. DASRI (déchets d'activités de soins à risques infectieux)

**Tonnage**
- [ARS-HDF-2026](https://www.cpias.chu-lille.fr/wp-content/uploads/sites/15/2026/03/4.-Pierre-Conseil-RETEX-DASRI-ARS-journee-CPIAS.pdf) (`verifie-recontrole`) : « 170 000 tonnes de DASRI (24 %, des déchets hospitaliers) » ; « 700 000 tonnes dans le secteur hospitalier (2024) ».
- Même chiffre chez [ARS-PACA-DASRI](https://paca.ars.sante.fr/system/files/2024-07/DASRI.pdf) : « Une production nationale annuelle de 170 000 tonnes de DASRI estimée (ADEME) ». L'étude ADEME d'origine n'est pas datée.
- Patients en autotraitement ([DASTRI-2025](https://www.dastri.fr/wp-content/uploads/2026/06/CP-DASTRI-resultats_annuels_2025.pdf)) : 2 192 t brutes collectées en 2025 ; 20 165 points de collecte.

**Modes de traitement** ([HCSP-2021](https://www.hcsp.fr/Explore.cgi/Telecharger?NomFichier=hcspa20210423_covimodadincietratidesdasr.pdf), `verifie-recontrole`)
- « En 2019, 81 % du tonnage des DASRI ont été incinérés dans 25 unités autorisées […] dont 21 sont des UIOM et 4 des incinérateurs spécialisés pour le traitement des déchets dangereux. »
- « 19 % du tonnage des DASRI ont été prétraités par désinfection dans une vingtaine de centres de prétraitement. »
- « 45 unités peuvent traiter des DASRI en France métropolitaine ».
- En UIOM, les DASRI sont plafonnés à 10 % en masse en moyenne annuelle (arrêté du 20/09/2002).

**Coût**
- [ARS-HDF-2026](https://www.cpias.chu-lille.fr/wp-content/uploads/sites/15/2026/03/4.-Pierre-Conseil-RETEX-DASRI-ARS-journee-CPIAS.pdf) : DASRI « 500 à 1 000 € / tonne » ; déchets non dangereux assimilables aux ordures ménagères « 150 à 250 € / tonne ».
- Ce chiffre remonte à [ARS-IDF-2011](https://www.iledefrance.ars.sante.fr/media/2853/download), qui cite un référentiel ADEME 2007-2008. Collecte et TGAP non précisées.
- **Statut `ancien`.** Aucun prix d'appel d'offres réel n'a pu être lu. Action : obtenir un bordereau de prix de CHU ou de GHT.

**Réglementation**
- Code de la santé publique, art. R.1335-1 à R.1335-8.
- Arrêtés du 7/09/1999 (entreposage) et du 24/11/2003 (emballages).
- Traçabilité dématérialisée depuis le 1/07/2022.

**Lecture pour Urban Rig :** c'est la filière au coût le plus élevé, avec une voie thermique de fait obligatoire (incinération ou désinfection préalable). C'est l'hypothèse « DASRI 800 €/t » du modèle V3 : elle se situe dans la fourchette publiée, mais la source est ancienne et doit être actualisée avant d'être mise en avant.

---

## 2. DAE non dangereux (industrie, tertiaire, refus de tri)

- Tonnage : ≈ **65,0 Mt [calcul]** en 2022, soit 92 071 kt de déchets non dangereux non minéraux moins 27 074 kt des ménages ([SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline), Tableau 1).
  - Industrie 15 845 kt ; tertiaire 14 689 kt ; construction 14 149 kt ; traitement des déchets et de l'eau 18 172 kt ; agriculture 2 143 kt.
- Refus de tri stockés : « 2 738 kt de refus de tri » en 2020 ([FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf), p. 4).
- Résidus de tri, tous flux : 5 123 kt en 2022 ([SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline), Tableau 2).

**Coûts**

| Filière | Prix | Source | Statut |
|---|---|---|---|
| ISDND, horizon 2025 | 160 €/t, dont TGAP 65 €/t | [FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf), p. 5 | hypothèse de modèle |
| UVE, clients privés, 2021 | moyenne 133 €/t (83 à 262), hors transport | [AMORCE-DT139](https://amorce.asso.fr/publications/performances-recettes-et-couts-des-unites-de-traitement-thermique-des-dechets-donnees-2020-2021-dt139/download), p. 33 | verifie |
| Chaufferie CSR | 40 à 50 €/t payés par le producteur | [FNADE-CSR-2023](https://www.fnade.org/ressources/documents/source/1/4855-FNADE-SN2E-Synthese-modele-economique-CSR-VDEF.pdf) | modèle |
| DIB, coût global collecte comprise | 172 €/t (2019), puis 245 €/t (2023) | [PHENIX-2023](https://www.wearephenix.com/pro/etudepourquoi-le-cout-des-biodechets-et-du-dib-continue-daugmenter/) | entreprise, source unique |
| Tout-venant incinérable en déchèterie | 195 € HT/t | [TERREDEAU-2024](https://www.cc-terredeau.fr/UserFiles/1/File/dechets-menagers/2024-grille-tarifs-public-2024-2025.pdf) | barème local |
| Encombrants enfouis en déchèterie | 219 € HT/t | [POINTFORT-2025](https://www.pointfortenvironnement.fr/wp-content/uploads/2024/12/Tarifs-pros-2025.pdf) | barème local |

Le prix facturé aux **clients privés** en UVE (133 €/t en moyenne en 2021) est le repère le plus solide pour un gate fee DAE.

---

## 3. Plastiques

- Tonnage et recyclage : voir `01-composition-tonnages-OMR-France.md`, section 4.
- Sur 3,76 Mt de 2020 ([OPECST-2023](https://www.senat.fr/rap/r22-808/r22-8081.pdf)) : 929 kt préparés pour le recyclage (24,7 %) ; 690 kt recyclés en France (18,3 %).
- « Seuls 25,2 % des emballages en plastique en France étaient recyclés en 2022 » ([STRAT3R-2025](https://www.ecologie.gouv.fr/sites/default/files/documents/Bilan%20interm%C3%A9diaire_Strat%C3%A9gie%203R_%20juin%202025.pdf)). 19 % des emballages plastiques à usage unique n'ont pas de filière de recyclage (p. 13).

**Prix de reprise** ([DOMITIENNE-2023](https://www.ladomitienne.com/wp-content/uploads/2024/02/24.010.3_Annexe_DECH_Contrats_Plastiques_lot_3.pdf), contrat avec Paprec, prix de septembre 2023, départ centre de tri) :
- PET clair : +240 €/t (plancher 180) ;
- PEHD/PP : +90 €/t (plancher 60).

**Volatilité** ([ENVMAG-2023](https://www.environnement-magazine.fr/recyclage/article/2023/07/10/145056/matieres-plastiques-recyclees-des-perspectives-sombres-pour-second-semestre-2023), communiqué Federec) : « les prix du PET recyclé en collecte sélective baissaient de 700 €/t pour le PET clair et de 240 €/t pour le PET coloré » entre mai 2022 et mai 2023.

**Refus et plastiques en mélange :** aucun prix public sourcé (`non-verifie`). Par défaut, se référer à l'ISDND, à l'UVE ou au CSR.

**Plastiques agricoles** ([REUSSIR-2025](https://www.reussir.fr/dechets-plastiques-agricoles-une-collecte-historique-de-102-000-tonnes-pour-adivalor-en-2024), Adivalor) : 102 000 t collectées et recyclées en 2024 ; taux de collecte supérieur à 70 %.

---

## 4. Déchets dangereux

- Tonnage : **11 391 kt** en 2022 ([SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline), Tableau 1). Le dossier SARPI ([SARPI-2022](https://www.debatpublic.fr/sites/default/files/2022-09/ISDD_synth%C3%A8se_du_dossier.pdf)) cite « plus de 12 millions de tonnes ».
- Traitement 2022 ([SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline), Tableau 4, 7 529 kt traités ; parts **[calcul]**) :
  - valorisation matière 2 416 kt (32 %) ;
  - stockage en ISDD 2 411 kt (32 %) ;
  - incinération sans récupération d'énergie 1 628 kt (22 %) ;
  - incinération avec récupération d'énergie 1 074 kt (14 %).
- 13 ISDD en France ([SARPI-2022](https://www.debatpublic.fr/sites/default/files/2022-09/ISDD_synth%C3%A8se_du_dossier.pdf)).

**Coûts** ([ADEME-EY-2014](https://upds.org/wp-content/uploads/2018/10/Taux-dutilisation-et-cou%CC%82t-des-diffe%CC%81rentes-techniques-et-filie%CC%80res-de-traitement-des-sols-et-des-eaux-souterraines-pollue%CC%81s-en-France-donne%CC%81es-2012-ADEME-2014.pdf), p. 33, Tableau 8, données 2012, terres polluées, HT hors TGAP, statut `ancien`) :
- incinération DD : 265 à 450 €/t ;
- ISDD : 130 à 350 €/t ;
- cimenterie : 50 à 70 €/t.

---

## 5. Filières REP

| Filière | Données | Source |
|---|---|---|
| Pneus usagés | 533 104 t collectées (2023) ; valorisation énergétique 48 % (cimenteries), matière 38,4 %, réutilisation et rechapage 13,6 % | [CCFA-2025](https://ccfa.fr/wp-content/uploads/2025/12/CCFA-2025-FR-68-69.pdf), p. 68 |
| VHU | 1,17 million de VHU (2022) ; réutilisation et valorisation 96 % | [CCFA-2025](https://ccfa.fr/wp-content/uploads/2025/12/CCFA-2025-FR-68-69.pdf), p. 68-69 ; [ADEME-VHU](https://www.data.gouv.fr/datasets/rep-vhu-performances-cumulees-depuis-2018) |
| DEEE ménagers | 694 814 t collectées (2024) ; recyclage 79,2 % | [ECOSYSTEM-2025](https://www.ecosystem.eco/document/443) |
| Mobilier | 1 749 kt collectées (2024) ; recyclage 44 % ; valorisation énergétique 48 % ; **340 kt de CSR produites** | [ECOMAISON-2024](https://ecomaison.com/wp-content/uploads/2025/07/250192_plaquette-chiffres-cles-WEB-DEF-1.pdf) |
| Textiles | 891 kt mises sur le marché ; 289 kt collectées ; CSR 8 % ; appel d'offres « préparation de flux TLC en CSR » en mai 2026 | [REFASHION-2026](https://media-pro.refashion.fr/2026/05/webinaire-ao-csr-1-250912.pdf) |

Non trouvé : tonnage des résidus de broyage automobile (RBA), coûts à la tonne de ces filières.

---

## 6. Boues de stations d'épuration

- ≈ **1 Mt de matière sèche par an** (7 à 8 Mt de matière brute), données 2016 ([AMORCE-EAT11](https://amorce.asso.fr/publications/gestion-des-boues-urbaines-quelle-methodologie-pour-elaborer-une-strategie-territoriale-dans-un-contexte-reglementaire-mouvant-eat11/download), p. 2).
- Destinations (même source) : épandage 44 % ; compostage 36 % ; incinération 17 % ; valorisation industrielle 1 % ; ISDND ≈ 1 %.
- Coût : « Le coût du co-traitement thermique de boues est en moyenne de 75 €HT/tMB » ([AMORCE-DT51](https://bdd.pseau.org/outils/ouvrages/amorce_boues_de_step_techniques_de_traitement_valorisation_et_elimination_2012.pdf), p. 26, 2012, `ancien`).

---

## 7. Biodéchets des gros producteurs

- « Déchets animaux et végétaux » : 12 012 kt en 2022, dont 4 833 kt de ménages ([SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline)). Non ménagers : ≈ 7,2 Mt **[calcul]**, périmètre plus large que les seuls déchets alimentaires.
- Tri à la source généralisé au 1/01/2024 (loi AGEC).
- Compostage sur plateforme : « de 25 à 45 €/t entrante (sans le transport) » ([ADEME-RA-2011](https://draaf.auvergne-rhone-alpes.agriculture.gouv.fr/IMG/pdf/guide-dechets-alimentaires_cle4a682d.pdf), `ancien`).
- Hausse : « la facture biodéchets a explosé de 70% en 4 ans » ([PHENIX-2023](https://www.wearephenix.com/pro/etudepourquoi-le-cout-des-biodechets-et-du-dib-continue-daugmenter/), entreprise).

---

## 8. BTP

- Construction : 247 435 kt en 2022 ([SDES-2022](https://www.statistiques.developpement-durable.gouv.fr/media/6908/download?inline)). Bâtiment seul : ≈ 42 Mt/an, dont 75 % d'inertes, 23 % de non dangereux non inertes et 2 % de dangereux, surtout de l'amiante ([MTE-PMCB](https://www.ecologie.gouv.fr/politiques-publiques/produits-materiaux-construction-du-secteur-du-batiment-pmcb)).
- « Le taux de valorisation des déchets du bâtiment est estimé à près de 70 % » ([MTE-PMCB](https://www.ecologie.gouv.fr/politiques-publiques/produits-materiaux-construction-du-secteur-du-batiment-pmcb)).
- Coûts ([ADEME-EY-2014](https://upds.org/wp-content/uploads/2018/10/Taux-dutilisation-et-cou%CC%82t-des-diffe%CC%81rentes-techniques-et-filie%CC%80res-de-traitement-des-sols-et-des-eaux-souterraines-pollue%CC%81s-en-France-donne%CC%81es-2012-ADEME-2014.pdf), 2012) : ISDI 3 à 40 €/t ; ISDND 24 à 150 €/t. Plâtre en déchèterie : 175 à 178 € HT/t ([POINTFORT-2025](https://www.pointfortenvironnement.fr/wp-content/uploads/2024/12/Tarifs-pros-2025.pdf), [TERREDEAU-2024](https://www.cc-terredeau.fr/UserFiles/1/File/dechets-menagers/2024-grille-tarifs-public-2024-2025.pdf)).

---

## 9. Huiles usagées

« On estime que les quantités d'huiles usagées en France s'établissent à environ 260 000 tonnes par an » ([MTE-HUILES](https://www.ecologie.gouv.fr/politiques-publiques/huiles-minerales-synthetiques)). REP depuis le 1/01/2022 (éco-organisme Cyclevia).

---

## 10. Aéroports et déchets de restauration internationale (ICW)

**Réglementation** ([UE-1069-2009](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32009R1069), `verifie`)
- Article 8 f) : sont des matières de catégorie 1 « les déchets de cuisine et de table provenant de moyens de transport opérant au niveau international ».
- Article 12 : elles sont « éliminées comme déchets, par incinération » ou « éliminées ou valorisées par coïncinération ».
- Conséquence : **voie thermique obligatoire**, ni compostage ni méthanisation.

**Tonnages**
- Aéroports franciliens : « plus de 43 000 tonnes de déchets » ([PAPREC-2019](https://www.mypaprecsolutions.com/paprec-aerport-paris/), source d'entreprise unique et ancienne).
- Aucune statistique publique sur le tonnage d'ICW ni sur son coût n'a été trouvée. Action : rapport RSE ou déclaration de Groupe ADP, à récupérer à la main.
