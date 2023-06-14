import pygame
import random

def execute(prob_bosss, prob_loots):
    random = random.randint(0, 1)
    if random <= prob_bosss:
        return("B")
    else if random <= prob_loots + prob_bosss:
        return("L")
    else>
        return("P")

def inside_room(posiciones, x, y, cuadrado_sizex, cuadrado_sizey, cuadrado, prob_boss, prob_item):
    for i, pos in enumerate(posiciones):
        inside = execute(prob_boss, prob_loot)
        if i == 0:
            inside = "L
        x, y = pos
        game.draw.rect(screen, cuadrado, (x, y, cuadrado_sizex, cuadrado_sizey))
        inside_rect = inside.get_rect(center=(x + cuadrado_sizex // 2, y + cuadrado_sizey // 2))
        screen.blit(inside, inside_rect)
