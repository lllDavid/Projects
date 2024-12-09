from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.exceptions import BadRequest
from marketplace.app.user import user_db
from marketplace.app.user.user import User
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_details import UserDetails
from marketplace.utils.roles import Role
from marketplace.utils.validation import is_valid_email, is_valid_password, is_unique_user

user_creator = Blueprint('user_creator', __name__)

class UserCreator:
    def create_user(self, username: str, email: str, role: Role) -> User:
        return User(id=None, username=username, email=email, role=role)

    def create_user_security(self, password: str) -> UserSecurity:
        two_factor_backup_codes = UserSecurity.generate_backup_codes()
        return UserSecurity(
            password_hash=UserSecurity.hash_password(password),
            two_factor_enabled=False,
            two_factor_secret_key=None,
            two_factor_backup_codes=two_factor_backup_codes,
            two_factor_backup_codes_hash=UserSecurity.hash_backup_codes(two_factor_backup_codes)
        )

    def create_user_status(self) -> UserStatus:
        return UserStatus(
            is_online=True,
            is_banned=False,
            ban_reason=None,
            ban_duration=None,
        )

    def create_user_history(self) -> UserHistory:
        return UserHistory(
            login_count=0,
            failed_login_count=0,
            last_login=None,
            last_failed_login=None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

    def create_user_details(self, username: str, email: str, password: str) -> UserDetails:
        user = self.create_user(username, email, role=Role.USER)
        user_security = self.create_user_security(password)
        user_status = self.create_user_status()
        user_history = self.create_user_history()

        return UserDetails(
            user=user,
            user_security=user_security,
            user_status=user_status,
            user_history=user_history,
        )

    def create_and_save_user(self, username: str, email: str, password: str) -> UserDetails | None:
        try:
            user_details = self.create_user_details(username, email, password)
            user_db.insert_user(user_details)
            return user_details
        except ValueError as e:
            print(f"Error: {e}")
            return None


@user_creator.route('/signup', methods=['GET'])
def create_user_form():
    return render_template('signup.html')

@user_creator.route('/signup', methods=['POST'])
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
            flash("Password must be between 30 and 64 characters, contain an uppercase letter, a number, and a special character.", "error")
            return redirect(url_for('user_creator.create_user_form'))

        if not is_unique_user(username):
            flash("Username already taken.", "error")
            return redirect(url_for('user_creator.create_user_form'))

        user_creator = UserCreator()
        user_details = user_creator.create_and_save_user(username, email, password)

        if user_details:
            session["user_id"] = user_details.user.id
            return redirect(url_for('home'))  
        else:
            return redirect(url_for('user_creator.create_user_form'))  

    except BadRequest as br:
        flash(f"Bad Request: {str(br)}", "error")
        return redirect(url_for('user_creator.create_user_form'))

    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}", "error")
        return redirect(url_for('user_creator.create_user_form'))

