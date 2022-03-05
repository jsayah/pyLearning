load = open('file.txt', 'r')
l = load.readlines()

list = []

for lines in l:
    list.append(lines.strip())

load.close

file = open('file.txt', 'w')

x = 0

for i in list:
    file.write(list[int(x)] + '\n')
    x += 1