from flask import Flask, session
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

    # Register Google OAuth2 client
    google = oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        client_kwargs={'scope': 'openid profile email'},
    )

    # Mock Google OAuth token in session
    @app.before_request
    def mock_google_token():
        # Simulate that the user is authenticated with a mock Google token
        if 'google_token' not in session:
            # Example of a mock Google OAuth token (simulating a valid access token)
            session['google_token'] = {
                'access_token': 'mock-access-token',
                'token_type': 'bearer',
                'expires_in': 3600,
                'scope': 'openid profile email'
            }
            # Simulate mock user info (normally this would come from Google)
            session['user_info'] = {
                'id': '123456',
                'name': 'John Doe',
                'email': 'johndoe@example.com',
                'picture': 'https://example.com/profile_pic.jpg'
            }

    register_routes(app)

    return app
