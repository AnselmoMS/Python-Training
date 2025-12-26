from setuptools import setup
from Cython.Build import cythonize
import os

# Lista manual dos arquivos para garantir que sejam tratados como módulos independentes
files = [
    "app/models/entities.py",
    "app/models/repository.py",
    "app/models/sqlite_database_connector.py",
    "app/presenters/task_presenter.py",
    "app/views/task_view.py",
    "app/views/gui_task_view.py"
]

setup(
    ext_modules=cythonize(files, language_level="3")
)