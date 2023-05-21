class Jogador:
    def __init__(self, nome, id_jogador, id_time):
        self.nome = nome
        self.id_jogador = id_jogador
        self.id_time = id_time
        self.cartas = []

    def __eq__(self, other):
        return self.nome == other.nome and self.id_jogador == other.id_jogador and self.id_time == other.id_time
    
    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return self.nome

    def receber_cartas(self, cartas):
        self.cartas = cartas

    def converter_mao_em_string(self):
        return ','.join(map(str, self.cartas))

    def realizar_jogada(self):
        print(f"Sua mão {self.nome}:")
        print(self.converter_mao_em_string())
        jogada = int(input("Qual jogada deseja realizar? ")) - 1  # 1, 2 ou 3 por enquanto
        return self.cartas.pop(jogada)
    