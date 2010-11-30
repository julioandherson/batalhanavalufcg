import pygame
from pygame.locals import *
import os


def main():
    
    tela = pygame.display.set_mode( (800,600), 0, 32 )
    pygame.init()
    relogio = pygame.time.Clock()
    contador = 1

    while True:
        #relogio.tick(1)
        explosao = pygame.image.load("imagens" + os.sep + "explosao" + str(contador) + ".jpg")
        contador += 0


        tela.blit(explosao, (400,400))
    
    
    
if __name__ == "__main__":
    main()
