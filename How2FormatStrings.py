## Three main methods to format strings
#First uses Modulo (%)
#Second uses .format()
#Third uses f-strings

#You can inject one or more things, and they can be strings or variables

        ##MODULO METHOD

##there are different types of modulos for formatting strings
# %s converts to a string with the str() function. this changes integers, floats, and escape sequences
# %r converts to a string with the repr() function. this leaves escape sequences unchanged.
# %d converts to a string by first converting all numbers to integers without rounding
# floating points use the format %x.yf.
    #the x indicates the minimum number of characters the string should contain, whitespace will be added if necesarry
    #the y indicated the maximum number of characters after the decimal point


#This shows how to format in one thing, multiple things, and variables
x = "some"
y = "more"
print("I'm going to inject %s here." %"something")
print("I'm going to inject %s text here, and %s text here." %("some","more"))
print("I'm going to inject %s text here, and %s text here." %(x,y))

#This shows the difference between %s and %r
print('He said his name was %s.' %'Fred')
print('He said his name was %r.' %'Fred')
print('I once caught a fish %s.' %'this \tbig')
print('I once caught a fish %r.' %'this \tbig')

##This shows the difference between %s and %d
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)

##This shows how floating points works
print('Floating point numbers: %5.2f' %(13.144)) # outputs Floating point numbers: 13.14
print('Floating point numbers: %1.0f' %(13.144)) # outputs Floating point numbers: 13
print('Floating point numbers: %1.5f' %(13.144)) # outputs Floating point numbers: 13.14400
print('Floating point numbers: %10.2f' %(13.144)) # outputs Floating point numbers:      13.14
print('Floating point numbers: %25.2f' %(13.144)) # outputs Floating point numbers:                     13.14

##Any combination of conversion tools can be used in a single print statement
print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!')) # outputs First: hi!, Second:  3.14, Third: 'bye!'


        ## .format() METHOD
print('This is a string with an {}'.format('insert')) # outputs This is a string with an insert
##A few advantages
#Inserted objects can be called by index
print('The {2} {1} {0}'.format('fox','brown','quick')) # outputs The quick brown fox
#Inserted objects can be assigned keywords
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3)) # First Object: 1, Second Object: Two, Third Object: 12.3
#Inserted objects can be reused, avoiding duplication
print('A %s saved is a %s earned.' %('penny','penny')) # outputs A penny saved is a penny earned.
print('A {p} saved is a {p} earned.'.format(p='penny')) # outputs A penny saved is a penny earned.

        ## Formatted String Literals Method (f-strings)
name = "Fred"
print(f"He said his name is {name}.") # outputs He said his name is Fred.
print(f"He said his name is {name!r}") # outputs He said his name is "Fred"

num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num)) # outputs My 10 character, four decimal number is:   23.4568
print(f"My 10 character, four decimal number is:{num:{10}.{6}}") # outputs My 10 character, four decimal number is:   23.4568

#Note that in fstrings, the second number, or "precision", refers to the total number of digits, not just those after the decimal.
#Fstrings do not pad to the right of the decimal, even if precision allows it
#If this is important, you can always use .format() syntax inside of an fstring

num2 = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num2)) # outputs My 10 character, four decimal number is:   23.4500
print(f"My 10 character, four decimal number is:{num2:{10}.{6}}") # outputs My 10 character, four decimal number is:     23.45

print("My 10 character, four decimal number is:{0:10.4f}".format(num2)) # outputs My 10 character, four decimal number is:   23.4500
print(f"My 10 character, four decimal number is:{num2:10.4f}") # outputs My 10 character, four decimal number is:   23.4500
