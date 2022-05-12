from abc import ABC, abstractmethod


class Colleague(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def broadcast(self, msg):
        pass

    @abstractmethod
    def direct(self, msg):
        pass


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, coleague, msg):
        pass

    @abstractmethod
    def direct(self, sender, receiver, msg):
        pass


class Chatroom(Mediator):
    def __init__(self):
        self.colleagues = []

    def is_colleague(self, colleague):
        return colleague in self.colleagues

    def add(self, coleague):
        if not self.is_colleague(coleague):
            self.colleagues.append(coleague)

    def remove(self, coleague):
        if self.is_colleague(coleague):
            self.colleagues.remove(coleague)

    def broadcast(self, coleague, msg):
        if not self.is_colleague(coleague):
            return
        print(f"{coleague.name} says {msg}")

    def direct(self, sender, receiver, msg):
        if not self.is_colleague(sender):
            return
        receiver_obj = [
            coleague for coleague in self.colleagues if coleague.name == receiver
        ]
        if not receiver_obj:
            return
        receiver_obj[0].direct(f"{sender.name} for {receiver_obj[0].name} says {msg}")


class Person(Colleague):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg):
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver, msg):
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg):
        print(msg)


if __name__ == "__main__":
    chatrom = Chatroom()

    jhon = Person("Jhon", chatrom)
    even = Person("Even", chatrom)
    josef = Person("Josef", chatrom)

    chatrom.add(jhon)
    chatrom.add(even)

    jhon.broadcast("Hello peoples")
    jhon.send_direct("Even", "Hello even")
