'''
Задача : Разбиение числа на цифры
Задача: Напишите функцию, которая разбивает число на его цифры и возвращает их в виде списка.
Результат: Список цифр числа.
'''

from random import randint

num = randint(1111, 99999)

print(f'{num=}')

#variant 1
num_str = str(num)
num_str_list = list()
for i in num_str:
    num_str_list.append(int(i))

del num_str
print(f'{num_str_list=}')

#variant 2
num_list=list()

num_tmp = num
while True:
    if num_tmp > 10:
        remainder = num_tmp % 10
        num_tmp = num_tmp // 10
        num_list.insert(0,remainder)
    else:
        num_list.insert(0, num_tmp)
        break

print(f'{num_list=}')