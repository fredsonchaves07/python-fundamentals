from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.operation1()
        self.operation2()

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass


class ConcreteClass(Abstract):
    def operation1(self):
        print("Operation 1 finish!")

    def operation2(self):
        print("Operation 2 finish!")


if __name__ == "__main__":
    c1 = ConcreteClass()
    c1.template_method()
