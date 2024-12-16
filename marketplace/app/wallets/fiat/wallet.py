from dataclasses import dataclass, field
from datetime import datetime

from marketplace.app.user.user import User

@dataclass
class FiatWallet:
    user: User
    wallet_id: int
    bank_name: str
    account_number:str
    account_holder: str
    routing_number:str
    iban: str | None
    swift_bic: str | None
    wallet_balance: float | None
    deposit_history: dict[str, float] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, float]] = field(default_factory=dict)
    account_status: str | None = None
    last_accessed: datetime | None = None
    encryption_key: str | None = None

    def update_last_accessed(self):
        self.last_accessed = datetime.now()

    def add_deposit(self, date: str, amount: float) -> None:
        self.deposit_history[date] = self.deposit_history.get(date, 0) + amount

    def withdraw_to_bank(self, amount: float, date: str):
        # Check if balance is sufficient
        if self.wallet_balance is None or self.wallet_balance < amount:
            return f"Insufficient funds to withdraw {amount}. Current balance: {self.wallet_balance}"

        # Deduct the amount from the wallet balance
        self.wallet_balance -= amount
        
        # Add the withdrawal to the withdrawal history
        if date not in self.withdrawal_history:
            self.withdrawal_history[date] = {}

        self.withdrawal_history[date]['amount'] = amount
        
        
        # Log the withdrawal
        self.last_accessed = datetime.now()
        
        return f"Withdrawal of {amount} to account {self.account_number} completed on {date}. New balance: {self.wallet_balance}"

    def get_balance(self) -> float:
        # Calculate total deposits (sum of deposit amounts)
        total_deposits = sum(self.deposit_history.values())

        # Calculate total withdrawals (ensure we are summing float values)
        total_withdrawals = sum(
            float(amount) for methods in self.withdrawal_history.values() for amount in methods.values()
        )

        # Return the balance
        return total_deposits - total_withdrawals



    def update_account_status(self, status: str) -> None:
        self.account_status = status

    def is_active(self) -> bool:
        return self.account_status == "Active"

    def __str__(self) -> str:
        return f"FiatWallet(wallet_id={self.wallet_id}, user_id={self.user.user_profile.id}, bank={self.bank_name}, balance={self.get_balance():.2f}, status={self.account_status})"
    




 