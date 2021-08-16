from pybank.account import Account


class CheckingAccount(Account):
    def __init__(self, agency, account_number):
        super().__init__(agency, account_number)
        self.limit = 1000
