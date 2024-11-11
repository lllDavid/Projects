from dataclasses import dataclass
from datetime import datetime

@dataclass
class Main:
    app_name:str

def starting_app(app_name:str) -> None:
    print(f"{app_name} started application at: {datetime.now()}")

starting_app(123)


