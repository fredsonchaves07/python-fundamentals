from abc import ABC, abstractmethod


class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self):
        pass

    @abstractmethod
    def get_all_user_data(self):
        pass


class RealUser(IUser):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @abstractmethod
    def get_addresses(self):
        return [{"Rua": "Avenida Brasil", "Número": 500}]

    @abstractmethod
    def get_all_user_data(self):
        return {"address": [{"Rua": "Avenida Brasil", "Número": 500}], "CPF": "1111111"}


class IUserProxy(IUser):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser

    def get_real_user(self):
        if not hasattr(self, "_real_user"):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self):
        return self.get_addresses()

    def get_all_user_data(self):
        return self.get_all_user_data()
