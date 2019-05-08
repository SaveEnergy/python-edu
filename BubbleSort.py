import random

rand_data = [random.randint(0, 100) for i in range(10)]


def swap(x: int, array: list):
    tmp = array.pop(x)
    array.insert(x + 1, tmp)


index = 0

while index < len(rand_data) - 1:
    if rand_data[index] > rand_data[index + 1]:
        swap(index, rand_data)
        if index > 0:
            index -= 1
    else:
        index += 1

print(rand_data)
