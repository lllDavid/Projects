from flask import Blueprint, render_template, redirect, url_for, session, request, jsonify

from app.db.crypto_wallet_db import get_crypto_wallet_by_user_id
from app.controllers.auth_controller import check_authentication

from os import getenv
from dotenv import load_dotenv

from flask import Blueprint, render_template, redirect, url_for, flash, request
from itsdangerous import URLSafeTimedSerializer

from app.user.user_security import UserSecurity
from app.db.user_db import update_password, get_user_by_email
from helpers.validation import is_valid_password

support_email = Blueprint('support_email', __name__)

SECRET_KEY = getenv('URL_STS_SECRET_KEY')
if SECRET_KEY:
    s = URLSafeTimedSerializer(SECRET_KEY)
else:
    print("Not secret key provided")

TOKEN_EXPIRATION_TIME = 3600  

@support_email.route('/support', methods=['GET'])
def create_support_form():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    return render_template('support.html')

@support_email.route('/support', methods=['GET', 'POST'])
def send_support_email():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))
    
    user_email = request.form['email']

    if request.method == 'POST':
        subject = request.form['subject']  # Get the subject entered by the user
        to_email = request.form['email']  # Get the recipient email address
        message = request.form['message']  # Get the message entered by the user

        # Optionally, you can generate a reset URL if needed
        reset_url = generate_reset_url(to_email)  # Your logic for the reset URL (if applicable)
        
        # Send the email with subject and message from the form
        send_reset_email(to_email, reset_url, subject, message)
        
        return 'Email sent successfully!'

    return render_template('reset_password.html')


    
