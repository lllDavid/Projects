from flask import render_template, redirect, url_for, session
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.db.user_db import update_username, update_email, update_password, get_user_by_username, get_user_by_id

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
    user = get_user_by_id(user_id)
    if not user:
        return None
    return user

def update_current_username(request, user_id, user):
    new_username = request.form.get("username")

    if new_username != user.username:
        update_username(user_id, new_username)
        session["username"] = new_username

    return get_user_by_id(user_id)

def update_current_email(request, user_id, user):
    new_email = request.form.get("email")

    if new_email != user.email:
        update_email(user_id, new_email)
        session["email"] = new_email

    return get_user_by_id(user_id)

def update_current_password(request, user_id, user):
    new_password = request.form.get("new-password")

    if new_password != user.password:
        update_password(user_id, new_password)

    return get_user_by_id(user_id)

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
            update_username(user_id, new_username)
            session["username"] = new_username

        if new_email:
            update_email(user_id, new_email)

        if new_password:
            update_password(user_id, new_password)

        user = get_user_by_id(user_id)
        return redirect(url_for("settings"))

    return render_template("settings.html", username=current_username, email=current_email, user=user)
