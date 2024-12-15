from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.exceptions import BadRequest

from marketplace.app.user.user_creator import UserCreator
from marketplace.helpers.validation import validate_user_input

user_creator = Blueprint('user_creator', __name__)

@user_creator.route('/signup', methods=['GET'])
def create_user_form():
    return render_template('signup.html')

@user_creator.route('/signup', methods=['POST'])
def create_user():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not validate_user_input(username, email, password):
            return redirect(url_for('user_creator.create_user_form'))

        user_creator = UserCreator()
        user = user_creator.create_and_save_user(username, email, password)

        if user:
            session["user_id"] = user.user_profile.id
            session["username"] = username
            return redirect(url_for('home'))
        else:
            flash("Failed to create user.", "error")
            return redirect(url_for('user_creator.create_user_form'))

    except BadRequest as br:
        flash(f"Bad Request: {str(br)}", "error")
        return redirect(url_for('user_creator.create_user_form'))

    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for('user_creator.create_user_form'))
