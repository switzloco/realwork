const LEDGER_URL = 'https://raw.githubusercontent.com/switzloco/realwork/main/data/la_alliance/ledger.json';
const REFRESH_MS = 60_000; // re-fetch every 60s

// ── Live ledger fetch ────────────────────────────────────────────────────────

async function fetchLedger() {
    try {
        const r = await fetch(LEDGER_URL + '?t=' + Date.now());
        if (!r.ok) return null;
        return await r.json();
    } catch { return null; }
}

function fmtDollars(n) {
    if (n >= 1_000_000) return '$' + (n / 1_000_000).toFixed(1) + 'M';
    if (n >= 1_000)     return '$' + (n / 1_000).toFixed(0) + 'K';
    return '$' + n.toFixed(0);
}

function confidenceBadge(c) {
    const colors = { high: 'rgba(80,255,180,0.8)', medium: 'rgba(255,200,80,0.8)', low: 'rgba(180,180,180,0.5)' };
    const col = colors[c] || colors.low;
    return `<span style="color:${col}; font-size:0.75rem;">${c || '—'}</span>`;
}

function renderLedger(records) {
    const real = records.filter(r => r.billed_amount && r.vendor && r.vendor !== 'DEMO - Sliced Invoices');

    // stats
    const totalDollars = real.reduce((s, r) => s + (r.billed_amount || 0), 0);
    const providers    = new Set(real.map(r => r.vendor)).size;

    animateStat('alliance-docs',      real.length,     v => v.toLocaleString());
    animateStat('alliance-dollars',   totalDollars,    fmtDollars);
    animateStat('alliance-providers', providers,       v => v.toLocaleString());

    // table — show most recent 12, sorted by date desc then amount desc
    const sorted = [...real].sort((a, b) => {
        const da = a.invoice_date || '', db = b.invoice_date || '';
        if (db !== da) return db.localeCompare(da);
        return (b.billed_amount || 0) - (a.billed_amount || 0);
    }).slice(0, 12);

    const tbody = document.getElementById('ledger-tbody');
    if (!tbody) return;

    tbody.innerHTML = sorted.map(r => `
        <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
            <td style="padding:0.55rem 0.75rem; color:rgba(255,255,255,0.85);">${r.vendor || '—'}</td>
            <td style="padding:0.55rem 0.75rem; color:rgba(255,255,255,0.5);">${r.invoice_date || '—'}</td>
            <td style="padding:0.55rem 0.75rem; text-align:right; font-family:monospace; color:rgba(80,255,180,0.85);">${r.billed_amount ? '$' + r.billed_amount.toLocaleString('en-US', {minimumFractionDigits:2}) : '—'}</td>
            <td style="padding:0.55rem 0.75rem;">${confidenceBadge(r.confidence)}</td>
        </tr>`).join('');

    const el = document.getElementById('ledger-updated');
    if (el) el.textContent = 'Updated ' + new Date().toLocaleTimeString();
}

function animateStat(id, target, fmt) {
    const el = document.getElementById(id);
    if (!el) return;
    const start = Date.now(), dur = 1200;
    const ease = t => 1 - Math.pow(2, -10 * t);
    const tick = () => {
        const p = Math.min((Date.now() - start) / dur, 1);
        el.textContent = fmt(Math.floor(ease(p) * target));
        if (p < 1) requestAnimationFrame(tick);
        else el.textContent = fmt(target);
    };
    requestAnimationFrame(tick);
}

async function refreshLedger() {
    const data = await fetchLedger();
    if (data) renderLedger(data);
}

// ── Hero counter (existing) ──────────────────────────────────────────────────

function startHeroCounter() {
    const counter = document.getElementById('counter');
    if (!counter) return;
    const target = parseInt(counter.getAttribute('data-target'), 10);
    const fmt = n => new Intl.NumberFormat('en-US').format(n);
    let startTime = null;
    const dur = 2500;
    const ease = t => t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
    const tick = ts => {
        if (!startTime) startTime = ts;
        const p = Math.min((ts - startTime) / dur, 1);
        counter.innerText = fmt(Math.floor(ease(p) * target));
        if (p < 1) requestAnimationFrame(tick);
        else counter.innerText = fmt(target);
    };
    setTimeout(() => requestAnimationFrame(tick), 500);
}

// ── Scroll reveal ────────────────────────────────────────────────────────────

function initScrollReveal() {
    const els = document.querySelectorAll('.card, .case-card, .method-step');
    els.forEach(el => el.classList.add('fade-up'));
    const obs = new IntersectionObserver((entries, o) => {
        entries.forEach((e, i) => {
            if (e.isIntersecting) {
                setTimeout(() => e.target.classList.add('visible'), i * 100);
                o.unobserve(e.target);
            }
        });
    }, { threshold: 0.1 });
    els.forEach(el => obs.observe(el));
}

// ── Smooth scroll ────────────────────────────────────────────────────────────

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            e.preventDefault();
            document.querySelector(a.getAttribute('href'))?.scrollIntoView({ behavior: 'smooth' });
        });
    });
}

// ── Tabs ─────────────────────────────────────────────────────────────────────

function initTabs() {
    const btns = document.querySelectorAll('.tab-btn');
    const contents = document.querySelectorAll('.tab-content');
    btns.forEach(btn => {
        btn.addEventListener('click', () => {
            btns.forEach(b => b.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));
            btn.classList.add('active');
            document.getElementById('tab-' + btn.getAttribute('data-target'))?.classList.add('active');
        });
    });
}

// ── Boot ─────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
    startHeroCounter();
    initScrollReveal();
    initSmoothScroll();
    initTabs();

    // live ledger: first fetch immediately, then every 60s
    refreshLedger();
    setInterval(refreshLedger, REFRESH_MS);
});
