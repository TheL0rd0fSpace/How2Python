#dictionaries are mappings of objects stored with an associated key, rather than an index
#dictionaries are not ordered objects, they can't be indexed

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key2'])

#dictionaries are flexible in the data types they can hold
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'])
#can call a value, then the index of that value
print(my_dict['key3'][0])
#can also call methods of that value
print(my_dict['key3'][0].upper())
print(my_dict['key1'])

#can also reassign values, provided you know the key
print(my_dict['key1'])
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])
my_dict['key1'] -= 123
print(my_dict['key1'])

#create new empty dictionary
d = {}
#create new key-value combo by assignment
d['animal'] = "Dog"
print(d)
d['answer'] = 42
print(d)
d['animal'] = "Cat"
print(d)
#this assigns the key to have a new value. if the key being assigned doesnt exist, it creates that key and assigns the value to it

#Nested Dictionaries
d2 = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d2['key1']['nestkey']['subnestkey'])

#Dictionary Methods
d3 = {'key1':1,'key2':2,'key3':3}
d3.keys()
d3.values()
d3.items()
