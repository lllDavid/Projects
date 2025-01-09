from flask import render_template, redirect, url_for, request, session
from requests_oauthlib import OAuth2Session
from marketplace.app.controllers.auth_controller import handle_login, handle_logout, handle_settings, handle_deposit
import os
import random
import string

client_id = "mock_client_id"
client_secret = "mock_client_secret"
redirect_uri = 'http://localhost:5000/callback'
mock_user_data = {
    'id': '12345',
    'email': 'mockuser@example.com',
    'name': 'Mock User',
}

def generate_mock_oauth_token():
    return {
        'access_token': ''.join(random.choices(string.ascii_letters + string.digits, k=40)),
        'token_type': 'bearer',
        'expires_in': 3600,
    }

def register_routes(app):
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
    
    @app.route("/signup")
    def signup():
        return render_template("signup.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            return handle_login(request)
        return render_template("login.html")
    
    @app.route("/demo")
    def demo():
        mock_oauth_token = generate_mock_oauth_token()
        session['oauth_token'] = mock_oauth_token
        return redirect(url_for('.callback'))
    
    @app.route("/callback", methods=["GET"])
    def callback():
        token = session.get('oauth_token')
        if token:
            session['user_info'] = mock_user_data
            return redirect(url_for('home'))
        else:
            return "OAuth failed, no token found!", 400

    @app.route("/profile", methods=["GET"])
    def profile():
        user_info = session.get('user_info')
        if user_info:
            return jsonify(user_info)
        else:
            return "User not logged in!", 400

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for('.index'))

    @app.route("/home")
    def home():
        return render_template("home.html")
    
    @app.route("/trade", methods=["GET", "POST"])
    def trade():
        return render_template("trade.html") 

    @app.route("/wallet", methods=["GET", "POST"])
    def wallet():
        return render_template("wallet.html")
    
    @app.route("/deposit")
    def deposit():
        return handle_deposit()

    @app.route("/settings", methods=["GET", "POST"])
    def settings():
        return handle_settings(request)

    @app.route("/support")
    def support():
        return render_template("support.html")
    
    if __name__ == "__main__":
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
        app.secret_key = os.urandom(24)
        app.run(debug=True)
