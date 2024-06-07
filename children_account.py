from account2 import Account


class ChildrenAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self._interest_rate = 0.007

    def withdraw(self, amount):
        print("Withdrawal allowed for Children Account")
