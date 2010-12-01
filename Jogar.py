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

    #FONTE
    branco = (255, 255, 255)
    fonte = pygame.font.SysFont("comic sans", 28, bold = True)

    venceu = False
    voce_venceu = fonte.render("Parabens!! Voce venceu!! Pressione Esc para retornar ao Menu Principal.", True, branco)
    medida_voce_venceu = voce_venceu.get_size()
    centro_tela_venceu = largura / 2 - medida_voce_venceu[0] / 2, altura / 2 - medida_voce_venceu[1] / 2
    perdeu = False
    voce_perdeu = fonte.render("Que pena!! Voce perdeu!! Pressione Esc para retornar ao Menu Principal.", True, branco)
    medida_voce_perdeu = voce_perdeu.get_size()
    centro_tela_perdeu = largura / 2 - medida_voce_perdeu[0] / 2, altura / 2 - medida_voce_perdeu[1] / 2
    
    #MUSICA E SONS
    pygame.mixer.music.load("audio" + os.sep + "jogando.mp3")
    pygame.mixer.music.play(-1)
    acertou = pygame.mixer.Sound("audio" + os.sep + "acertou.wav")

    #IMAGENS
    campo = pygame.image.load("imagens" + os.sep + "campo.jpg")
    mira = pygame.image.load("imagens" + os.sep + "mira.png")
    vida = pygame.image.load("imagens" + os.sep + "vida.jpg")

    #DESABILITA O CURSOR DO MOUSE
    pygame.mouse.set_visible(False)

    #INSTANCIA O METODO MAPA PARA JOGADOR
    campo_jogador = Mapa(50, 125)
    campo_jogador.coloca_barcos(0)

    #LISTA COM AS COORDENADAS DOS BARCOS DO JOGADOR
    coordenadas_porta_avioes_oponente = campo_jogador.coordenadas_porta_avioes
    coordenadas_submarino_oponente = campo_jogador.coordenadas_submarino
    coordenadas_navio_de_guerra_oponente = campo_jogador.coordenadas_navio_de_guerra
    coordenadas_navio_de_guerraII_oponente = campo_jogador.coordenadas_navio_de_guerraII
    coordenadas_barco_oponente = campo_jogador.coordenadas_barco

    #INSTANCIA O METODO MAPA PARA O OPONENTE
    campo_oponente = Mapa(450, 125)
    campo_oponente.coloca_barcos(0)

    #LISTA COM AS COORDENADAS DOS BARCOS DO OPONENTE
    coordenadas_porta_avioes_jogador = campo_oponente.coordenadas_porta_avioes
    coordenadas_submarino_jogador = campo_oponente.coordenadas_submarino
    coordenadas_navio_de_guerra_jogador = campo_oponente.coordenadas_navio_de_guerra
    coordenadas_navio_de_guerraII_jogador = campo_oponente.coordenadas_navio_de_guerraII
    coordenadas_barco_jogador = campo_oponente.coordenadas_barco

    #COORDENADAS DO JOGADOR
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

    #COORDENADAS DO OPONENTE
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
    #VARIAVEIS PRA DEFINIR VEZ
    vez_jogador = True
    vez_oponente = False

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
                if vez_jogador == True and vez_oponente == False:
                    if not (clique_linha >= 10 or clique_coluna >= 10) and (clique_linha, clique_coluna) in lista_coordenadas:
                        posicao = campo_jogador.matriz[clique_linha][clique_coluna]
                        posicao.click()
                        lista_coordenadas.remove( (clique_linha, clique_coluna) )

                        #QUANDO CLICAR EM ALGUM QUADRADO 
                        if not posicao.click():
                            #SE NAO TIVER BARCO
                            if posicao.tem_barco() == False:
                                vez_jogador = False
                                vez_oponente = True

                            #SE TIVER BARCO
                            elif posicao.tem_barco() == True:
                                acertou.play()
                                vez_jogador = True
                                vez_oponente = False

                                #VERIFICA A COORDENADA QUE O JOGADOR ATINGIU PRA RETIRAR DA LISTA DE COORDENADAS
                                if (clique_linha, clique_coluna) in coordenadas_porta_avioes_oponente:
                                    coordenadas_porta_avioes_oponente.remove( (clique_linha, clique_coluna) )
                                elif (clique_linha, clique_coluna) in coordenadas_submarino_oponente:
                                    coordenadas_submarino_oponente.remove( (clique_linha, clique_coluna) )
                                elif (clique_linha, clique_coluna) in coordenadas_navio_de_guerra_oponente:
                                    coordenadas_navio_de_guerra_oponente.remove( (clique_linha, clique_coluna) )
                                elif (clique_linha, clique_coluna) in coordenadas_navio_de_guerraII_oponente:
                                    coordenadas_navio_de_guerraII_oponente.remove( (clique_linha, clique_coluna) )
                                elif (clique_linha, clique_coluna) in coordenadas_barco_oponente:
                                    coordenadas_barco_oponente.remove( ( clique_linha, clique_coluna) )

            #VEZ OPONENTE
            if vez_jogador == False and vez_oponente == True:       
                #VERIFICA UMA COORDENADA QUE NAO FOI JOGADA
                while True:
                    linha_oponente = randint(0, 9)
                    coluna_oponente = randint(0, 9)
                    if (linha_oponente, coluna_oponente) in lista_coordenadas_oponente:
                        #RETIRA A COORDENADA PRA NAO SER JOGADA 2 VEZES NO MESMO LUGAR
                        lista_coordenadas_oponente.remove( (linha_oponente, coluna_oponente) )
                        break

                posicao_oponente = campo_oponente.matriz[linha_oponente][coluna_oponente]
                posicao_oponente.click()
                
                #QUANDO CLICAR EM ALGUM QUADRADO 
                if not posicao_oponente.click():
                    #SE NAO TIVER BARCO
                    if posicao_oponente.tem_barco() == False:
                        vez_jogador = True
                        vez_oponente = False
                    #SE TIVER BARCO    
                    elif posicao_oponente.tem_barco() == True:
                        acertou.play()
                        vez_jogador = False
                        vez_oponente = True

                        #VERIFICA A COORDENADA QUE O COMPUTADOR ATINGIU PRA RETIRAR DA LISTA DE COORDENADAS
                        if (linha_oponente, coluna_oponente) in coordenadas_porta_avioes_jogador:
                            coordenadas_porta_avioes_jogador.remove( (linha_oponente, coluna_oponente) )
                        elif (linha_oponente, coluna_oponente) in coordenadas_submarino_jogador:
                            coordenadas_submarino_jogador.remove( (linha_oponente, coluna_oponente) )
                        elif (linha_oponente, coluna_oponente) in coordenadas_navio_de_guerra_jogador:
                            coordenadas_navio_de_guerra_jogador.remove( (linha_oponente, coluna_oponente) )
                        elif (linha_oponente, coluna_oponente) in coordenadas_navio_de_guerraII_jogador:
                            coordenadas_navio_de_guerraII_jogador.remove( (linha_oponente, coluna_oponente) )
                        elif (linha_oponente, coluna_oponente) in coordenadas_barco_jogador:
                            coordenadas_barco_jogador.remove( ( linha_oponente, coluna_oponente) )


        #VERIFICA SE O JOGO ACABOU
        if coordenadas_porta_avioes_jogador == [] and coordenadas_submarino_jogador == [] and coordenadas_navio_de_guerra_jogador == [] and coordenadas_navio_de_guerraII_jogador == [] and coordenadas_barco_jogador == []:
            vez_jogador = False
            vez_oponente = False
            perdeu = True
        elif coordenadas_porta_avioes_oponente == [] and coordenadas_submarino_oponente == [] and coordenadas_navio_de_guerra_oponente == [] and coordenadas_navio_de_guerraII_oponente == [] and coordenadas_barco_oponente == []:
            vez_jogador = False
            vez_oponente = False
            venceu = True
                  
        #BLITANDO O FUNDO DE TELA
        tela.blit(campo, (0,0))

        #BLITA OS CAMPOS
        campo_jogador.blitar(tela)
        campo_oponente.blitar(tela)

        #VIDA PORTA AVIOES DO OPONENTE
        for i in coordenadas_porta_avioes_oponente:
            if len(coordenadas_porta_avioes_oponente) == 5:
                tela.blit(vida, (165, 445) )
                tela.blit(vida, (175, 445) )
                tela.blit(vida, (185, 445) )
                tela.blit(vida, (195, 445) )
                tela.blit(vida, (205, 445) )
            elif len(coordenadas_porta_avioes_oponente) == 4:
                tela.blit(vida, (165, 445) )
                tela.blit(vida, (175, 445) )
                tela.blit(vida, (185, 445) )
                tela.blit(vida, (195, 445) )
            elif len(coordenadas_porta_avioes_oponente) == 3:
                tela.blit(vida, (165, 445) )
                tela.blit(vida, (175, 445) )
                tela.blit(vida, (185, 445) )
            elif len(coordenadas_porta_avioes_oponente) == 2:
                tela.blit(vida, (165, 445) )
                tela.blit(vida, (175, 445) )
            elif len(coordenadas_porta_avioes_oponente) == 1:
                tela.blit(vida, (165, 445) )

        #VIDA SUBMARINO DO OPONENTE
        for i in coordenadas_submarino_oponente:
            if len(coordenadas_submarino_oponente) == 4:
                tela.blit(vida, (165, 480) )
                tela.blit(vida, (175, 480) )
                tela.blit(vida, (185, 480) )
                tela.blit(vida, (195, 480) )
            elif len(coordenadas_submarino_oponente) == 3:
                tela.blit(vida, (165, 480) )
                tela.blit(vida, (175, 480) )
                tela.blit(vida, (185, 480) )
            elif len(coordenadas_submarino_oponente) == 2:
                tela.blit(vida, (165, 480) )
                tela.blit(vida, (175, 480) )
            elif len(coordenadas_submarino_oponente) == 1:
                tela.blit(vida, (165, 480) )

        #VIDA NAVIO DE GUERRA DO OPONENTE
        for i in coordenadas_navio_de_guerra_oponente:
            if len(coordenadas_navio_de_guerra_oponente) == 3:
                tela.blit(vida, (165, 510) )
                tela.blit(vida, (175, 510) )
                tela.blit(vida, (185, 510) )
            elif len(coordenadas_navio_de_guerra_oponente) == 2:
                tela.blit(vida, (165, 510) )
                tela.blit(vida, (175, 510) )
            elif len(coordenadas_navio_de_guerra_oponente) == 1:
                tela.blit(vida, (165, 510) )

        #VIDA NAVIO DE GUERRA II DO OPONENTE
        for i in coordenadas_navio_de_guerraII_oponente:
            if len(coordenadas_navio_de_guerraII_oponente) == 2:
                tela.blit(vida, (165, 545) )
                tela.blit(vida, (175, 545) )
            elif len(coordenadas_navio_de_guerraII_oponente) == 1:
                tela.blit(vida, (165, 545) )

        #VIDA BARCO DO OPONENTE
        for i in coordenadas_barco_oponente:
            if len(coordenadas_barco_oponente) == 1:
                tela.blit(vida, (165, 575) )

        #VIDA PORTA AVIOES DO JOGADOR
        for i in coordenadas_porta_avioes_jogador:
            if len(coordenadas_porta_avioes_jogador) == 5:
                tela.blit(vida, (565, 445) )
                tela.blit(vida, (575, 445) )
                tela.blit(vida, (585, 445) )
                tela.blit(vida, (595, 445) )
                tela.blit(vida, (605, 445) )
            elif len(coordenadas_porta_avioes_jogador) == 4:
                tela.blit(vida, (565, 445) )
                tela.blit(vida, (575, 445) )
                tela.blit(vida, (585, 445) )
                tela.blit(vida, (595, 445) )
            elif len(coordenadas_porta_avioes_jogador) == 3:
                tela.blit(vida, (565, 445) )
                tela.blit(vida, (575, 445) )
                tela.blit(vida, (585, 445) )
            elif len(coordenadas_porta_avioes_jogador) == 2:
                tela.blit(vida, (565, 445) )
                tela.blit(vida, (575, 445) )
            elif len(coordenadas_porta_avioes_jogador) == 1:
                tela.blit(vida, (565, 445) )
                    

        #VIDA SUBMARINO DO JOGADOR
        for i in coordenadas_submarino_jogador:
            if len(coordenadas_submarino_jogador) == 4:
                tela.blit(vida, (565, 480) )
                tela.blit(vida, (575, 480) )
                tela.blit(vida, (585, 480) )
                tela.blit(vida, (595, 480) )
            elif len(coordenadas_submarino_jogador) == 3:
                tela.blit(vida, (565, 480) )
                tela.blit(vida, (575, 480) )
                tela.blit(vida, (585, 480) )
            elif len(coordenadas_submarino_jogador) == 2:
                tela.blit(vida, (565, 480) )
                tela.blit(vida, (575, 480) )
            elif len(coordenadas_submarino_jogador) == 1:
                tela.blit(vida, (565, 480) )

        #VIDA NAVIO DE GUERRA DO JOGADOR
        for i in coordenadas_navio_de_guerra_jogador:
            if len(coordenadas_navio_de_guerra_jogador) == 3:
                tela.blit(vida, (565, 510) )
                tela.blit(vida, (575, 510) )
                tela.blit(vida, (585, 510) )
            elif len(coordenadas_navio_de_guerra_jogador) == 2:
                tela.blit(vida, (565, 510) )
                tela.blit(vida, (575, 510) )
            elif len(coordenadas_navio_de_guerra_jogador) == 1:
                tela.blit(vida, (565, 510) )

        #VIDA NAVIO DE GUERRA II DO JOGADOR
        for i in coordenadas_navio_de_guerraII_jogador:
            if len(coordenadas_navio_de_guerraII_jogador) == 2:
                tela.blit(vida, (565, 545) )
                tela.blit(vida, (575, 545) )
            elif len(coordenadas_navio_de_guerraII_jogador) == 1:
                tela.blit(vida, (565, 545) )

        #VIDA BARCO DO JOGADOR
        for i in coordenadas_barco_jogador:
            if len(coordenadas_barco_jogador) == 1:
                tela.blit(vida, (565, 575) )

        #BLITA IMAGEM QUE O JOGADOR PERDEU OU GANHOU
        if perdeu == True:
            tela.blit(voce_perdeu, (centro_tela_perdeu) )
        elif venceu == True:
            tela.blit(voce_venceu, (centro_tela_venceu) )

        #BLITA O CURSO DO MOUSE NA POSICAO DELE
        tela.blit(mira, posicao_mouse_mira)

        #ATUALIZANDO A TELA
        pygame.display.flip()

if __name__ == "__main__":
    main()
