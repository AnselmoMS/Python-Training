"""Presenter that mediates between the repository and the view."""

from typing import Optional

from app.models.task_repository import TaskRepository
from app.views.task_view import TaskView
from app.services.currency_service import obter_cotacoes


class TaskPresenter:
    """Coordinate data flow between a `TaskRepository` and a `TaskView`."""

    def __init__(self, repository: TaskRepository, view: TaskView) -> None:
        """Initialize the presenter.

        Args:
            repository: TaskRepository instance for data access.
            view: TaskView instance for user interaction.
        """
        self.repository = repository
        self.view = view
        
        self.view.on_load = self.carregar_tarefas
        self.exibir_moedas()

    def exibir_moedas(self) -> None:
        """Fetch currency info and update the view status."""
        if self.view is None:
            return
        info_moedas = obter_cotacoes()
        self.view.atualizar_status(info_moedas)

    def carregar_tarefas(self) -> None:
        """Load tasks from the repository and display them via the view."""
        try:
            tasks = self.repository.get_all()
            self.view.exibir_lista(tasks)
        except Exception as e:
            self.view.mostrar_erro(str(e))