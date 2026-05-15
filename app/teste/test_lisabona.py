import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.lib.biblioteca_orase import get_populatie_lisabona, get_descriere_lisabona

def test_populatie_tip():
    rezultat = get_populatie_lisabona()
    assert isinstance(rezultat, int)

def test_populatie_valoare():
    rezultat = get_populatie_lisabona()
    assert rezultat > 0

def test_descriere_tip():
    rezultat = get_descriere_lisabona()
    assert isinstance(rezultat, str)

def test_descriere_continut():
    rezultat = get_descriere_lisabona()
    assert "Lisabona" in rezultat
