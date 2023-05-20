import unittest
from baralho import Baralho

class TestCarta(unittest.TestCase):
    def test_baralho__inicia_com_52_cartas(self):
        baralho = Baralho()
        self.assertEqual(len(baralho.cartas), 52)

    def test_remover_cartas_inutilizaveis_nao_possui_inutilizadas(self):
        baralho = Baralho()
        baralho.remover_cartas_inutilizaveis()
        
        cartas_inutilizaveis = ['8♦','8♠','8♥','8♣','9♦','9♠','9♥','9♣','10♦','10♠','10♥','10♣']
        for carta_inutilizavel in cartas_inutilizaveis :
            self.assertNotIn(carta_inutilizavel, baralho.cartas)

    def test_remover_cartas_inutilizaveis_40_cartas(self):
        baralho = Baralho()
        baralho.remover_cartas_inutilizaveis()
        
        self.assertEqual(len(baralho.cartas), 40)

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
        carta_virada = baralho.virar()
        self.assertEqual(len(baralho.cartas), 51)

    def test_virar_carta_em_baralho_vazio_lanca_excecao(self):
        baralho = Baralho()
        for i in range(52) :
            baralho.virar()

        with self.assertRaises(Exception):
            baralho.virar()