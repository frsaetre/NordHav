/* NordHav shared JS — particles, scroll reveal, mermaid init */

// ── Particle Canvas ──────────────────────────────────────────
function initParticles() {
  const c = document.getElementById('bg-canvas');
  if (!c) return;
  const ctx = c.getContext('2d');
  let W, H, pts = [];
  function resize() { W = c.width = window.innerWidth; H = c.height = window.innerHeight; }
  resize(); window.addEventListener('resize', resize);
  class P {
    constructor() { this.init(); }
    init() { this.x=Math.random()*W; this.y=Math.random()*H; this.r=Math.random()*1.6+0.3; this.vx=(Math.random()-.5)*0.28; this.vy=(Math.random()-.5)*0.28; this.a=Math.random()*0.45+0.08; this.h=190+Math.random()*30; }
    step() { this.x+=this.vx; this.y+=this.vy; if(this.x<0||this.x>W||this.y<0||this.y>H) this.init(); }
    draw() { ctx.beginPath(); ctx.arc(this.x,this.y,this.r,0,Math.PI*2); ctx.fillStyle=`hsla(${this.h},75%,65%,${this.a})`; ctx.fill(); }
  }
  for(let i=0;i<160;i++) pts.push(new P());
  function loop() {
    ctx.clearRect(0,0,W,H);
    pts.forEach(p=>p.step());
    for(let i=0;i<pts.length;i++) for(let j=i+1;j<pts.length;j++){
      const dx=pts[i].x-pts[j].x, dy=pts[i].y-pts[j].y, d=Math.hypot(dx,dy);
      if(d<90){ ctx.beginPath(); ctx.moveTo(pts[i].x,pts[i].y); ctx.lineTo(pts[j].x,pts[j].y); ctx.strokeStyle=`rgba(0,180,216,${0.055*(1-d/90)})`; ctx.lineWidth=0.5; ctx.stroke(); }
    }
    pts.forEach(p=>p.draw());
    requestAnimationFrame(loop);
  }
  loop();
}

// ── Scroll Reveal ────────────────────────────────────────────
function initReveal() {
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('vis'); io.unobserve(e.target); } });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal,.reveal-l,.reveal-r,.stagger,.tl-item').forEach(el=>io.observe(el));
}

// ── Nav shrink on scroll + mobile hamburger ─────────────────
function initNav() {
  const nav = document.querySelector('nav');
  if(!nav) return;
  const links = nav.querySelector('.nav-links');

  // Shrink on scroll (desktop only)
  window.addEventListener('scroll', ()=>{
    if(window.innerWidth > 768){
      nav.style.height = window.scrollY>60 ? '52px' : '64px';
    }
  });

  // Inject hamburger button if missing
  if(links && !nav.querySelector('.nav-toggle')){
    const btn = document.createElement('button');
    btn.className = 'nav-toggle';
    btn.setAttribute('aria-label','Toggle navigation');
    btn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
    nav.insertBefore(btn, links);

    btn.addEventListener('click', ()=>{
      links.classList.toggle('open');
      nav.classList.toggle('nav-open');
      // Toggle icon between hamburger and X
      const isOpen = links.classList.contains('open');
      btn.innerHTML = isOpen
        ? '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="6" y1="18" x2="18" y2="6"/></svg>'
        : '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
    });

    // Close menu when a link is clicked
    links.querySelectorAll('.nav-link').forEach(a=>{
      a.addEventListener('click', ()=>{
        links.classList.remove('open');
        nav.classList.remove('nav-open');
        btn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
      });
    });
  }

  // Reset nav on resize
  window.addEventListener('resize', ()=>{
    if(window.innerWidth > 768 && links){
      links.classList.remove('open');
      nav.classList.remove('nav-open');
      nav.style.height = '';
    }
  });
}

// ── Mermaid init ────────────────────────────────────────────
function initMermaid() {
  if(typeof mermaid==='undefined') return;
  mermaid.initialize({
    theme:'dark',
    themeVariables:{
      primaryColor:'#00b4d8', primaryTextColor:'#d4eaf5', primaryBorderColor:'#1e3a5f',
      lineColor:'#00b4d8', secondaryColor:'#0a1a2e', tertiaryColor:'#071221',
      background:'#040d1a', mainBkg:'#0a1a2e', nodeBorder:'#00b4d8',
      clusterBkg:'#071221', titleColor:'#d4eaf5', edgeLabelBackground:'#0a1a2e',
      fontFamily:'Inter,sans-serif', fontSize:'13px'
    }, startOnLoad:true
  });
}

// ── Hero wave animation ─────────────────────────────────────
function initHeroWave() {
  const paths = document.querySelectorAll('.hero-wave-path');
  let t = 0;
  function wave() {
    t += 0.008;
    paths.forEach((p, i) => {
      const amp = 28 + i * 12;
      const freq = 0.003 - i * 0.0005;
      const phase = i * 1.2;
      const d = `M0,${80+amp*Math.sin(t+phase)} C300,${80+amp*Math.sin(t+phase+1)} 600,${80-amp*Math.sin(t+phase+2)} 900,${80+amp*Math.sin(t+phase+1)} C1200,${80-amp*Math.sin(t+phase)} 1440,${80+amp*Math.sin(t+phase+1)} 1440,140 L1440,200 L0,200Z`;
      p.setAttribute('d', d);
    });
    requestAnimationFrame(wave);
  }
  wave();
}

// ── AI Disclaimer Pill (top banner) ─────────────────────────
function initAIDisclaimer() {
  // Top pill
  const pill = document.createElement('div');
  pill.className = 'ai-disclaimer-pill';
  pill.innerHTML = `<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M7 0L8.5 5.5L14 7L8.5 8.5L7 14L5.5 8.5L0 7L5.5 5.5Z" fill="#fca311"/></svg> This is a completely AI-generated example and may contain errors <button class="dismiss-btn" title="Dismiss">&times;</button>`;
  document.body.appendChild(pill);
  pill.querySelector('.dismiss-btn').addEventListener('click', () => {
    pill.style.opacity = '0';
    setTimeout(() => pill.remove(), 300);
  });

  // Footer notice
  const footer = document.querySelector('footer');
  if (footer) {
    const notice = document.createElement('div');
    notice.className = 'ai-footer-notice';
    notice.innerHTML = `<strong>AI-Generated Scenario</strong> — All data, companies, and business scenarios presented here are entirely fictitious and were generated completely by AI. This project demonstrates how AI can be used to build, respond to, and deploy complex business application requirements end to end.`;
    footer.appendChild(notice);
  }
}

// ── Run everything ───────────────────────────────────────────
document.addEventListener('DOMContentLoaded', ()=>{
  initParticles();
  initReveal();
  initNav();
  initMermaid();
  initHeroWave();
  initAIDisclaimer();
});

// ── Shared logo SVG string ───────────────────────────────────
window.NORDHAV_LOGO = `<svg class="nha-logo" viewBox="0 0 1000 800" xmlns="http://www.w3.org/2000/svg">
<g class="logo-fill">
<circle cx="245" cy="115" r="10"/><circle cx="290.4" cy="120.4" r="9.28"/><circle cx="339.2" cy="125.8" r="8.72"/><circle cx="391" cy="131.2" r="8.32"/><circle cx="445.4" cy="136.6" r="8.08"/><circle cx="500" cy="142" r="8"/><circle cx="554.6" cy="136.6" r="8.08"/><circle cx="609" cy="131.2" r="8.32"/><circle cx="660.8" cy="125.8" r="8.72"/><circle cx="709.6" cy="120.4" r="9.28"/><circle cx="755" cy="115" r="10"/>
<circle cx="500" cy="310" r="6"/><circle cx="345" cy="310" r="8"/><circle cx="655" cy="310" r="8"/>
<path d="M 165 650 V 550 H 183 L 217 610 V 550 H 235 V 650 H 217 L 183 590 V 650 Z"/>
<path d="M 295 550 C 317 550 335 572 335 600 C 335 628 317 650 295 650 C 273 650 255 628 255 600 C 255 572 273 550 295 550 Z M 295 568 C 307 568 317 582 317 600 C 317 618 307 632 295 632 C 283 632 273 618 273 600 C 273 582 283 568 295 568 Z"/>
<path d="M 450 650 V 550 H 495 C 525 550 530 575 530 600 C 530 625 525 650 495 650 Z M 468 632 H 495 C 510 632 512 615 512 600 C 512 585 510 568 495 568 H 468 Z"/>
<path d="M 550 650 V 550 H 568 V 591 H 602 V 550 H 620 V 650 H 602 V 609 H 568 V 650 Z"/>
<path d="M 675 550 L 640 650 H 660 L 670 620 H 700 L 710 650 H 730 L 695 550 Z M 685 575 L 675 605 H 695 Z"/>
<path d="M 750 550 H 770 L 800 630 L 830 550 H 850 L 810 650 H 790 Z"/>
</g>
</svg>`;
