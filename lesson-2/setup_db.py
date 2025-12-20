import sqlite3
from db import DB

database = DB()

# con = sqlite3.connect("db.sqlite3")
con = database.con
cur = con.cursor()


create_table_script = """
create table users(
    id int IDENTITY,
    name nvarchar(255),
    username nvarchar(255),
    password NVARCHAR(255)
);
create table chats(
    id int IDENTITY,
    user_id int,
    name nvarchar(255),
);
create table messages(
    id int IDENTITY,
    chat_id int,
    role nvarchar(10),
    text NVARCHAR(max)
);
"""


cur.executescript(create_table_script)

cur.close()
con.close()



