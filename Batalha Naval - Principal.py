#! /usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
import os

import Jogar
import Instrucoes
import Opcoes
import Creditos

pygame.init()

#CONFIGURACOES DE TELA
tamanho_da_tela = largura, altura = 800, 600
tela = pygame.display.set_mode( tamanho_da_tela, 0, 32 )
tela_cheia = False

#CARREGA SONS
sobre_opcao = pygame.mixer.Sound("audio" + os.sep + "sobre_opcao.wav")
escolhe_opcao = pygame.mixer.Sound("audio" + os.sep + "escolhe_opcao.wav")
som1, som2, som3, som4, som5 = False, False, False, False, False

#CARREGANDO IMAGENS
fundo = pygame.image.load("imagens" + os.sep + "fundo.jpg")
campo = pygame.image.load("imagens" + os.sep + "campo.jpg")
mira = pygame.image.load("imagens" + os.sep + "mira.png")

#BOTAO JOGAR
lista_botoes_jogar = [pygame.image.load("imagens" + os.sep + "jogar" + str(indice + 1) + ".png").convert() for indice in xrange(3)]
botao_jogar = lista_botoes_jogar[0]
medida_jogar = botao_jogar.get_size()
posicao_jogar = ( largura / 2 + medida_jogar[0] / 2, 2 * altura/ 8 - medida_jogar[1] / 2 )

#BOTAO INSTRUCOES
lista_botoes_instrucoes = [pygame.image.load("imagens" + os.sep + "instrucoes" + str(indice + 1) + ".png").convert() for indice in xrange(3)]
botao_instrucoes = lista_botoes_instrucoes[0]
medida_instrucoes = botao_instrucoes.get_size()
posicao_instrucoes = ( largura / 2 + medida_instrucoes[0] / 2, 2 * altura / 5 - medida_instrucoes[1] / 2)

#BOTAO OPCOES
lista_botoes_opcoes = [pygame.image.load("imagens" + os.sep + "opcoes" + str(indice + 1) + ".png").convert() for indice in xrange(3)]
botao_opcoes = lista_botoes_opcoes[0]
medida_opcoes = botao_opcoes.get_size()
posicao_opcoes = ( largura / 2 + medida_opcoes[0] / 2, 2 * altura / 3.75 - medida_opcoes[1] / 2)

#BOTAO CREDITOS
lista_botoes_creditos = [pygame.image.load("imagens" + os.sep + "creditos" + str(indice + 1) + ".png").convert() for indice in xrange(3)]
botao_creditos = lista_botoes_creditos[0]
medida_creditos = botao_creditos.get_size()
posicao_creditos = ( largura / 2 + medida_creditos[0] / 2, 2 * altura / 3.0 - medida_creditos[1] / 2)

#BOTAO SAIR
lista_botoes_sair = [pygame.image.load("imagens" + os.sep + "sair" + str(indice + 1) + ".png").convert() for indice in xrange(3)]
botao_sair = lista_botoes_sair[0]
medida_sair = botao_sair.get_size()
posicao_sair = ( largura / 2 + medida_sair[0] / 2, 2 * altura / 2.5 - medida_sair[1] / 2)

#DESABILITA O CURSOR DO MOUSE
pygame.mouse.set_visible(False)

#GUARDA EM UM ARQUIVO O TIPO DE TELA INICIAL
arquivo = open("Tela.txt", "w")
arquivo.write("Janela")
arquivo.close()

pressionado = False

while True:
    pygame.display.set_caption("Batalha Naval - Menu Principal")

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("audio" + os.sep + "menu.mp3")
        pygame.mixer.music.play(-1)
        
    #CAPTURA A POSICAO DO MOUSE
    posicao_mouse = pygame.mouse.get_pos()
    posicao_mouse_mira = (posicao_mouse[0] - 29, posicao_mouse[1] - 29)

    #CAPTURA EVENTOS PELO TECLADO E MOUSE
    tecla_pressionada = pygame.key.get_pressed()
    clique_mouse = pygame.mouse.get_pressed()

    #MENU (JOGAR)
    if posicao_jogar[0] <= posicao_mouse[0] <= posicao_jogar[0] + medida_jogar[0] and posicao_jogar[1] <= posicao_mouse[1] <= posicao_jogar[1] + medida_jogar[1]:
        botao_jogar = lista_botoes_jogar[1]
        if som1 == False:
            sobre_opcao.play()
            som1 = True
        if clique_mouse[0]:
            botao_jogar = lista_botoes_jogar[2]
            pressionado = True
        if pressionado and not clique_mouse[0]:
            botao_jogar = lista_botoes_jogar[1]
            if som1 == True:
                escolhe_opcao.play()
                som1 = False
                Jogar.main()
    else:
        botao_jogar = lista_botoes_jogar[0]
        som1 = False

    #MENU (INSTRUCOES)
    if posicao_instrucoes[0] <= posicao_mouse[0] <= posicao_instrucoes[0] + medida_instrucoes[0] and posicao_instrucoes[1] <= posicao_mouse[1] <= posicao_instrucoes[1] + medida_instrucoes[1]:
        botao_instrucoes = lista_botoes_instrucoes[1]
        if som2 == False:
            sobre_opcao.play()
            som2 = True
        if clique_mouse[0]:
            botao_instrucoes = lista_botoes_instrucoes[2]
            pressionado = True
        if pressionado and not clique_mouse[0]:
            botao_instrucoes = lista_botoes_instrucoes[1]
            if som2 == True:
                escolhe_opcao.play()
                som2 = False
                Instrucoes.main()
    else:
        botao_instrucoes = lista_botoes_instrucoes[0]
        som2 = False

    #MENU (OPCOES)
    if posicao_opcoes[0] <= posicao_mouse[0] <= posicao_opcoes[0] + medida_opcoes[0] and posicao_opcoes[1] <= posicao_mouse[1] <= posicao_opcoes[1] + medida_opcoes[1]:
        botao_opcoes = lista_botoes_opcoes[1]
        if som3 == False:
            sobre_opcao.play()
            som3 = True
        if clique_mouse[0]:
            botao_opcoes = lista_botoes_opcoes[2]
            pressionado = True
        if pressionado and not clique_mouse[0]:
            botao_opcoes = lista_botoes_opcoes[1]
            if som3 == True:
                escolhe_opcao.play()
                som3 = False
                Opcoes.main()
    else:
        botao_opcoes = lista_botoes_opcoes[0]
        som3 = False

    #MENU (CREDITOS)
    if posicao_creditos[0] <= posicao_mouse[0] <= posicao_creditos[0] + medida_creditos[0] and posicao_creditos[1] <= posicao_mouse[1] <= posicao_creditos[1] + medida_creditos[1]:
        botao_creditos = lista_botoes_creditos[1]
        if som4 == False:
            sobre_opcao.play()
            som4 = True
        if clique_mouse[0]:
            botao_creditos = lista_botoes_creditos[2]
            pressionado = True
        if pressionado and not clique_mouse[0]:
            if som4 == True:
                escolhe_opcao.play()
                som4 = False
                Creditos.main()
    else:
        botao_creditos = lista_botoes_creditos[0]
        som4 = False

    #MENU (SAIR)
    if posicao_sair[0] <= posicao_mouse[0] <= posicao_sair[0] + medida_sair[0] and posicao_sair[1] <= posicao_mouse[1] <= posicao_sair[1] + medida_sair[1]:
        botao_sair = lista_botoes_sair[1]
        if som5 == False:
            sobre_opcao.play()
            som5 = True
        if clique_mouse[0]:
            botao_sair = lista_botoes_sair[2]
            pressionado = True
        if pressionado and not clique_mouse[0]:
            if som5 == True:
                escolhe_opcao.play()
                som5 = False
                exit()
    else:
        botao_sair = lista_botoes_sair[0]
        som5 = False

    if not clique_mouse[0]:
        pressionado = False

    #SAIDA SEM ERRO
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        #SAIDA QUANDO PRESSIONAR ESCAPE
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

        #TELA CHEIA OU JANELA QUANDO PRESSIONA F
        elif tecla_pressionada[K_f]:
            if tela_cheia == False:
                tela = pygame.display.set_mode( tamanho_da_tela, FULLSCREEN, 32 )
                tela_cheia = True
                arquivo = open("Tela.txt", "w")
                arquivo.write("Tela Cheia")
                arquivo.close()
            else:
                tela = pygame.display.set_mode( tamanho_da_tela, 0, 32 )
                arquivo = open("Tela.txt", "w")
                arquivo.write("Janela")
                arquivo.close()

    #BLITANDO AS IMAGENS NA TELA            
    tela.blit(fundo, (0, 0) )
    tela.blit(botao_jogar, posicao_jogar)
    tela.blit(botao_instrucoes, posicao_instrucoes)
    tela.blit(botao_opcoes, posicao_opcoes)
    tela.blit(botao_creditos, posicao_creditos)
    tela.blit(botao_sair, posicao_sair)
    tela.blit(mira, posicao_mouse_mira)

    #ATUALIZANDO A TELA  
    pygame.display.flip()
