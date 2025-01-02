from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet
from marketplace.app.db.fiat_wallet import insert_fiat_wallet
from marketplace.app.db.user_db import get_user_from_db
from decimal import Decimal

def create_fiat_wallet(user_id: int) -> FiatWallet | None:
    user = get_user_from_db(user_id)
    if user is not None:
        wallet_id = None
        balance = Decimal(5000.00)
        deposit_history = {}
        withdrawal_history = {}
        last_accessed = None
        encryption_key = None

        wallet = FiatWallet(
            user_id=user.id,
            wallet_id=wallet_id,
            balance=balance,
            deposit_history=deposit_history,
            withdrawal_history=withdrawal_history,
            last_accessed=last_accessed,
            encryption_key=encryption_key
        )
        insert_fiat_wallet(wallet)
        return wallet




