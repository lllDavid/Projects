from dataclasses import dataclass
from datetime import datetime

from marketplace.app.user.user import User

@dataclass
class CryptoWallet:
    user_id: int
    wallet_id: int
    coin_amount = dict | None
    total_coin_value = float | None
    deposit_history: dict | None 
    withdrawal_history: dict | None 
    account_status: str | None 
    last_accessed: datetime 
    encryption_key: str | None 
    
    