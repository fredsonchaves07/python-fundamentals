from abc import ABC, abstractmethod


class IObservable(ABC):
    @property
    def state(self):
        pass

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(IObservable):
    def __init__(self):
        self._observers = []
        self._state = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update):
        new_state = {**self._state, **state_update}
        if new_state != self.state:
            self._state = new_state
            self.notify_observers()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def reset_state(self):
        self._observers = {}


class IObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class Smartphone(IObserver):
    def __init__(self, name, observable):
        self._name = name
        self._observable = observable

    def update(self):
        observable_name = self._observable.__class__.__name__
        print(f"{self._name} o objeto {observable_name} foi atualizado")


class WeatherStationFacade:
    def __init__(self):
        self.weather_station = WeatherStation()
        self.smartphone = Smartphone("iPhone", self.weather_station)

        self.weather_station.add_observer(self.smartphone)

    def add_observer(self, observer):
        self.weather_station.add_observer(observer)

    def change_state(self, state):
        self.weather_station.state = state


if __name__ == "__main__":
    weather_station = WeatherStationFacade()
    weather_station.change_state({"temperature": 30})
