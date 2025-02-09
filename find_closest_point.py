# Задача 5: **Поиск ближайшей точки**
# **Уровень:** Мидл
#
# **Описание задачи:**
# Напишите функцию `find_closest_point(points: list, target: tuple) -> tuple`,
# которая принимает список точек (каждая точка — это кортеж `(x, y)`)
# и целевую точку `target`. Функция должна вернуть точку из списка,
# которая находится ближе всего к целевой.
#
# **Пример:**
# ```python
# points = [(1, 2), (4, 6), (7, 8)]
# target = (5, 5)
# result = find_closest_point(points, target)
# print(result)  # (4, 6)
# ```
#
# **Требования:**
# - Если список точек пустой, верните `None`.
# - Если несколько точек находятся на одинаковом расстоянии, верните первую из них.
from typing import List, Tuple
from math import sqrt

points = [(1, 2), (4, 6), (7, 8)]

def distance(p1: tuple, p2: tuple) -> float:
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def find_closest_point(points: List[Tuple[int, int]] = None, target: Tuple[int, int] = None) -> Tuple[int, int]:
    if not points or not target:
        return None

    result = min(points, key=lambda p: distance(p, target))
    return result

target = (5, 5)
result = find_closest_point(points, target)
print(result)  # (4, 6)
