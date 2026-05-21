import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.lib.biblioteca_orase import populatie_las_vegas, descriere_las_vegas


def test_populatie_las_vegas():
    rezultat = populatie_las_vegas()
    logging.info("test_populatie_las_vegas rezultat: %s", rezultat)
    assert "Las Vegas" in rezultat, "Rezultatul trebuie sa contina 'Las Vegas'"
    assert len(rezultat) > 0, "Rezultatul nu trebuie sa fie gol"


def test_descriere_las_vegas():
    rezultat = descriere_las_vegas()
    logging.info("test_descriere_las_vegas rezultat: %s", rezultat)
    assert "Las Vegas" in rezultat, "Rezultatul trebuie sa contina 'Las Vegas'"
    assert len(rezultat) > 0, "Rezultatul nu trebuie sa fie gol"
