# Задача: Подсчет голосов
# Уровень: 🟢⚪️⚪️
#
# Описание задачи:
# Вам нужно написать функцию count_votes(votes: list) -> dict,
# которая принимает список голосов и возвращает словарь
# с подсчетом голосов за каждого кандидата.
#
# Пример:
# votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
# result = count_votes(votes)
# print(result)  # {"Alice": 3, "Bob": 2, "Charlie": 1}
#
# Требования:
# - Если список пустой, верните пустой словарь.
# - Кандидаты могут повторяться в списке.

# from https://t.me/pytonism

from collections import defaultdict, Counter

votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

def count_votes_1(votes: list) -> dict:
    if not votes:
        return {}

    votes_dict = defaultdict(int)
    for vote in votes:
        votes_dict[vote] += 1

    return votes_dict

def count_votes_2(votes: list) -> dict:
    if not votes:
        return {}

    votes_dict = Counter(votes)
    return votes_dict

print(count_votes_1(votes))
print(count_votes_2(votes))