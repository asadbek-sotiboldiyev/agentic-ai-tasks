import os
import sys
from getpass import getpass

from dotenv import load_dotenv

from agent import Agent
from db import DB
from pretty_print import (
    print_chats_list,
    print_input,
    print_model,
    print_model_thinking,
    print_user,
)

load_dotenv(".env")


class Application:
    def __init__(self):
        self.db = DB()
        self.agent = None
        self.commands = {
            0: self.show_menu,
            1: self.register,
            2: self.login,
            3: self.select_chat,
            4: sys.exit,
        }
        self.chat_id = 0
        self.menu = """Menu:
0. Show Menu
1. Register
2. Login
3. Select chat
4. Exit
"""

    def show_menu(self):
        print(self.menu)

    def register(self, username=None):
        if username:
            print("Username:", username)
        else:
            username = input("Username: ")
        password1 = getpass("Password: ")
        password2 = getpass("Password (again): ")

        if password1 != password2:
            print("Passwords do not match.")
            self.register(username=username)

        self.db.register(username=username, password=password1)
        print("Registered")

    def select_chat(self):
        if self.agent is None:
            self.login()
            return
        chats = self.agent.get_chats()
        print_chats_list(chats)
        while True:
            chat_id = input("Choose chat_id or create [new]: ")
            if chat_id == "0":
                return
            elif chat_id == "new":
                # new chat
                new_chat_id = self.db.create_chat(user_id=self.agent.user_id)
                self.chat_id = new_chat_id
                break
            if chats.get(int(chat_id), False):
                self.chat_id = chat_id
                break
            else:
                print("Invalid chat_id. Select another (or 0 for quit )")
        self.agent.change_chat(self.chat_id)

    def login(self):
        username = input("Username: ")
        password = getpass("Password: ")
        user_id = self.db.login(username=username, password=password)

        os.system("cls")
        if user_id != 0:
            agent = Agent(user_id=user_id)
            self.agent = agent
            self.select_chat()
            while True:
                user_message = print_input()
                delete_last_lines(2)
                if user_message.strip().lower() == "/bye":
                    os.system("cls")
                    break
                print_user(user_message)
                print_model_thinking()
                ai_message = agent.ask(user_message)
                delete_last_lines(3)
                print_model(ai_message)
        else:
            return

    def run(self):
        self.show_menu()

        while True:
            command_id = input("Command ID:")
            command_id = int(command_id)
            command = self.commands[command_id]
            command()
