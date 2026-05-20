from flask import Flask, render_template
from app.lib.biblioteca_orase import populatie_manchester, descriere_manchester

app = Flask(__name__, template_folder='app/templates')

@app.route('/')
def home():
    return render_template('index.html', sectiune='home')

@app.route('/descriere')
def descriere():
    date = descriere_manchester()
    return render_template('index.html', sectiune='descriere', date_ruta=date)

@app.route('/populatie')
def populatie():
    date = populatie_manchester()
    return render_template('index.html', sectiune='populatie', date_ruta=date)

@app.route('/monumente')
def monumente():
    # Dacă ai o funcție pentru monumente în bibliotecă o poți apela aici,
    # altfel lăsăm un text static placeholder.
    date = "Old Trafford, Etihad Stadium, Science and Industry Museum, Manchester Cathedral."
    return render_template('index.html', sectiune='monumente', date_ruta=date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011)