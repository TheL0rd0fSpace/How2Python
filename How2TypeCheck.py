number = 10
print(type(number))

name = 'Sam'

butts = 1

if type(name) == str:
    print(f"{name} is a string.")
else:
    print(f"{name} is not a string.")

if type(number) == str:
    print(f"{number} is a string.")
else:
    print(f"{number} is not a string.")

if type(number) == int:
    print(f"{number} is a integer.")
else:
    print(f"{number} is not a integer.")

if type(name) == int:
    print(f"{name} is a integer.")
else:
    print(f"{name} is not a integer.")

if type(name) == str and type(number) is int and butts == True:
    print("You can test several things in one line!")
