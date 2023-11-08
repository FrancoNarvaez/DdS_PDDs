class Command:
    def execute(self):
        pass

class OrderCommand(Command):
    def __init__(self, chef, order):
        self.chef = chef
        self.order = order

    def execute(self):
        self.chef.cook(self.order)

class Chef:
    def cook(self, order):
        if order == "Pizza":
            print("El chef está preparando una pizza")
        elif order == "Hamburguesa":
            print("El chef está preparando una hamburguesa")
        else:
            print("No podemos preparar ese pedido")

if __name__ == "__main__":
    pass
