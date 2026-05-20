from flask import Flask
from app.lib.biblioteca_orase import populatie_sarajevo, descriere_sarajevo

app = Flask(__name__)

@app.route('/')
def home():
    return 'Aplicatie Flask - Orase. Disponibil: /orase, /sarajevo, /sarajevo/populatie, /sarajevo/descriere'

@app.route('/orase')
def orase():
    return 'Orase disponibile: sarajevo'

@app.route('/sarajevo')
def sarajevo():
    return 'Sarajevo - capitala Bosniei si Hertegovina'

@app.route('/sarajevo/populatie')
def populatie():
    return populatie_sarajevo()

@app.route('/sarajevo/descriere')
def descriere():
    return descriere_sarajevo()
