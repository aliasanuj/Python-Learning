==========================
#decorator================
==========================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        print("abc function")
    return inner
def outer1():
    print("in outer1 function")
obj = outer(outer1)
obj()

#inner function
#in outer1 function
#abc function
=====================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer1,outer2)
obj()
#inner function
#in outer2 function
#abcd function
#in outer1 function
#abc function
=======================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        print("abc function")
    return inner
@outer
def outer1():
    print("in outer1 function")
outer1()
#nner function
#in outer1 function
#abc function
==========================
def add_num_decorate(abc):
    def add_num1(i,j):
        print("before adding")
        print("sum = ",abc(i,j))
        print("after adding")
    return add_num1
def add_num2(i,j):
    return i+j
obj = add_num_decorate(add_num2)
obj(10,15)
#before adding
#sum =  25
#after adding
========================
def add_num_decorate(abc):
    def add_num1(i,j):
        print("before adding")
        print("sum = ",abc(i,j))
        print("after adding")
    return add_num1

@add_num_decorate
def add_num2(i,j):
    return i+j
@add_num_decorate
def add_num3(i,j):
    return i+j
add_num2(10,15)
add_num3(10,10)
#before adding
#sum =  25
#after adding
#before adding
#sum =  20
#after adding
============================
def add_num_decorate(abc):
    def add_num1(i,j):
        print("before adding")
        print("sum = ",abc(i,j))
        print("after adding")
    return add_num1

@add_num_decorate
def add_num2(i,j):
    return i+j
add_num2(10,10)
#before adding
#sum =  20
#after adding
============================
def outer(abc,abcd,abcde):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
        abcde()
        print("abcde function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer1,outer2)
obj()
#TypeError: outer() missing 1 required positional argument: 'abcde'
============================
def outer(abcd):
    def inner():
        print("inner function")
        print("after inner",abcd())
    return inner
def outer1():
    print("in outer1 function")
obj = outer(outer1)
obj()
#inner function
#in outer1 function
#after inner None
===========================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        print("abc function 00 ")
        abc()
        print("abc function 01")
    return  inner
@outer
def outer1():
    print("outer1 function")
outer1()
#inner function
#outer1 function
#abc function 00 
#outer1 function
#abc function 01
=======================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        abc()
    return  inner
@outer
def outer1():
    print("outer1 function")
outer1()
#inner function
#outer1 function
#outer1 function
=====================
#file name : learning.py
def outer(abc):
    def inner():
        print("inner function")
        abc()
        abc()
    return  inner

#file name : learning1.py

from learning import outer
@outer
def outer1():
    print("outer1 function")
outer1()

#inner function
#outer1 function
#outer1 function
========================
def outer(abc):
    def inner(*args):
        print("*" * 5)
        abc(*args)
        print("%" * 10)
        abc(*args)
        print("^" * 15)
    return inner
@outer
def inner01(x):
    print("Here we go :")
inner01(10)
#*****
#Here we go :
#%%%%%%%%%%
#Here we go :
#^^^^^^^^^^^^^^^
============================
def star(star):
    def inner(*a,**b):
        print("X" *10)
        star(*a,**b)
        print("X"*15)
        star(*a,**b)
        print("X"*30)
    return inner
@star
def inner01(x,y):
    print("anuj")
inner01("anything","anything")
#XXXXXXXXXX
#anuj
#XXXXXXXXXXXXXXX
#anuj
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
=============================================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer2,outer1)
obj()
#inner function
#in outer1 function
#abcd function
#in outer2 function
#abc function
===============================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        print("abc function")
        abcd()
        print("abcd")
    return inner
def outer1():
    print("in outer1 function")
obj = outer(outer1)
obj()
#inner function
#in outer1 function
#abc function
#NameError: name 'abcd' is not defined
==========================================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abc()
        print("abc function")
        abcd()
        print("abcd")
    return inner
def outer1():
    print("in outer1 function")
obj = outer(outer1)
obj()
#TypeError: outer() missing 1 required positional argument: 'abcd'
==============================================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abc function")
        abcd()
        print("abcd")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer1,outer2)
obj()
#inner function
#in outer2 function
#abc function
#in outer2 function
#abcd
=============================================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abc function")
        abcd()
        print("abcd")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer2,outer1)
obj()
#inner function
#in outer1 function
#abc function
#in outer1 function
#abcd
===============================================
def outer(abc):
  def inner(i,j):
    print("sadding starts :")
    print("sum is :",abc(i,j))
    print("after ading")
  return inner
def add_number(i,j):
  return (i+j)
obj = outer(add_number)
obj(10,15)
#sadding starts :
#sum is : 25
#after ading
===============================================
