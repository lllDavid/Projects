from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Payment:
    transaction_id: str 
    payment_service_id: str 
    amount: float 
    status: str 

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

class PaymentServices(Enum):
    PAYPAL = auto()
    APPLE_PAY = auto()
    GOOGLE_PAY = auto()
    AMAZON_PAY = auto()

def select_payment_service(payment_service_id):
    try:
        return PaymentServices(payment_service_id)
    except ValueError:
        print(f"No valid Payment Service ID")

