## Determine el valor de un pasaje en avión

class Vuelo():
    def __init__(self, DistR, TiempoE):
        self.DistR = DistR
        self.TiempoE = TiempoE
        # metodos
        CostoTotal = self.CostoVuelo(self.DistR)

#CostoTotal = CostoVuelo(DistR)
        if self.DescVuelo(self.DistR, self.TiempoE):
            Descuento  = 0.3 * CostoTotal
            CostoTotal = CostoTotal - Descuento
        print(f' el valor del vuelo es. : {CostoTotal}')

#metodos

    def CostoVuelo (self, DistR):
        ValorKm = 35
        "Esta función retorna el costo de vuelo por kilometros recorridos "
        return DistR * ValorKm

    def DescVuelo (self, DistR, TiempoE ):
        "Esta función me dice si  el viaje  aplica un  descuento  "
        if DistR > 1000 and TiempoE > 7:
             return True
        return False

DistR =int(input("¿distancia ha recorrer en Kilometros?:  "))
TiempoE =int(input("¿Cuantos días se desea quedar?:  "))


CostoVuelo =  Vuelo(DistR, TiempoE)
## hacer validacionde parametros para meter rangos aceptables
























