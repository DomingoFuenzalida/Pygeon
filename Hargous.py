import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

# Función para encontrar la raíz de un componente
def encontrar_raiz(componentes, nodo):
    while nodo != componentes[nodo]:
        nodo = componentes[nodo]
    return nodo

# Función para unir dos componentes en un conjunto
def unir_componentes(componentes, nodo1, nodo2):
    raiz1 = encontrar_raiz(componentes, nodo1)
    raiz2 = encontrar_raiz(componentes, nodo2)
    componentes[raiz2] = raiz1
    

#Funcion General
def triangular(c,x,y):
    c = np.array(c)

    coor = []
    correccion = np.array([x, y])
    for i in c:
        coor.append(i+correccion)
    coor = np.array(coor)
    #print(coor)

    # Triangulación de Delaunay
    triangulacion = Delaunay(coor)

    # Obtener los triángulos
    triangulos = triangulacion.simplices

    # Crear una matriz de distancias entre los puntos
    distancias = np.sqrt(np.sum((coor[:, np.newaxis] - coor) ** 2, axis=2))

    # Crear una lista de aristas y sus pesos
    aristas = []
    for i in range(len(coor)):
        for j in range(i + 1, len(coor)):
            aristas.append((i, j, distancias[i][j]))

    # Ordenar las aristas por peso
    aristas.sort(key=lambda x: x[2])

    # Inicializar el conjunto de componentes conectadas
    componentes = {i: i for i in range(len(coor))}
    
    # Lista para almacenar las aristas del árbol de expansión mínima
    aristas_arbol = []

    # Lista para almacenar las aristas de los loops
    aristas_loops = []

    # Recorrer las aristas en orden ascendente de peso
    for arista in aristas:
        nodo1, nodo2, peso = arista
        if encontrar_raiz(componentes, nodo1) != encontrar_raiz(componentes, nodo2):
            # Verificar aleatoriamente si se realiza la verificación de ciclos
            if np.random.random() < 0.85:
                aristas_arbol.append(arista)
                unir_componentes(componentes, nodo1, nodo2)
            else:
                # Verificar si la inclusión de la arista crea un ciclo
                temp_componentes = componentes.copy()
                unir_componentes(temp_componentes, nodo1, nodo2)
                ciclo = False
                for nodo in temp_componentes:
                    if encontrar_raiz(temp_componentes, nodo) != 0:
                        ciclo = True
                        break
                if ciclo:
                    aristas_loops.append(arista)
                else:
                    aristas_arbol.append(arista)
                    unir_componentes(componentes, nodo1, nodo2)

    # Crear un diccionario para almacenar las conexiones de cada punto
    conexiones = {i: [] for i in range(len(coor))}

    # Agregar las conexiones del árbol de expansión mínima
    for arista in aristas_arbol:
        nodo1, nodo2, _ = arista
        conexiones[nodo1].append(nodo2)
        conexiones[nodo2].append(nodo1)

    # Agregar las conexiones de los loops
    for arista in aristas_loops:
        nodo1, nodo2, _ = arista
        conexiones[nodo1].append(nodo2)
        conexiones[nodo2].append(nodo1)

    # Visualizar el árbol de expansión mínima y los loops
    plt.figure()
    for arista in aristas_arbol:
        punto1 = coor[arista[0]]
        punto2 = coor[arista[1]]
#        plt.plot([punto1[0], punto2[0]], [punto1[1], punto2[1]], 'r')

    for arista in aristas_loops:
        punto1 = coor[arista[0]]
        punto2 = coor[arista[1]]
        plt.plot([punto1[0], punto2[0]], [punto1[1], punto2[1]], 'r--')

#    plt.xlabel('X')
#    plt.ylabel('Y')
#    plt.title('Árbol de Expansión Mínima y Loops')
#    plt.show()

    # Imprimir las conexiones de cada punto
    # Crear una lista para almacenar las conexiones de cada punto
    conexiones = []

    # Agregar las conexiones del árbol de expansión mínima
    for arista in aristas_arbol:
        nodo1, nodo2, _ = arista
        conexiones.append([coor[nodo1].tolist(), coor[nodo2].tolist()])

    # Agregar las conexiones de los loops
    for arista in aristas_loops:
        nodo1, nodo2, _ = arista
        conexiones.append([coor[nodo1].tolist(), coor[nodo2].tolist()])
    conec = []
    # Imprimir las conexiones de cada punto
    for i, conexion in enumerate(conexiones):
        punto = conexion[0]
        conexiones_punto = [conexion[1]]
        conec.append([punto,conexiones_punto[0]])
    return conec






