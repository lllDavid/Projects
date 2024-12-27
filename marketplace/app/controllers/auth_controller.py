from flask import render_template, redirect, url_for, flash, session

from marketplace.app.user.user_security import UserSecurity
from marketplace.app.db.user_db import update_username, get_user_by_username, get_user_by_id

def handle_login(request):
    username = request.form["username"]
    password = request.form["password"]

    user = get_user_by_username(username)
    if user and UserSecurity.validate_password_hash(
        password, user.user_security.password_hash
    ):
        flash("Login successful", "success")
        session["user_id"] = user.id
        session["username"] = user.username
        session.modified = True
        return redirect(url_for("home"))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for("login"))

def handle_logout():
    session.pop("user_id", None)
    session.pop("username", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("index"))

def handle_settings(request):
    if "user_id" not in session:
        flash("You need to log in first.", "error")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    user = get_user_by_id(user_id)

    if not user:
        flash("User not found.", "error")
        return redirect(url_for("login"))

    current_username = session.get("username")

    if request.method == "POST":
        new_username = request.form.get("username")

        if new_username != user.username:
            update_username(user_id, new_username)
            session["username"] = new_username

            flash("Account details updated successfully.", "success")
        else:
            flash("No changes detected.", "info")

        user = get_user_by_id(user_id)
        return redirect(url_for("settings"))

    return render_template("settings.html", username=current_username, user=user)
