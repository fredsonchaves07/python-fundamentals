class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.address = []

    def add_address(self, address):
        self.address.append(address)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number


if __name__ == "__main__":
    from copy import deepcopy

    fred = Person("Fred", "Chaves")
    fred_address = Address("Av Principal", "100A")
    fred.add_address(fred_address)
    darly = deepcopy(fred)
    darly.firstname = "Darly"
