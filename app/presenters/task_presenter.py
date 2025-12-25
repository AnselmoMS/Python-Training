from repository import TaskRepository
from app.views.task_view import TaskView
from app.services.currency_service import obter_cotacoes

class TaskPresenter:
    def __init__(self, repository: TaskRepository, view: TaskView):
        self.repository = repository
        self.view = view

        # Chamamos a atualização das moedas assim que o Presenter é criado
        self.exibir_moedas()
    
    def exibir_moedas(self):
        info_moedas = obter_cotacoes()
        self.view.atualizar_status(info_moedas)

    def carregar_tarefas(self):
        try:
            tasks = self.repository.get_all()
            self.view.exibir_lista(tasks)
        except Exception as e:
            self.view.mostrar_erro(str(e))