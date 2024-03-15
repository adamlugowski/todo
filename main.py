from database import init_db
import sqlite3
from tasks import todo_manager


if __name__ == '__main__':
    init_db()
    print('This app provide you adding up to 5 tasks')
    user_input = int(input('Would you like to view (1) or add(2) tasks?'))
    if user_input == 2:
        while True:
            number_of_tasks = int(input('How many tasks would you like to add? '))
            try:
                if number_of_tasks not in range(6):
                    raise Exception('You should type 1, 2, 3, 4, 5')
            except Exception as message:
                print(message)
            if number_of_tasks in range(6):
                break

        for _ in range(number_of_tasks):
            while True:
                category = input('Category name: ')
                try:
                    if category not in ('event', 'todo'):
                        raise Exception('Type event or todo')
                except Exception as message:
                    print(message)
                if category in ('event', 'todo'):
                    break

            name = input('Task name: ')
            user_task = todo_manager.make_task(category, name)
            try:
                if user_task is None:
                    raise Exception('Failed to create task')
            except Exception as message:
                print(message)

            with sqlite3.connect('todo') as db:
                cursor = db.cursor()
                cursor.execute('INSERT INTO tasks (category_id, name) VALUES (?, ?)', (user_task.task_type, user_task.description))
                db.commit()
    if user_input == 1:
        by_category = input('Which category (event, todo) would you like to see?')
        if by_category == 'event':
            with sqlite3.connect('todo') as db:
                cursor = db.cursor()
                event_tasks = cursor.execute('select * from tasks where category_id=1')
                for event in event_tasks:
                    print(event[2])
                db.commit()
        if by_category == 'todo':
            with sqlite3.connect('todo') as db:
                cursor = db.cursor()
                todo_tasks = cursor.execute('select * from tasks where category_id=2')
                for todo in todo_tasks:
                    print(todo[2])
                db.commit()
