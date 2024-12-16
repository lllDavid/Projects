from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet
from marketplace.app.user.user import User
from marketplace.app.user.user_db import get_user
from datetime import datetime

def generate_wallet() -> FiatWallet | None:
    user = get_user(9)
    if user is not None:
        wallet_id = None
        wallet_balance = None
        bank_name = None
        account_number = None
        account_holder = None
        routing_number = None
        iban = None 
        swift_bic = None
        deposit_history = None
        withdrawal_history = None
        last_accessed = None
        encryption_key = None

        wallet = FiatWallet(
            user=user,
            wallet_id=wallet_id,
            bank_name=bank_name,
            account_number=account_number,
            account_holder=account_holder,
            routing_number=routing_number,
            iban=iban,
            swift_bic=swift_bic,
            wallet_balance=wallet_balance,
            deposit_history=deposit_history,
            withdrawal_history=withdrawal_history,
            last_accessed=last_accessed,
            encryption_key=encryption_key
        )
        
        return wallet

