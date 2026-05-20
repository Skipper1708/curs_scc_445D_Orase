import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.lib.biblioteca_orase import populatie_como, descriere_como

class TestComo(unittest.TestCase):
    def test_populatie_como(self):
        result = populatie_como()
        self.assertIn("Como", result)
        self.assertIsInstance(result, str)

    def test_descriere_como(self):
        result = descriere_como()
        self.assertIn("Como", result)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
