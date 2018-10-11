#generator :
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

