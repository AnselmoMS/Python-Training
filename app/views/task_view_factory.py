"""Factory for creating and configuring task views.

This module decouples view instantiation from command binding,
allowing clean separation between presenter and view setup.
"""

from enum import Enum
from typing import Callable, Optional

from app.views.task_view import TaskView

class TaskViewType(Enum):
    CONSOLE = "console"
    DEFAULT_VIEW = "default"
    MODERN_VIEW = "modern"


class TaskViewFactory:
    # Lazy imports to avoid circular dependencies and missing modules
    _VIEW_MAP = None

    @classmethod
    def _get_view_map(cls):
        """Lazily load and cache the view class mapping."""
        if cls._VIEW_MAP is not None:
            return cls._VIEW_MAP

        view_map = {}

        # Try to import ConsoleTaskView
        try:
            from app.views.console_task_view import ConsoleTaskView

            view_map[TaskViewType.CONSOLE] = ConsoleTaskView
        except Exception:
            pass

        # Try to import DefaultGuiTaskView (frm_task_view)
        try:
            from app.views.frm_task_view import FrmTaskView as DefaultGuiTaskView

            view_map[TaskViewType.DEFAULT_VIEW] = DefaultGuiTaskView
        except Exception:
            pass

        # Try to import ModernGuiTaskView (frm_task_custom_tkinter_view)
        try:
            from app.views.frm_task_custom_tkinter_view import (
                FrmTaskCustomTkinterView as ModernGuiTaskView,
            )

            view_map[TaskViewType.MODERN_VIEW] = ModernGuiTaskView
        except Exception:
            pass

        cls._VIEW_MAP = view_map
        return view_map

    def __init__(self, view_type: TaskViewType = TaskViewType.MODERN_VIEW):
        view_map = self._get_view_map()
        if view_type not in view_map:
            available = [v.value for v in view_map.keys()]
            raise ValueError(
                f"View type '{view_type.value}' not available. "
                f"Available types: {available}"
            )
        self.view_class = view_map[view_type]
    
    #Instantiate the view and bind commands.
    def create_view(self) -> TaskView:
        view = self.view_class()
        return view
