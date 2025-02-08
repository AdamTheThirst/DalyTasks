# Задача 2: **Сортировка студентов**
# **Уровень:** Джун
#
# **Описание задачи:**
# Вам нужно написать функцию `sort_students(students: list) -> list`, которая принимает список студентов, представленных кортежами `(name, grade)`, и возвращает список, отсортированный по оценкам (от большего к меньшему).
#
# **Пример:**
# ```python
# students = [("Alice", 85), ("Bob", 90), ("Charlie", 80)]
# result = sort_students(students)
# print(result)  # [("Bob", 90), ("Alice", 85), ("Charlie", 80)]
# ```
#
# **Требования:**
# - Если оценки одинаковые, сохраняйте исходный порядок.
# - Если список пустой, верните пустой список.

def sort_students(students: list = None) -> list:
    if students is None:
        students = []
    else:
        sorted_students = sorted(students, key=lambda student: student[1])
    return sorted_students

students = [("Alice", 85), ("Bob", 90), ("Charlie", 80)]
result = sort_students(students)
print(result)  # [("Bob", 90), ("Alice", 85), ("Charlie", 80)]