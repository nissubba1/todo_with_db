from datetime import datetime
from unittest.mock import MagicMock

import pytest

from todo.task_manager import TaskManager
from todo.task import Task


# Create instance of DB connection with Mock
@pytest.fixture
def task_manager_mock_db():
    manager = TaskManager()
    manager.db = MagicMock()
    return manager


@pytest.fixture
def mock_task():
    return Task(
        task_id=1,
        title="Test Task",
        created_at=datetime.now(),
        due_date=datetime(2025, 6, 20, 12, 0),
        is_complete=False,
        note="Mock note"
    )


def test_add_task_new(task_manager_mock_db, mock_task):
    task_manager_mock_db.db.fetch_value.return_value = 0  # Simulate not found
    task_manager_mock_db.add_task(mock_task)

    task_manager_mock_db.db.insert_task.assert_called_once()
    task_manager_mock_db.db.fetch_value.assert_called_once()


def test_add_task_existing(task_manager_mock_db, mock_task):
    task_manager_mock_db.db.fetch_value.return_value = 1  # Already exists
    task_manager_mock_db.add_task(mock_task)

    task_manager_mock_db.db.insert_task.assert_not_called()


def test_is_task_true(task_manager_mock_db):
    task_manager_mock_db.db.fetch_value.return_value = 1
    assert task_manager_mock_db.is_task(1) is True


def test_is_task_false(task_manager_mock_db):
    task_manager_mock_db.db.fetch_value.return_value = 0
    assert task_manager_mock_db.is_task(2) is False


def test_delete_task_exists(task_manager_mock_db, mock_task):
    task_manager_mock_db.db.fetch_value.return_value = 1
    task_manager_mock_db.db.fetch_task.return_value = mock_task
    task_manager_mock_db.db.delete_task.return_value = True
    task_manager_mock_db.delete_task(mock_task.task_id)
    task_manager_mock_db.db.delete_task.assert_called_once()


def test_delete_task_not_exists(task_manager_mock_db):
    task_manager_mock_db.db.fetch_value.return_value = 0
    task_manager_mock_db.delete_task(999)
    task_manager_mock_db.db.delete_task.assert_not_called()


def test_update_task_exists(task_manager_mock_db, mock_task):
    task_manager_mock_db.db.fetch_value.return_value = 1
    task_manager_mock_db.db.update_task.return_value = True
    task_manager_mock_db.update_task(mock_task)
    task_manager_mock_db.db.update_task.assert_called_once()


def test_update_task_not_exists(task_manager_mock_db, mock_task):
    task_manager_mock_db.db.fetch_value.return_value = 0
    task_manager_mock_db.update_task(mock_task)
    task_manager_mock_db.db.update_task.assert_not_called()


def test_get_task_exists(task_manager_mock_db, mock_task):
    task_manager_mock_db.db.fetch_value.return_value = 1
    task_manager_mock_db.db.fetch_task.return_value = mock_task
    result = task_manager_mock_db.get_task(mock_task.task_id)
    assert result == mock_task


def test_get_task_not_exists(task_manager_mock_db):
    task_manager_mock_db.db.fetch_value.return_value = 0
    result = task_manager_mock_db.get_task(404)
    assert result is None
