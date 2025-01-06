from flask import Flask

from marketplace.app.views.user_creator import user_creator
from marketplace.app.views.crypto_purchase import crypto_purchase
from marketplace.app.views.crypto_liquidation import crypto_liquidation
from marketplace.app.views.wallet_values import wallet_values
from marketplace.app.routes.routes import register_routes

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = "secret_key"
    
    app.register_blueprint(user_creator)
    app.register_blueprint(wallet_values)
    app.register_blueprint(crypto_purchase)
    app.register_blueprint(crypto_liquidation)

    register_routes(app)

    return app
