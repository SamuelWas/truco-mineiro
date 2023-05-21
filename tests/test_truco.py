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

        resultado = self.truco.calcular_vencedor(
            pilha_de_cartas, dict_pontos_cartas)

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

    def test_rodar_vez_rotacao_4_jogadores(self):
        jogadores = [
            Jogador("John", 1, 2),
            Jogador("Alice", 2, 2),
            Jogador("Bob", 3, 1),
            Jogador("Eve", 4, 1)
        ]
        vencedor_da_rodada = 3

        rotated_jogadores = Truco().rodar_vez(jogadores, vencedor_da_rodada)

        expected_rotated_jogadores = [
            Jogador("Bob", 3, 1),
            Jogador("Eve", 4, 1),
            Jogador("John", 1, 2),
            Jogador("Alice", 2, 2)
        ]
        self.assertEqual(rotated_jogadores, expected_rotated_jogadores)

    def test_rodar_vez_rotacao_2_jogadores(self):
        jogadores = [
            Jogador("John", 1, 1),
            Jogador("Alice", 2, 2),
        ]
        vencedor_da_rodada = 2

        rotated_jogadores = Truco().rodar_vez(jogadores, vencedor_da_rodada)

        expected_rotated_jogadores = [
            Jogador("Alice", 2, 2),
            Jogador("John", 1, 1)
        ]
        self.assertEqual(rotated_jogadores, expected_rotated_jogadores)

    def test_obter_ordem_truco_mineiro_esta_na_ordem(self):
        result = Truco().obter_ordem_truco_mineiro()
        all_cards = {'4♦': 1, '4♠': 1, '4♥': 1, '5♦': 2, '5♠': 2, '5♥': 2, '5♣': 2, '6♦': 3, '6♠': 3, '6♥': 3, '6♣': 3, '7♠': 4, '7♣': 4, 'J♦': 5, 'J♠': 5, 'J♥': 5, 'J♣': 5, 'Q♦': 6, 'Q♠': 6, 'Q♥': 6,
                     'Q♣': 6, 'K♦': 7, 'K♠': 7, 'K♥': 7, 'K♣': 7, 'A♦': 8, 'A♥': 8, 'A♣': 8, '2♦': 9, '2♠': 9, '2♥': 9, '2♣': 9, '3♦': 10, '3♠': 10, '3♥': 10, '3♣': 10, '7♦': 11, 'A♠': 12, '7♥': 13, '4♣': 14}
        self.assertEqual(result, all_cards)

    def test_obter_ordem_truco_mineiro_possui_40_cartas(self):
        self.assertEqual(len(Truco().obter_ordem_truco_mineiro()), 40)

    def test_calcular_vencedor_unica_carta(self):
        dict_pontos_cartas = Truco().obter_ordem_truco_mineiro()
        pilha_de_cartas = [('5♦', 1)]
        expected_result = 1
        self.assertEqual(Truco().calcular_vencedor(
            pilha_de_cartas, dict_pontos_cartas), expected_result)

    def test_calcular_vencedor_multiplas_cartas_manilha(self):
        dict_pontos_cartas = Truco().obter_ordem_truco_mineiro()
        pilha_de_cartas = [('4♣', 1), ('5♦', 2), ('6♦', 3), ('2♠', 4)]
        expected_result = 1
        self.assertEqual(Truco().calcular_vencedor(
            pilha_de_cartas, dict_pontos_cartas), expected_result)
    
    def test_calcular_vencedor_multiplas_cartas_sem_manilha(self):
        dict_pontos_cartas = Truco().obter_ordem_truco_mineiro()
        pilha_de_cartas = [('4♦', 1), ('5♦', 2), ('6♦', 3), ('2♠', 4)]
        expected_result = 4
        self.assertEqual(Truco().calcular_vencedor(
            pilha_de_cartas, dict_pontos_cartas), expected_result)

    def test_calcular_vencedor_cartas_mesmo_valor(self):
        dict_pontos_cartas = Truco().obter_ordem_truco_mineiro()

        pilha_de_cartas = [('Q♦', 1), ('Q♥', 2), ('Q♣', 3)]
        expected_result = 0
        self.assertEqual(Truco().calcular_vencedor(
            pilha_de_cartas, dict_pontos_cartas), expected_result)
