#map_function.py
==============================

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

