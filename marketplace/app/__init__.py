from flask import Flask
from marketplace.app.views.coin_creator import coin_creator
from marketplace.app.views.user_creator import user_creator
from marketplace.app.views.user_purchase import user_purchase
from marketplace.app.views.user_trade import user_trade
from marketplace.app.routes.routes import register_routes

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = "secret_key"
    
    app.register_blueprint(coin_creator)
    app.register_blueprint(user_creator)
    app.register_blueprint(user_purchase)
    app.register_blueprint(user_trade)

    register_routes(app)

    return app
