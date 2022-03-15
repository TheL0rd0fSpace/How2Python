class Dog():

    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY AND ALL INSTANCES OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name):

        #each argument after first is an attribute
        #first arguemnt is which instance that attribute is assigned to
        #assigned using self.attribute_name
        self.breed = breed
        self.name = name

    #Operations/Actions, formally called "Methods"
    def bark(self,num):
        print(f"{self.name} says WOOF! "*num)

my_dog = Dog(breed='Lab',name='Sam')

print(type(my_dog))
print(my_dog.species)
print(my_dog.breed)
print(my_dog.name)

my_dog.bark(7)



class Circle():

    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    #METHOD
    def get_cir(self):
        return self.radius * Circle.pi * 2

default_circle = Circle()
print(f"the default circle radius is {default_circle.radius}")
print(f"the default circle area is {default_circle.area}")
print(f"the default circle circumference is {default_circle.get_cir()}")

custom_circle = Circle(3)
print(f"the custom circle radius is {custom_circle.radius}")
print(f"the custom circle area is {custom_circle.area}")
print(f"the custom circle circumference is {custom_circle.get_cir()}")
