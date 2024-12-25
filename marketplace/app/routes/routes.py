from flask import render_template, redirect, url_for, flash, session, request
from marketplace.app.db.user_db import update_username, get_user_by_username, get_user_by_id
from marketplace.app.user.user_security import UserSecurity

def register_routes(app):

    # Landing Routes
    @app.route("/")
    def index():
        return render_template("landing.html")

    @app.route("/terms")
    def terms():
        return render_template("terms.html")
    
    @app.route("/privacy")
    def privacy():
        return render_template("privacy.html")
    
    @app.route("/cookies")
    def cookies():
        return render_template("cookies.html")
    
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

    # Home Routes
    @app.route("/home")
    def home():
        current_username = session.get("username")
        return render_template("home.html")
    
    @app.route("/trade")
    def trade():
        return render_template("trade.html")

    @app.route("/wallet")
    def wallet():
        return render_template("wallet.html")

    @app.route("/settings", methods=["GET", "POST"])
    def settings():
        return handle_settings(request)

    # Additional Routes
    @app.route("/support")
    def support():
        return render_template("support.html")

    # Trade Routes
    @app.route("/submit_buy_order")
    def submit_buy_order():
        return render_template("trade.html")
    
    @app.route("/submit_sell_order")
    def submit_sell_order():
        return render_template("trade.html")
    

# Request Handlers
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
