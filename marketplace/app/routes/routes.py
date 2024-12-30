from flask import render_template, request

from marketplace.app.controllers.auth_controller import handle_login, handle_logout, handle_settings, handle_deposit

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
        return render_template("home.html")
    
    @app.route("/trade", methods=["GET", "POST"])
    def trade():
        return render_template("trade.html") 

    @app.route("/wallet")
    def wallet():
        return render_template("wallet.html")
    
    @app.route("/deposit")
    def deposit():
        return handle_deposit(request)


    @app.route("/settings", methods=["GET", "POST"])
    def settings():
        return handle_settings(request)

    # Additional Routes
    @app.route("/support")
    def support():
        return render_template("support.html")

