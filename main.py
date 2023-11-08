from builder import Pizzeria, Hamburgueseria, cliente

def main():
    pizzeria = Pizzeria()
    hamburgueseria = Hamburgueseria()

    cliente(pizzeria)
    print("\n")
    cliente(hamburgueseria)

if __name__ == "__main__":
    main()