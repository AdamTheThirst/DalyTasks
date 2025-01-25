# Задача: Анализ заказов в интернет-магазине
# Уровень: 🟢⚪⚪️
#
# Описание задачи:
# Вам нужно написать функцию calculate_total(orders: dict) -> float,
# которая принимает словарь с заказами и возвращает общую сумму всех заказов.
# Словарь имеет следующую структуру:
# - Ключи — это названия товаров.
# - Значения — это словари с ключами price (цена за единицу) и quantity (количество).
#
# Пример:
# orders = {
#     "laptop": {"price": 1000, "quantity": 2},
#     "mouse": {"price": 50, "quantity": 5},
#     "keyboard": {"price": 80, "quantity": 3},
# }
# result = calculate_total(orders)
# print(result)  # 2490.0
#
# Требования:
# - Убедитесь, что цена и количество всегда положительные числа.
# - Если словарь пустой, верните 0.

# from https://t.me/pytonism

orders = {
    "laptop": {"price": 1000, "quantity": 2},
    "mouse": {"price": 50, "quantity": 5},
    "keyboard": {"price": 80, "quantity": 3},
}

def calculate_total(orders: dict) -> float:
    result = 0

    for order in orders:
        result += orders[order]["price"] * orders[order]["quantity"]


    return float(result)

print(calculate_total(orders))