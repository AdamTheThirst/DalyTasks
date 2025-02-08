# Задача 3: **Работа с namedtuple: Сотрудники**
# **Уровень:** Джун
#
# **Описание задачи:**
# Создайте `namedtuple` с именем `Employee`, который содержит поля: `name`, `age`, `department`.
# Напишите функцию `filter_employees(employees: list, department: str) -> list`,
# которая возвращает список сотрудников из указанного отдела.
#
# **Пример:**
# ```python
# from collections import namedtuple
#
# Employee = namedtuple("Employee", ["name", "age", "department"])
# employees = [
#     Employee("Alice", 30, "HR"),
#     Employee("Bob", 25, "IT"),
#     Employee("Charlie", 35, "HR"),
# ]
# result = filter_employees(employees, "HR")
# print(result)  # [Employee(name='Alice', age=30, department='HR'), Employee(name='Charlie', age=35, department='HR')]

from collections import namedtuple

Employee = namedtuple("Employee", ["name", "age", "department"])
employees = [
    Employee("Alice", 30, "HR"),
    Employee("Bob", 25, "IT"),
    Employee("Charlie", 35, "HR"),
]

def filter_employees(employees: list = None, department: str = None) -> list:
    if employees is None:
        return []
    else:
        result = filter(lambda e: e.department == department, employees)
    return list(result)

result = filter_employees(employees, "HR")
print(result)  # [Employee(name='Alice', age=30, department='HR'), Employee(name='Charlie', age=35, department='HR')]
