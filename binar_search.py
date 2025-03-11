from random import randint

sorted_list = [randint(0, 100) for _ in range(100)]
sorted_list.sort()

sl = [1, 3, 6, 7, 8, 10, 13, 15, 15, 16, 16, 16, 17, 17, 17, 18, 19, 21, 22, 22, 24, 26, 26, 28, 29, 30, 30, 31, 33, 33, 34, 36, 37, 40, 40, 41, 43, 43, 44, 44, 46, 48, 50, 50, 50, 51, 52, 52, 53, 53, 56, 56, 57, 59, 59, 61, 63, 65, 65, 65, 65, 66, 68, 68, 70, 70, 71, 71, 72, 74, 75, 76, 76, 79, 80, 80, 81, 81, 81, 82, 83, 83, 84, 84, 85, 88, 89, 89, 91, 92, 92, 93, 93, 95, 95, 98, 99, 99, 99, 100]
num = 38
number = randint(0, 20)


def binar_search(inner_sorted_list, number):
    if len(inner_sorted_list) == 0:
        return False

    mid = len(inner_sorted_list) // 2


    if inner_sorted_list[mid] == number:
        return True

    elif number < inner_sorted_list[mid]:
            return binar_search(inner_sorted_list[:mid], number)

    elif number > inner_sorted_list[mid+1]:
            return binar_search(inner_sorted_list[mid + 1:], number)

    else:
        return False


print(binar_search(sl, num))
