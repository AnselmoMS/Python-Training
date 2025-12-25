from abc import ABC, abstractmethod
from app.models.entities import Task

class TaskView(ABC):
    @abstractmethod
    def exibir_lista(self, tasks: list[Task]):
        pass

    @abstractmethod
    def mostrar_erro(self, mensagem: str):
        pass
    
    @abstractmethod
    def atualizar_status(self, texto):
        pass

# Implementação concreta para Console
class ConsoleTaskView(TaskView):
    def exibir_lista(self, tasks: list[Task]):
        print("\n--- LISTA DE TAREFAS ---")
        for t in tasks:
            print(f"[{t.id}] {t.description}")

    def mostrar_erro(self, mensagem: str):
        print(f"\n[ERRO]: {mensagem}")

    def atualizar_status(self, texto):
        print(f"\n[Cotações]: {texto}")