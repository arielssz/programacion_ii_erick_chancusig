class Guerrero:
    nombre: str
    def __init__(self, nombre:str):
        self.nombre =nombre 

    def atacar (self):
        print (f"{self.nombre}realiza un ataque ")

class Goku(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre)

    def atacar (self):
        print (self.nombre, "Utiliza Kamehameha")

    def calcular_poder (self):
        return self.poder_inicial + self.horas*150

class Vegeta(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def atacar (self):
        print (self.nombre , "utiliza final flash")

    def calcular_poder (self):
            return self.poder_inicial + self.horas*150
    


goku =Goku ("Gran goku")
vegeta = Vegeta ("Vegeta")
goku.atacar ()
vegeta.atacar()
goku.calcular_poder ()
vegeta.calcular_poder ()