from carta import Carta

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

    def receber_carta(self, carta):
        if(len(self.cartas) >= 3):
            raise Exception("Jogador não pode receber mais cartas")
        
        if carta in self.cartas:
            raise Exception("Jogador já possui essa carta")
        
        self.cartas.append(carta)

    def converter_mao_em_string(self):
        return ','.join(map(str, self.cartas))

    def mostrar_mao(self):
        print(f"Sua mão {self.nome}:")
        print(self.converter_mao_em_string())
   
    def realizar_jogada(self):
        self.mostrar_mao()
        jogada = int(input("Qual carta deseja Jogar? ")) - 1  # 1, 2 ou 3 por enquanto
        return self.cartas.pop(jogada)
    
    def limpar_mao(self):
        self.cartas.clear()
    