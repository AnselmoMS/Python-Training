from app.models.repository import SqliteTaskRepository
# from app.views.frm_task_view import GuiTaskView # Alternativa de view GUI
from app.views.frm_task_custom_tkinter_view import FrmTaskCustomTkinterView as GuiTaskView
from app.presenters.task_presenter import TaskPresenter


def main():
    repo = SqliteTaskRepository("database.db")
    view = GuiTaskView()
    presenter = TaskPresenter(repo, view)
    
    # Vinculamos o evento do botão ao método do Presenter
    # No Delphi seria o OnClick
    view.btn_carregar.configure(command=presenter.carregar_tarefas)
    
    # Iniciamos a interface
    view.iniciar_loop()

if __name__ == "__main__":
    main()