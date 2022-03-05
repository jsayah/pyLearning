from operator import truediv


age = input("Input your age: ")


#age is recieved as string needs to be converted with int modifier
if int(age) >= 21: # : to end funtion statements like if statements
    print("Then its time to get stoned!")
else:
    print("Woah there! No smoke for you homie!")

for x in range(0, 10, 1): #start, stop, step
    print(x)

loop = True

while loop:
    name = input("Type stop: ")
    if name == 'stop': # can use single and double brackets
        loop = False # will only stop loop if given stop
        break


