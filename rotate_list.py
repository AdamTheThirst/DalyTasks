# Задача 5: **Ротация списка**
# **Уровень:** Джун
#
# **Описание задачи:**
# Напишите функцию `rotate_list(data: list, k: int) -> list`, которая принимает список и число `k`, и возвращает новый список, сдвинутый вправо на `k` позиций.
#
# **Пример:**
# ```python
# data = [1, 2, 3, 4, 5]
# k = 3
# result = rotate_list(data, k)
# print(result)  # [4, 5, 1, 2, 3]
# ```
#
# **Требования:**
# - Если `k` больше длины списка, используйте `k % len(data)` для вычисления реального сдвига.
# - Если список пустой, верните пустой список.

data = [1, 2, 3, 4, 5]

def rotate_list(data: list, k: int) -> list:
    rotated_data = list()
    if k > len(data):
        k = k % len(data)

    if not data:
        return rotated_data

    rotated_data.extend(data[k:])
    rotated_data.extend(data[0:k])

    return rotated_data

res = rotate_list(data, 7)

print(res)