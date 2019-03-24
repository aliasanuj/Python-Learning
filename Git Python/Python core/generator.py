#generator :
==============================
#Generator 
#a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
#If a function contains at least one yield statement (it may contain other yield or return statements), 
#it becomes a generator function. Both yield and return will return some value from a function.
#The difference is that, while a return statement terminates a function entirely, yield 
#statement pauses the function saving all its states and later continues from there on successive calls.
#every generator is an iterator, but not every iterator is a generator
#Generator function contains one or more yield statement.
#When called, it returns an object (iterator) but does not start execution immediately.
#Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
#Once the function yields, the function is paused and the control is transferred to the caller.
#Local variables and their states are remembered between successive calls.
#Finally, when the function terminates, StopIteration is raised automatically on further calls.
#It is also called lazy evaluation
#Generator-Function
#Generator-Object
=============================
def my_gen():
    yield 7
    yield 6
    yield 8
    yield 4
    yield 5
    yield 6
print("by objevt creation")
obj = my_gen()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print("by for loop")
for i in my_gen():
  print(i)
print("x.__next__()")
print(obj.__next__())
print(obj.__next__())
print(obj.__next__()) #error -> StopIteration
#by objevt creation
#7
#6
#8
#4
#by for loop
#7
#6
#8
#4
#5
#6
#x.__next__()
#5
#6
Traceback (most recent call last):
  File "python", line 20, in <module>
StopIteration
=============================
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
a = my_gen()
next(a)
next(a)
next(a)
#This is printed first
#This is printed second
#This is printed at last
=======================
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
for i in my_gen():
    print(i)
#This is printed first
#1
#This is printed second
#2
#This is printed at last
#3
========================
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
#1
#2
#3
=======================
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
# x is a generator object
x = simpleGeneratorFun()
# Iterating over the generator object using next
print(x.__next__());  # In Python 3, __next__()
print(x.__next__());  # In Python 3, __next__()
print(x.__next__());  # In Python 3, __next__()
#1
#2
#3
======================
import random
def lottery():
    for i in range(5):
        yield random.randint(1,15)
    yield random.randint(16,20)
for i in lottery():
    print("number is %d "%(i))
#number is 6 
#number is 12 
#number is 14 
#number is 12 
#number is 6 
#number is 20 
=====================
def abc():
    for i in range(5):
        yield i
for i in abc():
    print(i)
#0
#1
#2
#3
#4
=====================
def generator():
    n = 1
    print("value of n is :",n)
    yield n
    n = n+1
    print("value of n is :", n)
    yield n
a = generator()
print(next(a))
print(next(a))
#value of n is : 1
#1
#value of n is : 2
#2
===========================
def generator():
    n = 1
    print("value of n is :",n)
    yield n
    n = n+1
    print("value of n is :", n)
    yield n
a = generator()
print(next(a))
print(next(a))
print(next(a))
#value of n is : 1
#1
#value of n is : 2
#2
#Traceback (most recent call last):
#    print(next(a))
#StopIteration
============================
def generator():
    n = 1
    print("value of n is :",n)
    yield n
    n = n+1
    print("value of n is :", n)
    yield n
for i in generator():
    print(i)
#value of n is : 1
#1
#value of n is : 2
#2
===========================
def abc():
    for i in range(5):
        yield i
obj = abc()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
#0
#1
#2
#3
#4
============================
def my_gen():
    n = 1
    # Generator function contains yield statements
    yield n
    n += 1
    yield n
    n += 1
    yield n
for i in my_gen():
  print(i)
#1
#2
#3
===========================================
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
# x is a generator object
x = simpleGeneratorFun()
# Iterating over the generator object using next
print(next(x));  # In Python 3, __next__()
print(x.__next__());  # In Python 3, __next__()
print(next(x));  # In Python 3, __next__()
#1
#2
#3
=================================================
def generator():
    n = 1
    print("value of n is :",n)
    yield n
    n = n+1
    print("value of n is :", n)
    yield n
a = generator()
print(next(a))
#value of n is : 1
#1
==================================================
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
a = my_gen()
next(a)
print(next(a))
next(a)
#This is printed first
#This is printed second
#2
#This is printed at last
===============================================
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
a = my_gen()
next(a)
next(a)
#This is printed first
#This is printed second
=======================================
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
a = my_gen()
print(next(a))
print(next(a))
#This is printed first
#1
#This is printed second
#2
======================================
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
print("another way :")
obj = simpleGeneratorFun()
print(next(obj))
print(next(obj))
print(next(obj))
#1
#2
#3
#another way :
#1
#2
#3
=================================================
def my_gen():
    n = 1
    print(n)
    # Generator function contains yield statements
    yield n
    n += 1
    print(n)
    yield n
    n += 1
    print(n)
    yield n
a = my_gen()
next(a)
next(a)
next(a)
#1
#2
#3
====================================
import random
def lottery():
    for i in range(5):
        yield random.randint(1,8)
    yield random.randint(11,20)
for i in lottery():
    print("number is ",i)
#number is  5
#number is  4
#number is  2
#number is  6
#number is  3
#number is  13
====================================
whenever we are using object, we need to  apply "next" keyword.
print(next(x));  # In Python 3, __next__()
print(x.__next__());  # In Python 3, __next__()
#x is object
