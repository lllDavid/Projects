from dataclasses import dataclass
from datetime import datetime
from marketplace.app.user.user_deposit import UserDeposit


@dataclass
class Trade:
    user_id: int
    user_desposit: UserDeposit
    transaction_id: str
    sender_address: str
    receiver_address: str
    coin_name: str
    coin_amount: float
    transaction_fee: float
    created_at: datetime
    completed_at: datetime
    status: str
    successful: bool
