import unittest
from baralho import Carta

class TestCarta(unittest.TestCase):
    def test_carta_visualization(self):
        carta = Carta('A', '♦')
        self.assertEqual(str(carta), 'A♦')
        self.assertEqual(repr(carta), 'A♦')