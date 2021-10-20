from abc import ABC, abstractmethod


class Order:
    def __init__(self, total, discount):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStategy(ABC):
    @abstractmethod
    def calculate(self, value):
        pass


class TwentyPercent(DiscountStategy):
    def calculate(self, value):
        return value - (value * 0.2)


if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    order = Order(1000, twenty_percent)
    print(order.total)
    print(order.total_with_discount)
