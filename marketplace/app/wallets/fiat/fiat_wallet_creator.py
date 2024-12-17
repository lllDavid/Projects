from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet
from marketplace.app.user.user import User
from marketplace.app.user.user_db import get_user

def generate_wallet() -> FiatWallet | None:
    user = get_user(7)
    if user is not None:
        wallet_id = None
        wallet_balance = None
        deposit_history = {}
        withdrawal_history = {}
        last_accessed = None
        encryption_key = None

        wallet = FiatWallet(
            user_id=user.user_profile.id,
            user_bank=user.user_bank,
            wallet_id=wallet_id,
            wallet_balance=wallet_balance,
            deposit_history=deposit_history,
            withdrawal_history=withdrawal_history,
            last_accessed=last_accessed,
            encryption_key=encryption_key
        )
        
        return wallet

print(generate_wallet())