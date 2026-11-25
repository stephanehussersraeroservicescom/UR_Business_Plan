# Contre-vérification de l'annexe 2, lot 1

Date : 2026-11-25  
Agent : codex  
Document vérifié : `nouveau-business-plan/annexes/annexe-02-html/index.html`, sections 2.1 à 2.3 et fiches liées  
Accès internet : OUI  
Lecture des PDF : OUI, originaux locaux ouverts aux pages citées

## Périmètre et méthode

Ce lot ne reprend pas les 346 lignes du contrôle d'octobre. Il réexamine seulement les réserves R-1 à R-5 du rapport du 15 octobre 2026 et recherche une modification ultérieure qui changerait une conclusion. Les règles de vérification légère du 25 novembre 2026 sont appliquées : cas standard, ordre de grandeur, effet réel sur la décision.

La version actuelle de l'annexe 2 est identique à la révision contrôlée en octobre : `git diff 676ce7e` ne relève aucune modification du Markdown, du HTML principal ou des fiches de preuve de l'annexe 2. Le contrôle automatique exécuté en mémoire, pour ne pas écrire hors du dossier autorisé, trouve 348 affirmations chiffrées, aucune sans source et aucune erreur dans le document. Les 34 erreurs globales restantes concernent les paramètres du projet et non ce lot.

## Tableau des verdicts

N° | Section ou fiche | Affirmation courte | Valeur annoncée | Source citée | Verdict | Citation exacte | Emplacement réel | Commentaire
---|---|---|---|---|---|---|---|---
1 | 2.2.2, R-1 | La composition du gaz analysé est transférable, seule la quantité est incertaine | « the uncertainty lies in the quantity, not the composition » | KANSO-B2002600 | ABSENT | « 試料名 [...] オフガス » ; « 採取年月日 2020年11月25日 » ; « 採取箇所 [vide] » | `Analysis-Results-Off-gas-Odor-Exhaust.pdf`, p. 1 | Le rapport caractérise un échantillon de 2020. Il ne démontre pas l'invariance de composition entre charges. D-029 présente bien ce transfert comme hypothèse dans la fiche 2.5.0. Réserve ouverte, MINEURE dans le cas standard.
2 | 2.2.3, R-2 | Définition du rendement hors inertes | huile rapportée à l'entrée moins métaux, verre et autres inorganiques | CHIBA-ESSAIS-FICHES | CONFIRMÉ | « 油化率：投入重量から油化に貢献しない金属・ガラスなど無機物の重量を差し引いた重量に対する生成油重量の割合。 » | `prefecture-shiba-test-data-2.pdf`, PDF p. 27 | La base de calcul observée est correctement reprise.
3 | 2.2.3, R-2 | Ce ratio est le rendement effectivement obtenu après le pré-tri projeté | « is the yield of the reactor feed after pre-sorting » | CHIBA-ESSAIS-FICHES et D-035 | ABSENT | « 油化率：投入重量から油化に貢献しない金属・ガラスなど無機物の重量を差し引いた重量に対する生成油重量の割合。 » | même source, PDF p. 27 | La source ne teste pas le pré-tri. D-035 en fait une hypothèse déclarée et les deux bases restent affichées. Réserve ouverte, MINEURE dans le cas standard.
4 | 2.2.1, R-3 | Valeurs de l'essai 3P du 11 juillet, écarté des moyennes | entrée 60,0 kg ; huile 49,4 kg ; résidu 9,3 kg ; gaz par différence 1,3 kg | CHIBA-ESSAIS-FICHES | CONFIRMÉ | « 投入重量 60.0kg 生成油重量 49.4kg 油化率 82% » ; « 油化残渣重量 9.3kg オフガス量 1.3kg » | `prefecture-shiba-test-data-2.pdf`, PDF p. 24 | Les valeurs sont exactes. La photo soutient l'interprétation de pièces non converties sans la démontrer analytiquement. L'exclusion est une décision D-034, pas un constat de laboratoire.
5 | 2.2.1 et fiches de calcul, R-3 | Effet de l'exclusion du 11 juillet sur la moyenne d'huile | 73,07 % sur 10 essais | CHIBA-ESSAIS-FICHES ; CALC-A2-HUILE10-MOY-POND | CALCUL FAUX | « 生成油重量 14.8kg [...] 30.7kg [...] 40.7kg [...] 16.2kg [...] 39.8kg [...] 36.5kg [...] 43.1kg [...] 36.3kg [...] 12.2kg [...] 22.0kg » ; entrées correspondantes « 20kg [...] 40kg [...] 50kg [...] 20kg [...] 50kg [...] 50kg [...] 60kg [...] 50kg [...] 20kg [...] 40kg » | même source, PDF p. 19 à 23 ; fiche 2.5.f.7 | 292,3 / 400 = 73,075 %, soit 73,08 % à deux décimales. Avec l'essai exclu : 341,7 / 460 = 74,28 %. L'écart de 1,21 point ne change pas la conclusion. Le 73,1 % du résumé est correct. Réserve ouverte, MINEURE.
6 | 2.3.3 et fiche 2.3.a, R-4 | Valeurs imprimées par OneWorld sur les ordures à 10 % de résines | char 25 % ; huile 5 % ; off-gas 5 % | UR2000-JP-P05-BILAN | CONFIRMÉ | « 樹脂系類含有率 10% で試算 » ; « 炭化物 25% (50m3/ 加工利用可能) » ; « 混合油 [...] 5% (10,000ℓ / 再利用可能) » ; « OFF ガス 5% (10,000ℓ / 再利用) » | `UR2000-JP.pdf`, p. 5 | nature: constructeur. OneWorld imprime bien ces valeurs.
7 | 2.3.3 et fiche 2.3.a, R-4 | Les pourcentages 25 %, 5 % et 5 % forment des fractions massiques homogènes de l'entrée | base massique | UR2000-JP-P05-BILAN | ABSENT | « 一般ゴミ 200ton. ▶ 200m3 (200,000L) » ; « 炭化物 25% (50m3/ 加工利用可能) » ; « 混合油 [...] 5% (10,000ℓ / 再利用可能) » ; « OFF ガス 5% (10,000ℓ / 再利用) » | même source, p. 5 | nature: constructeur. Les quantités associées sont en m3 ou en litres. La base masse/volume n'est pas définie. Réserve ouverte, IMPORTANTE si ces taux alimentent un bilan massique, non bloquante pour le rendement d'huile sur plastiques.
8 | fiche 2.1.g, R-5 | Le poids d'huile des fiches est explicitement obtenu par volume multiplié par densité | méthode de conversion | CHIBA-PROCEDE-HUILE | ABSENT | « ドラム缶で静置分離後に検尺棒を使用して油水量を計量した。 » ; « 全体の検尺量から、水の検尺量を差し引くことで、油の計量を行う。 » | `prefecture-shiba-test-data-2.pdf`, PDF p. 29 | La source décrit un jaugeage des volumes après décantation, pas la conversion de ce volume en masse. Réserve ouverte, MINEURE.
9 | 2.2.3, R-5 | Les volumes d'eau évaporée du bilan sont calculés | 27 L et 15 L | CHIBA-BILANS | CONFIRMÉ | « マテリアルバランスの水(排水)の蒸散水については、計算値とした。 » ; « 排出水 73ℓ [...] 蒸散水 27ℓ » ; « 排出水 85ℓ [...] 蒸散水 15ℓ » | `prefecture-shiba-test-data-2.pdf`, PDF p. 40 et 42 | Le caractère calculé est certain. La différence 100 - 73 et 100 - 85 reproduit les valeurs. Le mot « probably » du HTML est seulement trop prudent.

## État des réserves R-1 à R-5

| Réserve | Toujours ouverte ? | Gravité dans un cas standard | Conclusion |
|---|---|---|---|
| R-1, composition du gaz transférée | Oui | MINEURE | Le transfert est identifié comme hypothèse dans la fiche 2.5.0. Aucune contradiction manifeste ne justifie de rejeter l'analyse mesurée, mais la phrase principale devrait dire explicitement « the project assumes ». |
| R-2, hors inertes assimilé à après pré-tri | Oui | MINEURE | Le ratio hors inertes est exact. Son application après tri est une hypothèse D-035, raisonnable si le tri retire bien les mêmes inertes sans perte sensible de matière convertible. Les bases brute et hors inertes sont toutes deux visibles. |
| R-3, exclusion du 11 juillet et choix de p. 42 | Oui, sur la qualification | MINEURE | Les décisions sont transparentes. L'exclusion ne change la moyenne d'huile que de 1,21 point. Les fiches dépendantes affichent encore 95 % malgré le plafond de 90 % de la fiche d'hypothèses, mais cette étiquette éditoriale ne change aucun chiffre du modèle. |
| R-4, base masse/volume de la brochure japonaise | Oui | IMPORTANTE | Les chiffres constructeur sont fidèlement repris, mais ne doivent pas être utilisés comme fractions massiques avant clarification. Ce point ne remet pas en cause les rendements mesurés sur PE, PP et PS. |
| R-5, arrondis et traçabilité | Oui, partiellement | MINEURE | 73,07 % doit être 73,08 % à deux décimales ; cinq marqueurs `[calc:...]` restent bruts dans la fiche 2.5.0 ; la fiche 2.1.g affirme une conversion masse non explicitée par la source. Le caractère calculé de l'eau évaporée est en revanche confirmé. |

## Écarts à signaler

### E-1. Base masse/volume non définie dans la brochure japonaise

- Annexe : section 2.3.3 et fiche 2.3.a.
- Source : `UR2000-JP.pdf`, p. 5.
- Gravité : IMPORTANTE.
- Correction proposée : ajouter « percentages as printed; mass/volume basis unresolved » et ne jamais utiliser 25 %, 5 % et 5 % comme bilan massique sans confirmation de OneWorld.

### E-2. Statut d'hypothèse du transfert de composition du gaz

- Annexe : section 2.2.2.
- Source : KANSO B2002600, p. 1, et décision D-029.
- Gravité : MINEURE.
- Correction proposée : « For modelling, the project assumes the air-free composition of the analysed sample. »

### E-3. Projection après pré-tri formulée comme un résultat

- Annexe : section 2.2.3.
- Source : rapport Chiba, p. 27, et décision D-035.
- Gravité : MINEURE.
- Correction proposée : remplacer « is the yield » par « is used as the working yield, after pre-sorting, under D-035 ».

### E-4. Confiance de 95 % sur des calculs dépendant de D-033 ou D-034

- Annexe : fiches 2.5.a.19, 2.5.b.8, 2.5.f.7 et fiches liées.
- Source : fiche d'hypothèses 2.5.0, qui plafonne à 90 % les chiffres dépendants.
- Gravité : MINEURE.
- Correction proposée : plafonner à 90 % ou préciser que 95 % porte seulement sur l'arithmétique, pas sur la sélection des données.

### E-5. Arrondi et petits défauts de traçabilité

- Annexe : section 2.2.2 et fiches 2.5.f.7, 2.5.0, 2.1.g.
- Gravité : MINEURE.
- Correction proposée : 73,08 % à deux décimales ; générer les cinq liens de calcul ; qualifier la conversion volume-masse d'inférence.

## Autres interprétations

1. Exclure l'essai du 11 juillet peut paraître favorable ou défavorable selon l'indicateur. Il retire l'huile la plus haute, donc abaisse la moyenne d'huile de 74,28 % à 73,08 %. Il augmente en revanche la moyenne du gaz par différence. L'exclusion n'est donc pas une sélection destinée uniquement à embellir le rendement d'huile.
2. Garder les 11 essais donnerait le même ordre de grandeur et la même conclusion : les polyoléfines donnent couramment environ 70 % à 80 % d'huile dans ces essais en lots. La décision D-034 ne porte pas le résultat à elle seule.
3. Le ratio hors inertes peut raisonnablement servir de scénario après pré-tri si le tri enlève essentiellement verre et métaux. Si le tri perd des plastiques ou laisse des inertes, le rendement réel par tonne reçue sera entre la base brute et la base hors inertes. L'annexe montre déjà ces deux bornes.
4. Les 25 %, 5 % et 5 % de la brochure japonaise peuvent être des parts volumiques cohérentes avec les volumes indiqués. Cette lecture est plus solide que leur interprétation comme parts massiques, mais elle ne fournit pas un bilan massique industriel.
5. Les décisions D-029, D-033 à D-035 et D-038 sont identifiées comme hypothèses ou conventions. Aucune n'est manifestement déraisonnable dans un cas standard si son périmètre reste visible. D-035 et la base masse/volume de la brochure doivent être confirmées avant dimensionnement contractuel.

## Les cinq points les plus graves

1. IMPORTANTE : base masse/volume non définie pour le bilan japonais à 10 % de résines.
2. MINEURE : transfert de la composition d'un seul gaz analysé présenté trop catégoriquement dans le texte principal.
3. MINEURE : rendement hors inertes formulé comme rendement après pré-tri plutôt que comme hypothèse.
4. MINEURE : confiance de 95 % non cohérente avec le plafond de 90 % des hypothèses D-033 et D-034.
5. MINEURE : arrondi 73,07 % au lieu de 73,08 % et petits défauts de traçabilité.

## Manques évidents avant investissement

| Point à obtenir | Gravité avant décision d'investissement | Pourquoi |
|---|---|---|
| Essai continu sur la charge cible, avec bilan massique complet et durée représentative | BLOQUANT avant engagement industriel | Les résultats actuels viennent surtout de lots de 20 à 60 kg et ne garantissent ni le débit, ni le rendement, ni la stabilité du procédé continu sur la charge achetée. |
| Garanties contractuelles de débit, disponibilité, rendements, consommations et qualité des produits | BLOQUANT avant commande ferme | Les brochures et décisions de modèle ne remplacent pas des critères d'acceptation mesurables et des recours contractuels. |

Ces deux manques ne rendent pas la plausibilité technique impossible. Ils empêchent de traiter les performances industrielles comme garanties avant investissement.

## Conclusion en langage simple

**PASSE pour la conclusion du lot 1, sous conditions.** Les essais en lots soutiennent un rendement d'huile d'environ 70 % à 80 % sur PE et PP et l'ordre de grandeur de 73,1 % reste correct. Aucune réserve R-1 à R-5 ne crée un blocage dans un cas standard.

**NE PASSE PAS comme bilan massique établi :** les 25 %, 5 % et 5 % de la brochure japonaise n'ont pas de base masse/volume définie.

**POSSIBLE SOUS CONDITIONS :** appliquer les rendements hors inertes après pré-tri, à condition que le tri retire les mêmes inertes sans perte significative de matière convertible.

**À MESURER OU CONFIRMER :** essai continu sur la charge cible, bilan massique complet, composition du gaz sur cette charge et garanties contractuelles de performance.

## Ce qui n'a pas été vérifié dans ce lot

- Sections 2.4 à 2.10 : hors périmètre, prévues dans les lots 2 et 3.
- Pouvoir calorifique de 37,4 MJ/kg et autosuffisance : décisions D-038 et D-029, non recalculées ici ; leur présentation sera appréciée dans les lots 2 et 3.
- Performance réelle du pré-tri : aucune campagne du pré-tri projeté n'est versée au dossier.
- Performance continue de l'URC-2000 sur la charge cible : aucune pièce de test comparable n'est versée au dossier.

## Décompte

9 verdicts :

- CONFIRMÉ : 4
- DIFFÉRENT : 0
- ABSENT : 4
- INACCESSIBLE : 0
- NON SOURCÉ : 0
- CALCUL FAUX : 1

Gravité des écarts : 0 BLOQUANT dans l'annexe actuelle, 1 IMPORTANT, 4 MINEURS.

## Échantillon automatique de trois affirmations à faire contrôler par Stéphane

Le tirage reproductible du contrôle automatique, graine 20261125, a donné :

1. Rendements PE et PP de 73 % à 81 %, rapport Chiba, PDF p. 19 à 23.
2. Tableau OneWorld p. 16 : quantités totalisant 102 t pour une entrée imprimée de 200 t.
3. Réutilisation d'une partie de l'eau purifiée dans la chaudière, déclaration OneWorld.

