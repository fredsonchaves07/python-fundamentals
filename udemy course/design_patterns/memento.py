from copy import deepcopy


class Memento:
    def __init__(self, state):
        self._state = {}
        super().__setattr__("_state", state)

    def get_state(self):
        return self._state

    def __setattr__(self, name, value) -> None:
        raise AttributeError("Error: Class immutable")


class ImageEditor:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def save_state(self):
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento):
        self.__dict__ = memento.get_state()

    def __str__(self):
        return f"{self.__class__.__name__} - {self.__dict__}"


class Caretaker:
    def __init__(self, originator) -> None:
        self._originator = originator
        self._mementos = []

    def backup(self):
        self._mementos.append(self._originator.save_state())

    def restore(self):
        if not self._mementos:
            return
        self._originator.resotre(self._mementos.pop())


if __name__ == "__main__":
    img = ImageEditor("Foto1.jpg", 500, 500)
    caretaker = Caretaker(img)

    caretaker.backup()

    img.name = "FOTO2.jpg"
    img.height = 222

    caretaker.backup()

    img.name = "FOTO3.jpg"
    img.height = 333

    caretaker.backup()

    caretaker.restore()
    print(img)
