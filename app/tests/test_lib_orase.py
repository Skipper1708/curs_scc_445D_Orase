import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.lib.biblioteca_orase import populatie_viena, descriere_viena

def test_populatie():
    rezultat = populatie_viena()
    assert len(rezultat) > 0
    assert "Viena" in rezultat

def test_descriere():
    rezultat = descriere_viena()
    assert len(rezultat) > 0
    assert "Viena" in rezultat
