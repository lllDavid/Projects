from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.exceptions import BadRequest
from marketplace.app.user import user_db
from marketplace.app.user.user import User
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_details import UserDetails
from marketplace.utils.roles import Role
from marketplace.utils.validation import is_valid_email, is_valid_password, is_unique_user

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
            user_details = self.create_user_details(username, email, password)
            user_db.insert_user(user_details)
            return user_details
        except ValueError as e:
            print(f"Error: {e}")
            return None

@user_creator_blueprint.route('/signup', methods=['GET'])
def create_user_form():
    return render_template('signup.html')

@user_creator_blueprint.route('/signup', methods=['POST'])
def create_user():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not all([username, email, password]):
            flash("All fields are required!", "error")
            return redirect(url_for('user_creator.create_user_form'))

        if not is_valid_email(email):
            flash("Invalid email format.", "error")
            return redirect(url_for('user_creator.create_user_form'))

        if not is_valid_password(password):
            flash("Password must be at least 30 characters long, contain an uppercase letter, a number, and a special character.", "error")
            return redirect(url_for('user_creator.create_user_form'))

        if not is_unique_user(username):
            flash("Username already taken.", "error")
            return redirect(url_for('user_creator.create_user_form'))

        user_creator = UserCreator()
        user_details = user_creator.create_and_save_user(username, email, password)

        if user_details:
            return redirect(url_for('home'))  
        else:
            return redirect(url_for('user_creator.create_user_form'))  

    except BadRequest as br:
        flash(f"Bad Request: {str(br)}", "error")
        return redirect(url_for('user_creator.create_user_form'))

    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}", "error")
        return redirect(url_for('user_creator.create_user_form'))

