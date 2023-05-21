import unittest
from carta import Carta

class TestCarta(unittest.TestCase):
    def test_visualizar_carta(self):
        carta = Carta('A', '♦')
        self.assertEqual(str(carta), 'A♦')
        self.assertEqual(repr(carta), 'A♦')
        
    def test_carta_inicia_com_valor(self):
        carta = Carta("A", "♦")
        self.assertEqual(carta.valor, "A")

    def test_carta_inicia_com_naipe(self):
        carta = Carta("A", "♦")
        self.assertEqual(carta.naipe, "♦")
    
    def test_criar_carta_com_valor_invalido_lanca_excecao(self):
        with self.assertRaises(Exception):
            Carta("0", "♦")

    def test_criar_carta_com_naipe_invalido_lanca_excecao(self):
        with self.assertRaises(Exception):
            Carta("A", "X")