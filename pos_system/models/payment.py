import user_model
import Projects.pos_system.models.transaction as transaction

class PaymentModel:
    def __init__(self, transaction_id=None, payment_service_id=None, amount=None, status=None):
        self.transaction_id = transaction_id
        self.payment_service_id = payment_service_id
        self.amount = amount
        self.status = status 

    def new_transaction(self, amount, payment_service_id):
        pass

    def process_payment(self):
        pass

    def refund_payment(self):
        pass
     
    def get_transaction_status(self):
        pass

    def _call_payment_gateway(self):
        pass

    def _call_refund_gateway(self):
        pass

    def generate_transaction_id(self):
        pass
