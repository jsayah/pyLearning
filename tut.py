y = 23
text = input('Username: ')
try: #Try and Except blocks are good for error handling.
    number = int(text) #It will try the code block and if it fails it will do the other block instead.
    print(number)
except:
    print('Invalid Username.')

class number():
    def __init__(self):#initialize self, always required
        self.var = 23

    def display(self, x):#can be called with .
        print(x)


