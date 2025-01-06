from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.exceptions import BadRequest

from marketplace.app.db.crypto_wallet_db import get_crypto_wallet_by_user_id

wallet_values = Blueprint('wallet_values', __name__)

@wallet_values.route('/wallet', methods=['GET'])
def create_wallet_form():
    return render_template('wallet.html')

@wallet_values.route('/wallet', methods=['POST'])
def get_wallet_values():
    user_id = session.get('user_id')
    if user_id is None:
        flash('You must be logged in to perform this action.', 'error')
        return redirect(url_for('login'))
    try:
        crypto_wallet = get_crypto_wallet_by_user_id(user_id)
        if crypto_wallet is not None:
            for key, value in crypto_wallet.coins:
                print(f"Key: {key} Value: {value}")
        
        
        return redirect(url_for('trade'))
    
    except Exception as e:
        flash('An error occurred during the sale process. Please try again.', 'error')
        return redirect(url_for('trade'))