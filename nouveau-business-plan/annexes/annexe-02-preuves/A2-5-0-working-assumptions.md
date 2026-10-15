# Annex 2.5.0. Working assumptions

[Back to Annex 2](../ANNEX-02-Technical-Evidence.md) · [Index of evidence files](README.md)

These assumptions were decided by the project sponsor, Stéphane Husser, and are recorded as dated decisions in the project decision register (`working-folder/params/_decisions.yaml`). A figure that depends on one of them carries a confidence of 90 % at most [hyp:D-022].

### D-016

Decision of 14 October 2026 [hyp:D-016]. OneWorld's own documents (brochures, presentations, reports, e-mails) are admitted as evidence when they are cited with a page or a date. They are always attributed ("according to OneWorld"). Each statement without a measurement report gives rise to a request to OneWorld.

### D-020

Decision of 14 October 2026 [hyp:D-020]. OneWorld's documentation is the design basis of the URC-2000. The annex shows each test in a table, adds the gas to the oil as fuel, gives municipal yields on the convertible fraction, and compares emissions with the current EU limits and the best-available-technique levels.

### D-021

Decision of 14 October 2026 [hyp:D-021].

1. **Gas.** The off-gas is sampled at the outlet, mixed with air. Oxygen and nitrogen come from the air, not from the plastic. Everything that does not leave the reactor as oil, char or metal is counted as pyrolysis gas with the composition of analysis B2002600, from hydrogen to carbon dioxide ([Annex 2.2.f](A2-2-f-kanso-gas-analysis-2020.md)). Its net calorific value is the weighted average of its components' values ([Annex 2.5.c](A2-5-c-calc-gas-calorific-value.md)).
2. **Char.** The calorific value measured by Izumitec, 32,090 J/g, is used for Urban Rig char ([Annex 2.2.j](A2-2-j-izumitec-char-oil.md)) [IZUMITEC-R35-339439].
3. **Oil.** The oil is taken at 46,000 J/g, the gross value calculated by the Japan Lubricating Oil Society ([Annex 2.2.a](A2-2-a-jlos-oil-analyses.md)) [CHIBA-JLOS-HUILES].
4. **Batch tests.** They provide conversion coefficients and product qualities only. A small batch reactor heated for each run does not represent the consumption of a continuous plant, so no energy balance is drawn from them.
5. **Continuous plant.** The energy balance of the URC-2000 uses OneWorld's figures, taken as correct: burner of 833 kcal/s, fuel of 10,000 L/day (upper value), electricity of 600 kW ([Annex 2.3.a](A2-3-a-oneworld-urc2000-brochure.md), [Annex 2.3.c](A2-3-c-oneworld-energy-table.md)) [UR2000-JP-P08-SPEC] [OW-CONSO-ENERGIE]. The choice of 600 kW rather than the 20 kW of the brochure is to be confirmed.

### D-024

Decision of 15 October 2026 [hyp:D-024]. At the sponsor's request, the GC-MS peak area shares of the "drain" sample are taken as mass shares, to give a low and a high estimate of the share of the sample in the jet fuel carbon range (Annex 2.4.3). This working assumption was set by Claude and is not verified: the detector response differs between compounds. The result is an order of magnitude, before treatment, and is not used in the financial model.
