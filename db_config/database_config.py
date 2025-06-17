from todo.task import Task
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()


class DatabaseConfig:
    def __init__(self) -> None:
        """
        Create the database connection
        """
        try:
            self.conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_DATABASE")
            )
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            self.create_table()
            print("Database connection established")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Database connection failed", error)
            self.conn = None
            self.cur = None

    def fetch_all_tasks(self, query: str, params=None) -> list:
        """
        Fetches all tasks from the database.
        :param query: SQL query to execute
        :param params: Arguments to pass to the SQL query
        :return: List of tasks from the database
        """
        try:
            self.cur.execute(query, params)
            result_list: list[tuple] = self.cur.fetchall()
            task_list: list[Task] = []

            for row in result_list:
                task: Task = Task(*row)
                task_list.append(task)

            return task_list
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error executing query all", error)
            return []

    def fetch_task(self, query: str, params=None) -> Task | None:
        """
        Fetches a single task from the database.
        :param query: SQL query to execute
        :param params: Arguments to pass to the SQL query
        :return: A single Task object or None if not found
        """
        try:
            self.cur.execute(query, params)
            row: tuple = self.cur.fetchone()
            if row:
                return Task(*row)
            return None
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error executing query single", error)
            return None

    def create_table(self) -> bool:
        """
        Creates the table if it doesn't already exist.
        :return: None
        """
        try:
            query_stmt: str = ("CREATE TABLE IF NOT EXISTS tasks "
                               "(task_id INT PRIMARY KEY, "
                               "title VARCHAR(255), "
                               "created_at TIMESTAMP, "
                               "due_date TIMESTAMP, "
                               "is_complete BOOLEAN, "
                               "note TEXT);")
            self.cur.execute(query_stmt)
            print("Table created successfully")
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error creating table", error)
            return False

    def insert_task(self, query, params=None) -> bool:
        """
        Inserts a single task from the database.
        :param query: SQL query to execute
        :param params: Arguments to pass to the SQL query
        :return: True if the task was successfully inserted else False
        """
        try:
            self.cur.execute(query, params)
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error inserting task", error)
            return False

    def delete_task(self, query: str, params=None) -> bool:
        """
        Deletes a single task from the database.
        :param query: SQL query to execute
        :param params: Arguments to pass to the SQL query
        :return: True if the task was successfully deleted else False
        """
        try:
            self.cur.execute(query, params)
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error deleting task", error)
            return False

    def update_task(self, query: str, params=None) -> bool:
        """
        Updates a single task from the database.
        :param query: SQL query to execute
        :param params: Arguments to pass to the SQL query
        :return: True if the task was successfully updated else False
        """
        try:
            self.cur.execute(query, params)
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error updating task", error)
            return False

    def fetch_value(self, query: str, params=None) -> int | None:
        """
        Fetches a single value from the database.
        :param query: SQL query to execute
        :param params: Arguments to pass to the SQL query
        :return: Integer value or None if not found
        """
        try:
            self.cur.execute(query, params)
            row = self.cur.fetchone()
            if row:
                return row[0]
            return None
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error fetching value in db", error)

    def execute_query(self, query: str, params=None) -> bool:
        """
        Executes a SQL query.
        :param query: SQL query to execute
        :param params: Arguments to pass to the SQL query
        :return: True if the task was successfully executed else False
        """
        try:
            result = self.cur.execute(query, params)
            if result:
                return True
            return False
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error executing query", error)
            return False

    def close(self) -> None:
        """
        Closes the database connection
        :return: None
        """
        if self.conn:
            self.conn.close()
            print("Database connection closed")
        if self.cur:
            self.cur.close()
            print("Database cursor closed")
