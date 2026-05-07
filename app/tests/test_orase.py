from orase import app
from app.lib.biblioteca_orase import populatie_reykjavik, descriere_reykjavik

def test_functie_populatie():
    rezultat = populatie_reykjavik()
    assert "Reykjavik" in rezultat
    assert "locuitori" in rezultat

def test_functie_descriere():
    rezultat = descriere_reykjavik()
    assert "capitala Islandei" in rezultat

def test_ruta_index():
    client = app.test_client()
    raspuns = client.get("/")
    assert raspuns.status_code == 200
    assert b"Ora" in raspuns.data or b"Reykjavik" in raspuns.data

def test_ruta_orase():
    client = app.test_client()
    raspuns = client.get("/orase")
    assert raspuns.status_code == 200
    assert b"Reykjavik" in raspuns.data

def test_ruta_reykjavik():
    client = app.test_client()
    raspuns = client.get("/orase/reykjavik")
    assert raspuns.status_code == 200
    assert b"Reykjavik" in raspuns.data

def test_ruta_populatie():
    client = app.test_client()
    raspuns = client.get("/orase/reykjavik/populatie")
    assert raspuns.status_code == 200
    assert b"Reykjavik" in raspuns.data

def test_ruta_descriere():
    client = app.test_client()
    raspuns = client.get("/orase/reykjavik/descriere")
    assert raspuns.status_code == 200
    assert b"Islandei" in raspuns.data or b"Reykjavik" in raspuns.data
