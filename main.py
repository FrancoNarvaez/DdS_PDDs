from factory import ComidaFactory

def main():
    factory = ComidaFactory()

    comida1 = factory.create_comida("pizza")
    comida1.preparar()

    comida2 = factory.create_comida("hamburguesa")
    comida2.preparar()

if __name__ == "__main__":
    main()
