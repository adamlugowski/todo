import sqlite3


def init_db():
    with sqlite3.connect('todo') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category INTEGER
        )''')
    with sqlite3.connect('todo') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT
        )''')
