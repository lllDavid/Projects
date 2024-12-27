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
    coin_balance: dict[str, Decimal] = field(default_factory=dict)
    total_coin_value: Decimal | None = None
    last_accessed: datetime | None = None
    encryption_key: str | None = None
    deposit_history: dict[str, Decimal] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, Decimal]] = field(default_factory=dict)

    def add_deposit_to_history(self, date: datetime, amount: Decimal) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.deposit_history[formatted_date] = self.deposit_history.get(formatted_date, Decimal("0.00")) + amount

    def add_withdrawal_to_history(self, date: datetime, amount: Decimal, method: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.withdrawal_history.setdefault(formatted_date, {})[method] = amount

    def calculate_total_balance(self) -> Decimal:
        total_deposits = sum(self.deposit_history.values())
        total_withdrawals = sum(sum(methods.values()) for methods in self.withdrawal_history.values())
        coin_balance = sum(self.coin_balance.values()) if self.coin_balance else Decimal("0.00")
        total_balance = self.total_coin_value if self.total_coin_value is not None else Decimal("0.00")
        return (total_deposits - total_withdrawals + coin_balance + total_balance).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def increase_coin_balance(self, coin: str, amount: Decimal, date: datetime) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to add must be positive.")
        self.coin_balance[coin] = self.coin_balance.get(coin, Decimal("0.00")) + amount
        self.add_deposit_to_history(date, amount)

    def decrease_coin_balance(self, coin: str, amount: Decimal, date: datetime, method: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to subtract must be positive.")
        if coin not in self.coin_balance or self.coin_balance[coin] < amount:
            raise ValueError("Insufficient coin balance or coin does not exist.")
        self.coin_balance[coin] -= amount
        self.add_withdrawal_to_history(date, amount, method)

    def update_last_accessed(self):
        self.last_accessed = datetime.now()

    def __str__(self) -> str:
        coin_summary = ", ".join(f"{coin}: {amount}" for coin, amount in self.coin_balance.items()) if self.coin_balance else "No coins"
        return f"CryptoWallet(wallet_id={self.wallet_id}, user_id={self.user_id}, coins={coin_summary}, balance={self.calculate_total_balance():.2f}, last_accessed={self.last_accessed}))"
