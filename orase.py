from flask import Flask
from app.lib.biblioteca_orase import descriere_bucuresti, populatie_bucuresti

app = Flask(__name__)


def layout(title, content):
    return f"""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                color: #1f2937;
            }}

            header {{
                background: linear-gradient(135deg, #1e3a8a, #2563eb);
                color: white;
                padding: 40px 20px;
                text-align: center;
            }}

            header h1 {{
                margin: 0;
                font-size: 42px;
            }}

            header p {{
                margin-top: 10px;
                font-size: 18px;
                opacity: 0.9;
            }}

            main {{
                max-width: 900px;
                margin: 40px auto;
                padding: 0 20px;
            }}

            .card {{
                background: white;
                border-radius: 16px;
                padding: 28px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
                margin-bottom: 24px;
            }}

            .card h2 {{
                margin-top: 0;
                color: #1e3a8a;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 16px;
                margin-top: 20px;
            }}

            .button {{
                display: block;
                text-decoration: none;
                color: white;
                background: #2563eb;
                padding: 14px 18px;
                border-radius: 12px;
                text-align: center;
                font-weight: bold;
                transition: 0.2s ease;
            }}

            .button:hover {{
                background: #1e40af;
                transform: translateY(-2px);
            }}

            .back {{
                display: inline-block;
                margin-top: 20px;
                color: #2563eb;
                text-decoration: none;
                font-weight: bold;
            }}

            footer {{
                text-align: center;
                color: #6b7280;
                padding: 20px;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Proiect SCC - Orașe</h1>
            <p>Student: Paunoiu Ianis | Oraș ales: București</p>
        </header>

        <main>
            {content}
        </main>

        <footer>
            Servicii Cloud și Containerizare - 445D
        </footer>
    </body>
    </html>
    """


@app.route("/", methods=["GET"])
def index():
    content = """
    <section class="card">
        <h2>Aplicație Flask pentru tema Orașe</h2>
        <p>
            Această aplicație prezintă informații despre orașul București.
            Proiectul folosește Git, GitHub, Jenkins și Docker.
        </p>

        <div class="grid">
            <a class="button" href="/orase">Tema: Orașe</a>
            <a class="button" href="/orase/bucuresti">Oraș: București</a>
            <a class="button" href="/orase/bucuresti/descriere">Descriere București</a>
            <a class="button" href="/orase/bucuresti/populatie">Populație București</a>
        </div>
    </section>
    """
    return layout("Proiect SCC - Orașe", content)


@app.route("/orase", methods=["GET"])
def tema_orase():
    content = """
    <section class="card">
        <h2>Tema: Orașe</h2>
        <p>
            Tema proiectului este dezvoltarea unei aplicații web simple
            care permite afișarea unor informații despre orașe.
        </p>
        <p>
            În cadrul contribuției individuale, orașul ales este București.
        </p>
        <a class="back" href="/">Înapoi la pagina principală</a>
    </section>
    """
    return layout("Tema Orașe", content)


@app.route("/orase/bucuresti", methods=["GET"])
def oras_bucuresti():
    content = """
    <section class="card">
        <h2>București</h2>
        <p>
            București este orașul ales pentru implementarea funcționalității individuale.
            Aplicația oferă două informații principale: descriere și populație.
        </p>

        <div class="grid">
            <a class="button" href="/orase/bucuresti/descriere">Vezi descrierea</a>
            <a class="button" href="/orase/bucuresti/populatie">Vezi populația</a>
        </div>

        <a class="back" href="/">Înapoi la pagina principală</a>
    </section>
    """
    return layout("București", content)


@app.route("/orase/bucuresti/descriere", methods=["GET"])
def ruta_descriere_bucuresti():
    content = f"""
    <section class="card">
        <h2>Descriere București</h2>
        <p>{descriere_bucuresti()}</p>
        <a class="back" href="/orase/bucuresti">Înapoi la București</a>
    </section>
    """
    return layout("Descriere București", content)


@app.route("/orase/bucuresti/populatie", methods=["GET"])
def ruta_populatie_bucuresti():
    content = f"""
    <section class="card">
        <h2>Populație București</h2>
        <p>{populatie_bucuresti()}</p>
        <a class="back" href="/orase/bucuresti">Înapoi la București</a>
    </section>
    """
    return layout("Populație București", content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
