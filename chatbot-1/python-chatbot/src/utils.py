def validate_username(username):
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    return username

def validate_password(password):
    if not password or len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")
    return password

def format_message(message):
    return message.strip().capitalize()