from flask import Blueprint, render_template, redirect, url_for, flash, request
from decimal import Decimal
from datetime import datetime
from werkzeug.exceptions import BadRequest

from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.user.user_bank import UserBank

crypto_sell = Blueprint('crypto_sell', __name__)

@crypto_sell.route('/trade/sell', methods=['GET'])
def create_trade_form():
    return render_template('trade.html')

@crypto_sell.route('/trade/sell', methods=['POST'])
def sell_crypto():
    try:
        coin = request.form['coin-selection']
        amount = request.form['coin-amount']
        amount = Decimal(amount)
    
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
            coin_balance={'BTC': Decimal('0.5'), 'ETH': Decimal('10.0')},
            total_coin_value=Decimal('25000.00'),
            last_accessed=datetime(2024, 12, 26, 15, 45, 54, 455287),
            encryption_key='super_secret_key',
            deposit_history={'BTC': Decimal('0.5'), 'ETH': Decimal('10.0')},
            withdrawal_history={
                'BTC': {'tx1': Decimal('0.1')},
                'ETH': {'tx2': Decimal('2.0')}
            }
        )

        wallet.decrease_coin_balance(coin, amount, datetime.now(), "")
        wallet.add_deposit_to_history(datetime.now(), amount)

        flash(f'Successfully sold {amount} {coin}', 'success')

        return redirect(url_for('trade'))

    except BadRequest as e:
        flash(f'Invalid data: {e}', 'error')
        return redirect(url_for('trade'))

    except Exception as e:
        print(f'Error during purchase: {e}')
        flash('An error occurred during the purchase process. Please try again.', 'error')
        return redirect(url_for('trade'))
