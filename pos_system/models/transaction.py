import user_model
import payment

class Transaction:
    def __init__(self, transaction_id=None, user_id=None, amount=None, status=None, payment_method=None, created_at=None):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.status = status  
        self.payment_method = payment_method  
        self.created_at = created_at 

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