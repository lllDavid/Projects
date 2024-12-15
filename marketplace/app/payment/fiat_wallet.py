from dataclasses import dataclass
from datetime import datetime
from marketplace.app.user.user import User

@dataclass
class FiatWallet:
    user: User
    bank_name: str
    account_number:int
    holder_name: str
    routing_number:str
    iban: str | None
    deposits: dict | None 
    withdrawals: dict | None 
    account_status: str | None 
    last_accessed: str | None 
    encryption_key: str | None 
    
    