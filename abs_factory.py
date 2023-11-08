from abc import ABC, abstractmethod


class Comida(ABC):
    @abstractmethod
    def preparar(self):
        pass


class Pizza(Comida):
    def preparar(self):
        return "Preparando una pizza"


class Hamburguesa(Comida):
    def preparar(self):
        return "Preparando una hamburguesa"


class Postre(Comida):
    def preparar(self):
        return "Preparando un postre"


class Bebida(Comida):
    def preparar(self):
        return "Preparando una bebida"


class ComidaFactory(ABC):
    @abstractmethod
    def crear_comida(self, tipo):
        pass


class PizzaFactory(ComidaFactory):
    def crear_comida(self, tipo):
        if tipo == "pizza":
            return Pizza()
        else:
            raise ValueError("Tipo de comida no válido")


class HamburguesaFactory(ComidaFactory):
    def crear_comida(self, tipo):
        if tipo == "hamburguesa":
            return Hamburguesa()
        else:
            raise ValueError("Tipo de comida no válido")


class PostreFactory(ComidaFactory):
    def crear_comida(self, tipo):
        if tipo == "postre":
            return Postre()
        else:
            raise ValueError("Tipo de comida no válido")


class BebidaFactory(ComidaFactory):
    def crear_comida(self, tipo):
        if tipo == "bebida":
            return Bebida()
        else:
            raise ValueError("Tipo de comida no válido")
