/* ═══════════════════════════════════════════════════════════
   AquaMonitor Navigation Service
   Renders topbar + sidebar on every page
   Usage: renderNav('pageid')  — call after DOM ready
   ═══════════════════════════════════════════════════════════ */

const NAV_ITEMS = [
  { section: 'Overview' },
  { id: 'index',       icon: '🏠', label: 'Dashboard',         href: 'index.html' },
  { id: 'sites',       icon: '🗺', label: 'Sites & Licenses',  href: 'sites.html' },
  { section: 'Production' },
  { id: 'freshwater',  icon: '💧', label: 'Freshwater / Smolt',href: 'freshwater.html' },
  { id: 'sea-ops',     icon: '🐟', label: 'Sea Operations',    href: 'sea-ops.html' },
  { id: 'feed',        icon: '🌾', label: 'Feed Management',   href: 'feed.html' },
  { section: 'Monitoring' },
  { id: 'lice',        icon: '🦐', label: 'Lice Management',   href: 'lice.html',   badge: () => DB.getPensOverLiceLimit(0.5), badgeClass:'badge' },
  { id: 'health',      icon: '⚕️', label: 'Fish Health',       href: 'health.html', badge: () => DB.getActivePrescriptions().length, badgeClass:'badge amber' },
  { id: 'environmental',icon:'🌡', label: 'Environmental',     href: 'environmental.html' },
  { section: 'Planning' },
  { id: 'harvest',     icon: '🔪', label: 'Harvest Planning',  href: 'harvest.html' },
  { id: 'wellboat',    icon: '📅', label: 'Well-Boat Schedule',href: 'wellboat.html' },
  { section: 'Compliance' },
  { id: 'compliance',  icon: '📋', label: 'Regulatory Reports',href: 'compliance.html', badge: () => 2, badgeClass:'badge teal' },
  { id: 'escape',      icon: '🏛', label: 'Escape Register',   href: 'escape.html' },
  { section: 'Analytics' },
  { id: 'kpis',        icon: '📊', label: 'Farming KPIs',      href: 'kpis.html' },
  { id: 'genreport',   icon: '🧬', label: 'Generation Report', href: 'genreport.html' },
  { section: 'Reference' },
  { id: 'architecture',     icon: '🏗', label: 'Architecture',         href: 'architecture.html' },
  { id: 'erd',              icon: '🔷', label: 'Data Model ERD',       href: 'erd.html' },
  { id: 'erd-schema',       icon: '📐', label: 'Schema Reference',     href: 'erd-schema.html' },
  { id: 'integration-graph',icon: '🕸', label: 'Integration Graph',    href: 'integration-graph.html' },
  { id: 'settings',         icon: '⚙️', label: 'Settings',             href: 'settings.html' },
];

const TOP_NAV = [
  { id:'index',       label:'🏠 Home',       href:'index.html' },
  { id:'sites',       label:'🗺 Sites',       href:'sites.html' },
  { id:'sea-ops',     label:'🐟 Sea Ops',    href:'sea-ops.html' },
  { id:'lice',        label:'🦐 Lice',       href:'lice.html' },
  { id:'harvest',     label:'🔪 Harvest',    href:'harvest.html' },
  { id:'health',      label:'⚕️ Health',     href:'health.html' },
  { id:'compliance',  label:'📋 Compliance', href:'compliance.html' },
  { id:'architecture',label:'🏗 Architecture',href:'architecture.html' },
];

function renderNav(activeId) {
  // Inject topbar
  const tb = document.createElement('div');
  tb.id = 'topbar';
  tb.innerHTML = `
    <div class="logo">Aqua<span>Monitor</span></div>
    <div class="env-badge">DEMO · NordHav Aquaculture AS</div>
    <div class="spacer"></div>
    <nav class="top-nav">
      ${TOP_NAV.map(n=>`<a href="${n.href}" class="${n.id===activeId?'active':''}">${n.label}</a>`).join('')}
    </nav>
    <div class="user"><div class="avatar">KH</div><span>Knut Helgesen · Farming Mgr</span></div>`;
  document.body.insertBefore(tb, document.body.firstChild);

  // Inject sidebar
  const sb = document.getElementById('sidebar');
  if (!sb) return;
  sb.innerHTML = NAV_ITEMS.map(item => {
    if (item.section) return `<div class="nav-section">${item.section}</div>`;
    const badgeCount = item.badge ? item.badge() : 0;
    const badgeHtml  = (badgeCount > 0) ? `<span class="${item.badgeClass||'badge'}">${badgeCount}</span>` : '';
    return `<a href="${item.href}" class="nav-item${item.id===activeId?' active':''}">
      <span class="icon">${item.icon}</span>${item.label}${badgeHtml}
    </a>`;
  }).join('');
}
