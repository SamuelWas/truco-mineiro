from jogador import Jogador
from baralho import Baralho

def obter_jogadores():
    print("Digite o número de jogadores (2 ou 4): ")
    numero_jogadores = int(input())
    while numero_jogadores not in [2, 4]:
        print("O número de jogadores deve ser 2 ou 4! Digite novamente: ")
        numero_jogadores = int(input())

    lista_de_jogadores = list()
    for i in range(numero_jogadores):
        print("Escolha o nome do jogador "+str(i)+": ")
        nome_do_jogador = input()
        lista_de_jogadores.append(Jogador(nome_do_jogador))
    return lista_de_jogadores

if __name__ == '__main__':
    jogadores = obter_jogadores()

    '''while True:
        baralho = Baralho()
        baralho.remover_cartas_inutilizaveis()

        pontuacao = TabelaDePontosJogo()

        for jogador in jogadores:
            jogador.receber_cartas(baralho)

        rodadas = 3
        vencedor_mao = NULL
        while rodadas > 0:        
            pontos_da_mao = TabelaDePontosDaMao()
            pilha_de_cartas = list()    
            for jogador in jogadores:
                carta = realizar_jogada(jogador)
                pilha_de_cartas.push(carta)       

            vencedor_da_rodada = calcular_vencedor(pilha_de_cartas)

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

        baralho.embaralhar()'''
