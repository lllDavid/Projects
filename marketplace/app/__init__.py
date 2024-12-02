from flask import Flask
from .databases.user_manager import UserManager   
from .controllers.user.user_creator import UserCreator
from .controllers.coin.coin import CoinCreator
from .config import Config

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    user_manager = UserManager()
    app.user_manager = user_manager  

    app.register_blueprint(UserCreator, url_prefix='/user')
    app.register_blueprint(CoinCreator, url_prefix='/coin')

    return app
