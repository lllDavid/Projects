from datetime import datetime
from dataclasses import dataclass
from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet

@dataclass
class Trade:
    user_id: int
    transaction_id: str
    crypto_wallet: CryptoWallet
    fiat_wallet: FiatWallet
    sender_address: str
    receiver_address: str
    coin_name: str
    coin_amount: float
    transaction_fee: float
    created_at: datetime
    completed_at: datetime
    status: str
    successful: bool
