from flask import Flask, render_template, redirect, url_for, flash, session, request
from marketplace.app.user.user_creator import user_creator
from marketplace.app.user.user_db import update_user
from marketplace.app.user.user_db_controller import get_user_by_username, get_user_by_id
from marketplace.app.user.user_security import UserSecurity

def create_app() -> Flask:
    app = Flask(__name__, static_folder="app/static", template_folder="app/templates/")
    app.config["SECRET_KEY"] = "secret_key"

    app.register_blueprint(user_creator)

    # Register Routes
    @app.route("/")
    def index():
        return render_template("landing.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/services")
    def services():
        return render_template("services.html")

    @app.route("/legal")
    def legal():
        return render_template("legal.html")

    # Authentication Routes
    @app.route("/signup")
    def signup():
        return render_template("signup.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            return handle_login(request)

        return render_template("login.html")

    @app.route("/logout")
    def logout():
        return handle_logout()

    # User Account Routes
    @app.route("/dashboard")
    def dashboard():
        current_username = session.get("username")
        return render_template("dashboard.html", username=current_username)


    @app.route("/settings", methods=["GET", "POST"])
    def settings():
        return handle_settings(request)

    # Dashboard Routes
    @app.route("/trade")
    def trade():
        return render_template("trade.html")

    @app.route("/portfolio")
    def portfolio():
        return render_template("portfolio.html")

    @app.route("/support")
    def support():
        return render_template("support.html")

    return app


def handle_login(request):
    username = request.form["username"]
    password = request.form["password"]

    user = get_user_by_username(username)
    if user and UserSecurity.validate_password_hash(
        password, user.user_security.password_hash
    ):
        flash("Login successful", "success")
        session["user_id"] = user.user.id
        session["username"] = user.user.username
        session.modified = True
        return redirect(url_for("dashboard"))
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

    # Ensure user exists
    if not user:
        flash("User not found.", "error")
        return redirect(url_for("login"))

    current_username = session.get("username")

    if request.method == "POST":
        new_username = request.form.get("username")
    
        if new_username != user.username:
            update_user(user_id, new_username)
            session["username"] = new_username

            flash("Account details updated successfully.", "success")
        else:
            flash("No changes detected.", "info")

        user = get_user_by_id(user_id) 
        return redirect(url_for("settings"))

    return render_template("settings.html", username=current_username, user=user)


