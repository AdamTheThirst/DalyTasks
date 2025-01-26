# Задача: Слияние словарей с приоритетом
# Уровень: 🟠🟠⚪️
#
# Описание задачи:
# Напишите функцию `merge_dicts(dict1: dict, dict2: dict) -> dict`,
# которая объединяет два словаря. Если ключи совпадают,
# значение из второго словаря имеет приоритет.
#
# Пример:
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 20, "c": 30, "d": 40}
# result = merge_dicts(dict1, dict2)
# print(result)  # {"a": 1, "b": 20, "c": 30, "d": 40}
#
# Требования:
# - Не используйте встроенные функции для слияния словарей (например, `update` или `|`).
# - Если оба словаря пустые, верните пустой словарь.

# from https://t.me/pytonism

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    if not dict1 and not dict2:
        return {}

    for key, value in dict2.items():
        dict1[key] = value

    return dict1

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

print(merge_dicts(dict1, dict2))