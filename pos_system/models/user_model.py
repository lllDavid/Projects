class UserModel:
    def __init__(self, id: int = None, 
                 first_name: str = None, 
                 last_name: str = None, 
                 street_address: str = None, 
                 city: str = None, 
                 state: str = None, 
                 zip_code: int = None, 
                 country: str = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_address(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.zip_code}, {self.country}"

    def update_address(self, street_address: str, city: str, state: str, zip_code: int, country: str):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def save(self):
        if self.id:
            print(f"Updating user {self.id} in the database.")
        else:
            print("Saving new user to the database.")

    def delete(self):
        if self.id:
            print(f"Deleting user {self.id} from the database.")
        else:
            print("User does not exist in the database.")

    def get_user_info(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.get_address(),
            "full_name": self.get_full_name()
        }

    