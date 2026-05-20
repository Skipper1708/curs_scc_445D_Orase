from flask import Flask
from app.lib.biblioteca_orase import populatie_manchester, descriere_manchester

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Aplicatie Orase - SCC 445D</h1><p><a href="/orase">Lista orase</a></p>'

@app.route('/orase')
def orase():
    return '<h1>Orase disponibile</h1><ul><li><a href="/manchester">Manchester</a></li></ul>'

@app.route('/manchester')
def manchester():
    return '<h1>Manchester</h1><ul><li><a href="/manchester/populatie">Populatie</a></li><li><a href="/manchester/descriere">Descriere</a></li></ul>'

@app.route('/manchester/populatie')
def manchester_populatie():
    return populatie_manchester()

@app.route('/manchester/descriere')
def manchester_descriere():
    return descriere_manchester()