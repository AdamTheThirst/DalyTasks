# Дан массив целых чисел nums. Верните true, если любое значение появляется
# в массиве хотя бы дважды, и верните false, если каждый элемент уникален.

from random import randint

numbers = list()

for _ in range(randint(10,20), randint(50,99)):
    numbers.append(randint(1,80))

def contains_duplicates(numbers: list = None):
    if numbers is not None:
        numbers.sort()
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                return True
    return False

print(contains_duplicates(numbers))
print(numbers)
