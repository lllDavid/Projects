from dataclasses import dataclass
from datetime import datetime
import app
import sys

@dataclass
class Main:
    app_name: str
    app_version: str
    is_running: bool = False
    status: str = "Offline"

    def starting_app(self) -> None:
        """Starts the application and updates the status."""
        self.is_running = True
        self.status = "Online"
        print(f"{self.app_name} version {self.app_version} started at: {datetime.now():%Y-%m-%d %H:%M:%S}")
        print(f"Status: {self.status}, Is Running: {self.is_running}")

    def stop_app(self) -> None:
        """Stops the application and updates the status."""
        self.is_running = False
        self.status = "Offline"
        print(f"{self.app_name} stopped at: {datetime.now():%Y-%m-%d %H:%M:%S}")
        print(f"Status: {self.status}, Is Running: {self.is_running}")
        sys.exit()

instance = Main(app_name=app.get_name(), app_version=app.get_version())

if __name__ == "__main__":
    instance.starting_app()

    print("Press 'Enter' to stop the app...")
    input()  
    instance.stop_app() 
