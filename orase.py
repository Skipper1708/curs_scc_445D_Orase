from flask import Flask
from app.lib.biblioteca_orase import get_populatie_lisabona, get_descriere_lisabona

app = Flask(__name__)

CSS = """
<style>
    body { font-family: Arial, sans-serif; background-color: #f0f4f8; margin: 0; padding: 20px; }
    .card { background: white; border-radius: 12px; padding: 30px; margin: 20px auto; max-width: 800px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
    h1 { color: #1a3c6e; }
    h2 { color: #c0392b; }
    .btn { display: inline-block; padding: 10px 20px; margin: 8px 4px; border-radius: 25px; text-decoration: none; color: white; font-weight: bold; }
    .btn-blue { background-color: #1a3c6e; }
    .btn-red { background-color: #c0392b; }
    .btn-green { background-color: #27ae60; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 20px; }
    .info-card { background: #fff8f0; border: 1px solid #f0a500; border-radius: 8px; padding: 15px; }
    .info-card h3 { color: #f0a500; margin: 0 0 8px 0; }
    p { color: #444; line-height: 1.6; }
    nav { color: #666; margin-bottom: 10px; }
</style>
"""

@app.route('/')
def index():
    return f"""<html><head><title>Aplicatie Orase</title></head><body>{CSS}
    <div class='card'>
        <h1>Aplicatie Orase</h1>
        <p>Aceasta aplicatie prezinta informatii despre orase alese de studenti.</p>
        <a href='/orase' class='btn btn-blue'>Tema Orase</a>
        <a href='/lisabona' class='btn btn-red'>Lisabona</a>
    </div></body></html>"""

@app.route('/orase')
def orase():
    return f"""<html><head><title>Tema Orase</title></head><body>{CSS}
    <div class='card'>
        <nav>Orase</nav>
        <h1>Tema proiectului: Orase</h1>
        <p>Aceasta aplicatie Flask permite fiecarui student sa adauge propria functionalitate pentru un oras ales.</p>
        <p>Elementul implementat de Alina Pirvu este orasul <strong>Lisabona</strong>.</p>
        <a href='/lisabona' class='btn btn-blue'>Deschide pagina orasului Lisabona</a>
        <a href='/' class='btn btn-red'>Inapoi la pagina principala</a>
    </div></body></html>"""

@app.route('/lisabona')
def lisabona():
    populatie = get_populatie_lisabona()
    descriere = get_descriere_lisabona()
    return f"""<html><head><title>Lisabona</title></head><body>{CSS}
    <div class='card'>
        <nav>Orase / Lisabona</nav>
        <h1>Lisabona — capitala Portugaliei</h1>
        <p>{descriere}</p>
        <div class='grid'>
            <div class='info-card'><h3>Tara</h3><p>Portugalia</p></div>
            <div class='info-card'><h3>Rau</h3><p>Tejo</p></div>
            <div class='info-card'><h3>Cunoscuta pentru</h3><p>istorie, fado, arhitectura</p></div>
        </div>
        <br>
        <a href='/lisabona/populatie' class='btn btn-blue'>Populatie</a>
        <a href='/lisabona/descriere' class='btn btn-red'>Descriere</a>
        <a href='/orase' class='btn btn-green'>Inapoi la Orase</a>
    </div></body></html>"""

@app.route('/lisabona/populatie')
def lisabona_populatie():
    populatie = get_populatie_lisabona()
    return f"""<html><head><title>Populatie Lisabona</title></head><body>{CSS}
    <div class='card'>
        <nav>Orase / Lisabona / Populatie</nav>
        <h1>Populatia orasului Lisabona</h1>
        <p>Lisabona este cel mai mare oras din Portugalia si capitala tarii.</p>
        <div class='grid'>
            <div class='info-card'><h3>Populatie municipiu</h3><p>{populatie} locuitori</p></div>
            <div class='info-card'><h3>Zona metropolitana</h3><p>~2.8 milioane locuitori</p></div>
        </div>
        <br>
        <a href='/lisabona' class='btn btn-blue'>Inapoi la Lisabona</a>
    </div></body></html>"""

@app.route('/lisabona/descriere')
def lisabona_descriere():
    descriere = get_descriere_lisabona()
    return f"""<html><head><title>Descriere Lisabona</title></head><body>{CSS}
    <div class='card'>
        <nav>Orase / Lisabona / Descriere</nav>
        <h1>Descriere Lisabona</h1>
        <p>{descriere}</p>
        <p>Lisabona este cunoscuta pentru tramvaiele istorice, cartierul Alfama, 
        monumentele manueliene si cultura fado. Este unul dintre cele mai vechi orase din Europa,
        cu o istorie de peste 3000 de ani.</p>
        <div class='grid'>
            <div class='info-card'><h3>Fondare</h3><p>~1200 i.Hr.</p></div>
            <div class='info-card'><h3>Climat</h3><p>Mediterranean</p></div>
            <div class='info-card'><h3>Atractii</h3><p>Alfama, Torre de Belem, Jeronimos</p></div>
        </div>
        <br>
        <a href='/lisabona' class='btn btn-blue'>Inapoi la Lisabona</a>
    </div></body></html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=False)
