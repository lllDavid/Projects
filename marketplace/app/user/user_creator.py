from datetime import datetime
from werkzeug.exceptions import BadRequest
from flask import Blueprint, render_template, redirect, url_for, flash, request, session

from marketplace.helpers.roles import Role
from marketplace.app.user import user_db
from marketplace.app.user.user_profile import UserProfile
from marketplace.app.user.user_status import UserStatus
from marketplace.app.user.user_history import UserHistory
from marketplace.app.user.user_security import UserSecurity
from marketplace.app.user.user import User
from marketplace.helpers.validation import validate_user_input

user_creator = Blueprint("user_creator", __name__)


class UserCreator:
    def create_user_profile(self, username: str, email: str, role: Role) -> UserProfile:
        return UserProfile(id=None, username=username, email=email, role=role)

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

    def create_user_security(self, password: str) -> UserSecurity:
        # two_factor_backup_codes = UserSecurity.generate_backup_codes()
        return UserSecurity(
            password_hash=UserSecurity.hash_password(password),
            two_factor_enabled=False,
            two_factor_secret_key=None,
            two_factor_backup_codes=None,
            two_factor_backup_codes_hash=None,
            # two_factor_backup_codes=two_factor_backup_codes,
            # two_factor_backup_codes_hash=UserSecurity.hash_backup_codes(two_factor_backup_codes)
        )

    def create_user(self, username: str, email: str, password: str) -> User:
        user_profile = self.create_user_profile(username, email, role=Role.USER)
        user_security = self.create_user_security(password)
        user_status = self.create_user_status()
        user_history = self.create_user_history()

        return User(
            user_profile=user_profile,
            user_security=user_security,
            user_status=user_status,
            user_history=user_history,
        )

    def create_and_save_user(
        self, username: str, email: str, password: str
    ) -> User | None:
        try:
            user = self.create_user(username, email, password)
            user_db.insert_user(user)
            return user
        except ValueError as e:
            print(f"Error: {e}")
            return None


@user_creator.route("/signup", methods=["GET"])
def create_user_form():
    return render_template("signup.html")


@user_creator.route("/signup", methods=["POST"])
def create_user():
    try:
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if not validate_user_input(username, email, password):
            return redirect(url_for("user_creator.create_user_form"))

        user_creator = UserCreator()
        user = user_creator.create_and_save_user(username, email, password)

        if user:
            session["user_id"] = user.user_profile.id
            session["username"] = username
            return redirect(url_for("home"))
        else:
            flash("Failed to create user.", "error")
            return redirect(url_for("user_creator.create_user_form"))

    except BadRequest as br:
        flash(f"Bad Request: {str(br)}", "error")
        return redirect(url_for("user_creator.create_user_form"))

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for("user_creator.create_user_form"))
