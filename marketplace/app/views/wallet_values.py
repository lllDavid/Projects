from flask import Blueprint, render_template, redirect, url_for, session
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
        return redirect(url_for('login'))
    print(user_id)
    
    crypto_wallet = get_crypto_wallet_by_user_id(user_id)
    
    return render_template('wallet.html', crypto_wallet=crypto_wallet)

    
    