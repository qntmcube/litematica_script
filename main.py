file1 = open('file.txt', 'r')
lines = file1.readlines()
item = []
number = []
for i in lines:
    try:
        line = i.split("|")
        item.append(line[1])
        number.append(line[2])
    except:
        continue
for i in item:
    print(i)
input("------------------")
for i in number:
    print(i)