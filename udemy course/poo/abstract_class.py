"""
Classes que possui algo abstrato que não pode ser instanciado
Funciona como uma interface
A classe só não instancia se possuir métodos abstratos
Abstrai um conceito
"""

from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def speak(self):
        pass


class Male(Person):
    def speak(self):
        print("Male speak..")


jhon = Male()
jhon.speak()
