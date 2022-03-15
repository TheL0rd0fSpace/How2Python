#Lists can contain any quantity and type of objects
myList = [1,2,3]
aWord = 'apples'
myList = ['A string', 23,100.232,'o',aWord]
print(len(myList)) # prints the number of objects in myList

secondList = ['one','two','three',4,5]
print(secondList[0]) # prints the object at index 0
print(secondList[1:]) # prints index 1 and everything after it
print(secondList[:3]) # prints everything up to, but not including, index 3

#we can also use + to concatenate lists, like strings
print(secondList + ['new item'])
print(secondList + ['new item','other item'])
#this doesn't actually change the list!
print(secondList)
#use an assignment statement to permanently change the list
secondList += ['new item','other item']
print(secondList)
print(secondList * 2) # prints the list twice as one big list

##List Methods
#make a new list
methodList=[1,2,3]
#appending adds a new item to the end of the list
methodList.append('appendme!')
print(methodList)
#popping removes an item from the list. the default poition is index -1, or the last item
methodList.pop()
print(methodList)
methodList.append('appendme!')
#you can even assign the popped item to a variable
popped_item = methodList.pop()
print(popped_item)
#make a new list
letterList=['a','e','x','b','c']
print(letterList)
letterList.reverse() #reverses the objects in the list
print(letterList)
letterList.sort() #arranges the objects in the list alphabetically/numerically
print(letterList)
#insert into a list
var = 3
letterList.insert(var+1,'t')
print(letterList)

#Nesting Lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix = [lst_1,lst_2,lst_3]
print(matrix[0]) # prints first item in matrix variable, the entirety of lst_1
print(matrix[0][0]) # prints first item inside first item in matrix variable, which is the first object of lst_1

#List Comprehension
#Python allows you to quickly construct a list using a for loop
first_col = [row[0] for row in matrix] # for each object in matrix, it grabs that object's index 0
print(first_col)
