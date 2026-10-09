# Лабораторна робота №3
# Консольний мінімагазин
from dis import name

products = {
    1: {"name": "Ноутбук", "price": 25000.00, "stock": 5},
    2: {"name": "Мишка", "price": 450.50, "stock": 15},
    3: {"name": "Клавіатура", "price": 850.00, "stock": 10},
    4: {"name": "Навушники", "price": 1200.75, "stock": 8},
    5: {"name": "Монітор", "price": 6500.00, "stock": 4}
}

cart = {}

admin_login = ("Nazar")
admin_password = "1234"

# Лямбда-функція для форматування ціни
format_price = lambda price: f"{price:.2f} грн"


# Перегляд каталогу товарів
def show_catalog():
    print("\n КАТАЛОГ ТОВАРІВ ")

    for product_id, product in products.items():
        print(
            f"{product_id}. {product['name']} | "
            f"Ціна: {format_price(product['price'])} | "
            f"Залишок: {product['stock']}"
        )


# Перегляд кошика
def show_cart():
    print("\n КОШИК ")

    if not cart:
        print("Кошик порожній.")
        return

    total = 0

    for product_id, quantity in cart.items():
        product = products[product_id]
        cost = product["price"] * quantity
        total += cost

        print(
            f"{product['name']} x {quantity} = "
            f"{format_price(cost)}"
        )

    print(f"Загальна сума: {format_price(total)}")


# Додавання товару до кошика
def add_to_cart():
    show_catalog()

    try:
        product_id = int(input("\nВведіть номер товару: "))
        quantity = int(input("Введіть кількість: "))

        if product_id not in products:
            print("Такого товару немає.")
            return

        available = products[product_id]["stock"] - cart.get(
            product_id, 0
        )

        if quantity <= 0:
            print("Кількість повинна бути більшою за нуль.")
        elif quantity > available:
            print("Недостатньо товару на складі.")
        else:
            cart[product_id] = cart.get(product_id, 0) + quantity
            print("Товар додано до кошика.")

    except ValueError:
        print("Помилка! Введіть ціле число.")


# Видалення товару з кошика
def remove_from_cart():
    show_cart()

    if not cart:
        return

    try:
        product_id = int(input("\nВведіть номер товару для видалення: "))

        if product_id not in cart:
            print("Такого товару немає в кошику.")
            return

        quantity = int(
            input("Скільки одиниць видалити? ")
        )

        if quantity <= 0:
            print("Кількість повинна бути більшою за нуль.")
        elif quantity >= cart[product_id]:
            del cart[product_id]
            print("Товар повністю видалено з кошика.")
        else:
            cart[product_id] -= quantity
            print("Кількість товару зменшено.")

    except ValueError:
        print("Помилка! Введіть ціле число.")


# Купівля товарів
def buy_products():
    if not cart:
        print("\nКошик порожній.")
        return

    show_cart()
    answer = input("\nПідтвердити покупку? (так/ні): ").lower()

    if answer != "так":
        print("Покупку скасовано.")
        return

    for product_id, quantity in cart.items():
        products[product_id]["stock"] -= quantity

    cart.clear()
    print("Покупку успішно оформлено!")


# Вхід адміністратора
def admin_panel():
    login = input("Введіть логін адміністратора: ")
    password = input("Введіть пароль: ")

    if login == admin_login and password == admin_password:
        print("\n ПАНЕЛЬ АДМІНІСТРАТОРА ")

        # Лямбда-функція для сортування за назвою
        sorted_products = sorted(
            products.items(),
            key=lambda item: item[1]["name"]
        )

        for product_id, product in sorted_products:
            print(
                f"{product['name']} | "
                f"Ціна: {format_price(product['price'])} | "
                f"Залишок: {product['stock']}"
            )
    else:
        print("Неправильний логін або пароль.")
# Головне меню магазину
def main():
    while True:
        print("\n МІНІМАГАЗИН ")
        print("1. Переглянути каталог")
        print("2. Додати товар до кошика")
        print("3. Переглянути кошик")
        print("4. Видалити товар з кошика")
        print("5. Купити товари")
        print("6. Увійти як адміністратор")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            show_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            buy_products()
        elif choice == "6":
            admin_panel()
        elif choice == "0":
            print("Дякуємо за відвідування магазину!")
            break
        else:
            print("Невірний пункт меню.")


if __name__ == "__main__":
    main()