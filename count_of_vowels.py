'''
Подсчёт количества гласных букв
Задача: Напишите функцию, которая подсчитывает количество гласных букв в строке. Гласные буквы: a, e, i, o, u (регистр не имеет значения).
Результат: Целое число — количество гласных букв.
Вводные данные:

text = "Hello, World!"
'''

vowels = 'aeiou'
text = "Hello, World!"

counter = 0

for letter in text:
    if letter.lower() in vowels:
        counter += 1

print(counter)
