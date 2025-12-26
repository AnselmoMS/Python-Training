"""Utilities to create and initialize the SQLite database used by the app.

This module exposes helpers that create the `tasks` table expected by the
repository implementation. The file name follows PEP8 (snake_case).
"""

import sqlite3


def create_tasks_table(db_path: str) -> None:
    """Create the `tasks` table in the SQLite database at `db_path`.

    The schema matches what `app.models.repository` expects: columns
    `id` (INTEGER PRIMARY KEY) and `desc` (TEXT).
    """
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, desc TEXT)"
        )
        conn.commit()


if __name__ == "__main__":
    create_tasks_table("meu_projeto.db")
    print("Database initialized at 'meu_projeto.db'.")
