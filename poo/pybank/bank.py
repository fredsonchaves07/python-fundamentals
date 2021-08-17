class Bank:
    def __init__(self):
        self.__agencies = [1111, 2222, 3333]
        self.__costumers = []
        self.__accounts = []

    def insert_costumers(self, costumer):
        self.__costumers.append(costumer)

    def insert_accounts(self, account):
        self.__accounts.append(account)

    def authenticate(self, costumer):
        if costumer not in self.__costumers:
            return None
