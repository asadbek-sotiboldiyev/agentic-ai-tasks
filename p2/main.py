from db import DB

class App:
    def __init__(self) -> None:
        self.commands = {
            0: self.show_menu,
            1: self.register,
            2: self.login
        }
        self.db = DB()
    def show_menu(self):
        print("Commands:\n0-show menu\n1-register\n2-login\n3-exit")
    def register(self, username=None):
        if username:
            print("username:", username)
        else:
            username = input("username: ")
        password1 = input("Passwrod:")
        password2 = input("Repeat passwrod:")
        if password1 != password2:
            print("Passwrods dont match")
            self.register(username)
            print("Registered")
        self.db.register(username=username, password=password1)
    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        user_id = self.db.login(username=username, password=password)
    def run(self):
        self.show_menu()