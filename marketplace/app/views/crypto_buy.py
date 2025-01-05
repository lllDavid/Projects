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

    print(f"User ID: {user_id}")  # Debug: Print user_id

    fiat_wallet = get_fiat_wallet_by_user_id(user_id)
    print(f"Fiat Wallet: {fiat_wallet}")  # Debug: Print fiat_wallet

    if fiat_wallet is not None:
        if fiat_wallet.balance is None or fiat_wallet.balance <= 0:
            flash('Insufficient funds in your fiat wallet', 'error')
            return redirect(url_for('trade'))

        try:
            # Debug: Print all form data
            print(f"Form Data: {request.form}")

            coin = request.form['coin-selection']
            print(f"Coin selected: {coin}")  # Debug: Print coin selected

            amount = request.form['coin-amount']
            print(f"Amount input: {amount}")  # Debug: Print amount input

            amount = Decimal(amount)
            print(f"Amount after Decimal conversion: {amount}")  # Debug: Print amount as Decimal

            wallet = get_crypto_wallet_by_user_id(user_id)
            print(f"Crypto Wallet: {wallet}")  # Debug: Print crypto wallet

            if wallet is None:
                flash('No crypto wallet found for the user.', 'error')
                return redirect(url_for('trade'))

            wallet.increase_coin_balance(coin, amount, datetime.now())
            wallet.add_deposit_to_history(datetime.now(), amount)
           

            flash(f'Successfully purchased {amount} {coin}', 'success')
            print(f"Updated Wallet: {wallet}")  # Debug: Print updated wallet
            return redirect(url_for('trade'))

        except BadRequest as e:
            flash(f'Invalid data: {e}', 'error')
            print(f"BadRequest error: {e}")  # Debug: Print BadRequest error
            return redirect(url_for('trade'))

        except Exception as e:
            flash('An error occurred during the purchase process. Please try again.', 'error')
            print(f"General error: {e}")  # Debug: Print general error
            return redirect(url_for('trade'))

    else:
        flash('No fiat wallet found or invalid balance data', 'error')
        print("Fiat wallet is None or invalid")  # Debug: Print if no fiat wallet found
        return redirect(url_for('trade'))
