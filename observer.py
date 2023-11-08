class ComidaPublisher:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

class ComidaSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} recibió el mensaje: {message}")

if __name__ == "__main__":
    pass
