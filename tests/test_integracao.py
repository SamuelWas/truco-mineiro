import sys
import io
import unittest
from unittest import mock
from unittest.mock import patch
from jogo import Jogo
from jogador import Jogador

class TestIntegracao(unittest.TestCase):

    def setUp(self):
        self.jogo = Jogo(2)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['J', '1', 'J', '1'])
    def test_rodada_normal(self, mock_output, mock_input):
        jogador_1 = Jogador('Jonas', 1, '1')
        jogador_1.cartas = ['2♦', '3♠', 'A♥']
        jogador_2 = Jogador('Godofredo', 2, '2')
        jogador_2.cartas = ['3♣', '2♠', '5♣']
        lista_jogadores = [jogador_1, jogador_2]
        self.jogo.jogadores = lista_jogadores
        self.assertEqual(self.jogo.nova_rodada(), 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['A', 'A', '2', 'J', '2'])
    def test_rodada_truco(self, mock_output, mock_input):
        jogador_1 = Jogador('Jonas', 1, '1')
        jogador_1.cartas = ['2♦', '3♠', 'A♥']
        jogador_2 = Jogador('Godofredo', 2, '2')
        jogador_2.cartas = ['3♣', '2♠', '5♣']
        lista_jogadores = [jogador_1, jogador_2]
        self.jogo.jogadores = lista_jogadores
        self.assertEqual(self.jogo.nova_rodada(), 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['J', '1', 'J', '1','J', '1', 'J', '1','J', '1', 'J', '1'])
    def test_rodada_completa(self, mock_output, mock_input):
        jogador_1 = Jogador('Jonas', 1, '1')
        jogador_2 = Jogador('Godofredo', 2, '2')
        self.jogo.baralho.cartas = ['2♦', '3♠', 'A♥', '3♣', '2♠', '5♣']
        lista_jogadores = [jogador_1, jogador_2]
        self.jogo.jogadores = lista_jogadores
        self.assertEqual(self.jogo.controlar_fluxo_partida(), 1)
