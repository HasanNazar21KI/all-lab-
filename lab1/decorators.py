# decorators.py

def multiply_by_two(func):
    """Декоратор, який множить числовий результат виконання функції на 2."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Перевіряємо, чи результат є числом (int або float)
        if isinstance(result, (int, float)):
            return result * 2
        return result  # Якщо результат не число, повертаємо без змін
    return wrapper