from app.controllers.user_creation import UserCreator
from dataclasses import dataclass
from datetime import datetime
from app.version import Version

@dataclass
class Main:
    app_name: str
    app_version: str
    is_running: bool = False
    status: str = "Offline"
    start_time: datetime = None
    stop_time: datetime = None

    def start_app(self) -> datetime:
        self.is_running = True
        self.status = "Online"
        self.start_time = datetime.now()
        print(f"{self.app_name} version {self.app_version} started at: {self.start_time}")
        print(f"Status: {self.status}, Is Running: {self.is_running}")
        return self.start_time

    def stop_app(self) -> datetime:
        self.is_running = False
        self.status = "Offline"
        self.stop_time = datetime.now()
        print(f"{self.app_name} version {self.app_version} stopped at: {self.stop_time}")
        print(f"Status: {self.status}, Is Running: {self.is_running}")
        return self.stop_time

    def total_runtime(self) -> str:
        if self.start_time and self.stop_time:
            runtime = self.stop_time - self.start_time
            hours, remainder = divmod(runtime.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"Total runtime: {runtime.days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        return "App has not been started and stopped properly."

def get_user_input():
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    return {
        "username": username,
        "email": email,
        "password": password
    }

if __name__ == "__main__":
    # Initialize the application
    version_instance = Version()  # Assuming Version has get_name() and get_version()
    main_instance = Main(app_name=version_instance.get_name(), app_version=version_instance.get_version())

    # Start the application
    main_instance.start_app()

    # User creation workflow
    user_creator = UserCreator()

    while True:
        user_data = get_user_input()

        user_details = user_creator.create_and_save_user(
            user_data['username'], 
            user_data['email'], 
            user_data['password']
        )

        if user_details:
            print("User created successfully!")
            break
        else:
            print("User creation failed due to validation errors. Please try again.")

    # Stop the application
    input("Press 'Enter' to stop the app...")
    main_instance.stop_app()
    print(main_instance.total_runtime())
