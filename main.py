from abs_factory import PizzaFactory, HamburguesaFactory, PostreFactory, BebidaFactory


def main():
    comida_factories = [PizzaFactory(), HamburguesaFactory(), PostreFactory(), BebidaFactory()]

    for factory in comida_factories:
        comida = factory.crear_comida("pizza")
        print(f"En la pizzeria: {comida.preparar()}")

    for factory in comida_factories:
        comida = factory.crear_comida("hamburguesa")
        print(f"En la hamburguesería: {comida.preparar()}")

    for factory in comida_factories:
        comida = factory.crear_comida("postre")
        print(f"En la pastelería: {comida.preparar()}")

    for factory in comida_factories:
        comida = factory.crear_comida("bebida")
        print(f"En la cafetería: {comida.preparar()}")

if __name__ == "__main__":
    main()
