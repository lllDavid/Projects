from decimal import Decimal
from datetime import datetime
from werkzeug.exceptions import BadRequest
from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from marketplace.app.wallets.crypto.crypto_wallet import CryptoWallet
from marketplace.app.db.crypto_wallet_db import get_crypto_wallet_by_user_id
from marketplace.app.db.fiat_wallet_db import get_fiat_wallet_by_user_id
from marketplace.app.wallets.fiat.fiat_wallet import FiatWallet

crypto_buy = Blueprint('crypto_buy', __name__)

@crypto_buy.route('/trade', methods=['GET'])
def create_trade_form():
    return render_template('trade.html')

@crypto_buy.route('/trade', methods=['POST'])
def buy_crypto():
    user_id = session.get('user_id')
    if user_id is None:
        flash('You must be logged in to perform this action.', 'error')
        return redirect(url_for('login'))
    
    fiat_wallet = get_fiat_wallet_by_user_id(user_id)
    if fiat_wallet is not None:
        if fiat_wallet.balance is None or fiat_wallet.balance <= 0:
            flash('Insufficient funds in your fiat wallet', 'error')
            return redirect(url_for('trade'))

        try:
            coin = request.form['coin-selection']
            amount = Decimal(request.form['coin-amount'])
            total_cost = Decimal(request.form['total-cost'])

            wallet = get_crypto_wallet_by_user_id(user_id)
            if wallet is None:
                flash('No crypto wallet found for the user.', 'error')
                return redirect(url_for('trade'))

            wallet.increase_coin_balance(coin, amount, datetime.now())
            wallet.add_deposit_to_history(datetime.now(), amount)
            fiat_wallet.decrease_wallet_balance(total_cost)

            flash(f'Successfully purchased {amount} {coin}', 'success')
            return redirect(url_for('trade'))

        except BadRequest as e:
            flash(f'Invalid data: {e}', 'error')
            return redirect(url_for('trade'))

        except Exception as e:
            flash('An error occurred during the purchase process. Please try again.', 'error')
            return redirect(url_for('trade'))

    else:
        flash('No fiat wallet found or invalid balance data', 'error')
        return redirect(url_for('trade'))
