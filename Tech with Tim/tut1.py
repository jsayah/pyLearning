
class Dog(object):
    def __init__(self, name, age): #runs when an object of value dog is INITIALIZED not called
        self.name = name
        self.age = age

    def speak(self):#self binds it to self
        print(f"Hi I am {self.name} and I am {self.age} years old!")\

    def change_age(self, age): # Can add other variables
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

josh = Dog("Josh", 26) #Creates a new instance of Dog('name') the josh before = sets the self
fred = Dog("Fred", 19)

josh.speak() # Calls the speak method 
fred.speak()

fred.change_age(9)

fred.speak()
print(josh.weight)

josh.add_weight(14)
print(josh.weight)
