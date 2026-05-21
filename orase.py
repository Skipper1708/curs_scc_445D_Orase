from flask import Flask
from app.lib.biblioteca_orase import populatie_varsovia, descriere_varsovia

app = Flask(__name__)

@app.route('/')
def home():
    return "Aplicatie Flask - Orase. Accesati /orase pentru lista oraselor disponibile."

@app.route('/orase')
def orase():
    return "Orase disponibile: <a href='/varsovia'>Varsovia</a>"

@app.route('/varsovia')
def varsovia():
    return "Varsovia - capitala Poloniei. Accesati /varsovia/populatie sau /varsovia/descriere."

@app.route('/varsovia/populatie')
def varsovia_populatie():
    return populatie_varsovia()

@app.route('/varsovia/descriere')
def varsovia_descriere():
    return descriere_varsovia()
