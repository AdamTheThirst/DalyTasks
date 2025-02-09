# Задача 6: **График событий**
# **Уровень:** Мидл
#
# **Описание задачи:**
# Создайте `namedtuple` с именем `Event`, который содержит поля: `name`, `start_time`, `end_time`. Напишите функцию `find_overlapping_events(events: list) -> list`, которая возвращает список пар событий, которые пересекаются по времени.
#
# **Пример:**
# ```python
# from collections import namedtuple
#
# Event = namedtuple("Event", ["name", "start_time", "end_time"])
# events = [
#     Event("Meeting A", 9, 11),
#     Event("Meeting B", 10, 12),
#     Event("Meeting C", 13, 14),
# ]
# result = find_overlapping_events(events)
# print(result)  # [(Event(name='Meeting A', start_time=9, end_time=11), Event(name='Meeting B', start_time=10, end_time=12))]
# ```
#
# **Требования:**
# - События пересекаются, если их временные интервалы накладываются.
# - Если пересечений нет, верните пустой список.

from collections import namedtuple
from typing import List

Event = namedtuple("Event", ["name", "start_time", "end_time"])
events = [
    Event("Meeting A", 9, 11),
    Event("Meeting B", 10, 12),
    Event("Meeting C", 15, 16),
    Event("Meeting D", 18, 19),
    Event("Meeting E", 14, 17),
]

def find_overlapping_events(events: List[Event]) -> List[Event]:

    result = list()

    sorted_events = sorted(events, key=lambda e: e.start_time)

    for i in range(len(sorted_events) - 1):
        for j in range(i + 1, len(sorted_events)):
            event_1 = sorted_events[i]
            event_2 = sorted_events[j]

            if event_1.start_time < event_2.end_time and event_1.end_time > event_2.start_time:
                result.append((event_1, event_2))
    return result


result = find_overlapping_events(events)
for e in result:
    print(e)  # [(Event(name='Meeting A', start_time=9, end_time=11), Event(name='Meeting B', start_time=10, end_time=12))]