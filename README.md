# 📝 Todo CLI App with Python and PostgreSQL

This is a command-line Todo List application built in Python that uses PostgreSQL as a backend database. It allows users
to create, update, complete, delete, and view tasks with persistent storage.

## 🚀 Features

- ✅ Add new tasks with title, due date, and optional note
- 📋 View all tasks saved in the database
- ✏️ Update task details (title, note, due date)
- ✅ Mark tasks as complete
- ❌ Delete tasks by ID
- 💾 Persistent data storage using PostgreSQL
- 🔐 Environment variable support for secure database credentials (via .env)
- 🗂️ Interactive CLI menu for easy task management
- 🧪 Unit tests implemented with pytest for reliable code quality

## 🛠️ Tech Stack

- Python 3.11+
- PostgreSQL 17
- psycopg2 – for database connection
- python-dotenv – for managing environment variables
- pytest - unit test for test_manager class

## 📂 Project Structure

```
todo_with_db/
├── todo/                     # Main application package
│   ├── __init__.py
│   ├── database_config.py    # DB connection and queries
│   ├── task.py               # Task class model
│   ├── task_manager.py       # Core task operations logic
│
├── test/                    # Test suite
│   ├── __init__.py
│   ├── test_task_manager.py
│
├── .env                      # Environment variables (gitignored)
├── .gitignore                # Ignore.
├── main.py                   # Entry point to run the app
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

```

## 🧪 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/nissubba1/todo_with_db.git
cd todo_with_db
```

2. Create Postgres database

```sql
CREATE DATABASE todo;
```

3. Create a .env file:

```bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=todo
DB_USER=postgres
DB_PASSWORD=your_password
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the code

```bash
python3 main.py
```

6. Run the tests

```bash
pytest -v test/test_task_manager.py
```
