from colorama import Fore, Style, init


def colored(text, color="GREEN"):
    """colorama: повертає кольоровий текст."""
    init()
    return getattr(Fore, color) + text + Style.RESET_ALL
