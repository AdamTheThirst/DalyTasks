# Задача: Сводка по сотрудникам
# Уровень: 🟠🟠⚪️
#
# Описание задачи:
# Вам нужно написать функцию employee_summary(employees: list) -> dict,
# которая принимает список сотрудников и возвращает сводку по отделам.
# Каждый сотрудник представлен словарем с ключами name (имя) и department (отдел).
#
# Пример:
# employees = [
#     {"name": "Alice", "department": "HR"},
#     {"name": "Bob", "department": "IT"},
#     {"name": "Charlie", "department": "HR"},
#     {"name": "David", "department": "IT"},
#     {"name": "Eve", "department": "Finance"},
# ]
# result = employee_summary(employees)
# print(result)
# # {
# #   "HR": ["Alice", "Charlie"],
# #   "IT": ["Bob", "David"],
# #   "Finance": ["Eve"]
# # }
#
# Требования:
# - Сохраняйте порядок сотрудников в списках.
# - Если список сотрудников пустой, верните пустой словарь.

# from https://t.me/pytonism

from collections import defaultdict

employees = [
    {"name": "Alice", "department": "HR"},
    {"name": "Bob", "department": "IT"},
    {"name": "Charlie", "department": "HR"},
    {"name": "David", "department": "IT"},
    {"name": "Eve", "department": "Finance"},
]

def employee_summary(employees: list) -> dict:
    if employees:
        summury = defaultdict(list)
        for data in employees:
            summury[data["department"]].append(data["name"])
        return summury

    return {}

print(employee_summary(employees))