"""Bulk-update navigation bars across all HTML files in Documentation/html/."""
import re, os, glob

HTML_DIR = os.path.dirname(os.path.abspath(__file__))

# New navigation items (href, label)
NAV_ITEMS = [
    ("company.html", "Company"),
    ("customer-requirements.html", "Requirements"),
    ("architecture.html", "Architecture"),
    ("d365-coverage.html", "D365"),
    ("integrations.html", "Integration"),
    ("analytics.html", "Analytics"),
    ("agentic-automation.html", "Agents"),
    ("rollout.html", "Rollout"),
    ("tco-roi.html", "TCO &amp; ROI"),
]

# Map each HTML file to which nav item should be "active"
ACTIVE_MAP = {
    "company.html": "company.html",
    "customer-requirements.html": "customer-requirements.html",
    "req-finance.html": "customer-requirements.html",
    "req-aquaculture.html": "customer-requirements.html",
    "req-processing.html": "customer-requirements.html",
    "req-supply-chain.html": "customer-requirements.html",
    "req-quality.html": "customer-requirements.html",
    "req-hr.html": "customer-requirements.html",
    "req-technology.html": "customer-requirements.html",
    "ans-finance.html": "customer-requirements.html",
    "ans-aquaculture.html": "customer-requirements.html",
    "ans-processing.html": "customer-requirements.html",
    "ans-supply-chain.html": "customer-requirements.html",
    "ans-quality.html": "customer-requirements.html",
    "ans-hr.html": "customer-requirements.html",
    "ans-technology.html": "customer-requirements.html",
    "architecture.html": "architecture.html",
    "aquamonitor.html": "architecture.html",
    "financeapp.html": "architecture.html",
    "solution.html": "architecture.html",
    "d365-coverage.html": "d365-coverage.html",
    "erp-configuration.html": "d365-coverage.html",
    "environment-config.html": "d365-coverage.html",
    "integrations.html": "integrations.html",
    "analytics.html": "analytics.html",
    "rollout.html": "rollout.html",
    "rollout-report.html": "rollout.html",
    "deployment-summary.html": "rollout.html",
    "e2e-test-plan.html": "rollout.html",
    "e2e-test-results-nha.html": "rollout.html",
    "e2e-test-results-nhn.html": "rollout.html",
    "tco-roi.html": "tco-roi.html",
    "agentic-automation.html": "agentic-automation.html",
    "index.html": None,  # hub — no active
    "NordHavSupplyChainMap.html": None,
}

def build_nav_links(active_href):
    """Return the new <div class="nav-links">...</div> block."""
    lines = ['  <div class="nav-links">']
    for href, label in NAV_ITEMS:
        cls = ' active' if href == active_href else ''
        lines.append(f'    <a href="{href}" class="nav-link{cls}">{label}</a>')
    lines.append('  </div>')
    return "\n".join(lines)

# Regex to match the full nav-links div (handles multiline)
NAV_RE = re.compile(
    r'<div\s+class="nav-links">\s*.*?</div>',
    re.DOTALL
)

updated = []
skipped = []

for fpath in sorted(glob.glob(os.path.join(HTML_DIR, "*.html"))):
    fname = os.path.basename(fpath)
    if fname.startswith("_"):
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if not NAV_RE.search(content):
        skipped.append(fname)
        continue
    
    active_href = ACTIVE_MAP.get(fname, None)
    new_nav = build_nav_links(active_href)
    
    new_content = NAV_RE.sub(new_nav, content, count=1)
    
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated.append(fname)
    else:
        skipped.append(fname + " (no change)")

print(f"Updated {len(updated)} files:")
for f in updated:
    print(f"  ✓ {f}")
print(f"Skipped {len(skipped)} files:")
for f in skipped:
    print(f"  - {f}")
