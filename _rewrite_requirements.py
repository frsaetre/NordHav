"""Rewrite customer-requirements.html with redesigned content focused on requirements only."""
import pathlib

TARGET = pathlib.Path(__file__).parent / "customer-requirements.html"

NEW_CONTENT = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NordHav AquaMonitor &mdash; Requirements Overview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="_shared.css">
<style>
.hero{position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:url('FishFarm.png') center/cover no-repeat;opacity:.12;z-index:0;pointer-events:none;filter:saturate(.35) brightness(.7)}
.hero>*{position:relative;z-index:1}

.req-bar{display:flex;align-items:center;gap:.75rem;margin:.5rem 0}
.req-bar-label{font-size:.78rem;font-weight:600;color:var(--text);width:200px;flex-shrink:0}
.req-bar-track{flex:1;height:28px;background:var(--card2);border-radius:6px;position:relative;overflow:hidden}
.req-bar-fill{height:100%;border-radius:6px;display:flex;align-items:center;justify-content:flex-end;padding-right:.6rem;font-size:.72rem;font-weight:700;color:var(--bg);transition:width .8s ease}
.req-bar-count{font-size:.78rem;font-weight:700;color:var(--text);width:36px;text-align:right;flex-shrink:0}

.info-block{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem;position:relative;overflow:hidden}
.info-block::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,var(--glow),transparent);opacity:0;transition:opacity .35s}
.info-block:hover::before{opacity:1}
.info-block h3{font-size:1rem;font-weight:600;margin-bottom:.5rem;display:flex;align-items:center;gap:.5rem}
.info-block p,.info-block li{font-size:.86rem;color:var(--muted);line-height:1.65}
.info-block ul{list-style:none;padding:0}
.info-block ul li{padding:.3rem 0;padding-left:1.2rem;position:relative}
.info-block ul li::before{content:'&#x203A;';position:absolute;left:0;color:var(--primary);font-weight:700}

.company-card{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin:2rem 0}
.company-card-full{grid-column:1/-1}
@media(max-width:768px){.company-card{grid-template-columns:1fr}}

.split-section{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin:2rem 0}
@media(max-width:900px){.split-section{grid-template-columns:1fr}}

/* Category section cards */
.cat-section{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:2rem;margin-bottom:1.5rem;position:relative;overflow:hidden;transition:all .3s}
.cat-section:hover{border-color:rgba(0,180,216,.3)}
.cat-section::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.cat-fin::before{background:linear-gradient(90deg,var(--success),#34d399)}
.cat-aqu::before{background:linear-gradient(90deg,var(--primary),var(--secondary))}
.cat-prc::before{background:linear-gradient(90deg,var(--accent),#f59e0b)}
.cat-scm::before{background:linear-gradient(90deg,#90e0ef,var(--secondary))}
.cat-qac::before{background:linear-gradient(90deg,#8b5cf6,#a78bfa)}
.cat-hrp::before{background:linear-gradient(90deg,var(--danger),#f472b6)}
.cat-tec::before{background:linear-gradient(90deg,var(--secondary),var(--primary))}
.cat-header{display:flex;align-items:center;gap:1.25rem;margin-bottom:1.25rem;flex-wrap:wrap}
.cat-icon{font-size:2rem;flex-shrink:0}
.cat-title{font-family:'Space Grotesk',sans-serif;font-size:1.3rem;font-weight:700}
.cat-count{font-family:'Space Grotesk',sans-serif;font-size:1.1rem;font-weight:700;color:var(--primary);background:rgba(0,180,216,.1);border-radius:8px;padding:.3rem .85rem;margin-left:auto}
.cat-meta{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:1rem}
.cat-pill{display:inline-flex;align-items:center;gap:.35rem;padding:.2rem .6rem;border-radius:6px;font-size:.72rem;font-weight:600}
.cat-pill-m{background:rgba(239,71,111,.1);color:var(--danger)}
.cat-pill-h{background:rgba(252,163,17,.1);color:var(--accent)}
.cat-pill-d{background:rgba(106,143,168,.1);color:var(--muted)}
.cat-desc{font-size:.88rem;color:var(--muted);line-height:1.65;margin-bottom:1rem}
.cat-highlights{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:.75rem;margin-bottom:1.25rem}
.cat-highlight{background:rgba(0,180,216,.04);border:1px solid rgba(0,180,216,.1);border-radius:10px;padding:.85rem;font-size:.82rem;color:var(--text);line-height:1.5}
.cat-highlight strong{color:var(--primary);font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:.25rem}
.cat-links{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1rem}
.cat-link{display:inline-flex;align-items:center;gap:.35rem;font-size:.82rem;font-weight:600;color:var(--primary);text-decoration:none;padding:.35rem .85rem;border:1px solid rgba(0,180,216,.2);border-radius:8px;transition:all .2s}
.cat-link:hover{background:rgba(0,180,216,.1);border-color:var(--primary)}

.milestone-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem;margin:1.5rem 0}
.milestone-card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.25rem;transition:all .3s}
.milestone-card:hover{border-color:rgba(0,180,216,.35);transform:translateY(-2px)}
.milestone-date{font-family:'Space Grotesk',sans-serif;font-size:.8rem;font-weight:700;color:var(--primary);margin-bottom:.25rem}
.milestone-name{font-size:.88rem;font-weight:600;color:var(--text)}
.milestone-card.done{border-left:3px solid var(--success)}
.milestone-card.active{border-left:3px solid var(--accent)}
.milestone-card.future{border-left:3px solid var(--dim)}

.objective-list{counter-reset:obj;list-style:none;padding:0;margin:1rem 0}
.objective-list li{counter-increment:obj;position:relative;padding:.75rem 0 .75rem 2.5rem;border-bottom:1px solid rgba(255,255,255,.04);font-size:.86rem;color:var(--muted);line-height:1.6}
.objective-list li::before{content:counter(obj);position:absolute;left:0;top:.7rem;width:1.8rem;height:1.8rem;border-radius:50%;background:rgba(0,180,216,.12);color:var(--primary);font-family:'Space Grotesk',sans-serif;font-size:.78rem;font-weight:700;display:flex;align-items:center;justify-content:center}
.objective-list li strong{color:var(--text)}

@media(max-width:768px){
  .req-bar-label{width:120px;font-size:.72rem}
  .cat-header{gap:.75rem}
  .cat-count{margin-left:0}
  .cat-highlights{grid-template-columns:1fr}
  .milestone-grid{grid-template-columns:1fr}
}
@media(max-width:480px){
  .req-bar{flex-direction:column;align-items:stretch;gap:.35rem}
  .req-bar-label{width:auto}
  .req-bar-count{text-align:left}
}
</style>
</head>
<body>
<canvas id="bg-canvas"></canvas>

<nav>
  <a class="nav-logo" href="index.html">
    <svg height="28" viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg"><g class="logo-fill"><circle cx="126" cy="70" r="5.5"/><circle cx="151" cy="73" r="5.1"/><circle cx="178" cy="76" r="4.8"/><circle cx="205" cy="79" r="4.6"/><circle cx="232" cy="81" r="4.5"/><circle cx="260" cy="83" r="4.4"/><circle cx="288" cy="81" r="4.5"/><circle cx="315" cy="79" r="4.6"/><circle cx="341" cy="76" r="4.8"/><circle cx="366" cy="73" r="5.1"/><circle cx="390" cy="70" r="5.5"/><circle cx="260" cy="130" r="3.3"/><circle cx="210" cy="130" r="4.4"/><circle cx="310" cy="130" r="4.4"/><path d="M0 170 V100 H12 L35 145 V100 H47 V170 H35 L12 125 V170Z"/><path d="M70 100 C88 100 100 115 100 135 C100 155 88 170 70 170 C52 170 40 155 40 135 C40 115 52 100 70 100ZM70 114 C62 114 56 123 56 135 C56 147 62 156 70 156 C78 156 84 147 84 135 C84 123 78 114 70 114Z" transform="translate(60,0)"/><path d="M0 170 V100 H28 C42 100 46 108 46 120 C46 130 40 138 30 140 L46 170 H34 L19 141 H13 V170Z M13 129 H28 C34 129 35 126 35 120 C35 114 34 112 28 112 H13Z" transform="translate(170,0)"/><path d="M0 170 V100 H28 C48 100 50 116 50 135 C50 154 48 170 28 170ZM14 156 H28 C36 156 37 145 37 135 C37 125 36 114 28 114 H14Z" transform="translate(240,0)"/><path d="M0 170 V100 H14 V129 H36 V100 H50 V170 H36 V143 H14 V170Z" transform="translate(310,0)"/><path d="M20 100 L0 170 H12 L18 148 H38 L44 170 H56 L36 100ZM28 118 L21 138 H35Z" transform="translate(372,0)"/><path d="M0 100 H14 L32 152 L50 100 H64 L38 170 H26Z" transform="translate(438,0)"/></g></svg>
    <span class="nav-wordmark">ERP AI Response Demo</span>
  </a>
  <div class="nav-links">
    <a href="company.html" class="nav-link">Company</a>
    <a href="customer-requirements.html" class="nav-link active">Requirements</a>
    <a href="architecture.html" class="nav-link">Architecture</a>
    <a href="d365-coverage.html" class="nav-link">D365</a>
    <a href="integrations.html" class="nav-link">Integration</a>
    <a href="analytics.html" class="nav-link">Analytics</a>
    <a href="rollout.html" class="nav-link">Rollout</a>
    <a href="tco-roi.html" class="nav-link">TCO &amp; ROI</a>
  </div>
</nav>

<!-- HERO -->
<section class="hero" style="min-height:72vh">
  <div class="hero-eyebrow">
    <svg width="7" height="7" viewBox="0 0 7 7"><circle cx="3.5" cy="3.5" r="3.5" fill="#06d6a0"/></svg>
    RFP Response &middot; NHA-RFP-2026-001 &middot; Requirements Analysis
  </div>
  <h1>441 Requirements &middot; 7 Domains</h1>
  <p class="hero-sub">Comprehensive requirements analysis for NordHav Aquaculture&rsquo;s ERP transformation &mdash; spanning finance, aquaculture, processing, supply chain, quality, HR, and technology. Each requirement mapped to Dynamics 365 F&amp;O and the AquaMonitor platform.</p>
  <div class="hero-meta">
    <div class="hero-meta-item"><div class="hero-meta-val">441</div><div class="hero-meta-lbl">Total Requirements</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:var(--danger)">213</div><div class="hero-meta-lbl">Mandatory</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val" style="color:var(--accent)">183</div><div class="hero-meta-lbl">High Priority</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val">45</div><div class="hero-meta-lbl">Desirable</div></div>
    <div class="hero-meta-item"><div class="hero-meta-val">7</div><div class="hero-meta-lbl">Domains</div></div>
  </div>
  <div class="scroll-hint">&#x25BC; scroll to explore</div>
</section>

<!-- OVERVIEW -->
<section class="section" id="overview">
  <div class="section-inner">
    <div class="section-tag reveal">Overview</div>
    <h2 class="section-title reveal">Requirements Distribution</h2>
    <p class="section-sub reveal">48% Mandatory &middot; 42% High &middot; 10% Desirable &mdash; every domain mapped to D365 F&amp;O modules and the AquaMonitor Power Platform layer.</p>

    <div class="info-block reveal" style="margin-bottom:2rem">
      <h3 style="margin-bottom:1rem">By Domain</h3>
      <div class="req-bar"><span class="req-bar-label">Aquaculture Operations</span><div class="req-bar-track"><div class="req-bar-fill" style="width:18.1%;background:var(--primary)">80</div></div><span class="req-bar-count">80</span></div>
      <div class="req-bar"><span class="req-bar-label">Technology &amp; Integration</span><div class="req-bar-track"><div class="req-bar-fill" style="width:18.1%;background:var(--secondary)">80</div></div><span class="req-bar-count">80</span></div>
      <div class="req-bar"><span class="req-bar-label">Finance &amp; Accounting</span><div class="req-bar-track"><div class="req-bar-fill" style="width:17.5%;background:var(--success)">77</div></div><span class="req-bar-count">77</span></div>
      <div class="req-bar"><span class="req-bar-label">Processing &amp; VAP</span><div class="req-bar-track"><div class="req-bar-fill" style="width:15.2%;background:var(--accent)">67</div></div><span class="req-bar-count">67</span></div>
      <div class="req-bar"><span class="req-bar-label">Supply Chain &amp; Logistics</span><div class="req-bar-track"><div class="req-bar-fill" style="width:11.8%;background:#90e0ef">52</div></div><span class="req-bar-count">52</span></div>
      <div class="req-bar"><span class="req-bar-label">HR &amp; Payroll</span><div class="req-bar-track"><div class="req-bar-fill" style="width:10.2%;background:var(--danger)">45</div></div><span class="req-bar-count">45</span></div>
      <div class="req-bar"><span class="req-bar-label">Quality &amp; Compliance</span><div class="req-bar-track"><div class="req-bar-fill" style="width:9.1%;background:var(--dim)">40</div></div><span class="req-bar-count">40</span></div>
    </div>

    <div class="kpi-grid stagger">
      <div class="kpi-card danger"><div class="kpi-val">213</div><div class="kpi-lbl">Mandatory (M)</div></div>
      <div class="kpi-card accent"><div class="kpi-val">183</div><div class="kpi-lbl">High (H)</div></div>
      <div class="kpi-card"><div class="kpi-val">45</div><div class="kpi-lbl">Desirable (D)</div></div>
      <div class="kpi-card success"><div class="kpi-val">441</div><div class="kpi-lbl">Total</div></div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- PER-CATEGORY SECTIONS -->
<section class="section" id="categories">
  <div class="section-inner">
    <div class="section-tag reveal">Requirement Domains</div>
    <h2 class="section-title reveal">Deep Dive by Category</h2>
    <p class="section-sub reveal">Each of the 7 requirement domains analyzed in detail &mdash; key capabilities, priority breakdown, critical highlights, and full requirement listings.</p>

    <!-- FINANCE -->
    <div class="cat-section cat-fin reveal" id="cat-finance">
      <div class="cat-header">
        <div class="cat-icon">&#x1F4B0;</div>
        <div class="cat-title">Finance &amp; Accounting</div>
        <div class="cat-count">77 requirements</div>
      </div>
      <div class="cat-meta">
        <span class="cat-pill cat-pill-m">&#x1F534; 45 Mandatory</span>
        <span class="cat-pill cat-pill-h">&#x1F7E1; 27 High</span>
        <span class="cat-pill cat-pill-d">&#x26AA; 5 Desirable</span>
      </div>
      <div class="cat-desc">Complete Norwegian localized finance covering General Ledger, Accounts Payable &amp; Receivable, Cash &amp; Bank, Fixed Assets, Tax, Cost Management, and Biological Asset Accounting. Special focus on aquaculture-specific features: Fish Generation financial dimension for lifecycle P&amp;L, IAS 41/NRS 8 biological asset valuation, grunnrenteskatt (resource rent tax), and cost-per-kg tracking across the full value chain.</div>
      <div class="cat-highlights">
        <div class="cat-highlight"><strong>Norwegian Chart of Accounts</strong>NS 4102 standard, Fish Generation dimension, 4-segment structure enabling P&amp;L per generation batch.</div>
        <div class="cat-highlight"><strong>Biological Asset Accounting</strong>IAS 41 / NRS 8 fair-value measurement of live fish biomass. Monthly revaluation with automatic GL postings.</div>
        <div class="cat-highlight"><strong>Tax &amp; Compliance</strong>SAF-T Norway, MVA (VAT), EHF e-invoicing, grunnrenteskatt (25% resource rent tax from 2024), A-melding payroll reporting.</div>
        <div class="cat-highlight"><strong>Cost Per Kilogram</strong>Full cost allocation from smolt &#x2192; sea &#x2192; harvest, enabling generation-level profitability analysis and cost driver tracking.</div>
        <div class="cat-highlight"><strong>Multi-Currency</strong>Sales in EUR, GBP, USD, JPY. Hedging workflow support. Norwegian banking integration (IBAN/BBAN, BankID, Nets).</div>
        <div class="cat-highlight"><strong>Month-End Close</strong>Target: 3 days (down from 15+ with legacy). Automated biomass accruals, intercompany elimination.</div>
      </div>
      <div class="cat-links">
        <a href="req-finance.html" class="cat-link">&#x1F4CB; All 77 Requirements &#x2192;</a>
        <a href="ans-finance.html" class="cat-link">&#x2705; Solution Answers &#x2192;</a>
      </div>
    </div>

    <!-- AQUACULTURE -->
    <div class="cat-section cat-aqu reveal" id="cat-aquaculture">
      <div class="cat-header">
        <div class="cat-icon">&#x1F41F;</div>
        <div class="cat-title">Aquaculture Operations</div>
        <div class="cat-count">80 requirements</div>
      </div>
      <div class="cat-meta">
        <span class="cat-pill cat-pill-m">&#x1F534; 42 Mandatory</span>
        <span class="cat-pill cat-pill-h">&#x1F7E1; 30 High</span>
        <span class="cat-pill cat-pill-d">&#x26AA; 8 Desirable</span>
      </div>
      <div class="cat-desc">The heart of NordHav&rsquo;s operations &mdash; from smolt production through sea farming to harvest. Covers production planning (3&ndash;5 year horizon), site/pen registers, MAB monitoring, biomass estimation, feed management, sea lice control, fish health, mortality tracking, harvest coordination, and environmental monitoring. This is the domain where AquaMonitor MDA provides the primary user interface.</div>
      <div class="cat-highlights">
        <div class="cat-highlight"><strong>Smolt &amp; Post-Smolt</strong>3 RAS facilities, 20M smolt/year. Tank management, vaccination tracking, degree-day calculations, grading events, smoltification criteria.</div>
        <div class="cat-highlight"><strong>Sea Farming &amp; Biomass</strong>28 licenses, 180 pens. Daily biomass estimation, growth models, stocking density, pen-level inventory, catch-weight tracking.</div>
        <div class="cat-highlight"><strong>Feed Management</strong>Real-time IoT consumption from AKVA feed barges. Feed conversion ratio (FCR) tracking per pen/generation. Automatic D365 inventory postings.</div>
        <div class="cat-highlight"><strong>Sea Lice &amp; Fish Health</strong>Weekly lice counts, treatment records, veterinary prescriptions, withdrawal period enforcement, Mattilsynet reporting automation.</div>
        <div class="cat-highlight"><strong>Harvest Coordination</strong>7-stage Business Process Flow from planning to site close-out. D365 production order integration. Well-boat logistics.</div>
        <div class="cat-highlight"><strong>Regulatory Reporting</strong>BarentsWatch biomass/lice submission, Altinn reporting, Fiskeridirektoratet volume data &mdash; all automated via Power Automate.</div>
      </div>
      <div class="cat-links">
        <a href="req-aquaculture.html" class="cat-link">&#x1F4CB; All 80 Requirements &#x2192;</a>
        <a href="ans-aquaculture.html" class="cat-link">&#x2705; Solution Answers &#x2192;</a>
      </div>
    </div>

    <!-- PROCESSING -->
    <div class="cat-section cat-prc reveal" id="cat-processing">
      <div class="cat-header">
        <div class="cat-icon">&#x1F3ED;</div>
        <div class="cat-title">Processing &amp; VAP</div>
        <div class="cat-count">67 requirements</div>
      </div>
      <div class="cat-meta">
        <span class="cat-pill cat-pill-m">&#x1F534; 35 Mandatory</span>
        <span class="cat-pill cat-pill-h">&#x1F7E1; 25 High</span>
        <span class="cat-pill cat-pill-d">&#x26AA; 7 Desirable</span>
      </div>
      <div class="cat-desc">Austevoll processing plant operations: 180t/day primary processing and 60t/day value-added products. Covers harvest reception, stunning/slaughter, in-line weighing, yield tracking, catch-weight conversion, GS1 labeling, recipe management, OEE, cold chain monitoring, packaging, dispatch, and by-product costing across ~165 SKUs.</div>
      <div class="cat-highlights">
        <div class="cat-highlight"><strong>Harvest Reception</strong>Well-boat intake, live weight vs. gutted weight conversion, quality grading (Superior/Ordinary/Production), real-time weight capture.</div>
        <div class="cat-highlight"><strong>Production Control</strong>D365 manufacturing with Marel Innova integration. Route-based operations: slaughter &#x2192; gutting &#x2192; filleting &#x2192; packing. Yield % per step.</div>
        <div class="cat-highlight"><strong>Value-Added Products</strong>60t/day VAP: smoked, marinated, portions, meal kits. Recipe/BOM management, batch traceability, allergen tracking.</div>
        <div class="cat-highlight"><strong>GS1 &amp; Labeling</strong>SSCC generation, GS1-128 barcodes, labels in 10+ languages (NO, EN, FR, DE, ES, IT, JP, KR, ZH). Customer-specific formats.</div>
        <div class="cat-highlight"><strong>Cold Chain</strong>Temperature monitoring from slaughter through dispatch. IoT sensors on cold storage, packing lines, and transport vehicles.</div>
        <div class="cat-highlight"><strong>By-Product Costing</strong>Fish oil, fish meal, roe. Full cost allocation back to production batches. Revenue recognition per by-product stream.</div>
      </div>
      <div class="cat-links">
        <a href="req-processing.html" class="cat-link">&#x1F4CB; All 67 Requirements &#x2192;</a>
        <a href="ans-processing.html" class="cat-link">&#x2705; Solution Answers &#x2192;</a>
      </div>
    </div>

    <!-- SUPPLY CHAIN -->
    <div class="cat-section cat-scm reveal" id="cat-supply-chain">
      <div class="cat-header">
        <div class="cat-icon">&#x1F4E6;</div>
        <div class="cat-title">Supply Chain &amp; Logistics</div>
        <div class="cat-count">52 requirements</div>
      </div>
      <div class="cat-meta">
        <span class="cat-pill cat-pill-m">&#x1F534; 28 Mandatory</span>
        <span class="cat-pill cat-pill-h">&#x1F7E1; 20 High</span>
        <span class="cat-pill cat-pill-d">&#x26AA; 4 Desirable</span>
      </div>
      <div class="cat-desc">End-to-end supply chain from procurement through distribution. Covers sales order management with EDI integration, contract vs. spot allocation, variable-weight invoicing, procurement workflows, vendor management with certificate tracking, cold storage warehouse management, transport planning, and demand forecasting for the ~350 global customer base.</div>
      <div class="cat-highlights">
        <div class="cat-highlight"><strong>Sales &amp; Distribution</strong>~350 customers, contract/spot split. Variable-weight invoicing, catch-weight pricing, multi-currency, EU/Asia/NA market-specific rules.</div>
        <div class="cat-highlight"><strong>Procurement</strong>Feed (largest cost &mdash; 55% of COGS), packaging, chemicals, equipment. RFQ workflows, purchase agreements, vendor certificate management.</div>
        <div class="cat-highlight"><strong>Inventory &amp; Warehouse</strong>Cold storage WMS at Austevoll. Batch/lot tracking, FIFO/FEFO rotation, pen-level inventory for live fish, catch-weight adjustment journals.</div>
        <div class="cat-highlight"><strong>Transport &amp; Logistics</strong>Well-boat coordination, live fish transport (4&ndash;36 hr), cold chain freight, export documentation, Incoterms management.</div>
      </div>
      <div class="cat-links">
        <a href="req-supply-chain.html" class="cat-link">&#x1F4CB; All 52 Requirements &#x2192;</a>
        <a href="ans-supply-chain.html" class="cat-link">&#x2705; Solution Answers &#x2192;</a>
      </div>
    </div>

    <!-- QUALITY -->
    <div class="cat-section cat-qac reveal" id="cat-quality">
      <div class="cat-header">
        <div class="cat-icon">&#x2705;</div>
        <div class="cat-title">Quality &amp; Compliance</div>
        <div class="cat-count">40 requirements</div>
      </div>
      <div class="cat-meta">
        <span class="cat-pill cat-pill-m">&#x1F534; 25 Mandatory</span>
        <span class="cat-pill cat-pill-h">&#x1F7E1; 12 High</span>
        <span class="cat-pill cat-pill-d">&#x26AA; 3 Desirable</span>
      </div>
      <div class="cat-desc">Quality management system supporting 9 certifications (ASC, GlobalG.A.P., BRC, FSSC 22000, ISO 14001/22000/45001, SBTi, UNGC). Covers QMS document control, HACCP/CCP monitoring, non-conformance and CAPA workflows, LIMS integration, full egg-to-customer traceability, recall management, HSE, and environmental monitoring.</div>
      <div class="cat-highlights">
        <div class="cat-highlight"><strong>Full Traceability</strong>End-to-end: egg batch &#x2192; smolt &#x2192; sea pen &#x2192; harvest batch &#x2192; processing lot &#x2192; pallet/case &#x2192; customer. Single query across D365 + Dataverse.</div>
        <div class="cat-highlight"><strong>HACCP &amp; CCP</strong>Critical Control Point monitoring integrated with processing. Automated alerts on deviation. Corrective action workflow.</div>
        <div class="cat-highlight"><strong>LIMS Integration</strong>LabWare LIMS 7.x bidirectional integration. Sample results flow to D365 Quality Orders. Auto-release or hold based on specs.</div>
        <div class="cat-highlight"><strong>Recall Management</strong>Mock recall in &lt;4 hours. Forward/backward trace from any point. Automated customer notification workflow.</div>
      </div>
      <div class="cat-links">
        <a href="req-quality.html" class="cat-link">&#x1F4CB; All 40 Requirements &#x2192;</a>
        <a href="ans-quality.html" class="cat-link">&#x2705; Solution Answers &#x2192;</a>
      </div>
    </div>

    <!-- HR -->
    <div class="cat-section cat-hrp reveal" id="cat-hr">
      <div class="cat-header">
        <div class="cat-icon">&#x1F465;</div>
        <div class="cat-title">HR &amp; Payroll</div>
        <div class="cat-count">45 requirements</div>
      </div>
      <div class="cat-meta">
        <span class="cat-pill cat-pill-m">&#x1F534; 20 Mandatory</span>
        <span class="cat-pill cat-pill-h">&#x1F7E1; 18 High</span>
        <span class="cat-pill cat-pill-d">&#x26AA; 7 Desirable</span>
      </div>
      <div class="cat-desc">Full Norwegian HR and payroll covering 820 employees (peak 905 with seasonal workers). A-melding reporting, OTP pension, feriepenger holiday pay, collective agreements (NNN + Fellesforbundet), multi-shift patterns, Arbeidsmilj&oslash;loven compliance, employee self-service, competency management, and training tracking including mandatory maritime and safety certifications.</div>
      <div class="cat-highlights">
        <div class="cat-highlight"><strong>Norwegian Payroll</strong>A-melding electronic reporting, OTP pension calculation, feriepenger (holiday pay), sykepenger (sick pay), collective agreement rate tables.</div>
        <div class="cat-highlight"><strong>Shift &amp; Time Management</strong>2-shift (processing), 3-shift/24&#xD7;7 (smolt), offshore rotation (sea sites), hybrid office. Overtime, night premiums, weekend rates.</div>
        <div class="cat-highlight"><strong>Seasonal Workers</strong>+85 staff Aug&ndash;Dec peak. Rapid onboarding, temporary contracts, competency verification before site access.</div>
        <div class="cat-highlight"><strong>Training &amp; Certifications</strong>Mandatory maritime safety, chemical handling, fish welfare. Expiry alerts, compliance dashboards, training history.</div>
      </div>
      <div class="cat-links">
        <a href="req-hr.html" class="cat-link">&#x1F4CB; All 45 Requirements &#x2192;</a>
        <a href="ans-hr.html" class="cat-link">&#x2705; Solution Answers &#x2192;</a>
      </div>
    </div>

    <!-- TECHNOLOGY -->
    <div class="cat-section cat-tec reveal" id="cat-technology">
      <div class="cat-header">
        <div class="cat-icon">&#x2699;&#xFE0F;</div>
        <div class="cat-title">Technology &amp; Integration</div>
        <div class="cat-count">80 requirements</div>
      </div>
      <div class="cat-meta">
        <span class="cat-pill cat-pill-m">&#x1F534; 38 Mandatory</span>
        <span class="cat-pill cat-pill-h">&#x1F7E1; 31 High</span>
        <span class="cat-pill cat-pill-d">&#x26AA; 11 Desirable</span>
      </div>
      <div class="cat-desc">Platform architecture, cloud infrastructure, integration patterns, security, and operational requirements. Cloud SaaS with EU/Norwegian data residency, SSO via Entra ID, REST/OData API-first architecture, IoT integration for feed barges and environmental sensors, mobile with offline capability for sea sites, Power BI analytics, GDPR compliance, and 99.5% uptime SLA.</div>
      <div class="cat-highlights">
        <div class="cat-highlight"><strong>Cloud &amp; Data Residency</strong>Azure North Europe (Norway East). Full EU GDPR compliance. Data sovereignty guaranteed &mdash; no data leaves EU jurisdiction.</div>
        <div class="cat-highlight"><strong>API &amp; Integration</strong>REST/OData API-first. 22 AKVA IoT devices, 130+ environmental sensors, BarentsWatch/Altinn/Mattilsynet regulatory APIs, Marel Innova.</div>
        <div class="cat-highlight"><strong>Mobile &amp; Offline</strong>Sea-site workers need offline-capable mobile apps (mortality, lice counts, observations). Auto-sync when connectivity returns.</div>
        <div class="cat-highlight"><strong>Security &amp; Identity</strong>SSO via Entra ID, MFA, role-based access, row-level security in Power BI, audit trail, penetration testing annually.</div>
        <div class="cat-highlight"><strong>SLA &amp; DR</strong>99.5% uptime, RPO &lt;1h, RTO &lt;4h. Geo-redundant backup. Automated failover. 24/7 monitoring.</div>
        <div class="cat-highlight"><strong>Analytics Platform</strong>Power BI + Microsoft Fabric. 8 report domains, shared semantic model, real-time operational dashboards embedded in MDA.</div>
      </div>
      <div class="cat-links">
        <a href="req-technology.html" class="cat-link">&#x1F4CB; All 80 Requirements &#x2192;</a>
        <a href="ans-technology.html" class="cat-link">&#x2705; Solution Answers &#x2192;</a>
      </div>
    </div>

  </div>
</section>

<div class="divider"></div>

<!-- PROJECT OBJECTIVES -->
<section class="section" id="project-objectives">
  <div class="section-inner">
    <div class="section-tag reveal">Project Objectives</div>
    <h2 class="section-title reveal">What NordHav Needs From This ERP</h2>

    <div class="company-card stagger">
      <div class="info-block">
        <h3>&#x1F3AF; Primary Objectives</h3>
        <ol class="objective-list">
          <li><strong>Unified Platform:</strong> Replace 12+ fragmented systems with a single integrated ERP across all locations and business functions.</li>
          <li><strong>End-to-End Traceability:</strong> Full traceability from egg/smolt &#x2192; sea &#x2192; harvest &#x2192; processing &#x2192; delivery, meeting ASC/BRC/GlobalG.A.P./regulatory requirements.</li>
          <li><strong>Operational Efficiency:</strong> Eliminate manual data entry, spreadsheet planning, and paper workflows. Enable real-time cross-functional visibility.</li>
          <li><strong>Regulatory Compliance:</strong> SAF-T, MVA, grunnrenteskatt, A-melding, BarentsWatch lice reporting, food safety &mdash; all automated, all audit-ready.</li>
          <li><strong>Scalability:</strong> Support growth from 52k &#x2192; 75k tonnes GWE and VAP doubling without architecture changes.</li>
          <li><strong>Data-driven Decisions:</strong> Real-time dashboards and analytics: biomass, FCR, lice, generation P&amp;L, cost-per-kg, cash flow.</li>
          <li><strong>Industry Fit:</strong> Aquaculture-specific functionality for fish farming, seafood processing, cold-chain logistics, and biological asset accounting.</li>
        </ol>
      </div>
      <div class="info-block">
        <h3>&#x1F6E1;&#xFE0F; Technical Requirements</h3>
        <div class="table-wrap" style="margin:0">
          <table class="data-table" style="font-size:.8rem">
            <thead><tr><th>Requirement</th><th>Priority</th></tr></thead>
            <tbody>
              <tr><td>Cloud SaaS deployment</td><td><span class="badge badge-m">M</span></td></tr>
              <tr><td>Norwegian / EU data residency</td><td><span class="badge badge-m">M</span></td></tr>
              <tr><td>SSO via Entra ID</td><td><span class="badge badge-m">M</span></td></tr>
              <tr><td>Mobile + offline for sea sites</td><td><span class="badge badge-h">H</span></td></tr>
              <tr><td>REST / OData API-first architecture</td><td><span class="badge badge-h">H</span></td></tr>
              <tr><td>Multi-language UI (NO + EN)</td><td><span class="badge badge-m">M</span></td></tr>
              <tr><td>Role-based access control</td><td><span class="badge badge-m">M</span></td></tr>
              <tr><td>Full audit trail</td><td><span class="badge badge-m">M</span></td></tr>
              <tr><td>99.5% uptime SLA</td><td><span class="badge badge-h">H</span></td></tr>
              <tr><td>DR: RPO &lt;1h, RTO &lt;4h</td><td><span class="badge badge-h">H</span></td></tr>
              <tr><td>SAF-T + EHF support</td><td><span class="badge badge-m">M</span></td></tr>
              <tr><td>GDPR compliance</td><td><span class="badge badge-m">M</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- EVALUATION CRITERIA -->
<section class="section" id="evaluation">
  <div class="section-inner">
    <div class="section-tag reveal">Evaluation</div>
    <h2 class="section-title reveal">Vendor Evaluation Framework</h2>
    <p class="section-sub reveal">10 scoring categories. Functional fit is 65% of the total score, with Aquaculture Operations weighted highest at 16%.</p>

    <div class="info-block reveal" style="margin-bottom:2rem">
      <h3 style="margin-bottom:1rem">Scoring Category Weights</h3>
      <div class="req-bar"><span class="req-bar-label">Aquaculture Operations</span><div class="req-bar-track"><div class="req-bar-fill" style="width:16%;background:var(--primary)">16%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">Processing &amp; VAP</span><div class="req-bar-track"><div class="req-bar-fill" style="width:14%;background:var(--accent)">14%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">Core Finance</span><div class="req-bar-track"><div class="req-bar-fill" style="width:12%;background:var(--success)">12%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">Supply Chain &amp; Logistics</span><div class="req-bar-track"><div class="req-bar-fill" style="width:10%;background:var(--secondary)">10%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">Technology &amp; Architecture</span><div class="req-bar-track"><div class="req-bar-fill" style="width:10%;background:var(--secondary)">10%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">Total Cost of Ownership</span><div class="req-bar-track"><div class="req-bar-fill" style="width:10%;background:var(--danger)">10%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">Quality &amp; Compliance</span><div class="req-bar-track"><div class="req-bar-fill" style="width:8%;background:var(--dim)">8%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">Vendor Credentials</span><div class="req-bar-track"><div class="req-bar-fill" style="width:8%;background:var(--dim)">8%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">Implementation Approach</span><div class="req-bar-track"><div class="req-bar-fill" style="width:7%;background:rgba(255,255,255,.1)">7%</div></div></div>
      <div class="req-bar"><span class="req-bar-label">HR &amp; Payroll</span><div class="req-bar-track"><div class="req-bar-fill" style="width:5%;background:rgba(255,255,255,.1)">5%</div></div></div>
    </div>

    <div class="split-section stagger">
      <div class="info-block">
        <h3>&#x1F4CA; Response Scoring</h3>
        <div class="table-wrap" style="margin:0">
          <table class="data-table" style="font-size:.8rem">
            <thead><tr><th>Code</th><th>Meaning</th><th>Points</th></tr></thead>
            <tbody>
              <tr><td><span class="badge badge-ok">S</span></td><td>Standard (native)</td><td>4</td></tr>
              <tr><td><span class="badge badge-ok">C</span></td><td>Configuration (no code)</td><td>3</td></tr>
              <tr><td><span class="badge badge-wip">P</span></td><td>Partner / ISV</td><td>2.5</td></tr>
              <tr><td><span class="badge badge-h">D</span></td><td>Custom development</td><td>2</td></tr>
              <tr><td><span class="badge badge-h">R</span></td><td>Roadmap (future)</td><td>1</td></tr>
              <tr><td><span class="badge badge-m">N</span></td><td>Not supported</td><td>0</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="info-block">
        <h3>&#x26A0;&#xFE0F; Mandatory Gate</h3>
        <p>If a vendor responds <strong style="color:var(--danger)">N</strong> to any <strong>Mandatory</strong> requirement, the committee reviews whether an acceptable workaround exists. If not, the vendor may be <strong>disqualified</strong>.</p>
        <p style="margin-top:.75rem">Minimum threshold: <strong style="color:var(--accent)">70%</strong> weighted coverage per functional category to proceed to demonstrations.</p>
        <div style="margin-top:1rem">
          <h4 style="font-size:.82rem;color:var(--muted);margin-bottom:.4rem">Priority Multipliers</h4>
          <div class="chips">
            <span class="chip chip-danger">Mandatory &#xD7; 3.0</span>
            <span class="chip chip-accent">High &#xD7; 2.0</span>
            <span class="chip">Desirable &#xD7; 1.0</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- TIMELINE -->
<section class="section" id="timeline">
  <div class="section-inner">
    <div class="section-tag reveal">Timeline</div>
    <h2 class="section-title reveal">Project Milestones</h2>

    <div class="milestone-grid stagger">
      <div class="milestone-card done"><div class="milestone-date">Feb 20, 2026</div><div class="milestone-name">RFP Issued</div></div>
      <div class="milestone-card active"><div class="milestone-date">Mar 13, 2026</div><div class="milestone-name">Vendor Q&amp;A Deadline</div></div>
      <div class="milestone-card future"><div class="milestone-date">Mar 20, 2026</div><div class="milestone-name">NordHav Q&amp;A Responses</div></div>
      <div class="milestone-card future"><div class="milestone-date">Apr 30, 2026</div><div class="milestone-name">Proposal Submission</div></div>
      <div class="milestone-card future"><div class="milestone-date">May 22, 2026</div><div class="milestone-name">Shortlist Announced</div></div>
      <div class="milestone-card future"><div class="milestone-date">Jun 8&ndash;19, 2026</div><div class="milestone-name">Vendor Demos (Bergen)</div></div>
      <div class="milestone-card future"><div class="milestone-date">Jul 2026</div><div class="milestone-name">Reference Visits</div></div>
      <div class="milestone-card future"><div class="milestone-date">Aug&ndash;Sep 2026</div><div class="milestone-name">Final Selection &amp; Contract</div></div>
      <div class="milestone-card future"><div class="milestone-date">Oct 2026</div><div class="milestone-name">Project Kickoff</div></div>
      <div class="milestone-card future"><div class="milestone-date">Q3 2027</div><div class="milestone-name">Phase 1 Go-Live (Finance, Core Ops)</div></div>
      <div class="milestone-card future"><div class="milestone-date">Q1 2028</div><div class="milestone-name">Phase 2 Go-Live (Processing, VAP)</div></div>
      <div class="milestone-card future"><div class="milestone-date">Q2 2028</div><div class="milestone-name">Full Operational Go-Live</div></div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- DATA VOLUMES -->
<section class="section" id="scale">
  <div class="section-inner">
    <div class="section-tag reveal">Scale</div>
    <h2 class="section-title reveal">Transaction &amp; Data Volumes</h2>
    <p class="section-sub reveal">Key annual throughput metrics the ERP platform must handle.</p>

    <div class="split-section stagger">
      <div class="info-block">
        <h3>&#x1F4DD; Transaction Volumes (annual)</h3>
        <div class="table-wrap" style="margin:0">
          <table class="data-table" style="font-size:.8rem">
            <tbody>
              <tr><td>GL journal entries</td><td style="text-align:right;font-weight:600">850,000</td></tr>
              <tr><td>Purchase invoice lines</td><td style="text-align:right;font-weight:600">95,000</td></tr>
              <tr><td>Sales invoice lines</td><td style="text-align:right;font-weight:600">135,000</td></tr>
              <tr><td>Inventory transactions</td><td style="text-align:right;font-weight:600">500,000</td></tr>
              <tr><td>Production / batch orders</td><td style="text-align:right;font-weight:600">8,500</td></tr>
              <tr><td>Quality test results</td><td style="text-align:right;font-weight:600">120,000</td></tr>
              <tr><td>Environmental sensor readings</td><td style="text-align:right;font-weight:600">1,752,000</td></tr>
              <tr><td>Time registration entries</td><td style="text-align:right;font-weight:600">299,300</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="info-block">
        <h3>&#x1F4C1; Master Data Volumes</h3>
        <div class="table-wrap" style="margin:0">
          <table class="data-table" style="font-size:.8rem">
            <tbody>
              <tr><td>Customers</td><td style="text-align:right;font-weight:600">~650</td></tr>
              <tr><td>Vendors / suppliers</td><td style="text-align:right;font-weight:600">~1,800</td></tr>
              <tr><td>Finished goods SKUs</td><td style="text-align:right;font-weight:600">~1,200</td></tr>
              <tr><td>Raw materials / feed / packaging</td><td style="text-align:right;font-weight:600">~3,500</td></tr>
              <tr><td>Equipment / assets</td><td style="text-align:right;font-weight:600">~4,200</td></tr>
              <tr><td>Chart of accounts</td><td style="text-align:right;font-weight:600">~2,500</td></tr>
              <tr><td>Active sea cages / pens</td><td style="text-align:right;font-weight:600">~180</td></tr>
              <tr><td>Production licenses</td><td style="text-align:right;font-weight:600">28</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- NAVIGATE -->
<section class="section">
  <div class="section-inner">
    <div class="cta-block reveal">
      <h2>Explore the Solution</h2>
      <p>See how Dynamics 365 F&amp;O + AquaMonitor addresses every one of these 441 requirements.</p>
      <div class="btn-row">
        <a href="architecture.html" class="btn btn-primary">Architecture &#x2192;</a>
        <a href="d365-coverage.html" class="btn btn-ghost">D365 Coverage</a>
        <a href="integrations.html" class="btn btn-ghost">Integrations</a>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-links">
    <a href="company.html">Company</a><a href="customer-requirements.html">Requirements</a><a href="architecture.html">Architecture</a>
    <a href="d365-coverage.html">D365</a><a href="integrations.html">Integration</a>
    <a href="analytics.html">Analytics</a><a href="rollout.html">Rollout</a><a href="tco-roi.html">TCO &amp; ROI</a>
  </div>
  <div class="footer-copy">NordHav Aquaculture AS &middot; D365 F&amp;O + AquaMonitor Solution &middot; March 2026 &middot; Confidential</div>
</footer>

<script>
window.tourSections = [
  { id:'overview', label:'Overview', text:'NordHav has defined 441 requirements across seven functional domains for their ERP transformation. The distribution is led by Aquaculture Operations and Technology at eighty requirements each, followed by Finance at seventy-seven, Processing at sixty-seven, Supply Chain at fifty-two, H.R. at forty-five, and Quality at forty. Of these, forty-eight percent are mandatory, forty-two percent are high priority, and ten percent are desirable.' },
  { id:'cat-finance', label:'Finance', text:'The Finance and Accounting domain contains seventy-seven requirements covering the full Norwegian financial landscape. Key areas include the NS 4102 chart of accounts with a Fish Generation financial dimension, biological asset accounting under IAS 41 and NRS 8, SAF-T compliance, grunnrenteskatt resource rent tax, EHF electronic invoicing, multi-currency operations, and cost-per-kilogram tracking across the entire value chain from smolt to customer.' },
  { id:'cat-aquaculture', label:'Aquaculture', text:'Aquaculture Operations is the heart of NordHav with eighty requirements spanning the full production cycle. From smolt production across three RAS facilities to sea farming with twenty-eight licenses and one hundred eighty pens, this domain covers biomass estimation, feed management with IoT integration, sea lice monitoring, fish health and veterinary workflows, harvest coordination through a seven-stage business process, and automated regulatory reporting to BarentsWatch and Mattilsynet.' },
  { id:'cat-processing', label:'Processing', text:'Processing and V.A.P. covers sixty-seven requirements for the Austevoll plant handling one hundred eighty tonnes per day of primary processing and sixty tonnes of value-added products. Key areas include harvest reception with catch-weight conversion, Marel Innova integration for production control, recipe and B.O.M. management for V.A.P., GS1 labeling in ten-plus languages, cold chain monitoring, and by-product costing for fish oil, meal, and roe.' },
  { id:'cat-supply-chain', label:'Supply Chain', text:'Supply Chain and Logistics contains fifty-two requirements covering procurement, sales, inventory, and transport. NordHav serves approximately 350 customers globally with a mix of contract and spot sales. Feed procurement represents fifty-five percent of cost of goods sold. Cold storage warehouse management, batch tracking with FIFO and FEFO rotation, and transport planning including well-boat coordination are critical capabilities.' },
  { id:'cat-quality', label:'Quality', text:'Quality and Compliance has forty requirements supporting NordHav\'s nine major certifications. The domain requires full egg-to-customer traceability with a single-query capability, HACCP and Critical Control Point monitoring integrated with processing, LabWare LIMS bidirectional integration, and recall management with a target of less than four hours for mock recalls.' },
  { id:'cat-hr', label:'HR & Payroll', text:'H.R. and Payroll covers forty-five requirements for eight hundred twenty employees with seasonal peaks of nine hundred five. Norwegian payroll compliance includes A-melding, O.T.P. pension, feriepenger, and collective agreement management for N.N.N. and Fellesforbundet. Multiple shift patterns across processing, smolt, and sea-site operations require flexible time management.' },
  { id:'cat-technology', label:'Technology', text:'Technology and Integration has eighty requirements defining the platform architecture. Cloud deployment on Azure North Europe with Norwegian data residency, Entra I.D. single sign-on, REST and OData A.P.I. integration architecture, IoT connectivity for twenty-two A.K.V.A. devices and one hundred thirty-plus environmental sensors, offline-capable mobile apps, and a 99.5 percent uptime S.L.A. with R.P.O. under one hour.' },
  { id:'project-objectives', label:'Objectives', text:'NordHav has defined seven primary objectives: a unified platform replacing twelve-plus systems, end-to-end traceability, operational efficiency, automated regulatory compliance, scalability from fifty-two to seventy-five thousand tonnes, data-driven decision making, and true aquaculture industry fit.' },
  { id:'evaluation', label:'Evaluation', text:'The vendor evaluation framework uses ten scoring categories with functional fit at sixty-five percent of the total. Aquaculture Operations carries the highest weight at sixteen percent. Responses scored from S for standard at four points to N for not supported at zero. Mandatory requirements carry a triple multiplier.' },
  { id:'timeline', label:'Timeline', text:'The project timeline runs from R.F.P. issuance in February 2026 through full operational go-live in Q2 2028. Phase 1 covers finance and core operations by Q3 2027, Phase 2 adds processing and V.A.P. by Q1 2028.' },
  { id:'scale', label:'Data Scale', text:'The platform must handle 850,000 G.L. entries, 500,000 inventory transactions, and 1.75 million sensor readings annually. Master data includes 1,200 finished goods S.K.U.s, 3,500 raw materials, 4,200 equipment assets, and 180 active sea pens.' }
];
</script>
<script src="_shared.js"></script>
</body>
</html>'''

TARGET.write_text(NEW_CONTENT, encoding='utf-8')
print(f"Done. Wrote {len(NEW_CONTENT)} chars to {TARGET}")
