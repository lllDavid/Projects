from dataclasses import dataclass
from enum import Enum

@dataclass
class Payment:
    transaction_id: str 
    payment_service_id: str 
    amount: float 
    status: str 

    def new_transaction(self):
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

class PaymentServices(Enum):
    PAYPAL = 1
    APPLE_PAY = 2
    GOOGLE_PAY = 3
    AMAZON_PAY = 4

def select_payment_service(payment_service_id):
    try:
        return PaymentServices(payment_service_id)
    except ValueError:
        print(f"No valid Payment Service ID")

