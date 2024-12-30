from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from marketplace.app.user.user_bank import UserBank
from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet

@dataclass
class DepositFiat:
    user_id: int
    user_bank: UserBank
    fiat_wallet: FiatWallet
    amount: Decimal

    def deposit(self):
        amount = Decimal(input(("Amount to deposit: ")))
        self.fiat_wallet.increase_wallet_balance(amount)
        print(f"Wallet of {self.fiat_wallet.user_id} has increased by: {amount} ")

# Assuming UserBank and FiatWallet classes are implemented and you can create instances of them
user_bank = UserBank(user_id=1, bank_name="Bank A", balance=1000)  # Example user bank instance
fiat_wallet = FiatWallet(user_id=1, balance=500)  # Example fiat wallet instance

# Create the DepositFiat object with the required fields
deposit_fiat = DepositFiat(user_id=1, user_bank=user_bank, fiat_wallet=fiat_wallet, amount=Decimal('0'))

# Perform deposit (you will be prompted for input)
deposit_fiat.deposit()
