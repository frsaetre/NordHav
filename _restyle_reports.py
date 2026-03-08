"""
Inject shared dark-themed navigation bar and footer into standalone report HTML files.

These files use their own embedded Fluent UI / light-themed styles. This script
adds a self-contained dark nav and footer (matching the shared site theme) without
disturbing existing content styling.

Changes per file:
1. Google Fonts + inline nav/footer CSS injected into <head>
2. Back-link bar replaced with shared dark nav
3. Old footer (div.footer | div.report-footer | div.page-footer | <footer>) replaced with shared dark footer
4. Any old back-link <div> removed
"""
import re, os, pathlib

HTML_DIR = pathlib.Path(__file__).parent

# ── Files to process ─────────────────────────────────────────
TARGETS = [
    "deployment-summary.html",
    "e2e-test-plan.html",
    "e2e-test-results-nha.html",
    "e2e-test-results-nhn.html",
    "environment-config.html",
    "rollout-report.html",
]

# ── Active nav mapping ────────────────────────────────────────
ACTIVE_MAP = {
    "deployment-summary.html": "rollout.html",
    "e2e-test-plan.html":     "rollout.html",
    "e2e-test-results-nha.html": "rollout.html",
    "e2e-test-results-nhn.html": "rollout.html",
    "environment-config.html": "d365-coverage.html",
    "rollout-report.html":    "rollout.html",
}

# ── Inline CSS for nav + footer (self-contained, no _shared.css dependency) ──
INLINE_CSS = """
<!-- Shared Nav/Footer Theme -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style id="shared-nav-footer">
.sn-bar{position:sticky;top:0;width:100%;z-index:200;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);background:rgba(4,13,26,.95);border-bottom:1px solid rgba(0,180,216,.18);padding:0 2rem;display:flex;align-items:center;justify-content:space-between;height:52px;font-family:'Inter',sans-serif}
.sn-logo{display:flex;align-items:center;gap:.75rem;text-decoration:none!important}
.sn-logo svg{height:24px;width:auto}
.sn-logo .logo-fill{fill:#00b4d8}
.sn-wordmark{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:.9rem;color:#d4eaf5;letter-spacing:.05em}
.sn-links{display:flex;gap:.15rem;flex-wrap:wrap}
.sn-link{color:#6a8fa8!important;text-decoration:none!important;font-size:.8rem;font-weight:500;padding:.3rem .7rem;border-radius:6px;transition:all .2s;white-space:nowrap;font-family:'Inter',sans-serif}
.sn-link:hover,.sn-link.active{color:#00b4d8!important;background:rgba(0,180,216,.07);text-decoration:none!important}
.sn-toggle{display:none;background:none;border:none;cursor:pointer;color:#d4eaf5;padding:4px}
@media(max-width:768px){
  .sn-links{display:none;position:absolute;top:52px;left:0;right:0;background:rgba(4,13,26,.97);flex-direction:column;padding:.75rem 1rem;border-bottom:1px solid rgba(0,180,216,.18)}
  .sn-links.open{display:flex}
  .sn-toggle{display:block}
}
footer.sf-bar{background:rgba(4,13,26,.95);border-top:1px solid rgba(0,180,216,.18);padding:2rem;text-align:center;font-family:'Inter',sans-serif}
footer.sf-bar .sf-links{display:flex;justify-content:center;gap:.5rem;flex-wrap:wrap;margin-bottom:.75rem}
footer.sf-bar .sf-links a{color:#6a8fa8;text-decoration:none;font-size:.8rem;font-weight:500;padding:.25rem .6rem;border-radius:6px;transition:all .2s}
footer.sf-bar .sf-links a:hover{color:#00b4d8}
footer.sf-bar .sf-copy{font-size:.72rem;color:#3a5a72}
</style>
"""

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

NAV_SVG = '<svg height="24" viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg"><g class="logo-fill"><circle cx="126" cy="70" r="5.5"/><circle cx="151" cy="73" r="5.1"/><circle cx="178" cy="76" r="4.8"/><circle cx="205" cy="79" r="4.6"/><circle cx="232" cy="81" r="4.5"/><circle cx="260" cy="83" r="4.4"/><circle cx="288" cy="81" r="4.5"/><circle cx="315" cy="79" r="4.6"/><circle cx="341" cy="76" r="4.8"/><circle cx="366" cy="73" r="5.1"/><circle cx="390" cy="70" r="5.5"/><circle cx="260" cy="130" r="3.3"/><circle cx="210" cy="130" r="4.4"/><circle cx="310" cy="130" r="4.4"/><path d="M0 170 V100 H12 L35 145 V100 H47 V170 H35 L12 125 V170Z"/><path d="M70 100 C88 100 100 115 100 135 C100 155 88 170 70 170 C52 170 40 155 40 135 C40 115 52 100 70 100ZM70 114 C62 114 56 123 56 135 C56 147 62 156 70 156 C78 156 84 147 84 135 C84 123 78 114 70 114Z" transform="translate(60,0)"/><path d="M0 170 V100 H28 C42 100 46 108 46 120 C46 130 40 138 30 140 L46 170 H34 L19 141 H13 V170Z M13 129 H28 C34 129 35 126 35 120 C35 114 34 112 28 112 H13Z" transform="translate(170,0)"/><path d="M0 170 V100 H28 C48 100 50 116 50 135 C50 154 48 170 28 170ZM14 156 H28 C36 156 37 145 37 135 C37 125 36 114 28 114 H14Z" transform="translate(240,0)"/><path d="M0 170 V100 H14 V129 H36 V100 H50 V170 H36 V143 H14 V170Z" transform="translate(310,0)"/><path d="M20 100 L0 170 H12 L18 148 H38 L44 170 H56 L36 100ZM28 118 L21 138 H35Z" transform="translate(372,0)"/><path d="M0 100 H14 L32 152 L50 100 H64 L38 170 H26Z" transform="translate(438,0)"/></g></svg>'

HAMBURGER_SVG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>'


def build_nav_html(active_href):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' active' if href == active_href else ''
        links.append(f'    <a href="{href}" class="sn-link{cls}">{label}</a>')
    return f"""<nav class="sn-bar">
  <a class="sn-logo" href="index.html">
    {NAV_SVG}
    <span class="sn-wordmark">ERP AI Response Demo</span>
  </a>
  <button class="sn-toggle" aria-label="Toggle navigation" onclick="this.nextElementSibling.classList.toggle('open')">{HAMBURGER_SVG}</button>
  <div class="sn-links">
{chr(10).join(links)}
  </div>
</nav>"""

FOOTER_HTML = """<footer class="sf-bar">
  <div class="sf-links">
    <a href="company.html">Company</a><a href="customer-requirements.html">Requirements</a><a href="architecture.html">Architecture</a>
    <a href="d365-coverage.html">D365</a><a href="integrations.html">Integration</a>
    <a href="analytics.html">Analytics</a><a href="agentic-automation.html">Agents</a><a href="rollout.html">Rollout</a><a href="tco-roi.html">TCO &amp; ROI</a>
  </div>
  <div class="sf-copy">NordHav Aquaculture AS &middot; D365 F&amp;O + AquaMonitor Solution &middot; March 2026 &middot; Confidential</div>
</footer>"""


# ── Regex patterns ───────────────────────────────────────────
# Back-link bar: <div ...>← Back to Hub...</div>  (first div after body with a back link)
BACKLINK_RE = re.compile(
    r'<div[^>]*>\s*<a[^>]*>(?:←|&larr;|&#x2190;)\s*Back[^<]*</a>\s*</div>\s*',
    re.IGNORECASE
)

# Old footer (any of the variants)
OLD_FOOTER_RE = re.compile(
    r'(?:<footer[^>]*>.*?</footer>|<div\s+class="(?:footer|report-footer|page-footer)"[^>]*>.*?</div>)',
    re.DOTALL
)


def process_file(fname):
    fpath = HTML_DIR / fname
    text = fpath.read_text(encoding='utf-8')

    # 1. Inject inline CSS before </head>
    if 'id="shared-nav-footer"' not in text:
        text = text.replace('</head>', INLINE_CSS + '\n</head>', 1)

    # 2. Remove old back-link bar and inject nav after <body...>
    active = ACTIVE_MAP.get(fname)
    nav_html = build_nav_html(active)

    # Remove back-link bar if present
    text = BACKLINK_RE.sub('', text, count=1)

    # Inject nav right after <body> (or <body ...>)
    if '<nav class="sn-bar">' not in text:
        text = re.sub(
            r'(<body[^>]*>)\s*',
            r'\1\n' + nav_html + '\n',
            text,
            count=1
        )

    # 3. Replace old footer with shared footer
    if '<footer class="sf-bar">' not in text:
        if OLD_FOOTER_RE.search(text):
            text = OLD_FOOTER_RE.sub(FOOTER_HTML, text, count=1)
        else:
            # No footer found — insert before </body> or before last <script>
            text = text.replace('</body>', FOOTER_HTML + '\n</body>', 1)

    fpath.write_text(text, encoding='utf-8')
    return True


# ── Main ─────────────────────────────────────────────────────
updated = []
for fname in TARGETS:
    fpath = HTML_DIR / fname
    if not fpath.exists():
        print(f"  SKIP {fname} (not found)")
        continue
    try:
        process_file(fname)
        updated.append(fname)
        print(f"  ✓ {fname}")
    except Exception as e:
        print(f"  ✗ {fname}: {e}")

print(f"\nProcessed {len(updated)} files.")
