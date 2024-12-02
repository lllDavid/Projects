from flask import Flask
from .models import db
from .controllers.user_controller import user_bp
from .controllers.market_controller import market_bp
from .config import Config

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Load configuration from config.py (could include DB URI, etc.)
    app.config.from_object(Config)
    
    # Initialize the database
    db.init_app(app)
    
    # Register blueprints for the routes/controllers
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(market_bp, url_prefix='/market')
    
    # Return the created app
    return app
