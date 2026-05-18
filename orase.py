from flask import Flask
from app.lib.biblioteca_orase import populatie_barcelona, descriere_barcelona

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <html>
    <head><title>Aplicatie Orase</title></head>
    <body>
        <h1>Aplicatie Web - Orase</h1>
        <p>Aceasta aplicatie prezinta informatii despre orase din lume.</p>
        <ul>
            <li><a href="/orase"><button>Orase</button></a></li>
        </ul>
    </body>
    </html>
    '''


@app.route('/orase')
def orase():
    return '''
    <html>
    <head><title>Orase</title></head>
    <body>
        <h1>Lista Orase</h1>
        <ul>
            <li><a href="/barcelona"><button>Barcelona</button></a></li>
        </ul>
        <br><a href="/">Inapoi</a>
    </body>
    </html>
    '''


@app.route('/barcelona')
def barcelona():
    return '''
    <html>
    <head><title>Barcelona</title></head>
    <body>
        <h1>Barcelona</h1>
        <p>Informatii despre Barcelona, Spania.</p>
        <ul>
            <li><a href="/barcelona/populatie"><button>Populatie</button></a></li>
            <li><a href="/barcelona/descriere"><button>Descriere</button></a></li>
        </ul>
        <br><a href="/orase">Inapoi</a>
    </body>
    </html>
    '''


@app.route('/barcelona/populatie')
def populatie():
    info = populatie_barcelona()
    return f'''
    <html>
    <head><title>Populatie Barcelona</title></head>
    <body>
        <h1>Populatia Barcelonei</h1>
        <p>{info}</p>
        <br><a href="/barcelona">Inapoi</a>
    </body>
    </html>
    '''


@app.route('/barcelona/descriere')
def descriere():
    info = descriere_barcelona()
    return f'''
    <html>
    <head><title>Descriere Barcelona</title></head>
    <body>
        <h1>Descrierea Barcelonei</h1>
        <p>{info}</p>
        <br><a href="/barcelona">Inapoi</a>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
