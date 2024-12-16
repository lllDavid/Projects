from marketplace.app.wallets.fiat.wallet import FiatWallet
from marketplace.app.user.user import User
from marketplace.app.user.user_db import get_user
from datetime import datetime

def generate_wallet() -> FiatWallet | None:
    # Create a sample user
    user = get_user(9)
    if user is not None:
        # Sample bank details
        wallet_id = 1234567
        wallet_balance = 100.98
        bank_name = "Bank of America"
        account_number = "987654321012"
        account_holder = "John Doe"
        routing_number = "123456789"
        iban = "US12345678901234567890"  # Example IBAN
        swift_bic = "BOFAUS3N"  # Example SWIFT/BIC

        # Sample deposit and withdrawal history
        deposit_history = {
            "2024-01-01": 1500.00,
            "2024-05-10": 3200.50,
            "2024-09-15": 450.75
        }
        
        withdrawal_history = {
            "2024-02-20": {"amount": 200.00 },
            "2024-06-30": {"amount": 150.00 }
        }

        # Sample additional fields
        account_status = "active"  # Could be 'active', 'inactive', etc.
        last_accessed = datetime(2024, 12, 15, 10, 30, 0)
        encryption_key = "3f7f84a2d4e0b64f2bc39a2fc8830d1d987e8d12a9d92562fb6ac2398e71c15b"

        # Create and return the wallet object
        wallet = FiatWallet(
            user=user,
            wallet_id=wallet_id,
            bank_name=bank_name,
            account_number=account_number,
            account_holder=account_holder,
            routing_number=routing_number,
            iban=iban,
            swift_bic=swift_bic,
            wallet_balance=wallet_balance,
            deposit_history=deposit_history,
            withdrawal_history=withdrawal_history,
            account_status=account_status,
            last_accessed=last_accessed,
            encryption_key=encryption_key
        )
        
        return wallet

# Example usage
generated_wallet = generate_wallet()
print(generated_wallet)