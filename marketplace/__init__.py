from flask import Flask, render_template, request, redirect, url_for, session, flash
from marketplace.app.user.user import User  
from marketplace.app.user.user_db_controller import get_user_by_username, update_username_db
from marketplace.app.user.user_security import UserSecurity

def create_app() -> Flask:
    app = Flask(__name__, static_folder='app/static', template_folder='app/templates/')
    app.config['SECRET_KEY'] = 'secret_key'

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
            if user and UserSecurity.compare_password_hash(password, user.security.password_hash):
                session['user_id'] = user.  # Store user ID in session
                session['username'] = user.username  # Optionally, store username
                flash("Login successful", "success")
                return redirect(url_for('home'))
            else:
                flash("Invalid username or password", "error")
        
        return render_template('login.html')

    @app.route('/home')
    def home():
        if 'user_id' not in session:
            flash("You need to log in first.", "error")
            return redirect(url_for('login'))
        return render_template('home.html')

    @app.route('/settings', methods=['GET', 'POST'])
    def settings():
        if 'user_id' not in session:
            flash("You need to log in first.", "error")
            return redirect(url_for('login'))

        current_username = session.get('username')

        if request.method == 'POST':
            new_username = request.form.get('new_username')
            if new_username:
                update_username_db(session['user_id'], new_username)  # Update the username for the current user
                session['username'] = new_username  # Update the session with the new username
                flash("Username updated successfully.", "success")
            else:
                flash("Username cannot be empty.", "error")
        
        return render_template('settings.html', username=current_username)

    return app
