# Задача: Рейтинг продуктов
# Уровень: 🟠🟠⚪️
#
# Описание задачи:
# Напишите функцию top_products(products: dict, n: int) -> list,
# которая принимает словарь с продуктами и их рейтингами,
# а также число `n`, и возвращает список из `n` продуктов с самым высоким рейтингом.
#
# Пример:
# products = {
#     "laptop": 4.5,
#     "mouse": 4.7,
#     "keyboard": 4.2,
#     "monitor": 4.8,
#     "printer": 4.3,
# }
# result = top_products(products, 3)
# print(result)  # ["monitor", "mouse", "laptop"]
#
#
# Требования:
# - Если `n` больше количества продуктов, верните все продукты, отсортированные по рейтингу.
# - Если словарь пустой, верните пустой список.

# from https://t.me/pytonism

products = {
    "laptop": 4.5,
    "mouse": 4.7,
    "keyboard": 4.2,
    "monitor": 4.8,
    "printer": 4.3,
}

def top_products(products: dict, n: int) -> list:

    rate_list = []

    for key, value in products.items():
        rate_list.append((key, value),)

    rate_list = sorted(rate_list, key=lambda x: x[1], reverse=True)

    rate_list_final = list()
    if n <= len(rate_list):
        for i in range(n):
            rate_list_final.append(rate_list[i][0])
    else:
        for i in range(len(rate_list)):
            rate_list_final.append(rate_list[i][0])

    return rate_list_final



print(top_products(products, n=3))
print(top_products(products, n=6))