import pygame
from pygame.locals import *
from sys import exit
import os

def main():
    pygame.init()

    arquivo = open("Tela.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()

    #DEFINICAO DA TELA
    tamanho_da_tela = largura, altura = 800, 600
    pygame.display.set_caption("Batalha Naval - Creditos")
    if conteudo == "Tela Cheia":
        tela = pygame.display.set_mode( tamanho_da_tela, FULLSCREEN, 32 )
    elif conteudo == "Janela":
        tela = pygame.display.set_mode( tamanho_da_tela, 0, 32 )

    #MUSICA
    pygame.mixer.music.load("audio" + os.sep + "sub_menu.mp3")
    pygame.mixer.music.play(-1)

    sobre_opcao = pygame.mixer.Sound("audio" + os.sep + "sobre_opcao.wav")
    escolhe_opcao = pygame.mixer.Sound("audio" + os.sep + "escolhe_opcao.wav")
    som1 = False

    #CARREGANDO IMAGENS
    jaca_game = pygame.image.load("imagens" + os.sep + "jacagame.png").convert_alpha()
    creditos = pygame.image.load("imagens" + os.sep + "creditos.jpg").convert()
    mira = pygame.image.load("imagens" + os.sep + "mira.png")

    #BOTAO MENU PRINCIPAL
    lista_botoes_menu_principal = [pygame.image.load("imagens" + os.sep + "menu_principal" + str(indice + 1) + ".png").convert() for indice in xrange(3)]
    botao_menu_principal = lista_botoes_menu_principal[0]
    medida_menu_principal = botao_menu_principal.get_size()
    posicao_menu_principal = (500, 500)

    #DESABILITA O CURSOR DO MOUSE
    pygame.mouse.set_visible(False)

    pressionado = False
    
    while True:
        #CAPTURA A POSICAO DO MOUSE
        posicao_mouse = pygame.mouse.get_pos()
        posicao_mouse_mira = (posicao_mouse[0] - 29, posicao_mouse[1] - 29)

        #CAPTURA EVENTOS PELO MOUSE
        clique_mouse = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    return


        #MENU PRINCIPAL(BOTAO DE VOLTAR)
        if posicao_menu_principal[0] <= posicao_mouse[0] <= posicao_menu_principal[0] + medida_menu_principal[0] and posicao_menu_principal[1] <= posicao_mouse[1] <= posicao_menu_principal[1] + medida_menu_principal[1]:
            botao_menu_principal = lista_botoes_menu_principal[1]
            if som1 == False:
                sobre_opcao.play()
                som1 = True
            if clique_mouse[0]:
                botao_menu_principal = lista_botoes_menu_principal[2]
                pressionado = True
            if pressionado and not clique_mouse[0]:
                if som1 == True:
                    escolhe_opcao.play()
                    som1 = False
                    pygame.mixer.music.stop()
                    return
        else:
            botao_menu_principal = lista_botoes_menu_principal[0]
            som1 = False

        if not clique_mouse[0]:
            pressionado = False
    
        tela.blit(creditos, (0,0) )
        tela.blit(jaca_game, (300,250) )
        tela.blit(botao_menu_principal, posicao_menu_principal)
        tela.blit(mira, posicao_mouse_mira)

        pygame.display.flip()

if __name__ == "__main__":
    main()
