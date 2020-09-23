import pygame
import sys
from pygame.locals import *
from random import randint
import tkinter as tk
import os

def perder():
    global contador_pontos
    global contador
    janela = tk.Tk()
    janela.title("PERDEU")
    janela["bg"] = "white"
    janela.iconphoto(False, tk.PhotoImage(file=os.path.join(sys.path[0],"cobra5.png")))
    lb_perdeu = tk.Label(janela, text="GAME OVER!", bg= "white", foreground="red")
    lb_perdeu.grid(row=1, column=1, padx=40, pady=40)
    lb_pontos = tk.Label(janela, text=f'VOCÊ FEZ {pontos} PONTOS\n TAMANHO DA SUA COBRA: {int(pontos//100+3)} PIXEIS', bg="white", foreground="green")
    lb_pontos.grid(row=2, column=1, padx=40, pady=40)
    pygame.quit()
    janela.mainloop()

def nagrade():
    x = randint(10, 380)
    y = randint(10, 380)
    return (x//10*10, y//10*10)

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#INICIALIZAÇÃO PYGAME
pygame.init()
pygame.mixer.init()

#MÚSICA
pygame.mixer.music.load(os.path.join(sys.path[0], "soundtrack.mp3"))
pygame.mixer.music.play()

#CRIAÇÃO DA JANELA
janela = pygame.display.set_mode((400, 400))

#BACKGROUND
bg = pygame.image.load(os.path.join(sys.path[0],"BACKGROUND.png"))

#TÍTULO E ÍCONE
pygame.display.set_caption("SNAKE")
icone = pygame.image.load(os.path.join(sys.path[0],"cobra5.png"))
pygame.display.set_icon(icone)

#COBRA
cobra = [(200, 200), (210, 200), (220, 200)]
cobra_headskin = pygame.image.load(os.path.join(sys.path[0],"cobra3.png"))
cobra_bodyskin = pygame.image.load(os.path.join(sys.path[0],"cobra4.png"))

#DIREÇÕES
CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3
direcao = DIREITA

#FPS
clock = pygame.time.Clock()

#MAÇA
maca = pygame.image.load(os.path.join(sys.path[0],"maça.png"))
maca_posicao = nagrade()

#PONTOS
pontos = 0

#GAME LOOP
while True:
    #FPS
    clock.tick(20)

    #BACKGROUND
    janela.blit(bg, (0, 0))

    #PEGAR MAÇA
    if colisao(cobra[0], maca_posicao):
        maca_posicao = nagrade()
        cobra.append((0, 0))
        pontos += 100

    #VERIFICAÇÃO DE COLISÃO COBRA
    contador = 0
    for i in range(len(cobra)):
        if contador >= 3:
            if colisao(cobra[0], cobra[i]):
                perder()
        contador += 1

    #COLISÃO COM PAREDE
    if cobra[0] == (400, cobra[0][1]) or cobra[0] == (cobra[0][0], 400) or cobra[0] == (0, cobra[0][1]) or cobra[0] == (cobra[0][0], 0):
        perder()

    #OPÇÃO DE FECHAR A JANELA E TECLAS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN:
            if evento.key == K_UP and direcao != BAIXO:
                direcao = CIMA
            if evento.key == K_DOWN and direcao != CIMA:
                direcao = BAIXO
            if evento.key == K_RIGHT and direcao != ESQUERDA:
                direcao = DIREITA
            if evento.key == K_LEFT and direcao != DIREITA:
                direcao = ESQUERDA

    #MOVIMENTAÇÃO
    if direcao == CIMA:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DIREITA:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == BAIXO:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == ESQUERDA:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    # DESENHAR COBRA
    for pos in range(0, len(cobra)):
        if pos == 0:
            janela.blit(cobra_headskin, cobra[pos])
        elif pos != len(cobra) - 1:
            if cobra[pos][1] == cobra[pos + 1][1]:
                cobra_bodyskin = pygame.image.load(os.path.join(sys.path[0],"cobra4.png"))
                janela.blit(cobra_bodyskin, cobra[pos])
            else:
                cobra_bodyskin = pygame.image.load(os.path.join(sys.path[0],"cobra6.png"))
                janela.blit(cobra_bodyskin, cobra[pos])

    #ARRUMANDO AS TUPLAS DA COBRA
    for i in range(len(cobra) -1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    #DESENHAR MAÇA
    janela.blit(maca, maca_posicao)

    #UPDATE
    pygame.display.update()
