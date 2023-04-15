class Humano:
    def __init__(self, nombre: str, edad: int, ocupacion: str):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    
    def presentarse(self):
        print(f'Hola, soy {self.nombre}, tengo {self.edad} anhos y trabajo como {self.ocupacion}')

    def contratar(self, puesto):
        self.puesto = self.ocupacion = puesto
        print(f'Contratado como {self.puesto}')
        
    
    def __str__(self):
        return f"nombre = {self.nombre}, edad = {self.edad}, ocupacion = {self.ocupacion}"

jorge = Humano("Jorge", 23, "Desarrollador")

jorge.presentarse()
jorge.contratar("Desarrollador backend")
print(jorge.__dict__)
print(jorge.__sizeof__())