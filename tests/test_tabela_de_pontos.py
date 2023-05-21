import unittest
from tabela_de_pontos import TabelaDePontos

class TestTabelaDePontos(unittest.TestCase):

    def setUp(self):
        self.tabela = TabelaDePontos()

    def test_pontuar_time1(self):
        self.tabela.pontuar(1)
        self.assertEqual(self.tabela.pontos_t1, 2)

    def test_pontuar_time2(self):
        self.tabela.pontuar(2)
        self.assertEqual(self.tabela.pontos_t2, 2)

    def test_aumentar_multiplicador(self):
        self.tabela.aumentar_multiplicador()
        self.assertEqual(self.tabela.multiplicador, 4)

    def test_is_termino_time1(self):
        self.tabela.pontos_t1 = 12
        self.assertEqual(self.tabela.is_termino(), 1)

    def test_is_termino_time2(self):
        self.tabela.pontos_t2 = 12
        self.assertEqual(self.tabela.is_termino(), 2)

    def test_limpar_estado_de_jogo(self):
        self.tabela.limpar_estado_de_jogo()
        self.assertEqual(self.tabela.multiplicador, 2)

