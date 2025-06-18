############################################################
# Project Name : Todo App
# File Name    : todo/task_manager.py
# Author       : @nissubba1
# Created Date : 2025-06-16
# Updated Date : 2025-06-17
# Description  : Class to manage tasks and perform CURD operations with persistent database connection
############################################################

from .task import Task
from db_config.database_config import DatabaseConfig


class TaskManager:
    def __init__(self) -> None:
        """
        Initializes the database connection instance
        """
        self.db = DatabaseConfig()

    def add_task(self, task: Task) -> None:
        """
        Adds a task to the database.
        :param task: task to add
        :return: None
        """
        if self.is_task(task.task_id):
            print(f"{task.title} already exists")
        else:
            query_stmt: str = "INSERT INTO tasks (task_id, title, created_at, due_date, is_complete, note) VALUES (%s, %s, %s, %s, %s, %s)"
            self.db.insert_task(query_stmt,
                                (task.task_id, task.title, task.created_at, task.due_date, task.is_complete, task.note))
            print(f"{task.title} inserted to database")

    def is_task(self, task_id: int) -> bool:
        """
        Checks if the task is in the database.
        :param task_id: Task id to check
        :return: True if task is in the database else False
        """
        query_stmt = "SELECT COUNT(*) FROM tasks WHERE task_id = %s"
        result: int | None = self.db.fetch_value(query_stmt, (task_id,))
        return result > 0

    def delete_task(self, task_id: int) -> None:
        """
        Deletes a task from the database.
        :param task_id: Task id to delete
        :return: None
        """
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

    def update_task(self, task: Task) -> None:
        """
        Updates a task from the database.
        :param task: Task id to update
        :return: None
        """
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
        """
        Sets a task complete.
        :param task_id: Task id to change the status
        :return: None
        """
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

    def count_total_tasks(self) -> int:
        """
        Counts the total number of tasks in the database.
        :return: number of tasks in the database
        """
        query_stmt: str = "SELECT COUNT(*) FROM tasks"
        result: int | None = self.db.fetch_value(query_stmt)
        if result is not None:
            return result
        return -1

    def count_completed_task(self) -> int:
        """
        Counts the total number of completed tasks in the database.
        :return: Number of completed tasks in the database
        """
        query_stmt: str = "SELECT COUNT(*) FROM tasks WHERE is_complete = %s"
        result: int | None = self.db.fetch_value(query_stmt, (True,))
        if result is not None:
            return result
        return -1

    def count_incompleted_tasks(self) -> int:
        """
        Counts the total number of incompleted tasks in the database.
        :return: number of incompleted tasks in the database
        """
        query_stmt: str = "SELECT COUNT(*) FROM tasks WHERE is_complete = %s"
        result: int | None = self.db.fetch_value(query_stmt, (False,))
        if result is not None:
            return result
        return -1

    def show_completed_task(self) -> None:
        """
        Shows the completed task in the database.
        :return: None
        """
        query_stmt: str = "SELECT * FROM tasks WHERE is_complete = %s"
        result: list[Task] = self.db.fetch_all_tasks(query_stmt, (True,))
        self.display_tasks(result)

    def show_uncompleted_task(self) -> None:
        """
        Shows the uncompleted task in the database.
        :return: None
        """
        query_stmt: str = "SELECT * FROM tasks WHERE is_complete = %s"
        result: list[Task] = self.db.fetch_all_tasks(query_stmt, (False,))
        self.display_tasks(result)

    def get_task(self, task_id: int) -> Task | None:
        """
        Gets a task from the database.
        :param task_id: Task to get
        :return: Task or None if task does not exist
        """
        if self.is_task(task_id):
            query_stmt: str = "SELECT * FROM tasks WHERE task_id = %s"
            result: Task | None = self.db.fetch_task(query_stmt, (task_id,))
            return result
        return None

    @staticmethod
    def display_tasks(tasks_list: list[Task]) -> None:
        """
        Displays the tasks in the database.
        :param tasks_list: List of task to display
        :return: None
        """
        for task in tasks_list:
            print("*" * 40)
            print(task)
            print("*" * 40)

    def show_all_tasks(self) -> None:
        """
        Shows all tasks in the database.
        :return: None
        """
        query_stmt = "SELECT * FROM tasks"
        result: list[Task] = self.db.fetch_all_tasks(query_stmt)
        self.display_tasks(result)

    def close_connection(self) -> None:
        """
        Closes the database connection.
        :return: None
        """
        self.db.close()
        print("DB connection closed")
