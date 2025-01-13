from os import urandom
from flask import Flask
from flask_mail import Mail

from config import Config
from app.blueprints.user_creator import user_creator
from app.blueprints.crypto_purchase import crypto_purchase
from app.blueprints.crypto_liquidation import crypto_liquidation
from app.blueprints.wallet_values import wallet_values
from app.blueprints.password_reset import reset_password
from app.routes.routes import register_routes

mail = Mail()

def create_app() -> Flask:
    marketplace = Flask(__name__, static_folder="static", template_folder="templates")
    marketplace.secret_key = urandom(24)
    marketplace.config.from_object(Config)

    marketplace.config['MAIL_SERVER'] = 'smtp.gmail.com'
    marketplace.config['MAIL_PORT'] = 587
    marketplace.config['MAIL_USE_TLS'] = True
    marketplace.config['MAIL_USERNAME'] = 'your_email@gmail.com'  
    marketplace.config['MAIL_PASSWORD'] = 'your_email_password' 

    marketplace.register_blueprint(user_creator)
    marketplace.register_blueprint(wallet_values)
    marketplace.register_blueprint(crypto_purchase)
    marketplace.register_blueprint(crypto_liquidation)
    marketplace.register_blueprint(reset_password) 
            
    register_routes(marketplace)

    return marketplace
