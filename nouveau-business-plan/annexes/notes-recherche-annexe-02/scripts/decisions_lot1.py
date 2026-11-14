import yaml
p='working-folder/params/_decisions.yaml'; s=open(p,encoding='utf-8').read()
for n in range(33,39): assert f'D-0{n}:' not in s, n
add='''

D-033:
  date: 2026-10-15
  titre: "Annexe 2, ecart E-3 : page 42 du rapport de Chiba retenue pour l'essai du 9/9/2022 et pour l'eau des essais de Noda"
  de: "fiche d'essai p. 26 : metaux et corps etrangers 10,5 kg, char 13,9 kg ; eau de drainage 52 L"
  vers: "bilan p. 42 : char (油化残渣) 10,5 kg, metaux et corps etrangers (金属・異物) 13,9 kg, residu total 24,4 kg inchange ; eau : 100 L en entree, 73 L rejetes et 27 L evapores le 9/9, 85 L rejetes et 15 L evapores le 15/9"
  unite: "kg ; L"
  motif: >
    Decision de Stephane du 15/10/2026 (registre ecarts-annexe-02.md, E-3). Motifs de Stephane : la page 42 est un bilan
    complet (entrees, produits, energie) ; elle attribue une energie au char et decompose l'eau. Les 52 L de 'drainage
    water' de la page 26 ne sont plus utilises (sens exact inconnu) ; les volumes evapores sont probablement calcules par
    difference. Objections gardees visibles : le rendement de 41 % imprime page 26 est calcule avec 10,5 kg de metaux ;
    l'energie du char page 42 vient d'un facteur fixe de 5 880 kcal/kg (R-012). Consequences : base hors metaux 36,1 kg ;
    huile 44,6 % ; gaz par difference 26,3 % ; huile + gaz 70,9 % ; char 21,0 % de l'entree ; metaux 27,8 % ; sur l'entree
    brute, rien ne change (huile 32,2 %, gaz 19,0 %). Autres incoherences (16 h 51) : 16,1 kg d'huile conserve, valeur
    imprimee (la p. 29 decrit un jaugeage apres decantation, pas une pesee) ; 250 ou 310 kg, non bloquant ; PP et PS
    inverses p. 43, sans effet, non mentionne ; bidons PE, 50 kg conserve. L'encadre 'incoherences de la source' ne garde
    que les ecarts entre p. 26 et p. 42.
  preuves: [CHIBA-BILANS, CHIBA-ESSAIS-FICHES]

D-034:
  date: 2026-10-15
  titre: "Annexe 2, ecart E-4 : essai 3P du 11/7/2022 ecarte des moyennes ; statistiques des plastiques purs sur 10 essais"
  de: "11 essais de plastiques purs ; deux essais 3P dits identiques"
  vers: "10 essais (400 kg) ; essai du 11/7 affiche et marque ecarte ; libelle du rapport (成型端材, chutes de produits moules) cite tel quel, avec la lecture de Stephane"
  unite: "%"
  motif: >
    Decision de Stephane du 15/10/2026 (registre E-4) : matieres differentes les deux jours (photos) ; selon Stephane,
    dechets plastiques en melange a proportions inconnues de PE, PP et PS, pas des chutes de moulage ; essai du 11/7
    ecarte des moyennes (reaction probablement incomplete). Motifs verifies par Claude : pieces fibreuses colorees non
    converties visibles dans le residu (photo p. 24) ; gaz le plus bas des 11 essais (2,2 %, contre 6,8 % au plus bas
    ailleurs) avec l'huile la plus haute (82,3 %), bilan douteux. Recalcul sur 10 essais : gaz 16,3 % pondere
    (CALC-A2-GAZDIFF10-MOY-POND), moyenne simple 16,8 %, mediane 18,2 %, de 6,8 a 24,5 % ; huile 73,1 % ; residu 10,7 %.
    D-029 (10 %) inchangee ; ses statistiques passent de 11 a 10 essais. Les calculs sur 11 essais restent pour la tracabilite.
  preuves: [CHIBA-ESSAIS-FICHES]

D-035:
  date: 2026-10-15
  titre: "Annexe 2, ecarts E-2 et E-6 : capacite volumique 200 m3/jour, charge du reacteur a 0,7 t/m3 (140 t/jour), base hors inertes, tableau OneWorld p. 16 corrige"
  de: "200 t/jour ; base hors metaux presentee comme rendement apres pre-tri ; tableau p. 16 a densite 1"
  vers: "capacite du reacteur 200 m3/jour ; masse = volume x 0,7 t/m3 = 140 t/jour (HYPOTHESE de Stephane) ; tonnage recu = tonnage du reacteur / part de masse conservee apres tri ; inertes a rendement nul ; tableau p. 16 recalcule par nous"
  unite: "m3/jour ; t/m3"
  motif: >
    Decisions de Stephane du 15/10/2026 (registre E-2 et E-6). E-2 : la base hors inertes est le bon rendement de la
    charge du reacteur apres pre-tri ; les inertes ne produisent ni huile ni gaz ; seul effet, la chaleur qu'ils absorbent.
    Tri imparfait : enterine. Inertes internes au plastique (fibres de verre ou de carbone, certaines charges minerales) :
    valorisables, non bloquant. Si le tri retire la moitie de la masse (verre, metal), on recoit 280 t/jour au lieu de 140
    pour remplir le reacteur. Ne pas complexifier : une presse remet la charge triee a 0,7 t/m3. Libelle 'excluding
    metals and foreign matter recovered after treatment' ; la base brute (32,2 % et 45,0 %) reste affichee.
    E-6 : masse entrante = 200 m3 par jour x masse volumique de la charge ; valeur moyenne 0,7 t/m3, soit 140 t/jour
    (HYPOTHESE de Stephane) ; variable dans la simulation. Le tableau p. 16 compte une densite de 1 (1 L = 1 kg) : erreur
    interne de OneWorld, deja signalee par Stephane ; tableaux non refaits malgre ses demandes ; c'est a nous de corriger.
    Choix de Stephane du 15/10/2026 (17 h) : refaire le tableau, pourcentages de OneWorld appliques a 200 m3 x 0,6 t/m3
    (densite de la brochure) = 120 t, volumes d'huile a 0,8642 kg/L (CALC-A2-OW16C-*). Le 0,7 est cite comme hypothese
    de Stephane, jamais par la feuille Lufthansa (D-025). Volume 200, 216 (48 bennes) ou 229,5 m3 (51 bennes) a confirmer
    (R-010) ; plafond 4,17 t par benne de 4,5 m3. Les 76,5 % d'huile restent une declaration de OneWorld sur une charge a
    90 % de resines. Regle les arbitrages capacite_volumetrique_annexe01 et densite_dechet_annexe01.
  preuves: [OW-ENG-P16-BILAN, UR2000-JP-P08-SPEC, CHIBA-ESSAIS-FICHES]

D-036:
  date: 2026-10-15
  titre: "Annexe 2, ecart E-7 : rendements des essais en lots comme hypothese de depart du modele, sans bonus pour le continu"
  de: "coefficients des lots appliques au continu sans mention"
  vers: "rendements des lots en hypothese de depart ; phrase attribuee a l'equipe projet sur les essais internes en continu (HYPOTHESE)"
  unite: "-"
  motif: >
    Decision de Stephane du 15/10/2026 (registre E-7) : tout ce qui a ete observe jusqu'ici en continu a eu un effet
    positif sur le rendement ; des essais restent a faire sur la meme base de comparaison. Formulation validee :
    'According to the project team, the internal tests carried out so far in continuous operation have shown higher
    yields than the batch tests. These data are not yet in this dossier. Tests on the same feed and the same basis of
    comparison remain to be done.' Le modele part des rendements des lots. Verser les donnees des essais internes quand
    elles seront disponibles.
  preuves: []

D-037:
  date: 2026-10-15
  titre: "Annexe 2, ecart E-9 : residus de broyage exclus du plan"
  de: "exclusion rattachee a D-017"
  vers: "exclusion explicite des residus de broyage, sur le jugement du rapport de Chiba"
  unite: "-"
  motif: >
    Decision de Stephane du 15/10/2026 (registre E-9), recommandations de Claude acceptees : residus de broyage exclus du
    plan. Rapport de Chiba, PDF p. 1 note ※3 et p. 43 : 生成油の性状が非常に悪く、油化処理には適さないと判断. Memes
    recommandations : '15 runs, 13 with measured oil' ; odeurs 2020 par Total Kankyo System pour KANSO ; specification
    '2019 (English brochure); Japanese brochure undated' ; PVC 'no quantified yield data' ; retrait de 'tres inferieurs aux
    VLE usuelles' (fiche KANSO-20002610).
  preuves: [CHIBA-RAPPORT-2023, CHIBA-ESSAIS-FICHES]

D-038:
  date: 2026-10-15
  titre: "Annexe 2, ecart E-10 : gaz a 37,4 MJ/kg confirme ; char a deux valeurs selon la charge ; couverture du bruleur sur plastique pur en deux lignes"
  de: "D-021 : char a 32 090 J/g pour toutes les charges ; couverture du bruleur sur le seul exemple OneWorld"
  vers: "gaz 37,4 MJ/kg ; char de residus plastiques 24,6 MJ/kg (facteur de Chiba, 5 880 kcal/kg) ; char de dechets menagers 32,09 MJ/kg (HYPOTHESE de Stephane) ; couverture du bruleur sur plastique pur : exemple OneWorld a 11,5 % de gaz et hypothese de 15 % de gaz"
  unite: "MJ/kg"
  motif: >
    Decisions de Stephane du 15/10/2026 (registre E-10). Gaz : on garde 37,4 MJ/kg (D-021). Raisonnement de Stephane :
    l'azote et l'oxygene de l'echantillon KANSO viennent de l'air ajoute au prelevement (pris a la sortie du tuyau, sans
    protocole) ; ils ne viennent pas de la charge ; en procede ferme, tres peu d'oxygene. Le gaz produit par la charge
    (masse par difference) porte donc 37,4 MJ/kg ; la dilution ne change pas l'energie par tonne. Valide par Claude, avec
    deux corrections sans effet sur la conclusion : la dilution de 4 a 5 fois est en volume (en masse, l'echantillon brut
    vaut 3,4 MJ/kg) ; on ne peut pas dire que l'echantillon de Chiba etait dilue dans les memes proportions. Le facteur de
    Chiba pour l'off-gas (1 323,8 kcal/kg, 5,5 MJ/kg) n'est pas utilise, origine inconnue (R-011).
    Char : deux valeurs. Char de residus plastiques : 24,6 MJ/kg (facteur de Chiba, 5 880 kcal/kg, PDF p. 41 et 42,
    origine inconnue, R-012) ; s'applique aussi aux deux essais de Noda (choix de Stephane du 15/10/2026, 17 h). Char de
    dechets menagers : 32,09 MJ/kg (Izumitec), HYPOTHESE de Stephane : la matiere organique, videe de son eau, agit en fin
    de pyrolyse comme une eponge dont les pores se remplissent d'hydrocarbures lourds ; la valeur Izumitec vient d'un char
    d'urethane ; cendres et mineraux, qui baissent le pouvoir calorifique, restent a mesurer (R-012).
    Couverture du bruleur (choix de Stephane du 15/10/2026, 17 h) : deux hypotheses a chaque fois, plastique pur et ordures
    menageres. Plastique pur : deux lignes, l'exemple OneWorld a 11,5 % de gaz (2,9 fois) et une HYPOTHESE de 15 % de gaz,
    arrondi de Stephane des moyennes mesurees par difference (14,4 % sur 11 essais, 16,3 % sur 10 essais), soit 3,7 fois
    (CALC-A2-COUV-BRULEUR-PLASTIQUE15). Ordures menageres : pas d'autosuffisance affirmee (D-029), bilan en annexe 5.
    Modifie D-021.
  preuves: [KANSO-B2002600, CHIBA-BILANS, IZUMITEC-R35-339439]
'''
s=s.rstrip('\n')+add
yaml.safe_load(s)
open(p,'w',encoding='utf-8').write(s+'\n'); print('ok')
