import os


def list_py_files(folder="."):
    """os (вбудована): список .py файлів у папці."""
    return sorted(f for f in os.listdir(folder) if f.endswith(".py"))
