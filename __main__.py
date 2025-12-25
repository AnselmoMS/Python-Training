import sys
import os

# Garante que a raiz do projeto esteja no caminho de busca
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importação direta (os .pyd estão na mesma pasta)
try:
    from repository import SqliteTaskRepository
    from app.views.gui_task_view import GuiTaskView
    from app.presenters.task_presenter import TaskPresenter
    
    def main():
        # Se o banco de dados estiver na mesma pasta:
        repo = SqliteTaskRepository("database.db")
        view = GuiTaskView()
        presenter = TaskPresenter(repo, view)
        view.btn_carregar.config(command=presenter.carregar_tarefas)
        view.iniciar_loop()

    if __name__ == "__main__":
        main()
except Exception as e:
    print(f"\nERRO AO CARREGAR: {e}")
    import traceback
    traceback.print_exc()
    input("\nPressione Enter para fechar...")