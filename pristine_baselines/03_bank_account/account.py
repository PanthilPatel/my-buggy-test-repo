"""Bank account model.

Contains a bug: `withdraw` rejects a withdrawal that would bring the
balance to exactly 0, even though that should be allowed (only
withdrawals that would push the balance negative should be rejected).
"""


class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = round(balance, 2)
        self.history: list[str] = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance = round(self.balance + amount, 2)
        self.history.append(f"deposit {amount}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        # BUG: should allow withdrawing exactly the full balance
        # (balance - amount == 0 is valid); using `>=` here rejects
        # that case even though the resulting balance would be fine.
        if amount >= self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        self.balance = round(self.balance - amount, 2)
        self.history.append(f"withdraw {amount}")
