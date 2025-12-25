from app.models.repository import SqliteTaskRepository
from app.views.gui_task_view import GuiTaskView # Trocamos a View
from app.presenters.task_presenter import TaskPresenter

def main():
    repo = SqliteTaskRepository("database.db")
    view = GuiTaskView() # Instanciamos a versão GUI
    
    presenter = TaskPresenter(repo, view)
    
    # Vinculamos o evento do botão ao método do Presenter
    # No Delphi seria o OnClick
    view.btn_carregar.config(command=presenter.carregar_tarefas)
    
    # Iniciamos a interface
    view.iniciar_loop()

if __name__ == "__main__":
    main()