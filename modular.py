import math
import myModule
# imported other python script and used functions here with .
print(myModule.func(int(input('Give me a number to add 5 to: '))))
# Used func function from myModules with input to add 5

def bung(x, test='2'): #This is an optional param with a default value
    print(x)
    print(test)

bung('john', '5') #if no second variable is added it will default to 2

