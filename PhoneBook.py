try:
    file = open("phonebook.txt", "r")
    lines = file.read()
    file.close()
except:
    print("Can't read file!")
    lines = []

table = [i.strip() for i in lines.split(',')]

print(table)
