from flask import Blueprint
from app.lib.biblioteca_orase import descriere_paris, obiective_paris

paris_bp = Blueprint("paris", __name__)


@paris_bp.route("/orase")
def pagina_orase():
    return """
    <html>
    <head>
        <title>Tema Orase</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f5efe6;
                color: #1f2937;
            }

            .page {
                max-width: 1000px;
                margin: 0 auto;
                padding: 50px 24px;
            }

            .box {
                background: white;
                border-radius: 20px;
                padding: 36px;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
            }

            h1 {
                color: #1d4ed8;
                margin-top: 0;
            }

            p {
                font-size: 17px;
                line-height: 1.7;
            }

            a {
                display: inline-block;
                margin-top: 18px;
                background: #1d4ed8;
                color: white;
                padding: 12px 18px;
                border-radius: 999px;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="page">
            <div class="box">
                <h1>Tema proiectului: Orase</h1>
                <p>
                    Aceasta aplicatie Flask permite fiecarui student sa adauge
                    propria functionalitate pentru un oras ales.
                </p>
                <p>
                    Elementul implementat de Szabo Daria Ioana este orasul Paris.
                </p>
                <a href="/orase/paris">Deschide pagina orasului Paris</a>
            </div>
        </div>
    </body>
    </html>
    """


@paris_bp.route("/orase/paris")
def pagina_paris():
    return """
    <html>
    <head>
        <title>Orasul Paris</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #eef2ff, #fdf2f8);
                color: #1f2937;
            }

            .page {
                max-width: 1100px;
                margin: 0 auto;
                padding: 45px 24px;
            }

            .hero {
                background: white;
                padding: 38px;
                border-radius: 24px;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
                margin-bottom: 24px;
            }

            .hero h1 {
                margin-top: 0;
                font-size: 38px;
                color: #1d4ed8;
            }

            .hero p {
                font-size: 18px;
                line-height: 1.7;
                color: #374151;
            }

            .actions {
                margin-top: 24px;
            }

            .actions a {
                display: inline-block;
                margin-right: 12px;
                margin-bottom: 12px;
                background: #1d4ed8;
                color: white;
                padding: 12px 18px;
                border-radius: 999px;
                text-decoration: none;
                font-weight: bold;
            }

            .actions a.secondary {
                background: #be123c;
            }

            .quick-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
            }

            .quick-card {
                background: white;
                border-radius: 18px;
                padding: 22px;
                box-shadow: 0 6px 18px rgba(0, 0, 0, 0.07);
            }

            .quick-card h3 {
                margin-top: 0;
                color: #be123c;
            }

            @media (max-width: 800px) {
                .quick-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>

    <body>
        <div class="page">
            <div class="hero">
                <h1>Paris — orasul ales pentru proiect</h1>
                <p>
                    Paris este functionalitatea implementata in cadrul temei Orase.
                    Pagina prezinta informatii generale despre oras si obiective turistice importante.
                </p>

                <div class="actions">
                    <a href="/orase/paris/descriere">Descriere Paris</a>
                    <a href="/orase/paris/obiective" class="secondary">Obiective turistice</a>
                    <a href="/orase">Inapoi la Orase</a>
                </div>
            </div>

            <div class="quick-grid">
                <div class="quick-card">
                    <h3>Capitala</h3>
                    <p>Paris este capitala Frantei.</p>
                </div>

                <div class="quick-card">
                    <h3>Localizare</h3>
                    <p>Orasul este asezat pe raul Sena.</p>
                </div>

                <div class="quick-card">
                    <h3>Imagine urbana</h3>
                    <p>Este cunoscut pentru arta, moda, arhitectura, muzee si gastronomie.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """


@paris_bp.route("/orase/paris/descriere")
def ruta_descriere_paris():
    return descriere_paris()


@paris_bp.route("/orase/paris/obiective")
def ruta_obiective_paris():
    return obiective_paris()
