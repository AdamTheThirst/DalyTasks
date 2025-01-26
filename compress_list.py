# Задача: Сжатие списка
# Уровень: 🟠🟠⚪
#
# Описание задачи:
# Напишите функцию compress_list(data: list) -> list,
# которая принимает список и возвращает новый список,
# где последовательности одинаковых элементов заменены на один элемент.
#
# Пример:
# data = [1, 1, 2, 2, 2, 3, 1, 1, 4, 4]
# result = compress_list(data)
# print(result)  # [1, 2, 3, 1, 4]
#
#
# Требования:
# - Сохраняйте порядок элементов.
# - Если список пустой, верните пустой список.

# from https://t.me/pytonism

data = [1, 1, 2, 2, 2, 3, 1, 1, 4, 4]

def compress_list(data: list) -> list:
    result = []
    for i in data:
        if not result:
            result.append(i)
        elif result[-1] != i:
            result.append(i)

    return result

print(compress_list(data))