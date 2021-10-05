from abc import ABC, abstractmethod
from random import choice


class Car(ABC):
    @abstractmethod
    def find_costumer(self) -> None:
        pass


class BasicCar(Car):
    def find_costumer(self) -> None:
        print("Basic car...")


class LuxuryCar(Car):
    def find_costumer(self) -> None:
        print("Luxury car...")


class CarFactory(ABC):
    def __init__(self, car_type):
        self.car = self.get_carro(car_type)

    @staticmethod
    @abstractmethod
    def get_carro(self) -> None:
        pass

    def find_costumer(self):
        self.car.find_costumer()


class NorthZoneCarFactory(CarFactory):
    @staticmethod
    def get_carro(car_type: str) -> Car:
        if car_type == "luxury":
            return LuxuryCar()
        if car_type == "basic":
            return BasicCar()
        assert 0, "Car not exist"


class SouthZoneCarFactory(CarFactory):
    @staticmethod
    def get_carro(car_type: str) -> Car:
        if car_type == "basic":
            return BasicCar()
        assert 0, "Car not exist"


if __name__ == "__main__":
    available_car = ["luxury", "basic"]

    for i in range(10):
        car = NorthZoneCarFactory(choice(available_car))
        car.find_costumer()
