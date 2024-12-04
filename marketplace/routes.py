from flask import Blueprint, render_template, request, redirect, url_for, flash
from marketplace.utils.roles import Role  # Import the Role Enum or Class
from marketplace.app.user.user import User  # Assuming User is in models.py

# Define the user settings blueprint
user_settings = Blueprint('user_settings', __name__, template_folder='app/templates')

# Sample user object for testing (you'd typically fetch this from a database)
user = User(username="testuser", email="test@example.com", password="password123", role=Role.USER)

@user_settings.route('/settings', methods=['GET', 'POST'])
def settings():
    global user  # Use the global user object for this session (typically from the database)
    
    if request.method == 'POST':
        # Get data from the form
        new_username = request.form.get('username')
        new_email = request.form.get('email')
        new_password = request.form.get('password')
        new_role = request.form.get('role')

        # Update user information based on form submission
        if new_username:
            user.update_username(new_username)
        if new_email:
            user.update_email(new_email)
        if new_password:
            user.update_password(new_password)
        if new_role:
            user.update_role(Role[new_role.upper()])  # Assumes Role is an Enum

        flash("Settings updated successfully", 'success')
        return redirect(url_for('user_settings.settings'))

    return render_template('settings.html', user=user)
