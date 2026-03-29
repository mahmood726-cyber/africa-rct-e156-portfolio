# Malaria Deep Dive

This malaria-first layer adds two analytical layers on top of the existing benchmark and applies a topical validation pass to remove obvious off-topic registry hits:

- structured primary-outcome signal extraction from `resultsSection`
- a cautious leadership heuristic using sponsor names, investigator affiliations, and African site institutions

## Coverage

- Registry benchmark studies loaded: 80
- Malaria-relevant studies after topical validation: 69
- Transfer shortlist studies after topical validation: 23
- Studies with structured primary analyses: 29
- Studies with primary p-values: 21
- Studies with primary effect estimates or CIs: 25

## Leadership Heuristic

- All studies: likely_externally_run (60), mixed_local_site_with_external_sponsor (9)
- Transfer shortlist only: likely_externally_run (19), mixed_local_site_with_external_sponsor (4)

These leadership labels are heuristics, not definitive authorship or funding adjudications.

## Primary Signal Buckets

- no_primary_analysis_structured (40), effect_estimate_no_significance (16), effect_estimate_with_significance (9), analysis_reported_no_numeric_signal (3), significant_pvalue_only (1)

## What Looks Most Transferable

- The strongest malaria pattern remains single-country, often single-site trials with moderate enrollment.
- Countries most represented among the top topical-validated local-or-mixed candidates: Mali (4), Uganda (2), Tanzania (1), Ghana (1), South Africa (1)
- Mixed local-site participation may be more operationally informative than clearly external sponsor-led studies, but the leadership split remains heuristic.

## Top Likely Local Candidates

- none identified

## Top Local-Or-Mixed Candidates

- NCT05930782: Piperaquine Granule Formulation Relative Bioavailability and Food Effect Study in Healthy Volunteers. | mixed_local_site_with_external_sponsor | Tanzania | priority 72.44
- NCT04940130: PfSPZ Vaccine Trial in Malian Children | mixed_local_site_with_external_sponsor | Mali | priority 65.53
- NCT00460525: Phase II AMA-1 Malaria Vaccine FMP2.1/AS02A Trial in Mali | mixed_local_site_with_external_sponsor | Mali | priority 62.54
- NCT02118428: Clinical and Biological Efficacy of Mirasol-treated Fresh Whole Blood for the Prevention of Transfusion-transmitted Malaria | mixed_local_site_with_external_sponsor | Ghana | priority 49.47
- NCT02230579: Phase I Study of Ascending Doses of MMV390048 in Healthy Adult Volunteers | mixed_local_site_with_external_sponsor | South Africa | priority 47.09
- NCT00349713: FMP2.1/AS02A: Rabies Vaccine Malaria-Experienced Adults in Bandiagara, Mali | mixed_local_site_with_external_sponsor | Mali | priority 41.61
- NCT04566510: LLIN Evaluation in Uganda Project | mixed_local_site_with_external_sponsor | Uganda | priority 39.97
- NCT04336189: Optimal Chemopreventive Regimens to Prevent Malaria and Improve Birth Outcomes in Uganda | mixed_local_site_with_external_sponsor | Uganda | priority 38.77
- NCT04319380: Seasonal Malaria Vaccination (RTS,S/AS01) and Seasonal Malaria Chemoprevention (SP/AQ) Extension Study | mixed_local_site_with_external_sponsor | Burkina Faso | Mali | priority 34.09

## Caveat

A statistically significant primary result is not the same as real-world effectiveness, the leadership split is an inference from registry metadata, and the deep-dive layer excludes obvious off-topic registry hits from the displayed candidate set.
