import pygame
import sys
import random

pygame.init()

# Dimensiones de la ventana
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h-60


# Tamaño de los cuadrados
cuadrado_size = 150

# Cantidad de cuadrados a generar (excluyendo el primer cuadrado)
num_cuadrados = int(input("Ingrese número de habitaciones: "))-1

# Crear la ventana
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuadrados Numerados")

# Color de fondo
background_color = (255, 255, 255)

# Verificar si dos cuadrados se cruzan
def se_cruzan(x1, y1, x2, y2, size):
    if (abs(x1 - x2) < size) and (abs(y1 - y2) < size):
        return True
    return False

# Generar posiciones aleatorias para los cuadrados
posiciones = []
x = (width - cuadrado_size) // 2
y = height - 60 - cuadrado_size
posiciones.append((x, y))

for _ in range(num_cuadrados):
    contador = 0
    while True:
        
        x = random.randint(0, width - cuadrado_size)
        y = random.randint(0, posiciones[0][1] - cuadrado_size)

        se_cruza = False
        for pos in posiciones:
            if se_cruzan(x, y, pos[0], pos[1], cuadrado_size):
                se_cruza = True
                break

        if not se_cruza:
            break

        if contador == 1000:
            print("Hay muchas habitaciones")
            break
        contador += 1

    posiciones.append((x, y))

def coordenadas():
    global posiciones
    return posiciones


# Cargar una fuente de texto
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)

    # Dibujar los cuadrados en las posiciones generadas y agregar números
    for i, pos in enumerate(posiciones):
        x, y = pos
        pygame.draw.rect(screen, (255, 0, 0), (x, y, cuadrado_size, cuadrado_size))

        # Renderizar el número en el centro del cuadrado
        numero = font.render(str(i+1), True, (255, 255, 255))
        numero_rect = numero.get_rect(center=(x + cuadrado_size // 2, y + cuadrado_size // 2))
        screen.blit(numero, numero_rect)

    pygame.display.flip()
