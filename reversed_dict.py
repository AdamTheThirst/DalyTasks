# Задача: Обратный словарь
# Уровень: 🟢⚪⚪️
#
# Описание задачи:
# Напишите функцию invert_dict(d: dict) -> dict,
# которая принимает словарь и возвращает новый словарь,
# где ключи и значения поменяны местами.
# Если одно и то же значение встречается несколько раз,
# объедините соответствующие ключи в список.
#
# Пример:
# d = {"a": 1, "b": 2, "c": 1}
# result = invert_dict(d)
# print(result)  # {1: ["a", "c"], 2: ["b"]}
#
# Требования:
# - Сохраняйте порядок ключей в списках.
# - Если словарь пустой, верните пустой словарь.

# from https://t.me/pytonism

from collections import defaultdict

d = {"a": 1, "b": 2, "c": 1}

def invert_dict(d: dict) -> dict:
    if d:
        reversed = defaultdict(list)
        for k, v in d.items():
            reversed[v].append(k)

        return reversed
    return {}

print(invert_dict(d))