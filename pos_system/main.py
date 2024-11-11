from dataclasses import dataclass
from datetime import datetime

@dataclass
class Main:
    app_name:str
    app_version:str
    is_running:bool
    status:str


def starting_app(app_name:str) -> None:
    print(f"{app_name} started application at: {datetime.now()}")
    is_runnning = True

def get_products():
    ...


