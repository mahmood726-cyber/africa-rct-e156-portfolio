# Malaria Deep Dive

This malaria-first layer adds two things on top of the existing benchmark:

- structured primary-outcome signal extraction from `resultsSection`
- a cautious leadership heuristic using sponsor names, investigator affiliations, and African site institutions

## Coverage

- Africa malaria benchmark studies: 80
- Transfer shortlist studies: 27
- Studies with structured primary analyses: 32
- Studies with primary p-values: 22
- Studies with primary effect estimates or CIs: 28

## Leadership Heuristic

- All studies: likely_externally_run (69), mixed_local_site_with_external_sponsor (11)
- Transfer shortlist only: likely_externally_run (22), mixed_local_site_with_external_sponsor (5)

These leadership labels are heuristics, not definitive authorship or funding adjudications.

## Primary Signal Buckets

- no_primary_analysis_structured (48), effect_estimate_no_significance (18), effect_estimate_with_significance (10), analysis_reported_no_numeric_signal (3), significant_pvalue_only (1)

## What Looks Most Transferable

- The strongest malaria pattern remains single-country, often single-site trials with moderate enrollment.
- Countries most represented among the top local-or-mixed candidates: Mali (4), South Africa (2), Uganda (2), Burkina Faso (2), Tanzania (1)
- Local or mixed leadership gives a better template for African delivery models than lean but clearly external sponsor-led studies.

## Top Likely Local Candidates

- none identified

## Top Local-Or-Mixed Candidates

- NCT05930782: Piperaquine Granule Formulation Relative Bioavailability and Food Effect Study in Healthy Volunteers. | mixed_local_site_with_external_sponsor | Tanzania | priority 72.44
- NCT04940130: PfSPZ Vaccine Trial in Malian Children | mixed_local_site_with_external_sponsor | Mali | priority 65.53
- NCT00460525: Phase II AMA-1 Malaria Vaccine FMP2.1/AS02A Trial in Mali | mixed_local_site_with_external_sponsor | Mali | priority 62.54
- NCT02118428: Clinical and Biological Efficacy of Mirasol-treated Fresh Whole Blood for the Prevention of Transfusion-transmitted Malaria | mixed_local_site_with_external_sponsor | Ghana | priority 49.47
- NCT02230579: Phase I Study of Ascending Doses of MMV390048 in Healthy Adult Volunteers | mixed_local_site_with_external_sponsor | South Africa | priority 47.09
- NCT04532931: Four Different Experimental Drug Regimens to Standard of Care for the Treatment of Symptomatic Outpatients With COVID-19 | mixed_local_site_with_external_sponsor | South Africa | priority 45.7
- NCT00349713: FMP2.1/AS02A: Rabies Vaccine Malaria-Experienced Adults in Bandiagara, Mali | mixed_local_site_with_external_sponsor | Mali | priority 41.61
- NCT04566510: LLIN Evaluation in Uganda Project | mixed_local_site_with_external_sponsor | Uganda | priority 39.97
- NCT04336189: Optimal Chemopreventive Regimens to Prevent Malaria and Improve Birth Outcomes in Uganda | mixed_local_site_with_external_sponsor | Uganda | priority 38.77
- NCT03676764: Community Health Azithromycin Trial in Burkina Faso | mixed_local_site_with_external_sponsor | Burkina Faso | priority 37.13

## Caveat

A statistically significant primary result is not the same as real-world effectiveness, and the leadership split is an inference from registry metadata.
