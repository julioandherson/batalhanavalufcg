import os
from random import randint
import random
import pygame
relogio = pygame.time.Clock()

class Barco:
    def __init__(self):
        self.relogio = relogio
        self.contador = 1

        while self.contador <= 16:
            #self.relogio.tick(10)
            self.imagem = pygame.image.load("imagens" + os.sep + "explosao" + str(self.contador) + ".jpg")
            self.contador += 1

class Bloco:
    def __init__(self):
        self.barco = None
        self.imagem = pygame.image.load("imagens" + os.sep + "agua.jpg")

    def click(self):
        if not self.tem_barco():
            self.imagem = pygame.image.load("imagens" + os.sep + "errou.jpg")
        else:
            self.imagem = self.barco.imagem

    def tem_barco(self):
        return not self.barco == None

class Mapa:
    def __init__(self, x, y):
        self.matriz = None
        self.x = x
        self.y = y
        self.cria_matriz(10, 10) #ORDEM DA MATRIZ
        self.coloca_barcos(15) #QUANTIDADE BARCO
        self.vida = pygame.image.load("imagens" + os.sep + "vida.jpg") #134,415

        self.coordenadas_porta_avioes = None
        self.coordenadas_submarino = None
        self.coordenadas_navio_de_guerra = None
        self.coordenadas_navio_de_guerraII = None
        self.coordenadas_barco = None

    def cria_matriz(self, linhas, colunas):
        self.matriz = []
        for i in range(linhas):
            self.matriz.append([])
            for j in range(colunas):
                self.matriz[i].append( Bloco() )
                

    def coordenadas_barcos(self, barco):
        if barco == 1:
            return self.coordenadas_porta_avioes

    #METODO QUE DEFINE LUGARES DOS BARCOS E TRATA AS COLISOES
    def coloca_barcos(self, num_barcos):

        #PORTA AVIOES
        self.coordenadas_porta_avioes = []
        inclinacao = random.randint(0,1)
        if inclinacao == 0: #HORIZONTAL
            posicao_x = random.randint(0,9)
            posicao_y = random.randint(0,5)
            for i in xrange(5):
                self.matriz[posicao_x][posicao_y + i].barco = Barco()
                self.coordenadas_porta_avioes.append( (posicao_x, posicao_y + i) )
        elif inclinacao == 1: #VERTICAL
            posicao_x = random.randint(0,5)
            posicao_y = random.randint(0,9)
            for i in xrange(5):
                self.matriz[posicao_x + i][posicao_y].barco = Barco()
                self.coordenadas_porta_avioes.append( (posicao_x + i, posicao_y) )

        #SUBMARINO
        self.coordenadas_submarino = []
        inclinacao = random.randint(0,1)
        if inclinacao == 0: #HORIZONTAL
            #COLOCA EM UMA POSICAO QUE NAO ESTA OCUPADA
            while True:
                if self.coordenadas_submarino != []:
                    break
                posicao_x = random.randint(0,9)
                posicao_y = random.randint(0,6)
                for i in xrange(4):
                    self.coordenadas_submarino.append( (posicao_x, posicao_y + i) )
                    if (posicao_x, posicao_y + i) in self.coordenadas_porta_avioes:
                        self.coordenadas_submarino = []
                        break
            for i in xrange(4):
                self.matriz[posicao_x][posicao_y + i].barco = Barco()
                
        elif inclinacao == 1: #VERTICAL
            #COLOCA EM UMA POSICAO QUE NAO ESTA OCUPADA
            while True:
                if self.coordenadas_submarino != []:
                    break
                posicao_x = random.randint(0,6)
                posicao_y = random.randint(0,9)
                for i in xrange(4):
                    self.coordenadas_submarino.append( (posicao_x + i, posicao_y) )
                    if (posicao_x + i, posicao_y) in self.coordenadas_porta_avioes:
                        self.coordenadas_submarino = []
                        break
            for i in xrange(4):
                self.matriz[posicao_x + i][posicao_y].barco = Barco()
                
        #NAVIO DE GUERRA
        self.coordenadas_navio_de_guerra = []
        inclinacao = random.randint(0,1)
        if inclinacao == 0: #HORIZONTAL
            #COLOCA EM UMA POSICAO QUE NAO ESTA OCUPADA
            while True:
                if self.coordenadas_navio_de_guerra != []:
                    break
                posicao_x = random.randint(0,9)
                posicao_y = random.randint(0,7)                
                for i in xrange(3):
                    self.coordenadas_navio_de_guerra.append( (posicao_x, posicao_y + i) )
                    if (posicao_x, posicao_y + i) in self.coordenadas_porta_avioes or (posicao_x, posicao_y + i) in self.coordenadas_submarino:
                        self.coordenadas_navio_de_guerra = []
                        break
            for i in xrange(3):
                self.matriz[posicao_x][posicao_y + i].barco = Barco()

        elif inclinacao == 1: #VERTICAL
            #COLOCA EM UMA POSICAO QUE NAO ESTA OCUPADA
            while True:
                if self.coordenadas_navio_de_guerra != []:
                    break
                posicao_x = random.randint(0,7)
                posicao_y = random.randint(0,9)
                for i in xrange(3):
                    self.coordenadas_navio_de_guerra.append( (posicao_x + i, posicao_y) )
                    if (posicao_x + i, posicao_y) in self.coordenadas_porta_avioes or (posicao_x + i, posicao_y) in self.coordenadas_submarino:
                        self.coordenadas_navio_de_guerra = []
                        break
            for i in xrange(3):
                self.matriz[posicao_x + i][posicao_y].barco = Barco()

        #NAVIO DE GUERRA II
        self.coordenadas_navio_de_guerraII = []
        inclinacao = random.randint(0,1)
        if inclinacao == 0: #HORIZONTAL
            #COLOCA EM UMA POSICAO QUE NAO ESTA OCUPADA
            while True:
                if self.coordenadas_navio_de_guerraII != []:
                    break
                posicao_x = random.randint(0,9)
                posicao_y = random.randint(0,8)
                for i in xrange(2):
                    self.coordenadas_navio_de_guerraII.append( (posicao_x, posicao_y + i) )
                    if (posicao_x, posicao_y + i) in self.coordenadas_porta_avioes or (posicao_x, posicao_y + i) in self.coordenadas_submarino or (posicao_x, posicao_y + i) in self.coordenadas_navio_de_guerra:
                        self.coordenadas_navio_de_guerraII = []
                        break
            for i in xrange(2):
                self.matriz[posicao_x][posicao_y + i].barco = Barco()
                
        elif inclinacao == 1: #VERTICAL
            #COLOCA EM UMA POSICAO QUE NAO ESTA OCUPADA
            while True:
                if self.coordenadas_navio_de_guerraII != []:
                    break
                posicao_x = random.randint(0,5)
                posicao_y = random.randint(0,8)
                for i in xrange(2):
                    self.coordenadas_navio_de_guerraII.append( (posicao_x + i, posicao_y) )
                    if (posicao_x + i, posicao_y) in self.coordenadas_porta_avioes or (posicao_x + i, posicao_y) in self.coordenadas_submarino or (posicao_x + i, posicao_y) in self.coordenadas_navio_de_guerra:
                        self.coordenadas_navio_de_guerraII = []
                        break
            for i in xrange(2):
                self.matriz[posicao_x + i][posicao_y].barco = Barco()
                
        #BARCO
        self.coordenadas_barco = []
        #COLOCA EM UMA POSICAO QUE NAO ESTA OCUPADA
        while True:
            if self.coordenadas_barco != []:
                break
            posicao_x = random.randint(0,9)
            posicao_y = random.randint(0,9)
            for i in xrange(1):
                self.coordenadas_barco.append( (posicao_x, posicao_y) )
                if (posicao_x, posicao_y) in self.coordenadas_porta_avioes or (posicao_x, posicao_y) in self.coordenadas_submarino or (posicao_x, posicao_y) in self.coordenadas_navio_de_guerra or (posicao_x, posicao_y) in self.coordenadas_navio_de_guerraII:
                    self.coordenadas_barco = []
                    break
        for i in xrange(1):
            self.matriz[posicao_x][posicao_y].barco = Barco()

    def blitar(self, tela):
        for linha in range( len(self.matriz) ):
            for coluna in range( len(self.matriz[0] ) ):
                tela.blit(self.matriz[linha][coluna].imagem, (self.x + 30 * coluna, self.y + 30 * linha) )
