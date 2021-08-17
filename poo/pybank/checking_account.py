from pybank.account import Account


class CheckingAccount(Account):
    def __init__(self, agency, account_number):
        super().__init__(agency, account_number)
        self.__limit = 1000

    def withdraw(self, value):
        if self.__balance + self.__limit < value:
            print("Balance insuficient!")

        self.__balance -= value
