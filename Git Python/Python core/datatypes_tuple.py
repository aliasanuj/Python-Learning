#datatypes_tuple.py=================
====================================
====================================
#In Python programming, a tuple is similar to a list.
#The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas in a list,
#elements can be changed.

Advantages of Tuple over List:
1. Since, tuples are quite similiar to lists, both of them are used in similar situations as well.
2. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:
3. We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
4. Since tuple are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
5. Tuples that contain immutable elements can be used as key for a dictionary. With list, this is not possible.
6. If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
======================================
Creating a Tuple
1. A tuple is created by placing all the items (elements) inside a parentheses (), separated by comma.The parentheses are
optional but is a good practice to write it.
2. A tuple can have any number of items and they may be of different types (integer, float, list, string etc.).
=======================================
#Creating a tuple with one element is a bit tricky.
#Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is in fact a tuple.
my_tuple = ("hello")
print(type(my_tuple))
my_tuple = ("hello",)  
print(type(my_tuple))
my_tuple = "hello",
print(type(my_tuple))
#<class 'str'>
#<class 'tuple'>
#<class 'tuple'>


#Accessing Elements in a Tuple -->
#There are various ways in which we can access the elements of a tuple.
#1. Indexing :We can use the index operator [] to access an item in a tuple where the index starts from 0.
#So, a tuple having 6 elements will have index from 0 to 5. Trying to access an element other that (6, 7,...) will raise an IndexError.
#The index must be an integer, so we cannot use float or other types. This will result into TypeError.
my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])
#print(my_tuple[6]) --> error
#my_tuple[2.0] -->error
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3])
print(n_tuple[1][1])
#p
#t
#s
#4

#2. Negative Indexing
#Python allows negative indexing for its sequences.
#The index of -1 refers to the last item, -2 to the second last item and so on.

3. Slicing
#We can access a range of items in a tuple by using the slicing operator - colon ":".

my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])
#('r', 'o', 'g')
#('p', 'r')
#('i', 'z')
#('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

#4.Changing a Tuple
#Unlike lists, tuples are immutable.
#This means that elements of a tuple cannot be changed once it has been assigned. But, if the element is
#itself a mutable datatype like list, its nested items can be changed.
#We can also assign a tuple to different values (reassignment).
my_tuple = (4, 2, 3, [6, 5])
#my_tuple[1] = 9 error -->
# Output: (4, 2, 3, [9, 5])
my_tuple[3][0] = 9
print(my_tuple)
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple)
#(4, 2, 3, [9, 5])
#('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

#We can use + operator to combine two tuples. This is also called concatenation.
#We can also repeat the elements in a tuple for a given number of times using the * operator.
#Both + and * operations result into a new tuple.

print((1, 2, 3) + (4, 5, 6))
print(("Repeat",) * 3)
#(1, 2, 3, 4, 5, 6)
#('Repeat', 'Repeat', 'Repeat')

#5.Deleting a Tuple
#As discussed above, we cannot change the elements in a tuple. That also means we cannot delete or remove items from a tuple.
#But deleting a tuple entirely is possible using the keyword del.
my_tuple = ('p','r','o','g','r','a','m','i','z')
#del my_tuple[3] -->error
del my_tuple
print(my_tuple) #--> No tuple exist as error

#Python Tuple Methods -->
#Methods that add items or remove items are not available with tuple. Only the following two methods are available.
#Method		Description
#count(x)		Return the number of items that is equal to x
#index(x)		Return index of first item that is equal to x

my_tuple = ('a','p','p','l','e',)
print(my_tuple.count('p'))
print(my_tuple.index('l'))
#2
#3

#Tuple Membership Test
#We can test if an item exists in a tuple or not, using the keyword in.
my_tuple = ('a','p','p','l','e',)
print('a' in my_tuple)
print('b' in my_tuple)
print('g' not in my_tuple)
#True
#False
#True

#Iterating Through a Tuple
#Using a for loop we can iterate though each item in a tuple.
for name in ('John','Kate'):
     print("Hello",name) 
#Hello John
#Hello Kate

#Built-in Functions with Tuple
#Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), tuple() etc. are commonly used with tuple to perform different tasks.
Function		Description
all()		Return True if all elements of the tuple are true (or if the tuple is empty).
any()		Return True if any element of the tuple is true. If the tuple is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
len()		Return the length (the number of items) in the tuple.
max()		Return the largest item in the tuple.
min()		Return the smallest item in the tuple
sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
sum()		Retrun the sum of all elements in the tuple.
tuple()	Convert an iterable (list, string, set, dictionary) to a tuple.
====================================================
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')
============================================
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#banana
============================================
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)
#You cannot change values in a tuple:
===========================================
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#apple
#banana
#cherry
============================================
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#Yes, 'apple' is in the fruits tuple
=============================================
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#3
=============================================
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)
#error You cannot add items to a tuple:
================================================
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
#NameError: name 'thistuple' is not defined
#The del keyword can delete the tuple completely:
===================================================
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#('apple', 'banana', 'cherry')
===================================================
Method	Description
===================================================
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
===================================================
empty_tuple = () 
print (empty_tuple) 
#()
====================================================
tup = 'python', 'geeks'
print(tup) 
tup = ('python', 'geeks') 
print(tup) 
#('python', 'geeks')
#('python', 'geeks')
====================================================
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
print(tuple1 + tuple2) 
#(0, 1, 2, 3, 'python', 'geek')
====================================================
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
tuple3 = (tuple1, tuple2) 
print(tuple3)
#((0, 1, 2, 3), ('python', 'geek'))
==================================================
tuple3 = ('python',)*3
print(tuple3)
#('python', 'python', 'python')
=================================================
tuple1 = (0, 1, 2, 3) 
tuple1[0] = 4
print(tuple1)
#TypeError: 'tuple' object does not support item assignment
================================================
tuple1 = (0 ,1, 2, 3) 
print(tuple1[1:]) 
print(tuple1[::-1]) 
print(tuple1[2:4]) 
#(1, 2, 3)
#(3, 2, 1, 0)
#(2, 3)
==============================================
tuple3 = ( 0, 1) 
del tuple3 
print(tuple3)
#error
==================================================
tuple2 = ('python', 'geek') 
print(len(tuple2))
#2
=============================================
list1 = [0, 1, 2] 
print(tuple(list1)) 
print(tuple('python')) # string 'python'
#(0, 1, 2)
#('p', 'y', 't', 'h', 'o', 'n')
================================================
tup = ('geek',) 
n = 5  #Number of time loop runs 
for i in range(int(n)): 
    tup = (tup,) 
    print(tup
#(('geek',),)
#((('geek',),),)
#(((('geek',),),),)
#((((('geek',),),),),)
#(((((('geek',),),),),),)
==============================================
my_tuple = ()
print(my_tuple)
my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
#()
#(1, 2, 3)
#(1, 'Hello', 3.4)
#('mouse', [8, 4, 6], (1, 2, 3))
============================================
my_tuple = 3, 4.6, "dog"
print(my_tuple)
a, b, c = my_tuple
print(a)
print(b)
print(c)
#(3, 4.6, 'dog')
#3
#4.6
#dog
==============================================
my_tuple = ("hello")
print(type(my_tuple))
my_tuple = ("hello",)  
print(type(my_tuple))
my_tuple = "hello",
print(type(my_tuple))
#<class 'str'>
#<class 'tuple'>
#<class 'tuple'>
==================================================
my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3])
print(n_tuple[1][1])
#p
#t
#s
#4
==============================================
my_tuple = ('p','e','r','m','i','t')
print(my_tuple[-1])
print(my_tuple[-6])
#t
#p
==============================================
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])
#('r', 'o', 'g')
#('p', 'r')
#('i', 'z')
#('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
================================================
my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9
print(my_tuple)
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple)
#(4, 2, 3, [9, 5])
#('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
=========================================================
print((1, 2, 3) + (4, 5, 6))
print(("Repeat",) * 3)
#(1, 2, 3, 4, 5, 6)
#('Repeat', 'Repeat', 'Repeat')
=========================================================
my_tuple = ('p','r','o','g','r','a','m','i','z')
del my_tuple
print(my_tuple)
#NameError: name 'my_tuple' is not defined
======================================================
Method	Description
======================================================
count(x)	Return the number of items that is equal to x
index(x)	Return index of first item that is equal to x
=====================================================
my_tuple = ('a','p','p','l','e',)
print(my_tuple.count('p'))
print(my_tuple.index('l'))
#2
#3
=====================================================
my_tuple = ('a','p','p','l','e',)
print('a' in my_tuple)
print('b' in my_tuple)
print('g' not in my_tuple)
#True
#False
#True
=====================================================
for name in ('John','Kate'):
     print("Hello",name)
#Hello John
#Hello Kate
====================================
