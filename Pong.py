import pygame
from pygame.locals import *
import sys
from random import randint


# Classes
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
            if self.y < 300:
                move_IA = 1
                return move_IA
            elif self.y > 300:
                move_IA = -1
                return move_IA
            elif self.y == 300:
                move_IA = 0
                return move_IA
            elif self.y < 0 or self.y > 600:
                move_IA = 0
                return move_IA

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x - 15, self.y - 15, 30, 30)
    
    def atualizar_posicao_rect(self):
        self.rect = pygame.Rect(self.x - 15, self.y - 15, 30, 30)


# Init
pygame.init()

# Variáveis
move_y_p1 = 0
move_y_p2 = 0
move_x_bola = -1
move_y_bola = 1
score_p1 = 0
score_p2 = 0

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
bola = Ball(randint(100, 700), randint(100, 500))

# Clock
Clock = pygame.time.Clock()

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
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                move_y_p1 = 0
    
    # Movimento paddles
    p1.atualizar_posicao(move_y_p1)
    move_y_p2 = p2.IA(bola.x, bola.y)
    p2.atualizar_posicao(move_y_p2)
    
    # Desenhar
    pygame.draw.rect(janela, (255, 255, 255), p1.rect)
    pygame.draw.rect(janela, (255, 255, 255), p2.rect)
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
        bola.x = randint(250, 550)
        bola.y = randint(200, 400)
    elif bola.x > 800: 
        score_p1 +=1
        move_x_bola = -move_x_bola
        bola.x = randint(250, 550)
        bola.y = randint(200, 400)

    bola.atualizar_posicao_rect()
    bola.x += move_x_bola
    bola.y += move_y_bola

    # Colisão
    if bola.rect.colliderect(p1.rect):
        bola.x += 10
        move_x_bola = -move_x_bola
    elif bola.rect.colliderect(p2.rect):
        bola.x -= 10
        move_x_bola = -move_x_bola
    
    # Refresh
    pygame.display.update()
