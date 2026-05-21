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
        <li><a href="/populatie_viena">Populatie Viena</a></li>
        <li><a href="/descriere_viena">Descriere Viena</a></li>
    </ul>
    '''

@app.route('/orase')
def orase():
    return '<h2>Tema: Orase</h2><p>Student: Urmuz Laurentiu Ioan</p><p><a href="/viena">Vezi Viena</a></p>'

@app.route('/viena')
def viena():
    return '<h2>Viena</h2><p>Populatie: <a href="/populatie_viena">click</a></p><p>Descriere: <a href="/descriere_viena">click</a></p>'

@app.route('/populatie_viena')
def populatie_viena_route():
    return f'<h2>Populatia Vienei</h2><p>{populatie_viena()}</p>'

@app.route('/descriere_viena')
def descriere_viena_route():
    return f'<h2>Descrierea Vienei</h2><p>{descriere_viena()}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
