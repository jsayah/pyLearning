
load = open('file.txt', 'r')
l = load.readlines()

list = []

for lines in l:
    list.append(lines.strip())

load.close

print('Welcome to your list!')
print('You can use Add, Change, List, Remove and Stop!')
runprog = True

while runprog == True:
    choice = input('Choice: ')

    if choice == "Add" or choice == "add":
        add = input('Item to add: ')
        list.append(add.strip)
    elif choice == "Change" or choice == "change":
        x = 1
        for item in list:
            print(x, '. ', item)
            x += 1
        item = input('List Number: ')
        change = input('Change: ')
        list[int(item) - 1] = change
    elif choice == "List" or choice == "list":
        x = 1
        for item in list:
            print(x, '. ', item)
            x += 1
    elif choice == "Remove" or choice == "remove":
        x = 1
        for item in list:
            print(x, '. ', item)
            x += 1
        remove = input('List number: ')
        list.pop(int(remove) - 1)
    elif choice == "Stop" or choice == "stop":
        file = open('file.txt', 'w')
        x = 0
        for i in list:
            file.write(list[int(x)] + '\n')
            x += 1
        file.close
        break
    else:
        print('Invalid input!')