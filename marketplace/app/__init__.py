from flask import Flask, session, request, redirect, url_for
from authlib.integrations.flask_client import OAuth

from marketplace.config import Config
from marketplace.app.views.oauth import oauth_blueprint
from marketplace.app.views.user_creator import user_creator
from marketplace.app.views.crypto_purchase import crypto_purchase
from marketplace.app.views.crypto_liquidation import crypto_liquidation
from marketplace.app.views.wallet_values import wallet_values
from marketplace.app.routes.routes import register_routes

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = "secret_key"
    app.config.from_object(Config)

    app.register_blueprint(user_creator)
    app.register_blueprint(wallet_values)
    app.register_blueprint(crypto_purchase)
    app.register_blueprint(crypto_liquidation)
    app.register_blueprint(oauth_blueprint)

    # Initialize OAuth
    oauth = OAuth(app)

    '''
    google = oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        client_kwargs={'scope': 'openid profile email'},
    )
    '''

    @app.before_request
    def ensure_authenticated_user():
        print(f"Request endpoint: {request.endpoint}")
        print(f"Session content: {session}")
        
        if 'google_token' not in session or 'user_info' not in session:
            if request.endpoint not in ['index', 'signup', 'login', 'privacy', 'cookies', 'terms', 'static']: 
                print("User not authenticated")
                return redirect(url_for('login'))

            
    register_routes(app)

    return app
