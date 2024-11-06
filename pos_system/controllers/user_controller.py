from pos_system.models import * 

class UserController:
    def __init__(self):
        self.new_user = None

    def add_new_user(self, **user_data):
        required_fields = ["id", "first_name", "last_name", "street_address", "city", "state", "zip_code", "country"]
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
        
        # Create a new user from the provided data
        self.new_user = user_model.UserModel(**user_data)
        print("New user added successfully.")


user = UserController()
user.add_new_user(id=1,first_name="www",last_name="www",street_address="street",city="city",state="state",zip_code=1234,country="GER")