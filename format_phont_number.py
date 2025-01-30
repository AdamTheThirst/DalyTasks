# ### Задача 5: **Форматирование телефонных номеров**
# **Уровень:** Джун
#
# **Описание задачи:**
# Напишите функцию `format_phone_number(phone: str) -> str`, которая принимает строку с телефонным номером и возвращает его в формате `+X (XXX) XXX-XXXX`.
#
# **Пример:**
# ```python
# phone = "12345678901"
# result = format_phone_number(phone)
# print(result)  # "+1 (234) 567-8901"
# ```
#
# **Требования:**
# - Если длина номера не равна 11 символам, выбросьте исключение `ValueError`.
# - Убедитесь, что номер состоит только из цифр.


phone = "12345678901"

def format_phone_number(phone: str) -> str:
    if not phone.isdigit():
        raise ValueError('Number should be consists only of digits')
    if len(phone) != 11:
        raise ValueError('Wrong number of symbols')
    result = '+' + phone[0] + ' (' + phone[1:4] + ') ' + phone[4:7] + '-' + phone[7:11]
    return result



result = format_phone_number(phone)
print(result)  # "+1 (234) 567-8901"