from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account_number):
        self.__agency = agency
        self.__account_number = account_number
        self.__balance = 0

    @property
    def agency(self):
        return self.__agency

    @agency.setter
    def agency(self, agency):
        self.__agency = agency

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    def deposit(self, value):
        if value > 0:
            self.__balance += value

    @abstractmethod
    def withdraw(self, value):
        pass
