from dataclasses import dataclass
from datetime import datetime
from marketplace.app.user.user_deposit import UserDeposit


@dataclass
class Purchase:
    user_id: str
    user_desposit: UserDeposit
    transaction_id: str
    fiat_amount: float
    coin_name: str
    coin_amount: float
    created_at: datetime
    completed_at: datetime
    status: str
    successful: bool
