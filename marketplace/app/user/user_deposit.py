from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class UserDeposit:
    user_id: int               
    amount: float               
    deposit_date: datetime      
    status: str                 

    def update_status(self, new_status: str) -> None:
        valid_statuses = ["pending", "completed", "failed"]
        if new_status.lower() in valid_statuses:
            self.status = new_status
        else:
            print(f"Invalid status: {new_status}. Valid statuses are {valid_statuses}.")

    def update_amount(self, new_amount: float):
        self.amount = new_amount
        print(f"Amount updated to: {self.amount}")

    def desposit_successful(self) -> bool:
        return self.status.lower() == 'completed'

    def formatted_deposit_date(self, date_format: str = "%Y-%m-%d %H:%M:%S") -> str:
        return self.deposit_date.strftime(date_format)

    def is_recent_deposit(self) -> bool:
        now = datetime.now()
        return now - self.deposit_date < timedelta(days=1)

    def cancel_deposit(self) -> None:
        self.update_status("failed")
        self.amount = 0
        print("Deposit has been canceled. Amount is reset to 0.")

    def __str__(self) -> str:
        return (f"User ID: {self.user_id}, Amount: {self.amount}, Status: {self.status}, "
                f"Deposit Date: {self.formatted_deposit_date()}")
