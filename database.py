import sqlite3


def init_db():
    with sqlite3.connect('todo') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
            id INTEGER,
            category_name TEXT
        )''')
        categories_data = [
            (1, 'event'),
            (2, 'todo')
        ]
        cursor.executemany('INSERT INTO categories (id, category_name) VALUES (?, ?)', categories_data)
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            name TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )''')
        cursor.execute('''DROP TRIGGER IF EXISTS date_of_task_trigger''')
        cursor.execute('''CREATE TRIGGER IF NOT EXISTS date_of_task_trigger
        AFTER INSERT ON tasks
        BEGIN
            UPDATE tasks SET created_at = NEW.created_at
            WHERE id = NEW.id;
        END;''')
        db.commit()
