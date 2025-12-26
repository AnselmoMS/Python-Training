from app.views.task_view import TaskView
from app.models.task import Task

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

    def iniciar_loop(self) -> None:
        """Console view does not have a main loop; this is a no-op."""
        pass
