"""Repository implementations for task persistence using SQLite.

This module provides a concrete `SqliteTaskRepository` that implements the
`TaskRepository` interface defined in `app.models.task_repository`.
"""

import sqlite3

from app.models.task import Task
from app.models.task_repository import TaskRepository


class SqliteTaskRepository(TaskRepository):
    """SQLite-based task repository.

    The repository stores tasks in a table named `tasks` with columns
    `id` (INTEGER PRIMARY KEY) and `desc` (TEXT).
    """

    def __init__(self, db_path: str):
        """Initialize repository and ensure the table exists."""
        self.db_path = db_path
        self._create_table()

    def _create_table(self) -> None:
        """Create the `tasks` table if it does not exist."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, desc TEXT)"
            )

    def add(self, task_description: str) -> None:
        """Insert a new task with the given description into the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT INTO tasks (desc) VALUES (?)", (task_description,))
            conn.commit()

    def get_all(self) -> list[Task]:
        """Return all tasks stored in the database as a list of `Task`.

        The method maps each row (id, desc) to a `Task` instance.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, desc FROM tasks")
            # Map rows -> Task objects
            return [Task(id=row[0], description=row[1]) for row in cursor.fetchall()]