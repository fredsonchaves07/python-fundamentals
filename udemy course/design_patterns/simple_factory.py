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


class CarFactory:
    @staticmethod
    def get_carro(car_type: str) -> Car:
        if car_type == "luxury":
            return LuxuryCar()
        if car_type == "basic":
            return BasicCar()
        assert 0, "Car not exist"


if __name__ == "__main__":
    available_car = ["luxury", "basic"]

    for i in range(10):
        car = CarFactory.get_carro(choice(available_car))
        car.find_costumer()
