from app.models.repository import SqliteTaskRepository
from app.views.task_view_factory import TaskViewFactory, TaskViewType
from app.presenters.task_presenter import TaskPresenter


def main(view_type: TaskViewType = TaskViewType.DEFAULT_VIEW):
    """Run the task manager application.

    Args:
        view_type: ViewType enum specifying which view to use.
                  Defaults to MODERN_VIEW.
    """
    repo = SqliteTaskRepository("database.db")

    # Create a factory with the specified view type
    factory = TaskViewFactory(view_type)

    # Create presenter without view initially
    presenter = TaskPresenter(repo, None)

    # Create view with presenter's callback already bound
    view = factory.create_view(on_load_command=presenter.carregar_tarefas)

    # Assign view and initialize currency display
    presenter.view = view
    presenter.exibir_moedas()

    # Start the interface
    view.iniciar_loop()


if __name__ == "__main__":
    import sys

    # Parse --view=console|default|modern from command line
    view_choice = TaskViewType.MODERN_VIEW
    for arg in sys.argv[1:]:
        if arg.startswith("--view="):
            view_name = arg.split("=", 1)[1]
            try:
                view_choice = TaskViewType(view_name)
            except ValueError:
                print(
                    f"Unknown view: {view_name}. "
                    f"Available: {', '.join([v.value for v in TaskViewType])}"
                )
                sys.exit(1)

    main(view_choice)
