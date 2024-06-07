from account2 import Account


class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self._withdraw_limit = 700000
        self._interest_rate = 0.005

    def get_withdraw_limit(self, amount=0):
        if amount <= self._withdraw_limit:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded")

    def add_interest(self):
        self._balance += self._balance * self._interest_rate
