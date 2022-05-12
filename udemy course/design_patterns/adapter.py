from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def down(self):
        pass


class Control(IControl):
    def top(self):
        print("Movendo para cima..")

    def right(self):
        print("Movendo para direita..")

    def left(self):
        print("Movendo para esquerda..")

    def down(self):
        print("Movendo para baixo..")


class NewControl:
    def move_top(self):
        print("Movendo para cima..")

    def move_right(self):
        print("Movendo para direita..")

    def move_left(self):
        print("Movendo para esquerda..")

    def move_down(self):
        print("Movendo para baixo..")


class ControlAdapter:
    def __init__(self, new_control):
        self.new_control = new_control

    def top(self):
        self.new_control.move_top()

    def right(self):
        self.new_control.move_right()

    def left(self):
        self.new_control.move_left()

    def down(self):
        self.new_control.move_down()


if __name__ == "__main__":
    new_control = NewControl()
    c1 = ControlAdapter(new_control)

    c1.top()
