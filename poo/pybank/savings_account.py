from pybank.account import Account


class SavingsAccount(Account):
    def __init__(self, agency, account_number):
        super().__init__(agency, account_number)

    def withdraw(self, value):
        if self.__balance < value:
            print("Balance insuficient!")

        self.__balance -= value
