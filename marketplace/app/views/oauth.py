# marketplace/app/views/oauth.py
from flask import Blueprint, session, jsonify

# Create a Blueprint for OAuth routes
oauth_blueprint = Blueprint('oauth', __name__)

# Define a route for fetching user information from the session
@oauth_blueprint.route('/user')
def user():
    # Fetch mock user data from session
    user_info = session.get('user_info', None)
    if user_info:
        return jsonify(user_info)
    else:
        return "User not authenticated", 401
