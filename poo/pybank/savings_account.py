from pybank.account import Account


class SavingsAccount(Account):
    def __init__(self, agency, account_number):
        super().__init__(agency, account_number)
        self.limit = 1000

    def deposit(self, value):
        pass

    def withdraw(self, value):
        pass
