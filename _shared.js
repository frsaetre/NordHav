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

// ── Narrated Tour Engine ─────────────────────────────────────
function initNarration() {
  if (!window.tourSections || !window.tourSections.length) return;

  const synth = window.speechSynthesis;
  const voiceConfig = {
    engine:'system', systemVoiceName:'',
    azureKey:'', azureRegion:'eastus', azureVoice:'en-US-AriaNeural',
    azureStyle:'narration-professional', rate:1.05, pitch:1.0, volume:1.0
  };
  let tourActive = false, currentSectionIdx = 0, currentAudio = null, keepAliveInterval = null;

  // ── Inject HTML elements ──
  const progressBar = document.createElement('div');
  progressBar.className = 'tour-progress-bar'; progressBar.id = 'tourProgressBar';
  progressBar.innerHTML = '<div class="tour-progress-fill" id="tourProgressFill"></div>';
  document.body.appendChild(progressBar);

  const dotsContainer = document.createElement('div');
  dotsContainer.className = 'tour-section-indicator'; dotsContainer.id = 'tourDots';
  document.body.appendChild(dotsContainer);

  const caption = document.createElement('div');
  caption.className = 'narration-caption'; caption.id = 'narrationCaption';
  caption.innerHTML = '<div class="narration-section-label" id="narrationLabel">Section</div><div class="narration-text" id="narrationText"></div>';
  document.body.appendChild(caption);

  // Tour button in hero
  const hero = document.querySelector('.hero, .hero-hub');
  if (hero) {
    const tourBtn = document.createElement('button');
    tourBtn.className = 'tour-btn'; tourBtn.id = 'tourBtn';
    tourBtn.textContent = '\u25B6 Start Guided Tour';
    tourBtn.addEventListener('click', toggleTour);
    const scrollHint = hero.querySelector('.scroll-hint');
    if (scrollHint) hero.insertBefore(tourBtn, scrollHint); else hero.appendChild(tourBtn);
  }

  // Voice settings button in nav
  const nav = document.querySelector('nav');
  if (nav) {
    const voiceBtn = document.createElement('button');
    voiceBtn.className = 'voice-settings-btn';
    voiceBtn.innerHTML = '\uD83C\uDFA4 Voice';
    voiceBtn.addEventListener('click', openVoicePanel);
    nav.appendChild(voiceBtn);
  }

  // Voice panel overlay
  const overlay = document.createElement('div');
  overlay.className = 'voice-panel-overlay'; overlay.id = 'voicePanelOverlay';
  overlay.addEventListener('click', e => { if (e.target === overlay) closeVoicePanel(); });
  overlay.innerHTML = `<div class="voice-panel">
    <div class="vp-header"><span class="vp-title">\uD83C\uDFA4 Voice Settings <span class="vp-engine-badge system" id="vp-engine-badge">System TTS</span></span><button class="vp-close" id="vpClose">\u2715</button></div>
    <div class="vp-tabs"><button class="vp-tab active" data-tab="system">System Voices</button><button class="vp-tab" data-tab="azure">Azure Neural TTS</button><button class="vp-tab" data-tab="settings">Speed &amp; Pitch</button></div>
    <div class="vp-section active" id="vp-section-system"><div class="vp-label">Available English Voices</div><div class="vp-info">Voices installed on your device. Quality varies \u2014 Microsoft Neural voices (Online) are highest quality.</div><div class="vp-voice-grid" id="vpVoiceGrid">Loading voices\u2026</div><button class="vp-test-btn" id="vpTestSystem">\u25B6 Preview Selected Voice</button><div class="vp-status" id="vpSysStatus"></div></div>
    <div class="vp-section" id="vp-section-azure"><div class="vp-info">\uD83D\uDE80 <strong>Azure Neural TTS</strong> delivers studio-quality AI voices.<br>Get a free key at <a href="https://azure.microsoft.com/products/ai-services/text-to-speech" target="_blank" rel="noopener">Azure Speech</a> (free tier: 500K chars/month).</div><div class="vp-label">API Key</div><input class="vp-input" type="password" id="vpAzureKey" placeholder="Paste your Azure Speech key\u2026"><div class="vp-label">Region</div><input class="vp-input" type="text" id="vpAzureRegion" placeholder="e.g. eastus, westeurope\u2026" value="eastus"><div class="vp-label">Select Voice</div><div class="vp-azure-voice-grid" id="vpAzureVoiceGrid"><div class="vp-az-card selected" data-voice="en-US-AriaNeural"><div class="vp-az-name">Aria \u2640</div><div class="vp-az-style">en-US \u00B7 Natural, narration</div></div><div class="vp-az-card" data-voice="en-US-GuyNeural"><div class="vp-az-name">Guy \u2642</div><div class="vp-az-style">en-US \u00B7 News, authoritative</div></div><div class="vp-az-card" data-voice="en-US-AndrewNeural"><div class="vp-az-name">Andrew \u2642</div><div class="vp-az-style">en-US \u00B7 Warm, conversational</div></div><div class="vp-az-card" data-voice="en-US-JennyNeural"><div class="vp-az-name">Jenny \u2640</div><div class="vp-az-style">en-US \u00B7 Friendly, assistant</div></div><div class="vp-az-card" data-voice="en-US-BrandonNeural"><div class="vp-az-name">Brandon \u2642</div><div class="vp-az-style">en-US \u00B7 Clear, professional</div></div><div class="vp-az-card" data-voice="en-US-EricNeural"><div class="vp-az-name">Eric \u2642</div><div class="vp-az-style">en-US \u00B7 Deep, corporate</div></div><div class="vp-az-card" data-voice="en-US-MichelleNeural"><div class="vp-az-name">Michelle \u2640</div><div class="vp-az-style">en-US \u00B7 Calm, expressive</div></div><div class="vp-az-card" data-voice="en-GB-RyanNeural"><div class="vp-az-name">Ryan \u2642 \uD83C\uDDEC\uD83C\uDDE7</div><div class="vp-az-style">en-GB \u00B7 British, premium</div></div></div><div class="vp-label">Speaking Style</div><select class="vp-select" id="vpAzureStyle"><option value="narration-professional" selected>Narration Professional</option><option value="newscast">Newscast</option><option value="customerservice">Customer Service</option><option value="chat">Conversational</option><option value="enthusiastic">Enthusiastic</option><option value="empathetic">Empathetic</option></select><button class="vp-test-btn" id="vpTestAzure">\u25B6 Test Azure Voice</button><div class="vp-status" id="vpAzureStatus"></div></div>
    <div class="vp-section" id="vp-section-settings"><div class="vp-label">Playback Speed</div><div class="vp-slider-row"><span class="vp-slider-label">Speed</span><input class="vp-slider" type="range" min="0.6" max="1.8" step="0.05" value="1.05" id="vpRate"><span class="vp-slider-val" id="vpRateVal">1.05\u00D7</span></div><div class="vp-label">Pitch (System TTS Only)</div><div class="vp-slider-row"><span class="vp-slider-label">Pitch</span><input class="vp-slider" type="range" min="0.5" max="2" step="0.05" value="1" id="vpPitch"><span class="vp-slider-val" id="vpPitchVal">1\u00D7</span></div><div class="vp-label">Volume</div><div class="vp-slider-row"><span class="vp-slider-label">Volume</span><input class="vp-slider" type="range" min="0" max="1" step="0.05" value="1" id="vpVolume"><span class="vp-slider-val" id="vpVolumeVal">100%</span></div></div>
    <div class="vp-actions"><button class="vp-btn vp-btn-primary" id="vpApply">\u2713 Apply Settings</button><button class="vp-btn vp-btn-secondary" id="vpCancel">Cancel</button></div>
  </div>`;
  document.body.appendChild(overlay);

  // Wire up panel events
  overlay.querySelector('#vpClose').addEventListener('click', closeVoicePanel);
  overlay.querySelector('#vpCancel').addEventListener('click', closeVoicePanel);
  overlay.querySelector('#vpApply').addEventListener('click', applyVoiceSettings);
  overlay.querySelector('#vpTestSystem').addEventListener('click', testCurrentVoice);
  overlay.querySelector('#vpTestAzure').addEventListener('click', testAzureVoice);
  overlay.querySelector('#vpAzureKey').addEventListener('input', e => { voiceConfig.azureKey = e.target.value; });
  overlay.querySelector('#vpAzureRegion').addEventListener('input', e => { voiceConfig.azureRegion = e.target.value; });
  overlay.querySelector('#vpAzureStyle').addEventListener('change', e => { voiceConfig.azureStyle = e.target.value; });
  overlay.querySelector('#vpRate').addEventListener('input', e => { voiceConfig.rate = parseFloat(e.target.value); document.getElementById('vpRateVal').textContent = e.target.value + '\u00D7'; });
  overlay.querySelector('#vpPitch').addEventListener('input', e => { voiceConfig.pitch = parseFloat(e.target.value); document.getElementById('vpPitchVal').textContent = e.target.value + '\u00D7'; });
  overlay.querySelector('#vpVolume').addEventListener('input', e => { voiceConfig.volume = parseFloat(e.target.value); document.getElementById('vpVolumeVal').textContent = Math.round(e.target.value * 100) + '%'; });
  overlay.querySelectorAll('.vp-tab').forEach(tab => tab.addEventListener('click', function() {
    overlay.querySelectorAll('.vp-tab').forEach(t => t.classList.remove('active'));
    overlay.querySelectorAll('.vp-section').forEach(s => s.classList.remove('active'));
    this.classList.add('active');
    document.getElementById('vp-section-' + this.dataset.tab).classList.add('active');
  }));
  overlay.querySelectorAll('.vp-az-card').forEach(card => card.addEventListener('click', function() {
    overlay.querySelectorAll('.vp-az-card').forEach(c => c.classList.remove('selected'));
    this.classList.add('selected');
    voiceConfig.azureVoice = this.dataset.voice;
  }));

  // ── Build side dots ──
  function buildDots() {
    dotsContainer.innerHTML = '';
    window.tourSections.forEach((s, i) => {
      const dot = document.createElement('div');
      dot.className = 'tour-dot';
      dot.innerHTML = '<span class="dot-tip">' + s.label + '</span>';
      dot.addEventListener('click', () => { if (tourActive) jumpToSection(i); });
      dotsContainer.appendChild(dot);
    });
  }
  function updateDots(idx) {
    dotsContainer.querySelectorAll('.tour-dot').forEach((d, i) => {
      d.classList.toggle('done', i < idx);
      d.classList.toggle('current', i === idx);
    });
  }
  function updateProgress(idx) {
    document.getElementById('tourProgressFill').style.width = ((idx + 1) / window.tourSections.length * 100) + '%';
  }

  // ── Tour lifecycle ──
  function toggleTour() { if (tourActive) stopTour(); else startTour(); }
  function startTour() {
    tourActive = true; currentSectionIdx = 0;
    document.getElementById('tourBtn').textContent = '\u25FC Stop Tour';
    document.getElementById('tourBtn').classList.add('touring');
    progressBar.classList.add('active');
    dotsContainer.classList.add('active');
    caption.classList.add('visible');
    narrateNext();
  }
  function stopTour() {
    tourActive = false; synth.cancel(); stopKeepAlive(); stopCaptionScroll();
    if (currentAudio) { currentAudio.pause(); currentAudio = null; }
    document.getElementById('tourBtn').textContent = '\u25B6 Start Guided Tour';
    document.getElementById('tourBtn').classList.remove('touring');
    progressBar.classList.remove('active');
    dotsContainer.classList.remove('active');
    caption.classList.remove('visible');
    dotsContainer.querySelectorAll('.tour-dot').forEach(d => d.classList.remove('current', 'done'));
  }
  function jumpToSection(idx) {
    synth.cancel(); stopKeepAlive(); stopCaptionScroll();
    if (currentAudio) { currentAudio.pause(); currentAudio = null; }
    currentSectionIdx = idx; narrateSection(idx);
  }
  function narrateNext() {
    if (!tourActive) return;
    if (currentSectionIdx >= window.tourSections.length) { stopTour(); return; }
    narrateSection(currentSectionIdx);
  }
  // ── Word-scroll caption state ──
  let captionWords = []; let captionWordIdx = 0; let captionTimer = null;
  function stopCaptionScroll() { if (captionTimer) { clearInterval(captionTimer); captionTimer = null; } }
  function buildCaptionWords(text) {
    const box = document.getElementById('narrationText');
    const words = text.split(/\s+/);
    box.innerHTML = words.map((w, i) => '<span class="nw" data-i="' + i + '">' + w + ' </span>').join('');
    captionWords = box.querySelectorAll('.nw');
    captionWordIdx = 0;
  }
  function startCaptionScroll(text) {
    stopCaptionScroll();
    // Estimate words-per-second from speech rate (default rate 1 ≈ ~2.7 words/sec)
    const wps = 2.7 * (voiceConfig.rate || 1);
    const totalWords = captionWords.length;
    if (totalWords === 0) return;
    const msPerWord = 1000 / wps;
    captionTimer = setInterval(() => {
      if (captionWordIdx >= totalWords) { stopCaptionScroll(); return; }
      const span = captionWords[captionWordIdx];
      if (captionWordIdx > 0) { captionWords[captionWordIdx - 1].classList.remove('current'); captionWords[captionWordIdx - 1].classList.add('spoken'); }
      span.classList.add('current');
      // Auto-scroll to keep current word visible
      const box = document.getElementById('narrationText');
      const spanTop = span.offsetTop - box.offsetTop;
      const boxH = box.clientHeight;
      if (spanTop > box.scrollTop + boxH - 24) {
        box.scrollTo({ top: spanTop - 12, behavior: 'smooth' });
      }
      captionWordIdx++;
    }, msPerWord);
  }

  function narrateSection(idx) {
    const s = window.tourSections[idx];
    updateDots(idx); updateProgress(idx);
    document.getElementById('narrationLabel').textContent = s.label;
    buildCaptionWords(s.text);
    const el = document.getElementById(s.id);
    if (el) {
      const offset = el.getBoundingClientRect().top + window.pageYOffset - 80;
      window.scrollTo({ top: offset, behavior: 'smooth' });
    }
    if (voiceConfig.engine === 'azure' && voiceConfig.azureKey) speakAzure(s.text);
    else speakSystem(s.text);
    startCaptionScroll(s.text);
  }

  // ── Chrome keep-alive for long utterances ──
  function startKeepAlive() { keepAliveInterval = setInterval(() => { if (synth.speaking) { synth.pause(); synth.resume(); } }, 10000); }
  function stopKeepAlive() { if (keepAliveInterval) { clearInterval(keepAliveInterval); keepAliveInterval = null; } }

  // ── System TTS ──
  function speakSystem(text) {
    synth.cancel(); stopKeepAlive();
    const utter = new SpeechSynthesisUtterance(text);
    utter.rate = voiceConfig.rate; utter.pitch = voiceConfig.pitch; utter.volume = voiceConfig.volume;
    const v = voiceConfig.systemVoiceName ? synth.getVoices().find(x => x.name === voiceConfig.systemVoiceName) : pickBestVoice();
    if (v) utter.voice = v;
    utter.onend = () => { stopKeepAlive(); if (tourActive) { currentSectionIdx++; narrateNext(); } };
    utter.onerror = () => { stopKeepAlive(); };
    synth.speak(utter); startKeepAlive();
  }

  // ── Azure Neural TTS ──
  async function speakAzure(text) {
    try {
      const audio = await synthesizeAzure(text, voiceConfig.azureKey, voiceConfig.azureRegion, voiceConfig.azureVoice, voiceConfig.azureStyle);
      if (!tourActive) return;
      currentAudio = audio; audio.playbackRate = voiceConfig.rate; audio.volume = voiceConfig.volume;
      audio.onended = () => { if (tourActive) { currentSectionIdx++; narrateNext(); } };
      audio.play();
    } catch(e) { console.warn('Azure TTS error, falling back to system:', e); speakSystem(text); }
  }
  async function synthesizeAzure(text, key, region, voice, style) {
    const ssml = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='en-US'><voice name='" + voice + "'><mstts:express-as style='" + style + "'><prosody rate='" + voiceConfig.rate + "' volume='" + Math.round(voiceConfig.volume * 100) + "%'>" + text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;') + "</prosody></mstts:express-as></voice></speak>";
    const res = await fetch('https://' + region + '.tts.speech.microsoft.com/cognitiveservices/v1', {
      method:'POST',
      headers:{'Ocp-Apim-Subscription-Key':key,'Content-Type':'application/ssml+xml','X-Microsoft-OutputFormat':'audio-16khz-128kbitrate-mono-mp3'},
      body:ssml
    });
    if (!res.ok) throw new Error('Azure TTS ' + res.status + ': ' + (await res.text()));
    return new Audio(URL.createObjectURL(await res.blob()));
  }

  // ── Voice panel functions ──
  function openVoicePanel() { overlay.classList.add('open'); populateSystemVoices(); }
  function closeVoicePanel() { overlay.classList.remove('open'); }

  const VOICE_RANK = ['Microsoft Andrew Online (Natural)','Microsoft Aria Online (Natural)','Microsoft Guy Online (Natural)','Microsoft Jenny Online (Natural)','Microsoft Ryan Online (Natural)','Microsoft Ava Online (Natural)','Microsoft Andrew','Microsoft Aria','Microsoft Guy Online','Microsoft AriaNeural','Google US English','Microsoft Mark','Microsoft David','Microsoft DavidDesktop','Microsoft Zira'];
  function getVoiceScore(v) { for (let i = 0; i < VOICE_RANK.length; i++) { if (v.name.includes(VOICE_RANK[i])) return VOICE_RANK.length - i; } return 0; }
  function pickBestVoice() {
    const voices = synth.getVoices().filter(v => v.lang.startsWith('en'));
    if (!voices.length) return null;
    let best = null, bestScore = -1;
    voices.forEach(v => { const s = getVoiceScore(v); if (s > bestScore) { bestScore = s; best = v; } });
    return best || voices[0];
  }
  function populateSystemVoices() {
    const grid = document.getElementById('vpVoiceGrid');
    let voices = synth.getVoices().filter(v => v.lang.startsWith('en'));
    voices.sort((a, b) => getVoiceScore(b) - getVoiceScore(a) || a.name.localeCompare(b.name));
    if (!voices.length) { grid.textContent = 'No English voices found.'; return; }
    grid.innerHTML = voices.map(v => '<div class="vp-voice-card' + (v.name === voiceConfig.systemVoiceName ? ' selected' : '') + '" data-vname="' + v.name.replace(/"/g, '') + '"><div class="vp-voice-name">' + v.name + '</div><div class="vp-voice-lang">' + v.lang + '</div><span class="vp-voice-local">' + (v.localService ? 'Local' : 'Online') + '</span></div>').join('');
    grid.querySelectorAll('.vp-voice-card').forEach(card => card.addEventListener('click', function() {
      grid.querySelectorAll('.vp-voice-card').forEach(c => c.classList.remove('selected'));
      this.classList.add('selected');
      voiceConfig.systemVoiceName = this.dataset.vname;
      voiceConfig.engine = 'system';
    }));
  }
  function applyVoiceSettings() {
    voiceConfig.azureKey = document.getElementById('vpAzureKey').value.trim();
    voiceConfig.azureRegion = document.getElementById('vpAzureRegion').value.trim() || 'eastus';
    voiceConfig.azureStyle = document.getElementById('vpAzureStyle').value;
    if (voiceConfig.azureKey) {
      voiceConfig.engine = 'azure';
      document.getElementById('vp-engine-badge').textContent = 'Azure Neural';
      document.getElementById('vp-engine-badge').className = 'vp-engine-badge azure';
    } else {
      voiceConfig.engine = 'system';
      document.getElementById('vp-engine-badge').textContent = 'System TTS';
      document.getElementById('vp-engine-badge').className = 'vp-engine-badge system';
    }
    closeVoicePanel();
  }
  function testCurrentVoice() {
    synth.cancel();
    const utter = new SpeechSynthesisUtterance('Hello! This is how I will narrate the NordHav guided tour.');
    utter.rate = voiceConfig.rate; utter.pitch = voiceConfig.pitch; utter.volume = voiceConfig.volume;
    const v = voiceConfig.systemVoiceName ? synth.getVoices().find(x => x.name === voiceConfig.systemVoiceName) : pickBestVoice();
    if (v) utter.voice = v;
    const status = document.getElementById('vpSysStatus');
    status.textContent = '\u25B6 Playing: ' + (v ? v.name : 'default'); status.className = 'vp-status';
    utter.onend = () => { status.textContent = '\u2713 Done'; status.className = 'vp-status ok'; };
    synth.speak(utter);
  }
  async function testAzureVoice() {
    const key = document.getElementById('vpAzureKey').value.trim();
    const region = document.getElementById('vpAzureRegion').value.trim() || 'eastus';
    const status = document.getElementById('vpAzureStatus');
    if (!key) { status.textContent = '\u26A0 Enter API key first.'; status.className = 'vp-status err'; return; }
    status.textContent = '\u23F3 Connecting to Azure\u2026'; status.className = 'vp-status';
    try {
      const audio = await synthesizeAzure('Hello! This is how Azure Neural text to speech will narrate the NordHav tour.', key, region, voiceConfig.azureVoice, voiceConfig.azureStyle);
      audio.playbackRate = voiceConfig.rate; audio.play();
      status.textContent = '\u2713 Azure TTS working!'; status.className = 'vp-status ok';
    } catch(e) { status.textContent = '\u2717 Error: ' + e.message; status.className = 'vp-status err'; }
  }

  // ── Auto-select best voice ──
  buildDots();
  function autoPickBestVoice() {
    if (!voiceConfig.systemVoiceName) {
      const best = pickBestVoice();
      if (best) { voiceConfig.systemVoiceName = best.name; console.log('Auto-selected voice:', best.name); }
    }
  }
  if (synth.onvoiceschanged !== undefined) synth.onvoiceschanged = autoPickBestVoice;
  synth.getVoices(); setTimeout(autoPickBestVoice, 100);
}

// ── Run everything ───────────────────────────────────────────
document.addEventListener('DOMContentLoaded', ()=>{
  initParticles();
  initReveal();
  initNav();
  initMermaid();
  initHeroWave();
  initAIDisclaimer();
  initNarration();
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
