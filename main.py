

if __name__ == '__main__':
    numero_jogadores = input()
    jogadores = obter_jogadores(numero_jogadores)
    while True:
        baralho = Baralho()
        baralho.embaralhar()

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


