from abc import ABC, abstractmethod


class User:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.address = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result():
        pass

    @abstractmethod
    def add_firstname(self, firstname):
        pass

    @abstractmethod
    def add_lastname(self, lastname):
        pass

    @abstractmethod
    def add_age(self, age):
        pass

    @abstractmethod
    def add_phone(self, phone):
        pass

    @abstractmethod
    def add_address(self, address):
        pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        data = self._result
        self.reset()
        return data

    def add_firstname(self, firstname):
        self.result.firstname = firstname

    def add_lastname(self, lastname):
        self.result.lastname = lastname

    def add_age(self, age):
        self.result.age = age

    def add_phone(self, phone):
        self.result.phone_numbers.append(phone)

    def add_address(self, address):
        self.result.address.append(address)


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        return self._builder.result


if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age("Fred", "Chaves", 26)
    user2 = user_director.with_age("Darlynne", "Chaves", 34)
    print(user1, user2)
