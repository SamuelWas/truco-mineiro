from enum import Enum
from dataclasses import dataclass
from typing import List
import random

carta_valores=[
    'A',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K'
]

carta_naipes=[
   '♦',
   '♠',
   '♥',
   '♣'
]

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
        return self.cartas.pop()