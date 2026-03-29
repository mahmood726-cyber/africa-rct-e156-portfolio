#!/usr/bin/env python3
"""Render the portfolio landing page and topic matrix from MANIFEST.json."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "MANIFEST.json"
INDEX_PATH = ROOT / "index.html"
MATRIX_PATH = ROOT / "TOPIC_MATRIX.md"

BADGES = [
    "Recommended First",
    "Second Pass",
    "Selective Use",
    "Lowest Priority",
]


def load_manifest() -> list[dict[str, Any]]:
    entries = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return sorted(entries, key=lambda entry: int(entry.get("portfolio_rank", 999)))


def topic_display(entry: dict[str, Any]) -> str:
    return str(entry["display"])


def topic_label(entry: dict[str, Any]) -> str:
    value = topic_display(entry)
    return value if value == "HIV" else value.title()


def card_summary(entry: dict[str, Any]) -> str:
    notes = {
        "malaria-e156": "Strongest shortlist signal and broadest African country spread under these registry-based proxy measures.",
        "hiv-e156": "Reusable smaller-footprint designs exist, but they are more concentrated in established infrastructure hubs.",
        "maternal-health-e156": "Smaller shortlist overall, but still contains lower-footprint pregnancy-related designs.",
        "hypertension-e156": "Weakest shortlist signal and longest Africa-side trial durations in this set.",
    }
    return notes[entry["repo"]]


def card_detail(entry: dict[str, Any]) -> str:
    details = {
        "malaria-e156": "Best first repo if the question is which domain shows the strongest proxy-based shortlist signal for smaller-footprint African trials.",
        "hiv-e156": "Useful if the aim is to study transfer patterns in settings with stronger lab and follow-up systems.",
        "maternal-health-e156": "Worth using when the delivery question is focused on maternal or pregnancy-related operations.",
        "hypertension-e156": "Best treated as a contrast case rather than a first-pass template for smaller-footprint African trial delivery.",
    }
    return details[entry["repo"]]


def matrix_readout(entry: dict[str, Any]) -> str:
    return {
        "malaria-e156": "strongest cross-topic shortlist signal and broad African spread",
        "hiv-e156": "reusable lean designs, but more dependent on established trial hubs",
        "hypertension-e156": "weakest shortlist signal and longest Africa-side durations",
        "maternal-health-e156": "smaller shortlist, but some useful lower-footprint designs",
    }[entry["repo"]]


def render_topic_cards(entries: list[dict[str, Any]]) -> str:
    chunks: list[str] = []
    for idx, entry in enumerate(entries):
        featured = " featured" if idx == 0 else ""
        badge = str(entry.get("portfolio_badge") or (BADGES[idx] if idx < len(BADGES) else "Portfolio Topic"))
        chunks.append(
            f"""          <a class="topic-card{featured}" href="{entry['public_url']}">
            <div class="topic-badge">{badge}</div>
            <h3>{topic_label(entry)}</h3>
            <p>{card_summary(entry)}</p>
            <div class="topic-stats">
              <div><strong>{entry['k']}/{entry['n']}</strong><span>shortlist</span></div>
              <div><strong>{entry['proportion']}</strong><span>proportion</span></div>
              <div><strong>{entry['median_duration_days']}</strong><span>median duration</span></div>
            </div>
            <p>{card_detail(entry)}</p>
            <span class="topic-link">Open repo</span>
          </a>"""
        )
    return "\n".join(chunks)


def render_snapshot(entries: list[dict[str, Any]]) -> str:
    return "\n".join(
        f"          <li><strong>{topic_label(entry)}</strong>: <code>{entry['k']}/{entry['n']}</code> shortlist studies, proportion <code>{entry['proportion']}</code>, 95% CI <code>{entry['ci']}</code></li>"
        for entry in entries
    )


def render_matrix(entries: list[dict[str, Any]]) -> str:
    lines = [
        "# Topic Matrix",
        "",
        "All four topic repos are maintained in strict `E156` release mode.",
        "",
        "| Repo | Public Repo | Topic | Benchmark N | Shortlist N | Proportion | 95% CI | Median Duration Days | Median Results Lag Days | Main Readout |",
        "|---|---|---|---:|---:|---:|---|---:|---:|---|",
    ]
    for entry in entries:
        lines.append(
            f"| `{entry['repo']}` | `{entry['public_url'].replace('https://github.com/', '')}` | {topic_label(entry)} | {entry['n']} | {entry['k']} | {entry['proportion']} | {entry['ci']} | {entry['median_duration_days']} | {entry['median_results_lag_days']} | {matrix_readout(entry)} |"
        )
    lines.extend(["", "## Reading Order", ""])
    lines.extend(f"{index}. `{entry['repo']}`" for index, entry in enumerate(entries, start=1))
    lines.extend(["", "_Generated from `MANIFEST.json` by `scripts/render_portfolio_assets.py`._"])
    return "\n".join(lines) + "\n"


def render_index(entries: list[dict[str, Any]]) -> str:
    featured = entries[0]
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Africa RCT E156 Portfolio</title>
  <meta name="description" content="A portfolio of four strict E156 micro-papers on Africa-site randomized trials, with malaria as the strongest first entry point under registry-based proxy measures for smaller-footprint, faster-reporting trial patterns.">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap');

    :root {{
      --bg: #f7f1e3;
      --bg-accent: #efe2bf;
      --surface: rgba(255, 252, 243, 0.92);
      --surface-strong: #fffaf0;
      --ink: #1f2d2a;
      --muted: #586a63;
      --line: rgba(31, 45, 42, 0.14);
      --teal: #1f7a72;
      --teal-deep: #0f5f58;
      --rust: #b7582c;
      --gold: #d7a93b;
      --shadow: 0 24px 70px rgba(32, 43, 39, 0.14);
      --radius: 24px;
      --max: 1180px;
    }}

    * {{
      box-sizing: border-box;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      margin: 0;
      color: var(--ink);
      font-family: "Source Serif 4", Georgia, serif;
      background:
        radial-gradient(circle at 15% 15%, rgba(215, 169, 59, 0.25), transparent 28%),
        radial-gradient(circle at 88% 12%, rgba(31, 122, 114, 0.18), transparent 26%),
        linear-gradient(180deg, #fbf7eb 0%, var(--bg) 42%, #f4edd8 100%);
    }}

    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(31, 45, 42, 0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(31, 45, 42, 0.025) 1px, transparent 1px);
      background-size: 28px 28px;
      pointer-events: none;
      z-index: -1;
    }}

    a {{
      color: inherit;
    }}

    .shell {{
      width: min(var(--max), calc(100% - 32px));
      margin: 0 auto;
    }}

    .hero {{
      padding: 28px 0 24px;
    }}

    .topbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 28px;
      padding: 14px 18px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: rgba(255, 252, 243, 0.72);
      backdrop-filter: blur(10px);
      box-shadow: 0 10px 28px rgba(32, 43, 39, 0.08);
    }}

    .eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.86rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--teal-deep);
    }}

    .eyebrow::before {{
      content: "";
      width: 12px;
      height: 12px;
      border-radius: 999px;
      background: linear-gradient(135deg, var(--gold), var(--rust));
      box-shadow: 0 0 0 6px rgba(215, 169, 59, 0.16);
    }}

    .topbar nav {{
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.92rem;
    }}

    .topbar nav a {{
      color: var(--muted);
      text-decoration: none;
    }}

    .topbar nav a:hover {{
      color: var(--teal-deep);
    }}

    a:focus-visible {{
      outline: 3px solid var(--rust);
      outline-offset: 3px;
    }}

    .hero-grid {{
      display: grid;
      grid-template-columns: minmax(0, 1.25fr) minmax(300px, 0.85fr);
      gap: 22px;
      align-items: stretch;
    }}

    .hero-copy,
    .hero-panel,
    .section-card,
    .topic-card,
    .callout {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      backdrop-filter: blur(10px);
    }}

    .hero-copy {{
      padding: 34px;
      position: relative;
      overflow: hidden;
    }}

    .hero-copy::after {{
      content: "";
      position: absolute;
      width: 220px;
      height: 220px;
      border-radius: 50%;
      right: -80px;
      bottom: -80px;
      background: radial-gradient(circle, rgba(31, 122, 114, 0.18), transparent 70%);
    }}

    h1, h2, h3 {{
      font-family: "Space Grotesk", sans-serif;
      line-height: 1.02;
      margin: 0;
    }}

    h1 {{
      font-size: clamp(2.8rem, 6vw, 5.6rem);
      letter-spacing: -0.05em;
      max-width: 11ch;
      margin-top: 20px;
    }}

    .lead {{
      font-size: clamp(1.08rem, 1.2vw, 1.24rem);
      line-height: 1.58;
      color: var(--muted);
      max-width: 62ch;
      margin: 18px 0 0;
    }}

    .hero-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 28px;
      position: relative;
      z-index: 1;
    }}

    .button {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      min-height: 48px;
      padding: 0 20px;
      border-radius: 999px;
      font-family: "Space Grotesk", sans-serif;
      font-weight: 700;
      text-decoration: none;
      transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
    }}

    .button:hover {{
      transform: translateY(-1px);
    }}

    .button-primary {{
      color: #fffaf3;
      background: linear-gradient(135deg, var(--teal), var(--teal-deep));
      box-shadow: 0 16px 34px rgba(15, 95, 88, 0.26);
    }}

    .button-secondary {{
      color: var(--ink);
      background: rgba(255, 250, 240, 0.84);
      border: 1px solid rgba(31, 45, 42, 0.14);
    }}

    .hero-panel {{
      padding: 26px;
      display: grid;
      gap: 16px;
      align-content: start;
    }}

    .hero-panel h2 {{
      font-size: 1.28rem;
      letter-spacing: -0.03em;
    }}

    .metric-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }}

    .metric {{
      padding: 16px;
      border-radius: 18px;
      background: rgba(255, 250, 240, 0.82);
      border: 1px solid rgba(31, 45, 42, 0.08);
    }}

    .metric strong {{
      display: block;
      font-family: "Space Grotesk", sans-serif;
      font-size: 1.55rem;
      letter-spacing: -0.04em;
      margin-bottom: 4px;
    }}

    .metric span {{
      color: var(--muted);
      font-size: 0.94rem;
      line-height: 1.35;
    }}

    main {{
      padding: 8px 0 42px;
    }}

    .section {{
      margin-top: 26px;
    }}

    .section-card {{
      padding: 28px;
    }}

    .section-head {{
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 18px;
    }}

    .section-head p {{
      margin: 10px 0 0;
      color: var(--muted);
      max-width: 62ch;
      line-height: 1.55;
    }}

    .topics {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 16px;
    }}

    .topic-card {{
      padding: 22px;
      text-decoration: none;
      color: inherit;
      position: relative;
      overflow: hidden;
      transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    }}

    .topic-card:hover {{
      transform: translateY(-3px);
      border-color: rgba(31, 122, 114, 0.28);
      box-shadow: 0 28px 58px rgba(32, 43, 39, 0.16);
    }}

    .topic-card.featured {{
      background:
        linear-gradient(160deg, rgba(31, 122, 114, 0.1), rgba(215, 169, 59, 0.12)),
        var(--surface-strong);
    }}

    .topic-card h3 {{
      font-size: 1.3rem;
      letter-spacing: -0.03em;
      margin-bottom: 10px;
    }}

    .topic-card p {{
      margin: 0;
      color: var(--muted);
      line-height: 1.5;
    }}

    .topic-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 14px;
      padding: 7px 12px;
      border-radius: 999px;
      background: rgba(255, 250, 240, 0.9);
      border: 1px solid rgba(31, 45, 42, 0.1);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}

    .topic-stats {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
      margin: 18px 0 16px;
    }}

    .topic-stats div {{
      padding: 10px 10px 12px;
      border-radius: 16px;
      background: rgba(255, 250, 240, 0.76);
      border: 1px solid rgba(31, 45, 42, 0.08);
    }}

    .topic-stats strong {{
      display: block;
      font-family: "Space Grotesk", sans-serif;
      font-size: 1.02rem;
      margin-bottom: 2px;
    }}

    .topic-stats span {{
      color: var(--muted);
      font-size: 0.78rem;
      line-height: 1.3;
    }}

    .topic-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-top: 16px;
      color: var(--teal-deep);
      font-family: "Space Grotesk", sans-serif;
      font-weight: 700;
      text-decoration: none;
    }}

    .use-grid,
    .reading-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
    }}

    .callout {{
      padding: 20px 22px;
      background: rgba(255, 250, 240, 0.9);
    }}

    .callout h3 {{
      font-size: 1.06rem;
      margin-bottom: 10px;
    }}

    .callout p,
    .callout li {{
      color: var(--muted);
      line-height: 1.55;
    }}

    .callout ul,
    .callout ol {{
      margin: 0;
      padding-left: 20px;
    }}

    .snapshot-list {{
      margin: 18px 0 0;
      padding-left: 20px;
      color: var(--muted);
    }}

    .snapshot-list li {{
      line-height: 1.55;
      margin-bottom: 8px;
    }}

    .resource-list {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
      margin-top: 18px;
    }}

    .resource-list a {{
      display: block;
      padding: 16px 18px;
      border-radius: 18px;
      background: rgba(255, 250, 240, 0.86);
      border: 1px solid rgba(31, 45, 42, 0.1);
      text-decoration: none;
      transition: transform 180ms ease, border-color 180ms ease;
    }}

    .resource-list a:hover {{
      transform: translateY(-2px);
      border-color: rgba(31, 122, 114, 0.25);
    }}

    .resource-list strong {{
      display: block;
      font-family: "Space Grotesk", sans-serif;
      margin-bottom: 4px;
    }}

    .resource-list span {{
      color: var(--muted);
      line-height: 1.45;
    }}

    footer {{
      padding: 0 0 36px;
    }}

    .footer-card {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      padding: 18px 22px;
      border-radius: 22px;
      border: 1px solid var(--line);
      background: rgba(255, 252, 243, 0.76);
      box-shadow: 0 10px 30px rgba(32, 43, 39, 0.08);
    }}

    .footer-card p {{
      margin: 0;
      color: var(--muted);
      line-height: 1.45;
    }}

    [data-reveal] {{
      opacity: 0;
      transform: translateY(18px);
      animation: rise 700ms ease forwards;
    }}

    [data-reveal="2"] {{ animation-delay: 90ms; }}
    [data-reveal="3"] {{ animation-delay: 180ms; }}
    [data-reveal="4"] {{ animation-delay: 270ms; }}
    [data-reveal="5"] {{ animation-delay: 360ms; }}

    @keyframes rise {{
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      html {{
        scroll-behavior: auto;
      }}

      * {{
        animation: none !important;
        transition: none !important;
      }}

      [data-reveal] {{
        opacity: 1;
        transform: none;
      }}
    }}

    @media (max-width: 1080px) {{
      .hero-grid,
      .topics,
      .use-grid,
      .reading-grid,
      .resource-list {{
        grid-template-columns: 1fr 1fr;
      }}

      .hero-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    @media (max-width: 720px) {{
      .shell {{
        width: min(var(--max), calc(100% - 20px));
      }}

      .topbar {{
        border-radius: 28px;
        padding: 16px;
      }}

      .hero-copy,
      .hero-panel,
      .section-card {{
        padding: 22px;
      }}

      .metric-grid,
      .topics,
      .use-grid,
      .reading-grid,
      .resource-list {{
        grid-template-columns: 1fr;
      }}

      .topic-stats {{
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }}

      h1 {{
        max-width: 12ch;
      }}

      .section-head {{
        display: block;
      }}
    }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="shell">
      <div class="topbar" data-reveal="1">
        <div class="eyebrow">Africa RCT E156 Portfolio</div>
        <nav aria-label="Section links">
          <a href="#topics">Topics</a>
          <a href="#use">How To Use</a>
          <a href="#files">Files</a>
        </nav>
      </div>

      <div class="hero-grid">
        <section class="hero-copy" data-reveal="2">
          <div class="eyebrow">Strict E156 Releases</div>
          <h1>Four compact Africa-site RCT portfolios.</h1>
          <p class="lead">
            This portfolio packages four Africa-site RCT topic scans as strict E156 publication units: one validated 156-word body per topic, plus companion code, data, and HTML artifacts. Malaria is the strongest first entry point under these registry-based proxy measures if the goal is to find smaller-footprint, faster-reporting trial patterns.
          </p>
          <div class="hero-actions">
            <a class="button button-primary" href="{featured['public_url']}">Start With Malaria</a>
            <a class="button button-secondary" href="#topics">Compare All Topics</a>
          </div>
        </section>

        <aside class="hero-panel" data-reveal="3">
          <h2>Portfolio Snapshot</h2>
          <div class="metric-grid">
            <div class="metric">
              <strong>{len(entries)}</strong>
              <span>public topic repos in active E156 mode</span>
            </div>
            <div class="metric">
              <strong>{featured['k']}/{featured['n']}</strong>
              <span>{topic_display(featured)} shortlist yield, the strongest in the set</span>
            </div>
            <div class="metric">
              <strong>156</strong>
              <span>words in every active E156 release body</span>
            </div>
            <div class="metric">
              <strong>{featured['proportion']}</strong>
              <span>{topic_display(featured)} shortlist proportion, 95% CI {featured['ci']}</span>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </header>

  <main>
    <div class="shell">
      <section id="topics" class="section section-card" data-reveal="3">
        <div class="section-head">
          <div>
            <h2>Topic Entry Points</h2>
            <p>Each card links to a public repo with one validated E156 body and its companion files. The cards are ordered by the strength of their registry-based shortlist signal, not by direct cost or effectiveness estimates.</p>
          </div>
        </div>

        <div class="topics">
{render_topic_cards(entries)}
        </div>
      </section>

      <section id="use" class="section section-card" data-reveal="4">
        <div class="section-head">
          <div>
            <h2>How To Use The Set</h2>
            <p>The portfolio works best if you treat the E156 body as the compact publication unit and the companion files as the richer evidence layer.</p>
          </div>
        </div>

        <div class="use-grid">
          <div class="callout">
            <h3>For Fast Reading</h3>
            <ul>
              <li>Read the 156-word E156 body in each topic repo first.</li>
              <li>Use malaria as the anchor topic for the strongest first proxy signal.</li>
              <li>Use the matrix to decide whether a second topic is worth deeper review.</li>
            </ul>
          </div>
          <div class="callout">
            <h3>For Deeper Inspection</h3>
            <ul>
              <li>Open each repo’s <code>paper/index.html</code> companion for the richer artifact layer.</li>
              <li>Use the repo <code>data/</code> folders for benchmark outputs and shortlist files.</li>
              <li>Use the repo <code>code/</code> folders if you want to rerun or extend the scans.</li>
            </ul>
          </div>
        </div>

        <div class="reading-grid" style="margin-top: 16px;">
          <div class="callout">
            <h3>Suggested Review Order</h3>
            <ol>
              {"".join(f"<li>{topic_label(entry)}</li>" for entry in entries)}
            </ol>
          </div>
          <div class="callout">
            <h3>Interpretation Guardrail</h3>
            <p>This portfolio compares registry-visible operational proxies. It does not directly measure true trial cost or true clinical effectiveness.</p>
          </div>
        </div>

        <div class="callout" style="margin-top: 16px;">
          <h3>Portfolio Snapshot</h3>
          <ul class="snapshot-list">
{render_snapshot(entries)}
          </ul>
        </div>
      </section>

      <section id="files" class="section section-card" data-reveal="5">
        <div class="section-head">
          <div>
            <h2>Portfolio Files</h2>
            <p>Use the portfolio repo itself for orientation, and the topic repos for the actual paper and companion artifacts.</p>
          </div>
        </div>

        <div class="resource-list">
          <a href="TOPIC_MATRIX.md">
            <strong>Topic Matrix</strong>
            <span>Side-by-side comparison of benchmark size, shortlist size, proportions, timing, and practical readouts.</span>
          </a>
          <a href="MANIFEST.json">
            <strong>Manifest</strong>
            <span>Machine-readable list of public URLs, ordering metadata, release mode, and headline metrics.</span>
          </a>
          <a href="data/topic_comparison.md">
            <strong>Topic Comparison Note</strong>
            <span>Underlying cross-topic narrative explaining why malaria has the strongest proxy-based signal in this scan.</span>
          </a>
          <a href="data/malaria_deep_dive_summary.md">
            <strong>Malaria Deep Dive</strong>
            <span>Deeper malaria-only readout on structured outcomes, heuristic leadership tags, and several excluded off-topic registry hits.</span>
          </a>
        </div>
      </section>
    </div>
  </main>

  <footer>
    <div class="shell">
      <div class="footer-card">
        <p>Primary public landing set: <code>mahmood726-cyber/malaria-e156</code>, <code>hiv-e156</code>, <code>maternal-health-e156</code>, <code>hypertension-e156</code>, and this umbrella repo.</p>
        <a class="button button-secondary" href="https://github.com/mahmood726-cyber/africa-rct-e156-portfolio">Open portfolio repo</a>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def main() -> None:
    entries = load_manifest()
    INDEX_PATH.write_text(render_index(entries), encoding="utf-8")
    MATRIX_PATH.write_text(render_matrix(entries), encoding="utf-8")


if __name__ == "__main__":
    main()
