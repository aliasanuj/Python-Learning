#datatypes_tuple.py
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
=====================================================
Function	Description
=====================================================
all()		Return True if all elements of the tuple are true (or if the tuple is empty).
any()		Return True if any element of the tuple is true. If the tuple is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
len()		Return the length (the number of items) in the tuple.
max()		Return the largest item in the tuple.
min()		Return the smallest item in the tuple
sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
sum()		Retrun the sum of all elements in the tuple.
tuple()		Convert an iterable (list, string, set, dictionary) to a tuple.
========================================================

