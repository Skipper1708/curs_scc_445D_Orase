from flask import Flask
from app.lib.biblioteca_orase import populatie_como, descriere_como

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Aplicatie Orase</h1><br><a href="/orase">Vezi orase</a>'

@app.route('/orase')
def orase():
    return '<h1>Orase disponibile</h1><br><a href="/como">Como</a>'

@app.route('/como')
def como():
    return '<h2>Como</h2><a href="/como/populatie">Populatie</a> | <a href="/como/descriere">Descriere</a>'

@app.route('/como/populatie')
def como_populatie():
    return populatie_como()

@app.route('/como/descriere')
def como_descriere():
    return descriere_como()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
