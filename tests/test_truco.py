import unittest
from truco import Truco
from jogador import Jogador

class TestTruco(unittest.TestCase):
    def setUp(self):
        self.truco = Truco()

    def test_rodar_vez(self):
        jogadores = [
            Jogador("A", 1, 15),
            Jogador("A", 2, 15),
            Jogador("A", 3, 15),
            Jogador("A", 4, 15)
        ]

        vencedor_da_rodada = 3

        resultado = self.truco.rodar_vez(jogadores, vencedor_da_rodada)

        self.assertEqual(resultado, [
            Jogador("A", 3, 15),
            Jogador("A", 4, 15),
            Jogador("A", 1, 15),
            Jogador("A", 2, 15)
        ])


    def test_calcular_id_time_do_jogador(self):
        id_jogador = 2

        resultado = self.truco.calcular_id_time_do_jogador(id_jogador)

        self.assertEqual(resultado, "2")

    def test_calcular_vencedor(self):
        pilha_de_cartas = [("A", 1), ("2", 2), ("3", 3), ("4", 4)]
        dict_pontos_cartas = {"A": 1, "2": 2, "3": 3, "4": 4}

        resultado = self.truco.calcular_vencedor(pilha_de_cartas, dict_pontos_cartas)

        self.assertEqual(resultado, 4)

    def test_obter_ordem_truco_mineiro(self):
        dict_pontos_cartas_esperado = {
            "A♦": 1, "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7, "J♦": 11, "Q♦": 12, "K♦": 13,
            "A♥": 1, "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "J♥": 11, "Q♥": 12, "K♥": 13,
            "A♠": 1, "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7, "J♠": 11, "Q♠": 12, "K♠": 13,
            "A♣": 1, "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7, "J♣": 11, "Q♣": 12, "K♣": 13
        }

        resultado = self.truco.obter_ordem_truco_mineiro()

        self.assertCountEqual(resultado, dict_pontos_cartas_esperado)

