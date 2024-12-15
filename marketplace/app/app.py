from random import randint, uniform
from flask import Flask, render_template, redirect, url_for, flash, session, request, jsonify

from marketplace.app.views import user_creator
from marketplace.app.user.user_db import update_username
from marketplace.app.user.user_db import get_user_by_username, get_user_by_id
from marketplace.app.user.user_security import UserSecurity

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = "secret_key"

    app.register_blueprint(user_creator)

    def rand(range, typ='float'):
        return uniform(*range) if typ == 'float' else randint(*range)

    coins = [
        ('BTC', 'Bitcoin', (30000, 60000), (500000000000, 1000000000000), (18000000, 21000000)),
        ('ETH', 'Ethereum', (1500, 3500), (200000000000, 500000000000), (100000000, 120000000)),
        ('USDT', 'Tether', (0.99, 1.01), (65000000000, 70000000000), (65000000000, 70000000000)),
        ('XRP', 'XRP', (0.2, 2), (10000000000, 40000000000), (45000000000, 50000000000)),
        ('SOL', 'Solana', (10, 300), (10000000000, 40000000000), (300000000, 350000000)),
        ('BNB', 'Binance Coin', (200, 500), (30000000000, 50000000000), (150000000, 170000000)),
        ('DOGE', 'Dogecoin', (0.05, 0.25), (5000000000, 20000000000), (12000000000, 14000000000)),
        ('USDC', 'USD Coin', (0.99, 1.01), (30000000000, 60000000000), (30000000000, 60000000000)),
        ('ADA', 'Cardano', (0.1, 3), (10000000000, 50000000000), (30000000000, 40000000000)),
        ('TRX', 'TRON', (0.02, 1), (5000000000, 20000000000), (71000000000, 75000000000))
    ]

    mock_data = {coin[0].lower(): {
        'symbol': coin[0], 'name': coin[1], 'price_usd': rand(coin[2]), 'market_cap_usd': rand(coin[3], 'int'),
        '24h_change_percentage': rand((-5, 5)), 'logo': f'https://cryptologos.cc/logos/{coin[1].lower()}-{coin[0].lower()}-logo.png?v=040',
        'rank': coins.index(coin) + 1, 'one_hour': rand((-1, 1)), 'twenty_four_hour': rand((-5, 5)), 
        'seven_day': rand((-10, 10)), 'volume_24h': rand((1000000000, 10000000000), 'int'),
        'circulating_supply': rand(coin[4], 'int')} for coin in coins}

    @app.route('/api/crypto-data', methods=['GET'])
    def get_all_cryptos():
        # Return all cryptocurrencies
        return jsonify(mock_data), 200

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
    @app.route("/home")
    def home():
        current_username = session.get("username")
        return render_template("home.html", username=current_username)

    @app.route("/settings", methods=["GET", "POST"])
    def settings():
        return handle_settings(request)

    # Home Routes
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
        session["user_id"] = user.user_profile.id
        session["username"] = user.user_profile.username
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
