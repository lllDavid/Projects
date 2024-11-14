from dataclasses import dataclass
from .user import User
from .payment import Payment

@dataclass
class Transaction:
    transaction_id: str
    user_id: str
    amount: float
    status: str
    payment_method: str
    created_at: str

    def create_transaction(self, user_id, amount, payment_method):
        pass

    def get_transaction(self, transaction_id):
        pass

    def update_transaction_status(self, transaction_id, new_status):
        pass

    def process_refund(self, transaction_id):
        pass

    def get_user_transactions(self, user_id):
        pass

    def get_transaction_status(self, transaction_id):
        pass

    def log_transaction(self):
        pass

    def delete_transaction(self, transaction_id):
        pass

    def generate_transaction_id(self):
        pass