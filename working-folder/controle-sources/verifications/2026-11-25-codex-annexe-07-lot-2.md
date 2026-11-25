# Contre-verification de l'annexe 7, lot 2

Date : 2026-11-25  
Agent : codex  
Document de reference : `nouveau-business-plan/annexes/annexe-07-html/index.html`  
Perimetre : Key Messages et sections 7.4 a 7.9  
Acces internet : OUI  
Lecture des PDF en ligne : OUI

## Sources effectivement ouvertes

- ADEME, rapport final sur les installations de tri des DAE, novembre 2025 : https://www.rdcenvironment.be/wp-content/uploads/2026/01/performance-tri-DAE-rapport-1.pdf
- Institut Paris Region et ORDIF, rapport de suivi n° 3 du PRPGD d'Ile-de-France : https://www.institutparisregion.fr/fileadmin/DataStorage/user_upload/Rapport-de-suivi-PRPGD_2023.pdf
- Region Ile-de-France et ADEME Ile-de-France, *Economie circulaire et plastique en Ile-de-France*, 2023 : https://www.iledefrance.fr/sites/default/files/2023-11/Livret-zero-plastique_ADEME-Region-Ile-de-France.pdf
- Dossier public de demande d'autorisation de la chaufferie CSR de Neuvillette et Thenelles, 2021 : https://www.aisne.gouv.fr/contenu/telechargement/35465/227231/file/10%20-%20E3790P02T01_SUEZ_CH-CSR_DDAE_E7.5_EDD_E-annexes.pdf
- Fiches de preuve des annexes 2, 5 et 8 pour les valeurs reprises, puis registres de calculs et de decisions du projet.

Les donnees Insee, PRPGD et de composition deja contre-verifiees dans le lot 1 ne sont pas recomptees ici, sauf lorsque la section 7.8 repete l'affirmation erronee sur l'absence de tonnage regional en melange.

## Tableau des verdicts

| N° | Section ou fiche | Affirmation courte | Valeur annoncee | Source citee | Verdict | Citation exacte | Emplacement reel | Commentaire |
|---:|---|---|---:|---|---|---|---|---|
| 1 | 7.4, D-049 | Le bilan est une hypothese sur masse brute, humidite inconnue | hypothese de travail | D-049 | CONFIRMÉ | « rendements appliques a la masse brute, l'humidite n'etant pas connue [...] Les elements fins ou non reconnaissables (34 %) ne sont pas attribues faute de composition. » | `_decisions.yaml`, D-049 | Etiquetage clair. Hypothese utile pour explorer, trop optimiste pour dimensionner. |
| 2 | CALC-A7-HUILE-BAS-KG-T | Huile, scenario bas | 27,5 kg/t | CALC-A7-HUILE-BAS-KG-T | CONFIRMÉ | « Le bois (28%) [...] plastiques - 5% » | ADEME, figure 14, p. 30 ; calculs.yaml | 1 000 x 5 % x 55 % = 27,5 kg. |
| 3 | CALC-A7-HUILE-CENT-KG-T | Huile, scenario standard | 36,5 kg/t | CALC-A7-HUILE-CENT-KG-T | CONFIRMÉ | « formule: p * r / 10 [...] resultat: 36.535 » | calculs.yaml, CALC-A7-HUILE-CENT-KG-T | 1 000 x 5 % x 73,07 % = 36,535 kg, correctement arrondi a 36,5. |
| 4 | CALC-A7-HUILE-HAUT-KG-T | Huile, scenario haut | 40,5 kg/t | CALC-A7-HUILE-HAUT-KG-T | CONFIRMÉ | « formule: p * r / 10 [...] resultat: 40.5 » | calculs.yaml, CALC-A7-HUILE-HAUT-KG-T | 1 000 x 5 % x 81 % = 40,5 kg. |
| 5 | CALC-A7-GAZ-PLAST-KG-T | Gaz issu des plastiques | 5,0 kg/t | CALC-A7-GAZ-PLAST-KG-T | CONFIRMÉ | « gaz issu du plastique = 10 % de la masse de plastique entrante (HYPOTHESE) » | `_decisions.yaml`, D-029 | 1 000 x 5 % x 10 % = 5,0 kg. |
| 6 | CALC-A7-CHAR-BAS-KG-T | Char, scenario bas | 95 kg/t | CALC-A7-CHAR-BAS-KG-T | CONFIRMÉ | « char = 30 % de la matiere seche des fractions organiques non plastiques ; bas 25 %, haut 40 % » | `_decisions.yaml`, D-045 | 1 000 x 38 % x 25 % = 95 kg. |
| 7 | CALC-A7-CHAR-CENT-KG-T | Char, scenario standard | 114 kg/t | CALC-A7-CHAR-CENT-KG-T | CONFIRMÉ | « formule: o * c / 10 [...] resultat: 114.0 » | calculs.yaml, CALC-A7-CHAR-CENT-KG-T | 1 000 x 38 % x 30 % = 114 kg. |
| 8 | CALC-A7-CHAR-HAUT-KG-T | Char, scenario haut | 152 kg/t | CALC-A7-CHAR-HAUT-KG-T | CONFIRMÉ | « formule: o * c / 10 [...] resultat: 152.0 » | calculs.yaml, CALC-A7-CHAR-HAUT-KG-T | 1 000 x 38 % x 40 % = 152 kg. |
| 9 | CALC-A7-LIQ-BAS-KG-T | Liquide oxygene, scenario bas | 20,0 kg/t | CALC-A7-LIQ-BAS-KG-T | CONFIRMÉ | « Waste paper and textile wastes exhibit relatively lower pyrolysis oil yields (20-25 wt%) » | Bhatt et al., resume et section 3.3 | 1 000 x (7 % + 3 %) x 20 % = 20 kg. |
| 10 | CALC-A7-LIQ-CENT-KG-T | Liquide oxygene, scenario standard | 22,5 kg/t | CALC-A7-LIQ-CENT-KG-T | CONFIRMÉ | « reste des textiles sanitaires et textiles : liquide oxygene 20 / 22,5 / 25 % » | `_decisions.yaml`, D-048 | 1 000 x 10 % x 22,5 % = 22,5 kg. |
| 11 | CALC-A7-LIQ-HAUT-KG-T | Liquide oxygene, scenario haut | 25,0 kg/t | CALC-A7-LIQ-HAUT-KG-T | CONFIRMÉ | « Waste paper and textile wastes exhibit relatively lower pyrolysis oil yields (20-25 wt%) » | Bhatt et al., resume et section 3.3 | 1 000 x 10 % x 25 % = 25 kg. |
| 12 | CALC-A7-GAZ-ST-BAS-KG-T | Gaz fibreux et textiles, scenario bas | 45,0 kg/t | CALC-A7-GAZ-ST-BAS-KG-T | CONFIRMÉ | « The gas yield for these materials remains comparatively high (45-48 wt%) » | Bhatt et al., resume et section 3.3 | 1 000 x 10 % x 45 % = 45 kg. |
| 13 | CALC-A7-GAZ-ST-CENT-KG-T | Gaz fibreux et textiles, scenario standard | 46,5 kg/t | CALC-A7-GAZ-ST-CENT-KG-T | CONFIRMÉ | « reste des textiles sanitaires et textiles : [...] gaz 45 / 46,5 / 48 % » | `_decisions.yaml`, D-048 | 1 000 x 10 % x 46,5 % = 46,5 kg. |
| 14 | CALC-A7-GAZ-ST-HAUT-KG-T | Gaz fibreux et textiles, scenario haut | 48,0 kg/t | CALC-A7-GAZ-ST-HAUT-KG-T | CONFIRMÉ | « The gas yield for these materials remains comparatively high (45-48 wt%) » | Bhatt et al., resume et section 3.3 | 1 000 x 10 % x 48 % = 48 kg. |
| 15 | 7.4, coherence du scenario haut | Produits issus de 100 kg de fibreux et textiles | 40 kg char + 25 kg liquide + 48 kg gaz | D-045 et D-048 | CALCUL FAUX | « char selon D-045 » et « liquide 20 / 22,5 / 25 % et gaz 45 / 46,5 / 48 % » | `_decisions.yaml`, D-048 et D-049 | 40 + 25 + 48 = 113 kg pour 100 kg entrants. Les hypotheses independantes ne peuvent pas etre combinees ainsi dans le scenario haut. |
| 16 | 7.4, fermeture d'une tonne | Masse non affectee apres fines | bas 237,5 kg ; standard 205,465 kg ; haut 159,5 kg | tableau 7.4 | ABSENT | « Fines, water, gas and liquid from wood | Not allocated: no measurement on this feed » | HTML, section 7.4 | Les categories manquantes sont nommees, mais les 340 kg de fines et les masses residuelles ne sont pas affichees. Le titre « mass balance per tonne » est donc trompeur. |
| 17 | 7.4, energie | Besoin du bruleur | 1 507 MJ/t | CALC-A2-BRULEUR-MJ-T | CONFIRMÉ | « Burner rating 833 kcal/s, operated 24 hours a day, divided by 200 t/day » | annexe 2, fiche 2.5.d.1 | 833 x 86 400 x 4,1868 / 1 000 / 200 = 1 506,65 MJ/t. `nature: constructeur`. |
| 18 | 7.4, energie | Le gaz plastique seul est tres inferieur au besoin | 5 kg/t, soit 186,93 MJ/t | CALC-A7-GAZ-PLAST-KG-T et CALC-A2-GAZ-PCI-MJ-KG | CONFIRMÉ | « resultat: 37.386 MJ/kg » et « resultat: 5.0 kg par tonne » | calculs.yaml | 5 x 37,386 = 186,93 MJ/t, soit 12,4 % du besoin de 1 506,65 MJ/t. Cela ne permet pas de conclure sur le gaz du bois et des fibreux, dont l'energie est inconnue. |
| 19 | 7.4 et 7.8 | Une valeur publique generique permet de fermer le bilan du DAE brut en melange | aucune trouvee | R-048 | ABSENT | « La precision des identifications visuelles reste approximative par rapport a des caracterisations effectuees en bonne et due forme » | ADEME 2025, p. 28 ; recherche publique complementaire | Aucune valeur representative du flux brut de l'annexe n'a ete trouvee. Humidite et PCI doivent etre mesures sur le flux contractualise. |
| 20 | 7.4, autre source publique | Caracteristiques d'un CSR prepare a partir notamment de DAE et refus | PCI 12-18 MJ/kg ; humidite 15-25 % | dossier public chaufferie CSR | CONFIRMÉ | « PCI brut : 12-18 MJ/kg ; Humidite sur brut : 15-25% en masse ; Teneur en cendres : 10-20% en masse. » | dossier Neuvillette et Thenelles, p. 51/228 | C'est une specification de CSR prepare, pas une mesure du DAE brut de l'annexe. Elle ne permet pas de fermer le bilan Urban Rig. |
| 21 | 7.5 et Key Messages | Cout de traitement des refus | environ 200 EUR/t, TGAP comprise | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « le cout de traitement moyen des refus mesure est d'environ 200 €/tonne de refus produite, TGAP comprise » | ADEME 2025, p. 32 imprimee | Ordre de grandeur confirme. Ce n'est pas automatiquement un prix d'entree capturable par Urban Rig. |
| 22 | 7.5 | Chiffre d'affaires moyen des centres audites | environ 150 EUR/t, bas 70-80, haut plus de 200 | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « En moyenne, les sites ont un chiffre d'affaires aux alentours de 150 €/ tonne, avec une fourchette basse a 70-80 €/ tonne et une fourchette haute superieure a 200 €/ tonne. » | ADEME 2025, p. 32 imprimee | Il s'agit du chiffre d'affaires des centres, pas d'un gate fee Urban Rig. |
| 23 | 7.6 | Part de flux en melange selon le type de centre | 68 % mecanises ; 33 % engins | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « Centres de tri mecanises : 1/3 de monoflux pour 2/3 de flux en melange ; Centres de tri engins : 2/3 de monoflux pour 1/3 de flux en melange. » | ADEME 2025, p. 24, figure 6 | Les valeurs de la figure sont 68 % et 33 %. La variabilite est correctement signalee. |
| 24 | 7.8 | Aucun tonnage regional en melange n'est publie | aucun | R-048 | DIFFÉRENT | « Total DAE franciliens en melange [...] 2020 2,77 Mt » | PRPGD suivi 3, p. 82 | Ecart deja etabli au lot 1. La ligne R-048 est obsolete. 51 100 t/an representent environ 1,84 % de ce minimum. |
| 25 | Key Messages | Dechets plastiques d'activite economique franciliens | 260 000 t/an | A8-PRO-IDF-LIVRET-2023 | CONFIRMÉ | « Sur l'ensemble des 260 000 tonnes par an de dechets d'activite economique » | livret regional, p. 41 | Le texte parle des dechets plastiques d'activite economique. |
| 26 | Key Messages | Commerce et films etirables | commerce 34 %, dont la moitie en films pour palettes | A8-PRO-IDF-LIVRET-2023 | CONFIRMÉ | « pres du tiers (34 %) du commerce (la moitie est constituee de films etirables pour palettes) » | livret regional, p. 41 | Conforme. Le tonnage de films n'est pas mesure separement dans la source. |
| 27 | Key Messages | Le char est le produit principal en masse | 95 a 152 kg/t | CALC-A7-CHAR-* | CONFIRMÉ | « formule: o * c / 10 » | calculs.yaml, trois calculs char | Dans les hypotheses retenues, le char depasse chaque autre produit chiffre. Sa qualite commerciale n'est pas demontree. |
| 28 | 7.5 | Aucun prix d'entree DAE par defaut n'est decide | aucun | texte et decisions | CONFIRMÉ | « No default entry price is decided for mixed business waste. » | HTML, section 7.5 | Etiquetage prudent et conforme a la consigne. Un contrat ou une lettre d'intention reste necessaire. |

## Recalculs demandes

| Calcul | Recalcul independant | Verdict |
|---|---:|---|
| CALC-A7-HUILE-BAS-KG-T | 50 x 55 % = 27,5 kg | CONFIRMÉ |
| CALC-A7-HUILE-CENT-KG-T | 50 x 73,07 % = 36,535 kg | CONFIRMÉ |
| CALC-A7-HUILE-HAUT-KG-T | 50 x 81 % = 40,5 kg | CONFIRMÉ |
| CALC-A7-GAZ-PLAST-KG-T | 50 x 10 % = 5,0 kg | CONFIRMÉ |
| CALC-A7-CHAR-BAS-KG-T | 380 x 25 % = 95 kg | CONFIRMÉ |
| CALC-A7-CHAR-CENT-KG-T | 380 x 30 % = 114 kg | CONFIRMÉ |
| CALC-A7-CHAR-HAUT-KG-T | 380 x 40 % = 152 kg | CONFIRMÉ |
| CALC-A7-LIQ-BAS-KG-T | 100 x 20 % = 20 kg | CONFIRMÉ |
| CALC-A7-LIQ-CENT-KG-T | 100 x 22,5 % = 22,5 kg | CONFIRMÉ |
| CALC-A7-LIQ-HAUT-KG-T | 100 x 25 % = 25 kg | CONFIRMÉ |
| CALC-A7-GAZ-ST-BAS-KG-T | 100 x 45 % = 45 kg | CONFIRMÉ |
| CALC-A7-GAZ-ST-CENT-KG-T | 100 x 46,5 % = 46,5 kg | CONFIRMÉ |
| CALC-A7-GAZ-ST-HAUT-KG-T | 100 x 48 % = 48 kg | CONFIRMÉ |

Toutes les formules CALC-A7 demandees sont arithmetiquement justes. Le probleme apparait lorsqu'on additionne les rendements independants pour construire un bilan matiere unique.

### Fermeture de la tonne

| Scenario | Produits chiffres + 230 kg non convertis | + 340 kg de fines non attribuees | Reste non affecte pour atteindre 1 000 kg |
|---|---:|---:|---:|
| Bas | 422,5 kg | 762,5 kg | 237,5 kg |
| Standard | 454,535 kg | 794,535 kg | 205,465 kg |
| Haut | 500,5 kg | 840,5 kg | 159,5 kg |

Le reste se decompose en masse de plastique non attribuee, gaz et liquide du bois, eau et autres produits ou pertes. Pour les seuls 100 kg de fibreux et textiles, les trois jeux donnent 90 kg, 99 kg et 113 kg. Le scenario standard est proche d'une fermeture locale, le scenario haut est physiquement impossible tel qu'additionne.

## Appreciation legere des hypotheses, sans les remplacer

| Hypothese | Etiquette | Appreciation dans un cas standard |
|---|---|---|
| D-049, composition moyenne des 18 sites appliquee a une tonne | HYPOTHESE explicite | Raisonnable pour un ordre de grandeur exploratoire. Trop optimiste pour dimensionner, car la composition visuelle n'est pas une specification contractuelle. |
| D-049, rendements appliques a la masse brute | HYPOTHESE explicite | Optimiste, ce que le texte reconnait. L'eau est comptee comme si elle pouvait produire huile, gaz ou char. |
| D-044 et D-029, plastique | HYPOTHESE explicite | Le scenario standard est optimiste pour un plastique sale et humide ; le bas est plus prudent. |
| D-045, char bois, fibreux et textiles | HYPOTHESE explicite | 25 a 30 % est un ordre de grandeur plausible de litterature ; 40 % est optimiste et ne peut pas etre combine avec les maxima liquide et gaz. |
| D-048, liquide et gaz des fibreux et textiles | HYPOTHESE explicite | Bas et standard sont plausibles comme sensibilites. Le triplet haut totalise 113 % avec le char et doit etre corrige. |
| Inertes, metaux et platre inchanges | HYPOTHESE explicite | Raisonnable pour un bilan conservateur, a condition d'afficher 230 kg de residus a gerer par tonne. |
| Fines non attribuees | HYPOTHESE explicite | Prudente, mais elle bloque toute fermeture matiere et energie puisque 340 kg/t restent inconnus. |
| D-047, trois scenarios | HYPOTHESE explicite | Bonne pratique de sensibilite, mais les rendements doivent provenir de jeux coherents qui ferment chacun la masse. |
| D-035, 140 t/jour | HYPOTHESE explicite | Acceptable comme parametre de modele modifiable. Ce n'est pas une preuve de debit sur DAE heterogene. |
| Aucun prix DAE par defaut | Explicitement non decide | Prudent. Les 200 EUR/t sont un cout actuel des refus, pas une recette Urban Rig acquise. |

## Ecarts

### E-1 : le scenario haut depasse 100 % sur les fibreux et textiles

- Annexe : 40 % de char, 25 % de liquide et 48 % de gaz.
- Recalcul : 113 kg de produits pour 100 kg entrants.
- Gravite : IMPORTANT.
- Effet projet : le scenario optimiste surestime directement les produits et toute recette associee. Le scenario standard totalise 99 % sur cette fraction et reste coherent en ordre de grandeur.
- Correction proposee : construire trois jeux de rendements massiques coherents qui totalisent au plus 100 % pour chaque matiere, avec une ligne eau et pertes.

### E-2 : le « bilan d'une tonne » ne ferme pas la tonne

- Annexe : les categories non attribuees sont nommees, sans masse.
- Recalcul standard : 454,535 kg de produits et residus chiffres, plus 340 kg de fines, soit 794,535 kg ; il manque 205,465 kg.
- Gravite : IMPORTANT.
- Effet projet : le rendement total, les residus a evacuer et les recettes ne peuvent pas etre lus comme un bilan complet.
- Correction proposee : afficher pour chaque scenario les 340 kg de fines, la masse non attribuee du plastique, le gaz et le liquide du bois, l'eau et une ligne de fermeture a 1 000 kg.

### E-3 : le point ouvert R-048 nie un tonnage regional publie

- Annexe : « No regional tonnage of mixed business waste is published ».
- Source : 2,77 Mt en 2020, minimum regional.
- Gravite : IMPORTANT.
- Effet projet : 51 100 t/an representent environ 1,84 % de ce minimum. La correction renforce la plausibilite d'approvisionnement mais ne prouve pas l'accessibilite contractuelle.
- Correction proposee : reprendre 2,77 Mt comme minimum publie et retirer le tonnage regional de R-048.

### E-4 : les 200 EUR/t peuvent etre lus comme une recette disponible

- Annexe : recommande de preferer les refus, « paid about 200 EUR/t ».
- Source : mesure le cout moyen actuel de traitement des refus supporte par les centres, TGAP comprise.
- Gravite : IMPORTANT pour le modele economique, pas pour la faisabilite technique.
- Effet projet : ce cout evite ne devient un gate fee Urban Rig qu'apres negociation, prise en compte du transport, de la conformite et des solutions concurrentes.
- Correction proposee : ecrire « repere de cout d'elimination, non prix d'entree acquis » et exiger une offre ou lettre d'intention.

### E-5 : la formulation energetique est juste mais incomplete

- Annexe : 5 kg de gaz plastique sont tres inferieurs au besoin du bruleur et le bilan complet est impossible sans humidite ni PCI.
- Recalcul : 186,93 MJ/t, soit 12,4 % des 1 506,65 MJ/t.
- Gravite : MINEUR pour la phrase, BLOQUANT pour toute conclusion d'autosuffisance.
- Correction proposee : afficher le calcul en MJ/t et preciser que l'energie du gaz du bois, des fibreux et des fines reste inconnue.

## Points manquants pour juger la faisabilite DAE

| Point | Classement | Conclusion pratique |
|---|---|---|
| Bois traite, environ 21 % du flux selon l'hypothese de composition | BLOQUANT avant acceptation directe | POSSIBLE SOUS CONDITIONS : definir les bois acceptes, analyser les contaminants et faire un essai Urban Rig representatif. |
| Chlore dans l'alimentation, le gaz, l'huile et le char | BLOQUANT avant engagement | DONNEE A MESURER : le flux peut etre techniquement possible, mais aucune conclusion de conformite, corrosion ou qualite produit n'est possible sans analyse. |
| Platre et soufre | IMPORTANT | 10 kg/t de platre sont chiffres dans la composition, mais le devenir du soufre et le risque de gaz acides ne sont pas documentes. Pre-tri et mesure necessaires. |
| Inertes et metaux | IMPORTANT | 230 kg/t sont non convertis. Ils reduisent le debit utile et creent un residu a extraire et evacuer ; le pre-tri doit etre dimensionne. |
| Variabilite entre bennes et dans le temps | IMPORTANT | Le rapport ADEME la confirme. Un contrat doit imposer une specification, un plan d'echantillonnage et des criteres de refus. |
| Fines, 340 kg/t | BLOQUANT pour les bilans matiere et energie | Leur composition, humidite, cendres, chlore et PCI peuvent changer le resultat dans les deux sens. Elles doivent etre caracterisees ou retirees avant modelisation. |

Ces blocages portent sur la qualification technique du flux, pas sur l'existence du gisement. Une machine traite environ 51 100 t/an, soit environ 1 % des 5,09 Mt de DAE non dangereux non inertes franciliens et environ 1,84 % du minimum publie de DAE en melange.

## Autres interpretations

1. Le scenario standard est le plus defensable des trois pour les fibreux et textiles, car ses rendements additionnes donnent 99 %. Cela ne valide pas l'ensemble du bilan : 205,465 kg/t restent non affectes apres ajout des fines.
2. Les fines ne sont pas necessairement des inertes. Elles peuvent contenir de l'eau, des combustibles et des cendres. Les traiter comme inconnues est prudent ; les oublier dans l'affichage des sorties ne l'est pas.
3. Une source publique donne 12 a 18 MJ/kg et 15 a 25 % d'humidite pour un CSR prepare a partir notamment de DAE et refus de tri. Cette plage montre qu'un combustible prepare peut etre energetiquement interessant, mais elle ne peut pas etre transposee au DAE brut de l'annexe.
4. Les 200 EUR/t de refus representent la solution actuelle de traitement. Urban Rig ne peut en capter qu'une partie eventuelle, selon le transport, le pre-tri, les garanties de destruction et la concurrence des UVE, CSR et ISDND.
5. Les refus de tri peuvent etre plus accessibles et plus homogenes que le DAE brut, mais leur composition n'est pas celle de la figure 14. Changer de flux impose une nouvelle caracterisation et rend D-049 inapplicable sans essai.
6. Le char est bien le premier produit chiffre en masse. Avec environ 21 % de bois B dans le flux theorique, « produit principal » ne signifie toutefois ni produit commercialisable, ni sortie du statut de dechet, ni conformite a un usage.
7. Les 260 000 t/an de plastiques professionnels franciliens indiquent une piste alternative mieux orientee vers l'huile. La source les decrit comme diffuses et ne demontre ni disponibilite contractuelle ni prix.
8. L'approvisionnement d'une seule machine n'est pas le point faible : 51 100 t/an restent petits devant les millions de tonnes regionaux. La vraie condition est une qualite contractuelle stable et compatible avec le procede.

## Cinq erreurs ou risques les plus graves

1. Le scenario haut produit 113 kg a partir de 100 kg de fibreux et textiles.
2. Le bilan standard laisse 205,465 kg/t non affectes apres avoir compte les fines.
3. Les fines, le chlore et le bois B ne sont pas caracterises alors qu'ils peuvent changer le bilan et la qualite des produits.
4. Le point R-048 reste faux sur le tonnage regional en melange de 2,77 Mt.
5. Le cout de 200 EUR/t des refus pourrait etre confondu avec une recette Urban Rig acquise.

## Conclusion en langage simple

PASSE : tous les calculs CALC-A7-HUILE-*, GAZ-*, CHAR-* et LIQ-* sont arithmetiquement corrects. Le scenario standard donne bien 36,535 kg d'huile, 5 kg de gaz plastique, 114 kg de char, 22,5 kg de liquide oxygene et 46,5 kg de gaz fibreux/textiles. Les ordres de grandeur ADEME sur les refus et la variabilite sont correctement repris.

NE PASSE PAS : appeler le tableau un bilan massique complet d'une tonne, et utiliser le scenario haut tel quel. La tonne ne ferme pas et le sous-bilan fibreux/textiles du scenario haut atteint 113 %.

POSSIBLE SOUS CONDITIONS : un DAE ou un refus de tri caracterise, pretrie et contractualise peut rester une alimentation possible. Le scenario standard est utilisable comme sensibilite preliminaire, pas comme garantie de rendement.

A MESURER AVANT CONCLUSION : humidite, PCI, chlore, soufre, cendres, metaux, composition des fines, variabilite et rendement d'un essai representatif. Sans ces donnees, aucune autosuffisance energetique ni qualite commerciale du char ne peut etre affirmee.

Verdict global du lot 2 : PASSE SOUS CONDITIONS. Aucun blocage de gisement a l'echelle de 51 100 t/an. Les conditions bloquantes avant engagement sont la caracterisation du flux et un bilan matiere et energie ferme. Le scenario haut doit etre corrige ; le scenario standard reste un ordre de grandeur plausible mais incomplet.

## Ce qui n'a pas ete verifie dans ce lot

- Prix de 120 EUR/t en incineration et taxes : exclus du controle chiffre par les regles legeres ; a confirmer par offre ou contrat selon le site et l'annee.
- Prix d'entree reel Urban Rig : aucun prix par defaut n'est decide ; a confirmer par lettre d'intention ou contrat.
- Debit reel de 140 t/jour sur DAE heterogene : D-035 est une hypothese de modele, pas un essai sur ce flux.
- Qualite, statut reglementaire et debouche du char de bois B : aucune analyse du produit cible n'est fournie.
- Humidite et PCI du flux contractuel : aucune campagne representative n'est fournie. La specification publique de CSR prepare ne s'y substitue pas.

## Verification HTML contre source Markdown

Les Key Messages et sections 7.4 a 7.9 du HTML portent les memes valeurs et affirmations que la source Markdown. Aucun ecart HTML / source n'a ete trouve.

## Decompte

- CONFIRMÉ : 24
- DIFFÉRENT : 1
- ABSENT : 2
- NON SOURCÉ : 0
- INACCESSIBLE : 0
- CALCUL FAUX : 1
- Total : 28 verdicts
