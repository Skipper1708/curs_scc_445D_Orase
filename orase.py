from flask import Flask
from app.lib.biblioteca_orase import populatie_barcelona, descriere_barcelona

app = Flask(__name__)

STYLE = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Montserrat', sans-serif;
    background: #f0f4f8;
    color: #1a202c;
    min-height: 100vh;
  }

  nav {
    background: #003399;
    padding: 1rem 2rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.25);
  }
  nav .logo { font-weight: 700; font-size: 1.1rem; color: #fff; text-decoration: none; margin-right: auto; }
  nav a { color: #ffffffcc; text-decoration: none; font-size: 0.9rem; transition: color 0.2s; }
  nav a:hover { color: #fff; }

  .hero {
    background: linear-gradient(135deg, #003399 0%, #001a66 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
  }
  .hero .flag { font-size: 3.5rem; margin-bottom: 0.75rem; }
  .hero h1 { font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem; }
  .hero p { font-size: 1.05rem; opacity: 0.8; margin-bottom: 2rem; }

  .container { max-width: 860px; margin: 2rem auto; padding: 0 1.5rem; }

  .card {
    background: white;
    border-radius: 14px;
    padding: 2rem;
    box-shadow: 0 2px 14px rgba(0,0,0,0.07);
    margin-bottom: 1.5rem;
  }
  .card h2 { font-size: 1.25rem; font-weight: 600; color: #003399; margin-bottom: 0.75rem; }
  .card p { line-height: 1.75; color: #4a5568; }

  .stat-card {
    background: linear-gradient(135deg, #003399, #0055cc);
    color: white;
    border-radius: 14px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 20px rgba(0,51,153,0.3);
  }
  .stat-card .label { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px; opacity: 0.75; margin-bottom: 0.75rem; }
  .stat-card .value { font-size: 1.4rem; font-weight: 700; }

  .btn-grid { display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem; }

  .btn {
    display: inline-block;
    padding: 0.75rem 1.6rem;
    background: #003399;
    color: white;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    transition: background 0.2s, transform 0.15s;
  }
  .btn:hover { background: #0044cc; transform: translateY(-2px); }

  .btn-outline {
    display: inline-block;
    padding: 0.65rem 1.4rem;
    border: 2px solid #003399;
    color: #003399;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    transition: all 0.2s;
  }
  .btn-outline:hover { background: #003399; color: white; }

  .back { margin-bottom: 1.5rem; }

  .city-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1rem; margin-top: 1.5rem; }
  .city-card {
    background: #f7fafc;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    text-decoration: none;
    color: #1a202c;
    font-weight: 600;
    transition: all 0.2s;
  }
  .city-card:hover { border-color: #003399; background: #ebf0ff; transform: translateY(-2px); }
  .city-card .city-flag { font-size: 2.5rem; margin-bottom: 0.5rem; }

  footer { text-align: center; padding: 2.5rem 1rem; color: #a0aec0; font-size: 0.78rem; margin-top: 1rem; }
  footer span { color: #003399; font-weight: 600; }
</style>
"""


def page(title, body, nav_links=""):
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
    <a class="logo" href="/">🌍 Orase</a>
    <a href="/">Acasa</a>
    <a href="/orase">Orase</a>
    {nav_links}
  </nav>
  {body}
  <footer>Proiect SCC 445D &nbsp;·&nbsp; <span>Vlasceanu Mihnea-Stefan</span> &nbsp;·&nbsp; Barcelona</footer>
</body>
</html>"""


@app.route('/')
def index():
    body = """
    <div class="hero">
      <div class="flag">🌍</div>
      <h1>Aplicatie Orase</h1>
      <p>Informatii despre orase din intreaga lume</p>
      <a href="/orase" class="btn">Exploreaza orasele →</a>
    </div>
    <div class="container">
      <div class="card">
        <h2>Despre proiect</h2>
        <p>Aplicatie web dezvoltata in cadrul cursului <strong>Servicii Cloud si Containerizare</strong>.
        Prezinta informatii despre orase: populatie, descriere si repere culturale.</p>
        <div class="btn-grid">
          <a href="/orase" class="btn">Vezi orasele disponibile</a>
        </div>
      </div>
    </div>
    """
    return page("Acasa", body)


@app.route('/orase')
def orase():
    body = """
    <div class="container">
      <div class="back"><a href="/" class="btn-outline">← Acasa</a></div>
      <div class="card">
        <h2>🗺️ Orase disponibile</h2>
        <p>Selecteaza un oras pentru a vedea informatii detaliate.</p>
        <div class="city-grid">
          <a href="/barcelona" class="city-card">
            <div class="city-flag">🇪🇸</div>
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
    <div class="hero">
      <div class="flag">🇪🇸</div>
      <h1>Barcelona</h1>
      <p>Capitala Cataloniei &nbsp;·&nbsp; Spania</p>
    </div>
    <div class="container">
      <div class="back"><a href="/orase" class="btn-outline">← Orase</a></div>
      <div class="card">
        <h2>Informatii despre Barcelona</h2>
        <p>Alege o sectiune pentru a afla mai multe despre acest oras mediteranean.</p>
        <div class="btn-grid">
          <a href="/barcelona/populatie" class="btn">👥 Populatie</a>
          <a href="/barcelona/descriere" class="btn">📖 Descriere</a>
        </div>
      </div>
    </div>
    """
    return page("Barcelona", body, nav_links='<a href="/barcelona">Barcelona</a>')


@app.route('/barcelona/populatie')
def populatie():
    info = populatie_barcelona()
    body = f"""
    <div class="container">
      <div class="back"><a href="/barcelona" class="btn-outline">← Barcelona</a></div>
      <div class="stat-card">
        <div class="label">👥 Populatie</div>
        <div class="value">{info}</div>
      </div>
      <div class="card">
        <h2>Date demografice</h2>
        <p>Barcelona este unul dintre cele mai populate orase din Spania si din Europa de Sud.
        Zona metropolitana a orasului depaseste 5 milioane de locuitori, facand-o al doilea mare
        centru urban din Peninsula Iberica, dupa Madrid.</p>
      </div>
    </div>
    """
    return page("Populatie Barcelona", body, nav_links='<a href="/barcelona">Barcelona</a>')


@app.route('/barcelona/descriere')
def descriere():
    info = descriere_barcelona()
    body = f"""
    <div class="container">
      <div class="back"><a href="/barcelona" class="btn-outline">← Barcelona</a></div>
      <div class="card">
        <h2>📖 Descriere</h2>
        <p>{info}</p>
      </div>
      <div class="card">
        <h2>🏛️ Repere culturale</h2>
        <p>Barcelona este renumita pentru opera arhitectonica a lui <strong>Antoni Gaudi</strong>
        — Sagrada Familia, Park Guell, Casa Batllo. Orasul a gazduit <strong>Jocurile Olimpice din 1992</strong>
        si este sede al echipei de fotbal <strong>FC Barcelona</strong>.
        Bucataria catalana, plajele mediteraneene si viata culturala efervescenta
        atrag anual peste 12 milioane de turisti.</p>
      </div>
    </div>
    """
    return page("Descriere Barcelona", body, nav_links='<a href="/barcelona">Barcelona</a>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
