import random
from tkinter import *

from BubbleSort import bubble_sort

rand_data = [random.randint(0, 100) for i in range(10)]

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

print(bubble_sort(rand_data))

board = ["empty" for i in range(4)]

print(board)


root = Tk()


def hit(event):
    canvas.itemconfig(field00, fill='green')


header = Frame(root, width=800).pack()
Label(header, text="Battleships", font=("Sans", 32)).pack()

content = Frame(root, width=800).pack()
canvas = Canvas(content)
for i in range(0, 200, 25):
    canvas.create_rectangle(i-25, 0, i, 25, fill="green")
canvas.pack()
canvas.bind('<Button-1>', hit)


footer = Frame(root, width=800).pack()

mainloop()
