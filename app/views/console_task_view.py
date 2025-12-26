from collections.abc import Callable
from app.views.task_view import TaskView
from app.models.task import Task

# Implementação concreta para Console
class ConsoleTaskView(TaskView):
    """Console-based implementation of `TaskView` for demonstration."""

    def __init__(self):
        """Initialize the console view."""
        super().__init__()
        self._on_load = None
        self._on_load_command = None
        self._is_running = False

    def exibir_lista(self, tasks: list[Task]) -> None:
        print("\n--- LISTA DE TAREFAS ---")
        if not tasks:
            print("Nenhuma tarefa encontrada.")
        else:
            for t in tasks:
                print(f"[{t.id}] {t.description}")

    def mostrar_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO]: {mensagem}")

    def atualizar_status(self, texto: str) -> None:
        print(f"\n[Cotações]: {texto}")

    
    def iniciar_loop(self) -> None:
        self._on_load_command = self.on_load
        """Start an interactive console loop for task management."""
        self._is_running = True
        print("\n=== Gerenciador de Tarefas (Console) ===")
        print("Digite 'help' para ver as opções disponíveis.\n")

        while self._is_running:
            try:
                comando = input("> ").strip().lower()

                if comando in ["exit", "sair", "q"]:
                    self._is_running = False
                    print("\nEncerrando aplicação...")

                elif comando in ["help", "?"]:
                    self._exibir_menu()

                elif comando in ["carregar", "load", "l"]:
                    if self._on_load_command is not None:
                        self._on_load_command()
                    else:
                        self.mostrar_erro("Comando de carregamento não configurado.")

                elif comando in ["listar", "list", "ls"]:
                    # Trigger load to show tasks
                    if self._on_load_command is not None:
                        self._on_load_command()
                    else:
                        self.mostrar_erro("Comando de carregamento não configurado.")

                elif comando == "":
                    continue

                else:
                    print(f"Comando desconhecido: '{comando}'. Digite 'help' para ajuda.")

            except KeyboardInterrupt:
                print("\n\nInterrompido pelo usuário.")
                self._is_running = False
            except Exception as e:
                self.mostrar_erro(f"Erro ao processar comando: {str(e)}")

    def _exibir_menu(self) -> None:
        """Display the available commands menu."""
        menu =  """
                --- MENU DE OPÇÕES ---
                carregar, load, l       - Carrega e exibe a lista de tarefas
                listar, list, ls        - Exibe a lista de tarefas
                help, ?                 - Exibe este menu
                exit, sair, q           - Sai da aplicação
                """
        print(menu)

