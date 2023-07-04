file1 = open('file.txt', 'r')
lines = file1.readlines()
item = []
number = []
c = 0
for i in lines:
    if c > 4 and c < len(lines) - 3:
        line = i.split("|")
        item.append(line[1].strip())
        number.append(line[2].strip())
    c += 1
for i in item:
    print(i)
input("------------------")
for i in number:
    print(i)