from flask import Flask, render_template, redirect, url_for, flash, session, request
from marketplace.app.user.user_creator import user_creator
from marketplace.app.user.user_db import update_user
from marketplace.app.user.user_db_controller import get_user_by_username
from marketplace.app.user.user_security import UserSecurity

def create_app() -> Flask:
    app = Flask(__name__, static_folder='app/static', template_folder='app/templates/')
    app.config['SECRET_KEY'] = 'secret_key'
    app.register_blueprint(user_creator, url_prefix='/user_creator')

    @app.route('/')
    def index():
        return render_template('landing.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/services')
    def services():
        return render_template('services.html')

    @app.route('/legal')
    def legal():
        return render_template('legal.html')

    @app.route('/signup')
    def signup():
        return render_template('signup.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            user = get_user_by_username(username)
            if user and UserSecurity.validate_password_hash(password, user.security.password_hash):
                flash("Login successful", "success")
                session["user_id"] = user.user.
                return redirect(url_for('home'))
            else:
                flash("Invalid username or password", "error")
        
        return render_template('login.html')

    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/settings', methods=['GET', 'POST'])
    def settings():
        username = request.form['username']
        current_user = get_user_by_username(username)
        if 'user_id' not in session:
            flash("You need to log in first.", "error")
            return redirect(url_for('login'))

        current_username = session.get('username')

        if request.method == 'POST':

            new_username = request.form.get('new_username')
            if new_username:
                update_user(session['user_id'], new_username)  
                session['username'] = new_username  
                flash("Username updated successfully.", "success")
            else:
                flash("Username cannot be empty.", "error")
        return render_template('settings.html', username=username)

    return app
