import time
import pygame
def escrevendoPlacar(contador):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Pontos: "+str(contador), True, (255, 255, 255))
    display.blit(texto, (10, 10))
def dead():
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    font = pygame.font.SysFont(None, 150)
    texto = font.render("Você Morreu!", True, (0, 0, 0))
    display.blit(texto, (100, 200))
    pygame.display.update()
    time.sleep(5)