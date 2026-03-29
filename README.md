# Africa RCT E156 Portfolio

This umbrella repo ties together the four topic-specific public repos generated from the Africa-site ClinicalTrials.gov scan. All four active paper releases use strict E156 format: one validated 156-word body plus companion artifacts.

## Headline

Across the four scanned domains, malaria is the strongest starting point if the goal is to identify Africa-relevant RCT patterns that look more transferable to cheaper and faster delivery.

## Start Here

- Open `index.html` for the visual landing page.
- Read [`TOPIC_MATRIX.md`](TOPIC_MATRIX.md) for the side-by-side comparison.
- If you want the strongest first example set, start with `malaria-e156`.
- If you want the underlying cross-topic narrative, read `data/topic_comparison.md`.

## Included Topic Repos

- [`malaria-e156`](https://github.com/mahmood726-cyber/malaria-e156): strongest shortlist signal, broadest African country spread
- [`hiv-e156`](https://github.com/mahmood726-cyber/hiv-e156): useful lean designs, but more concentrated in established infrastructure hubs
- [`hypertension-e156`](https://github.com/mahmood726-cyber/hypertension-e156): weakest shortlist signal and longest Africa-side durations in this set
- [`maternal-health-e156`](https://github.com/mahmood726-cyber/maternal-health-e156): smaller but still useful pregnancy-related shortlist

## Active Release Model

- each topic repo has a validated `156`-word E156 body
- note blocks, metadata, and HTML companions sit outside the fixed body length
- long-form journal expansion is deferred unless explicitly requested

## Portfolio Snapshot

- `malaria`: `27/80` shortlist studies, proportion `0.34`, 95% CI `0.24 to 0.45`
- `hiv`: `18/80` shortlist studies, proportion `0.23`, 95% CI `0.15 to 0.33`
- `hypertension`: `8/65` shortlist studies, proportion `0.12`, 95% CI `0.06 to 0.22`
- `maternal health`: `12/80` shortlist studies, proportion `0.15`, 95% CI `0.09 to 0.24`

## How To Use This Portfolio

- Use the E156 body in each topic repo for the compact publication unit.
- Use the topic repo `paper/index.html` file for the richer interactive companion.
- Use the repo `data/` and `code/` folders if you want to inspect or extend the benchmark.
- Use `MANIFEST.json` if you want machine-readable repo paths, URLs, and headline metrics.

## Regeneration

- `index.html` and `TOPIC_MATRIX.md` are generated from `MANIFEST.json`.
- Rebuild them with `python3 scripts/render_portfolio_assets.py`.

## Included Portfolio Files

- `index.html`: visual landing page and repo entry point
- `TOPIC_MATRIX.md`: side-by-side topic snapshot
- `data/topic_comparison.md`: copied comparison note
- `MANIFEST.json`: local repo paths and key metrics
- `data/malaria_deep_dive_summary.md`: malaria-only deeper operational and leadership readout
