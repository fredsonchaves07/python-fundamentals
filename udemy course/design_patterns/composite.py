from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    def add(self, child):
        pass

    def remove(self, child):
        pass


class Box(BoxStructure):
    def __init__(self, name):
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self):
        for child in self._children:
            child.print_content()

    def get_price(self):
        return sum([child.get_price() for child in self._children])

    def add(self, child):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_content(self):
        print(self.name, self.price)

    def get_price(self):
        return self.price


if __name__ == "__main__":
    shirt1 = Product("Shirt 1", 49.90)
    shirt2 = Product("Shirt 2", 69.90)
    shirt3 = Product("Shirt 3", 89.90)

    box_shirts = Box("Box Shirts")
    box_shirts.add(shirt1)
    box_shirts.add(shirt2)
    box_shirts.add(shirt3)

    box_shirts.print_content()
