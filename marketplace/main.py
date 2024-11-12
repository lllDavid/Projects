from dataclasses import dataclass
from datetime import datetime
from sys import exit
import app

@dataclass
class Main:
    app_name: str
    app_version: str
    is_running: bool = False
    status: str = "Offline"

    def starting_app(self) -> None:
        self.is_running = True
        self.status = "Online"
        print(f"{self.app_name} version {self.app_version} started at: {datetime.now():%Y-%m-%d %H:%M:%S}")
        print(f"Status: {self.status}, Is Running: {self.is_running}")

    def stop_app(self) -> None:
        self.is_running = False
        self.status = "Offline"
        print(f"{self.app_name} version {self.app_version} stopped at: {datetime.now():%Y-%m-%d %H:%M:%S}")
        print(f"Status: {self.status}, Is Running: {self.is_running}")
        exit()

main_instance = Main(app_name=app.app_instance.get_name(), app_version=app.app_instance.get_version())

if __name__ == "__main__":
    main_instance.starting_app()

    print("Press 'Enter' to stop the app...")
    input()  
    main_instance.stop_app() 
