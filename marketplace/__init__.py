from flask import Flask
from marketplace.app.user.user_creator import user_creator_bp  

def create_app() -> Flask:
    app = Flask(__name__, template_folder='app/templates/')

    app.register_blueprint(user_creator_bp)
    app.config['SECRET_KEY'] = 'secret_key' 

    return app

