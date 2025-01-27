# Задача 2: **Сортировка задач по приоритету**
# **Уровень:** Джун
#
# **Описание задачи:**
# Вам нужно написать функцию `sort_tasks(tasks: list) -> list`,
# которая принимает список задач и возвращает его, отсортированный по приоритету.
# Каждая задача представлена словарем с ключами `name` (название задачи)
# и `priority` (число, где меньшее значение означает более высокий приоритет).
#
# **Пример:**
# ```python
# tasks = [
#     {"name": "Task A", "priority": 3},
#     {"name": "Task B", "priority": 1},
#     {"name": "Task C", "priority": 2},
# ]
# result = sort_tasks(tasks)
# print(result)
# # [
# #   {"name": "Task B", "priority": 1},
# #   {"name": "Task C", "priority": 2},
# #   {"name": "Task A", "priority": 3}
# # ]
# ```
#
# **Требования:**
# - Если приоритеты одинаковые, сохраняйте исходный порядок задач.
# - Если список пустой, верните пустой список.

def sort_tasks(tasks: list) -> list:
    if not tasks:
        return []
    else:
        result = sorted(tasks, key=lambda task: task["priority"])
        return result


tasks = [
    {"name": "Task A", "priority": 3},
    {"name": "Task B", "priority": 1},
    {"name": "Task C", "priority": 2},
]


print(sort_tasks(tasks))