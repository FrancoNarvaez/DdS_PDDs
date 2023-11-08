from observer import ComidaPublisher, ComidaSubscriber

def main():
    comida_pub = ComidaPublisher()

    sub1 = ComidaSubscriber("Comensal 1")
    sub2 = ComidaSubscriber("Comensal 2")

    comida_pub.add_subscriber(sub1)
    comida_pub.add_subscriber(sub2)

    comida_pub.notify_subscribers("La pizza está lista")

    comida_pub.remove_subscriber(sub1)

    comida_pub.notify_subscribers("Las hamburguesas están en la parrilla")

if __name__ == "__main__":
    main()
