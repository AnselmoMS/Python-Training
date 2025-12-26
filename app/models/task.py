from dataclasses import dataclass

"""Task entity for the task application.

Contains the `Task` dataclass used across the models and services.
"""


@dataclass
class Task:
    """Represents a task entity."""

    id: int
    description: str
