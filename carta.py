from constantes import carta_valores, carta_naipes


class Carta:
    def __init__(self, valor, naipe):
        if (valor not in carta_valores):
            raise Exception("Valor inválido")
        if (naipe not in carta_naipes):
            raise Exception("Naipe inválido")
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return self.valor + self.naipe

    def __repr__(self):
        return self.valor + self.naipe
