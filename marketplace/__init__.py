from flask import Flask, render_template, request, redirect, url_for, session, flash
from marketplace.app.user.user import User  
from marketplace.utils.roles import Role 
from marketplace.app.user.user_creator import user_creator_blueprint
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
            if user and UserSecurity.compare_password_hash(password, user.security.password_hash ):
                session['signed_in'] = True  # Set signed_in flag to True
               # session['user_id'] = user.user.id  # Store the user_id in session
                flash("Login successful", "success")
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

        # Get the user ID from session
        user_id = session['user_id']

        # Fetch user from the database by user ID
        created_user = get_user_by_id(user_id)

        if created_user:
            # Access the username through the User object
            current_username = created_user.user.username

            if request.method == 'POST':
                # Handle username update logic here (if any form is submitted)
                new_username = request.form.get('new_username')
                if new_username:
                    # Call a function to update the username in the database
                    update_username_db(user_id, new_username)
                    flash("Username updated successfully.", "success")
                    # Update the session username as well (optional)
                    session['username'] = new_username  # If you store username in session
                else:
                    flash("Username cannot be empty.", "error")
            
            return render_template('settings.html', username=current_username)
        else:
            flash("User not found.", "error")
            return redirect(url_for('home'))

    
    app.register_blueprint(user_creator_blueprint)

    return app
