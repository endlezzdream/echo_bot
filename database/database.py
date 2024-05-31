import sqlite3


def initialize_db():
    con = sqlite3.connect('data_bot.dp')
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT,
            first_name TEXT,
            last_name TEXT
        )
    ''')
    con.commit()
    con.close()


def add_user(user_id, username, first_name, last_name):
    con = sqlite3.connect('data_bot.dp')
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO users (user_id, username, first_name, last_name)
        VALUES (?, ?, ?, ?)
    ''', (user_id, username, first_name, last_name))
    con.commit()
    con.cursor()


def get_user(user_id):
    con = sqlite3.connect('data_bot.dp')
    cursor = con.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE user_id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    con.close()
    return user
