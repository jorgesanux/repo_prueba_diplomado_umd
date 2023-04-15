class Vehiculo:
    def __init__(self, marca) -> None:
        self.marca = marca
    
    def arrancar(self):
        print("Arrancando...")

class Carro(Vehiculo):
    def __init__(self, marca, modelo) -> None:
        super().__init__(marca)
        self.modelo = modelo

class Avion(Vehiculo):
    def __init__(self, marca, aerolinea) -> None:
        super().__init__(marca)
        self.aerolinea = aerolinea
    
    def volar(self) -> None:
        print("Volar")

avion = Avion("Boeing", "Avianca")

avion.arrancar()
avion.volar()

carro = Carro(marca="Mercedez", modelo="2023")
carro.arrancar()
