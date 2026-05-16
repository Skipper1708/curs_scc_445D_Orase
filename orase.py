.
from app.lib.biblioteca_orase import populatie_como, descriere_como

@app.route('/como')
def como():
    return '<h2>Como</h2><a href="/como/populatie">Populatie</a> | <a href="/como/descriere">Descriere</a>'

@app.route('/como/populatie')
def como_populatie():
    return populatie_como()

@app.route('/como/descriere')
def como_descriere():
    return descriere_como()
