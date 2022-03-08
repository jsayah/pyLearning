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
    
    def talk(self):
        print("Bark!")
        

class Cat(Dog):# inherits methods from dog
    def __init__(self, name, age, color):
        super().__init__(name, age)#super targets parent and passed values which assigned them to self. 
        self.color = color

    def talk(self):#Will override parent method
        print("Meow!")

josh = Cat("Josh", 26, "Brown")

print(josh.color)
print(josh.age)

josh.add_weight(19)#can use methods defined in dog since its parent of cat

print(josh.weight)

josh.speak()
josh.talk()
