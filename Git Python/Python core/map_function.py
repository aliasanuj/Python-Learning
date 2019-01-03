#map_function.py
==============================
#Map functions retrurns a list of results after applying the given function to each item of a given iterable (list | tuple).
#Syntax : map(function,iterable)
#It require two argument.
#We can pass one or more than one iteravle also.
#The return value from map then can be passed to functions like list,tuple.
#we need list | tuple while printing it.
=========================================
def map1(n):
    return n
numbers = (1,2,3,4,5,6)
result = map(map1,numbers)
print(list(result))
#[1, 2, 3, 4, 5, 6]
=========================
def map1(n):
    return n
numbers = (1,2,3,4,5,6)
result = map(map1,numbers)
print(tuple(result))
#(1, 2, 3, 4, 5, 6)
========================
def map1(n):
    return n
numbers = (1,2,3,4,5,6)
print(list(map(map1,numbers)))
#[1, 2, 3, 4, 5, 6]
==========================
def map1(n):
    return n
numbers = (1,2,3,4,5,6)
print(list(map(lambda x : x ,numbers)))
#[1, 2, 3, 4, 5, 6]
==========================
def map1(n):
    return n
numbers = (1,2,3,4,5,6)
print(list(map(lambda x : x+x ,numbers)))
#[2, 4, 6, 8, 10, 12]
============================
n1 = (1,2,3,4,5,6)  #we can use () | [] | {}
n2 = {1,2,3,4,5,6}
n3 = [1,2,3,4,5,6]
print(list(map(lambda x,y,z : x+y+z ,n1,n2,n3)))
#[3, 6, 9, 12, 15, 18]
=============================
a = {"sat","bat"}
test = map(list,a)
print(list(test))
#[['b', 'a', 't'], ['s', 'a', 't']]
=============================
a = {"sat","bat"}
print(list(map(list,a)))
#[['b', 'a', 't'], ['s', 'a', 't']]
==============================
def add(x,y):
    return x+y
x = map(add,("apple","orange","banana"),("coke","ice-cream","lemonade"))
print(list(x))
#['applecoke', 'orangeice-cream', 'bananalemonade']
==============================
def add(x):
    return x+x
def multiply(x):
    return x*x
func = (add,multiply)
for i in range(5):
    result = list(map(lambda x : x(i),func))
    print(result)
#[0, 0]
#[2, 1]
#[4, 4]
#[6, 9]
#[8, 16]
=====================================
list1 = ["aman","anuj","anshu"]
result = map(lambda x : x.replace("aman","anshu"),list1)
print(result)
print(list(result))
#<map object at 0x002E0CF0>
#['anshu', 'anuj', 'anshu']
=============================
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)
#[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
===================
def calculateSquare(n):
  return n*n
numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)
print(list(result))
#<map object at 0x7f5b520631d0>
#[1, 4, 9, 16]
=========================================
def calculateSquare(n):
  return n*n
numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
a = set(result)
print(a)
#{16, 1, 4, 9}
===================
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)
numbersSquare = set(result)
print(numbersSquare)
#<map object at 0x00499E50>
#{16, 1, 4, 9}
===================
def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))
#[5, 6, 6]
===================
def map1(n):
    return 
numbers = (1,2,3,4,5,6)
result = map(map1,numbers)
print(list(result))
#[None, None, None, None, None, None]
==================================
def map1(n):
    pass
numbers = (1,2,3,4,5,6)
result = map(map1,numbers)
print(list(result))
#[None, None, None, None, None, None]
===================================
def map1(n):
    return n 
numbers = (1,2,3,4,5,6)
result = map(map1,numbers)
print(tuple(result))
#(1, 2, 3, 4, 5, 6)
=======================================
list1 = ("anuj","kumar")
result = map(list,list1)
print(list(result))
#[['a', 'n', 'u', 'j'], ['k', 'u', 'm', 'a', 'r']]
=======================================
def myfunc(n):
  return len(n)
x = map(myfunc, ['apple', 'banana', 'cherry'])
print(list(x))
#[5, 6, 6]
==========================
list1 = [1,2,3,4,5,6]
result = map(lambda x : x+x, list1)
print(list(result))
#[2, 4, 6, 8, 10, 12]
=========================================
def calculateSquare(n):
  return n*n
numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
a = result
print(set(a))
print(list(a))
#{16, 1, 4, 9}
#[]
======================================
