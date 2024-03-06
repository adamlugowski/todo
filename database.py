import sqlite3


def init_db():
    with sqlite3.connect('todo') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
            id INTEGER,
            category_name TEXT
        )''')
        db.commit()
    with sqlite3.connect('todo') as db:
        categories_data = [
            (1, 'event'),
            (2, 'todo')
        ]
        cursor = db.cursor()
        cursor.executemany('INSERT INTO categories (id, category_name) VALUES (?, ?)', categories_data)
        db.commit()
    with sqlite3.connect('todo') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            name TEXT,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )''')
        db.commit()
