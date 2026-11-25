# Écarts de l'annexe 2 après contre-vérification Codex (25/11/2026)

Rapports : `2026-11-25-codex-annexe-02-lot-1.md` et `lot-2.md`. Lot 3 (sections 2.6, 2.8 à 2.10 et messages clés) : NON TROUVÉ dans le dossier au moment du traitement ; ses sections n'ont été touchées que par voie de conséquence des lots 1 et 2. Réserves R-1 à R-5 : `2026-10-15-codex-annexe-02-lot-1-reanalyse.md`. L'ancien registre `ecarts-annexe-02.md` (octobre) n'est pas modifié. Traitement par Claude le 25/11/2026. Version d'avant : commit `d604a2a`.

Sources rouvertes par Claude : rapport de Chiba, PDF p. 24, 27, 29, 40, 42 (pdftotext) et p. 55 et 56 (images) ; UR2000-JP p. 5 ; brochure anglaise p. 16 ; KANSO B2002600 p. 1 ; rapports 2023 (Tanabe, dioxines) ; directive 2010/75/UE sur EUR-Lex (article 50(2), annexe VI parties 3 et 6).

| Lot, écart | Gravité Codex | Sujet | Traitement |
|---|---|---|---|
| 1, E-1 (R-4) | important | Brochure japonaise p. 5 : base masse/volume | ACCEPTÉ : p. 5 relue ; les quantités imprimées sont les pourcentages du volume d'entrée (25 % de 200 m³ = 50 m³ ; 5 % de 200 000 L = 10 000 L). Sections 2.3.3, 2.8 et 2.9.1 : « shares of the input volume, not mass fractions » ; fiche UR2000-JP-P05-BILAN et descriptions CALC-A2-UR2000-NONAFFECTE-* dans le fichier de corrections ; complément R-010 |
| 1, E-2 (R-1) | mineur | Transfert de la composition du gaz | ACCEPTÉ : § 2.2.2 « For modelling, the project assumes the air-free composition of the single gas sample analysed in 2020 … to be confirmed (R-011) » ; phrase ajoutée à D-029 dans la fiche 2.5.0 (texte de la décision non modifié) |
| 1, E-3 (R-2) | mineur | Rendement hors inertes présenté comme rendement après pré-tri | ACCEPTÉ : § 2.2.3 « used as the working yield … no pre-sorting was tested … between the two bases » ; même précision sous D-035 (fiche 2.5.0) |
| 1, E-4 (R-3) | mineur | Confiance 95 % sur des calculs dépendant de D-033 ou D-034 | ACCEPTÉ dans la source : 17 liens passés à 90 % (CALC-A2-GAZDIFF10-*, HUILE10, RESIDU10, *-NODA-0909-HORSMETAUX, NONPLAST-NODA-0909). À FAIRE par le chat principal : les pages HTML des fiches tirent leur confiance de `generer_html.py` (ensemble HYP, ligne 337), que je n'ai pas modifié ; y ajouter ces calculs |
| 1, R-3, qualification de l'exclusion du 11/07 | (réserve) | Photo non probante analytiquement | CONTESTÉ : l'exclusion est déjà présentée comme décision D-034, avec ses motifs attribués et l'essai affiché ; aucune contradiction manifeste. Transparence renforcée : moyenne d'huile sur 11 essais ajoutée (74,28 %, CALC-A2-HUILE11-MOY-POND), qui montre que l'exclusion abaisse le rendement d'huile |
| 1, E-5 (R-5) | mineur | Arrondi 73,07 %, marqueurs bruts, fiche 2.1.g, eau évaporée | ACCEPTÉ : 73,08 % (292,3 / 400 = 73,075 %) dans l'annexe et résultat du calcul dans le fichier de corrections ; cinq marqueurs `[calc:…]` de la fiche 2.5.0 passés en commentaires avec lien ; fiche CHIBA-PROCEDE-HUILE : conversion par la densité qualifiée d'inférence (p. 24 : 60 L × 0,823 = 49,4 kg ; p. 26 : 18 L × 0,874 = 15,7 kg contre 16,1 kg imprimés) ; eau évaporée : « calculated value (PDF p. 40) », citation ajoutée à CHIBA-CONSTATS |
| 1, autres interprétations 1 à 5 | | | 1 et 2 ACCEPTÉES (moyenne sur 11 essais ajoutée) ; 3 = E-3 ; 4 = E-1 ; 5 sans effet |
| 1, manques avant investissement | bloquant avant engagement | Essai continu sur la charge cible, garanties contractuelles | CONTESTÉ comme écart de l'annexe : déjà demandés en 2.9.1 (R-009, R-010) ; formulation complétée (« continuous test with a complete mass balance »). Reste bloquant avant commande ferme, pas pour le plan d'affaires |
| 2, E-1 | important | « Recovery Loss » de 11,5 % traitée comme gaz combustible | À TRANCHER (correction provisoire appliquée) : p. 16 relue, la ligne s'appelle « Recovery Loss », « Mainly discharged as flue gas; a very small amount will be carbide ». Étiquette « working assumption D-038 » posée en 2.5.3, 2.6.2, 2.6.3, 2.9, message clé 4 et fiche 2.5.0 ; descriptions des calculs dans le fichier de corrections ; complément R-011. Décision de Stéphane : garder la ligne 2,9 fois ainsi étiquetée, ou la retirer jusqu'à un bilan gazeux mesuré. Ordre de grandeur (CALCULÉ ici, non repris dans l'annexe) : même à 10 % de gaz (D-029), 0,10 × 1 000 × 37,386 = 3 739 MJ/t, soit 2,5 fois le besoin de 1 507 MJ/t (CALC-A2-GAZ-PCI, CALC-A2-BRULEUR-MJ-T) : la conclusion sur charge riche en résines ne change pas |
| 2, E-2 | important | « Yes » réglementaire sans O2 ni moyennes | ACCEPTÉ : p. 55 et 56 vues (rapports 仮 du 18/10/2022, ni O2, ni CO, ni HCl ; mesures ponctuelles) ; colonnes renommées « Raw value below the limit value? », note sous le tableau, lecture investisseurs, message clé 5 et ligne de 2.9 réécrits : « compliance not demonstrated; undocumented, not disproved » |
| 2, E-3 | important | Liste de mesures de permis incomplète | ACCEPTÉ : EUR-Lex annexe VI partie 6, point 2.1 lu ; conditions complétées (COT, HF, CO, O2, périodes réglementaires, métaux lourds et dioxines, charge cible en continu) ; nouvelle fiche A2-IED-2010-75-ANX6-P6 dans le fichier de corrections ; complément R-016 |
| 2, E-4 | important | Traitement de l'eau non démontré | ACCEPTÉ : phrase ajoutée en 2.7.4 (essai de traitabilité, bilan eau, concentrats, critères de rejet) ; complément R-017 |
| 2, E-5 | mineur | Seuil de 1 % de chlore sans son périmètre | ACCEPTÉ : article 50(2) relu (déchets dangereux, déclencheur de température) ; message clé 6 et tableau 2.4.1 corrigés |
| 2, verdict 16 | | Période des dioxines | ACCEPTÉ : 2.7.1 « average over a sampling period of 6 to 8 hours rather than a daily average » |
| 2, autre interprétation 3 | | Char : CSR non démontré | ACCEPTÉ : 2.4.4 « possible under conditions » ; spécification par lot (complément R-012) |
| 2, autre interprétation 4 | | Chlore de l'huile et débouchés | CONTESTÉ : déjà dans l'annexe (2.4.1, R-013) |
| 2, manques avant investissement | bloquant / important | Campagne continue, garanties, eau, chlore du char, spécification de l'huile | CONTESTÉ comme écart : déjà en 2.9.1 (R-009, R-012, R-013, R-016, R-017) ; compléments ajoutés aux demandes |

Décompte : 12 ACCEPTÉS, 4 CONTESTÉS, 1 À TRANCHER.

Points pour le chat principal :
- `generer_html.py` : ajouter à HYP les calculs dépendant de D-033 et D-034 (plafond 90 %) ; ajouter la fiche A2-IED-2010-75-ANX6-P6 au tableau SRC (groupe A2.4.a) pour que ses liens s'affichent ;
- fusionner `notes-recherche-annexe-02/collecte-brute/corrections-2026-11-25.yaml` ;
- régénérer le HTML de l'annexe 2.

Échelle du projet : aucun de ces points ne change la faisabilité d'une URC-2000 (51 100 t/an). Les rendements mesurés sur PE et PP (73 % à 81 % d'huile) restent la base ; les corrections portent sur l'étiquetage d'hypothèses et sur la conformité des émissions, qui reste à démontrer par une campagne de permis.

Contrôle automatique après correction (`--sans-parametres`) : 1 erreur attendue, « Calcul inconnu : CALC-A2-HUILE11-MOY-POND », créé dans le fichier de corrections ; elle disparaît à la fusion.
