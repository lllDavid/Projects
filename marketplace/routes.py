from flask import Flask, render_template, request, redirect, url_for, session
from marketplace.utils.roles import Role  # Assuming the Role class is available
from dataclasses import dataclass

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management, adjust as needed

# Simulate a user for demonstration purposes
@dataclass
class User:
    username: str
    email: str
    password: str
    role: Role
    
    def update_username(self, new_username: str):
        self.username = new_username
        print(f"Username updated to {new_username}")

    def update_email(self, new_email: str):
        self.email = new_email
        print(f"Email updated to {new_email}")

    def update_password(self, new_password: str):
        self.password = new_password
        print("Password updated.")

    def update_role(self, new_role: Role):
        self.role = new_role
        print(f"Role updated to {new_role}")

    def display_details(self):
        return (f"Username: {self.username}\n"
                f"Email: {self.email}\n"
                f"Role: {self.role}\n")

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Role: {self.role}"

# Simulating a user in a session
user = User(username="john_doe", email="john@example.com", password="securepassword123", role=Role.ADMIN)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global user  # Use the global user object for demo

    if request.method == 'POST':
        # Handle form data to update user details
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        # Update username if provided
        if username and username != user.username:
            user.update_username(username)

        # Update email if provided
        if email and email != user.email:
            user.update_email(email)

        # Update password if provided
        if password and password == confirm_password:
            user.update_password(password)
        
        # Redirect to settings page after update
        return redirect(url_for('settings'))

    # Render settings page with user data
    return render_template('settings.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)
