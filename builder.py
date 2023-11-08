from abc import ABC, abstractmethod

class Comida(ABC):
    def __init__(self):
        self.preparacion = []

    @abstractmethod
    def preparar(self):
        pass

class Pizza(Comida):
    def preparar(self):
        self.preparacion.append("Masa de pizza")
        self.preparacion.append("Salsa de tomate")
        self.preparacion.append("Queso")
        self.preparacion.append("Ingredientes variados")

class Hamburguesa(Comida):
    def preparar(self):
        self.preparacion.append("Carne de hamburguesa")
        self.preparacion.append("Pan de hamburguesa")
        self.preparacion.append("Lechuga")
        self.preparacion.append("Tomate")
        self.preparacion.append("Cebolla")

class FabricaDeComida(ABC):
    @abstractmethod
    def crear_comida(self):
        pass

class Pizzeria(FabricaDeComida):
    def crear_comida(self):
        comida = Pizza()
        comida.preparar()
        return comida

class Hamburgueseria(FabricaDeComida):
    def crear_comida(self):
        comida = Hamburguesa()
        comida.preparar()
        return comida

def cliente(factory):
    comida = factory.crear_comida()
    print(f"Preparando {comida.__class__.__name__}:")
    for paso in comida.preparacion:
        print(f" - {paso}")


