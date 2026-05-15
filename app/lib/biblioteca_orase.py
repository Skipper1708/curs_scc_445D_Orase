def descriere_paris() -> str:
    return """
    <html>
    <head>
        <title>Descriere Paris</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f5efe6;
                color: #1f2937;
            }

            .page {
                max-width: 1100px;
                margin: 0 auto;
                padding: 40px 24px;
            }

            .nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 30px;
            }

            .nav a {
                color: #1d4ed8;
                text-decoration: none;
                font-weight: bold;
                margin-left: 18px;
            }

            .hero {
                background: #ffffff;
                border-radius: 20px;
                padding: 36px;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
                border-top: 6px solid #1d4ed8;
            }

            .hero h1 {
                margin-top: 0;
                font-size: 36px;
                color: #111827;
            }

            .subtitle {
                font-size: 18px;
                line-height: 1.7;
                color: #374151;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
                margin-top: 28px;
            }

            .info-box {
                background: #fff7ed;
                padding: 20px;
                border-radius: 16px;
                border: 1px solid #fed7aa;
            }

            .info-box h3 {
                margin-top: 0;
                color: #9a3412;
            }

            .section {
                margin-top: 28px;
                background: #ffffff;
                border-radius: 18px;
                padding: 28px;
                box-shadow: 0 6px 18px rgba(0, 0, 0, 0.06);
            }

            .section h2 {
                margin-top: 0;
                color: #1d4ed8;
            }

            .tags {
                margin-top: 16px;
            }

            .tag {
                display: inline-block;
                background: #dbeafe;
                color: #1e40af;
                padding: 8px 12px;
                border-radius: 999px;
                margin: 5px;
                font-size: 14px;
                font-weight: bold;
            }

            @media (max-width: 800px) {
                .grid {
                    grid-template-columns: 1fr;
                }

                .nav {
                    flex-direction: column;
                    align-items: flex-start;
                }

                .nav a {
                    margin-left: 0;
                    margin-right: 14px;
                }
            }
        </style>
    </head>

    <body>
        <div class="page">
            <div class="nav">
                <strong>Orase / Paris</strong>
                <div>
                    <a href="/orase">Tema Orase</a>
                    <a href="/orase/paris">Paris</a>
                    <a href="/orase/paris/obiective">Obiective</a>
                </div>
            </div>

            <div class="hero">
                <h1>Paris — orașul artei, modei și culturii</h1>
                <p class="subtitle">
                    Paris este capitala Frantei si unul dintre cele mai cunoscute orase din Europa.
                    Orasul este asezat pe raul Sena si este recunoscut pentru arhitectura eleganta,
                    muzeele importante, gastronomia, moda si atmosfera urbana.
                </p>

                <div class="grid">
                    <div class="info-box">
                        <h3>Tara</h3>
                        <p>Franta</p>
                    </div>
                    <div class="info-box">
                        <h3>Rau</h3>
                        <p>Sena</p>
                    </div>
                    <div class="info-box">
                        <h3>Cunoscut pentru</h3>
                        <p>arta, moda, gastronomie si turism</p>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2>Rolul orașului</h2>
                <p>
                    Parisul este un centru important pentru cultura, educatie, economie si turism.
                    Orasul atrage anual foarte multi vizitatori datorita monumentelor sale,
                    muzeelor renumite, bulevardelor, cafenelelor si cartierelor istorice.
                </p>
            </div>

            <div class="section">
                <h2>Ce face Parisul special?</h2>
                <p>
                    Parisul imbina zone istorice, cladiri emblematice si o viata urbana activa.
                    Este apreciat pentru patrimoniul cultural, pentru atmosfera sa si pentru modul
                    in care combina arta, arhitectura, moda si gastronomie.
                </p>

                <div class="tags">
                    <span class="tag">arta</span>
                    <span class="tag">arhitectura</span>
                    <span class="tag">muzee</span>
                    <span class="tag">moda</span>
                    <span class="tag">gastronomie</span>
                    <span class="tag">turism</span>
                </div>
            </div>
        </div>
    </body>
    </html>
    """


def obiective_paris() -> str:
    return """
    <html>
    <head>
        <title>Obiective Paris</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #eef2ff;
                color: #1f2937;
            }

            .page {
                max-width: 1100px;
                margin: 0 auto;
                padding: 40px 24px;
            }

            .nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 30px;
            }

            .nav a {
                color: #1d4ed8;
                text-decoration: none;
                font-weight: bold;
                margin-left: 18px;
            }

            .header {
                background: #1e3a8a;
                color: white;
                padding: 34px;
                border-radius: 20px;
                margin-bottom: 28px;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
            }

            .header h1 {
                margin-top: 0;
                font-size: 36px;
            }

            .header p {
                font-size: 17px;
                line-height: 1.6;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
            }

            .category {
                background: white;
                border-radius: 18px;
                padding: 24px;
                box-shadow: 0 6px 18px rgba(0, 0, 0, 0.07);
                border-bottom: 5px solid #2563eb;
            }

            .category h2 {
                margin-top: 0;
                color: #1d4ed8;
            }

            .category ul {
                padding-left: 20px;
                line-height: 1.8;
            }

            .experience {
                margin-top: 24px;
                background: #ffffff;
                border-radius: 18px;
                padding: 28px;
                box-shadow: 0 6px 18px rgba(0, 0, 0, 0.07);
            }

            .experience h2 {
                color: #1d4ed8;
                margin-top: 0;
            }

            .badge {
                display: inline-block;
                background: #fef3c7;
                color: #92400e;
                padding: 8px 12px;
                border-radius: 999px;
                margin: 5px;
                font-weight: bold;
                font-size: 14px;
            }

            @media (max-width: 800px) {
                .grid {
                    grid-template-columns: 1fr;
                }

                .nav {
                    flex-direction: column;
                    align-items: flex-start;
                }

                .nav a {
                    margin-left: 0;
                    margin-right: 14px;
                }
            }
        </style>
    </head>

    <body>
        <div class="page">
            <div class="nav">
                <strong>Orase / Paris</strong>
                <div>
                    <a href="/orase">Tema Orase</a>
                    <a href="/orase/paris">Paris</a>
                    <a href="/orase/paris/descriere">Descriere</a>
                </div>
            </div>

            <div class="header">
                <h1>Obiective turistice din Paris</h1>
                <p>
                    Parisul este vizitat pentru monumentele sale, muzeele de renume international,
                    cartierele istorice si experientele urbane specifice capitalei Frantei.
                </p>
            </div>

            <div class="grid">
                <div class="category">
                    <h2>Monumente si simboluri</h2>
                    <ul>
                        <li>Turnul Eiffel</li>
                        <li>Arcul de Triumf</li>
                        <li>Catedrala Notre-Dame</li>
                        <li>Basilica Sacre-Coeur</li>
                    </ul>
                </div>

                <div class="category">
                    <h2>Muzee si cultura</h2>
                    <ul>
                        <li>Muzeul Luvru</li>
                        <li>Muzeul Orsay</li>
                        <li>Centrul Pompidou</li>
                        <li>Opera Garnier</li>
                    </ul>
                </div>

                <div class="category">
                    <h2>Zone cunoscute</h2>
                    <ul>
                        <li>Champs-Elysees</li>
                        <li>Montmartre</li>
                        <li>Cartierul Latin</li>
                        <li>Gradina Luxemburg</li>
                    </ul>
                </div>

                <div class="category">
                    <h2>Experiente recomandate</h2>
                    <ul>
                        <li>plimbare pe malul Senei</li>
                        <li>vizitarea muzeelor</li>
                        <li>explorarea cartierelor istorice</li>
                        <li>vedere panoramica de la Turnul Eiffel sau Sacre-Coeur</li>
                    </ul>
                </div>
            </div>

            <div class="experience">
                <h2>Paris in cateva cuvinte</h2>
                <span class="badge">istorie</span>
                <span class="badge">arta</span>
                <span class="badge">muzee</span>
                <span class="badge">monumente</span>
                <span class="badge">cafenele</span>
                <span class="badge">Sena</span>
                <span class="badge">turism</span>
            </div>
        </div>
    </body>
    </html>
    """
