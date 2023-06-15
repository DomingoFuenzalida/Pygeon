import pygame
import random

def execute(prob_bosss, prob_loots):
    random1 = random.random()
    if random1 <= prob_bosss:
        return ("\U0001F47F")
    elif random1 <= prob_loots + prob_bosss:
        return ("\U00002728")
    else:
        return ("\U0001F92F")

def inside_room(posiciones, x, y, cuadrado_sizex, cuadrado_sizey, cuadrado, prob_boss, prob_item, screen, font):
    for i, pos in enumerate(posiciones):
        inside = font.render(execute(prob_boss, prob_item), True, (255, 255, 255)) 
        if i == 0:
            inside = font.render("\U00002728", True, (255, 255, 255))
        x, y = pos
        pygame.draw.rect(screen, cuadrado, (x, y, cuadrado_sizex, cuadrado_sizey))
        inside_rect = inside.get_rect(center=(x + cuadrado_sizex // 2, y + cuadrado_sizey // 2))
        screen.blit(inside, inside_rect)

print("\U00002728")