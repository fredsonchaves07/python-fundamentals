from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self):
        pass

    @abstractmethod
    def decrease_volume(self):
        pass

    @abstractmethod
    def power(self):
        pass


class RemoteControl(IRemoteControl):
    def __init__(self, device):
        self._device = device

    def increase_volume(self):
        self._device += 10

    def decrease_volume(self):
        self._device -= 10

    def power(self):
        self._device.power = not self._device.power


class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self):
        pass

    @volume.setter
    def volume(self, volume):
        pass

    @property
    @abstractmethod
    def power(self):
        pass

    @power.setter
    def power(self):
        pass


class TV(IDevice):
    def __init__(self):
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        if not self._power:
            print("TV Desligada!")
            return

        if volume > 100 or volume < 0:
            return

        self._volume = volume
        print(f"Volume é agora {self.volume}")

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self):
        self._power = not self._power


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)

    remote.power()
