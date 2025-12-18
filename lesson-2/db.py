import sqlite3
import pyodbc
from google.genai.types import UserContent, ModelContent
from custom_sxceptions import *

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
            raise UserNotFound(f"login or password is incorrect.")
        user_id = row[0]
        return user_id

    def load_chats(self, user_id):
        self.cur.execute("select * from chats where user_id = ?;", (user_id))
        chats = self.cur.fetchall()
        chats_json = dict()
        for i in chats:
            chats_json[i[0]] = i[2]
        return chats_json

    def load_history(self, chat_id, context_size):
        self.cur.execute(f"select top {context_size*2} text, role from messages where chat_id=? order by id desc;", (chat_id,))
        rows = self.cur.fetchall()
        formatted_history = []
        for row in rows:
            if row[1] == 'user':
                formatted_history.append(UserContent(row[0]))
            elif row[1] == 'model':
                formatted_history.append(ModelContent(row[0]))
        return formatted_history

    def save_message(self, chat_id, message, role):
        self.cur.execute("insert into messages (chat_id, text, role) values ( ?, ?, ?)", 
                         (chat_id, message, role))
        self.con.commit()