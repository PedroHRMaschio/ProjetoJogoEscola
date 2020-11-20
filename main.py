#Jogo desvie das notas ruins
import pygame
import random
import time

pygame.init()
relogio = pygame.time.Clock()
pygame.pygame.set_caption("Tire apenas A ou B")

icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

largura = 1080
altura = 720

display = pygame.pygame.set_mode((largura,altura))
background = pygame.image.load("assets/escolinha.png")
aluno = pygame.image.load("assets/aluno.png")

#teste de commit 2
