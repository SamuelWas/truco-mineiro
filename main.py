from jogador import Jogador
from baralho import Baralho
from tabela_de_pontos import TabelaDePontos

def obter_jogadores():
    print("Digite o número de jogadores (2 ou 4): ")
    numero_jogadores = int(input())
    while numero_jogadores not in [2, 4]:
        print("O número de jogadores deve ser 2 ou 4! Digite novamente: ")
        numero_jogadores = int(input())

    lista_de_jogadores = list()
    for i in range(1, numero_jogadores + 1):
        id_time = calcular_id_time_do_jogador(i)
        print("Escolha o nome do jogador "+str(i)+" (time "+str(id_time)+"): ")
        nome_do_jogador = input()
        lista_de_jogadores.append(Jogador(nome_do_jogador, i, id_time))
    return lista_de_jogadores

def calcular_vencedor(pilha_de_cartas, dict_pontos_cartas):
    maior_valor = 0
    id_jogador_vencedor = 0
    for carta, id_jogador in pilha_de_cartas:
        valor_carta = dict_pontos_cartas[str(carta)]
        if valor_carta > maior_valor:
            maior_valor = valor_carta
            id_jogador_vencedor = id_jogador
            maior_carta = carta
    return (maior_carta, id_jogador_vencedor)

def rodar_vez(jogadores, vencedor_da_rodada):
    i = 0
    eixo_de_rotacao = 0
    for jogador in jogadores:
        if jogador.id_jogador == vencedor_da_rodada:
            eixo_de_rotacao = i
        i += 1

    jogadores = jogadores[eixo_de_rotacao:] + jogadores[:eixo_de_rotacao]
            
    return jogadores

def obter_ordem_truco_mineiro():
    manilhas = ['7♦', 'A♠', '7♥', '4♣']
    valores = ['7', '6', '5', '4', 'J', 'Q', 'K', 'A', '2', '3']
    naipes= ['♦', '♠', '♥', '♣']
    
    score = 1
    dict_pontos_cartas = {}
    for valor in valores:
        for naipe in naipes:
            carta = valor + naipe
            if carta not in manilhas: 
                dict_pontos_cartas[carta] = score
        score = score + 1

    for manilha in manilhas:
        dict_pontos_cartas[manilha] = score
        score = score + 1

    return dict_pontos_cartas

def calcular_id_time_do_jogador(id_jogador):
    return str(2 - (id_jogador % 2))

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
        time_vencedor_mao = 0
        truco = False
        seis = False
        nove = False
        doze = False
        while rodadas > 0:        
            pontos_da_mao = {}
            pontos_da_mao['1'] = 0
            pontos_da_mao['2'] = 0

            pilha_de_cartas = list()    
            for jogador in jogadores:
                carta = jogador.realizar_jogada()
                # print(carta) DEBUG
                pilha_de_cartas.append((carta, jogador.id_jogador))       

            maior_carta, vencedor_da_rodada = calcular_vencedor(pilha_de_cartas, dict_pontos_cartas)
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
