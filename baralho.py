from enum import Enum
from dataclasses import dataclass
from typing import List
import random
from constantes import carta_valores, carta_naipes


@dataclass(frozen=True)
class Carta:
    valor: str
    naipe: str

    def __str__(self):
        return self.valor + self.naipe

    def __repr__(self):
        return self.valor + self.naipe

    
class Baralho:
    """ Classe que define um baralho de cartas. """
    def __init__(self):
        self.cartas = self.novodeque()

    def novodeque(self):
        """ Método de geração das cartas de forma ordenada. """
        cartas = [Carta(v, n) for v in list(carta_valores) for n in list(carta_naipes)]
        return self.embaralhar(cartas)
    
    def remover_cartas_inutilizaveis(self):
        self.cartas = [carta for carta in self.cartas if carta.valor not in ['8', '9', '10']]

    def embaralhar(self, cartas):
        random.shuffle(cartas)
        return cartas
    
    def virar(self):
        """ Retira a carta do topo e remove do baralho. """
        if(len(self.cartas)) == 0:
            raise Exception("Baralho vazio")
            
        return self.cartas.pop()
