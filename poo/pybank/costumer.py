from pybank.person import Person


class Costumer(Person):
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self.account = account
