from flask import Blueprint, render_template, redirect, url_for, session
from werkzeug.exceptions import BadRequest

from marketplace.app.db.crypto_wallet_db import get_crypto_wallet_by_user_id
from marketplace.app.controllers.auth_controller import check_authentication

wallet_values = Blueprint('wallet_values', __name__)

@wallet_values.route('/wallet', methods=['GET'])
def create_wallet_form():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    return render_template('wallet.html')

@wallet_values.route('/wallet', methods=['POST'])
def get_wallet_values():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))
    
    crypto_wallet = get_crypto_wallet_by_user_id(user_id)

    return render_template('wallet.html', crypto_wallet=crypto_wallet)

    
    