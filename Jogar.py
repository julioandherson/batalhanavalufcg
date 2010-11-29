import pygame
from pygame.locals import *
from sys import exit
import os

from random import randint
from Matriz import Matriz
from Barco import *

def main():
    pygame.init()

    arquivo = open("Tela.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()

    #DEFINICAO DA TELA
    tamanho_da_tela = largura, altura = 800, 600
    pygame.display.set_caption("Batalha Naval - Jogando")
    if conteudo == "Tela Cheia":
        tela = pygame.display.set_mode( tamanho_da_tela, FULLSCREEN, 32 )
    elif conteudo == "Janela":
        tela = pygame.display.set_mode( tamanho_da_tela, 0, 32 )

    #MUSICA
    pygame.mixer.music.load("audio" + os.sep + "jogando.mp3")
    pygame.mixer.music.play(-1)


    #IMAGENS
    campo = pygame.image.load("imagens" + os.sep + "campo.jpg")
    mira = pygame.image.load("imagens" + os.sep + "mira.png")

    #DESABILITA O CURSOR DO MOUSE
    pygame.mouse.set_visible(False)

    #POSICAO ONDE SERA BLITADO AS MATRIZES
    campo_jogador = Mapa(50, 125)
    campo_oponente = Mapa(450, 125)


    lista_coordenadas = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),
                         (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),
                         (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),
                         (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),
                         (4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),
                         (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),
                         (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),
                         (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),
                         (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),
                         (9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)]



    lista_coordenadas_oponente = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),
                                  (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),
                                  (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),
                                  (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),
                                  (4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),
                                  (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),
                                  (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),
                                  (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),
                                  (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),
                                  (9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)]
           
    while True:

        #CAPTURA EVENTOS PELO TECLADO E MOUSE
        tecla_pressionada = pygame.key.get_pressed()
        clique_mouse = pygame.mouse.get_pressed()

        #CAPTURA A POSICAO DO MOUSE
        posicao_mouse = pygame.mouse.get_pos()
        posicao_mouse_mira = (posicao_mouse[0] - 29, posicao_mouse[1] - 29)

        x, y = posicao_mouse_mira[0] + 29, posicao_mouse_mira[1] + 29

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    return

            if event.type == MOUSEBUTTONDOWN:
                clique_linha = (y - campo_jogador.y) / 30
                clique_coluna = (x - campo_jogador.x) / 30


                #VEZ DO JOGADOR
                if not (clique_linha >= 10 or clique_coluna >= 10) and (clique_linha, clique_coluna) in lista_coordenadas:
                    print "Jogador (%d,%d)" % (clique_linha, clique_coluna)
                    posicao = campo_jogador.matriz[clique_linha][clique_coluna]
                    posicao.click()
                    lista_coordenadas.remove( (clique_linha, clique_coluna) )

                    #VEZ OPONENTE
                    if not posicao.tem_barco():
                        
                        linha_oponente = randint(0, 9)
                        coluna_oponente = randint(0, 9)
                        campo_oponente.matriz[linha_oponente][coluna_oponente].click()                       
                        print "Oponente (%d,%d)" % (linha_oponente, coluna_oponente)
                        

        #BLITANDO O FUNDO DE TELA
        tela.blit(campo, (0,0))

        #BLITA OS CAMPOS
        campo_jogador.blitar(tela)
        campo_oponente.blitar(tela)
        
        #BLITA O CURSO DO MOUSE NA POSICAO DELE
        tela.blit(mira, posicao_mouse_mira)

        #ATUALIZANDO A TELA
        pygame.display.flip()

if __name__ == "__main__":
    main()
