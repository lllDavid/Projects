from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDeposit:
    user_id: int
    amount: float
    last_deposit: datetime
    last_payout: datetime
