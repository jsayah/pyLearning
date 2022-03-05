file = open('file.txt', 'r') #this will open file and prepere to read.
# The R sets it to read mode. 
f = file.readlines()

newList = []

for line in f:
    newList.append(line.strip())#Does same as below


    # if line[-1] == '\n': #To make sure it only appends lines that need it. 
    #     newList.append(line[:-1]) # : is the slice command and -1 exempts last char
    # else:
    #     newList.append(line)#Appends line that dont have /n by default
        
print(f)
print(newList)

# def test(number):
#     return number - 2 

# test2 = test(int(input('Give me a number to subtract 2 from: ')))

# print(test2)

