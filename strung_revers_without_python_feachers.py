'''Задача: Переворот строки
Задача: Напишите функцию, которая переворачивает строку без использования встроенных методов или срезов.
Результат: Строка, записанная в обратном порядке.
Вводные данные:
text = "Python"
'''

text = "Python"
revers_str = ''

for i in range(len(text)):
    revers_str += text[len(text)-i-1]

print(revers_str)
