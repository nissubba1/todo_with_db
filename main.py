from todo.task_manager import TaskManager
from todo.task import Task
from datetime import datetime


def welcome_msg(task_list: TaskManager, total_tasks: int, completed_tasks: int, incomplete_tasks: int) -> None:
    print("******************* Todo App ***********************")
    print(f"Number of Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Incomplete Tasks: {incomplete_tasks}")
    print("************* Incompleted Task *********************")
    if incomplete_tasks > 0:
        task_list.show_uncompleted_task()
    else:
        print("No incomplete tasks found")
    print("****************************************************")


def menu() -> None:
    print("*" * 52)
    print("1. Display all Tasks")
    print("2. Display completed tasks")
    print("3. Display incomplete tasks")
    print("4. Add new task")
    print("5. Remove task")
    print("6. Update task")
    print("7. Mark task as completed")
    print("8. Exit")
    print("*" * 52)


def get_date_time(prompt: str) -> datetime:
    while True:
        date_input = input(prompt)
        try:
            date_time = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
            return date_time
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD HH:MM (e.g., 2025-06-17 14:30)")


def menu_add_new_task(task_list: TaskManager) -> None:
    print("*" * 52)
    task_id: int | None = None
    while True:
        try:
            task_id: int = int(input("Enter task ID: "))
            if not task_list.is_task(task_id):
                break
            else:
                print(f"Task ID: {task_id} already exists, please choose another one.")
        except ValueError:
            print("Invalid input, please enter numeric input.")
    task_title: str = input("Enter task title: ")
    task_created_at: datetime = datetime.now()
    task_due_date: datetime = get_date_time("Enter task deadline (YYYY-MM-DD HH:MM): ")
    task_status: bool = False
    task_note: str = input("Enter note you want to add: ")
    task = Task(task_id, task_title, task_created_at, task_due_date, task_status, task_note)
    task_list.add_task(task)


def menu_update_task(task_list: TaskManager, task_id_update: int) -> None:
    print("*" * 52)
    if not task_list.is_task(task_id_update):
        print("Task ID not found")
        return
    task: Task = task_list.get_task(task_id_update)
    updated_task_title = task.title
    updated_task_created_at: datetime = task.created_at
    updated_task_due_date: datetime = task.due_date
    updated_task_status: bool = task.is_complete
    updated_task_note: str = task.note
    task_title: str = input("Enter new title or press Enter to keep it same: ")
    if task_title != updated_task_title:
        updated_task_title = task_title
    task_created_at: datetime = datetime.now()
    if task_created_at != updated_task_created_at:
        updated_task_created_at = task_created_at
    task_due_date: datetime = get_date_time("Enter new deadline (YYYY-MM-DD HH:MM) or press Enter to keep it samee: ")
    if task_due_date != updated_task_due_date:
        updated_task_due_date = task_due_date
    new_task_status: str = input("Enter task status(c = complete/i = incomplete) or press Enter to keep it same: ")
    task_status: bool = True if new_task_status == "c" else False
    if task_status != updated_task_status:
        updated_task_status = task_status
    task_note: str = input("Enter new note or press Enter to keep it same: ")
    if task_note != updated_task_note:
        updated_task_note = task_note
    task = Task(task_id_update, updated_task_title, updated_task_created_at, updated_task_due_date, updated_task_status,
                updated_task_note)
    task_list.update_task(task)


if __name__ == "__main__":
    manager = TaskManager()
    total_count: int = manager.count_total_tasks()
    total_count_incomplete: int = manager.count_incompleted_tasks()
    total_count_complete: int = manager.count_completed_task()
    choice = 0
    welcome_msg(manager, total_count, total_count_complete, total_count_incomplete)
    while choice != 8:
        menu()
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    manager.show_all_tasks()
                case 2:
                    manager.show_completed_task()
                case 3:
                    manager.show_uncompleted_task()
                case 4:
                    menu_add_new_task(manager)
                case 5:
                    del_task_id: int = int(input("Enter task ID: "))
                    manager.delete_task(del_task_id)
                case 6:
                    update_task_id: int = int(input("Enter task ID to update: "))
                    menu_update_task(manager, update_task_id)
                case 7:
                    task_to_complete: int = int(input("Enter task ID you want to mark complete: "))
                    manager.set_complete(task_to_complete)
                case 8:
                    print("Exiting program ...")
        except ValueError:
            print("Invalid input, please enter numeric input.")

    manager.close_connection()

    # task1 = Task(1, "Task 1", datetime.now(), datetime(2025, 6, 20, 10, 50), False, "This is note")
    # task2 = Task(2, "Task 2", datetime.now(), datetime(2025, 6, 20, 10, 50), False, "This is note 2")
    # task3 = Task(3, "Task 3", datetime.now(), datetime(2025, 6, 20, 10, 50), False, "This is note 3")
    # manager.add_task(task1)
    # manager.add_task(task2)
    # manager.add_task(task3)
    # manager.delete_task(2)
    # task_update = Task(3, "new title", datetime.now(), datetime(2025, 6, 20, 10, 50), True, "This is updated note")
    # manager.update_task(task_update)
    # manager.set_complete(3)
    # manager.show_all_tasks()
