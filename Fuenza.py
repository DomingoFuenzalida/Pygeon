#------------------------- Librerías -------------------------
import pygame
import random

#------------------------ Iniciador --------------------------
pygame.init()

#--------------------- Configurar ventana --------------------
# Obtener las dimensiones de la pantalla
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Crear la ventana con las dimensiones de la pantalla
screen = pygame.display.set_mode((screen_width, screen_height-60))

pygame.display.set_caption("Mazmorras")

# Restaurar el cursor del sistema (opcional)
pygame.mouse.set_visible(True)

#--------------------------- Loop ----------------------------
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Código de actualización y renderizado del juego
    screen.fill((20, 20, 20))  # Limpia la pantalla con color negro
    pygame.display.flip()  # Actualiza la pantalla

pygame.quit()