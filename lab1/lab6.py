# lab6.py

from decorators import multiply_by_two

@multiply_by_two
def calculate_math():
    """Приклад математичної функції для лабораторної."""
    x = 10
    y = 15
    return x + y  # 10 + 15 = 25, а декоратор помножить на 2 (буде 50)

if __name__ == "__main__":
    result = calculate_math()
    print("Результат виконання програми:", result)