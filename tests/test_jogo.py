import unittest
from unittest.mock import patch
from jogo import Jogo

class TestJogo(unittest.TestCase):
    
    def setUp(self):
        self.jogo = Jogo(4)

    @patch('builtins.input', side_effect=['Jogador 1', 'Jogador 2'])
    def test_obter_jogadores_dois_jogadores(self, mock_input):
        self.jogo.obter_jogadores(2)
        self.assertEqual(len(self.jogo.jogadores), 2)
        self.assertEqual(self.jogo.jogadores[0].nome, 'Jogador 1')
        self.assertEqual(self.jogo.jogadores[1].nome, 'Jogador 2')

    @patch('builtins.input', side_effect=['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4'])
    def test_obter_jogadores_quatro_jogadores(self, mock_input):
        self.jogo.obter_jogadores(4)
        self.assertEqual(len(self.jogo.jogadores), 4)
        self.assertEqual(self.jogo.jogadores[0].nome, 'Jogador 1')
        self.assertEqual(self.jogo.jogadores[1].nome, 'Jogador 2')
        self.assertEqual(self.jogo.jogadores[2].nome, 'Jogador 3')
        self.assertEqual(self.jogo.jogadores[3].nome, 'Jogador 4')

    def test_calcular_id_time_do_primeiro_jogador(self):
        self.assertEqual(self.jogo.calcular_id_time_do_jogador(1), '1')

    def test_limpar_pilha_cartas(self):
        self.jogo.pilha_de_cartas = [(3, 1), (4, 2), (2, 3)]
        self.jogo.limpar_pilha_cartas()
        self.assertEqual(len(self.jogo.pilha_de_cartas), 0)

    def test_adicionar_jogada_a_pilha(self):
        self.jogo.adicionar_jogada_a_pilha(5, 1)
        self.jogo.adicionar_jogada_a_pilha(2, 2)
        self.assertEqual(self.jogo.pilha_de_cartas, [(5, 1), (2, 2)])

    def test__resetar_estado_jogo(self):
        self.jogo._resetar_estado_jogo()
        for jogador in self.jogo.jogadores:
            self.assertEqual(len(jogador.mao), 0)

    def test__distribuir_cartas_para_jogadores(self):
        self.jogo._distribuir_cartas_para_jogadores()
        for jogador in self.jogo.jogadores:
            self.assertEqual(len(jogador.mao), 3)
