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
trian = Delaunay(coor)

triangulos = coor[trian.simplices]

# Visualizar la triangulación
plt.triplot(coor[:, 0], coor[:, 1], trian.simplices)
plt.plot(coor[:, 0], coor[:, 1], 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangulación de Delaunay')
plt.show()