import Fuenza as F
print("\U00002728")
while True:
    user = input()
    user = user.split(" ")
    if "ventana" in user:
        F.cambio_ventana(int(user[1]), int(user[2]))
    elif "tamaño" in user:
        F.cambiox(int(user[1]))
        F.cambioy(int(user[2]))
    elif "graficar" in user:
        gen = F.gen()
        if not gen:
            F.grafico()
    elif "cantidad" in user:
        F.cantidad(int(user[1]))
    elif "exit" in user: 
        break
    elif "fondo" in user:
        F.fondo(int(user[1]),int(user[2]),int(user[3]))
    elif "room" in user:
        F.habitacion(int(user[1]),int(user[2]),int(user[3]))
    elif "coo" in user:
        print(F.coordenadas())
    elif "probaitem" in user:
        F.probit(float(user[1]))
    elif "probaboss" in user:
        F.probbo(float(user[1]))
        
print("Programa finalizado")