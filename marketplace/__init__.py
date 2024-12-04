from flask import Flask, render_template, request, redirect, url_for, session
from marketplace.app.user.user import User  
from marketplace.utils.roles import Role 
from marketplace.app.user.user_creator import user_creator_blueprint
from marketplace.app.user.user_db_controller import update_username_db

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

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/home')
    def home():
        return render_template('home.html', username=user.username)

    @app.route('/settings', methods=['GET', 'POST'])
    def settings():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm-password')

            if username and username != user.username:
                new_username =  user.update_username(username)
                update_username_db(1, new_username)


            if email and email != user.email:
                user.update_email(email)

            if password and password == confirm_password:
                user.update_password(password)

            return redirect(url_for('settings')) 

        return render_template('settings.html', user=user)

    app.register_blueprint(user_creator_blueprint)

    return app
