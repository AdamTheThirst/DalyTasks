# ### Задача 4: **Анализ продаж**
# **Уровень:** Мидл
#
# **Описание задачи:**
# Создайте `namedtuple` с именем `Sale`, который содержит поля: `product`, `quantity`, `price`.
# Напишите функцию `total_sales(sales: list) -> float`,
# которая принимает список продаж и возвращает общую сумму продаж (количество * цена для каждого товара).
#
# **Требования:**
# - Если список продаж пустой, верните `0.0`.
# - Убедитесь, что количество и цена всегда положительные.

from collections import namedtuple
from functools import reduce
from typing import List

Sale = namedtuple("Sale", ["product", "quantity", "price"])
sales = [
    Sale("Laptop", 2, 1000.0),
    Sale("Mouse", 5, 50.0),
    Sale("Keyboard", 3, 80.0),
]


def reduce_price(i:float, sale: Sale) -> float:
    return ((sale.price * sale.quantity) + i)

def total_sales(sales: List[Sale] = None) -> float:
    if sales is None or len(sales) == 0:
        return 0.0

    result = reduce(reduce_price, sales, 0.0)

    return result

result = total_sales(sales)
print(result)