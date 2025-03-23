'''
Проверка на анаграммы
Задача: Напишите программу, которая проверяет, являются ли две строки анаграммами (строки состоят из одних и тех же букв, но в разном порядке).
Результат: Булево значение: True, если строки — анаграммы, иначе False.
Вводные данные:
str1 = "listen"
str2 = "silent"
'''

str1 = "listen"
str2 = "silent"

str1_sort = ''.join(sorted(str1)).lower()
str2_sort = ''.join(sorted(str2)).lower()

if str1_sort == str2_sort:
    print(True)
else:
    print(False)
