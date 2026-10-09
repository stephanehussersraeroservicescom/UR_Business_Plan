// Port JavaScript du moteur de calcul.
// Doit produire exactement les memes resultats que engine/modele.py.
// Le rapport HTML verifie cette egalite au chargement et affiche un bandeau rouge si elle est rompue.

function calculer(P) {
  const v = k => P[k].valeur;
  const R = {};
  const set = (cle, valeur, unite, depend) => { R[cle] = { valeur, unite, depend }; return valeur; };

  const n = v('nb_unites'), j = v('jours_exploitation');
  const debit = v('capacite_volumetrique') * v('densite_dechet');
  set('debit_massique', debit, 'T/j', ['capacite_volumetrique', 'densite_dechet']);
  const tonnage = debit * j * n;
  set('tonnage_annuel', tonnage, 'T/an',
      ['capacite_volumetrique', 'densite_dechet', 'jours_exploitation', 'nb_unites']);

  const net = debit * 1000 * (1 - v('taux_refus'));
  const plast = net * v('part_plastique'), org = net * v('part_organique');
  const met = net * v('part_metaux'), verre = net * v('part_verre');
  const inert = net * v('part_inertes');

  const huileReac = plast * v('rdt_huile_plastique') * j / 1000 * n;
  const gazP = plast * v('rdt_gaz_plastique');
  const resP = plast * v('rdt_residu_plastique');
  const charO = org * v('rdt_char_organique');
  const gazO = org - charO;

  const eau = net * v('part_humidite') * j / 1000 * n;
  const orgDec = eau * v('part_organique_eau');
  const orgRec = orgDec * v('part_organique_recyclee');
  const huileRec = orgRec * v('rdt_huile_recyclage');

  set('huile', huileReac + huileRec, 'T/an',
      ['part_plastique', 'rdt_huile_plastique', 'jours_exploitation', 'nb_unites',
       'part_organique_recyclee', 'rdt_huile_recyclage']);
  set('char', (charO + resP) * v('criblage_char') * j / 1000 * n, 'T/an',
      ['part_organique', 'rdt_char_organique', 'rdt_residu_plastique', 'criblage_char']);
  set('ferreux', met * v('part_ferreux') * v('rec_ferreux') * j / 1000 * n, 'T/an',
      ['part_metaux', 'part_ferreux', 'rec_ferreux']);
  set('aluminium', met * v('part_alu') * v('rec_alu') * j / 1000 * n, 'T/an',
      ['part_metaux', 'part_alu', 'rec_alu']);
  set('autres_metaux', met * (1 - v('part_ferreux') - v('part_alu')) * v('rec_metaux_char') * j / 1000 * n,
      'T/an', ['part_metaux', 'rec_metaux_char']);
  set('verre', verre * v('rec_verre') * j / 1000 * n, 'T/an', ['part_verre', 'rec_verre']);
  set('eau_procede', eau, 'T/an', ['part_humidite']);
  set('phase_organique_decantee', orgDec, 'T/an', ['part_organique_eau']);
  set('eau_douce', (eau - orgDec) * v('rendement_eau_seacoral'), 'T/an', ['rendement_eau_seacoral']);
  set('concentrat', (eau - orgDec) * (1 - v('rendement_eau_seacoral')), 'T/an', ['rendement_eau_seacoral']);
  set('residus',
      (orgDec - orgRec)
      + (net * v('taux_refus') / (1 - v('taux_refus'))
         + (charO + resP) * (1 - v('criblage_char'))
         + verre * (1 - v('rec_verre')) + inert) * j / 1000 * n,
      'T/an', ['taux_refus', 'criblage_char', 'rec_verre', 'part_inertes']);

  // ---- energie
  const dispo = gazP * v('pci_gaz_plastique') + gazO * v('pci_gaz_organique');
  const utile = dispo * v('rendement_bruleur');
  const besoin = v('capacite_volumetrique') * v('densite_dechet') * v('besoin_thermique');
  set('energie_gaz_disponible', dispo, 'MJ/j',
      ['pci_gaz_plastique', 'pci_gaz_organique', 'rdt_gaz_plastique', 'rdt_char_organique']);
  set('couverture_thermique', utile / besoin, 'fraction',
      ['pci_gaz_plastique', 'pci_gaz_organique', 'rendement_bruleur', 'besoin_thermique']);
  const deficit = Math.max(0, besoin - utile);
  const fioul = (deficit + v('provision_fioul_secours') * besoin) / v('pci_fioul') / v('rendement_bruleur');
  set('fioul_litres_jour', fioul, 'L/j', ['provision_fioul_secours', 'pci_fioul', 'besoin_thermique']);
  set('fioul_annuel', fioul * j * n, 'L/an', ['jours_exploitation', 'nb_unites']);
  set('energie_exportee', R.huile.valeur * v('pci_huile_gj') + R.char.valeur * v('pci_char'),
      'GJ/an', ['pci_huile_gj', 'pci_char']);

  // ---- capex
  const eq = ['machine', 'installation', 'fret', 'formation', 'pieces',
              'pre_tri', 'post_tri', 'atex', 'decanteur'].reduce((s, k) => s + v(k), 0) * n;
  const sUs = Math.max(2600, v('surface_usine_1') + v('surface_usine_d') * (n - 1)) * n;
  const sSd = (v('surface_stock_dechets_1') + v('surface_stock_dechets_d') * (n - 1)) * n;
  const sSp = Math.max(600, v('surface_stock_produits_1') + v('surface_stock_produits_d') * (n - 1)) * n;
  const sBu = Math.max(64, v('surface_bureaux_1') + v('surface_bureaux_d') * (n - 1)) * n;
  const bat = sUs * v('prix_usine') + (sSd + sSp) * v('prix_stockage') + sBu * v('prix_bureaux')
              + v('vrd_base') + v('vrd_par_unite') * (n - 1);
  const ing = v('ingenierie_base') * (1 + v('ingenierie_step') * (n - 1));
  const aleas = v('taux_aleas') * (eq + bat);
  set('surface_batie', sUs + sSd + sSp + sBu, 'm2',
      ['surface_usine_1', 'surface_stock_dechets_1', 'surface_stock_produits_1', 'surface_bureaux_1']);
  set('capex_equipement', eq, 'EUR', ['machine', 'pre_tri', 'post_tri', 'atex', 'decanteur']);
  set('capex_genie_civil', bat, 'EUR', ['prix_usine', 'prix_stockage', 'prix_bureaux', 'vrd_base']);
  const capex = eq + bat + ing + aleas;
  set('capex_total', capex, 'EUR', ['taux_aleas', 'ingenierie_base']);
  set('capex_par_tonne_an', capex / tonnage, 'EUR/T-an', []);
  const amort = capex / v('duree_amortissement');
  set('amortissement_annuel', amort, 'EUR/an', ['duree_amortissement']);
  const dette = capex * v('part_dette');
  set('dette', dette, 'EUR', ['part_dette']);
  set('fonds_propres', capex * (1 - v('part_dette')), 'EUR', ['part_dette']);

  // ---- compte de resultat
  const prixHuile = v('qualite_huile') === 'craqueur' ? v('prix_huile_craqueur') : v('prix_huile_combustible');
  const tauxMaint = an => {
    const a1 = v('maintenance_an_bas'), a2 = v('maintenance_an_haut');
    const lo = v('maintenance_bas'), hi = v('maintenance_haut');
    if (an <= a1) return lo;
    if (an >= a2) return hi;
    return lo + (hi - lo) * (an - a1) / (a2 - a1);
  };
  const pl = [];
  let cum = 0;
  for (let an = 1; an <= v('horizon'); an++) {
    const u = an === 1 ? v('charge_an1') : (an === 2 ? v('charge_an2') : 1.0);
    const inf = Math.pow(1 + v('inflation'), an - 1);
    const rec = {
      gate_fees: tonnage * u * v('gate_fee') * inf,
      huile: R.huile.valeur * u * prixHuile * inf,
      char: R.char.valeur * u * v('prix_char') * inf,
      metaux: (R.ferreux.valeur * v('prix_ferreux') + R.aluminium.valeur * v('prix_alu')
               + R.autres_metaux.valeur * v('prix_autres_metaux')) * u * inf,
      verre: R.verre.valeur * u * v('prix_verre') * inf,
      carbone: tonnage * u * v('reduction_carbone_certifiee') * v('prix_carbone') * inf,
    };
    const ch = {
      personnel: (v('etp_coeur_base') + v('etp_coeur_step') * (n - 1) + v('etp_tri') * n)
                 * v('cout_etp') * u * inf,
      maintenance: tauxMaint(an) * eq * u * inf,
      electricite: v('elec_par_unite') * n * j * v('prix_elec') * u * inf,
      fioul_secours: R.fioul_annuel.valeur * v('prix_fioul') * u * inf,
      elimination_residus: R.residus.valeur * v('cout_elimination') * u * inf,
      carbonate: tonnage * v('conso_carbonate') / 1000 * v('prix_carbonate') * u * inf,
      concentrat: R.concentrat.valeur * v('cout_concentrat') * u * inf,
      couche_catalytique: v('couche_catalytique') * n * u * inf,
      ceramique_seacoral: v('ceramique_seacoral') * n * inf,
      charbon_actif: v('charbon_actif') * n * u * inf,
      assurance: v('assurance') * capex * inf,
      provision_divers: v('provision') * capex * u * inf,
    };
    const recettes = Object.values(rec).reduce((a, b) => a + b, 0);
    const charges = Object.values(ch).reduce((a, b) => a + b, 0);
    const ebitda = recettes - charges;
    const dep = an <= v('duree_amortissement') ? amort : 0;
    const solde = an <= v('duree_pret') ? Math.max(0, dette * (1 - (an - 1) / v('duree_pret'))) : 0;
    const interets = solde * v('taux_interet');
    const ebt = ebitda - dep - interets;
    const impot = Math.max(0, ebt) * v('impot_societes');
    const principal = an <= v('duree_pret') ? dette / v('duree_pret') : 0;
    const fcf = ebitda - impot - principal;
    cum += fcf;
    const l = { annee: an, charge: u, tonnage: tonnage * u, recettes, charges, ebitda,
                marge: ebitda / recettes, amortissement: -dep, interets: -interets,
                resultat_avant_impot: ebt, impot: -impot, resultat_net: ebt - impot,
                flux_libre: fcf, flux_cumule: cum };
    for (const k in rec) l['rec_' + k] = rec[k];
    for (const k in ch) l['ch_' + k] = ch[k];
    pl.push(l);
  }
  const an3 = pl[2];
  set('ebitda_an3', an3.ebitda, 'EUR/an', ['gate_fee', 'prix_huile_craqueur', 'prix_char']);
  set('marge_ebitda_an3', an3.marge, 'fraction', []);
  set('gate_fee_equilibre',
      (an3.charges + amort - (an3.recettes - an3.rec_gate_fees)) / an3.tonnage, 'EUR/T', []);

  // ---- carbone
  const entrant = plast * v('teneur_c_plastique') * 3.667 * j / 1000 * n;
  const site = gazP * v('teneur_c_gaz') * 3.667 * j / 1000 * n
               + R.fioul_annuel.valeur * v('co2_fioul') / 1000;
  const aval = R.huile.valeur * v('co2_huile')
               + resP * v('criblage_char') * v('teneur_c_residu') * 3.667 * j / 1000 * n;
  const stocke = resP * (1 - v('criblage_char')) * v('teneur_c_residu') * 3.667 * j / 1000 * n;
  set('carbone_fossile_entrant', entrant, 'T CO2/an', ['teneur_c_plastique', 'part_plastique']);
  set('emissions_directes_site', site, 'T CO2/an', ['teneur_c_gaz', 'co2_fioul']);
  set('intensite_carbone_site', site / tonnage, 'T CO2/T', []);
  set('carbone_sortant_produits', aval, 'T CO2/an', ['co2_huile', 'teneur_c_residu']);
  set('carbone_stocke', stocke, 'T CO2/an', ['criblage_char']);
  set('ecart_bouclage_carbone', (site + aval + stocke) / entrant - 1, 'fraction', []);

  return { R, pl };
}

function gateFeeRequis(P, pl, R, annees) {
  const v = k => P[k].valeur;
  const capex = R.capex_total.valeur, amort = R.amortissement_annuel.valeur;
  const besoin = (capex - annees * v('impot_societes') * amort) / (1 - v('impot_societes'));
  let somme = 0, sens = 0;
  for (let i = 0; i < annees; i++) {
    somme += pl[i].ebitda;
    sens += pl[i].tonnage * Math.pow(1 + v('inflation'), i);
  }
  return v('gate_fee') + (besoin - somme) / sens;
}

if (typeof module !== 'undefined') module.exports = { calculer, gateFeeRequis };
