from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from marketplace.app.user.user_bank import UserBank

@dataclass
class CryptoWallet:
    user_id: int | None
    user_bank: UserBank
    wallet_id: int | None
    wallet_address: str | None
    coin_amount: dict[str, Decimal] = field(default_factory=dict)
    total_coin_value: Decimal = Decimal("0.00")
    last_accessed: datetime | None = None
    encryption_key: str | None = None
    deposit_history: dict[str, Decimal] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, Decimal]] = field(default_factory=dict)

    def add_deposit(self, date: str, amount: Decimal) -> None:
        amount = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.deposit_history[date] = self.deposit_history.get(date, Decimal("0.00")) + amount

    def add_withdrawal(self, date: str, amount: Decimal, method: str) -> None:
        amount = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.withdrawal_history.setdefault(date, {})[method] = amount

    def get_balance(self) -> Decimal:
        total_deposits = sum(self.deposit_history.values())
        total_withdrawals = sum(
            sum(methods.values()) for methods in self.withdrawal_history.values()
        )
        coin_balance = sum(self.coin_amount.values()) if self.coin_amount else Decimal("0.00")
        total_balance = coin_balance + self.total_coin_value
        return (total_deposits - total_withdrawals + total_balance).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def update_last_accessed(self):
        self.last_accessed = datetime.now()

    def add_coin_amount(self, coin: str, amount: Decimal) -> None:
        amount = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to add must be positive.")
        self.coin_amount[coin] = self.coin_amount.get(coin, Decimal("0.00")) + amount

    def subtract_coin_amount(self, coin: str, amount: Decimal) -> None:
        amount = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to subtract must be positive.")
        if coin not in self.coin_amount or self.coin_amount[coin] < amount:
            raise ValueError("Insufficient coin balance or coin does not exist.")
        self.coin_amount[coin] -= amount

    def __str__(self) -> str:
        coin_summary = (
            ", ".join(f"{coin}: {amount}" for coin, amount in self.coin_amount.items())
            if self.coin_amount else "No coins"
        )
        return (
            f"CryptoWallet(wallet_id={self.wallet_id}, user_id={self.user_id}, "
            f"coins={coin_summary}, balance={self.get_balance():.2f})"
        )