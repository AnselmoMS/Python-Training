from abc import ABC, abstractmethod
from typing import List
from .task import Task


class TaskRepository(ABC):
    """Abstract repository interface for task persistence.

    Implementations should provide `add` and `get_all` methods.
    """

    @abstractmethod
    def add(self, task_description: str) -> None:
        """Add a task with the given description to the repository."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Task]:
        """Return a list of all stored Task objects."""
        raise NotImplementedError
