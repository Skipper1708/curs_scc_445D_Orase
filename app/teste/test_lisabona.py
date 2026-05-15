import os
import importlib.util

cale_biblioteca = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../lib/biblioteca_orase.py")
)

spec = importlib.util.spec_from_file_location("biblioteca_orase", cale_biblioteca)
biblioteca_orase = importlib.util.module_from_spec(spec)
spec.loader.exec_module(biblioteca_orase)

get_populatie_lisabona = biblioteca_orase.get_populatie_lisabona
get_descriere_lisabona = biblioteca_orase.get_descriere_lisabona

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
