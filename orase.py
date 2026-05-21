from flask import Flask
from app.lib.biblioteca_orase import populatie_barcelona, descriere_barcelona

app = Flask(__name__)

_ARR = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
_BCK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="m12 5-7 7 7 7"/></svg>'
_PIN = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 13-8 13S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
_DWN = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="m5 12 7 7 7-7"/></svg>'
_GLB = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'

STYLE = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

  :root {
    --bg:      #070d1a;
    --surf:    rgba(255,255,255,0.04);
    --surf-hv: rgba(255,255,255,0.07);
    --bd:      rgba(255,255,255,0.08);
    --bd-hv:   rgba(56,189,248,0.45);
    --pri:     #38bdf8;
    --pri-d:   #0ea5e9;
    --acc:     #f97316;
    --acc-d:   #ea580c;
    --gold:    #fbbf24;
    --text:    #eef4ff;
    --muted:   rgba(238,244,255,0.52);
    --dim:     rgba(238,244,255,0.28);
    --glow-b:  rgba(56,189,248,0.2);
    --glow-o:  rgba(249,115,22,0.38);
    --spring:  cubic-bezier(0.16, 1, 0.3, 1);
    --ease-o:  cubic-bezier(0, 0, 0.2, 1);
    --t-fast:  150ms;
    --t-mid:   280ms;
    --t-enter: 600ms;
  }

  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100dvh;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
  }

  nav {
    position: fixed;
    inset: 0 0 auto 0;
    z-index: 200;
    height: 58px;
    display: flex;
    align-items: center;
    gap: 1.75rem;
    padding: 0 2.5rem;
    background: rgba(7,13,26,0.82);
    backdrop-filter: blur(24px) saturate(1.6);
    -webkit-backdrop-filter: blur(24px) saturate(1.6);
    border-bottom: 1px solid var(--bd);
  }
  .nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text);
    text-decoration: none;
    margin-right: auto;
    letter-spacing: 0.04em;
    display: flex;
    align-items: center;
    gap: 0.45rem;
  }
  .nav-logo svg { color: var(--pri); flex-shrink: 0; }
  nav a:not(.nav-logo) {
    color: var(--muted);
    text-decoration: none;
    font-size: 0.84rem;
    font-weight: 500;
    letter-spacing: 0.03em;
    padding: 0.3rem 0;
    position: relative;
    transition: color var(--t-fast) var(--ease-o);
  }
  nav a:not(.nav-logo)::after {
    content: '';
    position: absolute;
    bottom: -1px; left: 0;
    width: 0; height: 1.5px;
    background: var(--pri);
    transition: width var(--t-mid) var(--spring);
  }
  nav a:not(.nav-logo):hover { color: var(--text); }
  nav a:not(.nav-logo):hover::after { width: 100%; }

  .hero {
    position: relative;
    min-height: 100dvh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 8rem 2rem 5rem;
    overflow: hidden;
    background:
      linear-gradient(175deg,
        rgba(7,13,26,0.72) 0%,
        rgba(10,45,80,0.58) 45%,
        rgba(234,88,12,0.22) 100%),
      url('https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=1600&q=80')
      center/cover no-repeat;
  }

  #heroCanvas {
    position: absolute;
    inset: 0;
    width: 100%; height: 100%;
    z-index: 1;
    pointer-events: none;
  }

  .hero > *:not(#heroCanvas) {
    position: relative;
    z-index: 2;
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--pri);
    padding: 0.38rem 1rem;
    background: rgba(56,189,248,0.1);
    border: 1px solid rgba(56,189,248,0.28);
    border-radius: 999px;
    backdrop-filter: blur(8px);
    margin-bottom: 1.5rem;
    animation: si var(--t-enter) var(--spring) both;
  }

  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3.25rem, 9vw, 6.75rem);
    font-weight: 700;
    line-height: 1.04;
    letter-spacing: -0.025em;
    color: var(--text);
    margin-bottom: 0.75rem;
    animation: si var(--t-enter) var(--spring) both 80ms;
  }

  .hero h1 em {
    font-style: italic;
    background: linear-gradient(130deg, var(--pri) 0%, var(--gold) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-sub {
    font-size: 0.95rem;
    font-weight: 400;
    color: var(--muted);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 2.75rem;
    animation: si var(--t-enter) var(--spring) both 160ms;
  }

  .hero-tags {
    display: flex;
    gap: 0.55rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 3rem;
    animation: si var(--t-enter) var(--spring) both 240ms;
  }

  .hero-tag {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.11);
    color: rgba(255,255,255,0.75);
    padding: 0.28rem 0.85rem;
    border-radius: 999px;
    font-size: 0.76rem;
    font-weight: 500;
    letter-spacing: 0.04em;
  }

  .hero-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--acc);
    color: #fff;
    padding: 0.875rem 2.25rem;
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.9rem;
    text-decoration: none;
    letter-spacing: 0.02em;
    min-height: 48px;
    box-shadow: 0 4px 28px var(--glow-o);
    touch-action: manipulation;
    animation: si var(--t-enter) var(--spring) both 320ms;
    transition:
      background var(--t-fast) var(--ease-o),
      box-shadow var(--t-mid) var(--ease-o),
      transform var(--t-fast) var(--spring);
  }
  .hero-cta:hover {
    background: var(--acc-d);
    box-shadow: 0 8px 40px var(--glow-o);
    transform: translateY(-2px) scale(1.02);
  }
  .hero-cta:active { transform: scale(0.97); transition-duration: 80ms; }

  .hero-scroll {
    position: absolute;
    bottom: 2.25rem; left: 50%;
    transform: translateX(-50%);
    z-index: 3;
    color: var(--dim);
    font-size: 0.68rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
    animation: bounce-y 2.6s ease-in-out infinite;
  }

  .container {
    max-width: 920px;
    margin: 0 auto;
    padding: 5rem 1.5rem;
  }

  .sec-label {
    font-size: 0.67rem;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--pri);
    margin-bottom: 0.5rem;
  }

  .sec-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 2rem;
    line-height: 1.2;
  }

  .card {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 20px;
    padding: 2rem;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    margin-bottom: 1.5rem;
    transition:
      border-color var(--t-mid) var(--ease-o),
      background var(--t-mid) var(--ease-o),
      box-shadow var(--t-mid) var(--ease-o),
      transform var(--t-mid) var(--spring);
  }
  .card:hover {
    border-color: var(--bd-hv);
    background: var(--surf-hv);
    box-shadow: 0 0 0 1px rgba(56,189,248,0.08), 0 12px 48px rgba(0,0,0,0.45);
    transform: translateY(-3px);
  }
  .card h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    color: var(--text);
    margin-bottom: 0.75rem;
    font-weight: 700;
  }
  .card p {
    line-height: 1.82;
    color: var(--muted);
    font-size: 0.93rem;
  }
  .card strong { color: var(--text); font-weight: 600; }

  .stat-card {
    background: linear-gradient(135deg,
      rgba(14,165,233,0.12) 0%,
      rgba(56,189,248,0.06) 100%);
    border: 1px solid rgba(56,189,248,0.22);
    border-radius: 20px;
    padding: 2.75rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(20px);
  }
  .stat-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 65% -5%,
      rgba(56,189,248,0.16) 0%, transparent 55%);
    pointer-events: none;
  }
  .stat-card .s-label {
    font-size: 0.67rem;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--pri);
    margin-bottom: 1rem;
  }
  .stat-card .s-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.65rem;
    font-weight: 700;
    color: var(--text);
    line-height: 1.3;
    position: relative;
  }

  .geo-card {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 20px;
    padding: 2rem 2.25rem;
    margin-bottom: 1.5rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.75rem 2.5rem;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
  }
  .geo-item .gi-label {
    font-size: 0.64rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--dim);
    margin-bottom: 0.3rem;
  }
  .geo-item .gi-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--pri);
  }

  .city-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(185px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
  }
  .city-card {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 18px;
    padding: 1.75rem 1.25rem;
    text-align: center;
    text-decoration: none;
    color: var(--text);
    font-weight: 600;
    font-size: 0.9rem;
    backdrop-filter: blur(12px);
    touch-action: manipulation;
    transition:
      border-color var(--t-mid) var(--ease-o),
      background var(--t-mid) var(--ease-o),
      transform var(--t-mid) var(--spring),
      box-shadow var(--t-mid) var(--ease-o);
  }
  .city-card:hover {
    border-color: var(--bd-hv);
    background: var(--surf-hv);
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 12px 40px rgba(0,0,0,0.38), 0 0 0 1px rgba(56,189,248,0.08);
  }
  .city-card:active { transform: scale(0.97); transition-duration: 80ms; }
  .city-flag { font-size: 2.5rem; margin-bottom: 0.65rem; display: block; }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.75rem 1.75rem;
    background: var(--pri-d);
    color: #fff;
    text-decoration: none;
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.875rem;
    min-height: 44px;
    touch-action: manipulation;
    box-shadow: 0 2px 16px var(--glow-b);
    transition:
      background var(--t-fast) var(--ease-o),
      box-shadow var(--t-mid) var(--ease-o),
      transform var(--t-fast) var(--spring);
  }
  .btn:hover {
    background: var(--pri);
    box-shadow: 0 6px 24px var(--glow-b);
    transform: translateY(-1px);
  }
  .btn:active { transform: scale(0.97); transition-duration: 80ms; }

  .btn-ghost {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.7rem 1.5rem;
    border: 1px solid var(--bd);
    color: var(--muted);
    background: var(--surf);
    text-decoration: none;
    border-radius: 10px;
    font-weight: 500;
    font-size: 0.85rem;
    min-height: 44px;
    backdrop-filter: blur(8px);
    touch-action: manipulation;
    transition:
      border-color var(--t-fast) var(--ease-o),
      color var(--t-fast) var(--ease-o),
      transform var(--t-fast) var(--spring);
  }
  .btn-ghost:hover {
    border-color: var(--bd-hv);
    color: var(--text);
    transform: translateY(-1px);
  }
  .btn-ghost:active { transform: scale(0.97); transition-duration: 80ms; }

  .btn-row { display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem; }
  .back { margin-bottom: 2.25rem; }

  .info-banner {
    background: linear-gradient(135deg,
      rgba(249,115,22,0.08) 0%,
      rgba(251,191,36,0.04) 100%);
    border: 1px solid rgba(249,115,22,0.2);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(12px);
  }
  .info-banner p {
    line-height: 1.85;
    color: var(--muted);
    font-size: 0.93rem;
  }
  .info-banner strong { color: var(--text); }

  .divider {
    width: 48px; height: 2px;
    background: linear-gradient(90deg, var(--pri), transparent);
    margin: 0 0 2rem;
    border-radius: 999px;
  }

  footer {
    border-top: 1px solid var(--bd);
    text-align: center;
    padding: 2.25rem 1rem;
    font-size: 0.78rem;
    letter-spacing: 0.06em;
    color: var(--dim);
  }
  footer .ft-acc { color: var(--pri); font-weight: 600; }

  @media (prefers-reduced-motion: no-preference) {
    .sr {
      opacity: 0;
      transform: translateY(20px) scale(0.97);
      transition:
        opacity var(--t-enter) var(--spring),
        transform var(--t-enter) var(--spring);
      transition-delay: calc(var(--i, 0) * 50ms);
    }
    .sr.in {
      opacity: 1;
      transform: none;
    }
  }

  @keyframes si {
    from { opacity: 0; transform: translateY(18px) scale(0.96); }
    to   { opacity: 1; transform: none; }
  }
  @keyframes bounce-y {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50%       { transform: translateX(-50%) translateY(8px); }
  }

  @media (max-width: 640px) {
    nav { padding: 0 1.25rem; gap: 1.25rem; }
    .hero h1 { font-size: 2.75rem; }
    .geo-card { gap: 1.25rem 1.5rem; padding: 1.5rem; }
    .container { padding: 4rem 1.25rem; }
    .stat-card { padding: 2rem 1.5rem; }
  }
</style>
"""

SHADER_JS = """
<script>
(function() {
  var c = document.getElementById('heroCanvas');
  if (!c) return;
  var gl = c.getContext('webgl') || c.getContext('experimental-webgl');
  if (!gl) return;
  var vs = 'attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}';
  var fs = [
    'precision highp float;',
    'uniform float T;uniform vec2 R;',
    'float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}',
    'float n(vec2 p){vec2 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);',
    'return mix(mix(h(i),h(i+vec2(1,0)),u.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),u.x),u.y);}',
    'float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<4;i++){v+=a*n(p);p=p*2.1+vec2(1.3*float(i)+.7,1.7*float(i)+.3);a*=.5;}return v;}',
    'void main(){',
    'vec2 uv=gl_FragCoord.xy/R;float t=T*.1;',
    'vec2 q=vec2(fbm(uv*3.+t),fbm(uv*3.+vec2(1.)));',
    'vec2 r=vec2(fbm(uv*3.+2.*q+vec2(1.7,9.2)+.15*t),fbm(uv*3.+2.*q+vec2(8.3,2.8)+.126*t));',
    'float f=fbm(uv*3.+2.*r);',
    'vec3 c1=vec3(.047,.29,.431),c2=vec3(.055,.647,.914),c3=vec3(.918,.345,.047);',
    'vec3 col=mix(c1,c2,clamp(f*2.+.2,0.,1.));',
    'col=mix(col,c3,clamp(f*f*3.-.5,0.,1.));',
    'col+=vec3(.04,.1,.18)*clamp(f*f*f*2.,0.,1.);',
    'col*=smoothstep(0.,1.,1.-length((uv-.5)*1.8))*.55+.45;',
    'gl_FragColor=vec4(col,.5);}'
  ].join('');
  function sh(t,s){var x=gl.createShader(t);gl.shaderSource(x,s);gl.compileShader(x);return x;}
  var p=gl.createProgram();
  gl.attachShader(p,sh(gl.VERTEX_SHADER,vs));
  gl.attachShader(p,sh(gl.FRAGMENT_SHADER,fs));
  gl.linkProgram(p);gl.useProgram(p);
  var b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);
  gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  var al=gl.getAttribLocation(p,'a');gl.enableVertexAttribArray(al);
  gl.vertexAttribPointer(al,2,gl.FLOAT,false,0,0);
  gl.enable(gl.BLEND);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);
  var uT=gl.getUniformLocation(p,'T'),uR=gl.getUniformLocation(p,'R'),t0=performance.now();
  function resize(){c.width=Math.floor(c.offsetWidth*.6);c.height=Math.floor(c.offsetHeight*.6);gl.viewport(0,0,c.width,c.height);}
  window.addEventListener('resize',resize);resize();
  (function loop(){gl.uniform1f(uT,(performance.now()-t0)*.001);gl.uniform2f(uR,c.width,c.height);gl.clear(gl.COLOR_BUFFER_BIT);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);requestAnimationFrame(loop);})();
})();
</script>
"""

MOTION_JS = """
<script>
(function() {
  var els = document.querySelectorAll('.sr');
  if (!els.length) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach(function(el) { el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -32px 0px' });
  var seen = new Map();
  els.forEach(function(el) {
    var parent = el.parentElement;
    var idx = seen.get(parent) || 0;
    el.style.setProperty('--i', idx);
    seen.set(parent, idx + 1);
    io.observe(el);
  });
})();
</script>
"""


def page(title, body, nav_links="", shader=False, motion=False):
    return f"""<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Orase SCC</title>
  {STYLE}
</head>
<body>
  <nav>
    <a class="nav-logo" href="/">{_GLB} Orase</a>
    <a href="/">Acasa</a>
    <a href="/orase">Orase</a>
    {nav_links}
  </nav>
  {body}
  <footer>
    Proiect SCC 445D &nbsp;&middot;&nbsp;
    <span class="ft-acc">Vlasceanu Mihnea-Stefan</span>
    &nbsp;&middot;&nbsp; Barcelona
  </footer>
  {SHADER_JS if shader else ""}
  {MOTION_JS if motion else ""}
</body>
</html>"""


@app.route('/')
def index():
    body = f"""
    <div class="hero">
      <canvas id="heroCanvas"></canvas>
      <div class="hero-badge">
        {_PIN} &nbsp;41.3851° N &nbsp;·&nbsp; 2.1734° E
      </div>
      <h1>Explore <em>Orase</em></h1>
      <p class="hero-sub">Informatii despre orase din lume</p>
      <div class="hero-tags">
        <span class="hero-tag">Geografie</span>
        <span class="hero-tag">Populatie</span>
        <span class="hero-tag">Cultura</span>
        <span class="hero-tag">Arhitectura</span>
      </div>
      <a href="/orase" class="hero-cta">
        Exploreaza orasele {_ARR}
      </a>
      <div class="hero-scroll">
        {_DWN}
        scroll
      </div>
    </div>
    <div class="container">
      <div class="sec-label sr">Despre proiect</div>
      <div class="sec-title sr">Servicii Cloud si Containerizare</div>
      <div class="card sr">
        <p>Aplicatie web dezvoltata in cadrul cursului <strong>SCC</strong>, grupa 445D.
        Prezinta informatii geografice, demografice si culturale despre orase din intreaga lume.</p>
        <div class="btn-row">
          <a href="/orase" class="btn">
            {_PIN} &nbsp;Vezi orasele
          </a>
        </div>
      </div>
    </div>
    """
    return page("Acasa", body, shader=True, motion=True)


@app.route('/orase')
def orase():
    body = f"""
    <div style="padding-top:58px"></div>
    <div class="container">
      <div class="back sr">
        <a href="/" class="btn-ghost">{_BCK} &nbsp;Acasa</a>
      </div>
      <div class="sec-label sr">Explorare</div>
      <div class="sec-title sr">Orase disponibile</div>
      <div class="divider sr"></div>
      <div class="card sr">
        <p>Selecteaza un oras pentru a vedea informatii detaliate despre localizare,
        populatie si cultura.</p>
        <div class="city-grid">
          <a href="/barcelona" class="city-card sr">
            <span class="city-flag">&#127466;&#127480;</span>
            Barcelona
          </a>
        </div>
      </div>
    </div>
    """
    return page("Orase", body,
                nav_links=f'<a href="/barcelona">Barcelona</a>',
                motion=True)


@app.route('/barcelona')
def barcelona():
    body = f"""
    <div class="hero" style="min-height:65vh; background-image:
      linear-gradient(175deg,
        rgba(7,13,26,0.75) 0%,
        rgba(10,50,90,0.6) 50%,
        rgba(234,88,12,0.22) 100%),
      url('https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=1600&q=80')">
      <canvas id="heroCanvas"></canvas>
      <div class="hero-badge">
        {_PIN} &nbsp;41.3851° N &nbsp;·&nbsp; 2.1734° E
      </div>
      <h1><em>Barcelona</em></h1>
      <p class="hero-sub">Capitala Cataloniei &nbsp;·&nbsp; Spania</p>
      <div class="hero-tags">
        <span class="hero-tag">Costa Mediteraneana</span>
        <span class="hero-tag">Arhitectura Gaudi</span>
        <span class="hero-tag">JO 1992</span>
      </div>
    </div>
    <div class="container">
      <div class="back sr">
        <a href="/orase" class="btn-ghost">{_BCK} &nbsp;Orase</a>
      </div>
      <div class="geo-card sr">
        <div class="geo-item">
          <div class="gi-label">Latitudine</div>
          <div class="gi-value">41.3851° N</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Longitudine</div>
          <div class="gi-value">2.1734° E</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Altitudine</div>
          <div class="gi-value">12 m</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Tara</div>
          <div class="gi-value">Spania</div>
        </div>
      </div>
      <div class="card sr">
        <h2>Informatii despre Barcelona</h2>
        <p>Alege o sectiune pentru a afla mai multe despre acest oras mediteranean unic.</p>
        <div class="btn-row">
          <a href="/barcelona/populatie" class="btn">{_ARR} &nbsp;Populatie</a>
          <a href="/barcelona/descriere" class="btn">{_ARR} &nbsp;Descriere</a>
        </div>
      </div>
    </div>
    """
    return page("Barcelona", body,
                nav_links=f'<a href="/barcelona">Barcelona</a>',
                shader=True, motion=True)


@app.route('/barcelona/populatie')
def populatie():
    info = populatie_barcelona()
    body = f"""
    <div style="padding-top:58px"></div>
    <div class="container">
      <div class="back sr">
        <a href="/barcelona" class="btn-ghost">{_BCK} &nbsp;Barcelona</a>
      </div>
      <div class="sec-label sr">Date demografice</div>
      <div class="sec-title sr">Populatia Barcelonei</div>
      <div class="divider sr"></div>
      <div class="stat-card sr">
        <div class="s-label">Populatie &nbsp;&middot;&nbsp; Barcelona</div>
        <div class="s-value">{info}</div>
      </div>
      <div class="info-banner sr">
        <p>Barcelona este al doilea cel mai populat oras din Spania, dupa Madrid.
        Zona metropolitana depaseste <strong>5.5 milioane</strong> de locuitori,
        facand-o unul dintre cele mai mari centre urbane din sudul Europei.
        Densitatea populatiei in centrul orasului este de aproximativ
        <strong>16.000 locuitori/km&sup2;</strong>.</p>
      </div>
    </div>
    """
    return page("Populatie Barcelona", body,
                nav_links=f'<a href="/barcelona">Barcelona</a>',
                motion=True)


@app.route('/barcelona/descriere')
def descriere():
    info = descriere_barcelona()
    body = f"""
    <div style="padding-top:58px"></div>
    <div class="container">
      <div class="back sr">
        <a href="/barcelona" class="btn-ghost">{_BCK} &nbsp;Barcelona</a>
      </div>
      <div class="sec-label sr">Despre oras</div>
      <div class="sec-title sr">Descriere</div>
      <div class="divider sr"></div>
      <div class="card sr">
        <h2>Prezentare generala</h2>
        <p>{info}</p>
      </div>
      <div class="card sr">
        <h2>Repere culturale</h2>
        <p>Barcelona este renumita la nivel mondial pentru operele arhitectului
        <strong>Antoni Gaudi</strong>: Sagrada Familia, Park Guell, Casa Batllo si Casa Mila.
        Orasul a gazduit <strong>Jocurile Olimpice din 1992</strong>, eveniment care a
        transformat infrastructura urbana. Bucataria catalana, viata de noapte, plajele
        mediteraneene si muzeele de arta atrag anual peste
        <strong>12 milioane de turisti</strong>.</p>
      </div>
      <div class="geo-card sr">
        <div class="geo-item">
          <div class="gi-label">Fondare</div>
          <div class="gi-value">230 i.Hr.</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Suprafata</div>
          <div class="gi-value">101 km&sup2;</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Climat</div>
          <div class="gi-value">Mediteranean</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Temp. medie</div>
          <div class="gi-value">17.5° C</div>
        </div>
      </div>
    </div>
    """
    return page("Descriere Barcelona", body,
                nav_links=f'<a href="/barcelona">Barcelona</a>',
                motion=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
