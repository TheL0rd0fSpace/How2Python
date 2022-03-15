numSeven = 7
numFour = 4


## Addition
print(numSeven + numFour) #outputs 11

## Subtraction
print(numSeven - numFour) #outputs 3

## Multiplication
print(numSeven * numFour) #outputs 28

## Division
print(numSeven / numFour) #outputs 1.75

## Floor Division - Division that cuts off the decimal without rounding
print(numSeven // numFour) #outputs 1

## Modulo - Division that outputs the remainder
print(numSeven % numFour) #outputs 3

## Powers
print(numSeven**2) #outputs 49

## The Square Root of a number is the same as it taken to the 0.5 power
print(numFour**0.5) #outputs 2

## Python follows order of operations
print(2 + 10 * 10 + 3) #outputs 105

## Parenthesis can override order of operations, as normal
print((2+10) * (10+3)) #outputs 156

## You can use a variable to overwrite itself
numFourteen = numSeven
print("numFourteen equals {}, but we can add it to itself to make it bigger.".format(numFourteen))
numFourteen = numFourteen + numFourteen
print("Now numFourteen equals {}.".format(numFourteen))
