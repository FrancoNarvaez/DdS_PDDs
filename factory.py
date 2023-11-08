class Comida:
    def __init__(self, nombre):
        self.nombre = nombre

    def preparar(self):
        pass

class Pizza(Comida):
    def preparar(self):
        print(f"Preparando {self.nombre}")

class Hamburguesa(Comida):
    def preparar(self):
        print(f"Preparando {self.nombre}")

class ComidaFactory:
    def create_comida(self, tipo):
        if tipo == "pizza":
            return Pizza("Pizza")
        elif tipo == "hamburguesa":
            return Hamburguesa("Hamburguesa")
        else:
            print("Tipo de comida no válido")

if __name__ == "__main__":
    pass
