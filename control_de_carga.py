import numpy as np
# es una extensión de Python, que le agrega mayor soporte para vectores y matrices, constituyendo una biblioteca de
# funciones matemáticas

def ingresar_carga():
    '''Esta funcion permite ingresar los bultos
       retorna el arreglo carga'''
    carga = np.array([]) # genero un arreglo por el momento vacio
    while True:
        peso = int(input("ingrese el peso del bulto: "))

        # condiciones de funcionamiento
        # salir
        if peso < 0:
            print("Salir")
            break

        # si la el peso es mayor a todo
        if peso > 5000:
            print("El peso maximo de un bulto es de 500 kg!")
            continue

        if carga.sum() + peso > 18000:
            print(f"La carga acumulada es de {carga.sum()}")
            print(f"El maximo valor de carga disponible para tranporte es de {18000 - carga.sum()}")
            continue

        carga = np.append(carga, peso)
    return carga

# calcular precios
def calcular_precio(carga):
    '''Esta funcion calcula y retorna el precio total de la carga'''
    cost = 0
    for x in carga:
        y = 0
        if x >= 26 and x <= 300:
            y = x * 1500
        elif x >= 300 and x <= 500:
            y = x * 2500

        cost +=y #costo


    #print("el costo:", cost)

    return cost

carga = ingresar_carga()
cost = calcular_precio(carga)
print("La carga:", carga)
print("carga total", np.sum([carga]))
print("El promedio:", carga.mean())
print("El valor mas grande:", carga.max())
print("El valor menor:", carga.min())
print("El costo total:", cost)


