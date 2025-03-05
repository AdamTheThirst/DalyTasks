'''Надо объеденить 2 упорядоченных списка'''

from random import randint

# version 1

lst_1 = [randint(0, 50) for i in range(10)]
lst_2 = [randint(30, 70) for i in range(12)]

lst_1.sort()
lst_2.sort()

if lst_1 < lst_2:
    lst_1, lst_2 = lst_2, lst_1

result = list()

print(lst_1)
print(lst_2)

flag = True

while flag:
    n = lst_1.pop(0)

    while True:
        if n >= lst_2[0]:
            result.append(lst_2.pop(0))
            flag = False
        else:
            result.append(n)
            break


if len(lst_1) > 0:
    result.extend(lst_1)

print(result)


# version 2

lst_1 = [randint(0, 50) for i in range(randint(10, 15))]
lst_2 = [randint(30, 70) for i in range(randint(10, 15))]

lst_1.sort()
lst_2.sort()

if lst_1 < lst_2:
    lst_1, lst_2 = lst_2, lst_1

print()
print(lst_1)
print(lst_2)


result = list()

j = 0

for i in range(len(lst_1)):
    if j >= len(lst_2):
        result.extend(lst_1[i-1:-1])
        break
    for _ in range(len(lst_2)-j):
        if lst_1[i] >= lst_2[j]:
            result.append(lst_2[j])
            j += 1
        else:
            result.append(lst_1[i])
            break

print(result)