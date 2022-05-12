from pybank.person import Person


class Costumer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__account = None

    def insert_account(self, account):
        self.__account = account
