# База даних користувачів: логін, пароль та список оцінок (мінімум 4 користувачі)
users_db = {
    "ivan_petrov": {"password": "password123", "grades": [10, 4, 8, 3, 12, 5]},
    "olga_sid": {"password": "qwerty2026", "grades": [12, 11, 9, 8, 10]},
    "alex_k": {"password": "admin_pass", "grades": [2, 3, 5, 4, 1]},
    "mari_shev": {"password": "secret_key", "grades":[12, 10, 2 ,5 ,1]}
    }
print("=== Вхід у систему оцінок ===")
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

# Перевірка наявності користувача та правильності пароля
if login in users_db and users_db[login]["password"] == password:
    print(f"\nУспішний вхід! Вітаємо, {login}.")

    # Отримуємо список оцінок користувача
    user_grades = users_db[login]["grades"]
    print(f"Ваші оцінки: {user_grades}")

    # Підрахунок задовільних та незадовільних оцінок
    satisfactory_count = 0
    unsatisfactory_count = 0

    for grade in user_grades:
        if 5 <= grade <= 12:
            satisfactory_count += 1
        elif 1 <= grade <= 4:
            unsatisfactory_count += 1

    # Виведення результатів аналізу
    print(f"Кількість задовільних оцінок (5-12): {satisfactory_count}")
    print(f"Кількість незадовільних оцінок (1-4): {unsatisfactory_count}")

else:
    print("\nПомилка: Неправильний логін або пароль!")

