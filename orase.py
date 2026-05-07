from flask import Flask
from app.lib.biblioteca_orase import populatie_reykjavik, descriere_reykjavik

app = Flask(__name__)

def pagina_html(titlu, continut):
    return f"""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #e0f2fe, #f8fafc);
                color: #1e293b;
            }}
            header {{
                background: #0f172a;
                color: white;
                padding: 30px 20px;
                text-align: center;
            }}
            .container {{
                max-width: 1000px;
                margin: 30px auto;
                background: white;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            }}
            h1, h2, h3 {{
                color: #0f172a;
            }}
            p {{
                line-height: 1.7;
                font-size: 17px;
            }}
            .buttons {{
                margin-top: 20px;
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
            }}
            .btn {{
                display: inline-block;
                padding: 12px 18px;
                background: #2563eb;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-weight: bold;
            }}
            .btn:hover {{
                background: #1d4ed8;
            }}
            .card {{
                background: #f8fafc;
                border-left: 6px solid #2563eb;
                padding: 18px;
                border-radius: 10px;
                margin: 20px 0;
            }}
            ul {{
                line-height: 1.8;
            }}
            footer {{
                text-align: center;
                padding: 20px;
                color: #475569;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>{titlu}</h1>
        </header>
        <div class="container">
            {continut}
        </div>
        <footer>
            Proiect SCC - Tema Orașe - Ruxandra Apostol - Reykjavik
        </footer>
    </body>
    </html>
    """

@app.route("/")
def index():
    continut = """
    <h2>Bine ai venit!</h2>
    <p>
        Aceasta este o aplicație web realizată în Flask pentru tema <strong>Orașe</strong>.
        Orașul ales pentru această funcționalitate este <strong>Reykjavik</strong>.
    </p>

    <div class="card">
        <p>
            În această aplicație poți vedea informații generale despre Reykjavik,
            populația orașului și o descriere amplă a acestuia, împreună cu atracții turistice.
        </p>
    </div>

    <div class="buttons">
        <a class="btn" href="/orase">Tema: Orașe</a>
        <a class="btn" href="/orase/reykjavik">Pagina orașului Reykjavik</a>
        <a class="btn" href="/orase/reykjavik/populatie">Populația Reykjavik</a>
        <a class="btn" href="/orase/reykjavik/descriere">Descriere Reykjavik</a>
    </div>
    """
    return pagina_html("Aplicație web - Orașe", continut)

@app.route("/orase")
def pagina_orase():
    continut = """
    <h2>Tema proiectului: Orașe</h2>
    <p>
        Tema acestui proiect este reprezentată de orașe, iar în această implementare
        a fost ales orașul <strong>Reykjavik</strong>.
    </p>

    <div class="card">
        <h3>De ce Reykjavik?</h3>
        <p>
            Reykjavik este un oraș interesant datorită poziției sale geografice,
            culturii nordice, energiei geotermale și apropierii de peisaje naturale spectaculoase.
        </p>
    </div>

    <ul>
        <li>Țara: Islanda</li>
        <li>Rol: capitală și cel mai mare oraș al țării</li>
        <li>Caracteristici: climă rece, cultură nordică, peisaje vulcanice</li>
    </ul>

    <div class="buttons">
        <a class="btn" href="/">Pagina principală</a>
        <a class="btn" href="/orase/reykjavik">Pagina orașului Reykjavik</a>
        <a class="btn" href="/orase/reykjavik/populatie">Populația Reykjavik</a>
        <a class="btn" href="/orase/reykjavik/descriere">Descriere Reykjavik</a>
    </div>
    """
    return pagina_html("Tema proiectului: Orașe", continut)

@app.route("/orase/reykjavik")
def pagina_reykjavik():
    continut = """
    <h2>Reykjavik</h2>
    <p>
        Reykjavik este capitala Islandei și cel mai important centru urban al țării.
        Orașul este cunoscut pentru combinația dintre modernitate și natură,
        pentru energia geotermală și pentru stilul de viață nordic.
    </p>

    <div class="card">
        <h3>Informații generale</h3>
        <ul>
            <li>Este capitala Islandei</li>
            <li>Este cel mai mare oraș din țară</li>
            <li>Are o cultură urbană modernă, dar este aproape de natură</li>
            <li>Este renumit pentru energia geotermală</li>
            <li>Este un punct important pentru explorarea Islandei</li>
        </ul>
    </div>

    <div class="card">
        <h3>Atracții și particularități</h3>
        <ul>
            <li>Biserica Hallgrímskirkja</li>
            <li>Sala de concerte Harpa</li>
            <li>Portul vechi și viața culturală locală</li>
            <li>Peisaje vulcanice și izvoare termale în apropiere</li>
            <li>Aurora boreală poate fi observată în anumite perioade</li>
        </ul>
    </div>

    <div class="buttons">
        <a class="btn" href="/">Pagina principală</a>
        <a class="btn" href="/orase">Înapoi la tema Orașe</a>
        <a class="btn" href="/orase/reykjavik/populatie">Vezi populația</a>
        <a class="btn" href="/orase/reykjavik/descriere">Vezi descrierea</a>
    </div>
    """
    return pagina_html("Orașul Reykjavik", continut)

@app.route("/orase/reykjavik/populatie")
def pagina_populatie_reykjavik():
    continut = f"""
    <h2>Populația orașului Reykjavik</h2>

    <div class="card">
        <p>{populatie_reykjavik()}</p>
    </div>

    <div class="card">
        <h3>Importanța populației Reykjavikului</h3>
        <p>
            Reykjavik este centrul principal al vieții urbane din Islanda.
            O mare parte din populația țării trăiește în capitală sau în zona metropolitană
            din jurul acesteia, ceea ce face ca orașul să aibă un rol foarte important
            în organizarea economică, socială și culturală a statului islandez.
        </p>
    </div>

    <div class="card">
        <h3>De ce este important acest oraș?</h3>
        <ul>
            <li>este capitala Islandei</li>
            <li>este cel mai mare oraș din țară</li>
            <li>este principalul centru administrativ</li>
            <li>are un rol important în economie și educație</li>
            <li>concentrează activități culturale, turistice și comerciale</li>
        </ul>
    </div>

    <div class="card">
        <h3>Observații</h3>
        <p>
            Chiar dacă Reykjavik nu este un oraș foarte mare comparativ cu alte capitale europene,
            el este extrem de important pentru Islanda. Orașul are o densitate urbană bine organizată,
            un nivel ridicat de trai și o infrastructură modernă, fiind centrul principal al vieții
            publice din țară.
        </p>
    </div>

    <div class="buttons">
        <a class="btn" href="/">Pagina principală</a>
        <a class="btn" href="/orase">Tema Orașe</a>
        <a class="btn" href="/orase/reykjavik">Pagina orașului Reykjavik</a>
        <a class="btn" href="/orase/reykjavik/descriere">Descriere Reykjavik</a>
    </div>
    """
    return pagina_html("Populația orașului Reykjavik", continut)

@app.route("/orase/reykjavik/descriere")
def pagina_descriere_reykjavik():
    continut = f"""
    <h2>Descriere completă a orașului Reykjavik</h2>

    <div class="card">
        <p>{descriere_reykjavik()}</p>
    </div>

    <div class="card">
        <h3>Informații generale</h3>
        <ul>
            <li>Reykjavik este capitala Islandei.</li>
            <li>Este cel mai mare oraș din țară.</li>
            <li>Este una dintre cele mai nordice capitale ale lumii.</li>
            <li>Este centrul administrativ, economic și cultural al Islandei.</li>
            <li>Orașul este renumit pentru utilizarea energiei geotermale.</li>
        </ul>
    </div>

    <div class="card">
        <h3>Ce face Reykjavik special?</h3>
        <p>
            Reykjavik se remarcă prin atmosfera sa liniștită, curățenie, siguranță
            și stilul de viață nordic. Orașul are clădiri moderne, străzi pline
            de culoare, cafenele primitoare, artă urbană, muzee interesante și
            o viață culturală foarte activă. În același timp, în jurul orașului
            se găsesc peisaje naturale spectaculoase, ceea ce îl face o destinație
            foarte apreciată de turiști.
        </p>
    </div>

    <div class="card">
        <h3>Atracții turistice importante</h3>
        <ul>
            <li><strong>Hallgrímskirkja</strong> – una dintre cele mai cunoscute biserici din Islanda și un simbol al orașului.</li>
            <li><strong>Harpa Concert Hall</strong> – sală de concerte modernă, celebră pentru designul său spectaculos.</li>
            <li><strong>Sun Voyager</strong> – sculptură faimoasă aflată pe malul mării, foarte fotografiată de turiști.</li>
            <li><strong>Perlan</strong> – clădire modernă cu muzeu, expoziții și punct panoramic asupra orașului.</li>
            <li><strong>Portul vechi</strong> – zonă plăcută pentru plimbări, restaurante și excursii pe mare.</li>
            <li><strong>Laugavegur</strong> – una dintre cele mai populare străzi, plină de magazine, cafenele și restaurante.</li>
            <li><strong>Muzeul Național al Islandei</strong> – loc bun pentru a descoperi istoria și cultura islandeză.</li>
            <li><strong>Aurora boreală</strong> – în anumite perioade ale anului poate fi observată în apropierea orașului.</li>
        </ul>
    </div>

    <div class="card">
        <h3>Lucruri interesante pe care le poți face în Reykjavik</h3>
        <ul>
            <li>Să faci o plimbare prin centrul vechi al orașului.</li>
            <li>Să vizitezi muzeele și galeriile de artă.</li>
            <li>Să admiri panorama orașului din turnul bisericii Hallgrímskirkja.</li>
            <li>Să participi la excursii pentru observarea balenelor.</li>
            <li>Să explorezi zona portului și restaurantele locale.</li>
            <li>Să încerci băi termale și experiențe geotermale.</li>
            <li>Să faci excursii spre obiective naturale aflate aproape de oraș.</li>
        </ul>
    </div>

    <div class="card">
        <h3>Curiozități despre Reykjavik</h3>
        <ul>
            <li>Numele „Reykjavik” înseamnă aproximativ „Golful fumului”.</li>
            <li>Orașul este cunoscut pentru utilizarea energiei regenerabile.</li>
            <li>Are o populație relativ mică în comparație cu alte capitale europene.</li>
            <li>Este considerat un oraș foarte sigur și bine organizat.</li>
            <li>Este un punct de plecare ideal pentru explorarea Islandei.</li>
        </ul>
    </div>

    <div class="buttons">
        <a class="btn" href="/">Pagina principală</a>
        <a class="btn" href="/orase">Tema Orașe</a>
        <a class="btn" href="/orase/reykjavik">Pagina orașului Reykjavik</a>
        <a class="btn" href="/orase/reykjavik/populatie">Populația Reykjavik</a>
    </div>
    """
    return pagina_html("Descrierea orașului Reykjavik", continut)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
