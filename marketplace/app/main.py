from dataclasses import dataclass
from datetime import datetime
from app.version import Version

@dataclass
class Main:
    app_name: str
    app_version: str
    start_time: datetime 
    stop_time: datetime 
    running: bool = False
    status: str = "Offline"

    def start_app(self) -> datetime:
        self.running = True
        self.status = "Online"
        self.start_time = datetime.now()
        print(f"{self.app_name} version {self.app_version} started at: {self.start_time}")
        print(f"Status: {self.status}, Is Running: {self.running}")
        return self.start_time

    def stop_app(self) -> datetime:
        self.running = False
        self.status = "Offline"
        self.stop_time = datetime.now()
        print(f"{self.app_name} version {self.app_version} stopped at: {self.stop_time}")
        print(f"Status: {self.status}, Is Running: {self.running}")
        return self.stop_time

    def total_runtime(self) -> str:
        if self.start_time and self.stop_time:
            runtime = self.stop_time - self.start_time
            hours, remainder = divmod(runtime.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"Total runtime: {runtime.days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        return "App has not been started and stopped properly."

if __name__ == "__main__":
    version_instance = Version()  
    main_instance = Main(app_name=version_instance.get_name(), app_version=version_instance.get_version())

    main_instance.start_app()
    
    input("Press 'Enter' to stop the app...")
    main_instance.stop_app()
    print(main_instance.total_runtime())


        
