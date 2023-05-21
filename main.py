from jogador import Jogador
from baralho import Baralho
from truco import Truco
from jogo import Jogo
from tabela_de_pontos import TabelaDePontos
from constantes import manilhas, valores, naipes
import os
import platform

def main():
    num_jogadores = int(input("Numero de jogadores (2 ou 4): "))
    jogo = Jogo(num_jogadores)
    jogo.obter_jogadores(num_jogadores)
    jogo._limpar_cmd()
    time_ganhador = jogo.controlar_partida()
    print("O time "+str(time_ganhador)+" venceu!")

if __name__ == '__main__':
    main()
