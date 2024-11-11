from dataclasses import dataclass

@dataclass
class App:
    app_name:str
    app_version:str

app_instance = App(app_name = "POS_System", app_version = "1.0.0")

def get_name() -> str:
    return app_instance.app_name

def get_version() -> str:
    return app_instance.app_version