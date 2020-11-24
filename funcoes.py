import time
import pygame
def escrevendoPlacar(contador, display):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Pontos: "+str(contador), True, (255, 255, 255))
    display.blit(texto, (10, 10))
def dead(display):
    pygame.mixer.music.stop()
    font = pygame.font.SysFont(None, 150)
    texto = font.render("Você Morreu!", True, (0, 0, 0))
    display.blit(texto, (300, 600))
    pygame.display.update()
    time.sleep(5)