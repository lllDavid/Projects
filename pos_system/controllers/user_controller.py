from models import user

class UserController:
    def __init__(self,*args):
        self.new_user = user.User()
        print(f"New user added. {self.new_user}")
