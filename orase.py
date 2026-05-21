from flask import Flask
from app.lib.biblioteca_orase import populatie_viena, descriere_viena

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Aplicatie Orase - 445D</h1>
    <ul>
        <li><a href="/orase">Orase</a></li>
        <li><a href="/viena">Viena</a></li>
        <li><a href="/viena/populatie">Populatie Viena</a></li>
        <li><a href="/viena/descriere">Descriere Viena</a></li>
    </ul>
    '''

@app.route('/orase')
def orase():
    return '<h2>Tema: Orase</h2><p>Student: Urmuz Laurentiu Ioan</p><p><a href="/viena">Vezi Viena</a></p>'

@app.route('/viena')
def viena():
    return '<h2>Viena</h2><p>Populatie: <a href="/viena/populatie">click</a></p><p>Descriere: <a href="/viena/descriere">click</a></p>'

@app.route('/viena/populatie')
def populatie_viena_route():
    return f'<h2>Populatia Vienei</h2><p>{populatie_viena()}</p>'

@app.route('/viena/descriere')
def descriere_viena_route():
    return f'<h2>Descrierea Vienei</h2><p>{descriere_viena()}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
