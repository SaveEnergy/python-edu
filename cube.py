import random


def throw_cube():
    rand_cube_list = []
    while True:
        rand_cube_throw = random.randint(1, 6)
        if rand_cube_throw != 6:
            rand_cube_list.append(rand_cube_throw)
        else:
            return len(rand_cube_list)


count = 0
for i in range(100):
    count += throw_cube()
print(count / 100)
