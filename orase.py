from flask import Flask
from app.lib.biblioteca_orase import populatie_varsovia, descriere_varsovia

app = Flask(__name__)

STYLE = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', sans-serif; background: #f0f4f8; color: #333; }
    .navbar { background: #DC143C; padding: 16px 32px; display: flex; align-items: center; gap: 24px; }
    .navbar a { color: white; text-decoration: none; font-weight: 600; font-size: 15px; }
    .navbar a:hover { text-decoration: underline; }
    .navbar .brand { font-size: 20px; font-weight: 700; margin-right: auto; }
    .hero { background: linear-gradient(135deg, #DC143C, #8B0000); color: white; padding: 64px 32px; text-align: center; }
    .hero h1 { font-size: 48px; margin-bottom: 12px; }
    .hero p { font-size: 18px; opacity: 0.9; }
    .container { max-width: 900px; margin: 40px auto; padding: 0 24px; }
    .card { background: white; border-radius: 12px; padding: 32px; margin-bottom: 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
    .card h2 { color: #DC143C; margin-bottom: 16px; font-size: 24px; }
    .card p { line-height: 1.7; font-size: 16px; color: #555; }
    .btn { display: inline-block; background: #DC143C; color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 8px 8px 8px 0; transition: background 0.2s; }
    .btn:hover { background: #8B0000; }
    .btn-outline { background: white; color: #DC143C; border: 2px solid #DC143C; }
    .btn-outline:hover { background: #DC143C; color: white; }
    .flag { font-size: 48px; margin-bottom: 16px; }
    .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px; }
    .info-box { background: #fff5f5; border-left: 4px solid #DC143C; padding: 16px; border-radius: 8px; }
    .info-box h3 { color: #DC143C; margin-bottom: 8px; }
    footer { text-align: center; padding: 32px; color: #999; font-size: 14px; background: white; margin-top: 40px; }
</style>
"""

@app.route('/')
def home():
    return f"""<!DOCTYPE html><html lang="ro"><head><meta charset="UTF-8"><title>Orase Europene</title>{STYLE}</head>
    <body>
    <nav class="navbar">
        <span class="brand">🌍 Orase Europene</span>
        <a href="/">Acasa</a>
        <a href="/orase">Orase</a>
        <a href="/varsovia">Varsovia</a>
    </nav>
    <div class="hero">
        <h1>Orase Europene</h1>
        <p>Proiect SCC 445D — Grupa Politehnica București</p>
    </div>
    <div class="container">
        <div class="card">
            <h2>Bun venit!</h2>
            <p>Această aplicație prezintă informații despre orașe europene. Explorează colecția noastră de orașe și descoperă detalii despre populație și istorie.</p>
            <br>
            <a href="/orase" class="btn">Vezi toate orașele</a>
            <a href="/varsovia" class="btn btn-outline">Varsovia</a>
        </div>
    </div>
    <footer>SCC 445D — Ioana Elena Delia — Politehnica București 2026</footer>
    </body></html>"""

@app.route('/orase')
def orase():
    return f"""<!DOCTYPE html><html lang="ro"><head><meta charset="UTF-8"><title>Lista Orase</title>{STYLE}</head>
    <body>
    <nav class="navbar">
        <span class="brand">🌍 Orase Europene</span>
        <a href="/">Acasa</a>
        <a href="/orase">Orase</a>
        <a href="/varsovia">Varsovia</a>
    </nav>
    <div class="hero">
        <h1>Orașe Disponibile</h1>
        <p>Selectează un oraș pentru mai multe informații</p>
    </div>
    <div class="container">
        <div class="card">
            <div class="flag">🇵🇱</div>
            <h2>Varsovia</h2>
            <p>Capitala Poloniei, situată pe râul Vistula. Cunoscuta pentru Orașul Vechi reconstruit și arhitectura sa unică.</p>
            <br>
            <a href="/varsovia" class="btn">Detalii</a>
            <a href="/varsovia/populatie" class="btn btn-outline">Populație</a>
            <a href="/varsovia/descriere" class="btn btn-outline">Descriere</a>
        </div>
    </div>
    <footer>SCC 445D — Ioana Elena Delia — Politehnica București 2026</footer>
    </body></html>"""

@app.route('/varsovia')
def varsovia():
    return f"""<!DOCTYPE html><html lang="ro"><head><meta charset="UTF-8"><title>Varsovia</title>{STYLE}</head>
    <body>
    <nav class="navbar">
        <span class="brand">🌍 Orase Europene</span>
        <a href="/">Acasa</a>
        <a href="/orase">Orase</a>
        <a href="/varsovia">Varsovia</a>
    </nav>
    <div class="hero">
        <div class="flag">🇵🇱</div>
        <h1>Varsovia</h1>
        <p>Capitala Republicii Polonia</p>
    </div>
    <div class="container">
        <div class="card">
            <h2>Despre Varsovia</h2>
            <p>Varsovia este capitala și cel mai mare oraș al Poloniei, situat pe râul Vistula în centrul țării.</p>
            <div class="info-grid">
                <div class="info-box">
                    <h3>👥 Populație</h3>
                    <p>~1.8 milioane locuitori</p>
                </div>
                <div class="info-box">
                    <h3>🌍 Țara</h3>
                    <p>Polonia</p>
                </div>
                <div class="info-box">
                    <h3>🏛️ Statut</h3>
                    <p>Capitală națională</p>
                </div>
                <div class="info-box">
                    <h3>🌊 Râu</h3>
                    <p>Vistula</p>
                </div>
            </div>
            <br>
            <a href="/varsovia/populatie" class="btn">Populație</a>
            <a href="/varsovia/descriere" class="btn btn-outline">Descriere</a>
        </div>
    </div>
    <footer>SCC 445D — Ioana Elena Delia — Politehnica București 2026</footer>
    </body></html>"""

@app.route('/varsovia/populatie')
def varsovia_populatie():
    rezultat = populatie_varsovia()
    return f"""<!DOCTYPE html><html lang="ro"><head><meta charset="UTF-8"><title>Populatie Varsovia</title>{STYLE}</head>
    <body>
    <nav class="navbar">
        <span class="brand">🌍 Orase Europene</span>
        <a href="/">Acasa</a>
        <a href="/orase">Orase</a>
        <a href="/varsovia">Varsovia</a>
    </nav>
    <div class="hero">
        <h1>👥 Populația Varsoviei</h1>
    </div>
    <div class="container">
        <div class="card">
            <h2>Date despre populație</h2>
            <p>{rezultat}</p>
            <br>
            <a href="/varsovia" class="btn btn-outline">← Înapoi la Varsovia</a>
            <a href="/varsovia/descriere" class="btn">Descriere</a>
        </div>
    </div>
    <footer>SCC 445D — Ioana Elena Delia — Politehnica București 2026</footer>
    </body></html>"""

@app.route('/varsovia/descriere')
def varsovia_descriere():
    rezultat = descriere_varsovia()
    return f"""<!DOCTYPE html><html lang="ro"><head><meta charset="UTF-8"><title>Descriere Varsovia</title>{STYLE}</head>
    <body>
    <nav class="navbar">
        <span class="brand">🌍 Orase Europene</span>
        <a href="/">Acasa</a>
        <a href="/orase">Orase</a>
        <a href="/varsovia">Varsovia</a>
    </nav>
    <div class="hero">
        <h1>📖 Descrierea Varsoviei</h1>
    </div>
    <div class="container">
        <div class="card">
            <h2>Despre oraș</h2>
            <p>{rezultat}</p>
            <br>
            <a href="/varsovia" class="btn btn-outline">← Înapoi la Varsovia</a>
            <a href="/varsovia/populatie" class="btn">Populație</a>
        </div>
    </div>
    <footer>SCC 445D — Ioana Elena Delia — Politehnica București 2026</footer>
    </body></html>"""
