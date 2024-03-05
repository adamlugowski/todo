from database import init_db
import sqlite3
from tasks import todo_manager


if __name__ == '__main__':
    init_db()
    # in this section I will ask user how many tasks to add
    for _ in range(2):
        # in this section I will handle exceptions
        category = input('Category name: ')
        name = input('Task name: ')
        user_task = todo_manager.make_task(category, name)
        with sqlite3.connect('todo') as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO tasks (category_id, name) VALUES (?, ?)',
                           (user_task.task_type, user_task.description))
