class Task:
    def __init__(self, task: str):
        self.task = task
        self.data = []

    def save(self):
        with open('todo.text', 'a') as file:
            file.write(self.task)

    def show(self):
        with open('todo.text', 'r') as file:
            for line in file:
                self.data.append(line)

        return self.data


task1 = Task('foo')
task1.save()
print(task1.show())