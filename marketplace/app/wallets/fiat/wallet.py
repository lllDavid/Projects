from dataclasses import dataclass, field
from datetime import datetime



@dataclass
class FiatWallet:
    user_id: int
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
        return f"FiatWallet(wallet_id={self.wallet_id}, user_id={self.user_id}, bank={self.bank_name}, balance={self.get_balance():.2f}, status={self.account_status})"
    
# Create a new FiatWallet instance
wallet = FiatWallet(
    user_id=1,
    wallet_id=1001,
    bank_name="Bank of Python",
    account_number="1234567890",
    account_holder="John Doe",
    routing_number="987654321",
    iban=None,
    swift_bic=None,
)

# Print initial wallet details
print(wallet)

# Add a deposit
wallet.add_deposit("2024-12-16", 500.00)
wallet.add_deposit("2024-12-16", 200.00)  # Adding another deposit on the same day
wallet.add_deposit("2024-12-17", 300.00)

# Print updated wallet details with balance after deposits
print(wallet)

# Add a withdrawal
wallet.add_withdrawal("2024-12-16", 150.00, "ATM")
wallet.add_withdrawal("2024-12-17", 100.00, "Bank Transfer")

# Print updated wallet details with balance after withdrawal
print(wallet)

# Check if the account is active
print(f"Is the account active? {wallet.is_active()}")

# Update account status and print
wallet.update_account_status("Inactive")
print(f"Updated status: {wallet.account_status}")

# Print final wallet details
print(wallet)

# Check the balance
balance = wallet.get_balance()
print(f"Final Balance: ${balance:.2f}")

# Update last accessed timestamp
wallet.update_last_accessed()
print(f"Last accessed: {wallet.last_accessed}")