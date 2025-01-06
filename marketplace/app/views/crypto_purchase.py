from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from marketplace.app.db.crypto_wallet_db import get_crypto_wallet_by_user_id, update_crypto_wallet
from marketplace.app.db.fiat_wallet_db import get_fiat_wallet_by_user_id
from marketplace.app.transaction.purchase import process_crypto_purchase

crypto_purchase = Blueprint('crypto_purchase', __name__)

@crypto_purchase.route('/trade', methods=['GET'])
def create_trade_form():
    return render_template('trade.html')

@crypto_purchase.route('/trade', methods=['POST'])
def purchase_crypto():
    user_id = session.get('user_id')
    if user_id is None:
        flash('You must be logged in to perform this action.', 'error')
        return redirect(url_for('login'))
    
    try:
        fiat_wallet = get_fiat_wallet_by_user_id(user_id)
        success, message = process_crypto_purchase(user_id, fiat_wallet, request.form)
        
        flash(message[0], message[1])
        return redirect(url_for('trade'))
    
    except Exception as e:
        flash('An error occurred during the purchase process. Please try again.', 'error')
        return redirect(url_for('trade'))
