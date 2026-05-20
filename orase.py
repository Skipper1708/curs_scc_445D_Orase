from flask import Flask, render_template
from app.lib.biblioteca_orase import populatie_manchester, descriere_manchester

app = Flask(__name__, template_folder='app/templates') # Îi spunem exact unde e folderul

@app.route('/')
def home():
    descriere = descriere_manchester()
    populatie = populatie_manchester()
    return render_template('index.html', descriere=descriere, populatie=populatie)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011)