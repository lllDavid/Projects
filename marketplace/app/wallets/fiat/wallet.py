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
    deposit_history: dict[str, float] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, str]] = field(default_factory=dict)
    account_status: str | None = None
    last_accessed: datetime | None = None
    encryption_key: str | None = None

    def update_last_accessed(self):
        self.last_accessed = datetime.now()

    def add_deposit(self, date: str, amount: float) -> None:
        self.deposit_history[date] = self.deposit_history.get(date, 0) + amount

    def add_withdrawal(self, date: str, amount: float, method: str) -> None:
        self.withdrawal_history.setdefault(date, {})[method] = f"${amount:.2f}"

    def get_balance(self) -> float:
        total_deposits = sum(self.deposit_history.values())
        total_withdrawals = sum(
            float(amount.split('$')[1]) for methods in self.withdrawal_history.values() for amount in methods.values()
        )
        return total_deposits - total_withdrawals

    def update_account_status(self, status: str) -> None:
        self.account_status = status

    def is_active(self) -> bool:
        return self.account_status == "Active"

    def __str__(self) -> str:
        return f"FiatWallet(wallet_id={self.wallet_id}, user_id={self.user.user_profile.id}, bank={self.bank_name}, balance={self.get_balance():.2f}, status={self.account_status})"
    




 