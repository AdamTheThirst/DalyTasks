'''
Задача: Поиск самого длинного слова
Задача: Напишите программу, которая находит самое длинное слово в строке. Если таких слов несколько, вернуть первое из них.
Результат: Самое длинное слово.
Вводные данные:
text = "The quick brown fox jumps over the lazy dog"
'''

text = "The quick brown fox jumps over the lazy dog"
text_list = text.split()

word = text_list[0]


for i in range(len(text_list)-1):
    if len(word) < len(text_list[i+1]):
        word = text_list[i+1]

print(word)