'''Надо объеденить 2 упорядоченных списка'''

from random import randint

lst_1 = [randint(0, 50) for i in range(50)]
lst_2 = [randint(30, 70) for i in range(50)]

lst_1.sort()
lst_2.sort()

print(lst_1, lst_2)