class Handler:
    def handle(self, comida):
        pass

    def set_next(self, handler):
        self.next_handler = handler

class Cocinero(Handler):
    def handle(self, comida):
        if comida.tipo == "Pizza":
            print("Cocinero ha preparado una pizza")
            return True
        return False

class ChefPastelero(Handler):
    def handle(self, comida):
        if comida.tipo == "Pastel":
            print("Chef Pastelero ha preparado un pastel")
            return True
        return False

class Hamburguesero(Handler):
    def handle(self, comida):
        if comida.tipo == "Hamburguesa":
            print("Hamburguesero ha preparado una hamburguesa")
            return True
        return False

class Comida:
    def __init__(self, tipo):
        self.tipo = tipo

def cliente(chain):
    comida1 = Comida("Pizza")
    comida2 = Comida("Pastel")
    comida3 = Comida("Hamburguesa")

    print("Enviando solicitud...")
    chain.handle(comida1)
    chain.handle(comida2)
    chain.handle(comida3)

def main():
    cocinero = Cocinero()
    chef_pastelero = ChefPastelero()
    hamburguesero = Hamburguesero()

    cocinero.set_next(chef_pastelero)
    chef_pastelero.set_next(hamburguesero)

    # Usamos la cadena de responsabilidad para preparar comidas
    cliente(cocinero)

if __name__ == "__main__":
    main()
