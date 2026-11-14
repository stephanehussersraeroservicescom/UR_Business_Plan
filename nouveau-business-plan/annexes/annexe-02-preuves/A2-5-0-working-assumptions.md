# Annex 2.5.0. Working assumptions

[Back to Annex 2](../ANNEX-02-Technical-Evidence.md) · [Index of evidence files](README.md)

These assumptions were decided by the project sponsor, Stéphane Husser, and are recorded as dated decisions in the project decision register (`working-folder/params/_decisions.yaml`). A figure that depends on one of them carries a confidence of 90 % at most [hyp:D-022].

### D-016

Decision of 14 October 2026 [hyp:D-016]. OneWorld's own documents (brochures, presentations, reports, e-mails) are admitted as evidence when they are cited with a page or a date. They are always attributed ("according to OneWorld"). Each statement without a measurement report gives rise to a request to OneWorld.

### D-020

Decision of 14 October 2026 [hyp:D-020]. OneWorld's documentation is the design basis of the URC-2000. The annex shows each test in a table, adds the gas to the oil as fuel, gives municipal yields on the convertible fraction, and compares emissions with the current EU limits and the best-available-technique levels.

### D-021

Decision of 14 October 2026 [hyp:D-021].

1. **Gas.** The off-gas is sampled at the outlet, mixed with air. Oxygen and nitrogen come from the air, not from the plastic. Everything that does not leave the reactor as oil, char or metal is counted as pyrolysis gas with the composition of analysis B2002600, from hydrogen to carbon dioxide ([Annex 2.2.f](A2-2-f-kanso-gas-analysis-2020.md)). Its net calorific value is the weighted average of its components' values ([Annex 2.5.c](A2-5-c-calc-gas-calorific-value.md)). Updated by D-038: the oxygen and nitrogen of the KANSO sample come from the air added at sampling (taken at the pipe outlet, without a stated protocol), not from the feed; the gas produced by the feed therefore carries 37.4 MJ/kg, and the dilution does not change the energy per tonne [hyp:D-038].
2. **Char.** Replaced by D-038: two values by feed. Char from plastic residues, including the two Noda runs: 24.6 MJ/kg, the factor of the Chiba balances (5,880 kcal/kg, PDF p. 41 and 42) [CHIBA-BILANS] [hyp:D-038]. Char from household waste: 32.09 MJ/kg, measured by Izumitec on a urethane char [IZUMITEC-R35-339439], a working assumption of the sponsor [hyp:D-038].
3. **Oil.** The oil is taken at 46,000 J/g, the gross value calculated by the Japan Lubricating Oil Society ([Annex 2.2.a](A2-2-a-jlos-oil-analyses.md)) [CHIBA-JLOS-HUILES].
4. **Batch tests.** They provide conversion coefficients and product qualities only. A small batch reactor heated for each run does not represent the consumption of a continuous plant, so no energy balance is drawn from them.
5. **Continuous plant.** The energy balance of the URC-2000 uses OneWorld's figures, taken as correct: burner of 833 kcal/s, fuel of 10,000 L/day (upper value), electricity of 600 kW ([Annex 2.3.a](A2-3-a-oneworld-urc2000-brochure.md), [Annex 2.3.c](A2-3-c-oneworld-energy-table.md)) [UR2000-JP-P08-SPEC] [OW-CONSO-ENERGIE]. The choice of 600 kW rather than the 20 kW of the brochure is to be confirmed.

### D-024

Decision of 15 October 2026 [hyp:D-024]. At the sponsor's request, the GC-MS peak area shares of the "drain" sample are taken as mass shares, to give a low and a high estimate of the share of the sample in the jet fuel carbon range (Annex 2.4.3). This working assumption was set by Claude and is not verified: the detector response differs between compounds. The result is an order of magnitude, before treatment, and is not used in the financial model.

### D-029

Decision of 15 October 2026 [hyp:D-029], after point E-1 of the external check. The gas of the Chiba runs is not measured: it is the input minus the oil and the solid residue (operator definition, Chiba report p. 27). For a dry plastic this balance is essentially gas; for municipal feeds it also includes the moisture of the waste.

1. **Gas from plastic.** Working assumption set by the sponsor (prudent choice, close to the lowest values observed): the gas produced by plastic is taken at 10 % of the plastic input. [hyp:D-029] The sponsor's reasoning, also an assumption: the water condenses in the separator, the dry gas is reinjected, and its composition is close to the analysed gas without air (D-021). The uncertainty lies in the quantity, not the composition. For household waste with 10 % plastic, this gives about 1 % of the input as gas from plastic, plus an unknown share from organic matter; no Urban Rig test covers these materials (R-021). [hyp:D-029] Gas by difference on the 10 pure plastic runs retained (D-034): weighted mean 16.25 %, simple mean 16.84 %, median 18.15 %, range 6.75 % to 24.5 % [calc:CALC-A2-GAZDIFF10-MOY-POND] [calc:CALC-A2-GAZDIFF10-MOY-SIMPLE] [calc:CALC-A2-GAZDIFF10-MEDIANE] [calc:CALC-A2-GAZDIFF10-MIN] [calc:CALC-A2-GAZDIFF-MAX].
2. **No self-sufficiency claim on household or municipal waste.** OneWorld's statement that the plant needs no fuel after start-up is cited as a manufacturer statement, illustrated on a feed of 90 % resins [OW-ENG-P16-BILAN] [hyp:D-029]. The energy balance of household waste will be built in Annex 5, with declared assumptions.
3. **Wording.** "Conversion to fuel" becomes "oil + gas by difference", with a reservation on moisture for the two municipal runs, which were made on separately collected plastic packaging and on non-combustible residue, not on raw household waste.
4. **Scope, specified by the sponsor on 15 October 2026.** Pure resin feeds keep their previous treatment: their products (oils, char, gas) are known and the gas covers the heat demand as calculated (D-021). Only the confidence in self-sufficiency on household waste is withdrawn. Decisions D-026 and D-028 are kept; their heat balance will be calculated according to the feed chosen [hyp:D-029].

### D-033

Decision of 15 October 2026 [hyp:D-033]. For the Noda run of 9 September 2022, page 42 of the Chiba report (mass balance) is used rather than page 26 (test sheet): char 10.5 kg, metals and foreign matter 13.9 kg; process water of both Noda runs: 100 L in, 73 L discharged and 27 L evaporated on 9 September, 85 L and 15 L on 15 September [CHIBA-BILANS]. The printed oil mass of 16.1 kg is kept; it was measured by dipstick, not weighed [CHIBA-PROCEDE-HUILE].

### D-034

Decision of 15 October 2026 [hyp:D-034]. The mixed-plastic run of 11 July 2022 is excluded from the averages: unconverted pieces in the residue (photo, PDF p. 24) and the lowest gas with the highest oil yield of the 11 runs [CHIBA-ESSAIS-FICHES]. The pure plastic statistics use 10 runs.

### D-035

Decision of 15 October 2026 [hyp:D-035]. Reactor capacity 200 m³ per day; feed mass = volume x 0.7 t/m³ = 140 t per day, a working assumption of the sponsor (a press brings the sorted feed back to 0.7), variable in the model. Tonnage received = reactor tonnage / mass share kept after sorting; inert matter has a zero yield. The yield excluding metals and foreign matter recovered after treatment is the yield of the reactor feed after pre-sorting. OneWorld's daily table (English brochure p. 16) counts 1 L as 1 kg; it is corrected in Section 2.8 at 200 m³ x 0.6 t/m³ = 120 t per day [OW-ENG-P16-BILAN].

### D-036

Decision of 15 October 2026 [hyp:D-036]. The model starts from the batch yields, without a bonus for continuous operation. According to the project team, internal tests in continuous operation have shown higher yields; these data are not yet in this dossier.

### D-037

Decision of 15 October 2026 [hyp:D-037]. Shredder residue is excluded from the business plan, on the judgement of the Chiba report (PDF p. 1 note ※3 and p. 43) [CHIBA-RAPPORT-2023].

### D-038

Decision of 15 October 2026 [hyp:D-038]. Gas kept at 37.4 MJ/kg (see D-021, item 1). Char at two values by feed (see D-021, item 2). Burner coverage on pure plastic shown on two lines: OneWorld's example with 11.5 % gas and a working assumption of 15 % gas, a rounded value of the measured means set by the sponsor. Household waste: no self-sufficiency claimed (D-029). The Chiba factor of 1,323.8 kcal/kg for the off-gas is not used (origin unknown, R-011).
