from flask import Flask
from app.lib.biblioteca_orase import populatie_como, descriere_como

app = Flask(__name__)

STYLE = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', sans-serif; background: #f0f7ff; color: #1a3a4a; }
    .header { background: linear-gradient(135deg, #1a6b8a, #2ecc71); padding: 30px; text-align: center; color: white; }
    .header h1 { font-size: 2em; letter-spacing: 2px; }
    .header p { opacity: 0.85; margin-top: 5px; }
    .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
    .card { background: white; border-radius: 12px; padding: 30px; margin: 20px 0;
            box-shadow: 0 4px 15px rgba(26,107,138,0.1); border-left: 5px solid #1a6b8a; }
    .card h2 { color: #1a6b8a; margin-bottom: 15px; }
    .card p { line-height: 1.7; color: #445; }
    .btn { display: inline-block; margin: 8px 5px; padding: 10px 22px;
           border-radius: 8px; text-decoration: none; font-weight: bold; transition: 0.2s; }
    .btn-blue { background: #1a6b8a; color: white; }
    .btn-green { background: #2ecc71; color: white; }
    .btn-blue:hover { background: #155a75; }
    .btn-green:hover { background: #27ae60; }
    .breadcrumb { color: #888; margin-bottom: 10px; font-size: 0.9em; }
    .info-box { background: #e8f5f9; border-radius: 8px; padding: 20px; margin: 15px 0; }
</style>
"""

@app.route('/')
def index():
    return STYLE + """
    <div class='header'><h1>🏙️ Aplicatie Orase</h1><p>Descoperiti orasele Europei</p></div>
    <div class='container'>
        <div class='card'>
            <h2>Bine ati venit!</h2>
            <p>Aceasta aplicatie prezinta informatii despre orase europene.</p>
            <a href='/orase' class='btn btn-blue'>Vezi orasele</a>
        </div>
    </div>"""

@app.route('/orase')
def orase():
    return STYLE + """
    <div class='header'><h1>🗺️ Orase</h1><p>Lista oraselor disponibile</p></div>
    <div class='container'>
        <div class='card'>
            <h2>Orase disponibile</h2>
            <a href='/como' class='btn btn-blue'>🇮🇹 Como</a>
        </div>
    </div>"""

@app.route('/como')
def como():
    return STYLE + """
    <div class='header'><h1>🇮🇹 Como</h1><p>Lacul Como - Nordul Italiei</p></div>
    <div class='container'>
        <div class='breadcrumb'>Orase / Como</div>
        <div class='card'>
            <h2>Informatii despre Como</h2>
            <p>Alege o categorie pentru a afla mai multe:</p>
            <a href='/como/populatie' class='btn btn-blue'>👥 Populatie</a>
            <a href='/como/descriere' class='btn btn-green'>📖 Descriere</a>
        </div>
        <a href='/orase' class='btn btn-blue'>← Inapoi</a>
    </div>"""

@app.route('/como/populatie')
def como_populatie():
    return STYLE + f"""
    <div class='header'><h1>👥 Populatia Como</h1></div>
    <div class='container'>
        <div class='breadcrumb'>Orase / Como / Populatie</div>
        <div class='card'>
            <h2>Date demografice</h2>
            <div class='info-box'><p>{populatie_como()}</p></div>
        </div>
        <a href='/como' class='btn btn-blue'>← Inapoi la Como</a>
    </div>"""

@app.route('/como/descriere')
def como_descriere():
    return STYLE + f"""
    <div class='header'><h1>📖 Descriere Como</h1></div>
    <div class='container'>
        <div class='breadcrumb'>Orase / Como / Descriere</div>
        <div class='card'>
            <h2>Despre Como</h2>
            <div class='info-box'><p>{descriere_como()}</p></div>
        </div>
        <a href='/como' class='btn btn-blue'>← Inapoi la Como</a>
    </div>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
