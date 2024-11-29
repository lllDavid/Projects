from dataclasses import dataclass
from datetime import datetime
from app.models.user import User
from app.models.payment import Payment

@dataclass
class UserToUserTransaction:
    transaction_id: str
    sender_address: str
    receiver_address: str
    amount: float
    transaction_fee: float
    timestamp: datetime
    status: str
    successful: bool

@dataclass
class UserPurchaseTransaction:
    transaction_id: str
    user_id: str
    amount_paid: float
    cryptocurrency_amount: float
    payment_method: str
    created_at: datetime
    status: str
    successful: bool
