from dataclasses import dataclass
from datetime import datetime
from marketplace.app.user.user import User

@dataclass
class FiatWallet:
    user: User
    bank_name: str
    account_number:str
    account_holder: str
    routing_number:str
    iban: str | None
    swift_bic: str | None
    deposit_history: dict | None 
    withdrawal_history: dict | None 
    account_status: str | None 
    last_accessed: datetime 
    encryption_key: str | None 
    
    