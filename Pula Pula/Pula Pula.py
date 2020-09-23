import pygame as py
import sys
from pygame.locals import *
import tkinter as tk
from functools import partial
import os

def acao_personagem():
    global personagem_mexey
    global pico
    global pulou
    if len(onde_personagem) == 1:
        onde_personagem.pop()
    if pulou:
        if not pico:
            personagem_mexey -= 5
            janela.blit(personagem_pulando, (80, personagem_mexey))
            onde_personagem.append((80 , personagem_mexey))
            if personagem_mexey == 280:
                pico = True
        elif pico:
            janela.blit(personagem_pulando, (80, personagem_mexey))
            personagem_mexey += 5
            onde_personagem.append((80, personagem_mexey))
            if personagem_mexey == 350:
                pico = False
                pulou = False
    else:
        janela.blit(personagem, (80, personagem_mexey))
        onde_personagem.append((80, personagem_mexey))

def spawn_inimigos():
    global contador_tick
    for i in range(0, len(inimigos)-1):
        janela.blit(inimigo, inimigos[i])
        inimigos[i] = (inimigos[i][0] - 10, inimigos[i][1])
        if inimigos[i] == (-10, 350):
            del inimigos[i]
    if contador_tick % 120  == 0:
        inimigos.append((660, 350))
    contador_tick += 3

def fechar_janelas(janela):
    py.quit()
    sys.exit()
    janela.destroy()

def perder():
    janela_tk = tk.Tk()
    janela_tk.title("GAME OVER")
    janela_tk.iconphoto(False, tk.PhotoImage(file=os.path.join(sys.path[0],"PERSONAGEM.png")))
    janela_tk["bg"] = "WHITE"
    label_perdeu = tk.Label(janela_tk, text="GAME OVER!", background="WHITE", foreground="RED")
    label_perdeu.grid(row=1, column=1, padx=50, pady=30)
    label_pontos = tk.Label(janela_tk, text=f"VOCÊ FEZ {contador_pontos} PONTOS", background="WHITE", foreground="GREEN")
    label_pontos.grid(row=2, column=1, padx=50, pady=30)
    buttom_okay = tk.Button(janela_tk, text="OKAY :(", foreground="BLACK")
    buttom_okay["command"] =partial(fechar_janelas, janela_tk)
    buttom_okay.grid(row=3, column=1, pady=50)
    janela_tk.mainloop()

def colisao():
    global contador_pontos
    if inimigos[0][0] == 90:
        if onde_personagem[0][1] > 300:
            perder()
        else:
            contador_pontos += 1

#INICIALIZAÇÃO
py.init()
py.mixer.init()

#MÚSICA
py.mixer.music.load(os.path.join(sys.path[0],"soundtrack.mp3"))
py.mixer.music.play()

#BACKGROUND
bg = py.image.load(os.path.join(sys.path[0],"BACKGROUND.png"))
mexe_x = -10

#JANELA
janela = py.display.set_mode((600, 600))
py.display.set_icon(py.image.load(os.path.join(sys.path[0],"PERSONAGEM.png")))
py.display.set_caption("PULA PULA")

#PERSONAGEM
personagem = py.image.load(os.path.join(sys.path[0],"PERSONAGEM.png"))
personagem_pulando = py.image.load(os.path.join(sys.path[0],"PERSONAGEM_PULANDO.png"))
personagem_mexey = 350
#VARIÁVEIS
pulou = False
pico = False
contador_tick = 0
contador_pontos = 0
inimigos = [(650, 350)]
onde_personagem = []

#INIMIGOS
inimigo = py.image.load(os.path.join(sys.path[0],"INIMIGO_CERTO.png"))

#FPS
clock = py.time.Clock()
while True:
    #FPS
    clock.tick(60)
    #BACKGROUND
    if mexe_x == -1800:
        mexe_x = 0
    else:
        mexe_x -= 10
    janela.blit(bg, (mexe_x, 0))
    #FECHAR JANELA E PULO
    for evento in py.event.get():
        if evento.type == py.QUIT:
            py.quit()
            sys.exit()
        if evento.type == KEYDOWN and personagem_mexey == 350:
            if evento.key == K_SPACE:
                pulou = True
    #PERSONAGEM
    acao_personagem()
    #INIMIGO
    spawn_inimigos()
    #COLISÃO
    colisao()
#REFRESH
    py.display.update()
