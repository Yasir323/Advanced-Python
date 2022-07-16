from collections import deque


def count_down(n):
    while n > 0:
        print(f"T-minus {n}")
        yield
        n -= 1
    print("Blastoff!")


def count_up(n):
    x = 0
    while x < n:
        print(f"Counting up {x}")
        yield
        x += 1


class TaskScheduler:

    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        """Admit a newly started task to the scheduler."""
        self._task_queue.append(task)

    def run(self):
        """Run until there are no more tasks."""
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass


if __name__ == '__main__':
    sched = TaskScheduler()
    # Here the task scheduler will run the tasks in a round-robin manner.
    sched.new_task(count_down(10))
    sched.new_task(count_down(5))
    sched.new_task(count_up(15))
    sched.run()
