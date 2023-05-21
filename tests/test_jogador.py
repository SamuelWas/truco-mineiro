import unittest
from jogador import Jogador


class TestJogador(unittest.TestCase):
    def test_inicializar_jogador_nome(self):
        jogador = Jogador("João", 1, 10)
        self.assertEqual(jogador.nome, "João")

    def test_inicializar_jogador_id(self):
        jogador = Jogador("João", 1, 10)
        self.assertEqual(jogador.id_jogador, 1)

    def test_inicializar_jogador_time(self):
        jogador = Jogador("João", 1, 10)
        self.assertEqual(jogador.id_time, 10)

    def test_visualizar_jogador(self):
        jogador = Jogador("João", 1, 10)
        self.assertEqual(str(jogador), jogador.nome)

    def test_receber_carta_repetida(self):
        jogador = Jogador("João", 1, 10)
        jogador.receber_carta("A♠")

        with self.assertRaises(Exception):
            jogador.receber_carta("A♠")

    def test_receber_mais_de_3_cartas(self):
        jogador = Jogador("João", 1, 10)
        jogador.receber_carta("A♠")
        jogador.receber_carta("10♠")
        jogador.receber_carta("2♠")

        with self.assertRaises(Exception):
            jogador.receber_carta("K♠")

    def test_receber_zero_cartas(self):
        jogador = Jogador("João", 1, 10)
        self.assertEqual(jogador.cartas, [])

    def test_receber_cartas(self):
        jogador = Jogador("João", 1, 10)
        jogador.receber_carta("A♠")
        jogador.receber_carta("10♠")
        jogador.receber_carta("K♠")
        self.assertEqual(jogador.cartas, ["A♠", "10♠", "K♠"])

    def test_converter_mao_vazia_em_string(self):
        jogador = Jogador("João", 1, 1)
        self.assertEqual(jogador.converter_mao_em_string(), "")

    def test_converter_mao_unica_em_string(self):
        jogador = Jogador("Maria", 2, 1)
        jogador.receber_carta("A♦")
        self.assertEqual(jogador.converter_mao_em_string(), "A♦")

    def test_converter_mao_multipla_em_string(self):
        jogador = Jogador("Pedro", 3, 2)
        jogador.receber_carta("A♠")
        jogador.receber_carta("10♠")
        jogador.receber_carta("K♠")
        self.assertEqual(jogador.converter_mao_em_string(), "A♠,10♠,K♠")

    def test_limpar_mao(self):
        jogador = Jogador("Pedro", 3, 2)
        jogador.receber_carta("A♠")
        jogador.receber_carta("10♠")
        jogador.receber_carta("K♠")
        jogador.limpar_mao()
        self.assertEqual(jogador.cartas, [])

    def test_jogadores_sao_iguais(self):
        self.assertEqual(Jogador("Pedro", 3, 2), Jogador("Pedro", 3, 2))
