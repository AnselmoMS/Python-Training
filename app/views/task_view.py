"""View interfaces and simple console view implementations.

Defines `TaskView` abstract base class and a `ConsoleTaskView` concrete
implementation used for simple console-based interaction.
"""

from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Optional
from app.models.task import Task


class TaskView(ABC):
    """Abstract base class for task views."""
    
    on_load: Callable[[], None] | None
    """Callback to be invoked when the view is loaded or initialized."""
    
    @abstractmethod
    def exibir_lista(self, tasks: list[Task]) -> None:
        """Display a list of tasks to the user."""

    @abstractmethod
    def mostrar_erro(self, mensagem: str) -> None:
        """Display an error message to the user."""

    @abstractmethod
    def atualizar_status(self, texto: str) -> None:
        """Update status text in the UI (if applicable)."""
