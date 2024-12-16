from dataclasses import dataclass
from datetime import datetime

from marketplace.app.user.user import User

@dataclass
class FiatWallet:
    user_id: int
    wallet_id: int
    bank_name: str
    account_number:str
    account_holder: str
    routing_number:str
    iban: str | None
    swift_bic: str | None
    deposit_history: dict[str, float] | None 
    withdrawal_history: dict[str, dict[str, str]] | None 
    account_status: str | None 
    last_accessed: datetime | None
    encryption_key: str | None 
    
    