import pygame
import random

def execute(prob_bosss, prob_loots):
    random = random.randint(0, 1)
    if random <= prob_bosss:
        inside = font.render("B", True, (255, 255, 255))
    elif random <= prob_loots + prob_bosss:
        inside = font.render("L", True, (255, 255, 255))
    else:
        inside = font.render("P", True, (255, 255, 255))

def inside_room(posiciones, x, y, cuadrado_sizex, cuadrado_sizey, cuadrado, prob_boss, prob_item, screen):
    for i, pos in enumerate(posiciones):
        inside = execute(prob_boss, prob_item)
        if i == 0:
            inside = font.render("L", True, (255, 255, 255))
        x, y = pos
        pygame.draw.rect(screen, cuadrado, (x, y, cuadrado_sizex, cuadrado_sizey))
        inside_rect = inside.get_rect(center=(x + cuadrado_sizex // 2, y + cuadrado_sizey // 2))
        screen.blit(inside, inside_rect)
