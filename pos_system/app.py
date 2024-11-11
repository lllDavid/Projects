from dataclasses import dataclass

@dataclass
class App:
    app_name:str = "POS_System"
    app_version:str = "1.0.0"

    def get_name(self) -> str:
        name = self.app_name
        return name
    
    def get_version(self) -> str:
        version = self.app_version
        return version
    
    def update_name(self) -> str:
        name = input("New version:")
        self.app_name = name
        return name
    
    def update_version(self) -> str:
        version = input("New version: ")
        self.app_version = version
        return version
    
app_instance = App()

