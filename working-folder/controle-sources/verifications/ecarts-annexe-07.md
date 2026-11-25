# Écarts de l'annexe 7 après contre-vérification Codex (25/11/2026)

Rapports : `2026-11-25-codex-annexe-07-lot-1.md` et `lot-2.md`. Traitement par Claude le 25/11/2026. Version d'avant : commit `d604a2a`. Ajouts de registre à fusionner : `nouveau-business-plan/annexes/notes-recherche-annexe-07/collecte-brute/corrections-2026-11-25.yaml`.

| Lot, écart | Gravité Codex | Sujet | Traitement |
|---|---|---|---|
| 1, E-1 | important | « Aucun tonnage régional de DAE en mélange » : le PRPGD publie 2,77 Mt (2020), minimum | ACCEPTÉ : tableau du PRPGD relu par Claude (WebFetch) ; série 3,41 / 3,93 / 3,35 / 2,77 Mt et taux de tri 58 % en 2020 ajoutés ; une machine = 1,8 % du minimum (CALC-A7-PART-MACHINE-MELANGE-IDF-PCT) ; fiche A7-PRPGD-IDF-SUIVI3-2023 à corriger ; R-048 réduit |
| 1, E-2 | important | Enfouissement : 38,1 % = origine directe ; 77,6 % après réaffectation des refus | ACCEPTÉ : p. 5 de la notice ORDIF relue par Claude ; les deux lectures affichées, la seconde retenue pour l'origine économique (1 728 989 t, CALC-A7-IDF-DAE-ENFOUIS-REAFF-T) |
| 1, E-3 | important | Bois B : « peint, verni ou collé » non sourcé ; risque chlore et métaux | ACCEPTÉ : formule retirée ; définition prise dans le référentiel FCBA 2022 cofinancé par l'ADEME (nouvelle fiche A7-FCBA-CLASSIF-BOIS-2022, lue par WebFetch) ; mesure demandée (R-052) |
| 1, E-4 | mineur | Limites de la composition visuelle trop discrètes | ACCEPTÉ : p. 28 du rapport ADEME relue ; « tendance, pas spécification d'alimentation » |
| 1, E-5 | mineur | « Le tonnage réel est plus élevé » non démontré | ACCEPTÉ : « effet non quantifié » ; total présenté comme ordre de grandeur |
| 1, E-6 | mineur | 2021 / 2020 dans le rapport ADEME | ACCEPTÉ : 2021 gardé, incohérence du résumé signalée (relue par Claude) |
| 2, E-1 | important | Scénario optimiste : 113 kg de produits pour 100 kg de fibreux et textiles | ACCEPTÉ, À TRANCHER : char des fibreux et textiles limité à 27 % au cas optimiste (D-054) ; char optimiste 139 kg/t au lieu de 152 (CALC-A7-CHAR-HAUT-V2-KG-T) ; même cumul probable en annexe 5 (D-048), hors périmètre, signalé au chat principal |
| 2, E-2 | important | Le bilan d'une tonne ne ferme pas | ACCEPTÉ, À TRANCHER : fines 340 kg, non convertis 230 kg et masse non attribuée 237,5 / 205,5 / 172,5 kg/t affichées (CALC-A7-QUANT-*, CALC-A7-NONALLOUE-*) ; traitement par défaut comme D-053 (D-055) ; bilan massique exigé à l'essai R-021 |
| 2, E-3 | important | R-048 nie le tonnage régional | ACCEPTÉ (voir lot 1, E-1) |
| 2, E-4 | important | 200 EUR/t lisible comme recette acquise | ACCEPTÉ : « coût actuel des exutoires, non prix d'entrée acquis » ; lettre d'intention ou contrat (R-044) |
| 2, E-5 | mineur | Énergie : calcul en MJ/t absent | ACCEPTÉ : 186,93 MJ/t, 12,4 % du besoin du brûleur déclaré par OneWorld (CALC-A7-GAZ-PLAST-MJ-T, -PART-BRULEUR-PCT) ; « aucune autosuffisance ne peut être affirmée » |
| 2, points manquants | bloquant avant engagement | Bois traité, chlore, fines, variabilité, plâtre et soufre | ACCEPTÉ comme conditions avant contrat : nouvelle demande R-052 (caractérisation, spécification d'admission, plan d'échantillonnage) ; ne bloque pas le plan d'affaires |

| Autre interprétation | Traitement |
|---|---|
| Lot 1, n° 1 et 2 ; lot 2, n° 1 et 4 | Couvertes par les écarts ci-dessus |
| Lot 1, n° 3 ; lot 2, n° 5 | ACCEPTÉ : la composition décrit les flux reçus, pas les refus ni le flux contracté ; D-049 non applicable aux refus sans caractérisation |
| Lot 1, n° 4 | ACCEPTÉ : « les fines peuvent contenir eau, combustibles et inertes » |
| Lot 1, n° 5 | PARTIEL : risque du char de bois B ajouté ; « 5 % de plastiques plutôt conservateur » non repris (aucune donnée lue) |
| Lot 2, n° 2 | ACCEPTÉ (fines affichées) |
| Lot 2, n° 3 | CONTESTÉ pour l'annexe : spécification de CSR préparé (12 à 18 MJ/kg) non lue par Claude et non représentative du DAE brut ; mention dans R-048 seulement |
| Lot 2, n° 6 | ACCEPTÉ : « produit principal » ne veut pas dire produit vendable |
| Lot 2, n° 7 | ACCEPTÉ : disponibilité sous contrat et prix des plastiques professionnels non documentés ; le mot « diffus » n'est pas repris (non relu) |
| Lot 2, n° 8 | ACCEPTÉ : rapport à l'échelle d'une machine (1,0 % et 1,8 %) dans les messages clés |

Bilan : 12 écarts ACCEPTÉS (dont 2 avec une hypothèse À TRANCHER : D-054, D-055), 0 CONTESTÉ ; autres interprétations : 1 CONTESTÉE, 1 PARTIELLE. Aucun point bloquant pour le gisement : une machine représente environ 1 % des DAE franciliens et 1,8 % du minimum en mélange. Les conditions avant engagement portent sur la qualité du flux (R-052, R-021).

Contrôle automatique : 0 erreur sur l'annexe avec les registres complétés par le fichier de corrections (copie de travail hors dépôt) ; sur le dépôt actuel, seules les erreurs attendues sur les identifiants pas encore fusionnés.
