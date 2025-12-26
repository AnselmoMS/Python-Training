"""View interfaces and simple console view implementations.

Defines `TaskView` abstract base class and a `ConsoleTaskView` concrete
implementation used for simple console-based interaction.
"""

from abc import ABC, abstractmethod
from app.models.entities import Task


class TaskView(ABC):
    """Abstract base class for task views."""

    @abstractmethod
    def exibir_lista(self, tasks: list[Task]) -> None:
        """Display a list of tasks to the user."""

    @abstractmethod
    def mostrar_erro(self, mensagem: str) -> None:
        """Display an error message to the user."""

    @abstractmethod
    def atualizar_status(self, texto: str) -> None:
        """Update status text in the UI (if applicable)."""


# Implementação concreta para Console
class ConsoleTaskView(TaskView):
    """Console-based implementation of `TaskView` for demonstration."""

    def exibir_lista(self, tasks: list[Task]) -> None:
        print("\n--- LISTA DE TAREFAS ---")
        for t in tasks:
            print(f"[{t.id}] {t.description}")

    def mostrar_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO]: {mensagem}")

    def atualizar_status(self, texto: str) -> None:
        print(f"\n[Cotações]: {texto}")