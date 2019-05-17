import random

print("Hello World\n")
print("Yes, that's it... ")

t = "ABC abc 0456"
print(sorted(t))

my_list = [1, 2, 3, 4, 5]
print(my_list[2], my_list[2:2], my_list[2:3])


data = [random.randint(0, 100) for i in range(10)]
average = sum(data)//len(data)

print(data, average)
if data[len(data)//2] > average:
    print(True)
else:
    print(False)
