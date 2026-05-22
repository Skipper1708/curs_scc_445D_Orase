from flask import Flask
from app.lib.biblioteca_orase import populatie_viena, descriere_viena

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Orase - 445D</title>
        <style>
            body { font-family: Arial; background: #1a1a2e; color: white; text-align: center; padding: 50px; }
            h1 { color: #e94560; font-size: 3em; }
            a { display: block; margin: 15px auto; padding: 15px 30px; background: #e94560; color: white; text-decoration: none; border-radius: 10px; width: 200px; font-size: 1.2em; }
            a:hover { background: #c73652; }
        </style>
    </head>
    <body>
        <h1>🌍 Orase - 445D</h1>
        <p>Student: Urmuz Laurentiu Ioan</p>
        <a href="/orase">Orase</a>
        <a href="/viena">Viena</a>
        <a href="/viena/populatie">Populatie Viena</a>
        <a href="/viena/descriere">Descriere Viena</a>
    </body>
    </html>
    '''

@app.route('/orase')
def orase():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Orase</title>
        <style>
            body { font-family: Arial; background: #1a1a2e; color: white; text-align: center; padding: 50px; }
            h1 { color: #e94560; }
            a { color: #e94560; font-size: 1.2em; }
        </style>
    </head>
    <body>
        <h1>🏙️ Tema: Orase</h1>
        <p>Student: Urmuz Laurentiu Ioan | Grupa: 445D</p>
        <p><a href="/viena">Vezi Viena</a></p>
        <p><a href="/">Inapoi</a></p>
    </body>
    </html>
    '''

@app.route('/viena')
def viena():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Viena</title>
        <style>
            body { font-family: Arial; background: #1a1a2e; color: white; text-align: center; padding: 50px; }
            h1 { color: #e94560; font-size: 2.5em; }
            a { display: block; margin: 10px auto; padding: 12px 25px; background: #e94560; color: white; text-decoration: none; border-radius: 8px; width: 180px; }
            a:hover { background: #c73652; }
        </style>
    </head>
    <body>
        <h1>🎭 Viena</h1>
        <p>Capitala Austriei</p>
        <a href="/viena/populatie">Populatie</a>
        <a href="/viena/descriere">Descriere</a>
        <a href="/">Inapoi</a>
    </body>
    </html>
    '''

@app.route('/viena/populatie')
def populatie_viena_route():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Populatie Viena</title>
        <style>
            body {{ font-family: Arial; background: #1a1a2e; color: white; text-align: center; padding: 50px; }}
            h1 {{ color: #e94560; }}
            p {{ font-size: 1.3em; }}
            a {{ color: #e94560; }}
        </style>
    </head>
    <body>
        <h1>👥 Populatia Vienei</h1>
        <p>{populatie_viena()}</p>
        <p><a href="/viena">Inapoi</a></p>
    </body>
    </html>
    '''

@app.route('/viena/descriere')
def descriere_viena_route():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Descriere Viena</title>
        <style>
            body {{ font-family: Arial; background: #1a1a2e; color: white; text-align: center; padding: 50px; }}
            h1 {{ color: #e94560; }}
            p {{ font-size: 1.3em; max-width: 600px; margin: auto; }}
            a {{ color: #e94560; }}
        </style>
    </head>
    <body>
        <h1>🏰 Descrierea Vienei</h1>
        <p>{descriere_viena()}</p>
        <p><a href="/viena">Inapoi</a></p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
