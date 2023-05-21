from jogador import Jogador
from baralho import Baralho
from tabela_de_pontos import TabelaDePontos
from constantes import manilhas, valores, naipes
import os
import platform

class Jogo():
    def __init__(self, num_jogadores):
        
        self.numero_jogadores = num_jogadores
        self.jogadores = self.obter_jogadores(num_jogadores)
        self.vencedor_da_rodada = 0
        self.baralho = Baralho()
        self.tabela_pontos = TabelaDePontos()
        self.pilha_de_cartas = []
        self.dict_pontos_cartas = self.obter_ordem_truco_mineiro()
        self.rodada = 0
        self.estado_jogo = 0

    def _limpar_cmd(self):
        sistema_operacional = platform.system()
        if sistema_operacional == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    
    def obter_jogadores(self, numero_jogadores):
        lista_de_jogadores = list()
        for id in range(1, numero_jogadores + 1):
            id_time = self.calcular_id_time_do_jogador(id)
            print("Escolha o nome do jogador "+str(id)+" (time "+str(id_time)+"): ")
            nome_do_jogador = input()
            lista_de_jogadores.append(Jogador(nome_do_jogador, id, id_time))
        return lista_de_jogadores
    
    def calcular_id_time_do_jogador(self , id_jogador):
        return str(2 - (id_jogador % 2))
    
    def obter_ordem_truco_mineiro(self):
        score = 1
        dict_pontos_cartas = {}
        for valor in valores:
            for naipe in naipes:
                carta = valor + naipe
                if carta not in manilhas: 
                    dict_pontos_cartas[carta] = score
            score += 1

        for manilha in manilhas:
            dict_pontos_cartas[manilha] = score
            score += 1
        return dict_pontos_cartas 

    def limpar_pilha_cartas(self):
        self.pilha_de_cartas.clear()

    def adicionar_jogada_a_pilha(self, carta, jogador_id):
        self.pilha_de_cartas.append((carta, jogador_id))

    def _resetar_baralho(self):
        self.baralho = Baralho()
        print('Embaralhando as cartas...')
    
    def rodar_vez(self):
        idx = 0
        eixo_de_rotacao = 0
        for jogador in self.jogadores:
            if jogador.id_jogador == self.vencedor_da_rodada:
                eixo_de_rotacao = idx
            idx += 1
        self.jogadores = self.jogadores[eixo_de_rotacao:] + self.jogadores[:eixo_de_rotacao]

    def _calcular_vencedor(self):
        maior_valor = 0
        vencedores = []
        for carta, id_jogador in self.pilha_de_cartas:
            valor_carta = self.dict_pontos_cartas[str(carta)]
            if valor_carta > maior_valor:
                vencedores = []
                maior_valor = valor_carta
                vencedores.append((carta, id_jogador))
            elif valor_carta == maior_valor:
                vencedores.append((carta, id_jogador))
        
        if len(vencedores) == 1:
            return vencedores.pop()
        time_vencedor = self.calcular_id_time_do_jogador(vencedores[0][1])
        for carta,id_jogador in vencedores:
            if time_vencedor != self.calcular_id_time_do_jogador(id_jogador):
                return 0
        return vencedores.pop()
    
    def _resetar_estado_jogo(self):
        self.estado_jogo = 0
    
    def _receber_input_jogada(self):
        print("Qual jogada deseja realizar? A - Aumentar a aposta, J - jogar uma carta:  ")
        return str(input()).upper()
    
    def _receber_input_aposta(self):
        print('Digite D para dobrar a aposta, C para correr, ou A para aceitar: ')
        return str(input()).upper()
    
    def _distribuir_cartas_para_jogadores(self):
        for i in range (3):
            for jogador in self.jogadores:
                carta = self.baralho.virar()
                jogador.receber_carta(carta)

    def controlar_fluxo_partida(self):
        self._distribuir_cartas_para_jogadores()
        self.limpar_pilha_cartas()
        vencedor_partidas = []
        vencedor_rodada = self.nova_rodada()
        
        if vencedor_rodada != 0:
            #Se não empatou, comece uma nova rodada.
            vencedor_partidas.append(vencedor_rodada)
            vencedor_nova_rodada = self.nova_rodada()
            
            #Caso a nova rodada empatar, vence quem ganhou a primeira
            if vencedor_nova_rodada == 0:
                return  vencedor_partidas[0], self.estado_jogo
            
            elif vencedor_nova_rodada == vencedor_rodada:
                vencedor_rodada, self.estado_jogo
            
            #Caso não empatar, joguemos a terceira rodada. Como cada um ganhou uma rodada, ganha quem ganhar a terceira
            else:
                vencedor_terceira_rodada = self.nova_rodada()
                return vencedor_terceira_rodada, self.estado_jogo
        
        
        #Caso tenha empatado
        else:
            vencedor_rodada_empatada = self.nova_rodada()
            if vencedor_rodada_empatada != 0:
                return vencedor_rodada_empatada, self.estado_jogo
            
            #Caso empate novamente
            else:
                vencedor_nova_rodada_empatada = self.nova_rodada()
                return vencedor_nova_rodada_empatada, self.estado_jogo
                

    def nova_rodada(self):
        for idx, jogador in enumerate(self.jogadores):
            jogador.mostrar_mao()
            play = self._receber_input_jogada()
            
            if play == 'J':
                carta = jogador.realizar_jogada()
                self.adicionar_jogada_a_pilha(carta, jogador.id_jogador)
            else:
                self._limpar_cmd()
                print(f'{jogador.nome} Aumentou a aposta, deseja aceitar, correr ou aumentar a aposta novamente?')
                aceitou = self._receber_input_aposta()
                
                if aceitou == 'A':
                    self._limpar_cmd()
                    self.estado_jogo = 2
                    carta = jogador.realizar_jogada()
                    self.adicionar_jogada_a_pilha(carta, jogador.id_jogador)
                
                elif aceitou == 'C':
                    vencedor_rodada = jogador
                    return vencedor_rodada
                
                else:
                    carta = jogador.realizar_jogada()
                    self.adicionar_jogada_a_pilha(carta, jogador.id_jogador)
        
        return self._calcular_vencedor()       


def main():

    dict_pontos_cartas = obter_ordem_truco_mineiro()
    jogadores = obter_jogadores()

    while True:
        baralho = Baralho()
        baralho.remover_cartas_inutilizaveis()

        tabela_pontuacao = TabelaDePontos()

        for jogador in jogadores:
            mao = list()
            for i in range(3):
                mao.append(baralho.virar())
            jogador.receber_cartas(mao)

        rodadas = 3
        while rodadas > 0:        
            pontos_da_mao = {}
            pontos_da_mao['1'] = 0
            pontos_da_mao['2'] = 0

            pilha_de_cartas = list()    
            for jogador in jogadores:
                carta = jogador.realizar_jogada()
                limpar_cmd()
                # print(carta) DEBUG
                pilha_de_cartas.append((carta, jogador.id_jogador))       

            maior_carta, vencedor_da_rodada = calcular_vencedor(pilha_de_cartas, dict_pontos_cartas)
            if vencedor_da_rodada == 0:
                print("Empate!")
            else:
                print("Maior carta da pilha: " + str(maior_carta) +  " do jogador " + str(vencedor_da_rodada))
            
            jogadores = rodar_vez(jogadores, vencedor_da_rodada)

            time_vencedor = calcular_id_time_do_jogador(vencedor_da_rodada)
            pontos_da_mao[time_vencedor]
            if pontos_da_mao[time_vencedor] == 2:
                vencedor_mao = pontos_da_mao.get_vencedor()
                break
            rodadas = rodadas - 1
        
        tabela_pontuacao.pontuar(vencedor_mao)
        if tabela_pontuacao.is_termino():
            print("Os jogadores X e Y ganharam!")
            break

        baralho.embaralhar()


if __name__ == '__main__':
    main()
