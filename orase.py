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
    <a href="/">Inapoi la pagina principala</a>
    </body></html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=False).
