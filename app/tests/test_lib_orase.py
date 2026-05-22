import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.lib.biblioteca_orase import populatie_barcelona, descriere_barcelona


def test_populatie_barcelona():
    rezultat = populatie_barcelona()
    logging.info("test_populatie_barcelona rezultat: %s", rezultat)
    assert "Barcelona" in rezultat, "Rezultatul trebuie sa contina 'Barcelona'"
    assert len(rezultat) > 0, "Rezultatul nu trebuie sa fie gol"


def test_descriere_barcelona():
    rezultat = descriere_barcelona()
    logging.info("test_descriere_barcelona rezultat: %s", rezultat)
    assert "Barcelona" in rezultat, "Rezultatul trebuie sa contina 'Barcelona'"
    assert len(rezultat) > 0, "Rezultatul nu trebuie sa fie gol"
