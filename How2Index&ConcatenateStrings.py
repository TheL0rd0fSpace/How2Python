myString = "Hello World"
print(myString)

print(myString[0]) # outputs the first character of myString
print(myString[1]) # outputs the second character of myString
print(myString[2]) # outputs the third character of myString

#we can use : to perform a slice

print(myString[1:]) # outputs everything including and after the second character of myString
print(myString[:3]) # outputs everything up to, but not including, the fourth character of myString
print(myString[:]) # outputs myString

#negative indexing can go backwards

print(myString[-1]) # outputs the last character of myString
print(myString[:-1]) # outputs every up to, but not including the last character of myString

#can also use index and slice notation to grab elements of a sequance by a specified step size

print(myString[::1]) # outputs myString
print(myString[::2]) # outputs first letter, then every other letter after
print(myString[::-1]) # outputs myString backwards

print(myString + ' concatenate me!')
print(myString*10)
myString = myString + ' concatenate me!'
print(myString)
