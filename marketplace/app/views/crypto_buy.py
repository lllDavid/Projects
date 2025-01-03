from decimal import Decimal
from datetime import datetime

from werkzeug.exceptions import BadRequest
from flask import Blueprint, render_template, redirect, url_for, flash, request

from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet


crypto_buy = Blueprint('crypto_buy', __name__)

@crypto_buy.route('/trade', methods=['GET'])
def create_trade_form():
    return render_template('trade.html')

@crypto_buy.route('/trade', methods=['POST'])
def buy_crypto():
    if FiatWallet.balance is not None and FiatWallet.balance > 0:
        try:
            coin = request.form['coin-selection']
            amount = request.form['coin-amount']
            amount = Decimal(amount)

            wallet = CryptoWallet(
                user_id=1,
                wallet_id=101,
                wallet_address='0xABC123DEF456',
                balance={'BTC': Decimal('0.5'), 'ETH': Decimal('10.0')},
                total_coin_value=Decimal('25000.00'),
                last_accessed=datetime(2024, 12, 26, 15, 45, 54, 455287),
                encryption_key='super_secret_key',
                deposit_history={'BTC': Decimal('0.5'), 'ETH': Decimal('10.0')},
                withdrawal_history={
                    'BTC': {'tx1': Decimal('0.1')},
                    'ETH': {'tx2': Decimal('2.0')}
                }
            )

            wallet.increase_coin_balance(coin, amount, datetime.now())
            wallet.add_deposit_to_history(datetime.now(), amount)

            flash(f'Successfully purchased {amount} {coin}', 'success')

            return redirect(url_for('trade'))

        except BadRequest as e:
            flash(f'Invalid data: {e}', 'error')
            return redirect(url_for('trade'))

        except Exception as e:
            print(f'Error during purchase: {e}')
            flash('An error occurred during the purchase process. Please try again.', 'error')
            return redirect(url_for('trade'))

    else:
        flash('Insufficient funds in your fiat wallet', 'error')
        return redirect(url_for('trade'))