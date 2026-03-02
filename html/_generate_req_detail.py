"""Generate per-category requirement detail HTML pages from customer requirement markdown files.

Reads the original RFP requirement documents (Documents 05–11) and builds
requirement detail HTML pages that faithfully represent the CUSTOMER requirements
— organized by the customer's own RFP sections with full descriptions.
"""
import re, html as h
from collections import OrderedDict
from pathlib import Path

BASE = Path(__file__).parent
REQ_DIR = BASE.parent.parent / "Requirements"

# ---------------------------------------------------------------------------
# Parse a requirement markdown file into sections of requirements
# ---------------------------------------------------------------------------
def parse_requirements_md(filepath):
    """Parse an RFP requirements markdown file.
    Returns list of dicts: [{section_number, section_title, requirements: [{id, name, description, priority}]}]
    """
    text = filepath.read_text(encoding="utf-8")
    sections = []
    current_section = None

    for line in text.split("\n"):
        # Match section headers like "## 5.1 GENERAL LEDGER"
        sec_match = re.match(r"^##\s+(\d+\.\d+)\s+(.+)$", line.strip())
        if sec_match:
            current_section = {
                "number": sec_match.group(1),
                "title": sec_match.group(2).strip(),
                "requirements": [],
            }
            sections.append(current_section)
            continue

        # Match table rows like "| FIN-001 | Norwegian Chart of Accounts | Description... | M |"
        row_match = re.match(
            r"^\|\s*([A-Z]{2,4}-\d{3})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*([MHD])\s*\|$",
            line.strip(),
        )
        if row_match and current_section is not None:
            current_section["requirements"].append({
                "id": row_match.group(1).strip(),
                "name": row_match.group(2).strip(),
                "description": row_match.group(3).strip(),
                "priority": row_match.group(4).strip(),
            })

    return sections


# ---------------------------------------------------------------------------
# Category configuration — maps to the RFP requirement documents
# ---------------------------------------------------------------------------
CAT_META = OrderedDict([
    ("Finance & Accounting", {
        "slug": "req-finance",
        "icon": "💰",
        "desc": "General Ledger, Accounts Payable & Receivable, Cash & Bank Management, Fixed Assets, Tax, Cost Management, and Biological Asset Accounting.",
        "source": "05_Requirements_Finance_and_Accounting.md",
    }),
    ("Aquaculture Operations", {
        "slug": "req-aquaculture",
        "icon": "🐟",
        "desc": "Smolt production, sea farming, biomass estimation, feed management, lice and fish health monitoring, harvest coordination, and environmental reporting.",
        "source": "06_Requirements_Aquaculture_Operations.md",
    }),
    ("Processing & VAP", {
        "slug": "req-processing",
        "icon": "🏭",
        "desc": "Primary processing, VAP production, packing & labeling, cold storage, dispatch, in-process quality, and processing cost management.",
        "source": "07_Requirements_Processing_and_VAP.md",
    }),
    ("Supply Chain & Logistics", {
        "slug": "req-supply-chain",
        "icon": "📦",
        "desc": "Sales operations, procurement, inventory management, demand & supply planning, and transportation & logistics.",
        "source": "08_Requirements_Supply_Chain_and_Logistics.md",
    }),
    ("Quality & Compliance", {
        "slug": "req-quality",
        "icon": "✅",
        "desc": "QMS & food safety, HACCP/CCP monitoring, traceability & recall, HSE management, and environmental compliance.",
        "source": "09_Requirements_Quality_and_Compliance.md",
    }),
    ("HR & Payroll", {
        "slug": "req-hr",
        "icon": "👥",
        "desc": "Core HR, personnel management, Norwegian payroll processing, time & attendance, leave management, and learning & competence.",
        "source": "10_Requirements_HR_and_Payroll.md",
    }),
    ("Technology, Integration & Security", {
        "slug": "req-technology",
        "icon": "⚙️",
        "desc": "Platform & environment, user experience, security & compliance, integrations, reporting & analytics, asset management, and project cost management.",
        "source": "11_Requirements_Technology_and_Integration.md",
    }),
])


PRIORITY_BADGE = {
    "M": '<span class="badge badge-m">Mandatory</span>',
    "H": '<span class="badge badge-h">High</span>',
    "D": '<span class="badge badge-d">Desirable</span>',
}

PRIORITY_LABEL = {"M": "Mandatory", "H": "High", "D": "Desirable"}

NAV_LOGO = '''<svg height="28" viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg"><g class="logo-fill"><circle cx="126" cy="70" r="5.5"/><circle cx="151" cy="73" r="5.1"/><circle cx="178" cy="76" r="4.8"/><circle cx="205" cy="79" r="4.6"/><circle cx="232" cy="81" r="4.5"/><circle cx="260" cy="83" r="4.4"/><circle cx="288" cy="81" r="4.5"/><circle cx="315" cy="79" r="4.6"/><circle cx="341" cy="76" r="4.8"/><circle cx="366" cy="73" r="5.1"/><circle cx="390" cy="70" r="5.5"/><circle cx="260" cy="130" r="3.3"/><circle cx="210" cy="130" r="4.4"/><circle cx="310" cy="130" r="4.4"/><path d="M0 170 V100 H12 L35 145 V100 H47 V170 H35 L12 125 V170Z"/><path d="M70 100 C88 100 100 115 100 135 C100 155 88 170 70 170 C52 170 40 155 40 135 C40 115 52 100 70 100ZM70 114 C62 114 56 123 56 135 C56 147 62 156 70 156 C78 156 84 147 84 135 C84 123 78 114 70 114Z" transform="translate(60,0)"/><path d="M0 170 V100 H28 C42 100 46 108 46 120 C46 130 40 138 30 140 L46 170 H34 L19 141 H13 V170Z M13 129 H28 C34 129 35 126 35 120 C35 114 34 112 28 112 H13Z" transform="translate(170,0)"/><path d="M0 170 V100 H28 C48 100 50 116 50 135 C50 154 48 170 28 170ZM14 156 H28 C36 156 37 145 37 135 C37 125 36 114 28 114 H14Z" transform="translate(240,0)"/><path d="M0 170 V100 H14 V129 H36 V100 H50 V170 H36 V143 H14 V170Z" transform="translate(310,0)"/><path d="M20 100 L0 170 H12 L18 148 H38 L44 170 H56 L36 100ZM28 118 L21 138 H35Z" transform="translate(372,0)"/><path d="M0 100 H14 L32 152 L50 100 H64 L38 170 H26Z" transform="translate(438,0)"/></g></svg>'''


def build_page(cat_name, meta):
    slug = meta["slug"]
    icon = meta["icon"]
    desc = meta["desc"]
    source_file = REQ_DIR / meta["source"]

    if not source_file.exists():
        print(f"  ✗ Source not found: {source_file}")
        return

    sections = parse_requirements_md(source_file)

    # Collect all requirements for summary stats
    all_reqs = []
    for sec in sections:
        all_reqs.extend(sec["requirements"])

    total = len(all_reqs)
    m_count = sum(1 for r in all_reqs if r["priority"] == "M")
    h_count = sum(1 for r in all_reqs if r["priority"] == "H")
    d_count = sum(1 for r in all_reqs if r["priority"] == "D")
    num_sections = len(sections)

    # Build section sections
    section_html_parts = []
    for sec in sections:
        reqs = sec["requirements"]
        sec_total = len(reqs)
        sec_m = sum(1 for r in reqs if r["priority"] == "M")
        sec_h = sum(1 for r in reqs if r["priority"] == "H")
        sec_d = sum(1 for r in reqs if r["priority"] == "D")
        anchor = sec["title"].lower().replace(" ", "-").replace("&", "").replace("/", "-").replace("(", "").replace(")", "").replace("---", "-").replace("--", "-").strip("-")

        rows = []
        for r in reqs:
            rows.append(f"""          <tr>
            <td style="font-weight:600;color:var(--primary);white-space:nowrap">{h.escape(r["id"])}</td>
            <td style="font-weight:500">{h.escape(r["name"])}</td>
            <td style="font-size:.82rem;line-height:1.5;color:var(--text)">{h.escape(r["description"])}</td>
            <td style="text-align:center">{PRIORITY_BADGE.get(r["priority"], "")}</td>
          </tr>""")

        section_html_parts.append(f"""
<div class="divider"></div>

<section class="section" id="sec-{h.escape(anchor)}">
  <div class="section-inner">
    <div class="section-tag reveal">{h.escape(sec["number"])}</div>
    <h2 class="section-title reveal">{h.escape(sec["title"])}</h2>
    <div class="kpi-grid stagger" style="margin-bottom:2rem">
      <div class="kpi-card"><div class="kpi-val">{sec_total}</div><div class="kpi-lbl">Total</div></div>
      <div class="kpi-card danger"><div class="kpi-val">{sec_m}</div><div class="kpi-lbl">Mandatory</div></div>
      <div class="kpi-card accent"><div class="kpi-val">{sec_h}</div><div class="kpi-lbl">High</div></div>
      <div class="kpi-card"><div class="kpi-val">{sec_d}</div><div class="kpi-lbl">Desirable</div></div>
    </div>

    <div class="table-wrap reveal">
      <table class="data-table">
        <thead>
          <tr><th style="width:80px">ID</th><th style="width:20%">Requirement</th><th>Description</th><th style="width:100px;text-align:center">Priority</th></tr>
        </thead>
        <tbody>
{"".join(rows)}
        </tbody>
      </table>
    </div>
  </div>
</section>""")

    # Section quick-nav pills
    section_pills = []
    for sec in sections:
        anchor = sec["title"].lower().replace(" ", "-").replace("&", "").replace("/", "-").replace("(", "").replace(")", "").replace("---", "-").replace("--", "-").strip("-")
        sec_count = len(sec["requirements"])
        section_pills.append(
            f'<a href="#sec-{h.escape(anchor)}" class="chip chip-primary" style="text-decoration:none;padding:.4rem .85rem;font-size:.82rem">{h.escape(sec["number"])} {h.escape(sec["title"])} ({sec_count})</a>'
        )

    # Priority breakdown bars
    priority_bars = []
    for pkey, plabel, pcolor in [("M", "Mandatory", "var(--danger)"), ("H", "High", "var(--accent)"), ("D", "Desirable", "var(--dim)")]:
        count = sum(1 for r in all_reqs if r["priority"] == pkey)
        if count == 0:
            continue
        pct = count / total * 100 if total else 0
        priority_bars.append(
            f'      <div class="req-bar"><span class="req-bar-label">{plabel}</span>'
            f'<div class="req-bar-track"><div class="req-bar-fill" style="width:{pct:.0f}%;background:{pcolor}">{count}</div></div>'
            f'<span class="req-bar-count">{count}</span></div>'
        )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NordHav — {h.escape(cat_name)} Requirements Detail</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="_shared.css">
<style>
.back-link{{display:inline-flex;align-items:center;gap:.4rem;color:var(--muted);font-size:.85rem;font-weight:500;text-decoration:none;transition:color .2s;margin-bottom:1.5rem}}
.back-link:hover{{color:var(--primary)}}
.back-link svg{{width:16px;height:16px;fill:currentColor}}
.req-bar{{display:flex;align-items:center;gap:.75rem;margin:.5rem 0}}
.req-bar-label{{font-size:.78rem;font-weight:600;color:var(--text);width:180px;flex-shrink:0}}
.req-bar-track{{flex:1;height:28px;background:var(--card2);border-radius:6px;position:relative;overflow:hidden}}
.req-bar-fill{{height:100%;border-radius:6px;display:flex;align-items:center;justify-content:flex-end;padding-right:.6rem;font-size:.72rem;font-weight:700;color:var(--bg);transition:width .8s ease}}
.req-bar-count{{font-size:.78rem;font-weight:700;color:var(--text);width:36px;text-align:right;flex-shrink:0}}
.module-nav{{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.5rem 0 2rem}}
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
  </div>
</nav>

<!-- HERO -->
<section class="hero" style="min-height:50vh;padding-top:8rem;padding-bottom:3rem">
  <div class="hero-eyebrow">
    <svg width="7" height="7" viewBox="0 0 7 7"><circle cx="3.5" cy="3.5" r="3.5" fill="#06d6a0"/></svg>
    Requirements Detail · {h.escape(cat_name)}
  </div>
  <h1>{icon} {h.escape(cat_name)}</h1>
  <p class="hero-sub">{h.escape(desc)}</p>
  <div class="hero-meta">
    <div class="hero-meta-item"><div class="hero-meta-val">{total}</div><div class="hero-meta-lbl">Total Requirements</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:var(--danger)">{m_count}</div><div class="hero-meta-lbl">Mandatory</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:var(--accent)">{h_count}</div><div class="hero-meta-lbl">High</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val">{d_count}</div><div class="hero-meta-lbl">Desirable</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val">{num_sections}</div><div class="hero-meta-lbl">Sections</div></div>
  </div>
</section>

<!-- SUMMARY -->
<section class="section">
  <div class="section-inner">
    <a href="customer-requirements.html" class="back-link"><svg viewBox="0 0 24 24"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg> Back to Requirements Overview</a>

    <div class="section-tag reveal">Summary</div>
    <h2 class="section-title reveal">Priority Breakdown</h2>

    <div class="info-block reveal" style="margin-bottom:2rem">
{chr(10).join(priority_bars)}
    </div>

    <h3 class="reveal" style="margin-top:2rem;margin-bottom:.75rem">Jump to Section</h3>
    <div class="module-nav stagger">
      {"".join(section_pills)}
    </div>
  </div>
</section>

<!-- REQUIREMENT SECTIONS -->
{"".join(section_html_parts)}

<div class="divider"></div>

<!-- BACK -->
<section class="section" style="padding:3rem 2rem">
  <div class="section-inner" style="text-align:center">
    <a href="customer-requirements.html" class="btn btn-ghost" style="margin-right:1rem">&#x2190; Back to Requirements Overview</a>
    <a href="d365-coverage.html" class="btn btn-primary">View D365 Coverage &#x2192;</a>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-links">
    <a href="solution.html">Solution</a><a href="customer-requirements.html">Requirements</a><a href="architecture.html">Architecture</a>
    <a href="aquamonitor.html">AquaMonitor</a><a href="d365-coverage.html">D365</a><a href="erp-configuration.html">ERP Config</a>
    <a href="integrations.html">Integrations</a><a href="analytics.html">Analytics</a><a href="rollout.html">Rollout</a>
  </div>
  <div class="footer-copy">NordHav Aquaculture AS &middot; D365 F&amp;O + AquaMonitor Solution &middot; March 2026 &middot; Confidential — Implementation Team Use Only</div>
</footer>

<script src="_shared.js"></script>
</body>
</html>"""
    out_path = BASE / f"{slug}.html"
    out_path.write_text(page, encoding="utf-8")
    print(f"  ✓ {out_path.name}  ({total} requirements, {num_sections} sections)")


print("Generating requirement detail pages from customer RFP documents...")
for cat_name, meta in CAT_META.items():
    build_page(cat_name, meta)
print("Done!")
