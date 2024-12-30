from flask import render_template, redirect, url_for, flash, session
from marketplace.app.user.user_security import UserSecurity
from marketplace.helpers.validation import is_valid_password, is_unique_username, is_unique_email
from marketplace.app.db.user_db import update_username, update_email, update_password, get_user_by_id, get_user_by_username

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
        new_username = request.form.get("username")
        new_email = request.form.get("email")
        new_password = request.form.get("new-password")

        if new_username:
            update_current_username(user_id, new_username)

        if new_email:
            update_current_email(user_id, new_email)

        if new_password:
            update_current_password(user_id, new_password)

        user = get_user_by_id(user_id)
        return redirect(url_for("settings"))

    return render_template("settings.html", username=current_username, email=current_email, user=user)
