from flask import Flask
from .databases.user_db_controller import UserDBController   
from .controllers.user.user_creator import UserCreator
from .controllers.coin.coin import CoinCreator
from .config import Config

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    user_db_controller = UserDBController()
    app.user_db_controller = user_db_controller  

    app.register_blueprint(UserCreator, url_prefix='/user')
    app.register_blueprint(CoinCreator, url_prefix='/coin')

    return app
