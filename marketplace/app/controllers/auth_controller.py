from flask import render_template, redirect, url_for, flash, session

from app.user.user_bank import UserBank
from app.user.user_security import UserSecurity
from app.db.crypto_wallet_db import delete_crypto_wallet
from app.db.fiat_wallet_db import delete_fiat_wallet
from helpers.validation import is_valid_password, is_unique_username, is_unique_email
from app.db.user_db import update_username, update_email, update_password, update_user_bank, get_complete_user, get_user_by_id, get_user_by_email, get_user_by_username, delete_user


def handle_login(request):
    oauth_token = session.get('oauth_token')
    
    if oauth_token:
        user_info = session.get('user_info')
        if user_info:
            email = user_info.get('email')
            user = get_user_by_email(email)
            '''
            if not user:
                # If the user doesn't exist, create a new user in the database
                user = User(
                    username=user_info.get('name'),
                    email=email,
                    oauth_provider='google',  # Store that this user logged in with Google OAuth
                )
                save_user(user)  # Save the new user to the database
                '''
            if user:
                session["user_id"] = user.id
                session["username"] = user.username
                session["email"] = user.email
                session.modified = True
            
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))  
    
    username = request.form.get("username")
    password = request.form.get("password")

    user = get_user_by_username(username)
    if user and UserSecurity.validate_password_hash(password, user.user_security.password_hash):
        session["user_id"] = user.id
        session["username"] = user.username
        session["email"] = user.email
        session.modified = True
        
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))


def handle_logout():
    session.pop("user_id", None)
    session.pop("username", None)
    session.pop("email", None)
    session.clear() 
    return redirect(url_for("index"))

def check_authentication():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return None

def get_authenticated_user(user_id):
    return get_user_by_id(user_id)

def update_current_username(user_id, new_username):
    if is_unique_username(new_username):
        update_username(user_id, new_username)
        session["username"] = new_username
    else:
        flash("The new username is not valid. Please try again.", "error")

def update_current_email(user_id, new_email):
    if is_unique_email(new_email):
        update_email(user_id, new_email)
        session["email"] = new_email
    else:
        flash("The new email is not valid. Please try again.", "error")

def update_current_password(user_id, new_password):
    if is_valid_password(new_password):
        update_password(user_id, new_password)
    else:
        flash("The new password is not valid. Please try again.", "error")

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

def handle_settings(request):
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    user_id = session["user_id"]
    user = get_authenticated_user(user_id)
    if not user:
        return redirect(url_for("login"))

    current_username = session.get("username")
    current_email = user.email

    if request.method == "POST":
        if 'delete-account' in request.form:
            return delete_user_account(user_id)

        new_username = request.form.get("username")
        new_email = request.form.get("email")
        new_password = request.form.get("new-password")

        new_account_holder = request.form.get("bank_account_holder")
        new_iban = request.form.get("iban")
        new_swift = request.form.get("swift")
        new_routing_number = request.form.get("routing_number")

        if new_username:
            update_current_username(user_id, new_username)

        if new_email:
            update_current_email(user_id, new_email)

        if new_password:
            update_current_password(user_id, new_password)

        if new_account_holder:
            update_user_bank(user_id, new_account_holder=new_account_holder)

        if new_iban:
            update_user_bank(user_id, new_iban=new_iban)

        if new_swift:
            update_user_bank(user_id, new_swift=new_swift)

        if new_routing_number:
            update_user_bank(user_id, new_routing_number=new_routing_number)

        user = get_user_by_id(user_id)
        flash('Your account settings have been updated successfully.', 'success')

        return redirect(url_for("settings"))

    return render_template("settings.html", username=current_username, email=current_email, user=user)

def handle_deposit():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    user_id = session["user_id"]
    user = get_authenticated_user(user_id)
    
    if not user:
        return redirect(url_for("login"))

    account_holder_data = get_complete_user(session["user_id"])

    if account_holder_data is not None and account_holder_data.user_bank:
        account_holder = account_holder_data.user_bank.account_holder
    else:
        account_holder = None

    return render_template("deposit.html", account_holder=account_holder)

def handle_settings_bankdata(request):
    user_id = session["user_id"]
    user = get_authenticated_user(user_id)

    if request.method == "POST":
        if user:
            account_holder =  request.form.get("username")