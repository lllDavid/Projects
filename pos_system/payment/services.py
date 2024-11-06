from enum import Enum, auto

class Payment_Services(Enum):
    PAYPAL = auto()
    APPLE_PAY = auto()
    GOOGLE_PAY = auto()
    AMAZON_PAY = auto()
    BITCOIN = auto()
    ETHEREUM = auto()

def select_payment_service(payment_service_id):
    try:
        return Payment_Services(payment_service_id)
    except ValueError:
        print(f"No valid Payment Service ID")

# Example usage:
payment_service = select_payment_service(2)
print(payment_service)  # Output: Payment_Services.APPLE_PAY
