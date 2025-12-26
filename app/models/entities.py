from __future__ import annotations
"""Model entities for the task application.

This module defines the repository interface, the `Task` dataclass and a
simple in-memory `TaskManager` helper. Docstrings follow PEP 257.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List


class TaskRepository(ABC):
    """Abstract repository interface for task persistence.

    Implementations should provide `add` and `get_all` methods.
    """

    @abstractmethod
    def add(self, task_description: str) -> None:
        """Add a task with the given description to the repository."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List["Task"]:
        """Return a list of all stored Task objects."""
        raise NotImplementedError


@dataclass
class Task:
    """Represents a task entity."""

    id: int
    description: str


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