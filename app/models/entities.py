from __future__ import annotations # <--- A "mágica" para evitar erros de tipo Task em get_all na classe abstrata
from dataclasses import dataclass
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


# Esta é a sua "Interface" (IProductRepository do Delphi)
class TaskRepository(ABC):
    
    @abstractmethod
    def add(self, task_description: str) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass


@dataclass
class Task:
    id: int
    description: str

class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, description: str):
        if not description:
            raise ValueError("A descrição não pode ser vazia!")
        new_id = len(self._tasks) + 1
        self._tasks.append(Task(new_id, description))
        print(f"Tarefa '{description}' adicionada.")

    def show_tasks(self):
        for t in self._tasks:
            print(f"[{t.id}] {t.description}")