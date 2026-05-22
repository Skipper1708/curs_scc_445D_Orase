import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.lib.biblioteca_orase import populatie_varsovia, descriere_varsovia

def test_populatie():
    rezultat = populatie_varsovia()
    assert len(rezultat) > 0
    assert "Varsovia" in rezultat

def test_descriere():
    rezultat = descriere_varsovia()
    assert len(rezultat) > 0
    assert "Varsovia" in rezultat
