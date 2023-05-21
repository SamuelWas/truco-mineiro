
from constantes import manilhas, valores, naipes

class Truco:
    def rodar_vez(self, jogadores, vencedor_da_rodada):
        idx = 0
        eixo_de_rotacao = 0
        for jogador in jogadores:
            if jogador.id_jogador == vencedor_da_rodada:
                eixo_de_rotacao = idx
            idx += 1
        jogadores = jogadores[eixo_de_rotacao:] + jogadores[:eixo_de_rotacao]
        return jogadores

    def calcular_id_time_do_jogador(self , id_jogador):
        return str(2 - (id_jogador % 2))

    def calcular_vencedor(self,pilha_de_cartas, dict_pontos_cartas):
        maior_valor = 0
        vencedores = []
        for carta, id_jogador in pilha_de_cartas:
            valor_carta = dict_pontos_cartas[str(carta)]
            if valor_carta > maior_valor:
                vencedores = []
                maior_valor = valor_carta
                vencedores.append((carta, id_jogador))
            elif valor_carta == maior_valor:
                vencedores.append((carta, id_jogador))
        
        if len(vencedores) == 1:
            return vencedores.pop()[1]
        time_vencedor = self.calcular_id_time_do_jogador(vencedores[0][1])
        for carta,id_jogador in vencedores:
            if time_vencedor != self.calcular_id_time_do_jogador(id_jogador):
                return 0
        return vencedores.pop()[1]
    
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