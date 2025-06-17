from datetime import datetime
from typing import Optional


class Task:
    def __init__(self, task_id: int, title: str, created_at: datetime, due_date: datetime, is_complete: bool,
                 note: Optional[str] = None) -> None:
        self._task_id = task_id
        self._title = title
        self._created_at = created_at
        self._due_date = due_date
        self._is_complete = is_complete
        self._note = note

    @property
    def task_id(self) -> int:
        return self._task_id

    @task_id.setter
    def task_id(self, task_id: int) -> None:
        self._task_id = task_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime) -> None:
        self._created_at = created_at

    @property
    def due_date(self) -> datetime:
        return self._due_date

    @due_date.setter
    def due_date(self, due_date: datetime) -> None:
        self._due_date = due_date

    @property
    def is_complete(self) -> bool:
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete: bool) -> None:
        self._is_complete = is_complete

    @staticmethod
    def format_date_time(date) -> str:
        format_date = "%m/%d/%Y %I:%M:%S %p"
        return date.strftime(format_date)

    @property
    def note(self) -> str:
        return self._note

    @note.setter
    def note(self, note: str) -> None:
        self._note = note

    def __str__(self) -> str:
        return (f"ID: {self.task_id}\n"
                f"Title: {self.title}\n"
                f"Created At: {self.format_date_time(self.created_at)}\n"
                f"Due Date: {self.format_date_time(self.due_date)}\n"
                f"Is Complete: {self.is_complete}\n"
                f"Note: {self.note}")
