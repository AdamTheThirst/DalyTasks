# Задача: Координаты точек
# Уровень: 🟢⚪️⚪️
#
# Описание задачи:
# Напишите функцию calculate_distance(point1: tuple, point2: tuple) -> float, которая принимает две точки в виде кортежей (x, y) и возвращает расстояние между ними.
#
# Пример:
# point1 = (1, 2)
# point2 = (4, 6)
# result = calculate_distance(point1, point2)
# print(result)  # 5.0
#
# Требования:
# - Используйте формулу расстояния: sqrt((x2 - x1)^2 + (y2 - y1)^2).
# - Если точки совпадают, верните 0.0.

from math import sqrt

point1 = (1, 2)
point2 = (4, 6)

def calculate_distance(point1: tuple = None, point2: tuple = None) -> float:
    if point1 == point2:
        return 0.0
    result = sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    return result

result = calculate_distance(point1, point2)
print(result)  # 5.0
