from decimal import Decimal
from datetime import datetime
from werkzeug.exceptions import BadRequest
from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.db.crypto_wallet_db import get_crypto_wallet_by_user_id

crypto_sell = Blueprint('crypto_sell', __name__)

@crypto_sell.route('/trade/sell', methods=['GET'])
def create_trade_form():
    return render_template('trade.html')

@crypto_sell.route('/trade/sell', methods=['POST'])
def sell_crypto():
    user_id = session.get('user_id')
    if user_id is None:
        flash('You must be logged in to perform this action.', 'error')
        return redirect(url_for('login'))

    wallet = get_crypto_wallet_by_user_id(user_id)
    print(wallet)
    
    if wallet is not None:
        try:
            coin = request.form['coin-selection']
            amount = request.form['coin-amount']
            amount = Decimal(amount)

            if wallet.balance.get(coin, Decimal('0')) < amount:
                flash('Insufficient balance in your crypto wallet', 'error')
                return redirect(url_for('trade'))

            wallet.decrease_coin_balance(coin, amount, datetime.now(), "")
            wallet.add_deposit_to_history(datetime.now(), amount)
            print(wallet)

            flash(f'Successfully sold {amount} {coin}', 'success')
            return redirect(url_for('trade'))

        except BadRequest as e:
            flash(f'Invalid data: {e}', 'error')
            return redirect(url_for('trade'))

        except Exception as e:
            flash('An error occurred during the sale process. Please try again.', 'error')
            return redirect(url_for('trade'))

    else:
        flash('No crypto wallet found for the user.', 'error')
        return redirect(url_for('trade'))
