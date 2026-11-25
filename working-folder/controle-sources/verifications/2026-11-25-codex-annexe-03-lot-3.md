Accès internet : OUI
Lecture des PDF : OUI

# Contre-vérification de l'annexe 3, lot 3, vérification légère

Date : 25 novembre 2026. Agent : codex. Périmètre : sections 3.3 et 3.4 du HTML de référence. Selon la consigne révisée, ce lot vérifie seulement les seuils réglementaires et textes de loi, les valeurs mesurées, et les calculs sans prix. Aucun prix par défaut, aucune hypothèse D-xxx et aucune valeur de marché n'ont été recalculés ou actualisés.

**Conclusion : les calculs de gaz et d'hydrogène passent. Après retrait de tout l'hydrogène, le gaz restant couvre encore 1,79 fois le besoin thermique indiqué. La vente d'hydrogène reste une option à confirmer par un essai de purification, tandis que l'injection directe du gaz dans le réseau ne passe pas. Pour les métaux, les seuils sont correctement cités, mais aucune mesure de propreté ne démontre encore la sortie du statut de déchet.**

## 1. Tableau des verdicts

N° | Section ou fiche | Affirmation | Valeur annoncée | Source citée | Verdict | Citation exacte relevée | Emplacement réel | Commentaire
--- | --- | --- | --- | --- | --- | --- | --- | ---
| 1 | 3.3.1 / 3.R.u | Corps étrangers dans les débris de fer ou d'acier | Au plus 2 % | A3-UE-REG-333-2011 | CONFIRMÉ | « La quantité totale de corps étrangers (stériles) est inférieure ou égale à 2 % en poids. » | Règlement (UE) 333/2011, annexe I, point 1.2 | Seuil de sortie du statut de déchet. |
| 2 | 3.3.1 / 3.R.u | Oxyde et huile sur les débris de fer ou d'acier | Pas d'excès d'oxyde ni d'huile visible | A3-UE-REG-333-2011 | CONFIRMÉ | « Les débris ne contiennent pas d'oxyde de fer en excès » ; « Les débris sont exempts d'huiles, émulsions huileuses, lubrifiants ou graisses visibles » | Règlement (UE) 333/2011, annexe I, points 1.3 et 1.4 | Correct. |
| 3 | 3.3.1 / 3.R.u | Corps étrangers ou rendement des débris d'aluminium | Au plus 5 %, ou rendement d'au moins 90 % | A3-UE-REG-333-2011 | CONFIRMÉ | « La quantité totale de corps étrangers est inférieure ou égale à 5 % en poids ou le rendement en métal est supérieur ou égal à 90 %. » | Règlement (UE) 333/2011, annexe II, point 1.2 | Correct. |
| 4 | 3.3.1 / 3.P.r | Teneur magnétique du standard Citeo pour l'acier | Au moins 88 % | A3-CITEO-GUIDE-ODQ-2024-STANDARDS | CONFIRMÉ | « Minimum 95 % d'emballages en acier mis en paquet*, soit au minimum 88 % de teneur en métal magnétique » | Guide Citeo 2024, standard acier | Ce standard vise les emballages issus de collecte sélective. |
| 5 | 3.4.2 / 2.2.f | Hydrogène mesuré dans l'échantillon | 12,7 % vol. | KANSO-B2002600 | CONFIRMÉ | « 水素 ガスクロマトグラフ法 12.7 % » | Rapport B2002600, p. 1 | Mesure de laboratoire retenue comme applicable. |
| 6 | 3.4.2 / 2.2.f | Dilution de l'échantillon par l'air | O2 12,3 % ; N2 65,8 % | KANSO-B2002600 | CONFIRMÉ | « 酸素 ガスクロマトグラフ法 12.3 % » ; « 窒素 ガスクロマトグラフ法 65.8 % » | Rapport B2002600, p. 1 | Les deux valeurs confirment une forte dilution. |
| 7 | 3.4.2 / 2.2.f | Autres constituants utilisés dans les calculs | CO 0,6 % ; CH4 3,2 % ; CO2 1,7 % ; C2H4 0,2 % ; C2H6 0,7 % ; C3H8 0,3 % ; C3H6 0,3 % ; H2S < 0,5 ppm | KANSO-B2002600 | CONFIRMÉ | « CO 0,6 % ; CH4 3,2 % ; CO2 1,7 % ; C2H4 0,2 % ; C2H6 0,7 % ; C3H8 0,3 % ; C3H6 0,3 % ; H2S < 0,5 ppm » | Rapport B2002600, p. 1, tableau d'analyse | Mesures retenues comme applicables. |
| 8 | 3.4.2 | Part volumique d'hydrogène hors air | Environ deux tiers | KANSO-B2002600 | CONFIRMÉ | « H2 12,7 % ; CH4 3,2 % ; CO2 1,7 % ; CO 0,6 % ; C2H4 0,2 % ; C2H6 0,7 % ; C3H8 0,3 % ; C3H6 0,3 % » | Rapport B2002600, p. 1 ; recalcul | 12,7 / 19,7 = 64,47 %, soit environ deux tiers. |
| 9 | 3.4.2 / 3.C.ae | Part massique d'hydrogène dans le gaz hors air | 11,6 % | CALC-A3-H2-PART-MASSE | CONFIRMÉ | « x_h2*m_h2 / (x_h2*m_h2 + x_ch4*m_ch4 + x_c2h6*m_c2h6 + x_c2h4*m_c2h4 + x_c3h8*m_c3h8 + x_c3h6*m_c3h6 + x_co*m_co + x_co2*m_co2) * 100 » | calculs.yaml, CALC-A3-H2-PART-MASSE | Recalcul indépendant : 11,5807 %. |
| 10 | 3.4.2 / 3.C.af | Part de l'énergie du gaz portée par l'hydrogène | 37,2 % | CALC-A3-H2-PART-ENERGIE | CONFIRMÉ | « w / 100 * (p_h2 / m_h2) / pci * 100 » | calculs.yaml, CALC-A3-H2-PART-ENERGIE | Recalcul indépendant : 37,1590 %. |
| 11 | 3.4.1 / 2.5.d.8 | Énergie du gaz par tonne de charge riche en résines | 4 299 MJ/t | CALC-A2-NRJ-GAZ-RESINE | CONFIRMÉ | « part * 1000 * pci » | calculs.yaml, CALC-A2-NRJ-GAZ-RESINE | 0,115 × 1 000 × 37,3861 = 4 299,4 MJ/t. |
| 12 | 3.4.1 | Besoin thermique du brûleur par tonne | 1 506,65 MJ/t | CALC-A2-BRULEUR-MJ-T | CONFIRMÉ | « kcal_s * 86400 * kcal_kj / 1000 / capacite » | calculs.yaml, CALC-A2-BRULEUR-MJ-T | Recalcul indépendant : 1 506,645 MJ/t. |
| 13 | 3.4.1 / 3.C.ad | Surplus avant séparation de l'hydrogène | 2 793 MJ/t | CALC-A3-GAZ-SURPLUS-RESINE | CONFIRMÉ | « gaz - bruleur » | calculs.yaml, CALC-A3-GAZ-SURPLUS-RESINE | Recalcul : 4 299,4 - 1 506,65 = 2 792,75 MJ/t. |
| 14 | 3.4.2 / 3.C.h | Hydrogène avant purification | 13,3 kg/t | CALC-A3-H2-KG-T-RESINE | CONFIRMÉ | « part * 1000 * w / 100 » | calculs.yaml, CALC-A3-H2-KG-T-RESINE | Recalcul indépendant : 13,3178 kg/t. |
| 15 | 3.4.2 / 3.C.ag | Énergie du gaz après retrait de tout l'hydrogène | 2 702 MJ/t | CALC-A3-GAZ-SANS-H2-RESINE | CONFIRMÉ | « gaz * (1 - e / 100) » | calculs.yaml, CALC-A3-GAZ-SANS-H2-RESINE | Recalcul indépendant : 2 701,79 MJ/t. |
| 16 | 3.4.2 / 3.C.ah | Couverture du brûleur après retrait de tout l'hydrogène | 1,8 fois | CALC-A3-COUV-SANS-H2-RESINE | CONFIRMÉ | « reste / bruleur » | calculs.yaml, CALC-A3-COUV-SANS-H2-RESINE | Recalcul indépendant : 1,79325. Marge thermique : environ 1 195 MJ/t. |
| 17 | 3.4.2 / 3.L.u | Pureté et récupération d'un cas PSA publié | 99,9913 % et 75,5 % | A3J-MDPI-ENERGIES-2025-PSA | CONFIRMÉ | « produced hydrogen with 99.9913% purity, achieving 75.5% recovery » | Revue Energies 2025, passage citant Abdeljaoued et al. | Source secondaire et gaz d'alimentation différent. |
| 18 | 3.4.2 / 3.L.u | Plage générale de récupération PSA | 80 à 95 % | A3J-MDPI-ENERGIES-2025-PSA | CONFIRMÉ | « PSA can remove impurities to ppm levels and achieve recovery rates of 80-95%. » | Revue Energies 2025 | Ordre de grandeur, pas une garantie pour ce gaz. |
| 19 | 3.4.2 / 3.L.v | Pureté annoncée par un fabricant de PSA | Jusqu'à 99,9999 % | A3J-LINDE-PSA-H2 | CONFIRMÉ | « the resulting hydrogen gas meets all purity requirements up to 99.9999 mol-%. » | Documentation Linde Engineering | Déclaration commerciale du fabricant. |
| 20 | 3.4.3 / 3.R.v | Définition d'un carburant à base de carbone recyclé | Déchet non renouvelable impropre à la valorisation matière | A3J-UE-DIR-2018-2001-ART2-RCF | CONFIRMÉ | « produits à partir de flux de déchets liquides ou solides d'origine non renouvelable ne se prêtant pas à la valorisation de matières » | Directive (UE) 2018/2001, article 2, point 35 | La qualification suppose que l'impossibilité de valorisation matière soit démontrée. |
| 21 | 3.4.3 / 3.R.w | Méthode applicable aux carburants à base de carbone recyclé | Règlement 2023/1185, pas la méthode 2025/2359 | A3J-UE-REG-DEL-2025-2359 | CONFIRMÉ | « La méthode définie dans le règlement délégué (UE) 2023/1185 s'applique [...] aux carburants à base de carbone recyclé, qui constituent une sous-catégorie des carburants bas carbone. » | Règlement délégué (UE) 2025/2359, considérant 2 | La phrase de l'annexe est correcte pour la méthode 2025/2359, mais ne signifie pas une exclusion générale du statut bas carbone. |
| 22 | 3.4.3 / 3.R.x | Soutien français prévu au chapitre II | Réservé à l'électrolyse de l'eau | Code de l'énergie, article L.812-1 | CONFIRMÉ | « Le dispositif de soutien public prévu au présent chapitre est exclusivement réservé à la production d'hydrogène renouvelable ou d'hydrogène bas-carbone par électrolyse de l'eau » | Code de l'énergie, article L.812-1, version en vigueur | Le texte vise le dispositif de soutien de ce chapitre. |
| 23 | 3.4.4 / 3.L.x | Teneur maximale en hydrogène pour l'injection | Moins de 2 % molaire | A3J-NATRAN-SPEC-METHANE-SYNTHESE | CONFIRMÉ | « Teneur en H2 < 2 % (molaire) » | Prescriptions GRTgaz, annexe 4, p. 1 | Le gaz hors air contient 64,47 % H2. L'injection directe ne passe pas. |

## 2. Écarts

Aucun écart bloquant, important ou mineur n'est retenu dans ce lot. Les deux formulations réglementaires discutables sont traitées ci-dessous, car leur lecture correcte ne change pas la conclusion de l'annexe.

## 3. Vérification logique et conclusion pratique

### Métaux, verre et inertes

Les seuils réglementaires sont correctement reproduits. En revanche, aucune analyse ne donne le pourcentage de char, de verre, de terre ou d'huile restant sur les métaux récupérés. La sortie du statut de déchet n'est donc pas encore démontrée. Cela ne bloque pas une cession comme déchet métallique à un recycleur autorisé, mais cela peut entraîner un déclassement commercial ou un coût de préparation.

Verdict opérationnel : **PASSE comme flux de déchet métallique à faire préparer ; PAS ENCORE DÉMONTRÉ comme métal ayant cessé d'être un déchet. Risque commercial modéré, risque réglementaire maîtrisable par tri et analyse.**

### Hydrogène et surplus de gaz

- Hydrogène brut calculé : **13,32 kg/t** de charge riche en résines.
- Avec 75,5 à 95 % de récupération PSA : **10,1 à 12,7 kg/t** récupérables, avant validation sur ce gaz précis.
- Énergie restant dans le gaz après retrait de tout l'hydrogène : **2 701,8 MJ/t**.
- Besoin du brûleur : **1 506,6 MJ/t**. Marge : **1 195,1 MJ/t**, soit une couverture de **1,79 fois**.
- Après retrait de l'air, le gaz contient 64,47 % H2, 3,05 % CO et 8,63 % CO2. Les limites d'injection sont respectivement < 2 %, < 0,1 % et < 2,5 %. L'injection directe échoue donc sur au moins trois paramètres.

Verdict opérationnel : **PASSE pour la cohérence du bilan massique et thermique. L'option hydrogène présente un potentiel réel, sous réserve d'un essai PSA et d'un devis. L'injection directe du gaz NE PASSE PAS ; elle demanderait une conversion et une épuration complètes.**

## 4. Autres interprétations

### Carburant à base de carbone recyclé et statut bas carbone

- Lecture de l'annexe : la méthode européenne pour l'hydrogène bas carbone exclut les carburants à base de carbone recyclé, donc aucun statut bas carbone n'est établi.
- Ma lecture : le règlement 2025/2359 exclut ces carburants de **sa propre méthode**, parce que le règlement 2023/1185 s'applique. Le texte les appelle expressément « une sous-catégorie des carburants bas carbone ». Le règlement 2023/1185 exige une réduction d'émissions d'au moins 70 %.
- Conclusion : la formulation peut être lue trop largement, mais la conclusion prudente de l'annexe reste correcte. Sans calcul de cycle de vie démontrant 70 %, l'appellation bas carbone n'est pas acquise.

### Soutien public français

- Lecture de l'annexe : le soutien public français est réservé à l'électrolyse de l'eau.
- Ma lecture : l'article L.812-1 dit exactement « le dispositif de soutien public prévu au présent chapitre ». Il ne permet pas d'affirmer qu'aucune autre aide publique ne pourrait jamais exister.
- Conclusion : le mécanisme national visé exclut bien l'hydrogène de pyrolyse. La portée devrait être comprise comme celle du chapitre II du Code de l'énergie.

### Vente des métaux

- Lecture de l'annexe : les métaux et le verre sont vendus comme ressources recyclées, selon OneWorld.
- Ma lecture : « Metals and glasses = Recycled resources » est une déclaration du constructeur. Sans mesure de propreté, elle ne prouve pas la sortie du statut de déchet, mais reste compatible avec une vente à un recycleur sous statut de déchet.
- Conclusion : débouché plausible, qualité et prix à confirmer.

## 5. Autres points, une ligne chacun

- Propreté des métaux : mesurer les corps étrangers, l'huile visible et, pour l'aluminium, le rendement métallique, car ces paramètres déterminent la sortie du statut de déchet.
- Verre et inertes : obtenir une spécification d'acceptation et vérifier la réglementation locale de l'usage en remblai.
- PSA : faire analyser le gaz non dilué et réaliser un essai fournisseur, car C2, C3, CO et contaminants influencent la récupération et le prétraitement.
- Énergie auxiliaire de purification : obtenir la consommation de compression et de PSA, car la marge thermique calculée ne chiffre pas l'électricité de séparation.
- Acheteur du gaz : vérifier l'autorisation de combustion, la distance, la pression et la composition contractuelle.
- Prix des métaux, du gaz, de l'hydrogène, ratios Citeo, valeurs par tonne et hypothèses D-028 à D-031 : non vérifiés selon la consigne révisée.
- Valeurs de marché plus récentes : aucune recherche effectuée selon la consigne révisée.

## 6. Ce qui n'a pas pu être vérifié

- La propreté réelle des métaux, du verre et des inertes n'a pas été mesurée.
- La récupération et la pureté d'un PSA sur le gaz Urban Rig n'ont pas été essayées.
- Le bilan électrique et le coût de la purification ne sont pas disponibles.
- Le calcul de cycle de vie requis pour une qualification bas carbone n'est pas disponible.
- Aucun prix, aucune hypothèse D-xxx et aucune actualisation de marché ne sont vérifiés dans ce lot.

## 7. Décompte

Verdict | Nombre
--- | ---:
CONFIRMÉ | 23
DIFFÉRENT | 0
ABSENT | 0
INACCESSIBLE | 0
NON SOURCÉ | 0
CALCUL FAUX | 0
**Total** | **23**

23 verdicts portent une citation exacte et sont ajoutés au registre sans modifier les entrées antérieures.

## 8. Explication simple des conclusions

### Hydrogène

Le gaz mesuré après retrait de l'air contient environ 64,5 % d'hydrogène. À partir de la production de gaz annoncée, l'annexe calcule 13,3 kg d'hydrogène brut par tonne traitée. Une séparation PSA récupérant 75,5 % à 95 % donnerait environ 10,1 à 12,7 kg d'hydrogène séparé par tonne.

L'essai de purification demandé ne remet donc pas en cause la mesure. Il sert à confirmer, sur ce gaz précis, la quantité réellement récupérée, la pureté obtenue, le prétraitement nécessaire et la consommation d'électricité. La vente d'hydrogène est une option techniquement plausible, mais elle n'est pas encore un produit commercial démontré.

### Injection du gaz dans le réseau

Paramètre | Gaz Urban Rig après retrait de l'air | Limite du réseau citée | Résultat
--- | ---: | ---: | ---
Hydrogène | environ 64,5 % | inférieur à 2 % | Ne passe pas
Monoxyde de carbone | environ 3,05 % | inférieur à 0,1 % | Ne passe pas
Dioxyde de carbone | environ 8,63 % | inférieur à 2,5 % | Ne passe pas

Le gaz brut ne peut donc pas être injecté directement dans le réseau de gaz naturel. Cela n'empêche pas de séparer et vendre l'hydrogène, de brûler le gaz sur le site dans un équipement autorisé, ou de le fournir à un industriel proche disposant d'un équipement adapté. Une injection au réseau demanderait une conversion et une épuration beaucoup plus poussées.

### Métaux

Le procédé extrait bien des métaux et le constructeur les décrit comme des ressources recyclées. Pour une sortie du statut de déchet, les limites citées demandent notamment au plus 2 % de corps étrangers pour l'acier, sans huile visible ni excès d'oxyde, et au plus 5 % de corps étrangers pour l'aluminium, ou un rendement métallique d'au moins 90 %.

Aucune mesure de propreté n'est encore fournie. Cela signifie que la vente directe comme produit sorti du statut de déchet n'est pas démontrée. Les métaux peuvent néanmoins être vendus comme ferrailles sous statut de déchet à un recycleur autorisé. Une mesure simple des corps étrangers, de l'huile visible et du rendement métallique permettrait de trancher la voie de vente directe. Rien dans les données actuelles ne montre que le débouché de recyclage échouerait.
