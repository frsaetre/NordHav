"""Bulk-update old 11-item footers to new 8-item footers across all HTML files."""
import pathlib, re

FOLDER = pathlib.Path(__file__).parent

NEW_FOOTER = (
    '<footer>\n'
    '  <div class="footer-links">\n'
    '    <a href="company.html">Company</a><a href="customer-requirements.html">Requirements</a><a href="architecture.html">Architecture</a>\n'
    '    <a href="d365-coverage.html">D365</a><a href="integrations.html">Integration</a>\n'
    '    <a href="analytics.html">Analytics</a><a href="agentic-automation.html">Agents</a><a href="rollout.html">Rollout</a><a href="tco-roi.html">TCO &amp; ROI</a>\n'
    '  </div>\n'
    '  <div class="footer-copy">NordHav Aquaculture AS &middot; D365 F&amp;O + AquaMonitor Solution &middot; March 2026 &middot; Confidential</div>\n'
    '</footer>'
)

# Match any <footer>...</footer> block (non-greedy, DOTALL)
FOOTER_RE = re.compile(r'<footer>.*?</footer>', re.DOTALL)

updated = []
skipped = []

for f in sorted(FOLDER.glob('*.html')):
    text = f.read_text(encoding='utf-8')
    if '<footer>' not in text:
        skipped.append(f.name)
        continue
    # Check if footer already matches the new format
    if NEW_FOOTER in text:
        skipped.append(f.name + ' (already current)')
        continue
    new_text = FOOTER_RE.sub(NEW_FOOTER, text, count=1)
    if new_text != text:
        f.write_text(new_text, encoding='utf-8')
        updated.append(f.name)
    else:
        skipped.append(f.name + ' (no match)')

print(f"Updated {len(updated)} files: {', '.join(updated)}")
print(f"Skipped {len(skipped)} files: {', '.join(skipped)}")
