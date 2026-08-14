"""Transfer helpers that move money between two Account objects.

Contains a bug: `transfer` deducts the fee from the sender but never
adds the (fee-free) transferred amount... actually it credits the
recipient with `amount` MINUS the fee a second time, effectively
charging the fee twice.
"""

from account import Account, InsufficientFundsError


def transfer(sender: Account, recipient: Account, amount: float, fee: float = 0.0) -> None:
    total_debit = amount + fee
    if total_debit > sender.balance:
        raise InsufficientFundsError(
            f"{sender.owner} cannot cover transfer of {amount} plus fee {fee}"
        )
    sender.withdraw(total_debit)
    # BUG: should credit the recipient with the full `amount`, since
    # the fee was already deducted from the sender above. Subtracting
    # the fee again here shortchanges the recipient.
    recipient.deposit(amount - fee)
