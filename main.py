#Jogo desvie das notas ruins
from funcoes import escrevendoPlacar, dead, escrevendoVidas
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
letra = [
    pygame.image.load("assets/LetraA.png"),
    pygame.image.load("assets/LetraB.png"),
    pygame.image.load("assets/LetraC.png"),
    pygame.image.load("assets/LetraD.png"),
    pygame.image.load("assets/LetraE.png"),
    pygame.image.load("assets/LetraF.png")]
#parametros aluno
alunoLargura = 130
alunoPosicaoX = 640
alunoPosicaoY = 520
alunoMovimento = 0
alunoVelocidade = 20
#parametros letras
letraLargura = 100
letraAltura = 100
letraPosicaoX = 360
letraPosicaoY = 10 - letraAltura
letraMovimento = 0
letraVelocidade = 5
#musica e sons
pygame.mixer.music.load("assets/MusicaFundo.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
Sucesso = pygame.mixer.Sound("assets/Sucesso.wav")
Errou = pygame.mixer.Sound("assets/Errou.wav")
Morreu = pygame.mixer.Sound("assets/Morreu.wav")
Sucesso.set_volume(0.6)
Errou.set_volume(0.8)
Morreu.set_volume(0.8)
#Variáveis importantes
indiceLetra = random.randrange(0,5)
contador = 0
vida = 5
tirouvida = False
contou = False
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
        alunoPosicaoX = largura - alunoLargura
    display.blit(aluno, (alunoPosicaoX,alunoPosicaoY))
    #aparição e movimentação das letras
    letraPosicaoY = letraPosicaoY + letraVelocidade
    escrevendoPlacar(contador, display)
    escrevendoVidas(vida, display)    
    if letraPosicaoY > altura:
        tirouvida = False
        contou = False
        letraPosicaoY = 10 - letraAltura
        if letraVelocidade < 20:
            letraVelocidade = letraVelocidade + 1
        letraPosicaoX = random.randrange(0,largura-100)
        indiceLetra = random.randrange(0,6)
    display.blit(letra[indiceLetra], (letraPosicaoX,letraPosicaoY))
    #Verificação de colisão
    if indiceLetra == 0:
        if alunoPosicaoY < letraPosicaoY:
            if alunoPosicaoX < letraPosicaoX + letraLargura and letraPosicaoX < alunoPosicaoX + alunoLargura:
                if tirouvida == False:    
                    vida = vida+1
                    contador = contador + 1
                    tirouvida = True
                    pygame.mixer.Sound.play(Sucesso)
            else:
                if tirouvida == False:
                    vida = vida-1
                    tirouvida = True
                    pygame.mixer.Sound.play(Errou)
    elif indiceLetra == 1:
        if alunoPosicaoY < letraPosicaoY:
            if alunoPosicaoX < letraPosicaoX + letraLargura and letraPosicaoX < alunoPosicaoX + alunoLargura:
                if tirouvida == False:    
                    contador = contador + 1
                    tirouvida = True
                    pygame.mixer.Sound.play(Sucesso)
            else:
                if tirouvida == False:
                    vida = vida-1 
                    tirouvida = True
                    pygame.mixer.Sound.play(Errou) 
    else:
        if alunoPosicaoY < letraPosicaoY:
            if alunoPosicaoX < letraPosicaoX + letraLargura and letraPosicaoX < alunoPosicaoX + alunoLargura:
                if tirouvida == False:
                    vida = vida - 1
                    tirouvida = True
                    pygame.mixer.Sound.play(Errou) 
            if contou == False:
                contador = contador + 1
                contou = True


    if vida < 1: 
        dead(display,Morreu)
        letraVelocidade = 5
        letraPosicaoY = 0 - letraAltura
        contador = 0
        vida = 5

    pygame.display.update()
    relogio.tick(60)
print("Volte sempre...")

