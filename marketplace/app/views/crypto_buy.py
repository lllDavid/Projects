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
    print(user_id)
    if user_id is None:
        flash('You must be logged in to perform this action.', 'error')
        return redirect(url_for('login'))
    
    # Fetch the CryptoWallet instance for the current user (it may contain the fiat wallet)
    fiat_wallet = get_fiat_wallet_by_user_id(user_id)
    print(fiat_wallet)

    # Ensure fiat_wallet and fiat_wallet.balance are valid and contains a valid balance
    if fiat_wallet and isinstance(fiat_wallet.balance, dict):
        # Example: Accessing USD balance
        fiat_wallet_balance = fiat_wallet.balance.get("USD", Decimal("0.0"))
        print(fiat_wallet_balance)

        # Ensure balance is greater than 0
        if fiat_wallet_balance > 0:
            try:
                coin = request.form['coin-selection']
                amount = request.form['coin-amount']
                amount = Decimal(amount)

                # Fetch the crypto wallet for the user
                wallet = get_crypto_wallet_by_user_id(user_id)

                if wallet is None:
                    flash('No crypto wallet found for the user.', 'error')
                    return redirect(url_for('trade'))

                # Proceed with increasing the coin balance if the wallet is valid
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
    else:
        flash('No fiat wallet found or invalid balance data', 'error')
        return redirect(url_for('trade'))
