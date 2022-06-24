import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')

x_cobra = int(largura/2) 
y_cobra = int(altura/2)

cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

pygame.display.update()