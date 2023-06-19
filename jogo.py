from jogador import Jogador
from baralho import Baralho
from truco import Truco
from tabela_de_pontos import TabelaDePontos
from constantes import manilhas, valores, naipes
import os
import platform


class Jogo():
    def __init__(self, num_jogadores):
        
        self.numero_jogadores = num_jogadores
        self.jogadores = []
        self.vencedor_da_rodada = 0
        self.baralho = Baralho()
        self.tabela_pontos = TabelaDePontos()
        self.pilha_de_cartas = []
        self.dict_pontos_cartas = Truco().obter_ordem_truco_mineiro()
        self.rodada = 0
        self.terminar_rodada = False

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
        self.jogadores = lista_de_jogadores
    
    def calcular_id_time_do_jogador(self , id_jogador):
        return str(2 - (id_jogador % 2))

    def limpar_pilha_cartas(self):
        self.pilha_de_cartas.clear()

    def adicionar_jogada_a_pilha(self, carta, jogador_id):
        self.pilha_de_cartas.append((carta, jogador_id))

    def _resetar_baralho(self):
        self.baralho = Baralho()
        print('Embaralhando as cartas...')
    
    def _resetar_estado_jogo(self):
        for jogador in self.jogadores:
            jogador.limpar_mao()

    def _imprimir_pilha(self):
        print("Pilha de cartas:")
        print(','.join(map(str, self.pilha_de_cartas)))
        return
        
    def _receber_input_jogada(self):
        print("Qual jogada deseja realizar?")
        print("(A) - Aumentar a aposta")
        print("(J) - Jogar uma carta:  ")
        return str(input()).upper()
    
    def _receber_input_aposta(self):
        print("Digite D para dobrar a aposta, C para correr, ou A para aceitar:")
        print("(D) dobrar a aposta")
        print("(C) correr")
        print("(A) aceitar")

        return str(input()).upper()
    
    def _distribuir_cartas_para_jogadores(self):
        for i in range (3):
            for jogador in self.jogadores:
                carta = self.baralho.virar()
                jogador.receber_carta(carta)

    def controlar_partida(self):
        while True:
            id_vencedor = self.controlar_fluxo_partida()
            id_time_vencedor = int(self.calcular_id_time_do_jogador(id_vencedor))
            print("Time "+str(id_time_vencedor)+" venceu a mão!")
            print(str(self.tabela_pontos.multiplicador)+" pontos para o time "+str(id_time_vencedor))
            self.tabela_pontos.pontuar(id_time_vencedor)
            self.tabela_pontos.limpar_estado_de_jogo()
            if self.tabela_pontos.is_termino():
                return self.tabela_pontos.is_termino()

    def controlar_fluxo_partida(self):
        self.terminar_rodada = False
        self._resetar_estado_jogo()
        self._distribuir_cartas_para_jogadores()
        self.limpar_pilha_cartas()
        vencedor_partidas = []
        vencedor_rodada = self.nova_rodada()
        self.limpar_pilha_cartas()

        if self.terminar_rodada:
            return vencedor_rodada
        
        if vencedor_rodada != 0:
            #Se não empatou, comece uma nova rodada.
            vencedor_partidas.append(vencedor_rodada)
            vencedor_nova_rodada = self.nova_rodada()
            self.limpar_pilha_cartas()
            
            #Caso a nova rodada empatar, vence quem ganhou a primeira
            if vencedor_nova_rodada == 0:
                return  vencedor_partidas[0]
            
            elif vencedor_nova_rodada == vencedor_rodada:
                return vencedor_rodada
            
            #Caso não empatar, joguemos a terceira rodada. Como cada um ganhou uma rodada, ganha quem ganhar a terceira
            else:
                vencedor_terceira_rodada = self.nova_rodada()
                self.limpar_pilha_cartas()
                return vencedor_terceira_rodada
        
        
        #Caso tenha empatado
        else:
            vencedor_rodada_empatada = self.nova_rodada()
            self.limpar_pilha_cartas()
            if vencedor_rodada_empatada != 0:
                return vencedor_rodada_empatada
            
            #Caso empate novamente
            else:
                vencedor_nova_rodada_empatada = self.nova_rodada()
                self.limpar_pilha_cartas()
                return vencedor_nova_rodada_empatada
                

    def nova_rodada(self):
        for idx, jogador in enumerate(self.jogadores):
            self._imprimir_pilha()
            jogador.mostrar_mao()
            play = self._receber_input_jogada()
            self._limpar_cmd()
            
            if play == 'J':
                carta = jogador.realizar_jogada()
                self._limpar_cmd()
                self.adicionar_jogada_a_pilha(carta, jogador.id_jogador)
            else:
                print(f'{jogador.nome} Aumentou a aposta, deseja aceitar, correr ou aumentar a aposta novamente?')
                aceitou = self._receber_input_aposta()
                
                if aceitou == 'A':
                    self._limpar_cmd()
                    self.tabela_pontos.aumentar_multiplicador()
                    carta = jogador.realizar_jogada()
                    self.adicionar_jogada_a_pilha(carta, jogador.id_jogador)
                
                elif aceitou == 'C':
                    self.terminar_rodada = True
                    vencedor_rodada = jogador.id_jogador
                    return vencedor_rodada
                
                else:
                    self.tabela_pontos.aumentar_multiplicador()
                    self.tabela_pontos.aumentar_multiplicador()
                    carta = jogador.realizar_jogada()
                    self.adicionar_jogada_a_pilha(carta, jogador.id_jogador)
        
        return Truco().calcular_vencedor(self.pilha_de_cartas, self.dict_pontos_cartas)     
