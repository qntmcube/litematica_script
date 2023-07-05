file1 = open('file.txt', 'r')
lines = file1.readlines()
item = []
number = []
for i in lines:
    line = i.split("|")
    if len(line) == 6 and "Item" not in line[1]:
        item.append(line[1].strip())
        number.append(line[2].strip())
file1.close()
with open('output/items.txt', 'w') as f:
    for i in item:
        f.write(i + "\n")
with open('output/amounts.txt', 'w') as f:
    for i in number:
        f.write(i + "\n")