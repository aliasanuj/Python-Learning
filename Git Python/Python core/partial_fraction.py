#partial_fraction.py
======================================
#Partial function allow to fix a certail number of arguments of function and generate a new functions.
#we need to import is --> from functools import partial | from functools import *
=======================================
from functools import partial 
def f(a, b, c, x): 
    return 1000*a + 100*b + 10*c + x 
g = partial(f, 3, 1, 4) 
print(g(5))
#3145
======================
from functools import *
def add(a, b, c): 
   return 100*a + 10*b  + c 
add_part = partial(add, c=2, b=1) 
print(add_part(3)) 
#312
======================
from functools import partial
def multiply(x,y):
        return x * y
dbl = partial(multiply,2)
print(dbl(4))
#8
=======================
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
obj = partial(func,2,3,4)
print(obj(1))
#26
========================
from functools import partial
def add(x, y):
     return x + y
p_add = partial(add, 2)
print(p_add(4))
#6
=========================
from functools import partial
def multiplier(x, y):
    return x * y
double = partial(multiplier, y=2)
triple = partial(multiplier, y=3)
print('Double of 2 is {}'.format(double(5)))
#Double of 2 is 10
=========================
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
obj = partial(func,u=2,v=3,w=4)
print(obj(1))
#TypeError: func() got multiple values for argument 'u'
#we need to assign value of u and its mandetory.
=========================
from functools import partial
def multiplier(x, y):
    return x * y
double = partial(multiplier, y=2)
triple = partial(multiplier, y=3)
print(double(20))
print(triple(20))
print('Double of 2 is {}'.format(double(5)))
print('Double of 2 is {}'.format(triple(5)))
#40
#60
#Double of 2 is 10
#Double of 2 is 15
===========================================
def abc(a,b,c):
  print(a,b,c)
d = {"a":10,"b":20,"c":30}
abc(*d)
abc(**d)
#a b c
#10 20 30
==========================================
