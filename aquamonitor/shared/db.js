/* ═══════════════════════════════════════════════════════════
   AquaMonitor Data Service — localStorage-backed CRUD
   NordHav Aquaculture AS · Legal Entity: NHA
   ═══════════════════════════════════════════════════════════ */

const DB = (() => {
  const PREFIX = 'aqm_';

  // ── Core storage helpers ────────────────────────────────
  function _load(coll) {
    try { return JSON.parse(localStorage.getItem(PREFIX + coll) || '[]'); }
    catch { return []; }
  }
  function _save(coll, data) {
    localStorage.setItem(PREFIX + coll, JSON.stringify(data));
  }
  function _nextId(coll) {
    const rows = _load(coll);
    return rows.length ? Math.max(...rows.map(r => r.id || 0)) + 1 : 1;
  }

  // ── Public API ──────────────────────────────────────────
  const api = {
    getAll:  (c)       => _load(c),
    get:     (c, id)   => _load(c).find(r => r.id === id) || null,
    query:   (c, fn)   => _load(c).filter(fn),
    add:     (c, rec)  => { const rows = _load(c); rec.id = _nextId(c); rows.push(rec); _save(c, rows); return rec; },
    update:  (c, id, u)=> { const rows = _load(c).map(r => r.id === id ? {...r,...u} : r); _save(c, rows); },
    delete:  (c, id)   => { _save(c, _load(c).filter(r => r.id !== id)); },
    count:   (c)       => _load(c).length,
    clear:   (c)       => _save(c, []),
    clearAll:()        => Object.keys(localStorage).filter(k=>k.startsWith(PREFIX)).forEach(k=>localStorage.removeItem(k)),
  };

  // ── Seed data ───────────────────────────────────────────
  const SEED = {
    sites: [
      { id:1, name:'Rognøy',      code:'SEA-ROGNOY', kommune:'Bjørnafjorden', zone:'H3', mab:2800, biomass:2140, pens:8,  liceStatus:'amber', gen:'GEN-2023B', temp:8.2 },
      { id:2, name:'Kvitholmen',  code:'SEA-KVH',    kommune:'Øygarden',      zone:'H2', mab:1600, biomass:1380, pens:7,  liceStatus:'red',   gen:'GEN-2023A', temp:7.9 },
      { id:3, name:'Nordhamn',    code:'SEA-NHM',    kommune:'Fitjar',        zone:'H3', mab:2300, biomass:1300, pens:6,  liceStatus:'green', gen:'GEN-2022C', temp:8.0 },
    ],
    pens: [
      // Rognøy (siteId:1)
      { id:1,  siteId:1, name:'PEN-01', biomass:268, fishCount:70500, liceAF:0.18, withdrawal:false, withdrawalExpiry:null },
      { id:2,  siteId:1, name:'PEN-02', biomass:274, fishCount:70200, liceAF:0.29, withdrawal:false, withdrawalExpiry:null },
      { id:3,  siteId:1, name:'PEN-03', biomass:262, fishCount:70800, liceAF:0.44, withdrawal:false, withdrawalExpiry:null },
      { id:4,  siteId:1, name:'PEN-04', biomass:271, fishCount:75400, liceAF:0.62, withdrawal:false, withdrawalExpiry:null },
      { id:5,  siteId:1, name:'PEN-05', biomass:280, fishCount:72000, liceAF:0.12, withdrawal:false, withdrawalExpiry:null },
      { id:6,  siteId:1, name:'PEN-06', biomass:255, fishCount:65000, liceAF:0.21, withdrawal:false, withdrawalExpiry:null },
      { id:7,  siteId:1, name:'PEN-07', biomass:265, fishCount:68000, liceAF:0.35, withdrawal:false, withdrawalExpiry:null },
      { id:8,  siteId:1, name:'PEN-08', biomass:265, fishCount:68000, liceAF:0.19, withdrawal:false, withdrawalExpiry:null },
      // Kvitholmen (siteId:2)
      { id:9,  siteId:2, name:'PEN-01', biomass:198, fishCount:52000, liceAF:0.22, withdrawal:false, withdrawalExpiry:null },
      { id:10, siteId:2, name:'PEN-02', biomass:195, fishCount:51000, liceAF:0.55, withdrawal:true,  withdrawalExpiry:'2026-03-10' },
      { id:11, siteId:2, name:'PEN-03', biomass:202, fishCount:53000, liceAF:0.38, withdrawal:false, withdrawalExpiry:null },
      { id:12, siteId:2, name:'PEN-04', biomass:190, fishCount:50000, liceAF:0.48, withdrawal:false, withdrawalExpiry:null },
      { id:13, siteId:2, name:'PEN-05', biomass:198, fishCount:52000, liceAF:0.31, withdrawal:false, withdrawalExpiry:null },
      { id:14, siteId:2, name:'PEN-06', biomass:200, fishCount:53000, liceAF:0.72, withdrawal:false, withdrawalExpiry:null },
      { id:15, siteId:2, name:'PEN-07', biomass:197, fishCount:51800, liceAF:0.63, withdrawal:false, withdrawalExpiry:null },
      // Nordhamn (siteId:3)
      { id:16, siteId:3, name:'PEN-01', biomass:220, fishCount:58000, liceAF:0.14, withdrawal:false, withdrawalExpiry:null },
      { id:17, siteId:3, name:'PEN-02', biomass:215, fishCount:57000, liceAF:0.18, withdrawal:false, withdrawalExpiry:null },
      { id:18, siteId:3, name:'PEN-03', biomass:210, fishCount:55000, liceAF:0.09, withdrawal:true,  withdrawalExpiry:'2026-03-15' },
      { id:19, siteId:3, name:'PEN-04', biomass:225, fishCount:59000, liceAF:0.21, withdrawal:false, withdrawalExpiry:null },
      { id:20, siteId:3, name:'PEN-05', biomass:218, fishCount:57500, liceAF:0.17, withdrawal:false, withdrawalExpiry:null },
      { id:21, siteId:3, name:'PEN-06', biomass:212, fishCount:56000, liceAF:0.22, withdrawal:false, withdrawalExpiry:null },
    ],
    mortalities: [
      { id:1, siteId:1, penId:1, date:'2026-02-23', deadFish:12, avgWeight:3.8, cause:'Unknown',     notes:'' },
      { id:2, siteId:1, penId:2, date:'2026-02-23', deadFish:8,  avgWeight:3.9, cause:'Predation',   notes:'' },
      { id:3, siteId:1, penId:3, date:'2026-02-23', deadFish:5,  avgWeight:3.7, cause:'Unknown',     notes:'' },
      { id:4, siteId:1, penId:4, date:'2026-02-23', deadFish:34, avgWeight:3.6, cause:'Disease',     notes:'Gill issue noted' },
      { id:5, siteId:2, penId:9, date:'2026-02-23', deadFish:9,  avgWeight:3.5, cause:'Unknown',     notes:'' },
      { id:6, siteId:3, penId:16,date:'2026-02-22', deadFish:6,  avgWeight:4.1, cause:'Handling',    notes:'Post-crowding' },
      { id:7, siteId:1, penId:1, date:'2026-02-22', deadFish:10, avgWeight:3.8, cause:'Unknown',     notes:'' },
      { id:8, siteId:1, penId:4, date:'2026-02-22', deadFish:18, avgWeight:3.6, cause:'Disease',     notes:'AGD suspected' },
    ],
    liceCounts: [
      { id:1,  siteId:1, penId:1,  week:'W08-2026', date:'2026-02-17', chalimus:0.4, preAdultM:0.2, preAdultF:0.3, adultF:0.18, submitted:true },
      { id:2,  siteId:1, penId:2,  week:'W08-2026', date:'2026-02-17', chalimus:0.7, preAdultM:0.5, preAdultF:0.4, adultF:0.29, submitted:true },
      { id:3,  siteId:1, penId:3,  week:'W08-2026', date:'2026-02-17', chalimus:1.2, preAdultM:0.8, preAdultF:0.6, adultF:0.44, submitted:true },
      { id:4,  siteId:1, penId:4,  week:'W08-2026', date:'2026-02-17', chalimus:2.1, preAdultM:1.4, preAdultF:1.1, adultF:0.62, submitted:false },
      { id:5,  siteId:2, penId:14, week:'W08-2026', date:'2026-02-17', chalimus:2.8, preAdultM:1.9, preAdultF:1.4, adultF:0.72, submitted:false },
      { id:6,  siteId:2, penId:15, week:'W08-2026', date:'2026-02-17', chalimus:2.3, preAdultM:1.6, preAdultF:1.2, adultF:0.63, submitted:false },
      { id:7,  siteId:1, penId:1,  week:'W07-2026', date:'2026-02-10', chalimus:0.3, preAdultM:0.2, preAdultF:0.2, adultF:0.14, submitted:true },
      { id:8,  siteId:1, penId:4,  week:'W07-2026', date:'2026-02-10', chalimus:1.8, preAdultM:1.2, preAdultF:0.9, adultF:0.55, submitted:true },
    ],
    treatments: [
      { id:1, siteId:3, penId:18, type:'Bath',    medication:'Salmosan (Azamethiphos)', date:'2026-02-19', fishTreated:55000, vessel:'MS Nordic Star', preAF:0.68, postAF:0.11, withdrawalDays:24, withdrawalExpiry:'2026-03-15', d365WO:'WO-2026-0142' },
      { id:2, siteId:2, penId:10, type:'Bath',    medication:'AlphaMax (Deltamethrin)', date:'2026-01-10', fishTreated:51000, vessel:'MS Bergen Viking', preAF:0.72, postAF:0.08, withdrawalDays:14, withdrawalExpiry:'2026-01-24', d365WO:'WO-2026-0088' },
    ],
    prescriptions: [
      { id:1, siteId:3, penId:18, medication:'Salmosan (Azamethiphos)', issued:'2026-02-19', expiry:'2026-03-15', vet:'Dr. Hansen (Aqua Fish Health AS)', active:true },
      { id:2, siteId:2, penId:10, medication:'AlphaMax (Deltamethrin)',  issued:'2026-01-10', expiry:'2026-01-24', vet:'Dr. Løvås (Aqua Fish Health AS)',  active:false },
    ],
    healthVisits: [
      { id:1, siteId:1, date:'2026-02-22', vet:'Dr. Anette Løvås (Aqua Fish Health AS)', pens:'PEN-01, PEN-02, PEN-04', overallScore:'Moderate Concern', gillScore:2.1, notes:'PEN-04: AGD present. Gill histopathology sent to FHF. Reassess in 14 days.' },
      { id:2, siteId:3, date:'2026-02-10', vet:'Dr. Hansen (Aqua Fish Health AS)',       pens:'All pens',               overallScore:'Good',              gillScore:1.2, notes:'All pens normal. Continue monitoring.' },
    ],
    diseaseEvents: [
      { id:1, siteId:1, penId:4, date:'2026-02-22', diagnosis:'Amoebic Gill Disease (AGD)', severity:'Moderate', labRef:'FHF-2026-1182', notifiable:false, notes:'Sample sent to FHF Bergen' },
    ],
    harvestPlans: [
      { id:1, siteId:1, pens:'PEN-01, PEN-02', targetDate:'2026-03-03', biomass:520, fishCount:138000, vessel:'MS Nordic Star', status:'Approved', d365Order:'PO-NHA-18441', readiness:100 },
      { id:2, siteId:3, pens:'PEN-03',          targetDate:'2026-03-17', biomass:210, fishCount:54000,  vessel:'MS Bergen Viking', status:'On Hold',  d365Order:null, readiness:60 },
      { id:3, siteId:2, pens:'PEN-06, PEN-07',  targetDate:'2026-03-25', biomass:310, fishCount:80000,  vessel:'TBD',            status:'Draft',    d365Order:null, readiness:35 },
    ],
    wellBoatBookings: [
      { id:1, vesselName:'MS Nordic Star',   type:'Harvest',   siteId:1, siteName:'Rognøy',    date:'2026-03-03', purpose:'HP-2026-007 harvest PEN-01/02',       status:'Confirmed' },
      { id:2, vesselName:'MS Nordic Star',   type:'Transfer',  siteId:1, siteName:'Rognøy',    date:'2026-03-15', purpose:'Smolt transfer EGG-2025-A (420k fish)', status:'Confirmed' },
      { id:3, vesselName:'MS Bergen Viking', type:'Harvest',   siteId:3, siteName:'Nordhamn',  date:'2026-03-17', purpose:'HP-2026-008 harvest PEN-03',           status:'Tentative' },
      { id:4, vesselName:'MS Nordic Star',   type:'Treatment', siteId:2, siteName:'Kvitholmen',date:'2026-02-28', purpose:'Lice treatment KVH PEN-04/07',        status:'Planned' },
    ],
    escapeEvents: [],
    eggBatches: [
      { id:1, batchId:'EGG-2025-A', supplier:'AquaGen',    received:'2025-11-12', eggs:2400000, facility:'Masfjorden', degreeDays:810, stage:'Parr phase',    gen:'GEN-2025A' },
      { id:2, batchId:'EGG-2025-B', supplier:'SalmoBreed', received:'2025-12-03', eggs:1800000, facility:'Kvam',       degreeDays:640, stage:'First feeding',  gen:'GEN-2025B' },
      { id:3, batchId:'EGG-2026-A', supplier:'AquaGen',    received:'2026-01-08', eggs:2100000, facility:'Masfjorden', degreeDays:290, stage:'Incubation',     gen:'GEN-2026A' },
    ],
    weightSamples: [
      { id:1, siteId:1, penId:1,  date:'2026-02-20', sampleSize:30, avgWeight:3.82, minWeight:2.9, maxWeight:4.8 },
      { id:2, siteId:1, penId:5,  date:'2026-02-19', sampleSize:25, avgWeight:3.24, minWeight:2.6, maxWeight:4.1 },
      { id:3, siteId:2, penId:9,  date:'2026-02-18', sampleSize:30, avgWeight:3.55, minWeight:2.8, maxWeight:4.5 },
      { id:4, siteId:3, penId:16, date:'2026-02-17', sampleSize:30, avgWeight:4.10, minWeight:3.2, maxWeight:5.2 },
    ],
    feedDeliveries: [
      { id:1, siteId:1, date:'2026-02-23', feedType:'Biomar 9mm',  qty:48000, supplier:'BioMar AS', invoiceRef:'BM-2026-0441', d365PO:'PO-NHA-18290' },
      { id:2, siteId:2, date:'2026-02-20', feedType:'Biomar 8mm',  qty:32000, supplier:'BioMar AS', invoiceRef:'BM-2026-0438', d365PO:'PO-NHA-18280' },
      { id:3, siteId:3, date:'2026-02-18', feedType:'Skretting 9mm',qty:40000,supplier:'Skretting AS',invoiceRef:'SK-2026-0812',d365PO:'PO-NHA-18270' },
    ],
    sensorReadings: [
      { id:1, siteId:1, penId:1,  timestamp:'2026-02-25T08:00', oxygen:11.2, temp:8.2, salinity:33.4 },
      { id:2, siteId:1, penId:4,  timestamp:'2026-02-25T08:00', oxygen:10.8, temp:8.3, salinity:33.5 },
      { id:3, siteId:2, penId:9,  timestamp:'2026-02-25T08:00', oxygen:11.5, temp:7.9, salinity:33.8 },
      { id:4, siteId:3, penId:16, timestamp:'2026-02-25T08:00', oxygen:10.9, temp:8.0, salinity:33.6 },
      { id:5, siteId:3, penId:18, timestamp:'2026-02-25T08:00', oxygen: 9.1, temp:7.8, salinity:33.7 },
    ],
  };

  api.seed = function() {
    Object.entries(SEED).forEach(([coll, rows]) => {
      if (_load(coll).length === 0) _save(coll, rows);
    });
    // Settings
    if (!localStorage.getItem(PREFIX + 'settings')) {
      localStorage.setItem(PREFIX + 'settings', JSON.stringify({
        licestd: 0.5, licevpz: 0.2, licewarn: 0.4,
        mortday: 0.15, mortweek: 0.5, mortann: 10,
        d365url: 'https://frsaetrefy27.sandbox.operations.eu.dynamics.com',
        bwurl:   'https://www.barentswatch.no/bwapi/v1',
        company: 'NHA'
      }));
    }
  };

  api.getSettings = () => JSON.parse(localStorage.getItem(PREFIX + 'settings') || '{}');
  api.saveSettings = (s) => localStorage.setItem(PREFIX + 'settings', JSON.stringify(s));

  // ── Computed helpers ────────────────────────────────────
  api.getSiteById    = (id) => api.get('sites', id);
  api.getPensForSite = (siteId) => api.query('pens', p => p.siteId === siteId);
  api.getActivePrescriptions = () => api.query('prescriptions', p => p.active);
  api.getPrescriptionsForPen = (siteId, penName) => {
    const pens = api.query('pens', p => p.siteId === siteId && p.name === penName);
    if (!pens.length) return [];
    return api.query('prescriptions', p => p.penId === pens[0].id && p.active);
  };
  api.getTotalBiomass = () => api.getAll('sites').reduce((s,x)=>s+x.biomass,0);
  api.getTotalMAB     = () => api.getAll('sites').reduce((s,x)=>s+x.mab,0);
  api.getCompanyAvgLice = () => {
    const pens = api.getAll('pens');
    return pens.length ? (pens.reduce((s,p)=>s+p.liceAF,0)/pens.length).toFixed(2) : 0;
  };
  api.getPensOverLiceLimit = (limit) => api.query('pens', p => p.liceAF >= limit).length;
  api.getRecentMortalities = (days) => {
    const cutoff = new Date(); cutoff.setDate(cutoff.getDate() - days);
    return api.query('mortalities', m => new Date(m.date) >= cutoff);
  };

  // Init
  api.seed();
  return api;
})();
