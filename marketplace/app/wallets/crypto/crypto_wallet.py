from dataclasses import dataclass, field
from datetime import datetime
from marketplace.app.user.user_bank import UserBank

@dataclass
class CryptoWallet:
    user_id: int | None
    user_bank: UserBank
    wallet_id: int | None
    wallet_address: str | None
    coin_amount: dict[str, float] = field(default_factory=dict)
    total_coin_value: float | None = None
    last_accessed: datetime | None  = None
    encryption_key: str | None = None
    deposit_history: dict[str, float] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, str]] = field(default_factory=dict)

    def add_deposit(self, date: str, amount: float) -> None:
        self.deposit_history[date] = self.deposit_history.get(date, 0) + amount

    def add_withdrawal(self, date: str, amount: float, method: str) -> None:
        self.withdrawal_history.setdefault(date, {})[method] = f"${amount:.2f}"

    def get_balance(self) -> float:
        total_deposits = sum(self.deposit_history.values())
        total_withdrawals = sum(
            float(amount.split('$')[1]) for methods in self.withdrawal_history.values() for amount in methods.values()
        )
        coin_balance = sum(self.coin_amount.values()) if self.coin_amount else 0
        total_balance = coin_balance + (self.total_coin_value or 0)
        return total_deposits - total_withdrawals + total_balance
    
    def update_last_accessed(self):sync
        self.last_accessed = datetime.now()

    def __str__(self) -> str:
        coin_summary = ", ".join(f"{coin}: {amount}" for coin, amount in self.coin_amount.items()) if self.coin_amount else "No coins"
        return f"CryptoWallet(wallet_id={self.wallet_id}, user_id={self.user_id}, coins={coin_summary}, balance={self.get_balance():.2f})"