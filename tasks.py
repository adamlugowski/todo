class Task:
    def __init__(self, name: str):
        self.name = name


class EventTask(Task):
    pass


class ToDoTask(Task):
    pass


class ReminderTask(Task):
    pass


class Todo:
    def make_task(self, task_type, task):
        match task_type:
            case 'event':
                return EventTask(task)
            case 'to_do':
                return ToDoTask(task)
            case 'reminder':
                return ReminderTask(task)




