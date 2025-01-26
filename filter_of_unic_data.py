# Задача : Фильтр уникальных значений
# Уровень: 🟢⚪️⚪️
#
# Описание задачи:
# Напишите функцию filter_unique(data: list) -> list,
# которая принимает список и возвращает новый список,
# содержащий только те элементы, которые встречаются в исходном списке ровно один раз.
#
# Пример:
# data = [1, 2, 2, 3, 4, 4, 5]
# result = filter_unique(data)
# print(result)  # [1, 3, 5]
#
# Требования:
# - Сохраняйте порядок элементов из исходного списка.
# - Если список пустой, верните пустой список.

# from https://t.me/pytonism

from random import randint

data = [randint(0, 50) for _ in range(10_000)]

# print(data)

def filter_unique(data: list) -> list:

    filtered_data = []

    if data:
        for i in data:
            if i not in filtered_data:
                filtered_data.append(i)

    return filtered_data

print(filter_unique(data))
