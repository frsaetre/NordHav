"""Generate per-category Solution Answer HTML pages.

Reads the original RFP requirement markdown files (05-11), merges with solution
response data from _solution_data*.py files, and produces 7 HTML pages that
provide detailed, per-requirement D365 F&O solution responses — one page per
requirement category.

Output files:  ans-finance.html, ans-aquaculture.html, ans-processing.html,
               ans-supply-chain.html, ans-quality.html, ans-hr.html,
               ans-technology.html
"""
import re, html as h
from collections import OrderedDict
from pathlib import Path

# ---------------------------------------------------------------------------
# Import solution data from all 7 category files
# ---------------------------------------------------------------------------
from _solution_data     import SOLUTIONS       as SOL_FIN
from _solution_data_aqu import SOLUTIONS_AQU   as SOL_AQU
from _solution_data_prc import SOLUTIONS_PRC   as SOL_PRC
from _solution_data_scm import SOLUTIONS_SCM   as SOL_SCM
from _solution_data_qac import SOLUTIONS_QAC   as SOL_QAC
from _solution_data_hrp import SOLUTIONS_HRP   as SOL_HRP
from _solution_data_tec import SOLUTIONS_TEC   as SOL_TEC

BASE    = Path(__file__).parent
REQ_DIR = BASE.parent.parent / "Requirements"

# ---------------------------------------------------------------------------
# Response code descriptions and colours
# ---------------------------------------------------------------------------
RESP_META = {
    "S": ("Standard",      "var(--success)",  "Delivered by standard D365 F&O functionality"),
    "C": ("Configuration", "var(--primary)",   "Delivered by D365 F&O with project-specific configuration"),
    "D": ("Developed",     "var(--accent)",    "Delivered via custom development or Power Platform solution"),
    "P": ("Partner / ISV", "#c084fc",          "Delivered via partner/ISV solution or Microsoft 365"),
    "R": ("Roadmap",       "var(--secondary)", "On the Microsoft D365 product roadmap"),
    "N": ("Not Covered",   "var(--danger)",    "Not currently addressed by the proposed solution"),
}

# ---------------------------------------------------------------------------
# Parse requirement markdown (same logic as _generate_req_detail.py)
# ---------------------------------------------------------------------------
def parse_requirements_md(filepath):
    text = filepath.read_text(encoding="utf-8")
    sections = []
    current_section = None
    for line in text.split("\n"):
        sec_match = re.match(r"^##\s+(\d+\.\d+)\s+(.+)$", line.strip())
        if sec_match:
            current_section = {
                "number": sec_match.group(1),
                "title":  sec_match.group(2).strip(),
                "requirements": [],
            }
            sections.append(current_section)
            continue
        row_match = re.match(
            r"^\|\s*([A-Z]{2,4}-\d{3})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*([MHD])\s*\|$",
            line.strip(),
        )
        if row_match and current_section is not None:
            current_section["requirements"].append({
                "id":          row_match.group(1).strip(),
                "name":        row_match.group(2).strip(),
                "description": row_match.group(3).strip(),
                "priority":    row_match.group(4).strip(),
            })
    return sections

# ---------------------------------------------------------------------------
# Category metadata — maps categories to data and filenames
# ---------------------------------------------------------------------------
CAT_META = OrderedDict([
    ("Finance & Accounting", {
        "slug":   "ans-finance",
        "icon":   "💰",
        "desc":   "Detailed solution responses for General Ledger, Accounts Payable & Receivable, Cash & Bank, Fixed Assets, Tax, and Biological Asset Accounting.",
        "source": "05_Requirements_Finance_and_Accounting.md",
        "data":   SOL_FIN,
    }),
    ("Aquaculture Operations", {
        "slug":   "ans-aquaculture",
        "icon":   "🐟",
        "desc":   "Detailed solution responses for smolt production, sea farming, biomass, feed, lice & fish health, harvest, and environmental reporting.",
        "source": "06_Requirements_Aquaculture_Operations.md",
        "data":   SOL_AQU,
    }),
    ("Processing & VAP", {
        "slug":   "ans-processing",
        "icon":   "🏭",
        "desc":   "Detailed solution responses for primary processing, VAP production, packing, cold storage, dispatch, and processing cost management.",
        "source": "07_Requirements_Processing_and_VAP.md",
        "data":   SOL_PRC,
    }),
    ("Supply Chain & Logistics", {
        "slug":   "ans-supply-chain",
        "icon":   "📦",
        "desc":   "Detailed solution responses for sales operations, procurement, inventory, warehousing, demand planning, and transportation.",
        "source": "08_Requirements_Supply_Chain_and_Logistics.md",
        "data":   SOL_SCM,
    }),
    ("Quality & Compliance", {
        "slug":   "ans-quality",
        "icon":   "✅",
        "desc":   "Detailed solution responses for QMS, HACCP, laboratory/LIMS, traceability & recall, regulatory, HSE, and environmental compliance.",
        "source": "09_Requirements_Quality_and_Compliance.md",
        "data":   SOL_QAC,
    }),
    ("HR & Payroll", {
        "slug":   "ans-hr",
        "icon":   "👥",
        "desc":   "Detailed solution responses for core HR, recruitment, time & attendance, leave, Norwegian payroll, compensation, and training.",
        "source": "10_Requirements_HR_and_Payroll.md",
        "data":   SOL_HRP,
    }),
    ("Technology, Integration & Security", {
        "slug":   "ans-technology",
        "icon":   "⚙️",
        "desc":   "Detailed solution responses for platform, user experience, integrations, maintenance/CMMS, reporting, security, and implementation.",
        "source": "11_Requirements_Technology_and_Integration.md",
        "data":   SOL_TEC,
    }),
])

# ---------------------------------------------------------------------------
# Priority badge HTML
# ---------------------------------------------------------------------------
PRIORITY_BADGE = {
    "M": '<span class="badge badge-m">Mandatory</span>',
    "H": '<span class="badge badge-h">High</span>',
    "D": '<span class="badge badge-d">Desirable</span>',
}

# ---------------------------------------------------------------------------
# Navigation logo SVG
# ---------------------------------------------------------------------------
NAV_LOGO = '''<svg height="28" viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg"><g class="logo-fill"><circle cx="126" cy="70" r="5.5"/><circle cx="151" cy="73" r="5.1"/><circle cx="178" cy="76" r="4.8"/><circle cx="205" cy="79" r="4.6"/><circle cx="232" cy="81" r="4.5"/><circle cx="260" cy="83" r="4.4"/><circle cx="288" cy="81" r="4.5"/><circle cx="315" cy="79" r="4.6"/><circle cx="341" cy="76" r="4.8"/><circle cx="366" cy="73" r="5.1"/><circle cx="390" cy="70" r="5.5"/><circle cx="260" cy="130" r="3.3"/><circle cx="210" cy="130" r="4.4"/><circle cx="310" cy="130" r="4.4"/><path d="M0 170 V100 H12 L35 145 V100 H47 V170 H35 L12 125 V170Z"/><path d="M70 100 C88 100 100 115 100 135 C100 155 88 170 70 170 C52 170 40 155 40 135 C40 115 52 100 70 100ZM70 114 C62 114 56 123 56 135 C56 147 62 156 70 156 C78 156 84 147 84 135 C84 123 78 114 70 114Z" transform="translate(60,0)"/><path d="M0 170 V100 H28 C42 100 46 108 46 120 C46 130 40 138 30 140 L46 170 H34 L19 141 H13 V170Z M13 129 H28 C34 129 35 126 35 120 C35 114 34 112 28 112 H13Z" transform="translate(170,0)"/><path d="M0 170 V100 H28 C48 100 50 116 50 135 C50 154 48 170 28 170ZM14 156 H28 C36 156 37 145 37 135 C37 125 36 114 28 114 H14Z" transform="translate(240,0)"/><path d="M0 170 V100 H14 V129 H36 V100 H50 V170 H36 V143 H14 V170Z" transform="translate(310,0)"/><path d="M20 100 L0 170 H12 L18 148 H38 L44 170 H56 L36 100ZM28 118 L21 138 H35Z" transform="translate(372,0)"/><path d="M0 100 H14 L32 152 L50 100 H64 L38 170 H26Z" transform="translate(438,0)"/></g></svg>'''


# ---------------------------------------------------------------------------
# Build one HTML answer page
# ---------------------------------------------------------------------------
def build_page(cat_name, meta):
    slug   = meta["slug"]
    icon   = meta["icon"]
    desc   = meta["desc"]
    sol    = meta["data"]
    source_file = REQ_DIR / meta["source"]

    if not source_file.exists():
        print(f"  ✗  Source not found: {source_file}")
        return

    sections = parse_requirements_md(source_file)

    # Flatten all requirements
    all_reqs = []
    for sec in sections:
        all_reqs.extend(sec["requirements"])

    total = len(all_reqs)
    if total == 0:
        print(f"  ✗  No requirements parsed for {cat_name}")
        return

    # Compute coverage stats
    code_counts = {c: 0 for c in RESP_META}
    covered = 0
    for r in all_reqs:
        entry = sol.get(r["id"], {})
        code  = entry.get("code", "?")
        if code in code_counts:
            code_counts[code] += 1
        if code in ("S", "C", "D", "P"):
            covered += 1

    coverage_pct = covered / total * 100 if total else 0

    # Priority counts
    m_count = sum(1 for r in all_reqs if r["priority"] == "M")
    h_count = sum(1 for r in all_reqs if r["priority"] == "H")
    d_count = sum(1 for r in all_reqs if r["priority"] == "D")

    # ---- Coverage donut  ----
    donut_items = []
    offset = 0
    for code in ("S", "C", "D", "P", "R", "N"):
        cnt = code_counts.get(code, 0)
        if cnt == 0:
            continue
        pct = cnt / total * 100
        label, color, _ = RESP_META[code]
        donut_items.append((code, label, color, pct, offset, cnt))
        offset += pct

    donut_svg_parts = []
    for code, label, color, pct, off, cnt in donut_items:
        donut_svg_parts.append(
            f'<circle r="15.9" cx="50%" cy="50%" fill="none" stroke="{color}" stroke-width="6" '
            f'stroke-dasharray="{pct:.1f} {100-pct:.1f}" stroke-dashoffset="-{off:.1f}" />'
        )

    donut_svg = f"""<svg viewBox="0 0 42 42" style="width:140px;height:140px;transform:rotate(-90deg)">
      <circle r="15.9" cx="50%" cy="50%" fill="none" stroke="var(--card2)" stroke-width="6"/>
      {"".join(donut_svg_parts)}
    </svg>"""

    # ---- Legend for donut ----
    legend_items = []
    for code, label, color, pct, _, cnt in donut_items:
        legend_items.append(
            f'<div style="display:flex;align-items:center;gap:.5rem;font-size:.82rem">'
            f'<span style="display:inline-block;width:10px;height:10px;border-radius:3px;background:{color};flex-shrink:0"></span>'
            f'<span style="color:var(--text);font-weight:500">{label}</span>'
            f'<span style="color:var(--muted);margin-left:auto">{cnt} ({pct:.0f}%)</span>'
            f'</div>'
        )

    # ---- Section quick-nav pills ----
    section_pills = []
    for sec in sections:
        anchor = sec["title"].lower().replace(" ", "-").replace("&", "").replace("/", "-").replace("(", "").replace(")", "").replace("---", "-").replace("--", "-").strip("-")
        sec_count = len(sec["requirements"])
        section_pills.append(
            f'<a href="#sec-{h.escape(anchor)}" class="chip chip-primary" style="text-decoration:none;padding:.4rem .85rem;font-size:.82rem">'
            f'{h.escape(sec["number"])} {h.escape(sec["title"])} ({sec_count})</a>'
        )

    # ---- Requirement answer cards per section ----
    section_html_parts = []
    for sec in sections:
        reqs   = sec["requirements"]
        anchor = sec["title"].lower().replace(" ", "-").replace("&", "").replace("/", "-").replace("(", "").replace(")", "").replace("---", "-").replace("--", "-").strip("-")

        cards = []
        for r in reqs:
            entry   = sol.get(r["id"], {})
            code    = entry.get("code", "?")
            summary = entry.get("summary", "Solution response pending.")
            detail  = entry.get("detail", "<p><em>Detailed response to be provided.</em></p>")

            resp_label, resp_color, resp_tip = RESP_META.get(code, ("Unknown", "var(--muted)", ""))
            pri_badge = PRIORITY_BADGE.get(r["priority"], "")

            cards.append(f"""
      <div class="ans-card" id="{h.escape(r['id'])}">
        <div class="ans-header">
          <div class="ans-id">{h.escape(r["id"])}</div>
          <div class="ans-badges">
            <span class="ans-resp-badge" style="--resp-color:{resp_color}" title="{h.escape(resp_tip)}">{h.escape(resp_label)}</span>
            {pri_badge}
          </div>
        </div>
        <h3 class="ans-name">{h.escape(r["name"])}</h3>
        <div class="ans-req-desc"><strong>Requirement:</strong> {h.escape(r["description"])}</div>
        <div class="ans-summary"><strong>Summary:</strong> {h.escape(summary)}</div>
        <details class="ans-detail-wrap">
          <summary class="ans-detail-toggle">Show detailed solution response</summary>
          <div class="ans-detail">
            {detail}
          </div>
        </details>
      </div>""")

        section_html_parts.append(f"""
<div class="divider"></div>

<section class="section" id="sec-{h.escape(anchor)}">
  <div class="section-inner">
    <div class="section-tag reveal">{h.escape(sec["number"])}</div>
    <h2 class="section-title reveal">{h.escape(sec["title"])}</h2>
    <p class="reveal" style="color:var(--muted);font-size:.88rem;margin-bottom:1.5rem">{len(reqs)} requirements in this section</p>
    <div class="ans-grid stagger">
{"".join(cards)}
    </div>
  </div>
</section>""")

    # ---- Compose the full HTML page ----
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NordHav — {h.escape(cat_name)} Solution Answers</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="_shared.css">
<style>
/* ---- Back link ---- */
.back-link{{display:inline-flex;align-items:center;gap:.4rem;color:var(--muted);font-size:.85rem;font-weight:500;text-decoration:none;transition:color .2s;margin-bottom:1.5rem}}
.back-link:hover{{color:var(--primary)}}
.back-link svg{{width:16px;height:16px;fill:currentColor}}

/* ---- Coverage ring section ---- */
.cov-ring-wrap{{display:flex;flex-wrap:wrap;gap:2.5rem;align-items:center;margin:1.5rem 0 2rem}}
.cov-ring-chart{{position:relative;display:flex;align-items:center;justify-content:center}}
.cov-ring-pct{{position:absolute;font-family:'Space Grotesk',sans-serif;font-size:1.4rem;font-weight:700;color:var(--primary);transform:rotate(90deg)}}
.cov-legend{{display:flex;flex-direction:column;gap:.5rem;min-width:200px}}

/* ---- Section nav pills ---- */
.module-nav{{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.5rem 0 2rem}}

/* ---- Answer cards ---- */
.ans-grid{{display:flex;flex-direction:column;gap:1.25rem}}
.ans-card{{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.5rem 1.75rem;transition:border-color .25s}}
.ans-card:hover{{border-color:rgba(0,180,216,.3)}}
.ans-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:.6rem;flex-wrap:wrap;gap:.5rem}}
.ans-id{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:.92rem;color:var(--primary);letter-spacing:.04em}}
.ans-badges{{display:flex;align-items:center;gap:.45rem;flex-wrap:wrap}}
.ans-resp-badge{{display:inline-flex;align-items:center;font-size:.72rem;font-weight:700;padding:.22rem .65rem;border-radius:6px;background:color-mix(in srgb, var(--resp-color) 15%, transparent);color:var(--resp-color);border:1px solid color-mix(in srgb, var(--resp-color) 30%, transparent);text-transform:uppercase;letter-spacing:.06em}}
.ans-name{{font-size:1.05rem;font-weight:600;color:var(--text);margin-bottom:.5rem}}
.ans-req-desc{{font-size:.84rem;color:var(--muted);line-height:1.55;margin-bottom:.5rem;padding:.7rem .9rem;background:rgba(0,180,216,.04);border-left:3px solid rgba(0,180,216,.2);border-radius:0 6px 6px 0}}
.ans-summary{{font-size:.86rem;color:var(--text);line-height:1.55;margin-bottom:.65rem}}
.ans-detail-wrap{{margin-top:.3rem}}
.ans-detail-toggle{{font-size:.82rem;font-weight:600;color:var(--primary);cursor:pointer;user-select:none;padding:.3rem 0;list-style:none}}
.ans-detail-toggle::-webkit-details-marker{{display:none}}
.ans-detail-toggle::before{{content:'▸ ';transition:transform .2s;display:inline-block}}
details[open] .ans-detail-toggle::before{{content:'▾ '}}
.ans-detail{{font-size:.84rem;color:var(--text);line-height:1.65;margin-top:.65rem;padding:1rem 1.1rem;background:var(--card2);border-radius:10px;border:1px solid var(--border)}}
.ans-detail p{{margin:0 0 .65rem}}
.ans-detail ul{{margin:.4rem 0 .65rem 1.2rem;padding:0}}
.ans-detail li{{margin-bottom:.35rem}}
.ans-detail strong{{color:var(--secondary)}}

/* Tighter spacing between module sections on answer pages */
.divider + .section{{padding-top:2rem}}
.section:has(+ .divider){{padding-bottom:1.5rem}}
.divider{{margin:0}}

@media(max-width:640px){{
  .cov-ring-wrap{{flex-direction:column;align-items:flex-start}}
  .ans-card{{padding:1.1rem}}
  .ans-header{{flex-direction:column;align-items:flex-start}}
}}
</style>
</head>
<body>
<canvas id="bg-canvas"></canvas>

<nav>
  <a class="nav-logo" href="index.html">
    {NAV_LOGO}
    <span class="nav-wordmark">ERP AI Response Demo</span>
  </a>
  <div class="nav-links">
    <a href="solution.html" class="nav-link">Solution</a>
    <a href="customer-requirements.html" class="nav-link">Requirements</a>
    <a href="architecture.html" class="nav-link">Architecture</a>
    <a href="aquamonitor.html" class="nav-link">AquaMonitor</a>
    <a href="d365-coverage.html" class="nav-link">D365</a>
    <a href="erp-configuration.html" class="nav-link">ERP Config</a>
    <a href="integrations.html" class="nav-link">Integrations</a>
    <a href="analytics.html" class="nav-link">Analytics</a>
    <a href="rollout.html" class="nav-link">Rollout</a>
    <a href="tco-roi.html" class="nav-link">TCO &amp; ROI</a>
  </div>
</nav>

<!-- HERO -->
<section class="hero" style="min-height:50vh;padding-top:8rem;padding-bottom:3rem">
  <div class="hero-eyebrow">
    <svg width="7" height="7" viewBox="0 0 7 7"><circle cx="3.5" cy="3.5" r="3.5" fill="#06d6a0"/></svg>
    Solution Answers · {h.escape(cat_name)}
  </div>
  <h1>{icon} {h.escape(cat_name)} — Solution Response</h1>
  <p class="hero-sub">{h.escape(desc)}</p>
  <div class="hero-meta">
    <div class="hero-meta-item"><div class="hero-meta-val">{total}</div><div class="hero-meta-lbl">Requirements</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:var(--success)">{coverage_pct:.0f}%</div><div class="hero-meta-lbl">Covered</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:var(--success)">{code_counts.get("S",0)}</div><div class="hero-meta-lbl">Standard</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:var(--primary)">{code_counts.get("C",0)}</div><div class="hero-meta-lbl">Config</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:var(--accent)">{code_counts.get("D",0)}</div><div class="hero-meta-lbl">Developed</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:#c084fc">{code_counts.get("P",0)}</div><div class="hero-meta-lbl">Partner</div></div>
  </div>
</section>

<!-- COVERAGE SUMMARY -->
<section class="section">
  <div class="section-inner">
    <a href="customer-requirements.html" class="back-link"><svg viewBox="0 0 24 24"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg> Back to Requirements Overview</a>

    <div class="section-tag reveal">Coverage</div>
    <h2 class="section-title reveal">Response Code Breakdown</h2>

    <div class="cov-ring-wrap reveal">
      <div class="cov-ring-chart">
        {donut_svg}
        <div class="cov-ring-pct">{coverage_pct:.0f}%</div>
      </div>
      <div class="cov-legend">
{"".join(legend_items)}
      </div>
    </div>

    <h3 class="reveal" style="margin-top:2rem;margin-bottom:.75rem">Jump to Section</h3>
    <div class="module-nav stagger">
      {"".join(section_pills)}
    </div>
  </div>
</section>

<!-- REQUIREMENT ANSWER SECTIONS -->
{"".join(section_html_parts)}

<div class="divider"></div>

<!-- BOTTOM NAV -->
<section class="section" style="padding:3rem 2rem">
  <div class="section-inner" style="text-align:center">
    <a href="customer-requirements.html" class="btn btn-ghost" style="margin-right:1rem">&#x2190; Requirements Overview</a>
    <a href="d365-coverage.html" class="btn btn-primary">D365 Coverage Matrix &#x2192;</a>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-links">
    <a href="solution.html">Solution</a><a href="customer-requirements.html">Requirements</a><a href="architecture.html">Architecture</a>
    <a href="aquamonitor.html">AquaMonitor</a><a href="d365-coverage.html">D365</a><a href="erp-configuration.html">ERP Config</a>
    <a href="integrations.html">Integrations</a><a href="analytics.html">Analytics</a><a href="rollout.html">Rollout</a><a href="tco-roi.html">TCO &amp; ROI</a>
  </div>
  <div class="footer-copy">NordHav Aquaculture AS &middot; D365 F&amp;O + AquaMonitor Solution &middot; March 2026 &middot; Confidential — Implementation Team Use Only</div>
</footer>

<script src="_shared.js"></script>
</body>
</html>"""
    out_path = BASE / f"{slug}.html"
    out_path.write_text(page, encoding="utf-8")
    print(f"  ✓ {out_path.name}  ({total} req, {covered}/{total} covered = {coverage_pct:.0f}%)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("═" * 60)
    print("  Generating Solution Answer pages")
    print("═" * 60)
    for cat_name, meta in CAT_META.items():
        build_page(cat_name, meta)
    print("═" * 60)
    print("  Done — 7 answer pages generated")
    print("═" * 60)
