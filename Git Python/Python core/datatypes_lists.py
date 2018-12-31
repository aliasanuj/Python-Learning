#datatypes_lists.py

#List -->Python offers a range of compound datatypes often referred to as sequences. 
#List is one of the most frequently used and very versatile datatype used in Python.
#How to create a list? -->
#In Python programming, a list is created by placing all the items (elements) inside a square bracket [ ], separated by commas.
#It can have any number of items and they may be of different types (integer, float, string etc.).
# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed datatypes
my_list = [1, "Hello", 3.4]
#Also, a list can even have another list as an item. This is called nested list.
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
==================================================
#How to access elements from a list -->
#There are various ways in which we can access the elements of a list.

#List Index :
#We can use the index operator [] to access an item in a list.
#Index starts from 0. So, a list having 5 elements will have index from 0 to 4.
#Trying to access an element other that this will raise an IndexError.
#The index must be an integer. We can't use float or other types, this will result into TypeError.
#Nested list are accessed using nested indexing.
====================================================
my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[4])
n_list = ["Happy", [2,0,1,5]]
print(n_list[0][1])
print(n_list[1][3])
#p
#o
#e
#a
#5
=============================================
#Negative indexing -->
#Python allows negative indexing for its sequences.
#The index of -1 refers to the last item, -2 to the second last item and so on.
my_list = ['p','r','o','b','e']
print(my_list[-1])
print(my_list[-5])
#e
#p
============================================
#How to slice lists in Python -->
#We can access a range of items in a list by using the slicing operator (colon).
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:5])
print(my_list[:-5])
print(my_list[5:])
print(my_list[:])
#['o', 'g', 'r']
#['p', 'r', 'o', 'g']
#['a', 'm', 'i', 'z']
#['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
=========================================
#How to change or add elements to a list -->
#List are mutable, meaning, their elements can be changed unlike string or tuple.
#We can use assignment operator (=) to change an item or a range of items.
# mistake values
odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)
odd[1:4] = [3, 5, 7]
print(odd)
#[1, 4, 6, 8]
#[1, 3, 5, 7]
=======================================               
#We can add one item to a list using append() method or add several items using extend() method.
odd = [1, 3, 5]
odd.append(7)
print(odd)
odd.extend([9, 11, 13])
print(odd)
#[1, 3, 5, 7]
#[1, 3, 5, 7, 9, 11, 13]
====================================
#We can also use + operator to combine two lists. This is also called concatenation.
#The * operator repeats a list for the given number of times.
odd = [1, 3, 5]
print(odd + [9, 7, 5])
print(["re"] * 3)
#[1, 3, 5, 9, 7, 5]
#['re', 're', 're']
==================================
#Furthermore, we can insert one item at a desired location by using the method insert() or 
#insert multiple items by squeezing it into an empty slice of a list.
odd = [1, 9]
odd.insert(1,3)
print(odd)
odd[2:2] = [5, 7]
print(odd)
#[1, 3, 9]
#[1, 3, 5, 7, 9]
=================================
odd = [1, 9]
odd.insert(1,5)
print(odd)
odd[2:2] = [5, 7]
print(odd)
#[1, 5, 9]
#[1, 5, 5, 7, 9]
================================
#How to delete or remove elements from a list ->
#We can delete one or more items from a list using the keyword del.
#It can even delete the list entirely.
my_list = ['p','r','o','b','l','e','m']
del my_list[2]
print(my_list)
del my_list[1:5]
print(my_list)
del my_list
print(my_list)
#['p', 'r', 'b', 'l', 'e', 'm']
#['p', 'm']
#error
=============================
#We can use remove() method to remove the given item or pop() method to remove an item at the given index.
#The pop() method removes and returns the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure).
#We can also use the clear() method to empty a list.
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list)
print(my_list.pop(1))
print(my_list)
print(my_list.pop())
print(my_list)
my_list.clear()
print(my_list)
#['r', 'o', 'b', 'l', 'e', 'm']
#o
#['r', 'b', 'l', 'e', 'm']
#m
#['r', 'b', 'l', 'e']
#[]
==========================
my_list = ['p','r','o','b','l','e','m']
my_list.remove(1)
#error ValueError: list.remove(x): x not in list
=======================
my_list = ['p','r','o','b','l','e','m']
my_list.remove('r')
print(my_list)
#['p', 'o', 'b', 'l', 'e', 'm']
========================
#Finally, we can also delete items in a list by assigning an empty list to a slice of elements.
my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = []
print(my_list)
my_list[2:5] = []
print(my_list)
#['p', 'r', 'b', 'l', 'e', 'm']
#['p', 'r', 'm']
=========================
list1 = ['p','r','o','b','l','e','m']
list1.pop()
print(list1)
list1.pop(2)
print(list1)
#['p', 'r', 'o', 'b', 'l', 'e']
#['p', 'r', 'b', 'l', 'e']
============================================
#Python List Methods -->
#Methods that are available with list object in Python programming are tabulated below.
#They are accessed as list.method(). Some of the methods have already been used above.
============================================
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()		Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position #pop(index no)
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
=============================================
list1 = [1,2,3,4,5,6]
list2 = ["anuj","kumar","aman","anshu"]
list1.append(2) #only one argument
print(list1)
list2.append(10) #string or int, it will take all
print(list2)
#[1, 2, 3, 4, 5, 6, 2]
#['anuj', 'kumar', 'aman', 'anshu', 10]
================================
a1 = {1:"abc", 2:"boy", 3:"cat"}
print(list(a1))
#[1, 2, 3]
=============================
list1 = [1,2,3,4,5,6]
list2 = ["anuj","kumar","aman","anshu"]
list1.clear()
print(list1)
#[]
=======================
list1 = [1,2,3,4,5,6]
list2 = ["anuj","kumar","aman","anshu"]
x = list1.copy()
print(x)
#[1, 2, 3, 4, 5, 6]
=======================
list1 = [1,2,3,4,5,6]
list2 = ["anuj","kumar","aman","anshu"]
x = list1.copy()
print(x)
print(list1)
#[1, 2, 3, 4, 5, 6]
#[1, 2, 3, 4, 5, 6]
========================
list1 = [1,2,3,4,5,6,6]
list2 = ["anuj","kumar","aman","anshu"]
print(list1.count(6))
#2
===================
list1 = [1,2,3,4,5,6,6]
list2 = ["anuj","kumar","aman","anshu"]
list1.extend(list2)
print(list1)
#[1, 2, 3, 4, 5, 6, 6, 'anuj', 'kumar', 'aman', 'anshu']
======================
list1 = [1,2,3,4,5,6,6]
list2 = ["anuj","kumar","aman","anshu"]
print(list1.index(4))
print(list1.index(6))
print(list1.index(6))
#3
#5
#5
======================
list1 = [1,2,3,4,5,6,6]
list2 = ["anuj","kumar","aman","anshu"]
list1.insert(2,10)
print(list1)
#[1, 2, 10, 3, 4, 5, 6, 6]
==================
list1 = [1,2,3,4,5,6,6]
list2 = ["anuj","kumar","aman","anshu"]
list1.pop(2) #indexNo
print(list1)
#[1, 2, 4, 5, 6, 6]
====================
list1 = [1,2,3,4,5,6,6]
list2 = ["anuj","kumar","aman","anshu"]
list1.remove(2) #elements
print(list1)
#[1, 3, 4, 5, 6, 6]
======================
list1 = [1,2,3,4,5,6,6]
list2 = ["anuj","kumar","aman","anshu"]
list1.reverse()
print(list1)
#[6, 6, 5, 4, 3, 2, 1]
===================
list1 = [1,28,45,4,3,4,5,6,6]
list2 = ["anuj","kumar","aman","anshu"]
list1.sort() 
print(list1)
#[1, 3, 4, 4, 5, 6, 6, 28, 45]
=============================
list1 = [1,28,45,4]
list2 = ["anuj","kumar","aman","anshu"]
x = enumerate(list1)
print(list(x))
y = enumerate(list2,start=10)
print(list(y))
for i in enumerate(list1,start=5):
  print(list(i))
for i in enumerate(list1,start=15):
  print(i)
#[(0, 1), (1, 28), (2, 45), (3, 4)]
#[(10, 'anuj'), (11, 'kumar'), (12, 'aman'), (13, 'anshu')]
#[5, 1]
#[6, 28]
#[7, 45]
#[8, 4]
#(15, 1)
#(16, 28)
#(17, 45)
#(18, 4)
=============================
list1 = [1,4,7,9,5,4,77,55,7]
for i in range(len(list1)-1):
    for i in range(len(list1) -1):
        if list1[i] < list1[i+1]:
            temp = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = temp
print(list1)
list1.reverse()
print(list1)
#[77, 55, 9, 7, 7, 5, 4, 4, 1]
#[1, 4, 4, 5, 7, 7, 9, 55, 77]
=============================================
my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list.index(8))
print(my_list.count(8))
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
#1
#2
#[0, 1, 3, 4, 6, 8, 8]
#[8, 8, 6, 4, 3, 1, 0]
=========================================
#List Comprehension: Elegant way to create new List
#List comprehension is an elegant and concise way to create new list from an existing list in Python.
#List comprehension consists of an expression followed by for statement inside square brackets.
#Here is an example to make a list with each item being increasing power of 2.
=========================================
pow2 = [2 ** x for x in range(10)]
print(pow2)
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
========================================
#List Membership Test -->
#We can test if an item exists in a list or not, using the keyword in.
my_list = ['p','r','o','b','l','e','m']
print('p' in my_list)
print('a' in my_list)
print('c' not in my_list)
#True
#False
#True
=======================================
#Iterating Through a List
#Using a for loop we can iterate though each item in a list.
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
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
=======================================
thislist = list("apple", "banana", "cherry") # note the double round-brackets
print(thislist)
#error
=======================================
# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed datatypes
my_list = [1, "Hello", 3.4]
===================================================
my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[4])
n_list = ["Happy", [2,0,1,5]]
print(n_list[0][1])
print(n_list[1][3])
#p
#o
#e
#a
#5
=====================================================
my_list = ['p','r','o','b','e']
print(my_list[-1])
print(my_list[-5])
#e
#p
=====================================================
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:5])
print(my_list[:-5])
print(my_list[5:])
print(my_list[:])
#['o', 'g', 'r']
#['p', 'r', 'o', 'g']
#['a', 'm', 'i', 'z']
#['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
======================================================
# mistake values
odd = [2, 4, 6, 8]
odd[0] = 1            
print(odd)
odd[1:4] = [3, 5, 7]  
print(odd) 
#[1, 4, 6, 8]
#[1, 3, 5, 7]
=======================================================
odd = [1, 3, 5]
odd.append(7)
print(odd)
odd.extend([9, 11, 13])
print(odd)
#[1, 3, 5, 7]
#[1, 3, 5, 7, 9, 11, 13]
========================================================
odd = [1, 3, 5]
print(odd + [9, 7, 5])
print(["re"] * 3)
#[1, 3, 5, 9, 7, 5]
#['re', 're', 're']
=======================================================
odd = [1, 9]
odd.insert(1,3)
print(odd)
odd[2:2] = [5, 7]
print(odd)
#[1, 3, 9]
#[1, 3, 5, 7, 9]
========================================================
my_list = ['p','r','o','b','l','e','m']
del my_list[2]
print(my_list)
del my_list[1:5]  
print(my_list)
del my_list       
print(my_list)
#['p', 'r', 'b', 'l', 'e', 'm']
#['p', 'm']
#Traceback (most recent call last):
#  File "python", line 13, in <module>
#NameError: name 'my_list' is not defined
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
print(my_list.index(8))
print(my_list.count(8))
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
#1
#2
#[0, 1, 3, 4, 6, 8, 8]
#[8, 8, 6, 4, 3, 1, 0]
==============================================================
pow2 = [2 ** x for x in range(10)]
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
print('p' in my_list)
print('a' in my_list)
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
List = ['GeeksForGeeks'] 
print("\nList with the use of String: ") 
print(List) 
List = ["Geeks", "For", "Geeks"] 
print("\nList containing multiple values: ") 
print(List[0])  
print(List[2]) 
List = [['Geeks', 'For'] , ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List) 
List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ") 
print(List) 
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
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
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
