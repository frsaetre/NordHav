"""Solution response data — HR & Payroll (HRP-001 → HRP-045)"""

SOLUTIONS_HRP = {
# ═══════════════════════════════════════════════════════════════
#  10.1  HR MASTER DATA & ORGANISATION  (HRP-001 → HRP-007)
# ═══════════════════════════════════════════════════════════════
"HRP-001": {"code": "S", "summary": "Standard D365 HR — comprehensive employee master with personal, employment, position, and history data.",
    "detail": "<p>D365 <strong>Human Resources</strong> employee master: personal data (name, fødselsnummer, DOB, gender, address, emergency contacts, bank account, tax info), employment data (start date, contract type fast/midlertidig, working hours, FTE%, probation, notice period), position data (position, department, reporting line, cost centre, work location), and full employment history with effective dates.</p>"},
"HRP-002": {"code": "S", "summary": "Standard D365 HR — organisational hierarchy: company → division → department → team → position with historical views.",
    "detail": "<p>D365 organisational modelling: legal entities, operating units (departments, cost centres, business units by region), position hierarchy (CEO → directors → managers → team leaders → workers), and job framework (families, jobs, role descriptions). Historical views and planned reorganisations supported.</p>"},
"HRP-003": {"code": "S", "summary": "Standard D365 HR — position management independent of employees with descriptions, grades, reporting, and headcount planning.",
    "detail": "<p>Position management: positions defined independently of employees with: description, grade/level, reporting relationships, budget status (filled/vacant/planned), and headcount planning. Workforce planning uses position data for: budgeted FTE, vacancy tracking, and hiring pipeline.</p>"},
"HRP-004": {"code": "S", "summary": "Standard D365 HR — employment contract management per Norwegian AML with contract types, terms, and renewal tracking.",
    "detail": "<p>Contract management: types (permanent/fast, temporary/midlertidig, seasonal/sesong, apprentice/lærling, contractor). Terms: hours, position, salary, notice period, non-compete. Document generation from D365 templates. Temporary contract expiry tracking with alerts and AML §14-9 compliance checking for maximum duration.</p>"},
"HRP-005": {"code": "S", "summary": "Standard D365 HR document management — employee documents stored with GDPR-compliant access controls and retention policies.",
    "detail": "<p>HR document management: contracts, certifications, training records, performance reviews stored in D365/SharePoint with: access controls (HR-only for sensitive documents), retention policies per document type, GDPR compliance (data minimisation, purpose limitation), and audit trail on access.</p>"},
"HRP-006": {"code": "S", "summary": "Standard D365 HR Employee Self-Service — portal/app for payslips, personal details, leave, time, training, and policies.",
    "detail": "<p>Employee Self-Service (ESS): web/Teams access for: view/update personal details, submit leave requests with balance visibility, register time, view payslips and tax documents, view team calendar, access company policies, complete onboarding tasks, and view competence profile and training history.</p>"},
"HRP-007": {"code": "S", "summary": "Standard D365 HR Manager Self-Service — team management with approvals, dashboard, recruitment, and cost reporting.",
    "detail": "<p>Manager Self-Service (MSS): approve leave, view team attendance/absence calendar, initiate recruitment requisitions, conduct performance reviews, approve overtime/time adjustments, view team competence matrix, access team HR analytics. All workflows accessible via mobile for remote managers.</p>"},

# ═══════════════════════════════════════════════════════════════
#  10.2  RECRUITMENT & ONBOARDING  (HRP-008 → HRP-011)
# ═══════════════════════════════════════════════════════════════
"HRP-008": {"code": "S", "summary": "Standard D365 HR Recruitment — workflow from requisition through job posting, applicant tracking, interviews, offer, and hire.",
    "detail": "<p>D365 Recruitment: requisition (position, qualifications, employment type, compensation range, justification) → approval → recruitment project → job posting → applicant pipeline (Applied → Screened → Interviewed → Offered → Hired or Rejected) → offer letter generation → hire.</p>"},
"HRP-009": {"code": "C", "summary": "D365 HR — seasonal worker management with batch hiring, recurring contracts, re-hire preferences, and accommodation tracking.",
    "detail": "<p>Seasonal worker support: batch hiring processes for ~85 processing plant seasonal staff. Recurring seasonal contracts with previous-season assignment history. Re-hire preference tracking. Accommodation/dormitory tracking where NordHav provides housing. Seasonal contract template with simplified onboarding for returning workers.</p>"},
"HRP-010": {"code": "S", "summary": "Standard D365 HR — automated onboarding checklist: IT, HSE induction, food hygiene, PPE, workstation, mentor, orientation.",
    "detail": "<p>Onboarding: configurable checklist per position type with tasks assigned to: IT (accounts, equipment), HR (contract, policy acknowledgement), Manager (introduction, training plan), Facilities (access card, locker), Quality/HSE (safety induction, food hygiene). Task tracking with due dates relative to start. ESS access before Day 1.</p>"},
"HRP-011": {"code": "S", "summary": "Standard D365 HR — structured offboarding with IT deactivation, equipment return, final pay, exit interview, and archiving.",
    "detail": "<p>Offboarding: termination/resignation triggers checklist: IT deactivation, equipment return, final pay calculation, accrued leave settlement, exit interview, handover tasks. All tracked with responsible party and due dates relative to last working day.</p>"},

# ═══════════════════════════════════════════════════════════════
#  10.3  TIME & ATTENDANCE  (HRP-012 → HRP-018)
# ═══════════════════════════════════════════════════════════════
"HRP-012": {"code": "S", "summary": "Standard D365 Time & Attendance — multiple registration methods: time clocks, mobile app, web, and manager entry.",
    "detail": "<p>D365 Time &amp; Attendance: clock-in/out terminals at processing plants, mobile app for field/sea workers, web interface for office staff, manager entry on behalf. Working time profiles per shift pattern. Norwegian AML compliance: max 9h/day, overtime rules (40h/week basis), rest period requirements (11h daily, 35h weekly). Break handling per collective agreement.</p>"},
"HRP-013": {"code": "S", "summary": "Standard D365 Time & Attendance — complex shift patterns: 2-shift processing, 3-shift smolt, offshore rotation, and flextime.",
    "detail": "<p>Shift management: profiles for 2-shift processing (06-14, 14-22), 3-shift smolt (24/7), offshore-style sea-site rotation (2 on/2 off), and flexible office hours. Seasonal scaling: extra shifts during harvest peaks. Shift swap requests via ESS with manager approval.</p>"},
"HRP-014": {"code": "S", "summary": "Standard D365 Time & Attendance — automatic overtime calculation per AML and collective agreements with daily/weekly thresholds.",
    "detail": "<p>Overtime: automatic calculation per AML (40h/week base, or 36/38 per collective agreement). Rates per agreement: 50% first 2h Mon-Fri, 100% subsequent/weekends/holidays. Approval workflow. Overtime caps: 10h/week, 25h/4 weeks, 200h/year per AML §10-6.</p>"},
"HRP-015": {"code": "S", "summary": "Standard D365 Time & Attendance — shift premiums per collective agreement: evening, night, Saturday, Sunday/holiday, offshore.",
    "detail": "<p>Shift premiums: configurable per collective agreement — evening, night, Saturday, Sunday/holiday, offshore/remote allowance. Cold storage supplements for processing workers. All premiums calculated from Time &amp; Attendance data and passed to ISV payroll for payment.</p>"},
"HRP-016": {"code": "S", "summary": "Standard D365 Time & Attendance — manager approval workflow before payroll with exception highlighting.",
    "detail": "<p>Time approval: manager reviews and approves team time registrations before payroll processing. Exceptions highlighted: overtime, absences, deviations from schedule. Configurable delegation for absent managers. Approved time released to payroll integration.</p>"},
"HRP-017": {"code": "S", "summary": "Standard D365 Time & Attendance — Norwegian working time compliance monitoring with max hours, rest periods, and violation alerts.",
    "detail": "<p>Working time compliance: D365 monitors against AML: max daily/weekly hours, minimum 11h rest between shifts, max overtime hours. Violations flagged with alerts to HR and manager. Compliance reports for Arbeidstilsynet inspection readiness.</p>"},
"HRP-018": {"code": "S", "summary": "Standard D365 Time & Attendance — project/activity time registration for maintenance, capital projects, and farming operations.",
    "detail": "<p>Project time: employees optionally register time against: projects (maintenance, CAPEX), cost activities (specific farming operations), or indirect activities. Labour cost distributed to production orders, projects, and cost centres from time registrations.</p>"},

# ═══════════════════════════════════════════════════════════════
#  10.4  LEAVE MANAGEMENT  (HRP-019 → HRP-024)
# ═══════════════════════════════════════════════════════════════
"HRP-019": {"code": "S", "summary": "Standard D365 HR Leave — Norwegian annual leave (Ferie) per Ferieloven: 25 days, 60+ extra week, carry-forward, holiday pay.",
    "detail": "<p>Annual leave per Ferieloven: 25 working days/year (31 for 60+). Leave earned prior year, taken current year. Holiday pay 10.2% (12% for 60+). Carry-forward up to 12 days with agreement. June payout calculation.</p>"},
"HRP-020": {"code": "S", "summary": "Standard D365 HR Leave — Norwegian sick leave management: egenmelding, sykmelding, employer period (16d), NAV period, follow-up.",
    "detail": "<p>Sick leave per Norwegian rules: self-certification (egenmelding: 3 calendar days, 4× per 12 months; IA agreement: 8 days, 24 days total). Doctor's cert (sykmelding) from day 4. Employer period: first 16 days at 100% (up to 6G). NAV period from day 17 with reimbursement. Partial sick leave support. Follow-up milestones: 4 weeks (plan), 7 weeks (dialogue), 26 weeks (NAV activity).</p>"},
"HRP-021": {"code": "C", "summary": "D365 HR + NAV integration — digital sick note (digital sykmelding) automated receipt and processing.",
    "detail": "<p>Digital sykmelding integration: automated receipt from NAV's digital system. Sick note data (degree, diagnosis group, duration) auto-populated in D365 HR leave records. Reduces manual entry and ensures timely processing.</p>"},
"HRP-022": {"code": "S", "summary": "Standard D365 HR Leave — Norwegian parental leave with mother/father quota, shared period, 80%/100% rate, and NAV integration.",
    "detail": "<p>Parental leave per Folketrygdloven: leave tracking with quota allocation (mandatory mother period, father quota, shared period), percentage choice (100% or 80% NAV rate), gradual return support. D365 tracks employer obligation for equivalent position return.</p>"},
"HRP-023": {"code": "S", "summary": "Standard D365 HR Leave — additional leave types: compassionate, military, study, union, care leave with configurable rules.",
    "detail": "<p>Other leave types: care of sick child (omsorgsdager: 10 days/year per child under 12), compassionate leave, military service, study leave per AML §12-11, union representative leave, and collective agreement special leave (moving day, marriage). Each with configurable rules and entitlements.</p>"},
"HRP-024": {"code": "S", "summary": "Standard D365 HR Leave — visual leave calendar showing team plans for coverage checking and conflict avoidance.",
    "detail": "<p>Leave calendar: visual display of team leave plans accessible to managers and team members. Coverage checking to avoid scheduling conflicts. Manager can identify periods with insufficient coverage before approving leave requests.</p>"},

# ═══════════════════════════════════════════════════════════════
#  10.5  PAYROLL  (HRP-025 → HRP-036)
# ═══════════════════════════════════════════════════════════════
"HRP-025": {"code": "D", "summary": "Delivered via Norwegian Payroll ISV (Gap G-03) — certified payroll engine for gross-to-net with tax, pension, and deductions.",
    "detail": "<p>Norwegian payroll via <strong>certified ISV</strong> (Gap G-03 — e.g., Visma, Huldt &amp; Lillevik): gross-to-net computation with income tax (from Skatteetaten tax cards), employee pension, union dues, and other deductions. D365 HR exports employee/time/absence data; ISV returns payroll results for GL posting.</p>"},
"HRP-026": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — multiple collective agreement payroll rules: base rates, seniority, shift premiums, overtime.",
    "detail": "<p>Collective agreement rules in ISV: simultaneous support for NNN (processing), Fellesforbundet (operations), etc. Base rates, seniority increments, shift premiums, overtime rates all per specific agreement terms.</p>"},
"HRP-027": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — electronic tax card (skattekort) retrieval from Skatteetaten with automatic annual update.",
    "detail": "<p>Tax card via ISV: electronic skattekort retrieval from Skatteetaten (Altinn). Tax table calculation (monthly table, percentage, or bracketed per card type). Year-end årsoppgave production. Updated annually and upon changes.</p>"},
"HRP-028": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — arbeidsgiveravgift calculation with zone-differentiated rates per employee location.",
    "detail": "<p>Employer social contributions via ISV: zone-differentiated arbeidsgiveravgift rates per municipality (Sone 1-5). Correct rate per employee's work location. NordHav operations span multiple zones (rural northern Norway: lower rates). Contributions posted to D365 GL per department/cost centre.</p>"},
"HRP-029": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — mandatory pension (OTP) calculation per Norwegian OTP Act with contribution rates.",
    "detail": "<p>Pension via ISV: OTP calculated per Lov om obligatorisk tjenestepensjon: minimum 2% of salary between 1G-12G. NordHav scheme terms configured (contribution rates, disability/survivor coverage). Employee/employer shares processed. Annual pension provider reporting.</p>"},
"HRP-030": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — holiday pay (feriepenger) calculation at 10.2%/12% per Ferieloven with June payout.",
    "detail": "<p>Feriepenger via ISV: 10.2% (12% for 60+) of qualifying earnings. Base includes: salary, overtime, shift supplements, qualifying bonus, sick pay during employer period. June payout with vacation month withheld. Year-end feriepengeliste. Special cases: partial year, termination, carry-forward.</p>"},
"HRP-031": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — A-melding monthly reporting to Skatteetaten, NAV, and SSB in required electronic format.",
    "detail": "<p>A-melding via ISV payroll: combined monthly report of income, employment, and tax deduction information. Generated and submitted electronically to Skatteetaten, NAV, and SSB. All required data fields populated from payroll calculations.</p>"},
"HRP-032": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — digital payslip generation and distribution via ESS, email, or Digipost/Altinn.",
    "detail": "<p>Payslips via ISV: monthly payslip with Norwegian legal content: gross breakdown, variable pay, pension, tax, net pay, holiday pay accrual, employer costs. Electronic distribution via ISV portal, D365 ESS, or digital mailbox. Archive accessible for current and prior periods.</p>"},
"HRP-033": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — salary bank payment file in Norwegian format for bulk salary payments.",
    "detail": "<p>Bank payment file via ISV: standard Norwegian bank file format for bulk salary payments. Generated after payroll approval. Uploaded to banking system (DNB, Nordea) for processing.</p>"},
"HRP-034": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — annual payroll reporting: årsoppgave, A-melding reconciliation, and Skatteetaten submission.",
    "detail": "<p>Year-end reporting via ISV: annual summary per employee (årsoppgave), reconciliation of all A-melding submissions, and reporting to Skatteetaten. Ensures all annual totals balance with monthly submissions.</p>"},
"HRP-035": {"code": "D", "summary": "Delivered via ISV (Gap G-03) — retroactive pay adjustments with recalculation of tax and contributions.",
    "detail": "<p>Retroactive adjustments via ISV: collective agreement back-pay, correction of prior-period errors. Recalculation of: tax (updated table/percentage), employer NI, pension contributions, and holiday pay for affected periods. Difference amounts calculated and paid in current period.</p>"},
"HRP-036": {"code": "S", "summary": "Standard D365 Expense Management — expense claims with receipt upload, approval workflow, and tax treatment per Skatteetaten rules.",
    "detail": "<p>Expense reimbursement via D365 Expense Management: submission with receipt upload (photo capture on mobile), approval workflow, tax treatment per Skatteetaten rules (travel, subsistence/diett, mileage/kilometergodtgjørelse). Approved expenses paid via payroll or AP.</p>"},

# ═══════════════════════════════════════════════════════════════
#  10.6  COMPETENCE & TRAINING  (HRP-037 → HRP-040)
# ═══════════════════════════════════════════════════════════════
"HRP-037": {"code": "S", "summary": "Standard D365 HR — training register per employee: courses completed, certifications, expiry dates, and training history.",
    "detail": "<p>Training register: per employee records of: courses completed, certifications obtained, certification expiry dates, continuing education, and full training history. Accessible via ESS for employees and MSS for managers.</p>"},
"HRP-038": {"code": "S", "summary": "Standard D365 HR + Power Automate — mandatory training tracking by position with certification expiry alerts.",
    "detail": "<p>Mandatory training: required per position — food safety, HSE induction, first aid, maritime safety, forklift, electrical safety. Tracked with expiry dates. Power Automate alerts at 60 and 7 days before expiry. Compliance dashboard: % current by facility/department. Non-compliance escalation.</p>"},
"HRP-039": {"code": "C", "summary": "D365 HR — training planning with course catalogue, scheduling, enrolment, instructor assignment, and cost tracking.",
    "detail": "<p>Training planning: course catalogue with content, duration, prerequisites, max participants. Session scheduling and employee enrolment. Instructor assignment. Completion and attendance recording. Training spend tracked per department/employee for budget management.</p>"},
"HRP-040": {"code": "C", "summary": "D365 HR — visual competence matrix by team showing skills coverage, gaps, and development priorities.",
    "detail": "<p>Competence matrix: skills framework per job/position with required competences and proficiency levels. Employee competence profile: actual vs. required. Gap analysis → training needs. Visual matrix per department showing coverage per critical skill. Succession risk identification where single points of competence exist.</p>"},

# ═══════════════════════════════════════════════════════════════
#  10.7  HR ANALYTICS & REPORTING  (HRP-041 → HRP-045)
# ═══════════════════════════════════════════════════════════════
"HRP-041": {"code": "C", "summary": "D365 HR + Power BI — HR dashboard with headcount, turnover, sick leave, overtime, training, and recruitment KPIs.",
    "detail": "<p>HR dashboard: headcount by location/department, turnover rate (voluntary/involuntary), sick leave %, overtime hours, training completion rate, recruitment pipeline. Company-wide, regional, and per-facility views.</p>"},
"HRP-042": {"code": "C", "summary": "D365 HR + Power BI — sick leave analytics: absence rate, short/long-term trends, cost, and IA agreement target tracking.",
    "detail": "<p>Sickness analytics: absence rate per department/location/period (target: &lt;5.6% per IA agreement). Short vs. long-term breakdown. Cost: employer period cost, lost productivity. Trend: MoM, YoY, seasonal patterns. Follow-up compliance: % with timely plans at 4/7 weeks.</p>"},
"HRP-043": {"code": "S", "summary": "Standard D365 HR + ISV payroll + Power BI — payroll cost reports by department, cost centre, project, and breakdown.",
    "detail": "<p>Payroll cost reporting: total cost by department, cost centre, project, location, category. Breakdown: base salary, overtime, premiums, employer NI (arbeidsgiveravgift), pension (OTP), holiday pay accrual. Data from ISV payroll GL integration and D365 HR. Power BI visualisation.</p>"},
"HRP-044": {"code": "C", "summary": "D365 HR + Power BI — headcount/FTE reporting by location, department, contract type, age, gender, and seniority.",
    "detail": "<p>Headcount reporting: employee count and FTE by: location, department, contract type (permanent/temp/seasonal), age group, gender, seniority. Diversity and inclusion metrics. Trend analysis over time.</p>"},
"HRP-045": {"code": "S", "summary": "Standard D365 HR — full GDPR compliance: person search (DSAR), retention policies, consent management, and right to erasure.",
    "detail": "<p>GDPR compliance: Person Search for Data Subject Access Requests (DSAR). Data retention policies with automated purging beyond legal periods. Consent management per processing purpose. Right to erasure (with employment record retention exceptions). Data access logging. Privacy impact assessment support.</p>"},
}
