from flask import Flask, render_template, redirect, url_for
from marketplace.app.user.user_creator import user_creator_blueprint

def create_app() -> Flask:
    app = Flask(__name__, static_folder='app/static', template_folder='app/templates/')

    @app.route('/')
    def index():
        return render_template('landing.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/services')
    def services():
        return render_template('services.html')
    
    @app.route('/legal')
    def legal():
        return render_template('legal.html')
    
    @app.route('/signup')
    def signup():
        return render_template('signup.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/home')
    def home():
        return render_template('home.html')

    app.register_blueprint(user_creator_blueprint)
    app.config['SECRET_KEY'] = 'secret_key' 

    return app

