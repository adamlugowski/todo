class Task:
    def __init__(self, task_type: str, description: str):
        self.task_type = task_type
        self.description = description


class EventTask(Task):
    pass


class ToDoTask(Task):
    pass


class ReminderTask(Task):
    pass


class Todo:
    def make_task(self, task_type, description):
        match task_type:
            case 'event':
                return EventTask('1', description)
            case 'todo':
                return ToDoTask('2', description)
            # case 'reminder':
            #     return ReminderTask('3', description)


todo_manager = Todo()
