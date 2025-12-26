"""Presenter that mediates between the repository and the view."""

from app.models.task_repository import TaskRepository
from app.views.task_view import TaskView
from app.services.currency_service import obter_cotacoes


class TaskPresenter:
    """Coordinate data flow between a `TaskRepository` and a `TaskView`."""

    def __init__(self, repository: TaskRepository, view: TaskView) -> None:
        """Initialize the presenter and trigger an initial currency update."""
        self.repository = repository
        self.view = view

        # Chamamos a atualização das moedas assim que o Presenter é criado
        self.exibir_moedas()

    def exibir_moedas(self) -> None:
        """Fetch currency info and update the view status."""
        info_moedas = obter_cotacoes()
        self.view.atualizar_status(info_moedas)

    def carregar_tarefas(self) -> None:
        """Load tasks from the repository and display them via the view."""
        try:
            tasks = self.repository.get_all()
            self.view.exibir_lista(tasks)
        except Exception as e:
            self.view.mostrar_erro(str(e))