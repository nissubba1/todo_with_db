from task_manager import TaskManager
from task import Task
from datetime import datetime

if __name__ == "__main__":
    manager = TaskManager()

    task1 = Task(1, "Task 1", datetime.now(), datetime(2025, 6, 20, 10, 50), False, "This is note")
    task2 = Task(2, "Task 2", datetime.now(), datetime(2025, 6, 20, 10, 50), False, "This is note 2")
    task3 = Task(3, "Task 3", datetime.now(), datetime(2025, 6, 20, 10, 50), False, "This is note 3")
    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)
    manager.delete_task(2)
    task_update = Task(3, "new title", datetime.now(), datetime(2025, 6, 20, 10, 50), True, "This is updated note")
    manager.update_task(task_update)
    manager.set_complete(3)
    manager.display_tasks()
