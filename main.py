## Determine el valor de un pasaje en avión


#entradas

DistR =int(input("¿distancia ha recorrer en Kilometros?:  "))
TiempoE =int(input("¿Cuantos días se desea quedar?:  "))
ValorKm = 35

#variables

#funciones

def CostoVuelo (DistR):
    "Esta función retorna el costo de vuelo por kilometros recorridos "
    return DistR * ValorKm

def DescVuelo (DistR, TiempoE ):
    "Esta función me dice si  el viaje  aplica un  descuento  "
    if DistR > 1000 and TiempoE > 7:
        return True
    return False


CostoTotal = CostoVuelo(DistR)
if DescVuelo(DistR, TiempoE):
    CostoTotal  = 0.3 * CostoVuelo(DistR)
print(f' el valor del vuelo es. : {CostoTotal}')

## hacer validacionde parametros para meter rangos aceptables
























