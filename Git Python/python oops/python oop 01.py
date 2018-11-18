# Below are OOP programming in Python ===========================================
# I have used different websites for this code snippets. ========================
# It might possible that some of the snippets may repeted twice or thrice =======
# Happie Learning ===============================================================
#================================================================================
#================================================================================
#=====================
#=====================
#oops programming====
#=====================
class a01:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def sum(self):
    print(self.a*self.b)

class a02(a01):
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def sum(self):
    print(self.a+self.b)

obj = a02(10,20)
obj.sum()

#30

=========================
class a01:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def sum(self):
    print(self.a*self.b)

class a02(a01):
  def __init__(self,a,b):
    self.a = a
    self.b = b
  #def sum(self):
    #print(self.a+self.b)

obj = a02(10,20)
obj.sum()

#200

==========================
class base:
    def __init__(self,name):
        self.name = name
class derived(base):
    def __init__(self,name,city):
        base.name = name
        self.city = city
    def combine(self):
        print(base.name, self.city)

obj = derived("anuj","patna")
obj.combine()
#anuj patna
===========================================
class abc:
  def __init__(self,name,roll):
    self.name = name
    self.roll = roll

class x(abc):
  def __init__(self,name,age,roll):
    abc.name=name
    self.age = age
    self.roll = roll

obj = x("anuj",25,1001)
print(obj.name)
print(obj.age)
print(obj.roll)

#anuj
#25
#1001
=======================================
class abc:
  def __init__(self,name,roll):
    self.name = "kumar"
    self.roll = "101"

class x(abc):
  def __init__(self,name,age,roll):
    abc.name="aman"
    self.age = 102
    self.roll = 1002

obj = x("anuj",25,1001)
print(obj.name)
print(obj.age)
print(obj.roll)

#aman
#102
#1002
========================================
class base:
    def __init__(self,name):
        self.name = name
class derived(base):
    def __init__(self,name,city):
        base.name = name
        self.city = city
    def combine(self):
        print(base.name, self.city)
        print(self.name, self.city)

obj = derived("anuj","patna")
obj.combine()

#anuj patna
#anuj patna
========================================
class base:
    def __init__(self,name):
        self.name = name
class derived(base):
    def __init__(self,name,city):
        base.name = "aman"
        self.city = city
        self.name = "abc"
    def combine(self):
        print(base.name, self.city)
        print(self.name, self.city)

obj = derived("anuj","patna")
obj.combine()

#aman patna
#abc patna
===========================================
class base:
    def __init__(self,name):
        self.name = name
class derived(base):
    def __init__(self,name,city):
        self.name = name
        self.city = city
    def combine(self):
        print(self.name, self.city)

obj = derived("anuj","patna")
obj.combine()
#anuj patna
==========================================
class A:
    def __init__(self, i = 0):
        self.i = i
class B(A):
    def __init__(self, j = 0):
        self.i = 0
        self.j = j
b = B()
print(b.i)
print(b.j)
#0
#0
=============================================
class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = sal
        self.age = age
        print(sal)

    def getData(self):
        print("salary is {} and age is {}".format(self.sal,self.age))
obj = EmployeeData(30000,25)
obj.getData()

#30000
#salary is 30000 and age is 25
==============================================
class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = 100
        self.age = age
        print(sal)

    def getData(self):
        print("salary is {} and age is {}".format(self.sal,self.age))
obj = EmployeeData(30000,25)
obj.getData()

#30000
#salary is 100 and age is 25
==============================================
class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = sal
        self.age = age

    def getData(self):
        print("salary is {} and age is {}".format(self.sal,self.age))
obj = EmployeeData(30000,25)
obj.getData()
#salary is 30000 and age is 25
================================
class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = sal
        self.age = age
        print("anuj")

    def getData(self):
        print("salary is {} and age is {}".format(self.sal,self.age))
obj = EmployeeData(30000,25)
obj.getData()

#anuj
#salary is 30000 and age is 25
=======================================
class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = sal
        self.age = age

    def getData(self):
        print("salary is {0} and age is {1}".format(self.sal,self.age))
obj = EmployeeData(30000,25)
obj.getData()
#salary is 30000 and age is 25
==========================================
class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = sal
        self.age = age

    def getData(self):
        print("salary is {} and age is {}".format(self.sal,self.age))
obj = EmployeeData(30000)
obj.getData()
#salary is 30000 and age is 0
===============================
class EmployeeData:

    def __init__(self, sal, age=0):
        self.sal = sal
        self.age = age

    def getData(self):
        print("salary is {} and age is {}".format(self.sal,self.age))
obj = EmployeeData(30000)
obj.getData()

#salary is 30000 and age is 0
===============================
class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = sal
        self.age = age

    def getData(self):
        print("salary is {} and age is {}".format(sal,age))
obj = EmployeeData(30000)
obj.getData()

#raceback (most recent call last):
  File "python", line 10, in <module>
  File "python", line 8, in getData
NameError: name 'sal' is not defined
===============================
class EmployeeData:

    def __init__(self, sal=0, age=0):
        self.sal = sal
        self.age = age

    def getData(self):
        print("salary is {} and age is {}".format(1000,2000))
obj = EmployeeData(30000)
obj.getData()

#salary is 1000 and age is 2000
===============================
class Sales:
    def __init__(self, id):
        self.id = id
        id = 100

val = Sales(123)
print (val.id)
#123
===============================
class Sales:
    def __init__(self, id):
        self.id = id
        print(id)
        id = 100
        print(id)

val = Sales(123)
#print (val.id)
#123
#100

=============================
class Sales:
    def __init__(self, id):
        self.id = id
        print(id)
        id = 100
        print(id)

val = Sales(123)
print (val.id)
#123
#100
#123
=================================

s = "\t\tWelcome\n"
print(s.strip())
#Welcome
==================
class Person:
    def __init__(self, id):
        self.id = id
sam = Person(100)
sam.__dict__['age'] = 49
print (sam.age + len(sam.__dict__))
#51
=====================
class Person:
    def __init__(self, id):
        self.id = id
sam = Person(100)
sam.__dict__['age'] = 49
print(sam.age)
print(len(sam.__dict__))
print (sam.age + len(sam.__dict__))
#49
#2
#51
================================================
class Person:
    def __init__(self, id=0):
        self.id = id
sam = Person()
sam.__dict__['age'] = 49
print(sam.age)
print(len(sam.__dict__))
print (sam.age + len(sam.__dict__))
#49
#2
#51
==============================================
class Person:
    def __init__(self, id):
        self.id = id
sam = Person()
sam.__dict__['age'] = 49
print(sam.age)
print(len(sam.__dict__))
print (sam.age + len(sam.__dict__))
#TypeError: __init__() missing 1 required positional argument: 'id'
==============================================
class A:
    def __init__(self, i = 0):
        self.i = i
class B(A):
    def __init__(self, j = 0):
        self.j = j
b = B()
print(b.i)
print(b.j)

#AttributeError: 'B' object has no attribute 'i'
========================
class A:
    def __init__(self, i = 0):
        self.i = i
class B(A):
    def __init__(self, j = 0):
        self.j = j
b = B()
#print(b.i)
print(b.j)
#0
=========================
class A:
    def __init__(self, i = 0):
        self.i = i
class B(A):
    def __init__(self, j = 0):
        self.i = 0
        self.j = j
b = B()
print(b.i)
print(b.j)
#0
#0
=======================
class A:
    def __init__(self, i = 10):
        self.i = 20
class B(A):
    def __init__(self, j = 0):
        self.i = 30
        self.j = j
b = B()
print(b.i)
print(b.j)

#30
#0
=========================
class A:
    def __init__(self):
        self.abc(30)
        print(self.i) #2nd execute
        print("i from A is", self.i) #last execute

    def abc(self, i):
      print(i)  #1st exectte
      self.i = 2 * i;
class B(A):
    def __init__(self):
        super().__init__()
b = B()

#30
#60
#i from A is 60
==========================
class A:
    def __init__(self):
        self.abc(30)
        print("i from A is", self.i)

    def abc(self, i):
        self.i = 2 * i;
class B(A):
    def __init__(self):
        super().__init__()

    def abc(self, i):
        self.i = 3 * i;
b = B()
#i from A is 90
=======================
class A:
    def __init__(self):
        self.abc(30)
        print("i from A is", self.i)

    def abc(self, i): #it will not called
        print(i)
        self.i = 2 * i;
class B(A):
    def __init__(self):
        super().__init__()

    def abc(self, i):
        print(i)
        self.i = 3 * i;
b = B()

#30
#i from A is 90
=======================
class A:
    def __init__(self):
        self.abc(30)
        print("i from A is", self.i)

    def abc(self, i):
        self.i = 2 * i;
class B(A):
    def __init__(self):
        super().__init__()
b = B()
#i from A is 60
===============================
class A:
    def __init__(self):
        self.abc(20)
        print("i from A is", self.i)

    def abc(self, i):
        self.i = 3 * i;
        print("value is ",self.i)
class B(A):
    def __init__(self):
        super().__init__()

obj = B()

#value is  60
#i from A is 60
==============================
class A:
    def __init__(self):
        self.abc(30)
        print(self.i)
        print("i from A is", self.i)

    def abc(self, i): #it wont be called
        self.i = 2 * i;
class B(A):
    def __init__(self):
        super().__init__()

    def abc(self, i):
        self.i = 3 * i;
b = B()
#90
#i from A is 90
========================
class A:
    def __init__(self):
        self.abc(30)

    def abc(self, i):
        self.i = 2 * i;
class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)
    def abc(self, i):
        self.i = 3 * i;
b = B()
#i from B is 90
============================
class A:
    def __init__(self):
        
        self.abc(30)
        print(self.i)
        print("i from A is", self.i)

    def abca(self, i): #it wont called
        self.i = 2 * i;
        print("value is ",self.i)
class B(A):
    def __init__(self):
        super().__init__()

    def abc(self, i):
        self.i = 3 * i;
b = B()
b.abca(12)

#90
#i from A is 90
#value is  24
==========================
class A:
    def __init__(self):
        self.abc(30)
        print(self.i)
    def abc(self, i):
        self.i = 2 * i;
class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)
    def abc(self, i):
        self.i = 3 * i;
b = B()
#90
#i from B is 90
========================
class A:
    def __init__(self):
        self.abc(30)
        print(self.i)
    def abc(self, i):
        self.i = 2 * i;
class B(A):
    def __init__(self):
      print("zzz")
      super().__init__()
      self.abc(50)
      print("i from B is", self.i)
    def abcd(self, i):
        self.i = 3 * i;
b = B()

#zzz
#60
#i from B is 100

=====================
class Test:
    def __init__(self, s):
        self.s = s

    def print(self):
        print(self.s)
a = Test("Python Class")
a.print()
#python Class
=========================
class Test:
    def __init__(self, s):
        self.s = s

    def print(self):
        print(self.s)
msg = Test()
msg.print()
#TypeError: __init__() missing 1 required positional argument: 's'
========================
class Test:
    def __init__(self, s):
        self.s = s

    def print(self):
        print(self.s)
msg = Test("anuj")
msg.print()

#anuj
=================================
class Test:
     def __init__(self, s = "Welcome"):
         self.s = s
 
     def print(self):
         print(self.s)
msg = Test()
msg.print()
#welcome
=============================
class Test:
    def __init__(self):
        self.x = 1
        self.__y = 5
 
    def getY(self):
        return self.__y
val = Test()
print(val.x)
#print(val.y)
print(val.getY)
print(val.getY())
#1
#<bound method Test.getY of <__main__.Test object at 0x7f14a8a4c0f0>>
#5
===========================
class Test:
    def __init__(self):
        self.x = 1
        self.__y = 1
 
    def getY(self):
        return self.__y
val = Test()
print(val.x)
#1
==============================
class Test:
    def __init__(self,m=15):
        self.m = m
        self.x = 1
        self.__y = 1

    def getY(self):
        return self.__y
val = Test()
print(val.x)
print(val.m)
#1
#15
=============================
class Test:
    def __init__(self):
        self.x = 1
        self.__y = 1
 
    def getY(self):
        return self.__y
val = Test()
print(val.__y)
#The program has an error because y is private and should not access it from outside the class. 
===============================
class Test:
     def __init__(self):
         self.x = 1
         self.__y = 1
 
     def getY(self):
         return self.__y
val = Test()
val.x = 45
print(val.x)
#45
===========================
class Test:
     def __init__(self):
     __a = 1
     self.__b = 1
     self.__c__ = 1
     __d__ = 1
#self.__b Is A Private Data Field In The Given Code Snippet
========================
class Test:
     def __init__(self):
         self.x = 1
         self.__y = 1
 
     def getY(self):
         return self.__y

val= Test()
val.__y = 45
print(val.getY())

#The program has an error because y is private and should not access it from outside the class. 
============================
def main():
    myCounter = Counter()
    num = 0
    for i in range(0, 100):
        increment(myCounter, num)
    print("myCounter.counter =", myCounter.counter, ", number of times =", num)
def increment(c, num):
    c.counter += 1
    num += 1
class Counter:
    def __init__(self):
        self.counter = 0
main()
#myCounter.counter = 100 , number of times = 0
===================================
class A:
    def __init__(self, i = 1):
        self.i = i
class B(A):
    def __init__(self, j = 2):
        ___________________
        self.j = j
def main():
    b = B()
    print(b.i, b.j)
main()
#A.__init__(self)
#super().__init__() 
==========================
class A:
    def __init__(self, i = 1):
        self.i = i
class B(A):
    def __init__(self, j = 2):
        A.__init__(self)
        self.j = j
def main():
    b = B()
    print(b.i, b.j)
main()
#1 2
=========================
class A:
    def __init__(self, i = 1):
        self.i = i
class B(A):
    def __init__(self, j = 2):
        super().__init__()
        self.j = j
def main():
    b = B()
    print(b.i, b.j)
main()
#1 2
============================
class A:
    def __init__(self, x = 1):
        self.x = x
class B(A):
    def __init__(self, y = 2):
        super().__init__()
        self.y = y
def main():
    b = B()
    print(b.x, b.y)
main()
#12
===========================
class A:
     def __init__(self):
         self.__x = 1
         self.y = 10
 
     def print(self):
         print(self.__x, self.y)
class B(A):
     def __init__(self):
         super().__init__()
         self.__x = 2
         self.y = 20
c = B()
c.print()
#1 20
======================
class A:
     def __init__(self):
         self.__x = 1
         self.y = 10
 
     def print(self):
         print(self.__x, self.y)
class B(A):
     def __init__(self):
         self.__x = 15
         super().__init__()
         self.__x = 2
         self.y = 20
c = B()
c.print()

#1 20
==========================
class A:
     def __init__(self):
         self.__x = 1
         self.y = 10
 
     def print(self):
         print(self.__x, self.y)
class B(A):
     def __init__(self):
         self.__x = 15
         super().__init__()
         self.__x = 2
         #self.y = 20
c = B()
c.print()

#1 10
==========================
class A:
    def __init__(self):
        self.__x = 1
        self.y = 10

    def print(self):
        print(self.__x, self.y)
class B(A):
    def __init__(self):
        super().__init__()
        self.__x = 2
        self.y = 20
    def print(self):
        print(self.__x,self.y)
c = B()
c.print()
# 2 20
==========================
class A:
    def __init__(self):
        self.__x = 1
        self.y = 10

    def print1(self):
        print(self.__x, self.y)
class B(A):
    def __init__(self):
        super().__init__()
        self.__x = 2
        self.y = 20
    def print(self):
        print(self.__x,self.y)
c = B()
c.print1()

#1 20
==========================
class A:
    def __init__(self, x = 0):
        self.x = x

    def func1(self):
        self.x += 1
class B(A):
    def __init__(self, y = 0):
       A.__init__(self, 3)
        self.y = y

    def func1(self):
        self.y += 1
def main():
    b = B()
    b.func1()
    print(b.x, b.y)
main()
#3 1
==========================
class A:
    def __new__(self):
        self.__init__(self)
        print("A's __new__() invoked")

    def __init__(self):
        print("A's __init__() invoked")
class B(A):
    def __new__(self):
        print("B's __new__() invoked")

    def __init__(self):
        print("B's __init__() invoked")
def main():
    b = B()
    a = A()
main()
#B’s __new__() invoked A’s __init__() invoked A’s __new__() invoked 
===========================
class A:
    def __new__(self):
        #self.__init__(self)
        print("A's __new__() invoked")
    def __init__(self):
        self.__init__(self)
        print("A's __init__() invoked")
class B(A):
    def __init__(self):
        print("B's __init__() invoked")
    def __new__(self):
        print("B's __new__() invoked")
def main():
    b = B()
    a = A()
main()
#B's __new__() invoked
#A's __new__() invoked
==========================
class A:
    def __init__(self, num):
        self.x = num
class B(A):
    def __init__(self, num):
        self.y = num
obj = B(11)
print ("%d %d" % (obj.x, obj.y))
#AttributeError: ‘B’ object has no attribute ‘x’
================================
class A:
    def __init__(self, num):
        self.x = num
class B(A):
    def __init__(self, num):
        self.x = num
        self.y = num
obj = B(11)
print ("%d %d" % (obj.x, obj.y))
#11 11
================================
class A:
    def __init__(self, num):
        self.x = 10
class B(A):
    def __init__(self, num):
        super().__init__(self)
        self.y = num
obj = B(11)
print ("%d %d" % (obj.x, obj.y))
#10 11
=================================
class A:
    def __init__(self):
        self.x = 1

    def func(self):
        self.x = 10
class B(A):
    def func(self):
        self.x += 1
        return self.x
def main():
    b = B()
    print(b.func())
main()
#2
=================================
class A:
    def __init__(self):
        self.x = 1

    def func(self):
        self.x = 10
class B(A):
    def func(self):
        print(self.x)
        self.x += 1
        return self.x
def main():
    b = B()
    print(b.func())
main()
#1
#2
=================================
=================================
© 2018 GitHub, Inc.
=================================
=================================

