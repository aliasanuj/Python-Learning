#packing_unpacking.py
======================
def fun(a, b, c, d): 
    print(a, b, c, d) 
my_list = [1, 2, 3, 4] 
fun(my_list) 
#TypeError: fun() missing 3 required positional arguments: 'b', 'c', and 'd'
============================
def abc(*a):
    sum = 0
    for i in range(0,len(a)):
        sum = sum + a[i]
    return sum
print(abc(1,2,3,4,5))
#15
=============================
def fun(a, b, c, d): 
    print(a, b, c, d) 
my_list = [1, 2, 3, 4] 
fun(*my_list) 
#1 2 3 4
============================
def mySum(*args): 
    sum = 0
    for i in range(0, len(args)): 
        sum = sum + args[i] 
    return sum 
print(mySum(1, 2, 3, 4, 5)) 
print(mySum(10, 20))
#15
#30
=============================
def fun1(a, b, c): 
    print(a, b, c) 
def fun2(*args): 
  args = list(args) 
  args[0] = 'Geeksforgeeks'
  args[1] = 'awesome'
  fun1(*args) 
fun2('Hello', 'beautiful', 'world!') 
fun1("anuj","aman","anshu")
fun2('Hello', 'beautiful', 'world!') 
#Geeksforgeeks awesome world!
#anuj aman anshu
#Geeksforgeeks awesome world!
===============================
def fun(a, b, c): 
    print(a, b, c) 
d = {'a':2, 'b':4, 'c':10} 
fun(**d)
#2 4 10
===============================
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)
#Guru99
#20
#Education
==============================
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print  (tup1[0])
print  (tup2[1:4])
#Robert
#(2, 3, 4)
===============================
