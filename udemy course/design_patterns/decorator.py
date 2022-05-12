from abc import ABC
from copy import deepcopy
from dataclasses import dataclass
from typing import List


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.5


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.5


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PortatoStick(Ingredient):
    price: float = 0.99


class HotDog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self):
        return round(sum([ingredient.price for ingredient in self.ingredients]), 2)

    @property
    def name(self):
        return self._name

    @property
    def ingredients(self):
        return self._ingredients


class SimpleHotDog(HotDog):
    def __init__(self):
        self._name = "Simple HotDog"
        self._ingredients = [Bread(), Sausage(), PortatoStick()]


class SpecialHotDog(HotDog):
    def __init__(self):
        self._name = "Special HotDog"
        self._ingredients = [Bread(), Sausage(), PortatoStick(), Bacon()]


if __name__ == "__main__":
    simple_hot_dog = SimpleHotDog()
    print(simple_hot_dog.price)

    special_hot_dog = SpecialHotDog()
    print(special_hot_dog.price)
