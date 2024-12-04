from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from marketplace.app.user import user_db
from marketplace.app.user.user import User
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_details import UserDetails
from marketplace.utils.roles import Role
from marketplace.utils.validation import validate_user_data

user_creator_blueprint = Blueprint('user_creator', __name__)

class UserCreator:
    def create_user(self, username: str, email: str, password: str, role: Role) -> User:
        return User(username=username, email=email, password=password, role=role)

    def create_user_security(self, password: str) -> UserSecurity:
        return UserSecurity(
            password_hash=UserSecurity.hash_password(password),
            two_factor_enabled=False,
            two_factor_secret_key=None,
            two_factor_backup_codes=None,
            two_factor_backup_codes_hash=None,
        )

    def create_user_status(self) -> UserStatus:
        return UserStatus(
            is_online=True,
            is_banned=False,
            ban_reason="",
            ban_duration=0,
        )

    def create_user_history(self) -> UserHistory:
        return UserHistory(
            login_count=0,
            last_successful_login=None,
            last_failed_login=None,
            failed_login_attempts=0,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

    def create_user_details(self, username: str, email: str, password: str) -> UserDetails:
        user = self.create_user(username, email, password, role=Role.USER)
        security = self.create_user_security(password)
        status = self.create_user_status()
        history = self.create_user_history()

        return UserDetails(
            user=user,
            security=security,
            status=status,
            history=history,
        )

    def create_and_save_user(self, username: str, email: str, password: str) -> UserDetails | None:
        try:
            validate_user_data(username, email, password)
            user_details = self.create_user_details(username, email, password)
            print(f"User {username} created successfully.")
            user_db.insert_user(user_details)
            return user_details
        except ValueError as e:
            print(f"Error: {e}")
            return None

@user_creator_blueprint.route('/signup', methods=['GET'])
def create_user_form():
    return render_template('signup.html')

from flask import request, flash, redirect, url_for
from werkzeug.exceptions import BadRequest

@user_creator_blueprint.route('/signup', methods=['POST'])
def create_user():
    try:
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Ensure all fields are provided
        if not all([username, email, password]):
            flash("All fields are required!", "error")
            return redirect(url_for('user_creator.create_user_form'))  

        # Create UserCreator instance and attempt to create user
        user_creator = UserCreator()
        user_details = user_creator.create_and_save_user(username, email, password)

        # Handle success
        if user_details:
            flash("User created successfully!", "success")
            return redirect(url_for('home'))  
        else:
            if not username or len(username) < 4:
                raise BadRequest("Username must be at least 4 characters long.")
            return redirect(url_for('user_creator.create_user_form'))  

    except ValueError as ve:
        # Handle validation errors (e.g., invalid username, email, or password format)
        flash(f"Validation Error: {str(ve)}", "error")
        return redirect(url_for('user_creator.create_user_form'))

    except BadRequest as br:
        # Handle bad requests, like missing form data or invalid content
        flash(f"Bad Request: {str(br)}", "error")
        return redirect(url_for('user_creator.create_user_form'))

    except Exception as e:
        # Catch all other unexpected errors
        flash(f"An unexpected error occurred: {str(e)}", "error")
        return redirect(url_for('user_creator.create_user_form'))
