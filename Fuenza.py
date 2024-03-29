import pygame
import random
import Pede as P
import Hargous as H

pygame.init()

# Dimensiones de la ventana
width = pygame.display.Info().current_w
height =  pygame.display.Info().current_h-60
icon = pygame.image.load("icono.ico")
pygame.display.set_icon(icon)
posiciones = []
probb = 0.3
probi = 0.3
def probit(prob):
    global probi
    global probb
    if probb + prob <= 1:
        probi = prob
        return True
    else:
        print("La probabilidad es muy alta, intenta con otro número o cambiando la de los boses")
        return False

def probbo(prob):
    global probb
    global probi
    if probi + prob <= 1:
        probb = prob
        return True
    else:
        print("La probabilidad es muy alta, intenta con otro número o cambiando la de los items")
        return False
    
grosor_pasillo = 10
def grosor_pasillos(grosor):
    global grosor_pasillo
    grosor_pasillo = int(grosor)

# Tamaño de los cuadrados
cuadrado_sizex = 150
cuadrado_sizey = 150

def cambiox(tamaño):
    global cuadrado_sizex
    cuadrado_sizex = tamaño
def cambioy(tamaño):
    global cuadrado_sizey
    cuadrado_sizey = tamaño

# Cantidad de cuadrados a generar (excluyendo el primer cuadrado)
num_cuadrados = 10
def cantidad(numero):
    global num_cuadrados
    num_cuadrados = int(numero) - 1



def cambio_ventana(w, h):
    global screen
    global width
    global height
    width = w
    height = h

cuadrado = (0, 0, 0)
def habitacion(r,g,b):
    global cuadrado
    cuadrado = (r,g,b)


# Color de fondo
background_color = (255, 255, 255)
def fondo(r,g,b):
    global background_color
    background_color = (r,g,b)


# Verificar si dos cuadrados se cruzan
def se_cruzan(x1, y1, x2, y2, sizex, sizey):
    if (abs(x1 - x2) < sizex) and (abs(y1 - y2) < sizey):
        return True
    return False

def generación(width,height,cuadrado_sizex,cuadrado_sizey,num_cuadrados):

    # Generar posiciones aleatorias para los cuadrados
    global posiciones
    global se_cruza
    global x
    global y
    posiciones = []
    x = (width - cuadrado_sizex) // 2
    y = height - 60 - cuadrado_sizey
    posiciones.append((x, y))

    se_cruza = False
    for _ in range(num_cuadrados):
        contador = 0
        if se_cruza == False:
            while True:
                
                x = random.randint(0, width - cuadrado_sizex)
                y = random.randint(0, posiciones[0][1] - cuadrado_sizey)

                se_cruza = False
                for pos in posiciones:
                    if se_cruzan(x, y, pos[0], pos[1], cuadrado_sizex, cuadrado_sizey):
                        se_cruza = True
                        break

                if not se_cruza:
                    break

                if contador == 1000:
                    print("Hay muchas habitaciones")
                    return True
                contador += 1
        if se_cruza == False: 
            posiciones.append((x, y))
    return(se_cruza)

def coordenadas():
    global posiciones
    return posiciones


# Cargar una fuente de texto
def graficar(background_color, posiciones, width, height, x, y, cuadrado_sizex, cuadrado_sizey, se_cruza, cuadrado, probb, probi, grosor_pasillos):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mazmorras")
    font = pygame.font.Font("NotoEmoji-Medium.ttf", 25)
    if se_cruza == False:
        try:
            contenido = []
            font_color = []
            for i, pos in enumerate(posiciones):
                emoji = P.execute(probb, probi)
                contenido.append(emoji)
                if emoji == "💎":
                    font_color.append((60, 60, 255))
                elif emoji == "👹":
                    font_color.append((200,0,0))
                elif emoji == "🤯":
                    font_color.append((255,255,0))
            pasillos = []
            pasillo = H.triangular(posiciones, cuadrado_sizex, cuadrado_sizey)
            for i in pasillo:
                tempa = []
                tempa.append([i[0][0],i[0][1]])
                tempa.append([i[0][0],i[1][1]])
                pasillos.append(tempa)
                tempa = []
                tempa.append([i[0][0],i[1][1]])
                tempa.append([i[1][0],i[1][1]])
                pasillos.append(tempa)
                    
                
                
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                screen.fill(background_color)

                for i in pasillos:
                    pygame.draw.line(screen, (100,100,100), i[0], i[1], grosor_pasillos)

                for i, pos in enumerate(posiciones):
                    inside = font.render(contenido[i], True, font_color[i]) 
                    if i == 0:
                        inside = font.render("💎", True, (60, 60, 255))
                    x, y = pos
                    pygame.draw.rect(screen, cuadrado, (x, y, cuadrado_sizex, cuadrado_sizey))
                    inside_rect = inside.get_rect(center=(x + cuadrado_sizex // 2, y + cuadrado_sizey // 2))
                    screen.blit(inside, inside_rect)
                
                


                pygame.display.flip()
                
        except:
            pass



def grafico():
    global background_color, posiciones, width, height, x, y, cuadrado_sizex, cuadrado_sizey, se_cruza, cuadrado, probb, probi, grosor_pasillo
    return graficar(background_color, posiciones, width, height, x, y, cuadrado_sizex, cuadrado_sizey, se_cruza, cuadrado, probb, probi, grosor_pasillo)

def gen():
    global width,height,cuadrado_sizex,cuadrado_sizey,num_cuadrados
    return generación(width,height,cuadrado_sizex,cuadrado_sizey,num_cuadrados)
