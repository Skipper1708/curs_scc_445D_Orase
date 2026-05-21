import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))

from app.lib.biblioteca_orase import populatie_viena, descriere_viena


class TestBibliotecaOrase(unittest.TestCase):

    def test_populatie_viena_not_empty(self):
        rezultat = populatie_viena()
        self.assertIsNotNone(rezultat)
        self.assertGreater(len(rezultat), 0)

    def test_populatie_viena_contine_viena(self):
        rezultat = populatie_viena()
        self.assertIn("Viena", rezultat)

    def test_descriere_viena_not_empty(self):
        rezultat = descriere_viena()
        self.assertIsNotNone(rezultat)
        self.assertGreater(len(rezultat), 0)

    def test_descriere_viena_contine_austria(self):
        rezultat = descriere_viena()
        self.assertIn("Austria", rezultat)


if __name__ == '__main__':
    unittest.main()
