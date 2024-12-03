from flask import Flask, render_template, flash, redirect, url_for
from marketplace.app.user.user_creator import user_creator_bp  

def create_app() -> Flask:
    app = Flask(__name__, static_folder='app/static', template_folder='app/templates/')

    @app.route('/home')
    def home():
        return render_template('home.html')
    
    # Redirect root ("/") to "/home"
    @app.route('/')
    def index():
        return redirect(url_for('home'))

    app.register_blueprint(user_creator_bp)
    app.config['SECRET_KEY'] = 'secret_key' 

    return app

