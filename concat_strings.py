# Задача: Конкатенация строк с разделителем
# Уровень: 🟠🟠⚪️
#
# Описание задачи:
# Напишите функцию concat_strings(strings: list, delimiter: str) -> str,
# которая принимает список строк и строку-разделитель.
# Функция должна вернуть одну строку, где все строки из списка соединены через указанный разделитель.
#
# Пример:
# strings = ["apple", "banana", "cherry"]
# delimiter = ", "
# result = concat_strings(strings, delimiter)
# print(result)  # "apple, banana, cherry"
#
# Требования:
# - Используйте reduce для конкатенации строк.
# - Если список пустой, верните пустую строку.
from functools import reduce


strings = ["apple", "banana", "cherry"]
delimiter = ", "


def concat_strings(strings: str, delimiter: str = ', ') -> str:
    if not strings:
        return ''

    result = reduce(lambda x, y: x + delimiter + y, strings)
    return result

result = concat_strings(strings, delimiter)
print(result)  # "apple, banana, cherry"