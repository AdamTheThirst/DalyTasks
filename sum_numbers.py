# Задача: Сумма всех чисел в списке строк
# Уровень: 🟢⚪️⚪️
#
# Описание задачи:
# Напишите функцию sum_numbers(strings: list) -> int, которая принимает список строк,
# каждая из которых может содержать числа,
# разделённые пробелами. Функция должна вернуть сумму всех чисел из всех строк.
#
# Пример:
# strings = ["1 2 3", "4 5", "6"]
# result = sum_numbers(strings)
# print(result)  # 21
#
# Требования:
# - Используйте reduce для вычисления суммы.
# - Если список пустой или в строках нет чисел, верните 0.
# - Не используйте встроенные функции вроде sum.

from functools import reduce

strings = ["1 2 3", "4 5", "6"]

def reduce_sum(a: int, b: int) -> int:
    return a + b

def get_splited_list(str_list: list) -> list:
    str_ints = list()
    for item in str_list:
        tmp_list = item.split()
        str_ints.extend(tmp_list)
    return str_ints

def get_digit_list(str_list: list) -> list:
    int_list = list()
    for item in str_list:
        if item.isdigit():
            int_list.append(int(item))
    return int_list

def sum_numbers(strings: list) -> int:
    str_ints = get_splited_list(strings)
    int_list = get_digit_list(str_ints)
    final = reduce(reduce_sum, int_list)

    return final

print(sum_numbers(strings))




