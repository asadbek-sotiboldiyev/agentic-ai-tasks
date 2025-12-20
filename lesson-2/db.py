import sqlite3
import pyodbc
import secrets
from google.genai.types import UserContent, ModelContent
from custom_exceptions import *
from pretty_print import *

class DB:
    def __init__(self):
        try:
            self.con = pyodbc.connect(
                "Driver={ODBC Driver 17 for SQL Server};"
                "Server=localhost\\SQLEXPRESS;"
                "Database=aiagentcourse;"
                "Trusted_Connection=yes;"
            )
            self.cur = self.con.cursor()
        except Exception as e:
            print(f'==== Error creating connection: {e}')
            return

    def register(self, username, password):
        self.cur.execute("select 1 from users where username = ?;", (username,))
        is_exists = self.cur.fetchone()
        if is_exists:
            raise DuplicateUser(f"User with {username=} already exists.")
        try:
            self.cur.execute("insert into users(username, password) values (?, ?);", (username, password))
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(f"Error: {e}")


    def login(self, username, password):
        self.cur.execute("select id from users where username=? and password=?;", (username, password))
        row = self.cur.fetchone()
        if row is None:
            print(f"login or password is incorrect.")
            return 0
        user_id = row[0]
        return user_id

    def load_chats(self, user_id):
        self.cur.execute("select * from chats where user_id = ?;", (user_id))
        chats = self.cur.fetchall()
        chats_json = dict()
        for i in chats:
            chats_json[i[0]] = i[2]
        return chats_json
    
    def create_chat(self, user_id, chat_name = "chat-"):
        name = chat_name + secrets.token_hex(5)
        query = "INSERT INTO chats (user_id, name) OUTPUT INSERTED.id VALUES (?, ?);"
        self.cur.execute(query, (user_id, name))
        new_chat_id = self.cur.fetchone()
        print(new_chat_id)
        self.con.commit()
        return new_chat_id[0]

    def load_history(self, chat_id, context_size):
        self.cur.execute(f"select top {context_size*2} text, role from messages where chat_id=? order by id desc;", (chat_id,))
        rows = self.cur.fetchall()
        formatted_history = []
        for row in rows[::-1]:
            if row[1] == 'user':
                print_user(row[0])
                formatted_history.append(UserContent(row[0]))
            elif row[1] == 'model':
                print_model(row[0])
                formatted_history.append(ModelContent(row[0]))
        return formatted_history

    def save_message(self, chat_id, message, role):
        self.cur.execute("insert into messages (chat_id, text, role) values ( ?, ?, ?)", 
                         (chat_id, message, role))
        self.con.commit()
