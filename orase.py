from flask import Flask
from app.lib.biblioteca_orase import descriere_bucuresti, populatie_bucuresti

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return """
    <h1>Proiect SCC - Orașe</h1>
    <p>Student: Paunoiu Ianis</p>
    <p>Oraș ales: București</p>
    <ul>
        <li><a href="/orase">Tema: Orașe</a></li>
        <li><a href="/orase/bucuresti">București</a></li>
        <li><a href="/orase/bucuresti/descriere">Descriere București</a></li>
        <li><a href="/orase/bucuresti/populatie">Populație București</a></li>
    </ul>
    """


@app.route("/orase", methods=["GET"])
def tema_orase():
    return """
    <h1>Orașe</h1>
    <p>Această aplicație prezintă informații despre orașe.</p>
    <a href="/">Înapoi la pagina principală</a>
    """


@app.route("/orase/bucuresti", methods=["GET"])
def oras_bucuresti():
    return """
    <h1>București</h1>
    <p>Informații disponibile:</p>
    <ul>
        <li><a href="/orase/bucuresti/descriere">Descriere</a></li>
        <li><a href="/orase/bucuresti/populatie">Populație</a></li>
    </ul>
    <a href="/">Înapoi la pagina principală</a>
    """


@app.route("/orase/bucuresti/descriere", methods=["GET"])
def ruta_descriere_bucuresti():
    return f"""
    <h1>Descriere București</h1>
    <p>{descriere_bucuresti()}</p>
    <a href="/">Înapoi la pagina principală</a>
    """


@app.route("/orase/bucuresti/populatie", methods=["GET"])
def ruta_populatie_bucuresti():
    return f"""
    <h1>Populație București</h1>
    <p>{populatie_bucuresti()}</p>
    <a href="/">Înapoi la pagina principală</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
