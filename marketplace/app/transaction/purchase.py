from decimal import Decimal
from datetime import datetime
from marketplace.app.db.crypto_wallet_db import get_crypto_wallet_by_user_id, update_crypto_wallet

def process_crypto_purchase(user_id, fiat_wallet, form_data):
    if fiat_wallet is None or fiat_wallet.balance is None or fiat_wallet.balance <= 0:
        print(f"[DEBUG] Insufficient funds: Fiat wallet is either None or has insufficient balance.")
        return False, ('Insufficient funds in your fiat wallet', 'error')

    try:
        coin = form_data['coin-selection']
        amount = form_data['coin-amount']
        amount = Decimal(amount)

        print(f"[DEBUG] Coin selected: {coin}, Amount to purchase: {amount}")

        wallet = get_crypto_wallet_by_user_id(user_id)
        if wallet is None:
            print(f"[DEBUG] No crypto wallet found for user_id: {user_id}")
            return False, ('No crypto wallet found for the user.', 'error')

        print(f"[DEBUG] Adding {amount} {coin} to crypto wallet.")
        wallet.add_coins(coin, amount, datetime.now())
        wallet.add_deposit_to_history(datetime.now(), amount)
        wallet.calculate_total_coin_value()
        wallet.update_last_accessed()
        
        update_crypto_wallet(wallet)

        print(f"[DEBUG] Updated crypto wallet: {wallet}")
        
        return True, (f'Successfully purchased {amount} {coin}', 'success')
    
    except Exception as e:
        print(f"[DEBUG] Error occurred: {e}")
        return False, ('An error occurred during the purchase process. Please try again.', 'error')
