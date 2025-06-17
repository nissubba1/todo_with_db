import task
from task import Task
from database_config import DatabaseConfig


class TaskManager:
    def __init__(self):
        self.db = DatabaseConfig()

    def add_task(self, task: Task):
        if self.is_task(task.task_id):
            print(f"{task.title} already exists")
        else:
            query_stmt: str = "INSERT INTO tasks (task_id, title, created_at, due_date, is_complete, note) VALUES (%s, %s, %s, %s, %s, %s)"
            self.db.insert_task(query_stmt,
                                (task.task_id, task.title, task.created_at, task.due_date, task.is_complete, task.note))
            print(f"{task.title} inserted to database")

    def is_task(self, task_id: int) -> bool:
        query_stmt = "SELECT COUNT(*) FROM tasks WHERE task_id = %s"
        result: int | None = self.db.fetch_value(query_stmt, (task_id,))
        return result > 0

    def delete_task(self, task_id: int):
        if self.is_task(task_id):
            query_stmt: str = "SELECT * FROM tasks WHERE task_id = %s"
            task: Task | None = self.db.fetch_task(query_stmt, (task_id,))
            query_stmt: str = "DELETE FROM tasks WHERE task_id = %s"
            result = self.db.delete_task(query_stmt, (task_id,))
            task_title: str | int = task.title if task else task_id
            if result:
                print(f"{task_title} deleted successfully")
        else:
            print(f"Task ID {task_id} does not exist")

    def update_task(self, task: Task):
        if self.is_task(task.task_id):
            query_stmt: str = "UPDATE tasks SET title = %s, created_at = %s, due_date = %s, is_complete = %s, note = %s WHERE task_id = %s"
            result: bool = self.db.update_task(query_stmt,
                                               (task.title, task.created_at, task.due_date, task.is_complete, task.note,
                                                task.task_id))
            if result:
                print(f"{task.title} updated successfully")
            else:
                print(f"Task ID {task.task_id} does not exist")

    def set_complete(self, task_id: int) -> None:
        if self.is_task(task_id):
            query_stmt: str = "SELECT * FROM tasks WHERE task_id = %s"
            result: Task | None = self.db.fetch_task(query_stmt, (task_id,))
            if result:
                if not result.is_complete:
                    query_stmt: str = "UPDATE tasks SET is_complete = %s WHERE task_id = %s"
                    update_query: bool = self.db.execute_query(query_stmt, (True, task_id))
                    if update_query:
                        print(f"{result.title} marked complete")
                else:
                    print(f"{result.title} is already complete")
            else:
                print(f"Task ID {task_id} does not exist")

    def display_tasks(self):
        query_stmt = "SELECT * FROM tasks"
        result: list[Task] = self.db.fetch_all_tasks(query_stmt)
        print()
        for task in result:
            print("*" * 40)
            print(task)
            print("*" * 40)
