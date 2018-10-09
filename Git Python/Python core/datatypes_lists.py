#datatypes_lists.py
=======================
thislist = ["apple", "banana", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry']
========================================
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#banana
=========================================
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#['apple', 'blackcurrant', 'cherry']
=========================================
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#apple
#banana
#cherry
=========================================
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Yes, 'apple' is in the fruits list
==========================================
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#3
===========================================
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']
============================================
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#['apple', 'orange', 'banana', 'cherry']
============================================
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry']
===========================================
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#['apple', 'banana']
===========================================
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']
===========================================
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because "thislist" no longer exists.
#NameError: name 'thislist' is not defined
============================================
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#[]
============================================
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#['apple', 'banana', 'cherry']
============================================
Method	Description
append()	Adds an element at the end of the list
clear()		Removes all the elements from the list
copy()		Returns a copy of the list
count()		Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()		Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()		Sorts the list
==================================================
Function	Description
==================================================
all()		Return True if all elements of the list are true (or if the list is empty).
any()		Return True if any element of the list is true. If the list is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()		Return the length (the number of items) in the list.
list()		Convert an iterable (tuple, string, set, dictionary) to a list.
max()		Return the largest item in the list.
min()		Return the smallest item in the list
sorted()	Return a new sorted list (does not sort the list itself).
sum()		Return the sum of all elements in the list.
 
# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed datatypes
my_list = [1, "Hello", 3.4]
===================================================
my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])
# Output: o
print(my_list[2])
# Output: e
print(my_list[4])
# Error! Only integer can be used for indexing
# my_list[4.0]
# Nested List
n_list = ["Happy", [2,0,1,5]]
# Nested indexing
# Output: a
print(n_list[0][1])    
# Output: 5
print(n_list[1][3])
#p
#o
#e
#a
#5
=====================================================
my_list = ['p','r','o','b','e']
# Output: e
print(my_list[-1])
# Output: p
print(my_list[-5])
#e
#p
=====================================================
my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])
#['o', 'g', 'r']
#['p', 'r', 'o', 'g']
#['a', 'm', 'i', 'z']
#['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
======================================================
# mistake values
odd = [2, 4, 6, 8]
# change the 1st item    
odd[0] = 1            
# Output: [1, 4, 6, 8]
print(odd)
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  
# Output: [1, 3, 5, 7]
print(odd) 
#[1, 4, 6, 8]
#[1, 3, 5, 7]
=======================================================
odd = [1, 3, 5]
odd.append(7)
# Output: [1, 3, 5, 7]
print(odd)
odd.extend([9, 11, 13])
# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)
#[1, 3, 5, 7]
#[1, 3, 5, 7, 9, 11, 13]
========================================================
odd = [1, 3, 5]
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
#Output: ["re", "re", "re"]
print(["re"] * 3)
#[1, 3, 5, 9, 7, 5]
#['re', 're', 're']
=======================================================
odd = [1, 9]
odd.insert(1,3)
# Output: [1, 3, 9] 
print(odd)
odd[2:2] = [5, 7]
# Output: [1, 3, 5, 7, 9]
print(odd)
#[1, 3, 9]
#[1, 3, 5, 7, 9]
========================================================
my_list = ['p','r','o','b','l','e','m']
# delete one item
del my_list[2]
# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)
# delete multiple items
del my_list[1:5]  
# Output: ['p', 'm']
print(my_list)
# delete entire list
del my_list       
# Error: List not defined
print(my_list)
#['p', 'r', 'b', 'l', 'e', 'm']
#['p', 'm']
#Traceback (most recent call last):
#  File "python", line 13, in <module>
#NameError: name 'my_list' is not defined
=========================================================
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'o'
print(my_list.pop(1))
# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'm'
print(my_list.pop())
# Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()
# Output: []
print(my_list)
#['r', 'o', 'b', 'l', 'e', 'm']
#o
#['r', 'b', 'l', 'e', 'm']
#m
#['r', 'b', 'l', 'e']
#[]
==============================================================
my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = []
print(my_list)
my_list[2:5] = []
print(my_list)
#['p', 'r', 'b', 'l', 'e', 'm']
#['p', 'r', 'm']
================================================================
my_list = [3, 8, 1, 6, 0, 8, 4]
# Output: 1
print(my_list.index(8))
# Output: 2
print(my_list.count(8))
my_list.sort()
# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)
my_list.reverse()
# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)
#1
#2
#[0, 1, 3, 4, 6, 8, 8]
#[8, 8, 6, 4, 3, 1, 0]
==============================================================
pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)
#[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
==============================================================
pow2 = []
for x in range(10):
   pow2.append(2 ** x)
print(pow2)
#[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
==============================================================
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)
#[64, 128, 256, 512]
==================================================
odd = [x for x in range(20) if x % 2 == 1]
print(odd)
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
==================================================
print([x+y for x in ['Python ','C '] for y in ['Language','Programming']])
#['Python Language', 'Python Programming', 'C Language', 'C Programming']
==================================================
my_list = ['p','r','o','b','l','e','m']
# Output: True
print('p' in my_list)
# Output: False
print('a' in my_list)
# Output: True
print('c' not in my_list)
#True
#False
#True
=========================================================
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
#I like apple
#I like banana
#I like mango
==========================================================
List = [] 
print("Intial blank List: ") 
print(List) 
# Creating a List with  
# the use of a String 
List = ['GeeksForGeeks'] 
print("\nList with the use of String: ") 
print(List) 
# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 
print("\nList containing multiple values: ") 
print(List[0])  
print(List[2]) 
# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List = [['Geeks', 'For'] , ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List) 
# Creating a List with  
# the use of Numbers 
# (Having duplicate values) 
List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ") 
print(List) 
# Creating a List with  
# mixed type of values 
# (Having numbers and strings) 
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 
print("\nList with the use of Mixed Values: ") 
print(List) 
#Intial blank List: 
#[]

#List with the use of String: 
#['GeeksForGeeks']

#List containing multiple values: 
#Geeks
#Geeks

#Multi-Dimensional List: 
#[['Geeks', 'For'], ['Geeks']]

#List with the use of Numbers: 
#[1, 2, 4, 4, 3, 3, 3, 6, 5]

#List with the use of Mixed Values: 
#[1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
==============================================
List = [] 
print("Intial blank List: ") 
print(List) 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 
for i in range(1, 4): 
    List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 
List2 = ['For', 'Geeks'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 
List.insert(3, 12) 
List2.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 
List.extend([8, 'Geeks', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List) 
#Intial blank List: 
#[]

#List after Addition of Three elements: 
#[1, 2, 4]

#List after Addition of elements from 1-3: 
#[1, 2, 4, 1, 2, 3]

#List after Addition of a Tuple: 
#[1, 2, 4, 1, 2, 3, (5, 6)]

#List after Addition of a List: 
#[1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks']]

#List after performing Insert Operation: 
#[1, 2, 4, 12, 1, 2, 3, (5, 6), ['Geeks', 'For', 'Geeks']]

#List after performing Extend Operation: 
#[1, 2, 4, 12, 1, 2, 3, (5, 6), ['Geeks', 'For', 'Geeks'], 8, 'Geeks', 'Always']
==================================================
List = [1, 2, 3, 4, 5, 6,  
        7, 8, 9, 10, 11, 12] 
print("Intial List: ") 
print(List) 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 
for i in range(1, 5): 
    List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 
List.pop() 
print("\nList after popping an element: ") 
print(List) 
List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 
#Intial List: 
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#List after Removal of two elements: 
#[1, 2, 3, 4, 7, 8, 9, 10, 11, 12]

#List after Removing a range of elements: 
#[7, 8, 9, 10, 11, 12]

#List after popping an element: 
#[7, 8, 9, 10, 11]

#List after popping a specific element: 
#[7, 8, 10, 11]
============================================================
List = ['G','E','E','K','S','F', 
        'O','R','G','E','E','K','S'] 
print("Intial List: ") 
print(List) 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
      "element till the end: ") 
print(Sliced_List) 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List) 
#Intial List: 
#['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

#Slicing elements in a range 3-8: 
#['K', 'S', 'F', 'O', 'R']

#Elements sliced till 6th element from last: 
#['G', 'E', 'E', 'K', 'S', 'F', 'O']

#Elements sliced from 5th element till the end: 
#['F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

#Printing all elements using slice operation: 
#['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

#Printing List in reverse: 
#['S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G']
=====================================================

