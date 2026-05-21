from flask import Flask
from app.lib.biblioteca_orase import populatie_barcelona, descriere_barcelona

app = Flask(__name__)

STYLE = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap');

  :root {
    --primary:    #0EA5E9;
    --secondary:  #38BDF8;
    --accent:     #EA580C;
    --bg:         #F0F9FF;
    --fg:         #0C4A6E;
    --muted:      #E8F2F8;
    --border:     #BAE6FD;
    --white:      #FFFFFF;
    --dark:       #0F172A;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--fg);
    min-height: 100vh;
    overflow-x: hidden;
  }

  nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 100;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding: 1rem 2.5rem;
    display: flex;
    align-items: center;
    gap: 2rem;
  }
  nav .logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--white);
    text-decoration: none;
    margin-right: auto;
    letter-spacing: 0.02em;
  }
  nav a {
    color: rgba(255,255,255,0.65);
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    letter-spacing: 0.03em;
    transition: color 0.2s;
  }
  nav a:hover { color: var(--white); }

  .hero {
    min-height: 100vh;
    position: relative;
    background:
      linear-gradient(180deg,
        rgba(12, 74, 110, 0.72) 0%,
        rgba(14, 165, 233, 0.45) 55%,
        rgba(234, 88, 12, 0.35) 100%),
      url('https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=1600&q=80') center/cover no-repeat;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 8rem 2rem 4rem;
  }

  #heroCanvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    pointer-events: none;
  }

  .hero > *:not(#heroCanvas) {
    position: relative;
    z-index: 2;
  }

  .hero-coords {
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.6);
    margin-bottom: 1.25rem;
    animation: fadeDown 0.8s ease both;
  }
  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 8vw, 6rem);
    font-weight: 700;
    color: var(--white);
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 0.5rem;
    animation: fadeDown 0.9s ease both 0.1s;
  }
  .hero-subtitle {
    font-size: 1.1rem;
    font-weight: 300;
    color: rgba(255,255,255,0.75);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 2.5rem;
    animation: fadeDown 1s ease both 0.2s;
  }
  .hero-tags {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 3rem;
    animation: fadeDown 1.1s ease both 0.3s;
  }
  .hero-tag {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    color: rgba(255,255,255,0.9);
    padding: 0.35rem 1rem;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 500;
    letter-spacing: 0.05em;
    backdrop-filter: blur(6px);
  }
  .hero-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--accent);
    color: var(--white);
    padding: 0.9rem 2.25rem;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.95rem;
    text-decoration: none;
    letter-spacing: 0.02em;
    transition: background 0.2s, transform 0.15s, box-shadow 0.2s;
    box-shadow: 0 4px 20px rgba(234,88,12,0.4);
    animation: fadeDown 1.2s ease both 0.4s;
  }
  .hero-cta:hover {
    background: #C2410C;
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(234,88,12,0.5);
  }
  .hero-scroll {
    position: absolute;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(255,255,255,0.4);
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    animation: bounce 2s infinite;
    z-index: 2;
  }

  .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 4rem 1.5rem;
  }

  .section-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 0.5rem;
  }
  .section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 2rem;
  }

  .card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 2px 16px rgba(14,165,233,0.07);
    margin-bottom: 1.5rem;
    transition: box-shadow 0.25s, transform 0.25s;
    animation: fadeUp 0.6s ease both;
  }
  .card:hover {
    box-shadow: 0 8px 32px rgba(14,165,233,0.15);
    transform: translateY(-3px);
  }
  .card h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: var(--fg);
    margin-bottom: 0.75rem;
  }
  .card p {
    line-height: 1.8;
    color: #475569;
    font-size: 0.95rem;
  }

  .stat-card {
    background: linear-gradient(135deg, var(--fg) 0%, var(--primary) 100%);
    border-radius: 16px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px rgba(14,165,233,0.25);
    animation: fadeUp 0.6s ease both;
    position: relative;
    overflow: hidden;
  }
  .stat-card::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 180px; height: 180px;
    background: rgba(255,255,255,0.06);
    border-radius: 50%;
  }
  .stat-card .label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.6);
    margin-bottom: 0.75rem;
  }
  .stat-card .value {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--white);
    line-height: 1.3;
  }

  .geo-card {
    background: var(--dark);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    animation: fadeUp 0.6s ease both;
  }
  .geo-item .geo-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.4);
    margin-bottom: 0.25rem;
  }
  .geo-item .geo-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--secondary);
  }

  .city-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
  }
  .city-card {
    background: var(--white);
    border: 2px solid var(--border);
    border-radius: 14px;
    padding: 1.75rem 1.25rem;
    text-align: center;
    text-decoration: none;
    color: var(--fg);
    font-weight: 600;
    font-size: 0.95rem;
    transition: border-color 0.2s, background 0.2s, transform 0.2s, box-shadow 0.2s;
    cursor: pointer;
  }
  .city-card:hover {
    border-color: var(--primary);
    background: var(--muted);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(14,165,233,0.15);
  }
  .city-card .city-icon { font-size: 2.25rem; margin-bottom: 0.6rem; }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.75rem 1.75rem;
    background: var(--primary);
    color: var(--white);
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    transition: background 0.2s, transform 0.15s;
    cursor: pointer;
  }
  .btn:hover { background: #0284C7; transform: translateY(-1px); }

  .btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.65rem 1.4rem;
    border: 2px solid var(--border);
    color: var(--fg);
    background: var(--white);
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.875rem;
    transition: all 0.2s;
    cursor: pointer;
  }
  .btn-outline:hover { border-color: var(--primary); color: var(--primary); }

  .btn-grid { display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem; }
  .back { margin-bottom: 2rem; }

  .info-banner {
    background: linear-gradient(135deg, var(--muted), var(--white));
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    animation: fadeUp 0.6s ease both;
  }
  .info-banner p {
    line-height: 1.8;
    color: #334155;
    font-size: 0.95rem;
  }

  footer {
    background: var(--dark);
    color: rgba(255,255,255,0.4);
    text-align: center;
    padding: 2rem 1rem;
    font-size: 0.8rem;
    letter-spacing: 0.04em;
  }
  footer span { color: var(--secondary); font-weight: 600; }

  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes bounce {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50%       { transform: translateX(-50%) translateY(8px); }
  }

  @media (max-width: 600px) {
    .geo-card { grid-template-columns: 1fr 1fr; }
    nav { padding: 1rem 1.25rem; gap: 1rem; }
    .hero h1 { font-size: 2.75rem; }
  }
</style>
"""

SHADER_JS = """
<script>
(function() {
  var canvas = document.getElementById('heroCanvas');
  if (!canvas) return;
  var gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
  if (!gl) return;

  var vs = 'attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}';

  var fs = [
    'precision highp float;',
    'uniform float T;',
    'uniform vec2 R;',

    'float h(vec2 p){',
    '  return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);',
    '}',

    'float n(vec2 p){',
    '  vec2 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);',
    '  return mix(mix(h(i),h(i+vec2(1,0)),u.x),',
    '             mix(h(i+vec2(0,1)),h(i+vec2(1,1)),u.x),u.y);',
    '}',

    'float fbm(vec2 p){',
    '  float v=0.,a=.5;',
    '  for(int i=0;i<4;i++){v+=a*n(p);p=p*2.1+vec2(1.3*float(i)+.7,1.7*float(i)+.3);a*=.5;}',
    '  return v;',
    '}',

    'void main(){',
    '  vec2 uv=gl_FragCoord.xy/R;',
    '  float t=T*.1;',
    '  vec2 q=vec2(fbm(uv*3.+t),fbm(uv*3.+vec2(1.)));',
    '  vec2 r=vec2(fbm(uv*3.+2.*q+vec2(1.7,9.2)+.15*t),',
    '              fbm(uv*3.+2.*q+vec2(8.3,2.8)+.126*t));',
    '  float f=fbm(uv*3.+2.*r);',
    '  vec3 c1=vec3(.047,.29,.431);',
    '  vec3 c2=vec3(.055,.647,.914);',
    '  vec3 c3=vec3(.918,.345,.047);',
    '  vec3 col=mix(c1,c2,clamp(f*2.+.2,0.,1.));',
    '  col=mix(col,c3,clamp(f*f*3.-.5,0.,1.));',
    '  col+=vec3(.05,.1,.18)*clamp(f*f*f*2.,0.,1.);',
    '  float vig=1.-length((uv-.5)*1.8);',
    '  col*=smoothstep(0.,1.,vig)*.6+.4;',
    '  gl_FragColor=vec4(col,.52);',
    '}'
  ].join('\\n');

  function sh(type, src) {
    var s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    return s;
  }
  var prog = gl.createProgram();
  gl.attachShader(prog, sh(gl.VERTEX_SHADER, vs));
  gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(prog);
  gl.useProgram(prog);

  var buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1,1,-1,-1,1,1,1]), gl.STATIC_DRAW);
  var aLoc = gl.getAttribLocation(prog, 'a');
  gl.enableVertexAttribArray(aLoc);
  gl.vertexAttribPointer(aLoc, 2, gl.FLOAT, false, 0, 0);
  gl.enable(gl.BLEND);
  gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);

  var uT = gl.getUniformLocation(prog, 'T');
  var uR = gl.getUniformLocation(prog, 'R');
  var t0 = performance.now();

  function resize() {
    canvas.width  = Math.floor(canvas.offsetWidth  * .6);
    canvas.height = Math.floor(canvas.offsetHeight * .6);
    gl.viewport(0, 0, canvas.width, canvas.height);
  }
  window.addEventListener('resize', resize);
  resize();

  (function loop() {
    gl.uniform1f(uT, (performance.now() - t0) * .001);
    gl.uniform2f(uR, canvas.width, canvas.height);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    requestAnimationFrame(loop);
  })();
})();
</script>
"""


def page(title, body, nav_links="", with_shader=False):
    shader = SHADER_JS if with_shader else ""
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
    <a class="logo" href="/">Orase</a>
    <a href="/">Acasa</a>
    <a href="/orase">Orase</a>
    {nav_links}
  </nav>
  {body}
  <footer>
    Proiect SCC 445D &nbsp;&middot;&nbsp; <span>Vlasceanu Mihnea-Stefan</span> &nbsp;&middot;&nbsp; Barcelona
  </footer>
  {shader}
</body>
</html>"""


@app.route('/')
def index():
    body = """
    <div class="hero">
      <canvas id="heroCanvas"></canvas>
      <div class="hero-coords">41.3851° N &nbsp;·&nbsp; 2.1734° E &nbsp;·&nbsp; 12m alt</div>
      <h1>Orase</h1>
      <p class="hero-subtitle">Informatii despre orase din lume</p>
      <div class="hero-tags">
        <span class="hero-tag">Geografie</span>
        <span class="hero-tag">Populatie</span>
        <span class="hero-tag">Cultura</span>
        <span class="hero-tag">Arhitectura</span>
      </div>
      <a href="/orase" class="hero-cta">Exploreaza orasele &#8594;</a>
      <div class="hero-scroll">&#8595; scroll</div>
    </div>
    <div class="container">
      <div class="section-label">Despre proiect</div>
      <div class="section-title">Servicii Cloud si Containerizare</div>
      <div class="card">
        <p>Aplicatie web dezvoltata in cadrul cursului <strong>SCC</strong>, grupa 445D.
        Prezinta informatii geografice, demografice si culturale despre orase din intreaga lume.</p>
        <div class="btn-grid">
          <a href="/orase" class="btn">Vezi orasele</a>
        </div>
      </div>
    </div>
    """
    return page("Acasa", body, with_shader=True)


@app.route('/orase')
def orase():
    body = """
    <div style="padding-top:80px"></div>
    <div class="container">
      <div class="back"><a href="/" class="btn-outline">&#8592; Acasa</a></div>
      <div class="section-label">Explorare</div>
      <div class="section-title">Orase disponibile</div>
      <div class="card">
        <p>Selecteaza un oras pentru a vedea informatii detaliate despre localizare, populatie si cultura.</p>
        <div class="city-grid">
          <a href="/barcelona" class="city-card">
            <div class="city-icon">&#127466;&#127480;</div>
            Barcelona
          </a>
        </div>
      </div>
    </div>
    """
    return page("Orase", body, nav_links='<a href="/barcelona">Barcelona</a>')


@app.route('/barcelona')
def barcelona():
    body = """
    <div class="hero" style="min-height:60vh; background-image:
      linear-gradient(180deg, rgba(12,74,110,0.75) 0%, rgba(14,165,233,0.5) 60%, rgba(234,88,12,0.3) 100%),
      url('https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=1600&q=80')">
      <canvas id="heroCanvas"></canvas>
      <div class="hero-coords">41.3851° N &nbsp;·&nbsp; 2.1734° E</div>
      <h1>Barcelona</h1>
      <p class="hero-subtitle">Capitala Cataloniei &nbsp;·&nbsp; Spania</p>
      <div class="hero-tags">
        <span class="hero-tag">Costa Mediteraneana</span>
        <span class="hero-tag">Arhitectura Gaudi</span>
        <span class="hero-tag">JO 1992</span>
      </div>
    </div>
    <div class="container">
      <div class="back"><a href="/orase" class="btn-outline">&#8592; Orase</a></div>
      <div class="geo-card">
        <div class="geo-item">
          <div class="geo-label">Latitudine</div>
          <div class="geo-value">41.3851° N</div>
        </div>
        <div class="geo-item">
          <div class="geo-label">Longitudine</div>
          <div class="geo-value">2.1734° E</div>
        </div>
        <div class="geo-item">
          <div class="geo-label">Altitudine</div>
          <div class="geo-value">12 m</div>
        </div>
        <div class="geo-item">
          <div class="geo-label">Tara</div>
          <div class="geo-value">Spania</div>
        </div>
      </div>
      <div class="card">
        <h2>Informatii despre Barcelona</h2>
        <p>Alege o sectiune pentru a afla mai multe despre acest oras mediteranean unic.</p>
        <div class="btn-grid">
          <a href="/barcelona/populatie" class="btn">Populatie</a>
          <a href="/barcelona/descriere" class="btn">Descriere</a>
        </div>
      </div>
    </div>
    """
    return page("Barcelona", body, nav_links='<a href="/barcelona">Barcelona</a>', with_shader=True)


@app.route('/barcelona/populatie')
def populatie():
    info = populatie_barcelona()
    body = f"""
    <div style="padding-top:80px"></div>
    <div class="container">
      <div class="back"><a href="/barcelona" class="btn-outline">&#8592; Barcelona</a></div>
      <div class="section-label">Date demografice</div>
      <div class="section-title">Populatia Barcelonei</div>
      <div class="stat-card">
        <div class="label">Populatie &nbsp;&#183;&nbsp; Barcelona</div>
        <div class="value">{info}</div>
      </div>
      <div class="info-banner">
        <p>Barcelona este al doilea cel mai populat oras din Spania, dupa Madrid.
        Zona metropolitana depaseste <strong>5.5 milioane</strong> de locuitori,
        facand-o unul dintre cele mai mari centre urbane din sudul Europei.
        Densitatea populatiei in centrul orasului este de aproximativ
        <strong>16.000 locuitori/km&sup2;</strong>.</p>
      </div>
    </div>
    """
    return page("Populatie Barcelona", body, nav_links='<a href="/barcelona">Barcelona</a>')


@app.route('/barcelona/descriere')
def descriere():
    info = descriere_barcelona()
    body = f"""
    <div style="padding-top:80px"></div>
    <div class="container">
      <div class="back"><a href="/barcelona" class="btn-outline">&#8592; Barcelona</a></div>
      <div class="section-label">Despre oras</div>
      <div class="section-title">Descriere</div>
      <div class="card">
        <h2>Prezentare generala</h2>
        <p>{info}</p>
      </div>
      <div class="card" style="animation-delay:0.1s">
        <h2>Repere culturale</h2>
        <p>Barcelona este renumita la nivel mondial pentru operele arhitectului <strong>Antoni Gaudi</strong>:
        Sagrada Familia, Park Guell, Casa Batllo si Casa Mila.
        Orasul a gazduit <strong>Jocurile Olimpice din 1992</strong>, eveniment care a transformat
        infrastructura urbana. Bucataria catalana, viata de noapte, plajele mediteraneene
        si muzeele de arta atrag anual peste <strong>12 milioane de turisti</strong>.</p>
      </div>
      <div class="geo-card" style="animation-delay:0.2s">
        <div class="geo-item">
          <div class="geo-label">Fondare</div>
          <div class="geo-value">230 i.Hr.</div>
        </div>
        <div class="geo-item">
          <div class="geo-label">Suprafata</div>
          <div class="geo-value">101 km&sup2;</div>
        </div>
        <div class="geo-item">
          <div class="geo-label">Climat</div>
          <div class="geo-value">Mediteranean</div>
        </div>
        <div class="geo-item">
          <div class="geo-label">Temperatura medie</div>
          <div class="geo-value">17.5° C</div>
        </div>
      </div>
    </div>
    """
    return page("Descriere Barcelona", body, nav_links='<a href="/barcelona">Barcelona</a>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
