import random

class Matriz:
    def __init__(self, ordem):
        self.ordem = ordem
        self.matriz = None
        self.gera_matriz()

    def gera_matriz(self):
        self.matriz = []
        for i in range(self.ordem):
            self.matriz.append([])
            for j in range(self.ordem):
                self.matriz[i].append(random.randint(0, 1) )

matriz_lista = Matriz(10)

                                         
