from flask import render_template, redirect, url_for, flash, session

from marketplace.app.user.user_security import UserSecurity
from marketplace.helpers.validation import is_valid_password, is_unique_username, is_unique_email
from marketplace.app.db.user_db import update_username, update_email, update_password, get_complete_user, get_user_by_id, get_user_by_username

def handle_login(request):
    username = request.form["username"]
    password = request.form["password"]

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

from flask import flash, redirect, url_for, session, request
from marketplace.app.db.crypto_wallet_db import delete_crypto_wallet
from marketplace.app.db.fiat_wallet_db import delete_fiat_wallet
from marketplace.app.db.user_db import delete_user
from marketplace.app.controllers.auth_controller import check_authentication, get_authenticated_user, get_user_by_id


def handle_settings(request):
    # Check authentication
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    # Retrieve the authenticated user's ID and info
    user_id = session["user_id"]
    user = get_authenticated_user(user_id)
    if not user:
        return redirect(url_for("login"))

    current_username = session.get("username")
    current_email = user.email

    # Handling POST request
    if request.method == "POST":
        # Check if account deletion button was pressed
        if 'delete-account' in request.form:
            try:
                # Perform account deletion
                delete_crypto_wallet(user_id)
                delete_fiat_wallet(user_id)
                delete_user(user_id)

                # Flash success message
                flash('Your account has been successfully deleted.', 'success')

                # Redirect to login page after deletion
                return redirect(url_for("login"))
            except Exception as e:
                print("Error: ",e)

        # Handle changes for username, email, and password
        new_username = request.form.get("username")
        new_email = request.form.get("email")
        new_password = request.form.get("new-password")

        # Update username, email, or password if provided
        if new_username:
            update_current_username(user_id, new_username)

        if new_email:
            update_current_email(user_id, new_email)

        if new_password:
            update_current_password(user_id, new_password)

        # Refresh user data
        user = get_user_by_id(user_id)
        flash('Your account settings have been updated successfully.', 'success')

        return redirect(url_for("settings"))

    # Render the settings page
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
