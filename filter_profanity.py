# ### Задача 1: **Фильтр нецензурных слов**
# **Уровень:** Джун
#
# **Описание задачи:**
# Вам нужно разработать функцию `filter_profanity(text: str, banned_words: list) -> str`,
# которая заменяет все нецензурные слова в тексте на символы `*`. Длина замены должна совпадать с длиной слова.
#
# **Пример:**
# ```python
# text = "This is a bad and ugly example."
# banned_words = ["bad", "ugly"]
# result = filter_profanity(text, banned_words)
# print(result)  # "This is a *** and **** example."
# ```
#
# **Требования:**
# - Слова должны заменяться независимо от регистра (например, "Bad" и "bad" считаются одинаковыми).
# - Не используйте готовые библиотеки для фильтрации (например, `re`).

text = "This is a Bad and ugly example."
banned_words = ["bad", "ugly"]

def filter_profanity(text: str, banned_words: list = None) -> str:
    if banned_words is None:
        return text

    for item in banned_words:
        text = text.replace(item, "*"*len(item))

    return text

result = filter_profanity(text, banned_words)

print(result)