from dataclasses import dataclass
from datetime import datetime

from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet

@dataclass
class Sell:
    user_id: int
    crypto_wallet: CryptoWallet
    fiat_wallet: FiatWallet
    transaction_id: str
    reference_number: int
    fiat_amount: float
    coin_name: str
    coin_amount: float
    created_at: datetime
    status: str
    successful: bool
    completed_at: datetime
    

