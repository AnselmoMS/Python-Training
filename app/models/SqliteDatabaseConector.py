"""Compatibility shim for the older module name.

This module kept for backwards compatibility. Please import
`app.models.sqlite_database_connector.create_tasks_table` instead.
"""

from warnings import warn

from .sqlite_database_connector import create_tasks_table

warn(
    "app.models.SqliteDatabaseConector is deprecated; use "
    "app.models.sqlite_database_connector instead.",
    DeprecationWarning,
)


if __name__ == "__main__":
    create_tasks_table("meu_projeto.db")