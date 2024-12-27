# marketplace/app/views/user_purchase.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from decimal import Decimal
from datetime import datetime
from werkzeug.exceptions import BadRequest

from marketplace.app.coin.coin import Coin
from marketplace.app.transaction.purchase import Purchase
from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.user.user_bank import UserBank

user_purchase = Blueprint('user_purchase', __name__)

# Handle GET request to display the form (buy form on the /trade/buy page)
@user_purchase.route('/trade/buy', methods=['GET'])
def create_trade_form():
    return render_template('trade.html')

# Handle POST request when the form is submitted (for purchasing coins)
@user_purchase.route('/trade/buy', methods=['POST'])
def purchase_coin():
    try:
        # Extract form data
        coin = request.form['coin-selection']
        amount = request.form['coin-amount']
        amount = Decimal(amount)  # Ensure the amount is a Decimal for accurate calculations

        # Create or get a user's wallet (here, we mock a wallet object for demo purposes)
        wallet = CryptoWallet(
            user_id=1,
            user_bank=UserBank(
                bank_name='Example Bank',
                account_holder='John Doe',
                account_number='123456789',
                routing_number='987654321',
                iban='GB29NWBK60161331926819',
                swift_bic='NWBKGB2L',
                date_linked=datetime(2024, 12, 26, 15, 47, 16, 981356)
            ),
            wallet_id=101,
            wallet_address='0xABC123DEF456',
            coin_amount={'BTC': Decimal('0.5'), 'ETH': Decimal('10.0')},
            total_coin_value=Decimal('25000.00'),
            last_accessed=datetime(2024, 12, 26, 15, 45, 54, 455287),
            encryption_key='super_secret_key',
            deposit_history={'BTC': Decimal('0.5'), 'ETH': Decimal('10.0')},
            withdrawal_history={
                'BTC': {'tx1': Decimal('0.1')},
                'ETH': {'tx2': Decimal('2.0')}
            }
        )

        # Perform the purchase (add coins to the wallet)
        wallet.add_coin_amount(coin, amount)

        print(wallet)

        # Flash a success message
        flash(f'Successfully purchased {amount} {coin}', 'success')

        # Redirect back to the trade page after the purchase
        return redirect(url_for('trade'))

    except BadRequest as e:
        flash(f'Invalid data: {e}', 'error')
        return redirect(url_for('trade'))

    except Exception as e:
        # Log the exception for debugging purposes
        print(f'Error during purchase: {e}')
        flash('An error occurred during the purchase process. Please try again.', 'error')
        return redirect(url_for('trade'))
