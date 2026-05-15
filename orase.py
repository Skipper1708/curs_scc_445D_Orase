from flask import Flask
from app.lib.biblioteca_orase import get_populatie_lisabona, get_descriere_lisabona

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html><body>
    <h1>Aplicatie Orase</h1>
    <ul><li><a href="/lisabona">Lisabona</a></li></ul>
    </body></html>
    '''

@app.route('/lisabona')
def lisabona():
    populatie = get_populatie_lisabona()
    descriere = get_descriere_lisabona()
    return f'''
    <html><body>
    <h1>Lisabona</h1>
    <p>{descriere}</p>
    <p><b>Populatie:</b> {populatie} locuitori</p>
    <a href="/lisabona/populatie">Populatie</a><br>
    <a href="/lisabona/descriere">Descriere</a><br><br>
    <a href="/">Inapoi la pagina principala</a>
    </body></html>
    '''

@app.route('/orase')
def orase():
    return '''
    <html><body>
    <h1>Tema proiectului: Orase</h1>
    <p>Aceasta aplicatie prezinta informatii despre orase alese de studenti.</p>
    <ul><li><a href="/lisabona">Lisabona</a></li></ul>
    </body></html>
    '''

@app.route('/lisabona/populatie')
def lisabona_populatie():
    populatie = get_populatie_lisabona()
    return f'''
    <html><body>
    <h1>Populatia orasului Lisabona</h1>
    <p>{populatie} locuitori</p>
    <a href="/lisabona">Inapoi la Lisabona</a>
    </body></html>
    '''

@app.route('/lisabona/descriere')
def lisabona_descriere():
    descriere = get_descriere_lisabona()
    return f'''
    <html><body>
    <h1>Descriere Lisabona</h1>
    <p>{descriere}</p>
    <a href="/lisabona">Inapoi la Lisabona</a>
    </body></html>
    '''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=False)
