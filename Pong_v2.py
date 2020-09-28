import pygame
from pygame.locals import *
import sys
from random import randint
import tkinter as tk

# Paddle
class Bar():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 25, 150)
    
    def atualizar_posicao(self, move_paddle):
        self.rect[1] += move_paddle
    
    def IA(self, x_bola, y_bola):
        move_IA = 0
        self.y = self.rect[1]
        bobear = randint(1, 10)
        if x_bola > 400 and bobear != 5:
            if self.y > 650:
                move_IA = -1
                return move_IA
            elif self.y < 0:
                move_IA = 1
                return move_IA
            elif y_bola >= self.y:
                move_IA = 1
                return move_IA
            elif y_bola < self.y:
                move_IA = -1
                return move_IA
        else:
            if self.y < 250:
                move_IA = 1
                return move_IA
            elif self.y > 250:
                move_IA = -1
                return move_IA
            elif self.y == 250:
                move_IA = 0
                return move_IA
            elif self.y < 0 or self.y > 600:
                move_IA = 0
                return move_IA

# Bola
class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x - 15, self.y - 15, 30, 30)
    
    def atualizar_posicao_rect(self):
        self.rect = pygame.Rect(self.x - 15, self.y - 15, 30, 30)

def Singleplayer():
    global modo_jogo
    modo_jogo = True
    window.destroy()
    return modo_jogo

def Multiplayer():
    global modo_jogo
    modo_jogo = False
    window.destroy()
    return modo_jogo


# Init
pygame.init()

# Variáveis
move_y_p1 = 0
move_y_p2 = 0
move_x_bola = -1
move_y_bola = 1
score_p1 = 0
score_p2 = 0
modo_jogo = True
count_p1 = 0
count_p2 = 0
cor_p1 = [255, 255, 255]
cor_p2 = [255, 255, 255]

# Janela
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

# Fonte
font_name = pygame.font.match_font("arial")
font = pygame.font.Font(font_name, 50)

# Player
p1 = Bar(0, 250)
p2 = Bar(775, 250)

# Bola
bola = Ball(400, randint(100, 500))

# Clock
Clock = pygame.time.Clock()

# Multiplayer Option
window = tk.Tk()
window.title("MENU")
label_text = tk.Label(window, text="ESCOLHA O MODO DE JOGO", bg="white", foreground="BLACK")
label_text.config(font=("Courier", 18))
label_text.grid(row=1,column=1, pady=15, padx=15)
button_single = tk.Button(window, text="Single Player", bg="white", height=8, width=30, command=Singleplayer)
button_single.grid(row=2,column=1)
button_multi = tk.Button(window, text="Multi Player", bg="white", height=8, width=30, command=Multiplayer)
button_multi.grid(row=3,column=1, pady= 15)
window.geometry("+600+150")
window["bg"] = "white"
window.mainloop()

# Loop
while True:
    # Clock
    Clock.tick(600)

    # Background
    janela.fill((0, 0, 0))

    # Score Board
    text_surface_p1 = font.render(f"SCORE {score_p1}", True, (255, 255, 255))
    text_surface_p2 = font.render(f"SCORE {score_p2}", True, (255, 255, 255))
    janela.blit(text_surface_p1, (50, 50))
    janela.blit(text_surface_p2, (540, 50))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_s:
                if p1.rect[1] < 450:
                    move_y_p1 = 1
            elif event.key == K_w:
                if p1.rect[1] > 0:
                    move_y_p1 = -1
            if not modo_jogo:
                if event.key == K_DOWN:
                    if p2.rect[1] < 450:
                        move_y_p2 = 1
                elif event.key == K_UP:
                    if p2.rect[1] > 0:
                        move_y_p2 = -1
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                move_y_p1 = 0
            elif event.key == K_DOWN or event.key == K_UP:
                move_y_p2 = 0
    
    # Movimento paddles
    p1.atualizar_posicao(move_y_p1)
    if modo_jogo:
        move_y_p2 = p2.IA(bola.x, bola.y)
    p2.atualizar_posicao(move_y_p2)
    
    # Desenhar
    pygame.draw.rect(janela, cor_p1, p1.rect)
    pygame.draw.rect(janela, cor_p2, p2.rect)
    pygame.draw.circle(janela, (255, 255, 255), (bola.x, bola.y), 15)
    pygame.draw.lines(janela, (255, 255, 255), True, [(400, 0), (400, 600)], 10)

    # Movimento bola
    if bola.y >= 575:
        move_y_bola = -move_y_bola
    elif bola.y <= 15:
        move_y_bola = -move_y_bola
    elif bola.x < 0:
        score_p2 += 1
        move_x_bola = -move_x_bola
        bola.x = 400
        bola.y = randint(200, 400)
    elif bola.x > 800: 
        score_p1 +=1
        move_x_bola = -move_x_bola
        bola.x = 400
        bola.y = randint(200, 400)

    bola.atualizar_posicao_rect()
    bola.x += move_x_bola
    bola.y += move_y_bola

    # Colisão e Cores dos Paddles
    if bola.rect.colliderect(p1.rect):
        bola.x += 10
        move_x_bola = -move_x_bola
        cor_p1 = [0, 180, 0]
        if count_p1 == 0:
            count_p1 += 1
        else:
            count_p1 = 1
    elif bola.rect.colliderect(p2.rect):
        bola.x -= 10
        move_x_bola = -move_x_bola
        cor_p2 = [0, 180, 0]
        if count_p2 == 0:
            count_p2 += 1
        else:
            count_p2 = 1
    if count_p1 != 0:
        count_p1 += 1
        if count_p1 == 200:
            count_p1 = 0
            cor_p1 = [255, 255, 255]
    elif count_p2 != 0:
        count_p2 +=1
        if count_p2 == 200:
            count_p2 = 0
            cor_p2 = [255, 255, 255]

    # Refresh
    pygame.display.update()
