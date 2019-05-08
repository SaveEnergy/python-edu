import random

rand_data = [random.randint(0, 100) for i in range(10)]


def swap(x: int, array: list):
    tmp = array.pop(x)
    array.insert(x + 1, tmp)


def bubble_sort(array: list):
    index = 0

    while index < len(array) - 1:
        if array[index] > array[index + 1]:
            swap(index, array)
            if index > 0:
                index -= 1
        else:
            index += 1

    return array


print(bubble_sort(rand_data))

