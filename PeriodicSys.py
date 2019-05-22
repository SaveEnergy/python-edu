try:
    file = open("periodic_table.csv", "r")
    lines = file.readlines()
    file.close()
except:
    print("Can't read file!")
    lines = []

del(lines[0])


periodic = {}

for l in lines:
    entries = l.split(',')
    entries = [s.strip() for s in entries]
    periodic[entries[1]] = tuple(entries[:1] + entries[2:8])

elements = [key for key in periodic]
elements.sort()

symbols = list(periodic.keys())
symbols.sort()

print(elements)
print(symbols)

