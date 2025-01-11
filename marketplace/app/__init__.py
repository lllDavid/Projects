from flask import Flask

from config import Config
from app.blueprints.user_creator import user_creator
from app.blueprints.crypto_purchase import crypto_purchase
from app.blueprints.crypto_liquidation import crypto_liquidation
from app.blueprints.wallet_values import wallet_values
from app.routes.routes import register_routes

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = "secret_key"
    app.config.from_object(Config)

    app.register_blueprint(user_creator)
    app.register_blueprint(wallet_values)
    app.register_blueprint(crypto_purchase)
    app.register_blueprint(crypto_liquidation)
            
    register_routes(app)

    return app
