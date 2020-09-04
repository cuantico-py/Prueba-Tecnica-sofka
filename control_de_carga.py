import numpy as np
import sys


# es una extensión de Python, que le agrega mayor soporte para vectores y matrices, constituyendo una biblioteca de
# funciones matemáticas

def ingresar_carga():
    '''Esta funcion permite ingresar los bultos
       retorna el arreglo carga'''
    carga = np.array([]) # genero un arreglo por el momento vacio

   # while True:
       # peso = int(input("ingrese el peso del bulto: "))

    try:

        bultos = int(input("ingrese el numero de bultos: "))


    except ValueError:

        print("valor introducido es incorrecto, solo ingrese un valor númerico entero positivos")
        sys.exit(1)


    peso = np.random.random(bultos) * 600
    print("lista de bultos ",peso)
    # creo una lista de pesos con el numero de bultos indicados por el usuario
    # los valores tomaran un rango entre 0 y 600 kg lo que quiere decir que tenemos un margen del 20% de tener bultos mayores a 500kg

    for x in peso:
        # condiciones de funcionamiento


        # si un bulto es mayor a 500 kg advertirlo
        if x > 500:

            print(f" se detecta un bulto con peso de  {x}, este lote no pasa el bypass")
            continue



        carga = np.append(carga, x)
    return carga
try:
    carga = ingresar_carga()

except ValueError:
    print("No se aceptan numeros negativos")
    sys.exit(1)


if carga.sum()  > 18000:
    print(f"La carga acumulada es de {carga.sum()}")
    print("se excedio el tope maximo de carga del avion por favor ingrese otra lista de pesos ")


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


cost = calcular_precio(carga)
#print("La carga:", carga)
print("carga total", np.sum([carga]))
print("El promedio:", carga.mean())
print("El valor mas grande en peso:", carga.max(),"Kg")
print("El valor menor en peso :", carga.min(),"Kg")
print ("El costo total en pesos es :", cost)


