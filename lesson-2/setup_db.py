import sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()


create_table_script = """
create table users(
    id integer primary key,
    username text,
    password text
);

create table history(
    id integer primary key,
    user_id int,
    user_message_id int,
    message text,
    role text -- user, model
);
"""


cur.executescript(create_table_script)

cur.close()
con.close()



