#The backslash is a special character, called the "escape character"
#Putting a backslash in front of a speical character makes it normal

#The following strings are identical
print('I\'m having a great day today!')
print("I'm having a great day today!")

#This even works on the backslash character itself
print("// is the backslash character")

##Escape Sequences are special sets of characters which insert whitespace in different ways

#\n inserts a new line
print("This uses \n multiple lines.")

#\t inserts a tab
print("\t This line is tabbed.")

#str() returns the string, while interpreting escape sequences
#repr() returns the string without interpreting escape sequences
mySentence = "\t This line is tabbed. \n This line is not tabbed."
print(str(mySentence))
print(repr(mySentence))

#if formatting strings with modulo operators, %s and %r will function differently
