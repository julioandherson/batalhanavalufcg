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
    pygame.display.set_caption("Batalha Naval - Opcoes")
    if conteudo == "Tela Cheia":
        tela = pygame.display.set_mode( tamanho_da_tela, FULLSCREEN, 32 )
    elif conteudo == "Janela":
        tela = pygame.display.set_mode( tamanho_da_tela, 0, 32 )

    #MUSICA
    pygame.mixer.music.load("audio" + os.sep + "sub_menu.mp3")
    pygame.mixer.music.play(-1)

    sobre_opcao = pygame.mixer.Sound("audio" + os.sep + "sobre_opcao.wav")
    escolhe_opcao = pygame.mixer.Sound("audio" + os.sep + "escolhe_opcao.wav")
    som1, som2, som3 = False, False, False

    #CARREGANDO IMAGENS
    fundo = pygame.image.load("imagens" + os.sep + "opcoes.jpg")
    mira = pygame.image.load("imagens" + os.sep + "mira.png")

    #BOTAO JANELA
    lista_botoes_janela = [pygame.image.load("imagens" + os.sep + "janela" + str(indice + 1) + ".png").convert() for indice in xrange(3)]
    botao_janela = lista_botoes_janela[0]
    medida_janela = botao_janela.get_size()
    posicao_janela = ( largura / 2 - medida_janela[0] / 2, altura / 3 - medida_janela[1] / 2)

    #BOTAO TELA CHEIA
    lista_botoes_tela_cheia = [pygame.image.load("imagens" + os.sep + "tela_cheia" + str(indice + 1) + ".png").convert() for indice in xrange(3)]
    botao_tela_cheia = lista_botoes_tela_cheia[0]
    medida_tela_cheia = botao_tela_cheia.get_size()
    posicao_tela_cheia = ( largura / 2 - medida_janela[0] / 2, altura / 2 - medida_janela[1] / 2)

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

        #MENU (JANELA)
        if posicao_janela[0] <= posicao_mouse[0] <= posicao_janela[0] + medida_janela[0] and posicao_janela[1] <= posicao_mouse[1] <= posicao_janela[1] + medida_janela[1]:
            botao_janela = lista_botoes_janela[1]
            if som1 == False:
                sobre_opcao.play()
                som1 = True

            if clique_mouse[0]:
                botao_janela = lista_botoes_janela[2]
                pressionado = True
            if pressionado and not clique_mouse[0]:
                botao_janela = lista_botoes_janela[2]
                if som1 == True:
                    escolhe_opcao.play()
                    som1 = False
                    tela = pygame.display.set_mode( tamanho_da_tela, 0, 32 )
                    arquivo = open("Tela.txt", "w")
                    arquivo.write("Janela")
                    arquivo.close()
        else:
            botao_janela = lista_botoes_janela[0]
            som1 = False

        #MENU (TELA CHEIA)
        if posicao_tela_cheia[0] <= posicao_mouse[0] <= posicao_tela_cheia[0] + medida_tela_cheia[0] and posicao_tela_cheia[1] <= posicao_mouse[1] <= posicao_tela_cheia[1] + medida_tela_cheia[1]:
            botao_tela_cheia = lista_botoes_tela_cheia[1]
            if som2 == False:
                sobre_opcao.play()
                som2 = True
            if clique_mouse[0]:
                botao_tela_cheia = lista_botoes_tela_cheia[2]
                pressionado = True
            if pressionado and not clique_mouse[0]:
                if som2 == True:
                    escolhe_opcao.play()
                    som2 = False
                    tela = pygame.display.set_mode( tamanho_da_tela, FULLSCREEN, 32 )
                    arquivo = open("Tela.txt", "w")
                    arquivo.write("Tela Cheia")
                    arquivo.close()
        else:
            botao_tela_cheia = lista_botoes_tela_cheia[0]
            som2 = False

        #MENU PRINCIPAL(BOTAO DE VOLTAR)
        if posicao_menu_principal[0] <= posicao_mouse[0] <= posicao_menu_principal[0] + medida_menu_principal[0] and posicao_menu_principal[1] <= posicao_mouse[1] <= posicao_menu_principal[1] + medida_menu_principal[1]:
            botao_menu_principal = lista_botoes_menu_principal[1]
            if som3 == False:
                sobre_opcao.play()
                som3 = True
            if clique_mouse[0]:
                botao_menu_principal = lista_botoes_menu_principal[2]
                pressionado = True
            if pressionado and not clique_mouse[0]:
                if som3 == True:
                    escolhe_opcao.play()
                    som3 = False
                    pygame.mixer.music.stop()
                    return
        else:
            botao_menu_principal = lista_botoes_menu_principal[0]
            som3 = False

        if not clique_mouse[0]:
            pressionado = False
    
        tela.blit(fundo, (0,0) )
        tela.blit(botao_janela, posicao_janela)
        tela.blit(botao_tela_cheia, posicao_tela_cheia)
        tela.blit(botao_menu_principal, posicao_menu_principal)
        tela.blit(mira, posicao_mouse_mira)

        pygame.display.flip()

if __name__ == "__main__":
    main()
