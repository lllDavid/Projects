from dataclasses import dataclass
from datetime import datetime

from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet

@dataclass
class Purchase:
    user_id: int
    purchase_id: int
    crypto_wallet: CryptoWallet
    fiat_wallet: FiatWallet
    transaction_id: str
    fiat_amount: float
    coin_name: str
    coin_amount: float
    created_at: datetime
    completed_at: datetime
    status: str
    successful: bool

'''   def user_purchase_coin(self, coin:Coin, amount:float):
        if self.fiat_wallet:
            amount = self.fiat_amount
            self.fiat_wallet.add_deposit(date=datetime.now().strftime('%Y-%m-%d'), amount=amount)

        if self.crypto_wallet:
            self.crypto_wallet.add_deposit(date=datetime.now().strftime('%Y-%m-%d'), amount=amount)
            
'''