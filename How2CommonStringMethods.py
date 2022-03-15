myString = "Hello World"
print(myString)
print(myString.upper()) # prints the string uppercase
print(myString.lower()) # outputs the string lowercase
print(myString.split()) # prints the string, by each blank space, into a list
print(myString.split("W")) # prints the string, by each "W", into a list

#in order for any of these to be changes, you have to use an assignment statement

myString = myString.upper() # myString is now itself, but uppercase
print(myString)
myString = myString.lower() # myString is now itself, but lowercase
print(myString)
myString = myString.split() # mystring is now a list, split at each blank space
print(myString[1]) # prints the second item in the new myString list
