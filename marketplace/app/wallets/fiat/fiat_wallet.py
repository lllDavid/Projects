from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from marketplace.app.user.user_bank import UserBank

@dataclass
class FiatWallet:
    user_id: int | None
    user_bank: UserBank
    wallet_id: int | None
    wallet_balance: Decimal | None
    last_accessed: datetime | None
    encryption_key: str | None
    deposit_history: dict[str, Decimal] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, Decimal]] = field(default_factory=dict)

    def add_deposit(self, date: str, amount: Decimal) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.deposit_history[date] = self.deposit_history.get(date, Decimal("0.00")) + amount

    def withdraw_to_bank(self, amount: Decimal, date: str) -> str:
        if not self.has_sufficient_funds(amount):
            return f"Insufficient funds to withdraw {amount:.2f}. Current balance: {self.wallet_balance:.2f}"

        self.update_balance(amount)
        self.add_to_withdrawal_history(amount, date)
        self.update_last_accessed()
        
        if self.user_bank is not None:
            return f"Withdrawal of {amount:.2f} to account {self.user_bank.account_number} completed on {date}. New balance: {self.wallet_balance:.2f}"
        
        return "No bank account linked for withdrawal."

    def has_sufficient_funds(self, amount: Decimal) -> bool:
        return (self.wallet_balance or Decimal("0.00")) >= amount

    def update_balance(self, amount: Decimal) -> None:
        if self.wallet_balance is None:
            raise ValueError("Wallet balance is None, cannot perform withdrawal.")
        self.wallet_balance -= amount
        self.wallet_balance = self.wallet_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def add_to_withdrawal_history(self, amount: Decimal, date: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.withdrawal_history.setdefault(date, {})['amount'] = amount

    def get_balance(self) -> Decimal:
        total_deposits = sum(self.deposit_history.values())
        total_withdrawals = sum(
            amount for methods in self.withdrawal_history.values() for amount in methods.values()
        )
        current_balance = total_deposits - total_withdrawals
        dec_current_balance = Decimal(current_balance)
        return dec_current_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def update_last_accessed(self) -> None:
        self.last_accessed = datetime.now()

    def __str__(self) -> str:
        return (f"FiatWallet(wallet_id={self.wallet_id}, user_id={self.user_id}, "
                f"bank={self.user_bank.bank_name}, account_number={self.user_bank.account_number}, "
                f"balance={self.get_balance():.2f}, last_accessed={self.last_accessed})")
