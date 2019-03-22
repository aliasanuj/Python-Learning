#datatypes_dict.py
================================
1. Python dictionary is an unordered collection of items. While other compound data types have only value as an element,
a dictionary has a key: value pair.
2. Dictionaries are optimized to retrieve values when the key is known.
3. While values can be of any data type and can repeat, keys must be of immutable type (string, number or tuple with is immutable 
elements) and must be unique.
4. While indexing is used with other container types to access values, dictionary uses keys. Key can be used either inside square 
brackets or with the get() method.
5. The difference while using get() is that it returns None instead of KeyError, if the key is not found.
6. Dictionary are mutable. We can add new items or change the value of existing items using assignment operator.
7. If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.
8. We can remove a particular item in a dictionary by using the method pop(). This method removes as item with the provided key and 
returns the value.
9. The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. All the items 
can be removed at once using the clear() method.
10. We can also use the del keyword to remove individual items or the entire dictionary itself.
==========================================
Method	Description
==========================================
clear()	Removes all the elements from the dictionary
copy()		Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()		Returns the value of the specified key
items()	Returns a list containing the a tuple for each key value pair
keys()		Returns a list contianing the dictionary's keys
pop()		Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
===================================================
Function	Description
=======================================================
all()		Return True if all keys of the dictionary are true (or if the dictionary is empty).
any()		Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()		Return the length (the number of items) in the dictionary.
cmp()		Compares items of two dictionaries.
sorted()	Return a new sorted list of keys in the dictionary.
===========================================================
Method	Description	Syntax
===========================================================
copy()		dict.copy()		Copy the entire dictionary to new dictionary			
update()	Dict.update()		Update a dictionary by adding a new entry or a key-value pair to an existing entry or by 
					deleting an existing entry.
items()		dictionary.items()	Returns a list of tuple pairs (Keys, Value) in the dictionary.
sort()		sort()			You can sort the elements	dictionary.			
len()		len(dict)		Gives the number of pairs in the dictionary.			
cmp()		cmp(dict1, dict2) 	Compare values and keys of two dictionaries			
Str()		Str(dict)		Make a dictionary into a printable string format		
=============================================================
Sr.No.	Methods with Description
=============================================================
1	dict.clear()
	Removes all elements of dictionary dict
2	dict.copy()
	Returns a shallow copy of dictionary dict
3	dict.fromkeys()
	Create a new dictionary with keys from seq and values set to value.
4	dict.get(key, default=None)
	For key key, returns value or default if key not in dictionary
5	dict.has_key(key)
	Returns true if key in dictionary dict, false otherwise
6	dict.items()
	Returns a list of dict's (key, value) tuple pairs
7	dict.keys()
	Returns list of dictionary dict's keys
8	dict.setdefault(key, default=None)
	Similar to get(), but will set dict[key]=default if key is not already in dict
9	dict.update(dict2)
	Adds dictionary dict2's key-values pairs to dict
10	dict.values()
	Returns list of dictionary dict's values
==============================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
========================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#Mustang
========================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#Mustang
#Mustang
=================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
x = thisdict.get("anuj","not found")
print(x)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
#Mustang
#not found
============================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
for x in thisdict:
  print(x)
#brand
#model
#year
==============================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
for x in thisdict:
  print(thisdict[x])
#Ford
#Mustang
#2018
=======================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
#Ford
#Mustang
#1964
========================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
#brand Ford
#model Mustang
#year 1964
========================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Yes, 'model' is one of the keys in the thisdict dictionary
======================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
#3
=======================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
=======================================================
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items())
print(sorted_x)
#[(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]
==================================
import operator
x = {'a': "anuj", 't': "gfwe", 'e': "bfhjsd", 'd': "cbfhdcbf", 'q': "jhcfj"}
sorted_x = sorted(x.items())
print(sorted_x)
#[('a', 'anuj'), ('d', 'cbfhdcbf'), ('e', 'bfhjsd'), ('q', 'jhcfj'), ('t', 'gfwe')]
===================================
import operator
x = {1: "anuj", 't': "gfwe", 'e': "bfhjsd", 3: "cbfhdcbf", 'q': "jhcfj"}
sorted_x = sorted(x.items())
print(sorted_x)
#TypeError: '<' not supported between instances of 'str' and 'int'
====================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#{'brand': 'Ford', 'year': 1964}
==========================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#{'brand': 'Ford', 'year': 1964}
=======================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop()
print(thisdict)
#    thisdict.pop()
#TypeError: pop expected at least 1 arguments, got 0
=======================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang'}
====================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#{'brand': 'Ford', 'year': 1964}
=====================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists
#NameError: name 'thisdict' is not defined
=====================================================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#{}
=========================================
thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
==================================================================
creating a dict
my_dict = {}
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
# using dict()
my_dict = dict({1:'apple', 2:'ball'})
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
===================================================================
my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))
print(my_dict.get("anuj"))
#Jack
#26
#None
==============================================
my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))
# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']
#Jack
#26
=================================================================
my_dict = {'name':'Jack', 'age': 26}
# update value
my_dict['age'] = 27
#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)
# add item
my_dict['address'] = 'Downtown'  
# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)
#{'name': 'Jack', 'age': 27}
#{'name': 'Jack', 'age': 27, 'address': 'Downtown'}
===================================================================
marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)
for item in marks.items():
    print(item)
print(list(sorted(marks.keys())))
#{'Math': 0, 'English': 0, 'Science': 0}
#('Math', 0)
#('English', 0)
#('Science', 0)
#['English', 'Math', 'Science']
==================================================
marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)
for item in marks.items():
    print(item)
print(list(sorted(marks.values())))
print(list(sorted(marks.keys())))
#{'Math': 0, 'English': 0, 'Science': 0}
#('Math', 0)
#('English', 0)
#('Science', 0)
#[0, 0, 0]
#['English', 'Math', 'Science']
===================================================================
squares = {x: x*x for x in range(6)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
============================================================
squares = {}
for x in range(6):
   squares[x] = x*x
print(squares)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
================================================
odd_squares = {x: x*x for x in range(11) if x%2 == 1}
# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(odd_squares)
#{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
=================================================
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(1 in squares)
# Output: True
print(2 not in squares)
# membership tests for key only not value
# Output: False
print(49 in squares)
#True
#True
#False
====================================================
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
for i in squares:
    print(i)  
#1
#9
#25
#49
#81
#1
#3
#5
#7
#9
=======================================================
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: 5
print(len(squares))
# Output: [1, 3, 5, 7, 9]
print(sorted(squares))
#[1, 3, 5, 7, 9]
=======================================================
Dict = {} 
print("Empty Dictionary: ")
print(Dict) 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 
Dict = {1: {'A' : 'Geeks', 'B' : 'For', 'C' : 'Geeks'}, 
        2: {'D' : 'Welcome', 'E' : 'To', 'F' : 'Geeks'}} 
print("\nNested Dictionary: ") 
print(Dict) 
#Empty Dictionary: 
#{}
#Dictionary with the use of Integer Keys: 
#{1: 'Geeks', 2: 'For', 3: 'Geeks'}
#Dictionary with the use of Mixed Keys: 
#{'Name': 'Geeks', 1: [1, 2, 3, 4]}
#Dictionary with the use of dict(): 
#{1: 'Geeks', 2: 'For', 3: 'Geeks'}
#Dictionary with each item as a pair: 
#{1: 'Geeks', 2: 'For'}
#Nested Dictionary: 
#{1: {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}, 2: {'D': 'Welcome', 'E': 'To', 'F': 'Geeks'}}
=======================================================
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict)
#Empty Dictionary: 
#{}
#Dictionary after adding 3 elements: 
#{0: 'Geeks', 2: 'For', 3: 1}
#Dictionary after adding 3 elements: 
#{0: 'Geeks', 2: 'For', 3: 1, 'Value_set': (2, 3, 4)}
#Updated key value: 
#{0: 'Geeks', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4)}
#Adding a Nested Key: 
#{0: 'Geeks', 2: 'Welcome', 3: 1, 'Value_set': (2, 3, 4), 5: {'Nested': {'1': 'Life', '2': 'Geeks'}}}
==========================================================
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 
Dict.popitem() 
print("\nPops first element: ") 
print(Dict) 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict)
#Initial Dictionary: 
#{5: 'Welcome', 6: 'To', 7: 'Geeks', 'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'}, 'B': {1: 'Geeks', 2: 'Life'}}
#Deleting a specific key: 
#{5: 'Welcome', 7: 'Geeks', 'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'}, 'B': {1: 'Geeks', 2: 'Life'}}
#Deleting a key from Nested Dictionary: 
#{5: 'Welcome', 7: 'Geeks', 'A': {1: 'Geeks', 3: 'Geeks'}, 'B': {1: 'Geeks', 2: 'Life'}}
#Popping specific element: 
#{7: 'Geeks', 'A': {1: 'Geeks', 3: 'Geeks'}, 'B': {1: 'Geeks', 2: 'Life'}}
#Pops first element: 
#{7: 'Geeks', 'A': {1: 'Geeks', 3: 'Geeks'}}
#Deleting Entire Dictionary: 
#{}
====================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)
#{'Tim': 18, 'Charlie': 12, 'Robert': 25}
#{'Tiffany': 22}
==================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Dict.update({"Sarah":9})
print(Dict)
#{'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25, 'Sarah': 9}
===========================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Dict.update({"Tim":9})
print(Dict)
#{'Tim': 9, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
del Dict ['Charlie']
print(Dict)
#{'Tim': 18, 'Tiffany': 22, 'Robert': 25}
======================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))
#Students Name: [('Tim', 18), ('Charlie', 12), ('Tiffany', 22), ('Robert', 25)]
=======================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print(Dict.items())
print(list(Dict.items()))
#dict_items([('Tim', 18), ('Charlie', 12), ('Tiffany', 22), ('Robert', 25)])
#[('Tim', 18), ('Charlie', 12), ('Tiffany', 22), ('Robert', 25)]
======================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:       
        print(False)
#True
#True
#False
#True
===============================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
print(Students)
Students1 = list(Dict.values())
print(Students1)
a = sorted(Dict.items())
print(a)
#['Tim', 'Charlie', 'Tiffany', 'Robert']
#[18, 12, 22, 25]
#[('Charlie', 12), ('Robert', 25), ('Tiffany', 22), ('Tim', 18)]
==========================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))
#Charlie:12
#Robert:25
#Tiffany:22
#Tim:18
============================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Length : %d" % len (Dict))
#Length : 4
===========================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("variable Type: %s" %type (Dict))
#variable Type: <class 'dict'> #we cant give here as %d as it is not integer value
===========================================================
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("printable string:%s" % str (Dict))
#printable string:{'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
==============================================================
string1 = "anuj anuj anuj kumar"
dict1 = {}
for i in string1:
  if i in dict1:
    dict1[i] = dict1[i] + 1
  else:
    dict1[i] = 1
print(dict1)
#{'a': 4, 'n': 3, 'u': 4, 'j': 3, ' ': 3, 'k': 1, 'm': 1, 'r': 1}
===============================================================
string1 = "anuj anuj anuj kumar"
dict1 = {}
for i in string1:
  if i in dict1:
    dict1[i] = dict1[i] + 1
  else:
    dict1[i] = 1
for i,j in dict1.items():
  print(i, "=" ,j)
#a = 4
#n = 3
#u = 4
#j = 3
#  = 3
#k = 1
#m = 1
#r = 1
========================================
string1 = "anuj anuj anuj kumar"
string2 = string1.split()
dict1 = {}
for i in string2:
  if i in dict1:
    dict1[i] = dict1[i] + 1
  else:
    dict1[i] = 1
for i,j in dict1.items():
  print(i, "=" ,j)
#anuj = 3
#kumar = 1
===========================================
from collections import  Counter
a = "anuj kumar anuj kumar anuj"
s = a.split()
print(s)
c = dict(Counter(s))
print(c)

#['anuj', 'kumar', 'anuj', 'kumar', 'anuj']
#{'anuj': 3, 'kumar': 2}
===========================================
a = "anuj kumar anuj kumar anuj"
s = a.split()
d = {}
for i in s:
    if i in d:
        d [i] = d[i] + 1
    else :
        d[i] = 1
print(d)
#{'anuj': 3, 'kumar': 2}
===========================================
string1 = "kumar anuj anuj anuj"
string2 = string1.split()
dict1 = {}
for i in string2:
  if i in dict1:
    dict1[i] = dict1[i] + 1
  else:
    dict1[i] = 1
for i,j in sorted(dict1.items()):
  print(i, "=" ,j)
#anuj = 3
#kumar = 1
======================================
string1 = "kumar anuj anuj anuj"
string2 = string1.split()
dict1 = {}
for i in string2:
  if i in dict1:
    dict1[i] = dict1[i] + 1
  else:
    dict1[i] = 1
for a in dict1.items():
  print(list(a))
#['kumar', 1]
#['anuj', 3]
========================================
my_dict = {'name':'Jack', 'age': 26}
# Output: Jack
print(my_dict['name'])
# Output: 26
print(my_dict.get('age'))
# Trying to access keys which doesn't exist throws error
print(my_dict.get('address'))
#Jack
#26
#None
===================================
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
squares.clear()
print(squares)
del squares
print(squares) #error --> NameError: name 'squares' is not defined
#16
#{1: 1, 2: 4, 3: 9, 5: 25}
#(5, 25)
#{1: 1, 2: 4, 3: 9}
#{}
================================
marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)
for item in marks.items():
    print(item)
for item in marks.keys():
    print(item)
print(list(sorted(marks.keys())))
#{'Math': 0, 'English': 0, 'Science': 0}
#('Math', 0)
#('English', 0)
#('Science', 0)
#Math
#English
#Science
#['English', 'Math', 'Science']
===================================
squares = {x: x*x for x in range(6)}
print(squares)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
============================
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(len(squares))
print(sorted(squares))
#5
#[1, 3, 5, 7, 9]
===========================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)
#Ford
#Mustang
#1964
#brand
#model
#year
========================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "Ford" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#No OutPut
========================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("brand") #for specified key
print(x)
#ford
======================
my_dict = {'name':'Jack', 'age': 26}
# Output: Jack
print(my_dict['name'])
# Output: 26
print(my_dict.get('age'))
# Trying to access keys which doesn't exist throws error
print(my_dict.get('name',"not found"))
#Jack
#26
#Jack
=========================
squares = {1: 1, 11: 9, 5: 25, 7: 49, 9: 81}
print(sorted(squares))
#[1, 5, 7, 9, 11]
========================
