from enum import Enum

class Payment_Services(Enum):
    PAYPAL = 1
    APPLE_PAY = 2
    GOOGLE_PAY = 3
    AMAZON_PAY = 4
    BITCOIN = 5
    ETHEREUM = 6

def select_payment_service(payment_service_id):
    try:
        return Payment_Services(payment_service_id)
    except ValueError:
        print(f"No valid Payment Service ID")

