import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.lib.biblioteca_orase import populatie_sarajevo, descriere_sarajevo

def test_populatie():
    rezultat = populatie_sarajevo()
    assert len(rezultat) > 0
    assert "Sarajevo" in rezultat

def test_descriere():
    rezultat = descriere_sarajevo()
    assert len(rezultat) > 0
    assert "Sarajevo" in rezultat
