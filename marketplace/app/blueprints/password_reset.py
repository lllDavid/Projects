import os
from flask import Blueprint, render_template, request, redirect, url_for, flash

reset_password = Blueprint('reset_password', __name__)

tokens_db = {}

def send_reset_email(to_email, reset_url):
    from app import mail  # Import mail inside the function to avoid circular import
    from flask_mail import Message
    msg = Message('Password Reset Request',
                  sender='your_email@gmail.com',
                  recipients=[to_email])
    msg.body = f'Click the link to reset your password: {reset_url}'
    mail.send(msg)

@reset_password.route('/', methods=['GET', 'POST'])
def reset_user_password():
    if request.method == 'POST':
        email = request.form['email']
        token = os.urandom(24).hex()
        tokens_db[token] = {'email': email}
        reset_url = url_for('reset_password.reset_user_password_token', token=token, _external=True)
        send_reset_email(email, reset_url)
        flash('A password reset link has been sent to your email!', 'success')
        return redirect(url_for('reset_password.reset_user_password'))
    
    return render_template('reset-password.html')


@reset_password.route('/<token>', methods=['GET', 'POST'])
def reset_user_password_token(token):
    token_data = tokens_db.get(token)
    if not token_data:
        flash('The password reset link is invalid.', 'danger')
        return redirect(url_for('reset_password.reset_user_password'))

    if request.method == 'POST':
        new_password = request.form['password']
        flash('Your password has been updated!', 'success')
        return redirect(url_for('reset_password.login'))

    return render_template('reset_password_token.html', token=token)
