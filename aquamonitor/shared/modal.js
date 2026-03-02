/* ═══════════════════════════════════════════════════════════
   AquaMonitor UI Service — modals, toasts, confirm dialogs
   ═══════════════════════════════════════════════════════════ */

// ── Generic Form Modal ──────────────────────────────────────
function openFormModal({ title, headerClass='teal', size='', bodyHtml, onSave, saveLabel='💾 Save', saveBtnClass='btn-primary' }) {
  const overlay = document.getElementById('modal-overlay');
  const inner   = document.getElementById('modal-inner');
  inner.className = `modal${size?' modal-'+size:''}`;
  inner.innerHTML = `
    <div class="modal-header ${headerClass}">
      <span>${title}</span>
      <button class="modal-close" onclick="closeModal()">✕</button>
    </div>
    <div class="modal-body" id="modal-body-content">${bodyHtml}</div>
    <div class="modal-footer">
      <button class="btn btn-secondary" onclick="closeModal()">Cancel</button>
      <button class="btn ${saveBtnClass}" id="modal-save-btn">${saveLabel}</button>
    </div>`;
  overlay.classList.add('open');
  document.getElementById('modal-save-btn').onclick = () => {
    if (onSave()) { closeModal(); }
  };
}

function openInfoModal({ title, headerClass='teal', size='', bodyHtml }) {
  const overlay = document.getElementById('modal-overlay');
  const inner   = document.getElementById('modal-inner');
  inner.className = `modal${size?' modal-'+size:''}`;
  inner.innerHTML = `
    <div class="modal-header ${headerClass}">
      <span>${title}</span>
      <button class="modal-close" onclick="closeModal()">✕</button>
    </div>
    <div class="modal-body">${bodyHtml}</div>
    <div class="modal-footer">
      <button class="btn btn-secondary" onclick="closeModal()">Close</button>
    </div>`;
  overlay.classList.add('open');
}

function openConfirm({ title='Confirm', message, onConfirm, confirmLabel='Confirm', confirmClass='btn-danger' }) {
  const overlay = document.getElementById('modal-overlay');
  const inner   = document.getElementById('modal-inner');
  inner.className = 'modal modal-sm';
  inner.innerHTML = `
    <div class="modal-header danger">
      <span>${title}</span>
      <button class="modal-close" onclick="closeModal()">✕</button>
    </div>
    <div class="modal-body"><p>${message}</p></div>
    <div class="modal-footer">
      <button class="btn btn-secondary" onclick="closeModal()">Cancel</button>
      <button class="btn ${confirmClass}" id="modal-confirm-btn">${confirmLabel}</button>
    </div>`;
  overlay.classList.add('open');
  document.getElementById('modal-confirm-btn').onclick = () => { closeModal(); onConfirm(); };
}

function closeModal() {
  document.getElementById('modal-overlay').classList.remove('open');
}

// Close on backdrop click
document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.getElementById('modal-overlay');
  if (overlay) overlay.addEventListener('click', e => { if (e.target === overlay) closeModal(); });
});

// ── Toast Notifications ─────────────────────────────────────
function showToast(message, type='success', duration=3500) {
  const container = document.getElementById('toast-container');
  if (!container) return;
  const icons = { success:'✅', warning:'⚠️', error:'❌', info:'ℹ️' };
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span>${icons[type]||'ℹ️'}</span><span>${message}</span>`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.animation = 'fadeOut .3s forwards';
    setTimeout(() => toast.remove(), 300);
  }, duration);
}

// ── Field helpers ───────────────────────────────────────────
function fval(id) {
  const el = document.getElementById(id);
  return el ? el.value.trim() : '';
}
function fnum(id) {
  const v = parseFloat(fval(id));
  return isNaN(v) ? 0 : v;
}
function fint(id) {
  const v = parseInt(fval(id));
  return isNaN(v) ? 0 : v;
}
function fbool(id) {
  const el = document.getElementById(id);
  return el ? el.checked : false;
}

// ── Table builder helper ────────────────────────────────────
function buildTable(cols, rows, options={}) {
  if (!rows || rows.length === 0) {
    return `<div class="empty-state"><div class="empty-icon">${options.emptyIcon||'📋'}</div><p>${options.emptyText||'No records found.'}</p>${options.emptyAction||''}</div>`;
  }
  const thead = `<thead><tr>${cols.map(c=>`<th>${c.label}</th>`).join('')}${options.actions?'<th>Actions</th>':''}</tr></thead>`;
  const tbody = `<tbody>${rows.map(row => {
    const cls = options.rowClass ? options.rowClass(row) : '';
    const cells = cols.map(c => `<td>${c.render ? c.render(row) : (row[c.key]??'—')}</td>`).join('');
    const acts  = options.actions ? `<td>${options.actions(row)}</td>` : '';
    return `<tr class="${cls}">${cells}${acts}</tr>`;
  }).join('')}</tbody>`;
  return `<table class="data-table">${thead}${tbody}</table>`;
}

// ── Badge helpers ───────────────────────────────────────────
function badgeStatus(status) {
  const map = {
    'Approved':'green','Active':'green','Confirmed':'green','Cleared':'green','Filed':'green','Pass':'green',
    'On Hold':'amber','Tentative':'amber','Planned':'amber','Moderate':'amber','Near limit':'amber','In Progress':'amber',
    'Draft':'grey','Expired':'grey','Unavailable':'grey',
    'Blocked':'red','EXCEEDED':'red','Critical':'red','High':'red','Active (withdrawal)':'red',
  };
  const c = map[status] || 'grey';
  return `<span class="badge-pill badge-${c}">${status}</span>`;
}

function liceStatusBadge(af) {
  if (af >= 0.5) return `<span class="badge-pill badge-red">🚨 ${af} — EXCEEDED</span>`;
  if (af >= 0.4) return `<span class="badge-pill badge-amber">⚠ ${af} — Near limit</span>`;
  return `<span class="badge-pill badge-green">✓ ${af} — OK</span>`;
}

function penCellClass(af) {
  if (af >= 0.5) return 'lice-high';
  if (af >= 0.4) return 'lice-medium';
  return 'lice-ok';
}

function siteDot(liceStatus) {
  if (liceStatus === 'red')   return '<span class="dot dot-red"></span>';
  if (liceStatus === 'amber') return '<span class="dot dot-amber"></span>';
  return '<span class="dot dot-green"></span>';
}

function formatDate(d) {
  if (!d) return '—';
  try { return new Date(d).toLocaleDateString('en-GB',{day:'2-digit',month:'short',year:'numeric'}); }
  catch { return d; }
}
function today() { return new Date().toISOString().split('T')[0]; }
