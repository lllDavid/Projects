from threading import Thread
from datetime import datetime
from dataclasses import dataclass
from marketplace import create_app  
from marketplace.utils.version import Version  

@dataclass
class Main:
    app_name: str
    app_version: str
    is_running: bool = False
    start_time: datetime | None = None
    stop_time: datetime | None = None

    def _run_app(self):
        app = create_app()
        app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)

    def start_app(self) -> datetime:
        self.is_running = True
        self.start_time = datetime.now()
        Thread(target=self._run_app, daemon=True).start()
        print(f"{self.app_name} version {self.app_version} started at: {self.start_time}")
        return self.start_time

    def stop_app(self) -> datetime:
        self.is_running = False
        self.stop_time = datetime.now()
        print(f"{self.app_name} version {self.app_version} stopped at: {self.stop_time}")
        return self.stop_time

    def calculate_runtime(self) -> str:
        if self.start_time and self.stop_time:
            runtime = self.stop_time - self.start_time
            hours, remainder = divmod(runtime.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"Total runtime: {runtime.days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        return "App has not been started and stopped properly."

if __name__ == "__main__":
    version = Version()
    main = Main(app_name=version.get_name(), app_version=version.get_version())

    try:
        main.start_app()
        input()
    except KeyboardInterrupt:
        print()

    main.stop_app()
    print(main.calculate_runtime())
