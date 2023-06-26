import threading
import time


class Task:
    def __init__(self, task_id, task_func):
        self.task_id = task_id
        self.task_func = task_func

    def execute(self):
        self.task_func()
        print(f"Task {self.task_id} executed.")


class TaskQueue:
    def __init__(self):
        self.task_queue = []
        self.lock = threading.Lock()

    def add_task(self, task):
        with self.lock:
            self.task_queue.append(task)

    def process_tasks(self):
        while True:
            if len(self.task_queue) == 0:
                print("Task queue is empty. Waiting for tasks...")
                time.sleep(2)
                continue

            with self.lock:
                task = self.task_queue.pop(0)

            task.execute()


# Usage
def task_func_1():
    print("Executing task 1...")
    time.sleep(1)
    print("Task 1 completed.")


def task_func_2():
    print("Executing task 2...")
    time.sleep(2)
    print("Task 2 completed.")


def task_func_3():
    print("Executing task 3...")
    time.sleep(3)
    print("Task 3 completed.")


task_queue = TaskQueue()

task1 = Task(1, task_func_1)
task2 = Task(2, task_func_2)
task3 = Task(3, task_func_3)

task_queue.add_task(task1)
task_queue.add_task(task2)
task_queue.add_task(task3)

task_queue.process_tasks()
