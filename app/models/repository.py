import sqlite3
from app.models.entities import Task, TaskRepository

class SqliteTaskRepository(TaskRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, desc TEXT)")

    def add(self, task_description: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT INTO tasks (desc) VALUES (?)", (task_description,))
            conn.commit()

    def get_all(self) -> list[Task]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, desc FROM tasks")
            # Mapeamento: Linha do banco -> Objeto Task
            return [Task(id=row[0], description=row[1]) for row in cursor.fetchall()]