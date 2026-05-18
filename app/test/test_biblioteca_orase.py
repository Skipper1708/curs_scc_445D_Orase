import unittest
from app.lib.biblioteca_orase import descriere_paris, obiective_paris


class TestParis(unittest.TestCase):

    def test_descriere_paris(self):
        rezultat = descriere_paris()
        self.assertIn("Paris", rezultat)
        self.assertIn("Frantei", rezultat)

    def test_obiective_paris(self):
        rezultat = obiective_paris()
        self.assertIn("Paris", rezultat)
        self.assertIn("Turnul Eiffel", rezultat)


if __name__ == "__main__":
    unittest.main()
