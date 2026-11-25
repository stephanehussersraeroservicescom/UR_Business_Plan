# Réconciliation des annexes, plan d'affaires v3

Chat A, 25/11/2026. Document de travail (français), contrôlé par `verifier_sources.py`. Les annexes et le plan d'affaires restent en anglais.

**Ce qui a été comparé.** Les sources Markdown des annexes 1 à 5 et 7 à 9 (`annexes/ANNEX-0*.md`), après les corrections Codex du 25/11/2026, et les registres en lecture seule : `calculs.yaml`, `_decisions.yaml`, `a-rechercher.yaml`, registres d'écarts `ecarts-annexe-*.md`. Thèmes : capacité, CAPEX, statut de l'huile et du char, rendements, prix, classement ICPE et IED, énergie, hypothèses D-xxx. L'annexe 6 (CDG) est mise de côté et n'a pas été comparée. Aucun document de l'archive n'a été ouvert (règle 16). <!-- nosrc -->

**Décisions prises pendant ce chat.** Le chat du modèle financier (chat B) a enregistré à partir de 16 h 22 les décisions D-066 à D-073 de Stéphane. Elles tranchent plusieurs points relevés ici ; les annexes ont été alignées sur elles (section 2) et les points concernés sont classés en section 3. <!-- nosrc -->

**Règle appliquée.** Une contradiction simple (arrondi, texte non mis à jour après la correction d'une autre annexe ou après une décision datée, formulation plus affirmative que l'annexe qui porte la preuve) est corrigée dans l'annexe. Une contradiction qui change une valeur du modèle ou une hypothèse va dans « À trancher par Stéphane ». Aucune valeur de `params/` ni aucun registre partagé n'a été modifié ; les ajouts de registre sont dans `notes-reconciliation/corrections-registres-2026-11-25.yaml`.

## 1. Contradictions entre annexes, corrigées

| Réf. | Sujet | Formulation A | Formulation B | Bonne formulation et preuve | Correction faite |
|---|---|---|---|---|---|
| C-1 | Rendement moyen d'huile des 10 essais | Annexes 5 et 7 : « 73.07 % » | Annexe 2 : « 73.1 % », arrondi révisé à « 73.08 % » | 73,08 % : le calcul vaut 292,3 / 400 [calc:CALC-A2-HUILE10-MOY-POND] | Annexes 5 (3 occurrences) et 7 (1) passées à 73.08 % ; texte de D-044 à corriger (fichier de corrections). Aucun résultat de calcul ne change |
| C-2 | Exclusion de la pyrolyse du chapitre incinération de l'IED | Annexe 2, § 2.7.1 : texte de 2010 (gaz purifiés, émissions du gaz naturel) [IED-2010-75-ANX6-P3] | Annexes 1 et 4 : texte modifié en 2024 (combustible le moins polluant utilisable dans l'installation) [A4-IED-2024-1785-ART42] | Le texte en vigueur est celui de 2024 [A4-IED-2024-1785-ART42] | § 2.7.1 de l'annexe 2 réécrit, renvoi à l'annexe 4 ; la conclusion (limites de l'incinération, cas prudent) ne change pas |
| C-3 | Débouchés de l'huile sans PVC | Annexe 2, message clé 6 : sans PVC ou après déchloration, l'huile « ouvrirait » recyclage chimique, fioul marine et carburéacteur | Annexe 3 : vapocraqueur réservé aux plastiques triés, point d'éclair et soufre à raffiner, carburéacteur non ouvert à court terme [A3-ARRETE-SSD-HUILE-PYROLYSE-2024] | Annexe 3, qui lit les textes | Message clé 6 reformulé : le chlore ne ferme plus ces débouchés, les autres conditions de l'annexe 3 restent |
| C-4 | Statut de l'huile de déchets municipaux | Annexe 3 : déchet dangereux (HP 3, point d'éclair sous 40 °C) [A3-REG1357-2014-HP3] [CHIBA-JLOS-HUILES] | Annexes 1, 4 et 5 : « vendue comme déchet », sans le caractère dangereux | Annexe 3 [A3-REG1357-2014-HP3] | Mention HP 3 ajoutée : annexe 4 (message clé et § 4.3.1), annexe 5 (§ 5.6), annexe 1 (§ 1.4.7) |
| C-5 | Char : produit vendable | Annexe 5 : « Char is the main marketable product » | Annexe 3 : usage le plus souvent payé par le producteur [A3-OBS-NORMANDIE-CSR-2021] | Annexe 3 | Annexe 5 : « main solid product », vente et prix renvoyés à l'annexe 3 |
| C-6 | Valeur du char | Annexe 3, message clé : 123 à 255 EUR/t [calc:CALC-A3-CHAR-PARITE-PETCOKE] [calc:CALC-A3-CHAR-PARITE-INSEE] | Annexe 3, § 3.7 : de 50 EUR/t payés par l'usine à 123 EUR/t [A3G-ALBA-EBS-HINTERGRUND-2023] | Les deux sont sourcés ; le message clé ne donnait que la borne haute | Message clé complété (borne haute, pratique du marché, défaut D-068) |
| C-7 | Pouvoir calorifique du char | Annexe 3 : 32 090 J/g seul [IZUMITEC-R35-339439] | Annexes 2 et 5 : cas haut ; cas prudents 24,6 MJ/kg [calc:CALC-A2-PCI-CHAR-PLASTIQUE] et 24,55 MJ/kg [calc:CALC-A5-KHAN-PCS-MJ-KG] [hyp:D-038] | D-038 et annexe 5 [hyp:D-038] | § 3.2.1 de l'annexe 3 : 32 090 J/g présenté comme cas haut, cas prudents rappelés, sans nouveau chiffre de prix |
| C-8 | Consommations par tonne | Annexes 1, 3, 5, 7 : 1 507 MJ/t, 259 MJ/t, 72 kWh/t, 8,73 EUR/t « par tonne traitée » [calc:CALC-A2-BRULEUR-MJ-T] [calc:CALC-A3-ELEC-EUR-T] | Calculs faits à 200 t/jour [UR2000-JP-P08-SPEC] ; plan à 140 t/jour [hyp:D-035] | Base 200 t/jour des calculs ; le modèle prend les consommations par jour [hyp:D-072] [hyp:D-073] | Base « nominal 200 t per day » écrite à chaque occurrence, et valeur du modèle à 140 t/jour ajoutée en annexes 1, 3 et 5 [calc:CALC-MOD-BRULEUR-MJ-T-140] |
| C-9 | Combustible en régime établi | Annexe 1 : aucun combustible après le démarrage selon OneWorld [OW-ENG-P02-P14-AFFIRMATIONS] | Annexes 2, 3 et 9 : 10 000 L/jour dans le tableau de consommation [OW-CONSO-ENERGIE] | Les deux documents OneWorld se contredisent (règle 13) | Contradiction affichée en annexe 1 (§ 1.4.5) et en annexe 9 (§ 9.2) |
| C-10 | Grandpuits et Plastic Energy | Annexe 3 : TotalEnergies « with Plastic Energy » ; annexe 4 : « in production » | Annexe 8 : démarrage en mars 2026, TotalEnergies seul propriétaire [A8-CST-TTE-RACHAT-2026] ; « technology partner went into administration » | La fiche lue nomme une société de financement, Plastic Energy Finco Ltd [A8-CST-GAZETTE-PE-2026] | Annexes 3 et 4 mises à jour ; annexe 8 précisée (Plastic Energy Finco Ltd, pas tout le groupe) |

## 2. Annexes alignées sur les décisions D-066 à D-073

| Réf. | Ce que disait l'annexe | Décision | Correction faite |
|---|---|---|---|
| C-11 | Annexe 4, § 4.3.3 : TGAP payée par l'usine en interrupteur « off by default » | Interrupteur activé par défaut, 16 EUR/t [hyp:D-073] [CIBS-TGAP-2026] | Phrase remplacée |
| C-12 | Annexe 3, § 3.7 : facteur de qualité de l'huile et prix du char « to decide » ; hydrogène à 2 EUR/kg par défaut ; métaux à leur prix pour tous les flux | Huile à 0,80 du prix de référence [hyp:D-067] ; char à 0 EUR/t [hyp:D-068] ; hydrogène non compté par défaut, métaux des OMR et DAE à 0 par défaut [hyp:D-073] | Tableau 3.7, § 3.1.5, § 3.2.4, message clé du char et § 3.8 mis à jour |
| C-13 | Annexes 1, 3, 5 et 9 : chaleur manquante « achetée » ; disponibilité non déduite | Déficit couvert par l'huile par défaut [hyp:D-069] ; brûleur et électricité par jour [hyp:D-072] [hyp:D-073] ; 330 jours par an [hyp:D-073] | Phrases ajoutées en annexe 1 (§ 1.4.5), annexe 3 (§ 3.6.1 et § 3.6.2), annexe 5 (message clé énergie) et annexe 9 (§ 9.2) |

## 3. Points relevés et tranchés le 25/11/2026 (pour mémoire)

| Point relevé | Décision |
|---|---|
| Consommation par tonne à 140 t/jour, base 200 t/jour des calculs [calc:CALC-A2-BRULEUR-MJ-T] | Besoin du brûleur pris par jour, rapporté à 140 t/jour [hyp:D-072] [calc:CALC-MOD-BRULEUR-MJ-T-140] |
| Électricité 600 kW [OW-CONSO-ENERGIE] ou 20 kW [UR2000-JP-P08-SPEC] | 600 kW, soit 14 400 kWh/jour par ligne [hyp:D-073] |
| Chaleur manquante sur OMR et DAE [hyp:D-029] | Couverte par l'huile, puis par du gazole acheté [hyp:D-069] |
| Facteur de qualité de l'huile [hyp:D-030] | 0,80 par défaut [hyp:D-067] |
| Prix du char et sens du paiement | 0 EUR/t par défaut, bornes de la redevance à la parité coke [hyp:D-068] |
| Pouvoir calorifique du char par flux | 32,09 et 24,6 MJ/kg [hyp:D-066] [hyp:D-038] |
| Base des rendements, matière sèche [hyp:D-044] ou masse brute [hyp:D-049] | Les deux confirmées pour le modèle [hyp:D-073] ; le plan écrit qu'elles ne se comparent pas |
| Disponibilité de la machine | 330 jours par an [hyp:D-073] |
| Pré-traitement par ligne | 5 MEUR par ligne [hyp:D-066] ; ATEX, post-tri et décanteur compris dans les 10 MEUR [hyp:D-073] |

## 4. À trancher par Stéphane

| Réf. | Sujet | Formulation A | Formulation B | Ce que disent les sources et décisions | Choix à faire |
|---|---|---|---|---|---|
| T-1 | Tonnage reçu ou charge du réacteur | D-035 : 140 t/jour est la charge du réacteur après tri ; un tri qui retire de la masse impose de recevoir davantage [hyp:D-035] | Annexes 4, 5 et 7 : 51 100 t/an traités comme tonnage reçu, inertes compris (part de l'Île-de-France, 6 000 t de refus de tri) [calc:CALC-A8-CAPACITE-AN] [calc:CALC-A4-PART-OMR-IDF] [calc:CALC-A5-NONPROC-T-AN] | D-035 : « tonnage reçu = tonnage du réacteur / part conservée après tri » ; les bilans par tonne des annexes 5 et 7 sont exprimés par tonne reçue, inertes compris [hyp:D-035] | (a) 140 t/jour = charge du réacteur : le tonnage reçu, la redevance et les refus sont plus élevés selon le gisement ; (b) 140 t/jour = tonnage reçu : la charge réelle du réacteur est plus faible. Point le plus important pour le modèle par flux (D-070) |
| T-2 | « Recovery loss » de 11,5 % prise comme gaz | Annexes 1, 2 et 3 : gaz de conception, 2,9 fois le besoin du brûleur, surplus et hydrogène [calc:CALC-A2-COUV-BRULEUR-RESINE] [calc:CALC-A3-GAZ-SURPLUS-RESINE] [calc:CALC-A3-H2-KG-T-RESINE] | OneWorld écrit que cette perte part surtout en fumées [OW-ENG-P16-BILAN] | Écart E-1 du lot 2 de l'annexe 2, à trancher ; le modèle des flux plastiques compte 10 % de gaz [hyp:D-071] [hyp:D-029] | Garder la ligne étiquetée hypothèse de travail dans les annexes 1 à 3, ou la retirer jusqu'à un bilan gazeux mesuré ; aligner les annexes sur D-071 |
| T-3 | Combustible de 10 000 L/jour | Pas de combustible après démarrage [OW-ENG-P02-P14-AFFIRMATIONS] | 10 000 L/jour [OW-CONSO-ENERGIE] ; sur OMR à 10 % de résines, le gaz ne couvre que 0,94 fois ce combustible [hyp:D-028] | D-069 règle la chaleur manquante calculée sur le brûleur, pas cette consommation déclarée [hyp:D-069] | Retenir ou non les 10 000 L/jour comme cas de sensibilité (annexe 2, § 2.6.4) ; demande R-060 à OneWorld |
| T-4 | Double comptage en annexe 5 | Annexe 5 : textiles sanitaires et textiles comptés pour le liquide et le gaz (D-048) et aussi dans la matière organique du char (D-045) [calc:CALC-A5-SEC-ORG2-KG-T] [calc:CALC-A5-SEC-CELLU-ST-KG-T] | Annexe 7 : même cumul corrigé par D-054 (char limité au complément à 100 %) [hyp:D-054] | Au cas optimiste, liquide, gaz et char de ces fractions dépassent leur masse [hyp:D-048] [hyp:D-045] ; D-073 confirme D-054 pour le modèle sans dire s'il s'applique à l'annexe 5 [hyp:D-073] | Appliquer la règle de D-054 à l'annexe 5, puis refaire CALC-A5-CHAR2-* et CALC-A5-QUANT-* (registres, chat principal), puis le texte de l'annexe 5 |
| T-5 | Redevance d'entrée des DAE en mélange | OMR et refus de tri ménagers : 100 EUR/t [hyp:D-039] [hyp:D-042] | DAE en mélange : aucun défaut ; refus de tri payés environ 200 EUR/t aujourd'hui [A7-ADEME-TRI-DAE-2025] | Point B18, ouvert [hyp:D-073] | Valeur par défaut pour les DAE en mélange et leurs refus de tri |
| T-6 | Classement ICPE et IED | 2771 probable, 3520 par prudence [hyp:D-052] | Hypothèse posée par Claude, non confirmée par Stéphane | Annexes 1, 2 et 4 cohérentes avec D-052 | Confirmer D-052 comme hypothèse du plan (l'inspection reste à consulter, R-050) |
| T-7 | Facteur de qualité de l'huile selon le flux | Un facteur unique de 0,80 [hyp:D-067] | Huile d'OMR et de DAE : déchet dangereux hors spécifications, aucun acheteur identifié [A3-REG1357-2014-HP3] | D-067 s'appuie sur un précédent de 2009 pour des huiles de plastiques triés [A3F-SAPPORO-SPR-2009-PRIX-FRACTIONS] | Garder 0,80 pour tous les flux, ou un facteur plus bas pour les OMR et les DAE |

## 5. Points vérifiés sans contradiction

- **Capacité.** 200 t/jour nominal [UR2000-JP-P08-SPEC] et 140 t/jour de charge [hyp:D-035] sont employés de la même façon dans les annexes 1, 4, 7, 8 et 9 ; le tableau OneWorld refait à 120 t/jour en annexe 2 applique la masse volumique de OneWorld (0,6) à son propre exemple, comme le prévoit D-035 [calc:CALC-A2-OW16C-ENTREE].
- **CAPEX.** 60 MEUR par ligne avant transport [calc:CALC-A9-CAPEX-LIGNE] n'apparaît que dans l'annexe 9, comme base et non comme besoin de financement, et D-066 le reprend [hyp:D-066]. Le chiffre de 60 000 000 du document Hardin, sans devise, est affiché comme autre chiffre [HARDIN-LOI].
- **Classement.** Rubrique 2771 et IED 3520 par prudence dans les annexes 1, 2 et 4 [hyp:D-052].
- **Redevances de référence et TGAP.** Mêmes valeurs dans les annexes 4, 5, 7 et 8 : 109,4 EUR/t [A8-CST-SYCTOM-BP-2026], 120 EUR/t [A8-PRIX-AMORCE-DT156-2023], TGAP 2026 [CIBS-TGAP-2026].
- **Dioxines, fertilisant, carbone.** Mêmes valeurs et mêmes conclusions dans les annexes 1, 2 et 3 [DIOXINES-2023] [FPR-2019-1009] [hyp:D-028].
- **Gaz du plastique en mélange.** 10 % de la masse de plastique partout [hyp:D-029].

## 6. Compte rendu (règle 10)

| Élément | Statut | Où |
|---|---|---|
| Contradictions entre annexes, thèmes demandés | Trouvé : 10 corrigées entre annexes, 3 alignements sur D-066 à D-073, 7 à trancher | Sections 1, 2 et 4 | <!-- nosrc -->
| Base des consommations OneWorld (par jour ou par tonne) ; combustible de 10 000 L/jour [OW-CONSO-ENERGIE] | Non trouvé dans les documents OneWorld lus ; demande R-060 | Fichier de corrections |
| Annexe 6 (CDG) | Non comparée (mise de côté) | |
| Contradictions avec l'archive | Non recherchées (règle 16) | | <!-- nosrc -->

Points à faire contrôler par Stéphane : T-1 et T-4, qui changent des résultats par tonne.
