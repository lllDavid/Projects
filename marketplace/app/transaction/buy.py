from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet

@dataclass
class Buy:
    user_id: int
    crypto_wallet: CryptoWallet
    fiat_wallet: FiatWallet
    transaction_id: str
    fiat_amount: float
    coin_name: str
    coin_amount: float
    created_at: datetime
    status: str
    successful: bool
    completed_at: Optional[datetime] = None

    def update_crypto_wallet(self, new_crypto_wallet: CryptoWallet):
        self.crypto_wallet = new_crypto_wallet

    def update_fiat_wallet(self, new_fiat_wallet: FiatWallet):
        self.fiat_wallet = new_fiat_wallet

    def update_transaction_id(self, new_transaction_id: str):
        if not new_transaction_id:
            raise ValueError("Transaction ID cannot be empty.")
        self.transaction_id = new_transaction_id

    def update_fiat_amount(self, new_fiat_amount: float):
        if new_fiat_amount <= 0:
            raise ValueError("Fiat amount must be greater than zero.")
        self.fiat_amount = new_fiat_amount

    def update_coin_name(self, new_coin_name: str):
        if not new_coin_name:
            raise ValueError("Coin name cannot be empty.")
        self.coin_name = new_coin_name

    def update_coin_amount(self, new_coin_amount: float):
        if new_coin_amount <= 0:
            raise ValueError("Coin amount must be greater than zero.")
        self.coin_amount = new_coin_amount

    def update_status(self, new_status: str):
        if new_status not in ['pending', 'completed', 'failed']:
            raise ValueError("Invalid status. Must be 'pending', 'completed', or 'failed'.")
        self.status = new_status

    def update_successful(self, new_successful: bool):
        self.successful = new_successful

    def update_completed_at(self, new_completed_at: datetime):
        if new_completed_at < self.created_at:
            raise ValueError("Completed timestamp cannot be earlier than the created timestamp.")
        self.completed_at = new_completed_at

    def __repr__(self):
        return f"Buy(user_id={self.user_id}, transaction_id={self.transaction_id}, " \
               f"coin_name={self.coin_name}, fiat_amount={self.fiat_amount}, " \
               f"successful={self.successful})"
