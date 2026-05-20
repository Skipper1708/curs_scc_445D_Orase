import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.lib.biblioteca_orase import populatie_roma, descriere_roma


def test_populatie_roma():
    rezultat = populatie_roma()
    logging.info("test_populatie_roma rezultat: %s", rezultat)
    assert "Roma" in rezultat, "Rezultatul trebuie sa contina 'Roma'"
    assert len(rezultat) > 0, "Rezultatul nu trebuie sa fie gol"


def test_descriere_roma():
    rezultat = descriere_roma()
    logging.info("test_descriere_roma rezultat: %s", rezultat)
    assert "Roma" in rezultat, "Rezultatul trebuie sa contina 'Roma'"
    assert len(rezultat) > 0, "Rezultatul nu trebuie sa fie gol"
