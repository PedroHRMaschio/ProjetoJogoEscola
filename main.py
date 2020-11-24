#Jogo desvie das notas ruins
from funcoes import escrevendoPlacar, dead
import pygame
import random
import time
#inicialização
pygame.init()
relogio = pygame.time.Clock()
#visual
pygame.display.set_caption("Tire apenas A ou B")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)
largura = 1280
altura = 720
display = pygame.display.set_mode((largura,altura))
background = pygame.image.load("assets/escolinha.jpg")
aluno = pygame.image.load("assets/aluno.png")
letra = [pygame.image.load("assets/LetraA.png"),pygame.image.load("assets/LetraB.png"),pygame.image.load("assets/LetraC.png"),pygame.image.load("assets/LetraD.png"),pygame.image.load("assets/LetraE.png"),pygame.image.load("assets/LetraF.png")]
#parametros aluno
alunoLargura = 260
alunoPosicaoX = 640
alunoPosicaoY = 460
alunoMovimento = 0
alunoVelocidade = 10
#parametros letras
letraLargura = 100
letraAltura = 100
letraPosicaoX = 360
letraPosicaoY = 10 - letraAltura
letraMovimento = 0
letraVelocidade = 5
#musica e afins
pygame.mixer.music.load("assets/MusicaFundo.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

indiceLetra = random.randrange(0,5)
contador = 0
vida = 5
#Aqui o jogo começa
while True:
    display.fill((255, 255, 255))
    display.blit(background, (0, 0))
    #Comandos do jogador
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                alunoMovimento = -alunoVelocidade
            elif evento.key == pygame.K_RIGHT:
                alunoMovimento = alunoVelocidade
        if evento.type == pygame.KEYUP:
            alunoMovimento = 0
    #movimentação do aluno
    alunoPosicaoX = alunoPosicaoX + alunoMovimento
    if alunoPosicaoX < 0:
        alunoPosicaoX = 0
    elif alunoPosicaoX > largura - alunoLargura:
        alunoPosicaoX = largura -alunoLargura
    display.blit(aluno, (alunoPosicaoX,alunoPosicaoY))
    #aparição e movimentação das letras
    letraPosicaoY = letraPosicaoY + letraVelocidade
    escrevendoPlacar(contador, display)    
    if letraPosicaoY > altura:
        letraPosicaoX = 10 - letraAltura
        letraVelocidade = letraVelocidade + 1
        letraPosicaoX = random.randrange(0,largura)
        indiceLetra = random.randrange(0,5)
        contador += 1
    display.blit(letra[indiceLetra], (letraPosicaoX,letraPosicaoY))
    #Verificação de colisão
    if alunoPosicaoY < letraPosicaoY + letraAltura:
        if alunoPosicaoX < letraPosicaoX and alunoPosicaoX + alunoLargura > letraPosicaoX or letraPosicaoX + letraLargura > alunoPosicaoX and letraPosicaoX+letraLargura < alunoPosicaoX+alunoLargura:
            vida = vida - 1
            if vida < 1:
                dead(display)
                letraVelocidade = 5
                letraPosicaoY = 0 - letraAltura
                contador = 0
                vida = 5
            
    pygame.display.update()
    relogio.tick(60)
print("Volte sempre...")

