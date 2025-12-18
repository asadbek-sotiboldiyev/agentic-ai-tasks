from db import DB
from google.genai import Client
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = os.getenv('GEMINI_MODEL')

class Agent:
    def __init__(self, user_id):
        self.user_id = user_id
        self.client = Client(api_key=API_KEY)
        self.db = DB()
        self.chats = self.get_chats()
        self.current_chat = None
        self.context_size = 5
        # history = self.db.load_history(user_id=user_id)
        # self.chat = self.client.chats.create(model=MODEL, history=history)

    def ask(self, message):
        ai_message = self.chat.send_message(message).text
        for content in self.chat.get_history()[-2:]:
            self.db.save_message(self.current_chat, content.parts[0].text, content.role)
        return ai_message
    
    def get_chats(self):
        return self.db.load_chats(user_id=self.user_id)
    
    def change_chat(self, chat_id):
        history = self.db.load_history(chat_id=chat_id, context_size=self.context_size)
        self.chat = self.client.chats.create(model=MODEL, history=history)
        self.current_chat = chat_id
        print('Chat changed')
