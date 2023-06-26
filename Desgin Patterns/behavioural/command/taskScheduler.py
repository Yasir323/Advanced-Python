"""Suppose you have a task scheduler that needs to execute various tasks at different times or intervals. The Command
pattern can be used to implement the deferred execution of tasks. Each task is encapsulated as a command object,
which holds the task logic and execution time. The task scheduler maintains a collection of these commands and
executes them at the specified times or intervals. """

import time


class Command:
    def __init__(self, task, execution_time):
        self.task = task
        self.execution_time = execution_time

    def execute(self):
        if time.time() >= self.execution_time:
            self.task()


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def schedule_task(self, task, execution_time):
        command = Command(task, execution_time)
        self.tasks.append(command)

    def run_tasks(self):
        while self.tasks:
            task = self.tasks.pop(0)
            task.execute()


# Usage
def greet():
    print("Hello, world!")


def announce():
    print("Task execution time reached.")


scheduler = TaskScheduler()
scheduler.schedule_task(greet, time.time() + 5)
scheduler.schedule_task(announce, time.time() + 10)

scheduler.run_tasks()  # After 5 seconds: "Hello, world!" / After 10 seconds: "Task execution time reached."
