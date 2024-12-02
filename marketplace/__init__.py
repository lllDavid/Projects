from flask import Flask
from marketplace.app.user.user_db_controller import UserDBController   
from marketplace.app.user.user_creator import UserCreator
from marketplace.app.coin.coin_creator import CoinCreator
from marketplace.config import Config  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize any global resources
    user_db_controller = UserDBController()
    app.user_db_controller = user_db_controller  

    # Register blueprints
    app.register_blueprint(UserCreator, url_prefix='/user')
    app.register_blueprint(CoinCreator, url_prefix='/coin')

    return app
