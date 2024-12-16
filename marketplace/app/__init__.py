from flask import Flask
from marketplace.app.views.user_creator import user_creator
from marketplace.app.routes.routes import register_routes

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SECRET_KEY"] = "secret_key"

    app.register_blueprint(user_creator)

    register_routes(app)

    return app
