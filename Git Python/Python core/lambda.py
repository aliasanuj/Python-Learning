#lambda.py
====================================
#In python anonymous function is function that is defined without a name, while normal function defined using the def keyword.
#In python anonymous function is defined by using Lambda keyword.
#syntax : double(lambda : x*2)
#Lambda functions used with built in functions like Filter | Map | Reduce | Etc
====================================
x = lambda a : a + 10
print(x(5))
#15
========================
x = lambda a, b : a * b
print(x(5, 6))
#30
=========================
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#13
========================
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#22
=========================
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11)) 
print(mytripler(11))
#22
#33
============================
def cube(y): 
    return y*y*y; 
g = lambda x: x*x*x 
print(g(7)) 
print(cube(5)) 
#343
#125
============================
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list) 
#[5, 7, 97, 77, 23, 73, 61]
============================
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list)
#[10, 14, 44, 194, 108, 124, 154, 46, 146, 122]
============================
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
#193
============================
li = [5, 8, 10, 20, 50, 100] 
sum = map(lambda x: x + x,li) 
print(list(sum))
#[10, 16, 20, 40, 100, 200]
========================
import functools
li = [5, 8, 10, 20, 50, 100] 
sum = functools.reduce(lambda x,y: x + y,li) 
print(sum)
#193
========================
import itertools
li = [5, 8, 10, 20, 50, 100] 
sum = list(itertools.accumulate(li, lambda x,y : x+y)) 
print(sum)
#[5, 13, 23, 43, 93, 193]
=========================
from collections import Counter
a = ["java","python","asp","bigdata"]
b = "pthyno" #word is python but not arranged
result = filter(lambda x : Counter(b)==Counter(x),a)
print(list(result))
#['python']
==========================
list1 = ["anuj","anshu","amama"]
result = filter(lambda x : x == "".join(reversed(x)),list1)
print(list(result))
#['amama']
============================
