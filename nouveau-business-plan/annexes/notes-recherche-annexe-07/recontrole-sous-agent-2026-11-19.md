# Recontrôle indépendant des fiches de l'annexe 7

Vérificateur : agent Claude indépendant, qui n'a pas rédigé les fiches. Date : 19/11/2026.
Méthode : WebFetch de chaque URL de `A7-fiches.yaml` ; curl direct refusé par le proxy (403), donc aucune lecture du PDF brut. WebFetch passe par un modèle de résumé : les citations ci-dessous sont celles qu'il a renvoyées, ce n'est pas une lecture visuelle des pages.

## Version lue

- **Insee** : deux versions servies le même jour.
  - `https://www.insee.fr/fr/statistiques/8324486` (URL de la fiche) : version **antérieure** à l'erratum, sans mention d'erratum (services 5 601 / 4 323 ; mélange 29 % dans les services, 17 % au total ; figure 3 mélange 14 / 23 / 30 / 33).
  - `https://www.insee.fr/fr/statistiques/8324486?sommaire=8324486` : version **corrigée**, avec l'erratum : « Le 3 novembre 2026, plusieurs valeurs ont été modifiées dans les trois premières figures de cette publication ». Les verdicts ci-dessous portent sur cette version.
- **ADEME/RDC** : PDF lu par WebFetch, premiers 100 000 caractères sur 370 440 (pp. 1 à 32 environ). La mention « 162 pages » est lue dans le bloc de citation.
- **PRPGD IDF** : PDF lu par WebFetch, premiers 100 000 caractères sur 412 267. Couverture : « CCES du 28 novembre 2023 ».

## Tableau

| Fiche | Chiffre | Verdict | Citation courte | Page |
|---|---|---|---|---|
| INSEE | Industrie 14 891 kt | CONFORME | Fig. 1 « Ensemble hors minéraux et boues » 14 891 / 100 | fig. 1 |
| INSEE | Industrie banals 11 671 (78 %) | CONFORME | « Déchets banals 11 671 / 78 » | fig. 1 |
| INSEE | Industrie organiques 3 147 | CONFORME | « Déchets organiques 3 147 / 21 » | fig. 1 |
| INSEE | Commerce 5 649 | CONFORME | Ensemble 5 649 / 100 | fig. 1 |
| INSEE | Commerce banals 4 856 (86 %) | CONFORME | « Déchets banals 4 856 / 86 » | fig. 1 |
| INSEE | Services 5 405 | CONFORME (version corrigée) | Ensemble 5 405 / 100 (5 601 avant erratum) | fig. 1 |
| INSEE | Services banals 4 127 (76 %) | CONFORME (version corrigée) | « Déchets banals : 4 127 / 76 % » (4 323 / 77 avant) | fig. 1 |
| INSEE | Services organiques 913 | CONFORME | « Déchets organiques : 913 / 17 % » | fig. 1 |
| INSEE | En mélange 9 / 24 / 26 / 16 % | CONFORME (version corrigée) | Industrie 9, Commerce 24, Services 26, Ensemble 16 (avant : 29 et 17) | fig. 2 |
| INSEE | Papier-carton 17 / 46 / 49 / 30 | CONFORME (version corrigée) | 17, 46, 49, 30 (services 47 avant erratum) | fig. 2 |
| INSEE | Bois 39 / 13 / 14 / 28 | CONFORME (version corrigée) | 39, 13, 14, 28 (services 13 avant erratum) | fig. 2 |
| INSEE | Plastiques 4 / 6 / 5 / 5 | CONFORME | 4, 6, 5, 5 | fig. 2 |
| INSEE | Mélange : 15 / 19 / 32 / 34 % | CONFORME (version corrigée) | « recyclage 15 ; valorisation énergétique 19 ; non valorisés 32 ; centre de tri 34 » (avant : 14/23/30/33) | fig. 3 |
| INSEE | 34 % des mélanges valorisés | CONFORME | « sont deux fois moins souvent valorisés (34 %). » | texte |
| INSEE | 32 % non valorisés | CONFORME (version corrigée) | « tandis que 32 % sont incinérés sans récupération d'énergie ou mis en décharge » | texte |
| INSEE | 79 % des triés valorisés | CONFORME | « tous secteurs confondus, 79 % des déchets triés sont valorisés » | texte |
| INSEE | 19 % des triés en centre de tri | CONFORME | « 19 % sont envoyés en centre de tri » ; fig. 3 triés 67/11/2/19 | texte, fig. 3 |
| INSEE | IAA 30 % | CONFORME | « Dans l'industrie agroalimentaire (IAA), qui génère 30 % des quantités de déchets non dangereux » | texte |
| INSEE | IAA 71 % organiques | CONFORME | « majoritairement des déchets organiques (71 %) » | texte |
| INSEE | Champ 10 / 20 salariés | CONFORME | « 10 salariés ou plus de l'industrie manufacturière » ; « 20 salariés ou plus du tertiaire » | texte |
| ADEME | 57 Mt DAE | CONFORME | « production de déchets d'activités économiques de 2021 était de 57 millions de tonnes » | p. 7 |
| ADEME | 7 Mt assimilés | CONFORME | « 57 millions de tonnes et 7 millions de tonnes de déchets assimilés en 2020 » | résumé (non numéroté) |
| ADEME | Année 2021 / 2020 | CONFORME (contradiction interne déjà signalée par la fiche) | résumé « en 2020 » ; p. 7 « de 2021 » | résumé, p. 7 |
| ADEME | 64 Mt | ABSENT (somme 57 + 7, non lue telle quelle) | n/a | n/a |
| ADEME | 18 sites | CONFORME | « effectuée sur un panel de 18 sites » | p. 15, p. 21 |
| ADEME | 8 engins / 10 mécanisés | CONTRADICTION DANS LA SOURCE | Texte : « 8 sites effectuant un tri mécanique (E) et 10 un tri mécanisé (M) » ; tableau 8 : total M 8, E 10 | p. 21 |
| ADEME | 52 % mélange / 48 % monoflux | CONFORME | « 52% de flux en mélange pour 48% de monoflux » | p. 24 |
| ADEME | 68 % mélange (mécanisés) | CONFORME | « mécanisés : 1/3 de monoflux pour 2/3 de flux en mélange » ; étiquette 68 % | p. 24, fig. 6 |
| ADEME | 33 % mélange (engins) | CONFORME | « engins : 2/3 de monoflux pour 1/3 de flux en mélange » ; étiquette 33 % | p. 24, fig. 6 |
| ADEME | Bois 28 % (3/4 bois B) | CONFORME | « Le bois (28%), dont les 3/4 correspondent à du bois B » | p. 30, fig. 14 |
| ADEME | Inertes 19 % | CONFORME | « Les inertes (19%) » | p. 30 |
| ADEME | Fines 34 % | CONFORME | « 34% d'éléments fins ou non reconnaissables » | p. 30 |
| ADEME | Fibreux 7, plastiques 5, métaux 3, textiles 3, plâtre 1 | CONFORME | « fibreux – 7% ; plastiques – 5% ; métaux – 3% ; textiles – 3% ; plâtre – 1% » | p. 30 |
| ADEME | Refus environ 200 €/t TGAP comprise | CONFORME | « environ 200 €/tonne de refus produite, TGAP comprise » | p. 32 |
| ADEME | CA environ 150 €/t | CONFORME | « chiffre d'affaires aux alentours de 150 €/ tonne » | p. 32 |
| ADEME | Fourchette 70-80 à plus de 200 €/t | CONFORME | « fourchette basse à 70-80 €/ tonne » ; « fourchette haute supérieure à 200 €/ tonne » | p. 32 |
| ADEME | 162 p. | CONFORME | « 162 pages. » (bloc de citation) | avant sommaire |
| PRPGD | 5,09 Mt en 2020 | CONFORME | « 5,09 millions de tonnes de déchets d'activités économiques (DAE) non dangereux non inertes produits en 2020 » | p. 10 |
| PRPGD | Série 5,90 / 5,95 / 5,63 / 5,09 | CONFORME | « Total DAE (hors déchets inertes et SPGD) 5,90 Mt 5,95 Mt 5,63 Mt 5,09 Mt » | p. 42 |
| PRPGD | Objectif 5,87 Mt (2031) | CONFORME | « > 2031 : 5,87 Mt, soit 869 kg/emploi » | p. 14 |
| PRPGD | 100 % des DAE en mélange vers le tri en 2025 | CONFORME | « 100 % des DAE collectés en mélange orientés vers une chaîne de tri en 2025 » | p. 16 |
| PRPGD | Date 28/11/2023 | CONFORME | « CCES du 28 novembre 2023 » | couverture |

Les numéros de page du PRPGD et de l'ADEME sont ceux renvoyés par WebFetch, qui les déduit du texte extrait : à confirmer dans le PDF.

## Écarts et points à signaler

1. **Insee, URL de la fiche** : `https://www.insee.fr/fr/statistiques/8324486` sert encore la version d'avant l'erratum (sans mention d'erratum). La version corrigée s'obtient avec `?sommaire=8324486`. Toutes les valeurs de la fiche correspondent à la version corrigée. Avec l'ancienne version, sept valeurs diffèrent : services 5 601 et 4 323 (77 %) ; mélange services 29 % et ensemble 17 % ; papier-carton services 47 ; bois services 13 ; figure 3 mélange 14 / 23 / 30 / 33 ; texte « 30 % sont incinérés ». Suggestion : noter dans la fiche que la version corrigée est servie par l'URL avec `?sommaire=8324486` (ou indiquer comment lire la version corrigée).
2. **ADEME, répartition des 18 sites (règle 13)** : la source se contredit. Le texte p. 21 dit « 8 sites effectuant un tri mécanique (E) et 10 un tri mécanisé (M) ». Le tableau 8 de la même page donne 8 M et 10 E. Le libellé « mécanique (E) » est lui-même incohérent avec les définitions p. 20 (E = engins, M = mécanisés). La fiche reprend la version du texte (8 engins, 10 mécanisés) sans signaler le tableau. Je ne sais pas laquelle est juste ; à trancher par Stéphane sur le PDF, puis à présenter dans la fiche.
3. **ADEME, 64 Mt** : ce total ne figure pas dans la source lue ; c'est la somme 57 + 7. Il devrait être un CALCULÉ, pas un contenu de la source.
4. **ADEME, « résumé p. 5 »** : WebFetch donne le résumé sans numéro de page ; la p. 5 n'est pas confirmée.
5. **PRPGD** : la fiche dit « hors BTP gérés par le service public » ; la source p. 42 dit « hors déchets inertes et SPGD ». Ce n'est pas un chiffre, mais la formulation est à aligner sur la source. Les mentions « 2020 atypique, confinements » et « pas de tonnage des DAE en mélange » n'ont pas été contrôlées (hors des questions posées ; la deuxième ne peut pas être prouvée sur une lecture partielle).
6. **Limites** : PDF lus seulement sur les premiers 100 000 caractères ; WebFetch passe par un modèle de résumé (risque d'erreur de transcription). Pages à confirmer visuellement par Stéphane : ADEME p. 21 (tableau 8), p. 24 (fig. 6), p. 30 (fig. 14) ; Insee figures 2 et 3 de la version corrigée.

## Compte rendu (règle 10)

| Statut | Éléments |
|---|---|
| Trouvé (CONFORME) | Insee : les 20 chiffres demandés (version corrigée) ; ADEME : 57, 7, 18, 52/48, 68/33, fig. 14 entière, 200 €/t, 150 €/t et fourchette, 162 p. ; PRPGD : 5,09, série, 5,87, 100 % 2025, date |
| Partiel | ADEME 8 engins / 10 mécanisés (contradiction texte / tableau 8) ; Insee (deux versions selon l'URL) ; pages ADEME et PRPGD déduites par WebFetch |
| Non trouvé | ADEME 64 Mt (somme, absente telle quelle) |
| Non ouvert | Aucun (curl direct bloqué ; WebFetch a ouvert les trois URL) |
