"""Solution response data — Technology & Infrastructure (TEC-001 → TEC-080)"""

SOLUTIONS_TEC = {
# ═══════════════════════════════════════════════════════════════
#  11.1  PLATFORM & ARCHITECTURE  (TEC-001 → TEC-010)
# ═══════════════════════════════════════════════════════════════
"TEC-001": {
    "code": "S",
    "summary": "Standard D365 F&O — cloud-hosted SaaS platform on Microsoft Azure with Microsoft-managed infrastructure.",
    "detail": """
<p>D365 Finance &amp; Operations is a <strong>Microsoft-managed SaaS</strong> platform:</p>
<ul>
<li><strong>Hosting</strong>: Microsoft Azure data centers (Northern Europe / West Europe regions for NordHav)</li>
<li><strong>Infrastructure</strong>: Microsoft manages all infrastructure — compute, storage, networking, OS patching, and database management. NordHav does not manage any servers.</li>
<li><strong>SLA</strong>: Microsoft provides 99.9 % uptime SLA for the D365 production environment per the Microsoft Online Service Level Agreement</li>
<li><strong>Scalability</strong>: Azure auto-scaling for compute resources based on workload — handles NordHav's seasonal processing peaks without manual intervention</li>
</ul>
"""
},
"TEC-002": {
    "code": "S",
    "summary": "Standard D365 — all production data stored in Azure Northern Europe (Norway / Ireland) within the EU/EEA.",
    "detail": """
<p>D365 F&amp;O data residency:</p>
<ul>
<li><strong>Data centre region</strong>: NordHav's D365 tenant is provisioned in the <strong>Northern Europe</strong> Azure region (Dublin, Ireland) or <strong>Norway East</strong> (Oslo) — both within the EU/EEA. Microsoft documents exact data centre locations per the Microsoft Trust Center.</li>
<li><strong>Norwegian residency</strong>: If Norwegian data residency is required, Microsoft's <strong>Norway East / Norway West</strong> Azure regions keep data within Norway. Dataverse (Power Platform) can also be geo-pinned to Norway.</li>
<li><strong>Data isolation</strong>: NordHav's data is logically isolated in Azure SQL databases accessible only to NordHav's authenticated users. Microsoft does not access customer data without explicit permission.</li>
<li><strong>GDPR &amp; Schrems II</strong>: Microsoft's EU Data Boundary initiative ensures EU/EEA customer data is processed and stored within the EU/EEA geography.</li>
</ul>
"""
},
"TEC-003": {
    "code": "S",
    "summary": "Standard D365 — multi-tenant SaaS architecture with logical data isolation per Azure SQL elastic pools and Microsoft Entra ID tenant boundaries.",
    "detail": """
<p>D365 F&amp;O is a <strong>multi-tenant</strong> SaaS platform:</p>
<ul>
<li><strong>Tenant isolation</strong>: each customer (NordHav) runs on its own dedicated Azure SQL database — data is <em>not</em> shared in common tables with other tenants. Compute (AOS instances) are provisioned per customer.</li>
<li><strong>Identity boundary</strong>: Microsoft Entra ID (Azure AD) provides the tenant boundary — only authenticated NordHav users can reach NordHav's D365 environment.</li>
<li><strong>Network isolation</strong>: Azure networking controls ensure that tenant traffic is isolated. Microsoft regularly performs penetration testing and security audits to validate multi-tenant isolation.</li>
<li><strong>Compliance</strong>: multi-tenant architecture is SOC 1/2, ISO 27001 and ISO 27018 certified. Microsoft publishes audit reports on the Service Trust Portal.</li>
</ul>
"""
},
"TEC-004": {
    "code": "S",
    "summary": "Standard D365 — Azure auto-scaling supports NordHav's 50 % five-year growth plan without architectural changes.",
    "detail": """
<p>D365 SaaS scalability:</p>
<ul>
<li><strong>Horizontal compute scaling</strong>: the AOS (Application Object Server) tier can scale out automatically to handle increased concurrent users and batch workload.</li>
<li><strong>Azure SQL elastic performance</strong>: database compute and storage scale independently — Microsoft right-sizes production database tier based on workload telemetry.</li>
<li><strong>Seasonal peaks</strong>: NordHav's processing-plant seasonality (high volumes in lice-treatment and harvest seasons) is handled by Azure's elastic infrastructure without manual intervention.</li>
<li><strong>No architectural changes</strong>: the same D365 deployment, configuration, and integrations support 50 % or greater volume growth. Only Azure resource tiers scale — no re-architecture required.</li>
</ul>
"""
},
"TEC-005": {
    "code": "S",
    "summary": "Standard D365 — 99.9 % uptime SLA with Azure SQL automatic failover, paired-region redundancy, and defined maintenance windows.",
    "detail": """
<p>High availability built into D365 SaaS:</p>
<ul>
<li><strong>SLA</strong>: Microsoft's D365 production SLA is <strong>99.9 %</strong> (per the Online Services Level Agreement) — significantly exceeds NordHav's 99.5 % requirement.</li>
<li><strong>AOS tier</strong>: multiple AOS instances behind Azure load balancers — if one instance fails, traffic is routed to healthy instances automatically.</li>
<li><strong>Database tier</strong>: Azure SQL with automatic failover groups — standby replica in the same region provides near-instantaneous failover (typically &lt; 30 seconds).</li>
<li><strong>Maintenance windows</strong>: Microsoft communicates planned maintenance in advance via the Message Center. NordHav can configure preferred maintenance windows to minimise business impact (e.g., weekends).</li>
</ul>
"""
},
"TEC-006": {
    "code": "S",
    "summary": "Standard D365 — geo-redundant disaster recovery with RPO near-zero and RTO under 1 hour, exceeding NordHav's requirements.",
    "detail": """
<p>D365 disaster recovery:</p>
<ul>
<li><strong>Azure SQL geo-replication</strong>: production database is continuously replicated to a paired Azure region — asynchronous replication with RPO of seconds (well under the 1-hour requirement).</li>
<li><strong>RTO</strong>: in a full regional disaster, Microsoft initiates failover to the paired region. Typical RTO is under 1 hour — within NordHav's 4-hour requirement.</li>
<li><strong>DR testing</strong>: Microsoft performs regular DR drills across Azure regions. Customers can request DR test information from the Service Trust Portal.</li>
<li><strong>Business continuity plan</strong>: D365 environments are covered by Microsoft's Azure Business Continuity and Disaster Recovery (BCDR) programme with documented RPO/RTO commitments.</li>
</ul>
"""
},
"TEC-007": {
    "code": "S",
    "summary": "Standard D365 — automated daily backups with 28-day point-in-time restore and self-service database operations via LCS.",
    "detail": """
<p>D365 backup and restore:</p>
<ul>
<li><strong>Automated backups</strong>: Azure SQL performs continuous backups (transaction log backups every 5–10 minutes, differential backups every 12 hours, full backups weekly). No manual backup operations needed.</li>
<li><strong>Retention</strong>: production database point-in-time restore available for the last <strong>28 days</strong> — within the 30-day requirement for practical purposes. Longer retention achievable via database export (.bacpac) to Azure blob storage.</li>
<li><strong>Point-in-time restore</strong>: Microsoft or NordHav administrators (via support request) can restore the database to any point within the retention window.</li>
<li><strong>Self-service</strong>: sandbox environments support self-service database copy from production (with PII masking) and database refresh via LCS — enabling testing and data recovery scenarios.</li>
</ul>
"""
},
"TEC-008": {
    "code": "S",
    "summary": "Standard D365 — One Version continuous update model with 8 annual service updates, preview sandboxes, and rollback capability.",
    "detail": """
<p>D365 <strong>One Version</strong> update model:</p>
<ul>
<li><strong>Service updates</strong>: 8 updates per year (~every 6 weeks) — new features, improvements, and regulatory updates. NordHav can pause up to 3 consecutive updates (max 4-month delay).</li>
<li><strong>Quality updates</strong>: proactive quality updates applied automatically by Microsoft — bug fixes and performance improvements requiring no action from NordHav.</li>
<li><strong>Sandbox preview</strong>: service updates first deployed to UAT sandbox for NordHav to validate (minimum 2-week preview window). Only after NordHav validation is the update applied to production.</li>
<li><strong>Regression testing</strong>: RSAT (Regression Suite Automation Tool) available for automated regression testing of configured business processes before update go-live.</li>
<li><strong>Rollback</strong>: if a critical issue is found after a production update, Microsoft can rollback via support request. The preview/sandbox period is designed to prevent this need.</li>
</ul>
"""
},
"TEC-009": {
    "code": "S",
    "summary": "Standard D365 — multi-environment strategy with Production, UAT (Tier-2), and Development (Tier-1) plus additional sandboxes as needed.",
    "detail": """
<p>D365 <strong>environment strategy</strong>:</p>
<ul>
<li><strong>Production</strong>: live environment for all NordHav users — managed by Microsoft with Tier-2+ hardware.</li>
<li><strong>UAT / Sandbox (Tier-2)</strong>: pre-production environment for testing, configuration validation, and user acceptance testing before production deployment. Data refreshable from production.</li>
<li><strong>Development (Tier-1)</strong>: developer/ISV environment for customisation development and unit testing.</li>
<li><strong>Additional sandboxes</strong>: provisioned as needed for parallel testing, training, or data-migration testing — at least 2 non-production environments included in the standard D365 subscription.</li>
<li><strong>LCS (Lifecycle Services)</strong>: Microsoft's management portal for environment provisioning, code deployment, database movement, issue tracking, and update management.</li>
</ul>
"""
},
"TEC-010": {
    "code": "S",
    "summary": "Standard D365 — built-in performance monitoring with sub-2-second screen loads, batch framework, and Azure Application Insights telemetry.",
    "detail": """
<p>D365 performance management:</p>
<ul>
<li><strong>Screen load</strong>: D365 web client typical page-load time is 1–2 seconds on a standard connection — within the &lt; 2-second requirement.</li>
<li><strong>Report generation</strong>: standard SSRS reports generated server-side; most operational reports complete in &lt; 10 seconds. Complex analytical queries delegated to Power BI for optimal performance.</li>
<li><strong>Batch framework</strong>: background processing for period-end jobs (financial posting, MRP, settlement). Batch groups define priority and server allocation — NordHav can parallelise batch jobs to complete period-end within 2 hours.</li>
<li><strong>Monitoring</strong>: LCS Environment Monitoring provides real-time telemetry — SQL query performance, user response times, and batch job execution. Azure Application Insights for custom telemetry on integration components.</li>
</ul>
"""
},

# ═══════════════════════════════════════════════════════════════
#  11.2  USER EXPERIENCE & ACCESS  (TEC-011 → TEC-017)
# ═══════════════════════════════════════════════════════════════
"TEC-011": {
    "code": "S",
    "summary": "Standard D365 — fully web-based client accessible via Edge, Chrome, Firefox, and Safari on any device without client installation.",
    "detail": """
<p>D365 <strong>web client</strong>:</p>
<ul>
<li><strong>Browser support</strong>: fully browser-based — compatible with Microsoft Edge, Google Chrome, Mozilla Firefox, and Apple Safari. No client software or plugins required.</li>
<li><strong>Responsive design</strong>: works on desktop (full workspace navigation), tablet (touch-optimised), and mobile (essential functions).</li>
<li><strong>Access</strong>: all NordHav locations access D365 via browser through their normal internet connection — farm sites, processing plants, head office, and remote workers all use the same URL.</li>
<li><strong>No installation</strong>: zero-footprint client eliminates local software deployment and maintenance — reduces IT overhead significantly.</li>
</ul>
"""
},
"TEC-012": {
    "code": "S",
    "summary": "Standard D365 mobile app + AquaMonitor (Power Apps) — native mobile on iOS and Android for time, leave, approvals, and operational data entry.",
    "detail": """
<p>Mobile application:</p>
<ul>
<li><strong>D365 Finance and Operations mobile app</strong>: available for iOS and Android. Configured workspaces for: time registration (clock-in/out), expense entry, leave requests, inventory counting, and approval workflows.</li>
<li><strong>AquaMonitor mobile</strong> (Power Apps — Gap G-01): dedicated mobile application for farm-site operational data entry — mortality registration, feed recording, lice counts, environmental observations, and photo capture.</li>
<li><strong>Operational dashboards</strong>: mobile-accessible Power BI dashboards for key metrics when on the move — production status, site overview, financial KPIs.</li>
<li><strong>Push notifications</strong>: approval requests and critical alerts delivered to mobile devices via Power Automate.</li>
</ul>
"""
},
"TEC-013": {
    "code": "C",
    "summary": "AquaMonitor (Power Apps) offline mode — local data cache at sea sites with queue-and-sync and conflict resolution on reconnect.",
    "detail": """
<p>Offline capability:</p>
<ul>
<li><strong>Power Apps offline</strong>: AquaMonitor mobile app supports offline operation — data entered at remote sea sites (limited connectivity) is stored locally on the device.</li>
<li><strong>Queue-and-sync</strong>: when connectivity is restored, locally cached data syncs to Dataverse automatically. Sync status visible to the user.</li>
<li><strong>Conflict resolution</strong>: Dataverse handles merge conflicts using "last writer wins" by default. For critical data (e.g., inventory counts), the app prompts the user to review and resolve conflicting records.</li>
<li><strong>D365 mobile app</strong>: the Finance and Operations mobile app also caches data locally for basic offline scenarios (time entry, expense capture) and syncs when connected.</li>
</ul>
"""
},
"TEC-014": {
    "code": "S",
    "summary": "Standard D365 — multi-language UI with Norwegian Bokmål as primary and English as secondary; user-switchable language preference.",
    "detail": """
<p>D365 multi-language support:</p>
<ul>
<li><strong>Norwegian Bokmål (nb-NO)</strong>: configured as the primary system language for NordHav. All standard D365 labels, menus, error messages, and help text are available in Norwegian Bokmål — this is a fully supported language in D365.</li>
<li><strong>English (en-US)</strong>: available as secondary language. Users can switch language independently in their <strong>User Options → Preferences → Language</strong> setting — each user sees the UI in their chosen language without affecting other users.</li>
<li><strong>Custom labels</strong>: all NordHav-specific labels, reports, and documentation developed in both Norwegian Bokmål and English to ensure consistency.</li>
<li><strong>Nynorsk</strong>: Nynorsk is not a standard D365 language. As a desirable requirement, Nynorsk could be addressed via custom label translations for key forms if needed, or via the Terminology component in D365 Electronic Reporting for document output. This would be a minor customisation effort.</li>
<li><strong>Power Apps / AquaMonitor</strong>: multi-language labels configurable in Power Apps — Norwegian Bokmål and English supported. User language preference follows the user's browser/device language setting.</li>
<li><strong>Power BI reports</strong>: report labels and formatting localised per user language where applicable; most KPI dashboards labelled in Norwegian with English available.</li>
</ul>
"""
},
"TEC-015": {
    "code": "S",
    "summary": "Standard D365 — role-based workspaces with tailored dashboards, menus, and data access per user role (security role governs visibility).",
    "detail": """
<p>Role-based UI:</p>
<ul>
<li><strong>Workspaces</strong>: D365 provides role-based workspaces — each security role sees a tailored landing page with relevant tiles, lists, charts, and links. Examples: Production Manager workspace (production orders, schedules, KPIs), AP Clerk workspace (pending invoices, payment status), Quality Inspector workspace (open quality orders, test results).</li>
<li><strong>Menu filtering</strong>: navigation menus are filtered by security role — users only see modules and menu items they have access to. A site manager at a farming location does not see Finance configuration menus.</li>
<li><strong>Data-level security</strong>: row-level and entity-level security ensures users only see data for their authorised scope (legal entity, site, operating unit). An accountant at NordHav Processing AS sees only that entity's financial data.</li>
<li><strong>Power BI embedded</strong>: role-specific Power BI visuals embedded in workspaces provide at-a-glance KPIs relevant to each role.</li>
</ul>
"""
},
"TEC-016": {
    "code": "S",
    "summary": "Standard D365 — user personalization with saved views, form customisation, dashboard widgets, and notification preferences.",
    "detail": """
<p>Personalization:</p>
<ul>
<li><strong>Saved views</strong>: users save personalised list filters, column layouts, and sort orders as named views. Switch between views for different tasks (e.g., "My Open POs", "Overdue Invoices").</li>
<li><strong>Form personalization</strong>: users can rearrange, hide, show, and resize fields, FastTabs, and FactBoxes on forms — personalizations persist across sessions.</li>
<li><strong>Dashboard widgets</strong>: workspace tiles and Power BI visuals can be arranged by the user. Favourite links pinned to a personal navigation pane.</li>
<li><strong>Notification preferences</strong>: users configure alert rules and choose delivery channels — in-app, email, or Teams via Power Automate.</li>
<li><strong>Admin control</strong>: system administrators can publish personalizations to roles (default view for all AP Clerks) and restrict personalization scope if needed.</li>
</ul>
"""
},
"TEC-017": {
    "code": "S",
    "summary": "Standard D365 — WCAG 2.1 Level AA accessibility via the Microsoft-managed web client with keyboard navigation, screen reader support, and high-contrast themes.",
    "detail": """
<p>Accessibility:</p>
<ul>
<li><strong>WCAG 2.1 Level AA</strong>: D365 Finance and Operations web client is designed to meet WCAG 2.1 Level AA standards as part of Microsoft's commitment to accessibility across all products.</li>
<li><strong>Keyboard navigation</strong>: all forms, lists, and workspaces are navigable via keyboard — Tab, Enter, arrow keys, and shortcut keys for common actions.</li>
<li><strong>Screen reader support</strong>: compatible with screen readers (Narrator, JAWS, NVDA) — ARIA attributes and semantic HTML ensure meaningful page structure is communicated to assistive technology.</li>
<li><strong>High-contrast theme</strong>: D365 includes a high-contrast colour theme selectable in User Options for visually impaired users.</li>
<li><strong>Microsoft Accessibility Conformance Reports</strong>: Microsoft publishes VPATs (Voluntary Product Accessibility Templates) for D365 F&amp;O on the Microsoft Accessibility site, documenting conformance details.</li>
</ul>
"""
},

# ═══════════════════════════════════════════════════════════════
#  11.3  INTEGRATION  (TEC-018 → TEC-030)
# ═══════════════════════════════════════════════════════════════
"TEC-018": {
    "code": "S",
    "summary": "Standard D365 — comprehensive OData RESTful API with documented data entities for read/write access to all major business objects.",
    "detail": """
<p>D365 <strong>OData API</strong>:</p>
<ul>
<li><strong>RESTful interface</strong>: exposes 3,000+ data entities for CRUD operations over HTTPS. All major business objects — customers, vendors, items, sales orders, purchase orders, journals, production orders — are available as OData endpoints.</li>
<li><strong>Authentication</strong>: Azure Active Directory (Microsoft Entra ID) with OAuth 2.0 — service-to-service authentication using client credentials for system integrations, delegated tokens for user-context integrations.</li>
<li><strong>Documentation</strong>: full entity metadata available via the OData $metadata endpoint. Entity fields, relationships, and enumerations are self-documenting.</li>
<li><strong>Custom entities</strong>: NordHav can create custom data entities (X++ development) for any business data not covered by standard entities — ensuring comprehensive API coverage.</li>
</ul>
"""
},
"TEC-019": {
    "code": "C",
    "summary": "D365 Business Events + Azure Service Bus — real-time event-driven integration for feeding system, production line, and sensor data triggers.",
    "detail": """
<p>Real-time integration architecture:</p>
<ul>
<li><strong>D365 Business Events</strong>: D365 publishes business events (e.g., sales order confirmed, purchase order approved, production order completed) to Azure Service Bus. External systems subscribe to relevant events for downstream processing.</li>
<li><strong>Azure Service Bus</strong>: message broker for reliable asynchronous messaging. Message queues for point-to-point integration; topics for publish/subscribe patterns — ensuring no message loss even during temporary outages.</li>
<li><strong>Feed system data</strong>: AquaMonitor → Service Bus → D365 for real-time feed consumption and mortality events.</li>
<li><strong>Production line data</strong>: Marel Innova → Service Bus → D365 for real-time production output reporting.</li>
<li><strong>Sensor data</strong>: IoT Hub → Stream Analytics → Service Bus → D365 for critical threshold alerts (temperature exceedance triggers quality non-conformance).</li>
</ul>
"""
},
"TEC-020": {
    "code": "S",
    "summary": "Standard D365 — Data Management Framework (DMF) for batch/scheduled integration: bank files, payroll journals, regulatory reports, and periodic sync.",
    "detail": """
<p>D365 <strong>DMF</strong> for batch integration:</p>
<ul>
<li><strong>Bulk data operations</strong>: DMF handles scheduled import/export for large data volumes — CSV, XML, and Excel formats supported.</li>
<li><strong>Recurring data jobs</strong>: scheduled imports/exports at defined frequencies (hourly, daily, weekly) for ongoing integration — e.g., daily bank statement import, weekly payroll journal import.</li>
<li><strong>Bank file exchange</strong>: payment file export (pain.001) and bank statement import (camt.053/054) via scheduled DMF jobs.</li>
<li><strong>Payroll journal import</strong>: payroll results (from ISV payroll system) imported as GL journals via recurring DMF integration.</li>
<li><strong>Regulatory reporting</strong>: SAF-T, Intrastat, and A-melding data exported via D365 Electronic Reporting framework on scheduled or on-demand basis.</li>
</ul>
"""
},
"TEC-021": {
    "code": "C",
    "summary": "Azure Integration Services — Logic Apps, Service Bus, API Management, and Functions for enterprise integration middleware.",
    "detail": """
<p>NordHav's integration middleware:</p>
<ul>
<li><strong>Azure Service Bus</strong>: message broker for reliable asynchronous messaging between D365 and external systems. Queue-based for point-to-point, topic-based for publish/subscribe.</li>
<li><strong>Azure Logic Apps</strong>: workflow orchestration for integration scenarios requiring transformation, routing, and conditional logic — e.g., mapping AquaMonitor data to D365 entities.</li>
<li><strong>Azure Functions</strong>: serverless compute for custom integration logic — data transformation, validation, enrichment, and format conversion.</li>
<li><strong>Azure API Management</strong>: API gateway for external-facing APIs — rate limiting, authentication, monitoring, documentation, and developer portal for third-party integrators.</li>
<li><strong>Compatibility</strong>: all components are Azure-native and integrate seamlessly with D365 F&amp;O. MuleSoft or equivalent middleware is also compatible via REST/OData but Azure Integration Services is the recommended stack for NordHav.</li>
</ul>
"""
},
"TEC-022": {
    "code": "C",
    "summary": "D365 ↔ AKVA group AKVAcontrol — feed system integration via AquaMonitor and Azure Service Bus for feeding data and feeding plans.",
    "detail": """
<p>Feed system integration (AKVA group):</p>
<ul>
<li><strong>Inbound (AKVAcontrol → D365)</strong>: feeding data received — kg per pen, pellet type, feeding times, and water temperature during feeding. Data flows via AquaMonitor (which interfaces directly with AKVAcontrol) → Dataverse → D365 via dual-write or Service Bus.</li>
<li><strong>Outbound (D365 → AKVAcontrol)</strong>: feeding plans and parameters sent from D365 production planning — feed budgets per site/pen, pellet specifications from procurement, and feeding schedules aligned with growth models.</li>
<li><strong>Integration method</strong>: Azure Service Bus for event-driven data exchange. AquaMonitor (Power Apps) acts as the operational layer that farm-site staff interact with; D365 is the back-end for financial and inventory recording of feed consumption.</li>
<li><strong>Feed inventory</strong>: feed consumption data from AKVAcontrol triggers D365 inventory transactions (consumption journals) to keep feed stock levels accurate.</li>
</ul>
"""
},
"TEC-023": {
    "code": "C",
    "summary": "D365 ↔ Marel Innova — processing line integration via Azure Service Bus for production data exchange and shopfloor automation.",
    "detail": """
<p>Marel Innova integration (Gap G-09):</p>
<ul>
<li><strong>D365 → Marel</strong>: production orders, item specifications, customer grading requirements, and packing instructions sent to Marel Innova for processing execution.</li>
<li><strong>Marel → D365</strong>: production output (quantities, weights, grades, yields), raw material consumption, production time, and quality data reported back to D365 production control.</li>
<li><strong>Middleware</strong>: Azure Service Bus provides reliable messaging between the shopfloor automation system and D365. A middleware transformation layer handles data mapping between Marel's data model and D365 production entities.</li>
<li><strong>Real-time</strong>: production data flows in near real-time — D365 production orders are updated as Marel reports output, enabling live production monitoring in D365 workspaces.</li>
</ul>
"""
},
"TEC-024": {
    "code": "C",
    "summary": "D365 ↔ Norwegian banks (DNB, Nordea) — ISO 20022 payment files (pain.001), bank statement import (camt.053/054), and auto-reconciliation.",
    "detail": """
<p>Banking integration:</p>
<ul>
<li><strong>Payment file export</strong>: ISO 20022 pain.001 (credit transfer) and pain.008 (direct debit) formats configured for Norwegian banks (DNB, Nordea, SpareBank 1). Payment files generated from D365 AP payment journals.</li>
<li><strong>Bank statement import</strong>: camt.053 (end-of-day statement) and camt.054 (debit/credit notification) imported into D365 for automatic bank reconciliation.</li>
<li><strong>Auto-reconciliation</strong>: D365 Advanced Bank Reconciliation matches imported bank statements to D365 transactions automatically — reducing manual effort. Unmatched items flagged for manual review.</li>
<li><strong>Optional direct connectivity</strong>: for banks supporting host-to-host connections, Azure Logic Apps can automate file exchange (SFTP or API), eliminating manual file upload/download.</li>
</ul>
"""
},
"TEC-025": {
    "code": "C",
    "summary": "D365 Electronic Invoicing — Norwegian EHF 3.0 (PEPPOL BIS Billing 3.0) e-invoicing via PEPPOL Access Point.",
    "detail": """
<p>EHF e-invoicing:</p>
<ul>
<li><strong>Standard</strong>: D365 Electronic Reporting configured for Norwegian EHF 3.0 based on PEPPOL BIS Billing 3.0 — UBL XML format.</li>
<li><strong>Sales invoices</strong>: invoices generated in EHF format and transmitted to customers via a PEPPOL Access Point (e.g., Nets, Pagero, or equivalent Norwegian provider).</li>
<li><strong>Purchase invoices</strong>: electronic invoices received from suppliers via the same PEPPOL network and imported into D365 AP for processing.</li>
<li><strong>Compliance</strong>: mandatory for public-sector customers and increasingly expected by private-sector trading partners in Norway. NordHav is fully compliant from day one.</li>
</ul>
"""
},
"TEC-026": {
    "code": "C",
    "summary": "D365 + Azure Integration — government portal integration for Altinn, BarentsWatch, Mattilsynet, and TVINN filings.",
    "detail": """
<p>Government portal integration:</p>
<ul>
<li><strong>Altinn</strong>: A-melding (monthly employment/income reporting) from ISV payroll system. MVA-melding (VAT return) from D365 Finance. SAF-T export (Standard Audit File for Tax). Skattemelding (annual tax return) data preparation. Integration via Altinn web service API or file-based submission.</li>
<li><strong>BarentsWatch</strong>: lice counts, biomass reporting, and environmental data submitted via AquaMonitor integration — AquaMonitor prepares data from farming operations and submits to BarentsWatch APIs per regulatory schedule.</li>
<li><strong>Mattilsynet</strong>: health certificates and veterinary documentation generated from D365 Quality Management / AquaMonitor data — submitted electronically or as PDF depending on Mattilsynet's current submission format.</li>
<li><strong>TVINN</strong>: customs declarations for export shipments — D365 generates Intrastat/customs data; integration to TVINN via approved customs broker or direct submission where supported.</li>
</ul>
"""
},
"TEC-027": {
    "code": "C",
    "summary": "D365 + Power BI — embedded analytics with role-specific dashboards, drill-through to D365 transactions, and optimised data model for advanced analytics.",
    "detail": """
<p>Power BI integration:</p>
<ul>
<li><strong>Embedded Power BI</strong>: D365 workspaces embed Power BI visuals, delivering real-time KPIs within the user's workflow — users drill from a visual directly to the underlying D365 transaction.</li>
<li><strong>Data model</strong>: a governed Power BI semantic model built on D365 data (via Entity Store or Microsoft Fabric Lakehouse) provides a clean, performant layer for all analytics.</li>
<li><strong>Role-specific dashboards</strong>: pre-built dashboards for each functional area (Finance, Production, Quality, SCM, HR, Farming) delivered via Power BI workspaces with row-level security.</li>
<li><strong>Advanced analytics</strong>: the data model supports self-service analysis — business users create their own reports from managed datasets without IT assistance.</li>
</ul>
"""
},
"TEC-028": {
    "code": "C",
    "summary": "Azure IoT Hub + Stream Analytics — high-volume sensor data ingestion from water quality, temperature, and environmental monitoring stations.",
    "detail": """
<p>IoT data ingestion architecture:</p>
<ul>
<li><strong>Azure IoT Hub</strong>: scalable ingestion endpoint for sensor data — water quality sensors (temperature, oxygen, salinity at farm sites), processing-plant temperature loggers (cold rooms, blast freezers), and transport temperature monitors (reefer trucks/containers).</li>
<li><strong>Data volume</strong>: IoT Hub scales to millions of messages per day — easily handles NordHav's sensor estate. Device management (provisioning, firmware updates, health monitoring) included.</li>
<li><strong>Azure Stream Analytics</strong>: real-time processing for threshold alerting (temperature exceedance → immediate alert), anomaly detection, and dashboard data feeds.</li>
<li><strong>Storage</strong>: raw sensor data stored in Microsoft Fabric Lakehouse for historical trend analysis. Power BI dashboards visualise real-time and historical sensor data.</li>
<li><strong>D365 integration</strong>: critical alerts (e.g., cold-chain temperature breach) trigger D365 quality non-conformance creation via Azure Service Bus automatically.</li>
</ul>
"""
},
"TEC-029": {
    "code": "S",
    "summary": "Standard D365 + Microsoft 365 — email integration with Outlook, correspondence linked to transactions, automated notifications, and calendar integration.",
    "detail": """
<p>Email and calendar integration:</p>
<ul>
<li><strong>Outlook integration</strong>: D365 integrates with Microsoft 365 / Outlook — email correspondence can be linked to D365 transactions (purchase orders, sales orders, vendor inquiries, claims) via the D365 email tracking feature.</li>
<li><strong>Automated notifications</strong>: D365 workflow actions, alert rules, and Power Automate flows send email notifications — approval requests, overdue alerts, and status updates delivered to Outlook.</li>
<li><strong>Document output</strong>: D365 print management can send business documents (invoices, PO confirmations, packing slips) directly via email from within D365.</li>
<li><strong>Calendar integration</strong>: meeting scheduling and resource availability visible via Microsoft Teams / Outlook calendar integration with D365 Project Operations and HR.</li>
</ul>
"""
},
"TEC-030": {
    "code": "S",
    "summary": "Standard D365 — document management with SharePoint Online integration for version-controlled storage of all transaction-linked documents.",
    "detail": """
<p>Document management:</p>
<ul>
<li><strong>SharePoint integration</strong>: all document attachments in D365 stored in SharePoint Online (not in the D365 database) — full versioning, search capability, and compliance retention.</li>
<li><strong>Transaction linking</strong>: document types configured per entity — vendor invoices attached to AP invoices, quality certificates attached to purchase receipts, production documentation attached to production orders, contracts attached to vendor/customer records.</li>
<li><strong>User experience</strong>: users attach and view documents within D365 forms — physical storage is transparently managed in SharePoint.</li>
<li><strong>Version control</strong>: SharePoint versioning tracks all document changes with full audit trail — who changed what and when.</li>
<li><strong>Compliance</strong>: SharePoint retention policies enforce document retention per regulatory requirements (e.g., 5-year retention for accounting documents per Bokføringsloven).</li>
</ul>
"""
},

# ═══════════════════════════════════════════════════════════════
#  11.4  MAINTENANCE & ASSET MANAGEMENT  (TEC-031 → TEC-040)
# ═══════════════════════════════════════════════════════════════
"TEC-031": {
    "code": "S",
    "summary": "Standard D365 Asset Management — technical asset register with hierarchy, location, specifications, warranty, and criticality linked to financial assets.",
    "detail": """
<p>D365 <strong>Asset Management</strong> register:</p>
<ul>
<li><strong>Asset register</strong>: all NordHav technical assets — processing lines, slaughter equipment, packing machines, cold-storage systems, wellboats (if owned), feed barges, and facility infrastructure (buildings, electrical, plumbing, HVAC).</li>
<li><strong>Asset hierarchy</strong>: functional structure (Site → Area → Line → Equipment → Component) enabling maintenance planning and work-order creation at any level.</li>
<li><strong>Asset details</strong>: manufacturer, serial/model numbers, installation date, warranty expiry, criticality classification (A/B/C), and technical specifications.</li>
<li><strong>Financial link</strong>: each technical asset linked to D365 Fixed Assets for financial depreciation and capitalisation tracking — one record, two views (technical and financial).</li>
<li><strong>Location tracking</strong>: assets associated with functional locations — if an asset moves between sites or lines, the history is maintained.</li>
</ul>
"""
},
"TEC-032": {
    "code": "S",
    "summary": "Standard D365 Asset Management — preventive maintenance schedules with time-based, counter-based, and condition-based triggers.",
    "detail": """
<p>Preventive maintenance:</p>
<ul>
<li><strong>Maintenance plans</strong>: schedules based on calendar (weekly, monthly, quarterly, annual), counter-based (runtime hours, production cycles, throughput volume), or condition-based (triggered by IoT sensor thresholds).</li>
<li><strong>Task descriptions</strong>: each maintenance plan line includes task description, estimated duration, required skills, safety precautions, and linked spare-parts list (BOM).</li>
<li><strong>Maintenance rounds</strong>: routine checklists — daily production-line inspections, weekly equipment checks, monthly safety inspections — each generating a work order automatically when due.</li>
<li><strong>Auto-generation</strong>: work orders created automatically when schedule triggers fire — maintenance planners review and approve before execution.</li>
</ul>
"""
},
"TEC-033": {
    "code": "S",
    "summary": "Standard D365 Asset Management — full work order lifecycle: request → creation → planning → scheduling → execution → completion → close-out.",
    "detail": """
<p>Work order management:</p>
<ul>
<li><strong>Lifecycle</strong>: Created → Scheduled → In Progress → Completed → Closed. Each stage has configurable business rules and approval requirements.</li>
<li><strong>Work order content</strong>: asset, fault type (if corrective), maintenance type (preventive/corrective), job description, estimated duration, required skills, and spare parts.</li>
<li><strong>Corrective (reactive)</strong>: unplanned work orders created from maintenance requests when equipment fails or issues are reported.</li>
<li><strong>Planned</strong>: work orders generated from preventive maintenance plans — pre-populated with task details and parts requirements.</li>
<li><strong>Assignment</strong>: work orders assignable to internal maintenance workers or external contractors. Scheduling considers worker calendar and skill requirements.</li>
<li><strong>Completion</strong>: actual time, materials consumed, and completion notes recorded against each work order — feeding cost analysis and KPIs.</li>
</ul>
"""
},
"TEC-034": {
    "code": "C",
    "summary": "D365 Asset Management + mobile — maintenance technicians receive, execute, and close work orders from mobile devices with photo capture.",
    "detail": """
<p>Mobile maintenance:</p>
<ul>
<li><strong>Mobile work orders</strong>: maintenance technicians access assigned work orders on mobile devices (D365 mobile app or dedicated Power Apps maintenance form).</li>
<li><strong>Field execution</strong>: from the mobile device, technicians can: view work order details and task instructions, record tasks completed, register spare parts used (barcode scan), capture photos of work performed or damage found, and update work order status.</li>
<li><strong>Offline</strong>: Power Apps mobile supports offline caching for maintenance scenarios in areas with limited connectivity (e.g., remote farm barges). Data syncs when connected.</li>
<li><strong>Close-out</strong>: technicians close work orders from the field — completion data flows to D365 for cost allocation, KPI calculation, and asset history update.</li>
</ul>
"""
},
"TEC-035": {
    "code": "S",
    "summary": "Standard D365 Asset Management — equipment downtime tracking with planned vs. unplanned classification, root-cause analysis, and production impact reporting.",
    "detail": """
<p>Equipment downtime tracking:</p>
<ul>
<li><strong>Downtime recording</strong>: D365 Asset Management fault registration captures: start time, end time, duration, planned vs. unplanned classification, and affected asset/line.</li>
<li><strong>Root-cause analysis</strong>: fault causes, fault symptoms, and fault remedies recorded against each downtime event — enabling pattern analysis over time.</li>
<li><strong>Production impact</strong>: downtime linked to production orders — impact on output throughput, missed schedules, and cost of lost production calculable from D365 data.</li>
<li><strong>Work order link</strong>: every corrective maintenance work order references the downtime event — full traceability from failure to repair.</li>
<li><strong>Analytics</strong>: Power BI dashboards visualise downtime trends by asset, line, root cause, and time period — supporting prioritisation of reliability improvement initiatives.</li>
</ul>
"""
},
"TEC-036": {
    "code": "S",
    "summary": "Standard D365 Asset Management — spare parts linked to work orders with automatic reservation, consumption recording, and reorder-point replenishment.",
    "detail": """
<p>Spare parts management:</p>
<ul>
<li><strong>BOM per maintenance type</strong>: each maintenance job type has a standard spare-parts list (BOM) — when a work order is created, required parts are pre-populated.</li>
<li><strong>Automatic reservation</strong>: upon work order creation (or scheduling), spare parts are reserved from the maintenance warehouse inventory.</li>
<li><strong>Consumption recording</strong>: technicians record actual parts consumed during work execution — items issued from inventory to the work order via inventory journal.</li>
<li><strong>Reorder-point</strong>: D365 inventory management triggers automatic purchase requisitions (or planned orders) when spare-part stock falls below the configured reorder point — ensuring critical spares are always available.</li>
<li><strong>Cost allocation</strong>: parts cost flows from inventory to the work order → asset maintenance cost → cost-centre reporting.</li>
</ul>
"""
},
"TEC-037": {
    "code": "C",
    "summary": "D365 Asset Management + Power BI — maintenance KPIs: MTBF, MTTR, maintenance cost per asset, and planned-vs-unplanned ratio dashboards.",
    "detail": """
<p>Maintenance KPIs:</p>
<ul>
<li><strong>MTBF</strong> (Mean Time Between Failures): calculated from fault registration data per asset — identifies reliability trends.</li>
<li><strong>MTTR</strong> (Mean Time To Repair): calculated from work order duration — identifies repair efficiency opportunities.</li>
<li><strong>Maintenance cost per asset/line/site</strong>: aggregated from work order labour and parts costs — supports budgeting and investment decisions.</li>
<li><strong>Planned vs. unplanned ratio</strong>: target 80 % planned — tracked via work order type classification. Trend reporting shows improvement over time.</li>
<li><strong>OEE</strong> (Overall Equipment Effectiveness): calculated per production line using downtime data, production speed, and quality yield — surfaced in Power BI for production and maintenance managers.</li>
<li><strong>Dashboards</strong>: Power BI dashboards for maintenance manager daily view, monthly management report, and annual budgeting input.</li>
</ul>
"""
},
"TEC-038": {
    "code": "C",
    "summary": "D365 Asset Management + AquaMonitor — specialised asset tracking for net pens (mesh, antifouling), mooring systems (NYTEK compliance), and feed barges.",
    "detail": """
<p>Aquaculture-specific asset management:</p>
<ul>
<li><strong>Net pens</strong>: tracked as assets in D365 Asset Management — attributes include: dimension (circumference, depth), mesh size, antifouling treatment status and schedule, repair history, and location (which cage/site). Net service lifecycle managed from new → deployed → inspected → repaired → decommissioned.</li>
<li><strong>Mooring systems</strong>: inspection certificates, NYTEK (Norwegian standard for technical requirements for fish farming installations) compliance status, certification body, validity period, and renewal alerts.</li>
<li><strong>Feed barges</strong>: registered with specifications, maintenance schedules, inspection certificates, and operational status per site.</li>
<li><strong>AquaMonitor integration</strong>: farm-site staff record net inspections, mooring checks, and barge status via AquaMonitor mobile — data syncs to D365 Asset Management for central tracking and compliance reporting.</li>
</ul>
"""
},
"TEC-039": {
    "code": "C",
    "summary": "D365 Asset Management — regulatory inspection tracking for electrical, lifting, pressure vessels, and NYTEK with certification dates and renewal alerts.",
    "detail": """
<p>Regulatory equipment inspections:</p>
<ul>
<li><strong>Inspection register</strong>: each regulated asset has inspection records: inspection type (electrical, lifting equipment, pressure vessels, NYTEK, class certificates for vessels), certifying body, inspection date, result (pass/fail/conditional), validity period, and certificate reference.</li>
<li><strong>Renewal alerts</strong>: D365 alerts and Power Automate notifications triggered when an inspection validity period is approaching expiry — configurable lead time (e.g., 30 days, 60 days before expiry).</li>
<li><strong>Compliance dashboard</strong>: Power BI report showing all assets with upcoming or overdue inspections — filtered by type, site, and criticality.</li>
<li><strong>Audit trail</strong>: full history of all inspections per asset maintained in D365 — available for regulatory audits (Arbeidstilsynet, DSB, class societies).</li>
</ul>
"""
},
"TEC-040": {
    "code": "C",
    "summary": "D365 Asset Management — vessel and vehicle fleet management with registration, insurance, class certification, operating hours, fuel, and maintenance.",
    "detail": """
<p>Vessel and vehicle management:</p>
<ul>
<li><strong>Fleet register</strong>: company-owned service boats, workboats, wellboats (if owned), and vehicles registered as assets in D365 — registration numbers, insurance details, class certification (for vessels), and ownership documents.</li>
<li><strong>Operating hours / mileage</strong>: counter-based tracking — operating hours for vessels, mileage for vehicles. Counters trigger usage-based preventive maintenance.</li>
<li><strong>Fuel consumption</strong>: fuel purchases recorded via D365 procurement or expense claims — fuel cost per vessel/vehicle analysed in Power BI for cost control and environmental reporting (GHG emissions).</li>
<li><strong>Maintenance schedules</strong>: preventive maintenance plans linked to each vessel/vehicle — oil changes, engine service, hull inspections, class surveys — with auto-generated work orders.</li>
<li><strong>Certification tracking</strong>: vessel class certificates, safety equipment certificates, and insurance renewal tracked with expiry alerts.</li>
</ul>
"""
},

# ═══════════════════════════════════════════════════════════════
#  11.5  PROJECT & COST MANAGEMENT  (TEC-041 → TEC-045)
# ═══════════════════════════════════════════════════════════════
"TEC-041": {
    "code": "S",
    "summary": "Standard D365 Project Operations — project register with project types (CAPEX, OPEX, R&D), lifecycle tracking, and WBS structure.",
    "detail": """
<p>D365 <strong>Project Operations</strong>:</p>
<ul>
<li><strong>Project register</strong>: create and manage projects with: project name, code (number sequence), project type (CAPEX / OPEX / R&amp;D / Internal), responsible person, start/end dates, and status lifecycle (Created → In Process → Finished → Closed).</li>
<li><strong>Work Breakdown Structure (WBS)</strong>: hierarchical task structure within each project — activities, milestones, dependencies, and resource assignments.</li>
<li><strong>Project groups</strong>: projects categorised by group for reporting — e.g., Infrastructure, IT, Aquaculture Development, Processing Expansion.</li>
<li><strong>Budget assignment</strong>: budget allocated per project with tracking against committed and actual costs (see TEC-042).</li>
</ul>
"""
},
"TEC-042": {
    "code": "S",
    "summary": "Standard D365 Project Operations — project budgeting by cost category with committed, actual, and remaining budget tracking.",
    "detail": """
<p>Project budgeting:</p>
<ul>
<li><strong>Budget definition</strong>: budgets defined by cost category — materials, labour (internal hours), external services, travel, equipment, and contingency. Budget lines entered at the project level or WBS task level.</li>
<li><strong>Budget approval</strong>: budget workflow — project budgets submitted for approval before the project can incur costs. Budget revisions follow the same approval process.</li>
<li><strong>Tracking</strong>: D365 tracks committed costs (approved POs and requisitions), actual costs (posted transactions), and remaining budget at all times. Over-budget warnings configurable.</li>
<li><strong>Forecast</strong>: estimate at completion (EAC) calculated from actuals + remaining forecast — supports proactive budget management.</li>
</ul>
"""
},
"TEC-043": {
    "code": "S",
    "summary": "Standard D365 Project Operations — multi-source cost collection from purchase orders, timesheets, expenses, internal allocations, and journals.",
    "detail": """
<p>Project cost collection:</p>
<ul>
<li><strong>Purchase orders</strong>: procurement costs charged to projects when PO lines reference a project ID — committed on PO confirmation, actual on invoice posting.</li>
<li><strong>Timesheets</strong>: internal labour hours recorded via D365 timesheets — hours × internal cost rate = labour cost posted to the project.</li>
<li><strong>Expense claims</strong>: employee expenses (travel, accommodation, materials) charged to projects via D365 Expense Management.</li>
<li><strong>Internal allocations</strong>: overhead/indirect costs allocated to projects via allocation journals (e.g., IT support, facility costs).</li>
<li><strong>Manual journals</strong>: ad-hoc cost adjustments or corrections posted via project journals.</li>
<li><strong>All sources</strong>: every cost transaction carries the project ID and cost category — enabling accurate project-level reporting from any cost origin.</li>
</ul>
"""
},
"TEC-044": {
    "code": "S",
    "summary": "Standard D365 — CAPEX project capitalisation: construction-in-progress (CIP) accumulates costs and converts to fixed asset on completion.",
    "detail": """
<p>CAPEX project to asset:</p>
<ul>
<li><strong>Construction-in-Progress (CIP)</strong>: during a CAPEX project, all costs accumulate on the project in a CIP (work-in-progress) account — visible in the balance sheet as an asset under construction.</li>
<li><strong>Capitalisation</strong>: upon project completion (or phase completion), D365 creates a fixed asset from the project — transferring the accumulated cost to the Fixed Assets module as the asset's acquisition value.</li>
<li><strong>Partial capitalisation</strong>: if the project produces multiple assets, costs can be split across multiple fixed assets using allocation rules.</li>
<li><strong>Depreciation start</strong>: once capitalised, depreciation begins per the fixed asset's depreciation profile — fully integrated with D365 Finance GL posting.</li>
<li><strong>Audit trail</strong>: full traceability from individual project cost transactions to the capitalised asset value.</li>
</ul>
"""
},
"TEC-045": {
    "code": "S",
    "summary": "Standard D365 Project Operations + Power BI — project reporting with budget vs. actual, variance analysis, milestone progress, and forecast at completion.",
    "detail": """
<p>Project reporting:</p>
<ul>
<li><strong>Budget vs. actual</strong>: D365 project reports compare budgeted, committed, and actual costs by category — highlighting variances at project and WBS-task level.</li>
<li><strong>Milestone progress</strong>: project milestones tracked with status (not started / in progress / completed) and dates — Gantt-style views available in Project Operations.</li>
<li><strong>Forecast at completion</strong>: estimate at completion calculated from actual spend + remaining estimate — enables early identification of cost overruns.</li>
<li><strong>Power BI dashboards</strong>: project portfolio dashboard showing all active projects — budget utilisation, schedule status, cost risk, and resource allocation across NordHav's project portfolio.</li>
<li><strong>Drill-down</strong>: from summary KPIs → project → WBS task → individual cost transaction — full transparency.</li>
</ul>
"""
},

# ═══════════════════════════════════════════════════════════════
#  11.6  REPORTING & ANALYTICS  (TEC-046 → TEC-056)
# ═══════════════════════════════════════════════════════════════
"TEC-046": {
    "code": "S",
    "summary": "Standard D365 — comprehensive report library with SSRS operational reports and Electronic Reporting framework covering all functional areas.",
    "detail": """
<p>Standard report library:</p>
<ul>
<li><strong>SSRS reports</strong>: pre-built operational reports across all D365 modules — inventory valuations, aging reports (AP/AR), trial balance, production output, quality analysis, employee lists, asset registers, and more.</li>
<li><strong>Electronic Reporting (ER)</strong>: configurable framework for regulatory and business documents — invoice layouts, packing slips, labels, statutory reports. ER configurations downloadable from Microsoft's global repository.</li>
<li><strong>Functional coverage</strong>: Finance (GL, AP, AR, FA, budget), Supply Chain (inventory, procurement, production, warehouse), HR (headcount, absence, compensation), Quality (test results, non-conformance), and Asset Management (work order, maintenance history).</li>
<li><strong>Power BI reports</strong>: additional analytical reports delivered as Power BI dashboards embedded in D365 workspaces — complementing the transactional SSRS reports with visual analytics.</li>
</ul>
"""
},
"TEC-047": {
    "code": "C",
    "summary": "D365 + Power BI self-service — ad-hoc reporting using governed semantic models enabling business users to create reports without IT assistance.",
    "detail": """
<p>Ad-hoc reporting:</p>
<ul>
<li><strong>D365 list pages</strong>: all D365 list pages support user-defined filtering, column selection, and export to Excel — immediate ad-hoc querying without any report development.</li>
<li><strong>Saved views</strong>: users save frequently used filter/column combinations as named views — reusable personal "reports".</li>
<li><strong>Power BI self-service</strong>: centrally managed semantic models provide governed data access. Business users create their own reports and visuals using Power BI Desktop or Power BI web authoring — certified models ensure consistent definitions (e.g., "revenue" means the same thing in every report).</li>
<li><strong>Training</strong>: NordHav key users trained on Power BI report creation — enabling self-service analytical capability across the organisation.</li>
</ul>
"""
},
"TEC-048": {
    "code": "S",
    "summary": "Standard D365 — full drill-down capability from summary reports to source documents and from KPI tiles to underlying transaction lists.",
    "detail": """
<p>Report drill-down:</p>
<ul>
<li><strong>Financial drill-down</strong>: from trial balance → ledger transactions → source journal → source document (invoice, payment, production order). Each level links to the next with one click.</li>
<li><strong>Workspace tiles</strong>: KPI tiles in D365 workspaces drill through to the underlying transaction list — e.g., clicking "Overdue Invoices" tile opens the filtered invoice list.</li>
<li><strong>Power BI drill-through</strong>: Power BI dashboards support drill-through pages — from a summary visual to a detail page showing individual records, and from Power BI back to the D365 form for the specific transaction.</li>
<li><strong>Cross-module</strong>: drill-down works across modules — AP invoice → linked PO → linked inventory receipt → linked quality order — full transaction chain visible.</li>
</ul>
"""
},
"TEC-049": {
    "code": "C",
    "summary": "D365 workspaces + Power BI — configurable dashboards with KPI widgets, charts, lists, and role-based defaults that users can personalise.",
    "detail": """
<p>Dashboard builder:</p>
<ul>
<li><strong>D365 workspaces</strong>: each workspace is a configurable dashboard — tiles (count, sum, KPI), lists (filtered transaction lists), charts, and links. System administrators configure default workspace layouts per security role.</li>
<li><strong>Power BI dashboards</strong>: full dashboard builder capability in Power BI — users (with appropriate license) can create custom dashboards from any available Power BI reports and pin visuals from multiple reports onto a single dashboard.</li>
<li><strong>Role-based defaults</strong>: each D365 security role gets a default workspace/dashboard — e.g., Production Manager sees production KPIs, AP Clerk sees pending invoices.</li>
<li><strong>User personalization</strong>: users can rearrange tiles, pin favourites, and configure their personal home workspace.</li>
</ul>
"""
},
"TEC-050": {
    "code": "C",
    "summary": "Power BI subscriptions + D365 batch reports — scheduled automated report generation and email distribution for daily, weekly, and monthly reports.",
    "detail": """
<p>Scheduled reports:</p>
<ul>
<li><strong>Power BI subscriptions</strong>: users subscribe to Power BI reports/dashboards — receive automated email with a snapshot (PDF or image) on a schedule (daily, weekly, monthly). Configured per user or distributed to groups.</li>
<li><strong>D365 batch reports</strong>: SSRS reports scheduled via D365 batch framework — e.g., daily dispatch report generated at 06:00 and emailed to logistics team, weekly inventory valuation emailed to finance.</li>
<li><strong>Power Automate</strong>: for complex distribution rules — conditional report delivery based on data thresholds (e.g., send weekly lice-count summary only if thresholds are exceeded).</li>
<li><strong>Management pack</strong>: monthly management reporting pack assembled in Power BI — auto-refreshed and distributed to executive team via subscription.</li>
</ul>
"""
},
"TEC-051": {
    "code": "S",
    "summary": "Standard D365 — export to Excel, PDF, CSV from all reports and list pages; Power BI exports to Excel, PDF, PowerPoint, and CSV.",
    "detail": """
<p>Export capabilities:</p>
<ul>
<li><strong>D365 list pages</strong>: every list page supports "Export to Excel" (Open in Excel, Export to Excel) — filtered data exported maintaining column selections and filters.</li>
<li><strong>SSRS reports</strong>: standard export options — PDF, Excel, Word, and CSV.</li>
<li><strong>Electronic Reporting</strong>: ER documents exported in configured formats — XML, JSON, CSV, Excel, or PDF depending on the report definition.</li>
<li><strong>Power BI</strong>: reports exportable to PDF, PowerPoint (with live data connection), Excel (underlying data), and CSV. Power BI paginated reports (SSRS-style) support pixel-perfect export to PDF for formal reporting.</li>
</ul>
"""
},
"TEC-052": {
    "code": "C",
    "summary": "Microsoft Fabric — unified data platform providing lakehouse, data warehouse, and data factory for enterprise analytics beyond D365 native reporting.",
    "detail": """
<p>Data platform — Microsoft Fabric:</p>
<ul>
<li><strong>Lakehouse</strong>: raw data storage for D365, AquaMonitor, IoT sensor data, and external data sources — stored in Delta/Parquet format for optimal analytical performance.</li>
<li><strong>Data Factory</strong>: ETL pipelines extracting D365 data (via Synapse Link for D365 or data export framework) and transforming into analytical models.</li>
<li><strong>SQL analytics endpoint</strong>: structured querying over the lakehouse data — enabling T-SQL access for reporting tools and custom analytics.</li>
<li><strong>Data model / schema</strong>: documented star-schema data models built for each analytical domain (finance, production, quality, farming, HR) — the foundation for all Power BI reporting.</li>
<li><strong>Cross-system analytics</strong>: Fabric consolidates D365 operational data, AquaMonitor farming data, external market data, and IoT sensor data into a governed analytics estate — enabling analytics that span multiple source systems.</li>
</ul>
"""
},
"TEC-053": {
    "code": "C",
    "summary": "Power BI real-time dashboards — auto-refreshing operational dashboards for processing-plant status, biomass overview, and order fulfilment.",
    "detail": """
<p>Real-time dashboards:</p>
<ul>
<li><strong>DirectQuery / streaming</strong>: Power BI dashboards configured with DirectQuery (near real-time, query on demand) or streaming datasets (pushed updates) for operational monitoring.</li>
<li><strong>Processing plant</strong>: live production dashboard showing current run status, throughput rates, yield, and downtime — refreshed automatically every few minutes.</li>
<li><strong>Biomass overview</strong>: daily biomass dashboard (from AquaMonitor data) showing fish count, estimated biomass, feed conversion ratio, and lice levels per site/pen.</li>
<li><strong>Order fulfilment</strong>: live status of customer orders — picked, packed, shipped, delivered — with delivery performance KPIs updated in near real-time from D365 warehouse and transport management.</li>
<li><strong>Auto-refresh</strong>: dashboards auto-refresh in Power BI Service at configurable intervals (minimum every 15 minutes for import mode; real-time for streaming/DirectQuery).</li>
</ul>
"""
},
"TEC-054": {
    "code": "C",
    "summary": "Power BI — KPI scorecards with targets, actuals, traffic-light status, and trend indicators configurable by role and organisational level.",
    "detail": """
<p>KPI scorecards:</p>
<ul>
<li><strong>Power BI Metrics</strong>: NordHav's KPIs defined in Power BI Goals / Metrics — each KPI has: definition, target, actual value (auto-calculated from data), status (green/amber/red), and trend indicator.</li>
<li><strong>Role-based views</strong>: executive scorecard (high-level company KPIs), operational scorecards (per function — production, farming, finance, HR), and site-level scorecards.</li>
<li><strong>Traffic-light rules</strong>: configurable thresholds — e.g., green if on-time delivery ≥ 95 %, amber 90–95 %, red &lt; 90 %.</li>
<li><strong>Trend indicators</strong>: sparklines or trend arrows showing direction of change over the last periods — immediate visual indication of improvement or deterioration.</li>
<li><strong>Drill-through</strong>: from any KPI, drill through to the underlying Power BI report showing the details behind the number.</li>
</ul>
"""
},
"TEC-055": {
    "code": "S",
    "summary": "Standard D365 Financial Reporting — pre-built and customisable Balance Sheet, P&L, Cash Flow, trial balance, and dimension analysis reports.",
    "detail": """
<p>Financial reporting package:</p>
<ul>
<li><strong>Financial Reporting (Management Reporter)</strong>: D365's built-in financial report designer for: Balance Sheet, Profit &amp; Loss, Cash Flow Statement, trial balance, and customisable dimension-analysis reports.</li>
<li><strong>Row/column definitions</strong>: flexible design — NordHav defines row structures (account groupings per Norwegian regulations and internal management needs), column definitions (actuals, budget, prior year, variance), and report trees (roll-up by legal entity, department, site).</li>
<li><strong>Budget vs. actual</strong>: comparison reports showing budget, actual, and variance by cost centre, department, project, or any financial dimension.</li>
<li><strong>Drill-down</strong>: from Financial Reporting cells, drill directly to underlying GL transactions in D365 — full audit path from report to source.</li>
<li><strong>Distribution</strong>: reports generated on demand or scheduled; exportable to Excel and PDF.</li>
</ul>
"""
},
"TEC-056": {
    "code": "S",
    "summary": "Standard D365 — Norwegian regulatory report templates: SAF-T, MVA return, A-melding data, Intrastat, and annual financial statement support.",
    "detail": """
<p>Regulatory report templates:</p>
<ul>
<li><strong>SAF-T</strong>: D365 includes the Norwegian SAF-T export (Electronic Reporting format) per Skatteetaten's specification — chart of accounts, GL transactions, customer/vendor data, tax data, and inventory. Validated against the official XSD schema before submission.</li>
<li><strong>MVA return</strong>: VAT return data prepared from D365 tax transactions — formatted per Norwegian tax authority requirements for submission via Altinn.</li>
<li><strong>A-melding</strong>: employment and income data prepared from ISV payroll with D365 HR data support — submitted monthly via Altinn.</li>
<li><strong>Intrastat</strong>: D365 generates Intrastat declaration for NordHav's intra-EU trade — commodity codes (CN/HS) configured per fish product (0302, 0303, 0304, 0305 series). Filed via Altinn/SSB.</li>
<li><strong>Annual financial statements</strong>: D365 Financial Reporting supports Norwegian annual-accounts format (Regnskapsloven) — customisable report definitions aligned with Norwegian GAAP.</li>
</ul>
"""
},

# ═══════════════════════════════════════════════════════════════
#  11.7  SECURITY, ACCESS & DATA PRIVACY  (TEC-057 → TEC-072)
# ═══════════════════════════════════════════════════════════════
"TEC-057": {
    "code": "S",
    "summary": "Standard D365 — SSO via Microsoft Entra ID (Azure AD) using OpenID Connect, fully integrated with Microsoft 365 identity.",
    "detail": """
<p>Single Sign-On:</p>
<ul>
<li><strong>Microsoft Entra ID</strong>: D365 F&amp;O uses Microsoft Entra ID (Azure AD) as its identity provider — SSO is native, not an add-on.</li>
<li><strong>Protocol</strong>: OpenID Connect (OIDC) over OAuth 2.0 — industry standard, fully supported. SAML 2.0 also supported for federated scenarios.</li>
<li><strong>Single identity</strong>: NordHav employees use one identity across all Microsoft services — D365, Microsoft 365, Power Platform, Azure, Teams — with single sign-on.</li>
<li><strong>Federated identity</strong>: if NordHav has on-premises Active Directory, Azure AD Connect synchronises identities — users sign in with the same credentials everywhere.</li>
</ul>
"""
},
"TEC-058": {
    "code": "S",
    "summary": "Standard Microsoft Entra ID — MFA for all users with Authenticator app, SMS, phone call, and FIDO2 security key options.",
    "detail": """
<p>Multi-Factor Authentication:</p>
<ul>
<li><strong>Microsoft Entra MFA</strong>: built into the identity platform — MFA mandatory for all NordHav users (configurable per security policy).</li>
<li><strong>Methods</strong>: Microsoft Authenticator app (push notification or TOTP code), SMS verification, phone call, and FIDO2 hardware security keys. Authenticator app is the recommended default.</li>
<li><strong>Conditional Access</strong>: MFA requirements can be contextual — always required for admin roles, required when accessing from untrusted networks, or risk-based (triggered by unusual sign-in patterns detected by Azure AD Identity Protection).</li>
<li><strong>Seamless experience</strong>: with trusted devices and locations, MFA interruptions are minimised — users on compliant corporate devices in the office may not be prompted repeatedly.</li>
</ul>
"""
},
"TEC-059": {
    "code": "S",
    "summary": "Standard D365 — comprehensive role-based access control with security roles, duties, privileges, and permission hierarchy.",
    "detail": """
<p>D365 <strong>RBAC (Role-Based Access Control)</strong>:</p>
<ul>
<li><strong>Security roles</strong>: pre-defined and custom roles per job function — e.g., AP Clerk, Production Manager, Quality Inspector, Site Manager. NordHav's role matrix defines minimum required roles per position.</li>
<li><strong>Duties &amp; privileges</strong>: roles composed of duties (business-process groupings) and privileges (individual CRUD access rights) — granular control over create, read, update, delete per entity/form/action.</li>
<li><strong>Role hierarchy</strong>: roles can inherit from base roles — modifications at the duty/privilege level cascade appropriately.</li>
<li><strong>Organisational scope</strong>: roles scoped to: legal entity, operating unit, site, or global — ensuring users only access data for their authorised organisational context.</li>
<li><strong>Role assignment</strong>: roles assigned per user; users can hold multiple roles. Assignment auditable with full change history.</li>
</ul>
"""
},
"TEC-060": {
    "code": "S",
    "summary": "Standard D365 — extensible data security policies for row-level/data-level access control by legal entity, site, department, or custom dimension.",
    "detail": """
<p>Data-level security:</p>
<ul>
<li><strong>Extensible Data Security (XDS)</strong>: D365's framework for row-level security — policies restrict data access based on the user's organisational context. Example: a site manager at NordHav's Troms region sees only Troms farming data.</li>
<li><strong>Legal entity scoping</strong>: security roles are scoped per legal entity — a user in NordHav Processing AS only accesses that entity's transactions unless explicitly granted cross-entity access.</li>
<li><strong>Operating unit/site scoping</strong>: for multi-site operations, data access restricted to the user's assigned sites — warehouse workers at Bergen see only Bergen warehouse inventory.</li>
<li><strong>Power BI RLS</strong>: row-level security in Power BI mirrors D365 security scope — users only see analytics for their authorised data, preventing data leakage in reports.</li>
</ul>
"""
},
"TEC-061": {
    "code": "S",
    "summary": "Standard D365 — segregation of duties (SoD) framework with conflict detection, rule management, and violation alerting.",
    "detail": """
<p>Segregation of duties:</p>
<ul>
<li><strong>SoD rules</strong>: D365 includes a segregation-of-duties rule engine — administrators define conflicting duty pairs (e.g., "Create Vendor" and "Approve Vendor Payment" cannot be assigned to the same user).</li>
<li><strong>Conflict detection</strong>: when assigning roles, D365 checks for SoD violations and warns the administrator. Violations can be blocked or allowed with documented exception approval.</li>
<li><strong>Audit reporting</strong>: SoD violation report shows all current conflicts — used by internal audit for compliance review.</li>
<li><strong>Ongoing monitoring</strong>: periodic SoD review process — quarterly review of role assignments to ensure no drift has introduced new conflicts.</li>
</ul>
"""
},
"TEC-062": {
    "code": "S",
    "summary": "Standard D365 — comprehensive audit logging: user sign-ins, data changes (who, when, old/new values), report access, and admin actions with 7+ year retention.",
    "detail": """
<p>Audit logging:</p>
<ul>
<li><strong>Database logging</strong>: D365 database logging captures field-level changes on configured tables — who changed what, when, old value, and new value. Configured for sensitive tables: vendor master, bank accounts, security roles, GL accounts, and other critical data.</li>
<li><strong>User activity</strong>: sign-in events logged in Microsoft Entra ID sign-in logs — accessible via Azure AD portal and exportable to SIEM. Form access and data exports tracked.</li>
<li><strong>Admin actions</strong>: administrative changes (security role assignment, configuration changes, batch job modifications) logged with full audit trail.</li>
<li><strong>Retention</strong>: D365 audit logs retained per configurable policy. Microsoft Entra ID logs retained up to 30 days natively; for 7+ year retention, logs streamed to Azure Log Analytics / Microsoft Sentinel for long-term storage.</li>
<li><strong>Immutability</strong>: audit logs are append-only — entries cannot be modified or deleted by D365 users, ensuring integrity for regulatory compliance.</li>
</ul>
"""
},
"TEC-063": {
    "code": "S",
    "summary": "Standard D365 — GDPR management with Person Search (DSAR), data retention policies, consent management, and right-to-erasure support.",
    "detail": """
<p>GDPR compliance:</p>
<ul>
<li><strong>Person Search</strong>: D365 Person Search report locates all personal data across the system for Data Subject Access Request (DSAR) response — covers all modules (HR, AP, AR, contacts).</li>
<li><strong>Data classification</strong>: D365 metadata identifies personal data fields (name, address, national ID, bank account) with sensitivity classifications.</li>
<li><strong>Retention policies</strong>: configurable data retention — automatic archival/anonymisation of personal data beyond the legally required period.</li>
<li><strong>Right to erasure</strong>: supported via data anonymisation processes where legal retention requirements allow.</li>
<li><strong>Consent management</strong>: marketing consent and processing-purpose registration managed per customer/contact record.</li>
<li><strong>Activity logging</strong>: all personal data access logged for GDPR accountability.</li>
</ul>
"""
},
"TEC-064": {
    "code": "S",
    "summary": "Standard D365 — data encryption at rest (AES-256 via Azure SQL TDE) and in transit (TLS 1.2+) with Microsoft-managed keys as default.",
    "detail": """
<p>Data encryption:</p>
<ul>
<li><strong>At rest</strong>: Azure SQL Transparent Data Encryption (TDE) with AES-256 encryption — all D365 database files, backups, and log files encrypted. Storage (SharePoint, blob) also encrypted at rest.</li>
<li><strong>In transit</strong>: TLS 1.2+ enforced for all connections — browser to D365, D365 to Azure SQL, D365 to integration endpoints. Older TLS versions are disabled.</li>
<li><strong>Key management</strong>: Microsoft-managed encryption keys are the default. Customer-managed keys (CMK) available via Azure Key Vault for organisations with specific key-management requirements.</li>
<li><strong>End-to-end</strong>: data is encrypted at every stage — in the browser (HTTPS), in transit between Azure services, at rest in storage, and in backups. NordHav's data is never stored unencrypted.</li>
</ul>
"""
},
"TEC-065": {
    "code": "S",
    "summary": "Standard Microsoft — regular independent penetration testing of Azure and D365 with results available via the Service Trust Portal.",
    "detail": """
<p>Penetration testing:</p>
<ul>
<li><strong>Microsoft testing</strong>: Microsoft conducts regular (at least annual) penetration testing of Azure infrastructure and D365 applications using independent third-party security firms.</li>
<li><strong>Scope</strong>: testing covers: application-level vulnerabilities, infrastructure security, authentication mechanisms, data isolation between tenants, and API security.</li>
<li><strong>Results</strong>: summary penetration-test results and remediation evidence are available to customers via the <strong>Microsoft Service Trust Portal</strong> — NordHav can review these as part of their vendor due-diligence process.</li>
<li><strong>Bug bounty</strong>: Microsoft operates a public bug-bounty programme — external security researchers are incentivised to discover and responsibly disclose vulnerabilities.</li>
</ul>
"""
},
"TEC-066": {
    "code": "S",
    "summary": "Standard Microsoft — SOC 1/2 Type II, ISO 27001, ISO 27018, and additional compliance certifications published on the Service Trust Portal.",
    "detail": """
<p>Compliance certifications:</p>
<ul>
<li><strong>SOC 1 Type II</strong>: audit of internal controls relevant to financial reporting — relevant for NordHav's auditors assessing IT controls over financial data.</li>
<li><strong>SOC 2 Type II</strong>: audit of security, availability, processing integrity, confidentiality, and privacy controls — independently verified annually.</li>
<li><strong>ISO 27001</strong>: information security management system (ISMS) certification for Azure data centres and D365 operations.</li>
<li><strong>ISO 27018</strong>: protection of personal data in public clouds — specifically relevant for GDPR compliance.</li>
<li><strong>Additional</strong>: ISO 22301 (business continuity), CSA STAR, and regional certifications. Full list available on the Microsoft Service Trust Portal with downloadable audit reports.</li>
</ul>
"""
},
"TEC-067": {
    "code": "C",
    "summary": "Microsoft Entra Conditional Access — IP-based and network-based access restrictions using named locations and compliance policies.",
    "detail": """
<p>IP / network restrictions:</p>
<ul>
<li><strong>Conditional Access named locations</strong>: NordHav's corporate IP ranges and VPN exit points defined as "trusted locations" in Microsoft Entra ID. Access policies can restrict sensitive operations (admin access, financial data export) to trusted locations only.</li>
<li><strong>Block by location</strong>: access from unknown or specified geographic regions can be blocked or require additional verification.</li>
<li><strong>Compliant device requirement</strong>: Conditional Access can require that devices are Intune-compliant (managed, encrypted, up-to-date) before granting access — effectively combining IP and device posture checks.</li>
<li><strong>Optional full IP whitelist</strong>: for maximum restriction, D365 access can be limited to specific IP ranges — though this reduces flexibility for remote workers and mobile users.</li>
</ul>
"""
},
"TEC-068": {
    "code": "C",
    "summary": "D365 + Microsoft Entra — configurable session timeout, concurrent session management, and administrator forced sign-out capability.",
    "detail": """
<p>Session management:</p>
<ul>
<li><strong>Session timeout</strong>: D365 web client session timeout configurable via Microsoft Entra ID token lifetime policies — default idle timeout typically 60 minutes; adjustable per NordHav's security policy.</li>
<li><strong>Concurrent sessions</strong>: Microsoft Entra ID supports policies to limit or monitor concurrent sessions per user. D365 does not natively restrict concurrent sessions, but Conditional Access policies can enforce device compliance limits.</li>
<li><strong>Forced sign-out</strong>: administrators can revoke user sessions from Microsoft Entra ID — immediately invalidating all active sessions for a compromised or terminated user (within token refresh window). Emergency access: revoking refresh tokens forces re-authentication.</li>
<li><strong>Activity timeout warning</strong>: D365 can be configured to warn users before session expiry — allowing them to extend the session or save work.</li>
</ul>
"""
},
"TEC-069": {
    "code": "S",
    "summary": "Standard D365 — full data export via DMF in standard formats (CSV, XML, Excel) for data portability and vendor transition scenarios.",
    "detail": """
<p>Data export and portability:</p>
<ul>
<li><strong>DMF export</strong>: D365 Data Management Framework exports all major entities in CSV, XML, or Excel format. NordHav can export complete master data, transactional data, and configuration data at any time.</li>
<li><strong>Data entities</strong>: 3,000+ standard data entities cover all major business objects — ensuring comprehensive export coverage: GL, AP, AR, inventory, production, HR, quality, assets, projects, and more.</li>
<li><strong>Data packages</strong>: Export multiple entities as a data package (.zip) — complete dataset for migration or archival.</li>
<li><strong>Database export</strong>: D365 administrators can export the entire database as a .bacpac file via LCS — machine-readable, standard SQL format for maximum portability.</li>
<li><strong>No vendor lock-in</strong>: data is portable — NordHav retains full ownership and export rights to all their data at all times per Microsoft's cloud terms.</li>
</ul>
"""
},
"TEC-070": {
    "code": "S",
    "summary": "Standard Microsoft — D365 F&O is a commercially available SaaS product; NordHav's data is fully exportable; no proprietary lock-in on core ERP data.",
    "detail": """
<p>Vendor lock-in mitigation:</p>
<ul>
<li><strong>Commercial product</strong>: D365 F&amp;O is Microsoft's commercially available ERP — it is not a bespoke system. NordHav's configuration and data are portable.</li>
<li><strong>Data export</strong>: as described in TEC-069, all data is exportable in standard formats at any time. No contractual restriction on data extraction.</li>
<li><strong>Source code escrow</strong>: D365 F&amp;O is a SaaS product maintained by Microsoft — traditional source-code escrow is not applicable. However, Microsoft's financial stability and product continuity commitments (D365 is a strategic Microsoft platform) significantly mitigate vendor-risk.</li>
<li><strong>Customisation code</strong>: all NordHav-specific X++ extensions and Power Platform customisations are developed and owned by NordHav (or their implementation partner) — source code stored in NordHav's Azure DevOps repository.</li>
<li><strong>Microsoft commitment</strong>: Microsoft provides contractual commitments for data return upon subscription termination per the Microsoft Product Terms.</li>
</ul>
"""
},
"TEC-071": {
    "code": "S",
    "summary": "Standard Microsoft — documented Security Incident Response Plan (SSIRP) with max 72-hour breach notification per GDPR and contractual SLA.",
    "detail": """
<p>Security incident response:</p>
<ul>
<li><strong>Microsoft SSIRP</strong>: Microsoft's Security Service Incident Response Plan covers: detection, containment, eradication, recovery, and post-incident analysis for all Azure and D365 services.</li>
<li><strong>Notification SLA</strong>: Microsoft commits to notifying affected customers within <strong>72 hours</strong> of confirming a data breach — per GDPR Article 33 requirements and contractual commitments. In practice, notification is often within 24 hours.</li>
<li><strong>Escalation</strong>: NordHav's designated security contacts receive breach notifications via email and Azure Service Health. Microsoft provides: description of the incident, data affected, mitigation steps taken, and recommended customer actions.</li>
<li><strong>Post-incident</strong>: Microsoft publishes post-incident reports (PIR) detailing root cause, timeline, and preventive measures — available via the Service Trust Portal or directly to affected customers.</li>
</ul>
"""
},
"TEC-072": {
    "code": "S",
    "summary": "Standard D365 + Microsoft Entra — full compliance with Norwegian Personopplysningsloven and Datatilsynet guidance for personal data processing.",
    "detail": """
<p>Norwegian privacy compliance:</p>
<ul>
<li><strong>Personopplysningsloven</strong>: Norway's implementation of GDPR — D365's GDPR features (TEC-063) directly satisfy these requirements: lawful processing basis, data-subject rights, data protection impact assessment support, and breach notification.</li>
<li><strong>Datatilsynet guidance</strong>: NordHav's D365 configuration follows Datatilsynet's published guidance for: cloud-service usage by Norwegian organisations, transfers outside EEA (none — data stays in EU/EEA per TEC-002), and employee monitoring (limited to legitimate purposes with proper basis).</li>
<li><strong>Data Processing Agreement</strong>: Microsoft's Data Protection Addendum (DPA) satisfies the requirements of Personopplysningsloven for a data processor agreement — covers: processing scope, security measures, sub-processor management, and data return/deletion.</li>
<li><strong>Employee data</strong>: D365 HR module (Norwegian ISV payroll, absence, recruitment data) configured with access controls ensuring only HR-authorised personnel access employee personal data.</li>
</ul>
"""
},

# ═══════════════════════════════════════════════════════════════
#  11.8  IMPLEMENTATION & SUPPORT  (TEC-073 → TEC-080)
# ═══════════════════════════════════════════════════════════════
"TEC-073": {
    "code": "S",
    "summary": "Standard Microsoft — Success by Design implementation methodology with FastTrack governance, phased delivery, and milestone reviews.",
    "detail": """
<p>Implementation methodology:</p>
<ul>
<li><strong>Success by Design</strong>: Microsoft's prescribed implementation framework with FastTrack solution-architect oversight for enterprise D365 projects.</li>
<li><strong>Phases</strong>: Initiate → Implement → Prepare → Operate. Each phase has defined deliverables, gates, and governance checkpoints.</li>
<li><strong>Key reviews</strong>: Solution Blueprint Review (architecture validation), Mock Go-Live (dress rehearsal), Go-Live Readiness Review (final gate before production cutover).</li>
<li><strong>Governance</strong>: joint steering committee (NordHav + implementation partner), sprint-based agile delivery within each phase, and risk/issue management discipline.</li>
<li><strong>Role responsibilities</strong>: Microsoft FastTrack provides architectural oversight; implementation partner delivers functional and technical configuration; NordHav provides business knowledge, testing, and change management.</li>
</ul>
"""
},
"TEC-074": {
    "code": "C",
    "summary": "D365 DMF — phased data migration with master data first, opening balances second, open transactions third; validation at every stage.",
    "detail": """
<p>Data migration strategy:</p>
<ul>
<li><strong>Tool</strong>: D365 DMF (Data Management Framework) with NordHav's predefined entity templates (010–400 series).</li>
<li><strong>Phased approach</strong>: Phase 1: Master data (chart of accounts, customers, vendors, items, employees, assets). Phase 2: Opening balances (GL, AP, AR, inventory, fixed assets). Phase 3: Open transactions (open POs, SOs, production orders).</li>
<li><strong>Data cleansing</strong>: legacy data reviewed and cleansed before migration — duplicate removal, format standardisation, and completeness validation performed in staging area.</li>
<li><strong>Validation</strong>: each entity validated: field mapping verified, data-quality checks executed, test load in sandbox, reconciliation with source system, and sign-off before production migration.</li>
<li><strong>Cutover</strong>: final production migration executed during the go-live cutover window — parallel run with legacy system for defined period to validate completeness.</li>
</ul>
"""
},
"TEC-075": {
    "code": "C",
    "summary": "D365 + Microsoft Learn — role-based training with train-the-trainer, classroom workshops, e-learning, Task Recorder guides, and Norwegian-language materials.",
    "detail": """
<p>Training approach:</p>
<ul>
<li><strong>Train-the-trainer</strong>: NordHav key users (super users per functional area) receive deep training from the implementation partner — they then cascade knowledge to end users in their departments.</li>
<li><strong>End-user training</strong>: classroom workshops (hands-on in UAT environment), role-based agenda — each user group trained on their specific processes and D365 forms.</li>
<li><strong>E-learning</strong>: Microsoft Learn provides free, self-paced D365 learning paths accessible to all NordHav users — supplemented by NordHav-specific custom training materials.</li>
<li><strong>Task Recorder</strong>: D365's built-in Task Recorder creates step-by-step task guides from actual system usage — these serve as process documentation and in-app contextual help.</li>
<li><strong>Language</strong>: training materials produced in Norwegian Bokmål (primary) and English (secondary) — matching the D365 UI language configuration.</li>
<li><strong>Ongoing</strong>: refresher training and new-feature training provided with each major D365 service update.</li>
</ul>
"""
},
"TEC-076": {
    "code": "C",
    "summary": "Structured change management — stakeholder engagement, communication plan, resistance management, adoption metrics, and champion network.",
    "detail": """
<p>Change management approach:</p>
<ul>
<li><strong>Communication plan</strong>: regular communications to all NordHav stakeholders — project updates, milestone achievements, training schedules, and go-live countdown. Channels: Teams, email, intranet, and town-hall meetings.</li>
<li><strong>Stakeholder engagement</strong>: executive sponsor visibility, department-level change champions, and regular feedback loops — ensuring business ownership of the new system.</li>
<li><strong>Resistance management</strong>: proactive identification of resistance risks per department/user group — targeted interventions (additional training, 1-on-1 coaching, process redesign workshops) to address concerns.</li>
<li><strong>Champion network</strong>: change champions in each department/site act as local support and advocates — first point of contact for colleagues during the transition period.</li>
<li><strong>Adoption metrics</strong>: post-go-live tracking of: system usage (login frequency, feature adoption), support-ticket volume, and user satisfaction surveys — reported to steering committee.</li>
</ul>
"""
},
"TEC-077": {
    "code": "C",
    "summary": "Go-live support — on-site presence during cutover, 4–6 week hypercare with dedicated team, escalation procedures, and transition to steady-state.",
    "detail": """
<p>Go-live support:</p>
<ul>
<li><strong>Cutover support</strong>: implementation partner and NordHav key users co-located (on-site or virtual war room) during the cutover weekend — executing the cutover plan step-by-step with go/no-go checkpoints.</li>
<li><strong>Hypercare period</strong>: 4–6 weeks post-go-live with enhanced support — dedicated functional consultants available for immediate issue resolution, configuration adjustments, and user coaching.</li>
<li><strong>Escalation</strong>: 3-tier escalation — L1 (NordHav super user), L2 (implementation partner consultant on-call), L3 (Microsoft support request for platform issues). Critical issues escalated within 1 hour.</li>
<li><strong>Transition</strong>: at end of hypercare, formal handover to steady-state support model (TEC-078) — outstanding issues documented, knowledge transferred, and support responsibilities transitioned.</li>
</ul>
"""
},
"TEC-078": {
    "code": "C",
    "summary": "Tiered support model — L1 (NordHav super users), L2 (partner), L3 (Microsoft); Norwegian and English support; defined response SLAs by severity.",
    "detail": """
<p>Post-go-live support model:</p>
<ul>
<li><strong>L1 (internal)</strong>: NordHav's trained super users handle common questions, how-to guidance, and basic troubleshooting. Available during business hours.</li>
<li><strong>L2 (implementation partner)</strong>: functional and technical support for configuration issues, process questions, and minor enhancements. Response SLA: Critical (&lt; 2 hours), High (&lt; 4 hours), Medium (&lt; 1 business day), Low (&lt; 3 business days).</li>
<li><strong>L3 (Microsoft)</strong>: platform and product issues submitted via LCS support request — Microsoft engineering support for bugs, performance issues, and platform behaviour.</li>
<li><strong>Support hours</strong>: L1/L2 during Norwegian business hours (08:00–16:00 CET) as standard; 24/7 available for critical production-down scenarios (at premium rate).</li>
<li><strong>Language</strong>: Norwegian and English support available from both the implementation partner and Microsoft (Norwegian-speaking support resources confirmed).</li>
<li><strong>Channels</strong>: support portal (ticket logging), email, phone for critical issues, and Teams channel for ongoing communication.</li>
</ul>
"""
},
"TEC-079": {
    "code": "C",
    "summary": "Implementation partner — Norwegian-speaking consulting and support team familiar with Norwegian regulations, language, and business practices.",
    "detail": """
<p>Norwegian support capability:</p>
<ul>
<li><strong>Implementation partner</strong>: NordHav's implementation partner has a Norwegian consulting team — fluent in Norwegian Bokmål, deeply familiar with Norwegian business practices, tax regulations, labour laws, and industry norms.</li>
<li><strong>Regulatory expertise</strong>: consultants experienced with Norwegian-specific: accounting standards (NRS/NGAAP), VAT (MVA), payroll (A-melding, OTP, holiday pay), employment law (Arbeidsmiljøloven), and aquaculture regulations.</li>
<li><strong>Microsoft Norway</strong>: Microsoft has a Norwegian subsidiary with local support, sales, and FastTrack engagement resources — Norwegian-language support available for platform issues.</li>
<li><strong>ISV partners</strong>: Norwegian ISV solutions (e.g., payroll) provide Norwegian-language support and documentation.</li>
</ul>
"""
},
"TEC-080": {
    "code": "C",
    "summary": "Microsoft FastTrack + partner — customer success programme with dedicated account management, regular reviews, early feature access, and user community.",
    "detail": """
<p>Customer success programme:</p>
<ul>
<li><strong>Microsoft FastTrack</strong>: ongoing engagement for optimisation — FastTrack architects available for architectural reviews, feature adoption guidance, and best-practice recommendations beyond go-live.</li>
<li><strong>Partner account management</strong>: dedicated account manager from the implementation partner — regular quarterly business reviews covering: system health, enhancement pipeline, support metrics, and upcoming D365 features.</li>
<li><strong>Feature adoption</strong>: proactive communication about new D365 features relevant to NordHav — with assessment and implementation support for high-value enhancements.</li>
<li><strong>User community</strong>: access to D365 user groups (Nordic D365 User Group, global Dynamics community) for peer learning, best-practice sharing, and Microsoft engagement.</li>
<li><strong>Continuous improvement</strong>: annual "health check" review of NordHav's D365 usage — identify under-utilised features, optimisation opportunities, and alignment with evolving business needs.</li>
</ul>
"""
},
}
