from abc import ABC, abstractmethod


class Light:
    def __init__(self, name, room_name):
        self.name = name
        self.room_name = room_name
        self.color = "Defautl color"

    def on(self):
        print(f"Light {self.name} in {self.room_name} is now ON")

    def off(self):
        print(f"Light {self.name} in {self.room_name} is now OFF")

    def change_color(self, color):
        self.color = color
        print(f"Light {self.name} in {self.room_name} is now {self.color}")


class IComand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class LightOnComand(IComand):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class RemoteController:
    def __init__(self):
        self._buttons = {}

    def button_add_command(self, name, command):
        self._buttons[name] = command

    def button_execute(self, name):
        if name not in self._buttons:
            raise Exception("Button not already exist")
        self._buttons[name].execute()

    def button_addon(self, name):
        if name not in self._buttons:
            raise Exception("Button not already exist")
        self._buttons[name].undo()


if __name__ == "__main__":
    bedroom_ligh = Light("Luz 1", "Quarto")
    bathroom_ligh = Light("Luz 10", "Banheiro")
    bedroom_ligh_on = LightOnComand(bedroom_ligh)
    bathroom_ligh_on = LightOnComand(bathroom_ligh)
    remote = RemoteController()
    remote.button_add_command("First button", bedroom_ligh_on)
    remote.button_execute("First button")
