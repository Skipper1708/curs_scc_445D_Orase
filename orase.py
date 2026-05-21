from flask import Flask
from app.lib.biblioteca_orase import populatie_sarajevo, descriere_sarajevo

app = Flask(__name__)

CSS = """
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Segoe UI', sans-serif; background: #0f0f1a; color: #eee; min-height: 100vh; }
  nav { background: #1a1a2e; padding: 16px 40px; display: flex; align-items: center; gap: 20px; box-shadow: 0 2px 10px #0005; }
  nav a { color: #a78bfa; text-decoration: none; font-weight: 500; transition: color 0.2s; }
  nav a:hover { color: #fff; }
  nav .brand { color: #fff; font-size: 1.2rem; font-weight: 700; margin-right: auto; }
  .hero { background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460); padding: 80px 40px; text-align: center; }
  .hero h1 { font-size: 3rem; font-weight: 800; background: linear-gradient(90deg, #a78bfa, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 16px; }
  .hero p { font-size: 1.1rem; color: #94a3b8; max-width: 600px; margin: 0 auto 30px; }
  .btn { display: inline-block; padding: 12px 28px; background: linear-gradient(135deg, #7c3aed, #3b82f6); color: #fff; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 6px; transition: transform 0.2s, box-shadow 0.2s; }
  .btn:hover { transform: translateY(-2px); box-shadow: 0 8px 20px #7c3aed55; }
  .container { max-width: 900px; margin: 60px auto; padding: 0 40px; }
  .card { background: #1a1a2e; border: 1px solid #2d2d4e; border-radius: 16px; padding: 40px; margin-bottom: 24px; }
  .card h2 { font-size: 1.8rem; color: #a78bfa; margin-bottom: 16px; }
  .card p { color: #cbd5e1; line-height: 1.8; font-size: 1.05rem; }
  .badge { display: inline-block; background: #7c3aed22; color: #a78bfa; border: 1px solid #7c3aed55; border-radius: 20px; padding: 4px 14px; font-size: 0.85rem; margin-bottom: 20px; }
  .city-list { list-style: none; display: flex; flex-direction: column; gap: 12px; }
  .city-list li a { display: flex; align-items: center; gap: 12px; padding: 16px 24px; background: #16213e; border: 1px solid #2d2d4e; border-radius: 10px; color: #e2e8f0; text-decoration: none; transition: border-color 0.2s, background 0.2s; }
  .city-list li a:hover { border-color: #7c3aed; background: #1e1e3f; }
  .city-list li a .icon { font-size: 1.5rem; }
  footer { text-align: center; padding: 30px; color: #475569; font-size: 0.9rem; border-top: 1px solid #1e1e3f; margin-top: 60px; }
</style>
"""

@app.route('/')
def home():
    return CSS + """
<nav>
  <span class="brand">🌍 Orase</span>
  <a href="/orase">Orase</a>
  <a href="/sarajevo">Sarajevo</a>
</nav>
<div class="hero">
  <h1>Aplicatie Flask - Orase</h1>
  <p>Proiect SCC 445D — Servicii Cloud si Containerizare, Politehnica Bucuresti</p>
  <a href="/orase" class="btn">Vezi Orasele</a>
  <a href="/sarajevo" class="btn">Sarajevo</a>
</div>
<footer>SCC 445D &mdash; Rezus Catalin &mdash; Sarajevo</footer>
"""

@app.route('/orase')
def orase():
    return CSS + """
<nav>
  <span class="brand">🌍 Orase</span>
  <a href="/">Acasa</a>
  <a href="/sarajevo">Sarajevo</a>
</nav>
<div class="container">
  <div class="card">
    <span class="badge">Lista orase</span>
    <h2>Orase disponibile</h2>
    <ul class="city-list">
      <li><a href="/sarajevo"><span class="icon">🏙️</span> Sarajevo</a></li>
    </ul>
  </div>
</div>
<footer>SCC 445D &mdash; Rezus Catalin</footer>
"""

@app.route('/sarajevo')
def sarajevo():
    return CSS + """
<nav>
  <span class="brand">🌍 Orase</span>
  <a href="/">Acasa</a>
  <a href="/orase">Orase</a>
</nav>
<div class="hero">
  <h1>🏙️ Sarajevo</h1>
  <p>Capitala Bosniei si Hertegovina</p>
  <a href="/sarajevo/populatie" class="btn">Populatie</a>
  <a href="/sarajevo/descriere" class="btn">Descriere</a>
</div>
<footer>SCC 445D &mdash; Rezus Catalin</footer>
"""

@app.route('/sarajevo/populatie')
def populatie():
    return CSS + f"""
<nav>
  <span class="brand">🌍 Orase</span>
  <a href="/">Acasa</a>
  <a href="/orase">Orase</a>
  <a href="/sarajevo">Sarajevo</a>
</nav>
<div class="container">
  <div class="card">
    <span class="badge">Populatie</span>
    <h2>👥 Populatia Sarajevo</h2>
    <p>{populatie_sarajevo()}</p>
  </div>
</div>
<footer>SCC 445D &mdash; Rezus Catalin</footer>
"""

@app.route('/sarajevo/descriere')
def descriere():
    return CSS + f"""
<nav>
  <span class="brand">🌍 Orase</span>
  <a href="/">Acasa</a>
  <a href="/orase">Orase</a>
  <a href="/sarajevo">Sarajevo</a>
</nav>
<div class="container">
  <div class="card">
    <span class="badge">Descriere</span>
    <h2>📖 Despre Sarajevo</h2>
    <p>{descriere_sarajevo()}</p>
  </div>
</div>
<footer>SCC 445D &mdash; Rezus Catalin</footer>
"""
