from flask import Blueprint
from app.lib.biblioteca_orase import descriere_paris, obiective_paris

paris_bp = Blueprint("paris", __name__)


@paris_bp.route("/orase")
def pagina_orase():
    return "Tema proiectului este Orase. Elementul implementat de Szabo Daria este Paris."


@paris_bp.route("/orase/paris")
def pagina_paris():
    return (
        "Paris este orasul ales pentru proiect. "
        "Rutele disponibile sunt: /orase/paris/descriere si /orase/paris/obiective."
    )


@paris_bp.route("/orase/paris/descriere")
def ruta_descriere_paris():
    return descriere_paris()


@paris_bp.route("/orase/paris/obiective")
def ruta_obiective_paris():
    return obiective_paris()
