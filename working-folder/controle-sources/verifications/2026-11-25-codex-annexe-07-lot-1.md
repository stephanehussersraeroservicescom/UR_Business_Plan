# Contre-verification de l'annexe 7, lot 1

Date : 2026-11-25  
Agent : codex  
Document de reference : `nouveau-business-plan/annexes/annexe-07-html/index.html`  
Perimetre : sections 7.1 a 7.3, plus les calculs CALC-A7-MELANGE-*, CALC-A7-IDF-DAE-*, CALC-A7-NONCONV-PCT et CALC-A7-ORG-PCT  
Acces internet : OUI  
Lecture des PDF en ligne : OUI

## Sources effectivement ouvertes

- Insee Premiere n° 2034, page web corrigee apres l'erratum du 3 novembre 2026 : https://www.insee.fr/fr/statistiques/8324486
- Insee Premiere n° 2034, PDF imprimable : https://www.insee.fr/fr/statistiques/fichier/8324486/IP2034.pdf
- ADEME, rapport final sur les installations de tri des DAE, novembre 2025 : https://www.rdcenvironment.be/wp-content/uploads/2026/01/performance-tri-DAE-rapport-1.pdf
- Institut Paris Region et ORDIF, rapport de suivi n° 3 du PRPGD d'Ile-de-France : https://www.institutparisregion.fr/fileadmin/DataStorage/user_upload/Rapport-de-suivi-PRPGD_2023.pdf
- ORDIF, enfouissement des dechets non dangereux, donnees 2022-2023 : https://www.ordif.fr/fileadmin/DataStorage/user_upload/ORDIF_Notice_ISDND_2022-2023__1_.pdf
- ORDIF, incineration des dechets non dangereux, donnees 2022-2023 : https://www.institutparisregion.fr/fileadmin/DataStorage/user_upload/ORDIF_Notice_UIDND_2022-2023__janvier_2024_.pdf

Point de version Insee : le PDF imprimable contient encore les anciennes valeurs. La page web porte l'erratum et les valeurs corrigees. Pour les donnees modifiees, le present controle retient la page web officielle corrigee.

## Tableau des verdicts

| N° | Section ou fiche | Affirmation courte | Valeur annoncee | Source citee | Verdict | Citation exacte | Emplacement reel | Commentaire |
|---:|---|---|---:|---|---|---|---|---|
| 1 | 7.1 | DAE France hors construction, plus assimiles | 57 Mt + 7 Mt, 2021 | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « La production de dechets d'activites economiques de 2021 etait de 57 millions de tonnes (hors BTP et assimiles) et 7 millions de tonnes de dechets assimiles, soit 64 millions de tonnes. » | ADEME, p. 7 imprimee | La section 1.1 confirme 2021. Le resume du meme rapport indique 2020, contradiction interne mineure a signaler. |
| 2 | 7.1 | Dechets non dangereux hors mineraux et boues, industrie | 14 891 kt | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Ensemble hors mineraux et boues [...] 14 891 » | Insee, page web corrigee, figure 1 | Champ : industrie manufacturiere, etablissements de 10 salaries ou plus, 2022. |
| 3 | 7.1 | Meme perimetre, commerce | 5 649 kt | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Ensemble hors mineraux et boues [...] 5 649 » | Insee, page web corrigee, figure 1 | Etablissements de 20 salaries ou plus, 2022. |
| 4 | 7.1 | Meme perimetre, services | 5 405 kt | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Ensemble hors mineraux et boues [...] 5 405 » | Insee, page web corrigee, figure 1 | Valeur issue de l'erratum. Le PDF non corrige affiche encore 5 601 kt. |
| 5 | CALC-A7-MELANGE-IND-KT | Dechets banals de l'industrie | 11 671 kt | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Dechets banals [...] 11 671 » | Insee, page web corrigee, figure 1 | Entree du calcul. |
| 6 | CALC-A7-MELANGE-IND-KT | Part en melange, industrie | 9 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Industrie manufacturiere [...] En melange 9 » | Insee, page web corrigee, figure 2 | Part publiee arrondie a l'unite. |
| 7 | CALC-A7-MELANGE-IND-KT | Tonnage en melange, industrie | 1 050,39 kt, presente 1 050 kt | CALC-A7-MELANGE-IND-KT | CONFIRMÉ | « Dechets banals 11 671 » et « En melange 9 » | Insee, figures 1 et 2 | Recalcul : 11 671 x 9 % = 1 050,39 kt. |
| 8 | CALC-A7-MELANGE-COM-KT | Dechets banals du commerce | 4 856 kt | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Dechets banals [...] 4 856 » | Insee, page web corrigee, figure 1 | Entree du calcul. |
| 9 | CALC-A7-MELANGE-COM-KT | Part en melange, commerce | 24 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Commerce [...] En melange 24 » | Insee, page web corrigee, figure 2 | Part publiee arrondie a l'unite. |
| 10 | CALC-A7-MELANGE-COM-KT | Tonnage en melange, commerce | 1 165,44 kt, presente 1 165 kt | CALC-A7-MELANGE-COM-KT | CONFIRMÉ | « Dechets banals 4 856 » et « En melange 24 » | Insee, figures 1 et 2 | Recalcul : 4 856 x 24 % = 1 165,44 kt. |
| 11 | CALC-A7-MELANGE-SERV-KT | Dechets banals des services | 4 127 kt | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Dechets banals [...] 4 127 » | Insee, page web corrigee, figure 1 | Valeur issue de l'erratum. |
| 12 | CALC-A7-MELANGE-SERV-KT | Part en melange, services | 26 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Services [...] En melange 26 » | Insee, page web corrigee, figure 2 | Valeur issue de l'erratum, arrondie a l'unite. |
| 13 | CALC-A7-MELANGE-SERV-KT | Tonnage en melange, services | 1 073,02 kt, presente 1 073 kt | CALC-A7-MELANGE-SERV-KT | CONFIRMÉ | « Dechets banals 4 127 » et « En melange 26 » | Insee, figures 1 et 2 | Recalcul : 4 127 x 26 % = 1 073,02 kt. |
| 14 | CALC-A7-MELANGE-TOT-KT | Total des trois secteurs | 3 288,85 kt, presente environ 3 289 kt | CALC-A7-MELANGE-TOT-KT | CONFIRMÉ | « Dechets banals 11 671 [...] 4 856 [...] 4 127 » et parts « 9 [...] 24 [...] 26 » | Insee, figures 1 et 2 | Recalcul : 1 050,39 + 1 165,44 + 1 073,02 = 3 288,85 kt. Intervalle lie aux parts arrondies : environ 3,184 a 3,394 Mt. |
| 15 | 7.1 | Le tonnage reel est superieur car petits etablissements et construction exclus | superieur a 3,289 Mt | Inference du texte | NON SOURCÉ | « Champ : France, etablissements de l'industrie manufacturiere de 10 salaries ou plus, etablissements du tertiaire de 20 salaries ou plus. » | Insee, figures 1 et 2 | L'exclusion du BTP et des petits etablissements est confirmee. Le sens exact de l'effet sur la categorie comparable « dechets banals en melange » n'est pas chiffre dans la source. |
| 16 | 7.1 | DAE non dangereux non inertes en Ile-de-France | 5,09 Mt en 2020 | A7-PRPGD-IDF-SUIVI3-2023 | CONFIRMÉ | « 5,09 millions de tonnes de dechets d'activites economiques (DAE) non dangereux non inertes produits en 2020 et traites en Ile-de-France et hors Ile-de-France (DAE hors BTP non pris en charge par le SPGD). » | PRPGD suivi 3, p. 10 | Perimetre correctement indique dans l'annexe. |
| 17 | 7.1 | Serie regionale | 5,90 ; 5,95 ; 5,63 ; 5,09 Mt | A7-PRPGD-IDF-SUIVI3-2023 | CONFIRMÉ | « Total DAE (hors dechets inertes et SPGD) | 5,90 Mt | 2014 [...] 2016 5,95 Mt [...] 2018 5,63 Mt [...] 2020 5,09 Mt » | PRPGD suivi 3, p. 42 | Meme perimetre sur les quatre annees. |
| 18 | 7.1 | 2020 affectee par les confinements | oui | A7-PRPGD-IDF-SUIVI3-2023 | CONFIRMÉ | « 2020 est une annee particuliere avec un arret quasi-total des activites economiques pendant le 1er confinement du printemps et un arret partiel le reste de l'annee. » | PRPGD suivi 3, p. 42 | Reserve correctement donnee. |
| 19 | 7.1 | Objectif de tri des DAE en melange | 100 % en 2025 | A7-PRPGD-IDF-SUIVI3-2023 | CONFIRMÉ | « 100 % des DAE en melange orientes vers une chaine de tri en 2025 (51 % en 2014) » | PRPGD suivi 3, p. 82 | Il s'agit d'un objectif de planification, pas d'un resultat atteint. |
| 20 | 7.1 | Tonnage enfoui en Ile-de-France | 2 228 079 t | A8-CST-ORDIF-ISDND-2023 | CONFIRMÉ | « 2 228 079 tonnes de dechets non dangereux ont ete enfouies [...] en Ile-de-France. » | ORDIF enfouissement, p. 5 | Entree du calcul confirmee. |
| 21 | 7.1 | Part d'origine directe entreprises dans l'enfouissement | 38,1 % | A8-CST-ORDIF-ISDND-2023 | CONFIRMÉ | « Origines producteurs : [...] 38,1 % d'entreprises » | ORDIF enfouissement, p. 5 | Valeur vraie pour l'origine directe declaree, mais insuffisante pour attribuer les refus a leur producteur initial. |
| 22 | CALC-A7-IDF-DAE-ENFOUIS-T | DAE enfouis, lecture directe | 848 898 t | CALC-A7-IDF-DAE-ENFOUIS-T | CONFIRMÉ | « 2 228 079 tonnes » et « 38,1 % d'entreprises » | ORDIF enfouissement, p. 5 | Recalcul : 2 228 079 x 38,1 % = 848 898,099 t. Calcul arithmetiquement juste. |
| 23 | 7.1, autre lecture | Part entreprises apres reaffectation des refus | 77,6 % | A8-CST-ORDIF-ISDND-2023 | CONFIRMÉ | « En reaffectant les refus a leur producteurs initiaux... 77,6 % d'entreprises » | ORDIF enfouissement, p. 5 | Cette lecture donne 1 728 989 t. Elle est plus solide pour mesurer les dechets economiques a l'origine. |
| 24 | 7.1 | Tonnage incinere en Ile-de-France | 3 810 761 t | A8-CST-ORDIF-UIDND-2023 | CONFIRMÉ | « Apres ces detournements, les usines franciliennes ont alors incinere 3 810 761 tonnes en 2022. » | ORDIF incineration, p. 5 | Entree du calcul confirmee. |
| 25 | 7.1 | Part directe d'entreprises dans l'incineration | 8,8 % | A8-CST-ORDIF-UIDND-2023 | CONFIRMÉ | « 8,8 % d'entreprises » | ORDIF incineration, p. 6 | La source ne fournit pas ici de reaffectation des residus des installations de traitement. |
| 26 | CALC-A7-IDF-DAE-INCIN-T | Dechets d'entreprises incineres | 335 347 t | CALC-A7-IDF-DAE-INCIN-T | CONFIRMÉ | « 3 810 761 tonnes » et « 8,8 % d'entreprises » | ORDIF incineration, p. 5 et 6 | Recalcul : 3 810 761 x 8,8 % = 335 346,968 t. |
| 27 | 7.1 | Aucun tonnage regional de DAE en melange n'est publie | aucun | R-048, contredit par A7-PRPGD-IDF-SUIVI3-2023 | DIFFÉRENT | « Total DAE franciliens en melange [...] 2020 2,77 Mt » | PRPGD suivi 3, p. 82 | La source publie 2,77 Mt en 2020 et precise que c'est un minimum, les exports etant incompletement connus. |
| 28 | 7.2 | Parts de dechets banals en melange | 9 % ; 24 % ; 26 % ; 16 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Industrie manufacturiere [...] En melange 9 [...] Commerce [...] 24 [...] Services [...] 26 [...] Ensemble [...] 16 » | Insee, page web corrigee, figure 2 | Valeurs corrigees. |
| 29 | 7.2 | Papier-carton trie | 17 % ; 46 % ; 49 % ; 30 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Industrie manufacturiere [...] Papier-carton 17 [...] Commerce 46 [...] Services 49 [...] Ensemble 30 » | Insee, page web corrigee, figure 2 | Conforme. |
| 30 | 7.2 | Bois trie | 39 % ; 13 % ; 14 % ; 28 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Industrie manufacturiere [...] Bois 39 [...] Commerce 13 [...] Services 14 [...] Ensemble 28 » | Insee, page web corrigee, figure 2 | Conforme. |
| 31 | 7.2 | Plastiques tries | 4 % ; 6 % ; 5 % ; 5 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Industrie manufacturiere [...] Plastiques 4 [...] Commerce 6 [...] Services 5 [...] Ensemble 5 » | Insee, page web corrigee, figure 2 | Conforme. |
| 32 | 7.2 | Commerce et services : environ un quart en melange | 24 % et 26 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Commerce [...] En melange 24 » et « Services [...] En melange 26 » | Insee, page web corrigee, figure 2 | Reformulation correcte. |
| 33 | 7.2 | Industrie agroalimentaire | 30 % de l'industrie ; 71 % organiques | A7-INSEE-IP2034-2025 | CONFIRMÉ | « Dans l'industrie agroalimentaire (IAA), qui genere 30 % des quantites de dechets non dangereux de l'industrie manufacturiere hors mineraux et boues, les dechets sont majoritairement des dechets organiques (71 %). » | Insee, texte apres figure 1 | L'orientation vers compostage ou methanisation est une recommandation, pas un chiffre Insee. |
| 34 | 7.2 | Dechets tries valorises | 79 % | A7-INSEE-IP2034-2025 | CONFIRMÉ | « tous secteurs confondus, 79 % des dechets tries sont valorises » | Insee, texte avant figure 3 | Conforme. |
| 35 | 7.3 | Composition des flux en melange | bois 28 % ; inertes 19 % ; fines 34 % ; fibreux 7 % ; plastiques 5 % ; metaux 3 % ; textiles 3 % ; platre 1 % | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « Le bois (28%), dont les 3/4 correspondent a du bois B ; Les inertes (19%) ; 34% d'elements fins ou non reconnaissables ; 19% pour le reste [...] fibreux 7% ; plastiques 5% ; metaux 3% ; textiles 3% ; platre 1%. » | ADEME, figure 14, p. 30 imprimee | Meme valeur et meme perimetre : flux en melange recus par les centres audites. |
| 36 | 7.3 | Taille et nature de l'echantillon | 18 sites, donnees 2023 | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « L'etude a donc finalement ete effectuee sur un panel de 18 sites. » et « Les donnees recoltees concernent l'annee de reference 2023. » | ADEME, p. 16 et p. 20 imprimees | Sites volontaires, 8 sites a engins et 10 mecanises. |
| 37 | 7.3 | Repartition des entrants du panel | 52 % melange, 48 % monoflux | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « 52% de flux en melange pour 48% de monoflux » | ADEME, p. 24 imprimee, figure 6 | Conforme. |
| 38 | 7.3 | Composition visuelle, non assimilable a une campagne nationale | oui | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « La precision des identifications visuelles reste approximative par rapport a des caracterisations effectuees en bonne et due forme » | ADEME, p. 28 imprimee | L'annexe donne les limites essentielles : visuel, 18 sites, pas une campagne nationale. La variabilite temporelle pourrait etre rendue plus visible. |
| 39 | 7.3 | Humidite, PCI et chlore non mesures dans cette etude | aucune valeur | A7-ADEME-TRI-DAE-2025 | ABSENT | « Les donnees recoltees concernent l'annee de reference 2023. » | ADEME, rapport entier, recherche des termes et tableaux | Le rapport de composition ne fournit pas de mesure exploitable d'humidite, de PCI ou de chlore pour ces flux en melange. L'annexe signale correctement ce manque. |
| 40 | CALC-A7-NONCONV-PCT | Inertes + metaux + platre | 23 % | CALC-A7-NONCONV-PCT | CONFIRMÉ | « inertes (19%) [...] metaux 3% [...] platre 1% » | ADEME, figure 14, p. 30 imprimee | Recalcul : 19 + 3 + 1 = 23 %. |
| 41 | 7.3 | Fines de composition inconnue | 34 % | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « 34% d'elements fins ou non reconnaissables » | ADEME, figure 14, p. 30 imprimee | « Non reconnaissables » ne signifie pas chimiquement inertes. Leur devenir reste a mesurer. |
| 42 | 7.3 | Trois quarts du bois sont du bois B | 75 % du bois, soit environ 21 % du flux total | A7-ADEME-TRI-DAE-2025 | CONFIRMÉ | « Le bois (28%), dont les 3/4 correspondent a du bois B » | ADEME, figure 14, p. 30 imprimee | 28 % x 75 % = 21 % du flux total, ordre de grandeur. |
| 43 | 7.3 | Bois B decrit comme peint, verni ou colle | trois quarts du bois | A7-ADEME-TRI-DAE-2025 | ABSENT | « Le bois (28%), dont les 3/4 correspondent a du bois B » | ADEME, figure 14, p. 30 imprimee | Le rapport cite ne definit pas le bois B par les mots « peint, verni ou colle ». Une source de classification est necessaire. |
| 44 | 7.3 | Revetements et colles susceptibles d'apporter chlore et metaux au char | non chiffre | aucune source dans l'annexe | NON SOURCÉ | Aucune citation dans l'annexe. | Section 7.3 | Risque plausible, mais a sourcer et surtout a mesurer sur le flux cible. |
| 45 | CALC-A7-ORG-PCT | Bois + fibreux + textiles | 38 % | CALC-A7-ORG-PCT | CONFIRMÉ | « bois 28% [...] fibreux 7% [...] textiles 3% » | ADEME, figure 14, p. 30 imprimee | Recalcul : 28 + 7 + 3 = 38 %. |

## Verification HTML contre source Markdown

Les sections 7.1 a 7.3 du HTML et la source Markdown portent les memes valeurs et les memes affirmations. Aucun ecart HTML / source n'a ete trouve dans ce lot.

## Recalculs demandes

| Calcul | Recalcul independant | Verdict |
|---|---:|---|
| CALC-A7-MELANGE-IND-KT | 11 671 x 9 % = 1 050,39 kt | CONFIRMÉ |
| CALC-A7-MELANGE-COM-KT | 4 856 x 24 % = 1 165,44 kt | CONFIRMÉ |
| CALC-A7-MELANGE-SERV-KT | 4 127 x 26 % = 1 073,02 kt | CONFIRMÉ |
| CALC-A7-MELANGE-TOT-KT | 1 050,39 + 1 165,44 + 1 073,02 = 3 288,85 kt | CONFIRMÉ |
| CALC-A7-IDF-DAE-ENFOUIS-T | 2 228 079 x 38,1 % = 848 898,099 t | CONFIRMÉ arithmetiquement, interpretation incomplete |
| Lecture alternative enfouissement | 2 228 079 x 77,6 % = 1 728 989,304 t | CONFIRMÉ par la meme source |
| CALC-A7-IDF-DAE-INCIN-T | 3 810 761 x 8,8 % = 335 346,968 t | CONFIRMÉ |
| CALC-A7-NONCONV-PCT | 19 + 3 + 1 = 23 % | CONFIRMÉ |
| CALC-A7-ORG-PCT | 28 + 7 + 3 = 38 % | CONFIRMÉ |

Les parts Insee sont publiees sans decimales. En prenant pour chaque part un intervalle de plus ou moins 0,5 point, le total national calcule des trois secteurs est approximativement compris entre 3,184 et 3,394 Mt. L'affichage « about 3,289 kt » est donc acceptable, a condition de ne pas lui attribuer une precision excessive.

## Ecarts

### E-1 : le tonnage regional en melange existe

- Annexe : « No regional tonnage of mixed business waste is published ».
- Source : 2,77 Mt en 2020, presentees comme un minimum.
- Gravite : IMPORTANT.
- Effet projet : 51 100 t/an representent environ 1,84 % de ce minimum regional, contre environ 1,00 % des 5,09 Mt de DAE totaux. L'approvisionnement regional reste plausible en ordre de grandeur.
- Correction proposee : remplacer l'affirmation par « Le PRPGD estime au minimum 2,77 Mt de DAE franciliens en melange en 2020 ; les exports interregionaux incompletement connus rendent ce total minimal. »

### E-2 : le calcul de l'enfouissement utilise une origine directe, pas l'origine economique finale

- Annexe : 38,1 % et 848 898 t de dechets d'entreprises enfouis.
- Source : 38,1 % en origine directe, mais 77,6 % apres reaffectation des refus a leurs producteurs initiaux.
- Gravite : IMPORTANT.
- Effet projet : le total pertinent devient environ 1,729 Mt. Une machine de 51 100 t/an represente environ 3,0 % de ce volume, au lieu de 6,0 % du calcul direct. Cette correction renforce, et non affaiblit, l'ordre de grandeur du gisement.
- Correction proposee : afficher les deux lectures et retenir 1,729 Mt pour l'origine economique, avec une note methodologique.

### E-3 : definition et risque du bois B insuffisamment sources

- Annexe : « painted, varnished or glued » et risque de chlore et metaux dans le char.
- Source citee : confirme seulement « bois B » et la proportion de trois quarts.
- Gravite : IMPORTANT pour les essais et la qualite du char, mais pas une preuve d'impossibilite.
- Correction proposee : ajouter une source de classification du bois B et maintenir chlore et metaux comme donnees a mesurer avant validation du flux.

### E-4 : limites de la composition moyenne encore trop discretes

- Annexe : mentionne une estimation visuelle sur 18 sites et l'absence de campagne nationale.
- Source : ajoute que la precision visuelle est approximative, que chaque site a ses propres entrants et que la nature evolue dans le temps.
- Gravite : MINEUR dans la section 7.3, IMPORTANT si ces pourcentages sont utilises comme recette de dimensionnement sans essais.
- Correction proposee : ajouter une phrase indiquant que les pourcentages sont des tendances de sites volontaires, non une specification d'alimentation.

### E-5 : le sens « le tonnage reel est plus eleve » n'est pas demontre par la source

- Annexe : le tonnage reel serait superieur parce que le BTP et les petits etablissements sont exclus.
- Source : confirme les exclusions, mais ne publie pas le total comparable de dechets banals en melange ajoute par ces secteurs.
- Gravite : MINEUR.
- Correction proposee : ecrire « ce calcul ne couvre pas le BTP ni les petits etablissements » sans conclure quantitativement sur l'ecart.

### E-6 : annee contradictoire dans le rapport ADEME

- Annexe : 57 Mt et 7 Mt en 2021.
- Source : la section 1.1 indique 2021, le resume indique 2020.
- Gravite : MINEUR.
- Correction proposee : conserver 2021 avec renvoi a la p. 7, tout en signalant l'incoherence du resume.

## Autres interpretations

1. Le meilleur chiffre regional disponible pour le flux en melange est 2,77 Mt en 2020, mais la source le qualifie de minimum car les exports hors region sont incompletement connus. Il ne faut donc ni l'ignorer, ni le presenter comme exhaustif.
2. Pour l'enfouissement, 38,1 % repond a la question « qui livre directement l'ISDND ? ». La valeur 77,6 % repond mieux a « qui a produit initialement le dechet ? ». La seconde lecture est la plus solide pour dimensionner un gisement economique.
3. La composition ADEME de 2023 decrit des flux recus dans 18 centres de tri volontaires. Elle ne decrit pas necessairement un DAE brut moyen national, ni les refus de tri, ni le flux qui serait contractualise par Urban Rig.
4. Les 34 % de fines ou elements non reconnaissables peuvent contenir des fractions combustibles, de l'humidite et des inertes. Les laisser non affectes est prudent pour ce stade, mais empeche de fermer le bilan matiere et energetique.
5. Le 5 % de plastiques est plutot conservateur pour le rendement en huile. En revanche, les 28 % de bois, dont environ 21 points de bois B, peuvent rendre optimiste toute hypothese de char commercialisable sans analyse de chlore et de metaux.

## Hypothese D-049, appreciation legere

D-049 est clairement presentee comme HYPOTHESE dans l'annexe et dans la decision. Elle est raisonnable comme hypothese exploratoire d'ordre de grandeur, mais trop optimiste pour un dimensionnement standard si les rendements sont appliques a la masse brute sans humidite et si la composition visuelle moyenne est traitee comme une specification fixe. Elle doit etre remplacee par des mesures du flux contractualise avant decision d'investissement.

## Cinq erreurs les plus graves

1. Le texte nie l'existence du tonnage regional de 2,77 Mt de DAE en melange.
2. Le calcul d'enfouissement retient 38,1 % alors que 77,6 % est la lecture par producteur initial.
3. Le risque du bois B est formule sans source de classification ni analyse du flux cible.
4. La composition de 18 sites volontaires peut etre lue trop facilement comme une composition standard de DAE.
5. Le texte conclut que le tonnage national reel est plus eleve sans chiffrage comparable dans la source.

Aucun de ces points ne demontre une impossibilite d'approvisionnement pour une machine de 51 100 t/an. Les points 2 et 3 affectent toutefois directement la definition du flux et les essais necessaires.

## Conclusion en langage simple

PASSE : les tonnages nationaux Insee corriges, le total calcule de 3,289 Mt, les parts sectorielles, la composition ADEME et les sommes de 23 % et 38 % sont correctement reprises et calculees.

NE PASSE PAS : l'affirmation selon laquelle aucun tonnage francilien de DAE en melange n'est publie. Le PRPGD donne 2,77 Mt en 2020, en precisant qu'il s'agit d'un minimum.

POSSIBLE SOUS CONDITIONS : utiliser la composition des 18 sites comme hypothese de scenario. Elle suffit pour un ordre de grandeur, pas pour concevoir ou garantir l'exploitation.

A MESURER AVANT CONCLUSION : humidite, PCI, chlore, soufre, metaux, composition des fines, variabilite et composition exacte du bois B du flux contractualise.

Verdict global du lot 1 : PASSE SOUS CONDITIONS. Aucun ecart bloquant pour l'existence du gisement a l'echelle d'une machine. Trois ecarts importants doivent etre corriges : le tonnage regional en melange, l'interpretation de l'enfouissement, et la definition ainsi que le risque du bois B.

## Ce qui n'a pas ete verifie dans ce lot

- Sections 7.4 a 7.9 et Key Messages : reservees au lot 2.
- Rendements huile, gaz, char et liquide : reserves au lot 2.
- Prix d'entree et couts : exclus du controle chiffre et reserves au lot 2 pour leur etiquette d'hypothese.
- Bilan energetique, humidite et PCI publics alternatifs : reserve au lot 2.
- Applicabilite commerciale du char issu de bois B : aucune analyse du flux cible n'est fournie.

## Decompte

- CONFIRMÉ : 40
- DIFFÉRENT : 1
- ABSENT : 2
- NON SOURCÉ : 2
- INACCESSIBLE : 0
- CALCUL FAUX : 0
- Total : 45 verdicts

## Controle automatique

La commande de controle a ete lancee sur le HTML. Elle a detecte 21 affirmations chiffrees et les a classees « sans source » parce que le controleur automatique ne reconnait pas les liens vers les fiches HTML generees comme des identifiants de registre. Ce resultat technique ne remplace pas la lecture des fiches et des sources d'origine effectuee ci-dessus.
