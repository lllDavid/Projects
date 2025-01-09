from flask import Flask, redirect, url_for, session, render_template, flash, request
# Import the necessary functions for user management (from the second part of the provided code)
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.db.crypto_wallet_db import delete_crypto_wallet
from marketplace.app.db.fiat_wallet_db import delete_fiat_wallet
from marketplace.helpers.validation import is_valid_password, is_unique_username, is_unique_email
from marketplace.app.db.user_db import update_username, update_email, update_password, get_complete_user, get_user_by_id, get_user_by_username, delete_user
from authlib.integrations.flask_client import OAuth
import os

# Initialize Flask application
app = Flask(__name__)

# Secret key for sessions
app.secret_key = os.urandom(24)

# Initialize OAuth client
oauth = OAuth(app)

# Mocked Google OAuth provider
google = oauth.register(
    name='google',
    client_id='fake-client-id',  # Fake client ID for development
    client_secret='fake-client-secret',  # Fake client secret for development
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)

# Simulate user data for OAuth
mock_user_data = {
    'id': 'mock-user-id',
    'name': 'Mock User',
    'email': 'mockuser@example.com'
}

# Login route: Mock OAuth login process
@app.route('/login')
def login():
    # Normally, we would redirect to Google for OAuth, but we simulate the process here
    session['google_oauth_token'] = {'access_token': 'mock-access-token'}
    session['user_id'] = mock_user_data['id']
    session['username'] = mock_user_data['name']
    session['email'] = mock_user_data['email']
    return redirect(url_for('home'))

# Auth route: Simulate OAuth callback from Google
@app.route('/auth')
def auth():
    # In a real app, you'd get the access token and user data here
    # Mock the token and user info
    session['google_oauth_token'] = {'access_token': 'mock-access-token'}
    session['user_id'] = mock_user_data['id']
    session['username'] = mock_user_data['name']
    session['email'] = mock_user_data['email']

    return redirect(url_for('home'))

# Logout route: Clears the session and logs the user out
@app.route('/logout')
def logout():
    session.pop('google_oauth_token', None)
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('home'))

# Home route: Displays welcome message or login prompt
@app.route('/')
def home():
    if 'user_id' in session:
        return f'Hello, {session["username"]}! <a href="/settings">Go to Settings</a>'
    return 'You are not logged in. <a href="/login">Login with Google</a>'

# Authentication check for protected routes
def check_authentication():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return None

# Settings route for managing account settings
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    user_id = session["user_id"]
    # Here, we use the mock user data directly for the settings page
    user = mock_user_data  # In a real application, you would query your database here

    current_username = session.get("username")
    current_email = user.get("email", "")

    if request.method == "POST":
        # Handle settings updates (username, email, password, etc.)
        pass

    return render_template("settings.html", username=current_username, email=current_email, user=user)


# Handle User Account Deletion
def delete_user_account(user_id):
    try:
        delete_crypto_wallet(user_id)
        delete_fiat_wallet(user_id)
        delete_user(user_id)
        flash('Your account has been successfully deleted.', 'success')
        return redirect(url_for("login"))
    except Exception as e:
        print("Error: ", e)
        flash("An error occurred while deleting your account. Please try again.", "error")
        return redirect(url_for("settings"))

# Update Username
def update_current_username(user_id, new_username):
    if is_unique_username(new_username):
        update_username(user_id, new_username)
        session["username"] = new_username
    else:
        flash("The new username is not valid. Please try again.", "error")

# Update Email
def update_current_email(user_id, new_email):
    if is_unique_email(new_email):
        update_email(user_id, new_email)
        session["email"] = new_email
    else:
        flash("The new email is not valid. Please try again.", "error")

# Update Password
def update_current_password(user_id, new_password):
    if is_valid_password(new_password):
        update_password(user_id, new_password)
    else:
        flash("The new password is not valid. Please try again.", "error")

# Handle Deposit (for the user bank account management)
@app.route('/deposit')
def handle_deposit():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    user_id = session["user_id"]
    
    account_holder_data = get_complete_user(user_id)
    if account_holder_data is not None and account_holder_data.user_bank:
        account_holder = account_holder_data.user_bank.account_holder
    else:
        account_holder = None

    return render_template("deposit.html", account_holder=account_holder)

if __name__ == '__main__':
    app.run(debug=True)
