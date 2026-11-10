from rich.console import Console
from rich.table import Table


def show_table(rows):
    """rich: виводить гарну таблицю."""
    t = Table(title="Результати")
    t.add_column("Ім'я")
    t.add_column("Бал")
    for name, score in rows:
        t.add_row(name, str(score))
    Console().print(t)
