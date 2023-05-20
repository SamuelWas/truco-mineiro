import unittest
from jogador import Jogador

class JogadorTest(unittest.TestCase):
    def test_inicializar_jogador(self):
        jogador = Jogador("João", 1, 10)
        self.assertEqual(jogador.nome, "João")
        self.assertEqual(jogador.id_jogador, 1)
        self.assertEqual(jogador.id_time, 10)

    def test_receber_zero_cartas(self):
        jogador = Jogador("João", 1, 10)
        cartas = []
        jogador.receber_cartas(cartas)
        self.assertEqual(jogador.cartas, cartas)

    def test_receber_cartas(self):
        jogador = Jogador("João", 1, 10)
        cartas = ["A♠", "10♠", "K♠"]
        jogador.receber_cartas(cartas)
        self.assertEqual(jogador.cartas, cartas)

    def test_converter_mao_vazia_em_string(self):
        jogador = Jogador("João", 1, 1)
        jogador.receber_cartas([])
        self.assertEqual(jogador.converter_mao_em_string(), "")

    def test_converter_mao_unica_em_string(self):
        jogador = Jogador("Maria", 2, 1)
        jogador.receber_cartas(["A♦"])
        self.assertEqual(jogador.converter_mao_em_string(), "A♦")

    def test_converter_mao_multipla_em_string(self):
        jogador = Jogador("Pedro", 3, 2)
        jogador.receber_cartas(["A♠", "10♠", "K♠", "Q♦"])
        self.assertEqual(jogador.converter_mao_em_string(), "A♠,10♠,K♠,Q♦")

    def test_realizar_jogada(self):
        # Método com baixa testabilidade
        pass
