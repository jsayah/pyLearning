class Dog:
    dogs = [] #Static variable that is accesible by every instance of the class

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod #can be called by itself outside of class
    def num_dog(cls): #cls is the class
        return len(cls.dogs)

    @staticmethod #doesnt need class called at all. 
    def bark(n):#only need to pass a param if you WANT TO 
        """barks n times"""
        for _ in range(n):
            print("Bark!")



josh = Dog("Josh")
jon = Dog("Jon")

print(Dog.dogs)

print(Dog.num_dog()) #classmethod

Dog.bark(10) #staticmethod