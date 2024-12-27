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

    def add_deposit_to_history(self, date: str, amount: Decimal) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.deposit_history[date] = self.deposit_history.get(date, Decimal("0.00")) + amount

    def add_withdrawal_to_history(self, date: str, amount: Decimal, method: str) -> None:
        amount = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.withdrawal_history.setdefault(date, {})[method] = amount

    def withdraw_to_bank(self, amount: Decimal, date: str, method: str) -> str:
        if not self.has_sufficient_funds(amount):
            return f"Insufficient funds to withdraw {amount:.2f}. Current balance: {self.wallet_balance:.2f}"

        self.update_balance(amount)
        self.add_withdrawal_to_history(date, amount, method)
        self.update_last_accessed()
        
        if self.user_bank is not None:
            return f"Withdrawal of {amount:.2f} to account {self.user_bank.account_number} completed on {date}. New balance: {self.wallet_balance:.2f}"
        
        return "No bank account linked for withdrawal."
    
    def simulate_bank_transfer(self, amount: Decimal) -> str:
        # Simulate bank transfer here
        if self.user_bank:
            # You can simulate some transaction logic, like checking the bank details or confirming the transfer.
            print(f"Simulating bank transfer of {amount} to bank account: {self.user_bank.account_number}")
            # In reality, this would be replaced with an actual call to a bank API, e.g.:
            # bank_api.withdraw(self.user_bank, amount)
            return "Transfer successful"  # Placeholder message
        
        return "Bank account details are missing."

    def has_sufficient_funds(self, amount: Decimal) -> bool:
        return (self.wallet_balance or Decimal("0.00")) >= amount

    def update_balance(self, amount: Decimal) -> None:
        if self.wallet_balance is None:
            raise ValueError("Wallet balance is None, cannot perform withdrawal.")
        self.wallet_balance -= amount
        self.wallet_balance = self.wallet_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

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
