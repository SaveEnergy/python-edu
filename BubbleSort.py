import random

rand_data = [random.randint(0, 100) for i in range(10)]


def shift(x: int, array: list):
    array[x], array[x + 1] = array[x + 1], array[x]


def bubble_sort(array: list):
    sorted_list = list(array)
    for i in range(0, len(sorted_list) - 1):
        change = False
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                shift(j, sorted_list)
                change = True
        if not change:
            break
    return sorted_list


def some_sort(array: list):
    sorted_list = list(array)
    index = 0
    while index < len(sorted_list) - 1:
        if sorted_list[index] > sorted_list[index + 1]:
            shift(index, sorted_list)
            if index > 0:
                index -= 1
        else:
            index += 1
    return sorted_list


print("Sortierte Liste:")
print(some_sort(rand_data))
print("\nRandom Liste:")
print(rand_data)
print("\nBubblesort:")
print(bubble_sort(rand_data))

