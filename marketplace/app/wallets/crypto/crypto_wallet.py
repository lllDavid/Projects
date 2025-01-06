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
    # bug: always doubles decimal values
    def add_deposit_to_history(self, date: datetime, amount: Decimal) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        print(f"Before update: {self.deposit_history}")
        self.deposit_history[formatted_date] = self.deposit_history.get(formatted_date, Decimal("0.00")) + amount
        print(f"After update: {self.deposit_history}")

    def add_withdrawal_to_history(self, date: datetime, amount: Decimal, method: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.withdrawal_history.setdefault(formatted_date, {})[method] = amount

    def calculate_total_coin_value(self) -> Decimal:
        # Make sure deposit_history values are Decimal, just in case there are any non-Decimal values
        total_deposits = sum(Decimal(value) for value in self.deposit_history.values())

        # Similarly, handle withdrawal history ensuring proper Decimal values
        total_withdrawals = sum(sum(Decimal(amount) for amount in methods.values()) for methods in self.withdrawal_history.values())

        # Ensure that coins values are Decimal, and also handle any invalid types that may cause issues
        total_coin_value = sum(Decimal(coin_value) for coin_value in self.coins.values())

        # Round the total_coin_value properly
        total_coin_value = total_coin_value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        # Ensure total_balance is properly initialized as a Decimal
        total_balance = self.total_coin_value if self.total_coin_value is not None else Decimal("0.00")

        # Calculate total_value, ensure it's a Decimal, and round
        total_value = (total_deposits - total_withdrawals + total_balance).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return total_value

    def add_coins(self, coin: str, amount: Decimal, date: datetime) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to add must be positive.")
        self.coins[coin] = self.coins.get(coin, Decimal("0.00")) + amount
        self.add_deposit_to_history(date, amount)

    def remove_coins(self, coin: str, amount: Decimal, date: datetime, method: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to subtract must be positive.")
        if coin not in self.coins or self.coins[coin] < amount:
            raise ValueError("Insufficient coins or coin does not exist.")
        self.coins[coin] -= amount
        self.add_withdrawal_to_history(date, amount, method)

    def update_last_accessed(self):
        self.last_accessed = datetime.now()

