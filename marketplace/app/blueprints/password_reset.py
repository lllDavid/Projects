import os
import time
from flask import Blueprint, render_template, request, redirect, url_for, flash
from itsdangerous import URLSafeTimedSerializer

reset_password = Blueprint('reset_password', __name__)

# Secret key for generating and validating tokens (should be kept secure)
SECRET_KEY = "12345678"  # Use a secure key here for production
s = URLSafeTimedSerializer(SECRET_KEY)

# Token expiration time (in seconds)
TOKEN_EXPIRATION_TIME = 3600  # 1 hour expiration time

def send_reset_email(to_email, reset_url):
    from app import mail
    from flask_mail import Message
    msg = Message('Password Reset Request',
                  sender='your_email@gmail.com',
                  recipients=[to_email])
    msg.body = f'Click the link to reset your password: {reset_url}'
    mail.send(msg)

@reset_password.route('/reset-password', methods=['GET', 'POST'])
def reset_user_password():
    if request.method == 'POST':
        email = request.form['email']
        # Generate a token with the email address and timestamp
        token = s.dumps(email, salt="reset-password")
        reset_url = url_for('reset_password.reset_user_password_token', token=token, _external=True)
        send_reset_email(email, reset_url)
        flash('A password reset link has been sent to your email!', 'success')
        return redirect(url_for('reset_password.reset_user_password'))
    
    return render_template('reset-password.html')

@reset_password.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_user_password_token(token):
    try:
        # Try to load the email from the token, validate it within the expiration time
        email = s.loads(token, salt="reset-password", max_age=TOKEN_EXPIRATION_TIME)
    except Exception as e:
        flash('The password reset link is invalid or has expired.', 'danger')
        return redirect(url_for('reset_password.reset_user_password'))

    if request.method == 'POST':
        new_password = request.form['password']
        from app.db.user_db import update_password, get_user_by_email
        from app.user.user_security import UserSecurity
        # Here, you would update the user's password in the database
        user = get_user_by_email(email)
        hashed_password = UserSecurity.hash_password(new_password)
        if user and user.id:
            update_password(user.id, hashed_password)
        flash('Your password has been updated!', 'success')
        return redirect(url_for('reset_password.login'))

    return render_template('reset-password-token.html', token=token)
