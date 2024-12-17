from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.exceptions import BadRequest
from marketplace.app.user.user_creator import UserCreator
from marketplace.helpers.validation import validate_user_input

user_creator = Blueprint('user_creator', __name__)

def validate_and_redirect(username, email, password):
    if not validate_user_input(username, email, password):
        flash("Invalid input, please check your data.", "error")
        return True
    return False

def create_and_save_user(username, email, password):
    user_creator = UserCreator()
    user = user_creator.create_user(username, email, password)
    user_creator.save_user(user)
    return user

def set_user_session(user):
    session["user_id"] = user.id
    session["username"] = user.username

def handle_error(error):
    flash(f"Error: {str(error)}", "error")
    return redirect(url_for('user_creator.create_user_form'))

@user_creator.route('/signup', methods=['GET'])
def create_user_form():
    return render_template('signup.html')

@user_creator.route('/signup', methods=['POST'])
def create_user():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if validate_and_redirect(username, email, password):
            return redirect(url_for('user_creator.create_user_form'))

        user = create_and_save_user(username, email, password)
    
        if user:
            set_user_session(user)
            return redirect(url_for('home'))
        else:
            flash("Failed to create user.", "error")
            return redirect(url_for('user_creator.create_user_form'))

    except BadRequest as br:
        return handle_error(br)
    
    except Exception as e:
        return handle_error(e)
