import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.lib.biblioteca_orase import populatie_manchester, descriere_manchester

def test_populatie():
    rezultat = populatie_manchester()
    assert len(rezultat) > 0
    assert "Manchester" in rezultat

def test_descriere():
    rezultat = descriere_manchester()
    assert len(rezultat) > 0
    assert "Manchester" in rezultat
