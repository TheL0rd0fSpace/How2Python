class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"{self.name} says meow!"

class Cow(Animal):
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"{self.name} says mooo!"

harold = Cow("harold")
niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())
print(harold.speak())
