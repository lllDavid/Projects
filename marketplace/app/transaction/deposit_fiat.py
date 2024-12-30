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


