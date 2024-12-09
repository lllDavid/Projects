from flask import Flask, render_template, redirect, url_for, flash, session, request
from marketplace.app.user.user_creator import user_creator
from marketplace.app.user.user_db import update_user
from marketplace.app.user.user_db_controller import get_user_by_username, get_user_by_id
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
            if user and UserSecurity.validate_password_hash(password, user.user_security.password_hash):
                flash("Login successful", "success")
                session["user_id"] = user.user.id
                return redirect(url_for('home'))
            else:
                flash("Invalid username or password", "error")
        
        return render_template('login.html')

    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/settings', methods=['GET', 'POST'])
    def settings():
        if 'user_id' not in session:
            flash("You need to log in first.", "error")
            return redirect(url_for('login'))

        user_id = session['user_id']
        user = get_user_by_id(user_id)
        current_username = session.get('username')
        
        if request.method == 'POST':
            new_username = request.form.get('username')
            new_email = request.form.get('email')
            new_password = request.form.get('password')
            confirm_password = request.form.get('confirm-password')
            
            if new_password and new_password != confirm_password:
                flash("Passwords do not match.", "error")
                return redirect(url_for('settings'))
            
            if new_username != user.username or new_email != user.email or new_password:
                update_user(user_id, new_username)
                
                if new_username != user.username:
                    session['username'] = new_username
                flash("Account details updated successfully.", "success")
            else:
                flash("No changes detected.", "info")
            
            return redirect(url_for('settings'))
        
        return render_template('settings.html', username=current_username, user=user)

    return app
