import Fuenza
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

print(Fuenza.coordenadas())
c = Fuenza.coordenadas()
coor = []
for i in c:
    temp = []
    for j in i:
        j += Fuenza.cuadrado_size/2
        temp.append(j)
    coor.append(temp.copy())
print(coor)

coor = np.array(coor)
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

# Función para encontrar la raíz de un componente
def encontrar_raiz(componentes, nodo):
    while nodo != componentes[nodo]:
        nodo = componentes[nodo]
    return nodo

# Función para unir dos componentes en el conjunto
def unir_componentes(componentes, nodo1, nodo2):
    raiz1 = encontrar_raiz(componentes, nodo1)
    raiz2 = encontrar_raiz(componentes, nodo2)
    componentes[raiz2] = raiz1

# Lista para almacenar las aristas del árbol de expansión mínima
aristas_arbol = []

# Recorrer las aristas en orden ascendente de peso
for arista in aristas:
    nodo1, nodo2, peso = arista
    if encontrar_raiz(componentes, nodo1) != encontrar_raiz(componentes, nodo2):
        aristas_arbol.append(arista)
        unir_componentes(componentes, nodo1, nodo2)

# Visualizar el árbol de expansión mínima
plt.triplot(coor[:, 0], coor[:, 1], triangulacion.simplices)
plt.plot(coor[:, 0], coor[:, 1], 'o')
for arista in aristas_arbol:
    punto1 = coor[arista[0]]
    punto2 = coor[arista[1]]
    plt.plot([punto1[0], punto2[0]], [punto1[1], punto2[1]], 'r')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Árbol de Expansión Mínima')
plt.show()







