import unittest
from baralho import Baralho

class TestCarta(unittest.TestCase):
    def test_baralho_inicia_com_40_cartas(self):
        baralho = Baralho()
        self.assertEqual(len(baralho.cartas), 40)

    def test_baralho_inicia_sem_cartas_inutilizaveis(self):
        baralho = Baralho()
        cartas_inutilizaveis = ['8♦','8♠','8♥','8♣','9♦','9♠','9♥','9♣','10♦','10♠','10♥','10♣']

        for carta_inutilizavel in cartas_inutilizaveis :
            self.assertNotIn(carta_inutilizavel, baralho.cartas)

    def test_novo_deque_inicia_com_52_cartas(self):
        baralho = Baralho()
        self.assertEqual(len(baralho.novodeque()), 52)

    def test_embaralhar_altera_ordem_das_cartas(self):
        baralho = Baralho()
        nao_embaralhadas = baralho.cartas.copy()
        embaralhadas = baralho.embaralhar(baralho.cartas)
        self.assertNotEqual(embaralhadas, nao_embaralhadas)

    def test_virar_carta_pega_carta_do_topo(self):
        baralho = Baralho()
        carta_topo = baralho.cartas[-1]
        carta_virada = baralho.virar()
        self.assertEqual(carta_virada, carta_topo)
    
    def test_virar_carta_remove_carta_do_baralho(self):
        baralho = Baralho()
        expected_result = len(baralho.cartas) - 1
        baralho.virar()
        self.assertEqual(len(baralho.cartas), expected_result)

    def test_virar_carta_em_baralho_vazio_lanca_excecao(self):
        baralho = Baralho()
        for _ in range(40) :
            baralho.virar()
        with self.assertRaises(Exception):
            baralho.virar()