#reduce_function.py
===========================
list1 = [1,2,3,4,5,6]
def add(x):
  return x+x
result = map(add,list1)
print(list(result))
#[2, 4, 6, 8, 10, 12]
=============================
import functools
import operator
list1 = [1,2,3,4,5,6]
result = functools.reduce(operator.add,list1)
print(result)
#21
=============================
import functools
list1 = [1,2,3,6,5,4,7]
result = functools.reduce(lambda x,y : x+y, list1)
print(result)
#28
==============================
import functools
list1 = [1,4,5,9,7,8,6,5]
result = functools.reduce(lambda x,y : x , list1)
print(result)
result = functools.reduce(lambda x,y : y , list1)
print(result)
#1
#5
==============================
import functools 
lis = [ 1 , 3, 5, 6, 2, ]  
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 
#The sum of the list elements is : 17
#The maximum element of the list is : 6
================================
import functools
import operator 
lis = [ 1 , 3, 5, 6, 2, ] 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(operator.add,lis)) 
print ("The product of list elements is : ",end="") 
print (functools.reduce(operator.mul,lis)) 
print ("The concatenated product is : ",end="") 
print (functools.reduce(operator.add,["geeks","for","geeks"])) 
#The sum of the list elements is : 17
#The product of list elements is : 180
#The concatenated product is : geeksforgeeks
=================================
import itertools 
import functools 
lis = [ 1, 3, 4, 10, 4 ] 
print ("The summation of list using accumulate is :",end="") 
print (list(itertools.accumulate(lis,lambda x,y : x+y))) 
print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,lis)) 
#The summation of list using accumulate is :[1, 4, 8, 18, 22]
#The summation of list using reduce is :22
=====================================
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
#24
==============================
print(list( filter((lambda x: x < 0), range(-5,5))))
#[-5, -4, -3, -2, -1]
=============================
