class Agent:
    def __init__(self, user_id):
        self.user_id = user_id
        self.chat_history = []

    def ask(self, user_message):
        self.chat_history.append({"user": user_message})
        response = self.generate_response(user_message)
        self.chat_history.append({"agent": response})
        return response

    def generate_response(self, user_message):
        # Placeholder for response generation logic
        return f"You said: {user_message}"