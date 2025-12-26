from __future__ import annotations
"""Model entities for the task application.

This module defines a simple in-memory `TaskManager` helper. The `Task`
dataclass and the repository interface are defined in separate modules.
"""

from typing import List
from .task import Task


class TaskManager:
    """Simple in-memory manager for tasks used in examples and tests."""

    def __init__(self):
        """Create a new TaskManager with an empty task list."""
        self._tasks: List[Task] = []

    def add_task(self, description: str) -> None:
        """Validate and add a new task to the internal list.

        Raises ValueError if `description` is empty.
        """
        if not description:
            raise ValueError("A descrição não pode ser vazia!")
        new_id = len(self._tasks) + 1
        self._tasks.append(Task(new_id, description))
        print(f"Tarefa '{description}' adicionada.")

    def show_tasks(self) -> None:
        """Print all tasks to stdout in a readable format."""
        for t in self._tasks:
            print(f"[{t.id}] {t.description}")
