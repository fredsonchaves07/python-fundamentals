from typing import Dict, List


class Client:
    def __init__(self, name):
        self.name = name
        self._addresses: List = []
        self.address_number: str
        self.address_detail: str

    def add_address(self, address):
        self._addresses.append(address)

    def list_addresses(self):
        for address in self._addresses:
            address.show_address(self.address_number, self.address_detail)


class Address:
    def __init__(self, street, neighboor, zip_code):
        self._street = street
        self._neighboor = neighboor
        self._zip_code = zip_code

    def show_address(self, address_number, address_detail):
        print(
            self._street,
            address_number,
            self._neighboor,
            self._zip_code,
            address_detail,
        )


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs):
        return "".join(kwargs.values())

    def get_address(self, **kwargs):
        key = self._get_key(**kwargs)
        try:
            address_flyweight = self._addresses[key]
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()
    a1 = address_factory.get_address(
        street="Avenida Brasil", neighboor="Centro", zip_code="65055-142"
    )
    a2 = address_factory.get_address(
        street="Avenida Brasil", neighboor="Centro", zip_code="65055-142"
    )

    jhon = Client("Jhon")
    jhon.address_number = "50"
    jhon.address_detail = "Casa"
    jhon.add_address(a1)
    jhon.list_addresses()
