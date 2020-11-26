import time
import pygame
def escrevendoPlacar(contador, display):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Pontos: "+str(contador), True, (255, 255, 255))
    display.blit(texto, (10, 10))
def dead(display,Morreu):
    pygame.mixer.music.stop()
    font = pygame.font.SysFont(None, 150)
    texto = font.render("Você Morreu!", True, (0, 0, 0))
    display.blit(texto, (300, 600))
    pygame.display.update()
    pygame.mixer.Sound.play(Morreu) 
    time.sleep(3)
    pygame.mixer.music.play(-1)
def escrevendoVidas(vida, display):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Vidas: "+str(vida), True, (255, 255, 255))
    display.blit(texto, (600, 10))