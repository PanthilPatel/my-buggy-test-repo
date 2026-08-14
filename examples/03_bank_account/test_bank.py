import pytest

from account import Account, InsufficientFundsError
from transactions import transfer


def test_withdraw_full_balance_is_allowed():
    acc = Account("Alice", balance=100.0)
    acc.withdraw(100.0)
    assert acc.balance == 0.0


def test_withdraw_more_than_balance_raises():
    acc = Account("Bob", balance=50.0)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(50.01)


def test_deposit_increases_balance():
    acc = Account("Carol", balance=10.0)
    acc.deposit(5.5)
    assert acc.balance == 15.5


def test_transfer_recipient_gets_full_amount():
    sender = Account("Dave", balance=200.0)
    recipient = Account("Erin", balance=0.0)
    transfer(sender, recipient, amount=100.0, fee=2.0)
    assert sender.balance == 98.0  # 200 - (100 + 2 fee)
    assert recipient.balance == 100.0  # recipient should get the full amount


def test_transfer_insufficient_funds_raises():
    sender = Account("Frank", balance=10.0)
    recipient = Account("Grace", balance=0.0)
    with pytest.raises(InsufficientFundsError):
        transfer(sender, recipient, amount=9.0, fee=2.0)
