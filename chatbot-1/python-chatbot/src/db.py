class DB:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = password

    def login(self, username, password):
        if username not in self.users:
            raise ValueError("User not found.")
        if self.users[username] != password:
            raise ValueError("Incorrect password.")
        return username  # In a real application, this would return a user ID or similar.