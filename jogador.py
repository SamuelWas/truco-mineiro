class Jogador:
    def __init__(self, nome, id_jogador, id_time):
        self.nome = nome
        self.id_jogador = id_jogador
        self.id_time = id_time

    def receber_cartas(self, cartas):
        self.cartas = cartas

    def converter_mao_em_string(self):
        cartas_string = list()
        for carta in self.cartas:
            cartas_string.append(str(carta))
        return ','.join(cartas_string)
    
    def realizar_jogada(self):
        print("Sua mão:")
        print(self.converter_mao_em_string())
        print("Qual jogada dezeja realizar?")
        jogada = int(input()) - 1 # 1, 2 ou 3 por enquanto

        return self.cartas.pop(jogada)