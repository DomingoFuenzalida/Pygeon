#------------------------- Librerías -------------------------
import pygame
import sys
import random

#------------------------ Iniciador --------------------------
pygame.init()

#------------------------- Cuadrado 1 ------------------------
tamaño = 100
X = int(pygame.display.Info().current_w // 2 - tamaño/2)
Y = int(pygame.display.Info().current_h // 3 * 2)

color = (200, 20, 100)
# Crear un objeto de fuente
font = pygame.font.Font(None, 32)
text_color = (255, 255, 255)

#------------------------- Cuadrado 2 ------------------------

X2 = random.randint(X  - 200, X + 200)
Y2 = random.randint(Y - tamaño - 100, Y - tamaño-10)



#--------------------- Configurar ventana --------------------
# Obtener las dimensiones de la pantalla
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Crear la ventana con las dimensiones de la pantalla
screen = pygame.display.set_mode((screen_width, screen_height-60))

pygame.display.set_caption("Mazmorras")

# Restaurar el cursor del sistema (opcional)
pygame.mouse.set_visible(True)

#--------------------------- Loop ----------------------------
screen.fill((0, 0, 0))  # Limpia la pantalla con color negro

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Dibujar el cuadrado en la pantalla
    pygame.draw.rect(screen, color, (X, Y, tamaño, tamaño))
    pygame.draw.rect(screen, color, (X2, Y2, tamaño, tamaño))

    # Renderizar el texto en una superficie
    text_surface = font.render("1", True, text_color)
    text_surface2 = font.render("2", True, text_color)

    # Obtener las dimensiones del texto
    text_width, text_height = text_surface.get_size()

    # Calcular la posición para centrar el texto en el cuadrado
    text_x = X + (tamaño - text_width) // 2
    text_y = Y + (tamaño - text_height) // 2
    text_x2 = X2 + (tamaño - text_width) // 2
    text_y2 = Y2 + (tamaño - text_height) // 2

    # Blit (copiar) la superficie del texto en la ventana principal
    screen.blit(text_surface, (text_x, text_y))
    screen.blit(text_surface2, (text_x2, text_y2))

    # Código de actualización y renderizado del juego
    
    pygame.display.flip()  # Actualiza la pantalla

