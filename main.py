from jogador import Jogador
from baralho import Baralho

def obter_jogadores():
    print("Digite o número de jogadores (2 ou 4): ")
    numero_jogadores = int(input())
    while numero_jogadores not in [2, 4]:
        print("O número de jogadores deve ser 2 ou 4! Digite novamente: ")
        numero_jogadores = int(input())

    lista_de_jogadores = list()
    for i in range(1, numero_jogadores + 1):
        id_time = 2 - (i % 2)
        print("Escolha o nome do jogador "+str(i)+" (time "+str(id_time)+"): ")
        nome_do_jogador = input()
        lista_de_jogadores.append(Jogador(nome_do_jogador, i, id_time))
    return lista_de_jogadores

def calcular_vencedor(pilha_de_cartas, dict_pontos_cartas):
    maior_valor = 0
    for carta in pilha_de_cartas:
        valor_carta = dict_pontos_cartas[str(carta)]
        if valor_carta > maior_valor:
            maior_valor = valor_carta
    return

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

if __name__ == '__main__':
    dict_pontos_cartas = obter_ordem_truco_mineiro()
    jogadores = obter_jogadores()

    while True:
        baralho = Baralho()
        baralho.remover_cartas_inutilizaveis()

        # pontuacao = TabelaDePontosJogo()

        for jogador in jogadores:
            mao = list()
            for i in range(3):
                mao.append(baralho.virar())
            jogador.receber_cartas(mao)

        rodadas = 3
        time_vencedor_mao = 0
        while rodadas > 0:        
            # pontos_da_mao = TabelaDePontosDaMao()
            pilha_de_cartas = list()    
            for jogador in jogadores:
                carta = jogador.realizar_jogada()
                print(carta)
                pilha_de_cartas.append(carta)       

            vencedor_da_rodada = calcular_vencedor(pilha_de_cartas, dict_pontos_cartas)

            jogadores = rodar_vez(jogadores, vencedor_da_rodada)

            pontos_da_mao.pontuar(vencedor_da_rodada)
            if pontos_da_mao.is_termino():
                vencedor_mao = pontos_da_mao.get_vencedor()
                break
            rodadas = rodadas - 1
        
        pontuacao.pontuar(vencedor_mao)
        if pontuacao.is_termino():
            print("Os jogadores X e Y ganharam!")
            break

        baralho.embaralhar()
