from dataclasses import dataclass, field
from datetime import datetime

from marketplace.app.user.user import User
from marketplace.app.user.user_bank import UserBank

@dataclass
class FiatWallet:
    user_id: int | None
    user_bank: UserBank 
    wallet_id: int | None
    wallet_balance: float | None
    last_accessed: datetime | None 
    encryption_key: str | None
    deposit_history: dict[str, float] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, float]] = field(default_factory=dict)

    def add_deposit(self, date: str, amount: float) -> None:
        self.deposit_history[date] = self.deposit_history.get(date, 0) + amount

    def withdraw_to_bank(self, amount: float, date: str):
        if not self.has_sufficient_funds(amount):
            return f"Insufficient funds to withdraw {amount}. Current balance: {self.wallet_balance}"

        self.update_balance(amount)
        self.add_to_withdrawal_history(amount, date)
        self.update_last_accessed()
        if self.user_bank is not None:
            return f"Withdrawal of {amount} to account {self.user_bank.account_number} completed on {date}. New balance: {self.wallet_balance}"

    def has_sufficient_funds(self, amount: float) -> bool:
        return (self.wallet_balance or 0) >= amount

    def update_balance(self, amount: float):
        if self.wallet_balance is None:
            raise ValueError("Wallet balance is None, cannot perform withdrawal.")
        self.wallet_balance -= amount
 

    def add_to_withdrawal_history(self, amount: float, date: str):
        self.withdrawal_history.setdefault(date, {})['amount'] = amount

    def get_balance(self) -> float:
        total_deposits = sum(self.deposit_history.values())
        total_withdrawals = sum(
            float(amount) for methods in self.withdrawal_history.values() for amount in methods.values()
        )
        return total_deposits - total_withdrawals

    def update_last_accessed(self):
        self.last_accessed = datetime.now()

    def __str__(self) -> str:
        return (f"FiatWallet(wallet_id={self.wallet_id}, user_id={self.user_id}, "
                f"bank={self.user_bank.bank_name}, account_number={self.user_bank.account_number}, "
                f"balance={self.get_balance():.2f}, last_accessed={self.last_accessed})")

    




 