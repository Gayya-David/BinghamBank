from account2 import Account


class StudentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self._withdraw_limit = 2000
        self._deposit_limit = 50000

    def withdraw(self, amount):
        if amount <= self._withdraw_limit:
            super().withdraw(amount)
        else:
            print("withdrawal limit exceeded")

    def deposit(self, amount):
        if amount <= self._deposit_limit:
            super().deposit(amount)
        else:
            print("Deposit limit exceeded")
