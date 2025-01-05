from datetime import datetime
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP

@dataclass
class CryptoWallet:
    user_id: int | None
    wallet_id: int | None
    wallet_address: str | None
    coins: dict[str, Decimal] = field(default_factory=dict)
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

    def calculate_total_coins(self) -> Decimal:
        total_deposits = sum(self.deposit_history.values())
        total_withdrawals = sum(sum(methods.values()) for methods in self.withdrawal_history.values())
        coins = sum(self.coins.values()) if self.coins else Decimal("0.00")
        total_balance = self.total_coin_value if self.total_coin_value is not None else Decimal("0.00")
        return (total_deposits - total_withdrawals + coins + total_balance).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def increase_coins(self, coin: str, amount: Decimal, date: datetime) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to add must be positive.")
        self.coins[coin] = self.coins.get(coin, Decimal("0.00")) + amount
        self.add_deposit_to_history(date, amount)

    def decrease_coins(self, coin: str, amount: Decimal, date: datetime, method: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to subtract must be positive.")
        if coin not in self.coins or self.coins[coin] < amount:
            raise ValueError("Insufficient coin coins or coin does not exist.")
        self.coins[coin] -= amount
        self.add_withdrawal_to_history(date, amount, method)

    def update_last_accessed(self):
        self.last_accessed = datetime.now()
