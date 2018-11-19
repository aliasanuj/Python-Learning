#OOPS 
=======================
class A:
    def __str__(self):
        return "A"
class B(A):
    def __str__(self):
        return "B"
class C(B):
    def __str__(self):
        return "C"
def main():
    b = B()
    a = A()
    c = C()
    print(c, b, a)
main()
#CBA
=======================
class A:
    def __str__(self):
        return "A"
class B(A):
    def __str__(self):
        return "B"
class C(B):
    def __str__(self):
        return "C"

c = C()
print(c)


#C
=======================
class A:
    def __str__(self):
        return "A"
class B(A):
    def __init__(self):
        super().__init__()
class C(B):
    def __init__(self):
        super().__init__()
def main():
    b = B()
    a = A()
    c = C()
    print(a, b, c)
main()
#AAA
==========================
class A:
    def __init__(self, x = 2, y = 3):
        self.x = x
        self.y = y

    def __str__(self):
        return "A"

    def __eq__(self, num ):
        return self.x * self.y == num.x * num.y
def main():
    a = A(1, 2)
    b = A(2, 1)
    print(a == b)
main()
#True
================
class A:
    def getInfo(self):
        return "A's getInfo is called"
  
    def printInfo(self):
        print(self.getInfo(), end = ' ')

class B(A):
    def getInfo(self):
        return "B's getInfo is called"

def main():
    A().printInfo()
    B().printInfo()
main()
#A’s getInfo is called B’s getInfo is called 
=====================
class A:
    def __getInfo(self):
        return "A's getInfo is called"

    def printInfo(self):
        print(self.__getInfo(), end=' ')
class B(A):
    def __getInfo(self):
        return "B's getInfo is called"
def main():
    A().printInfo()
    B().printInfo()
main()
#A's getInfo is called A's getInfo is called 
=============================
class A:
    def __getInfo(self):
        return "A's getInfo is called"

    def printInfo(self):
        print(self.__getInfo(), end=' ')
class B(A):
    def __getInfoanything(self):
        return "B's getInfo is called"
def main():
    A().printInfo()
    B().printInfo()
main()
#A's getInfo is called A's getInfo is called 
=================================
class foo:
  def __init__(self, x):
    self.x = x
  def __lt__(self, other):
    if self.x < other.x:
      return False
    else:
      return True

a = foo(2)
b = foo(3)
print(a < b)
#False
======================
class foo:
    def __init__(self, x):
        self.x = x
    def __less__(self, other):
        if self.x > other.x:
            return False
        else:
            return True
a = foo(2)
b = foo(3)
print(a < b)
#TypeError: '<' not supported between instances of 'foo' and 'foo'
==============================
class foo:
    def __init__(self, x):
        self.x = x
    def __lt__(self, other):
        if self.x < other.x:
            return True
        else:
            return False
a = foo(2)
b = foo(3)
print(a < b)
#True
======================
class test:
     def __init__(self,a="Hello World"):
         self.a=a
 
     def display(self):
         print(self.a)
obj=test()
obj.display()
#Hello World
=====================
class change:
    def __init__(self, x, y, z):
        self.a = x + y + z
 
x = change(1,2,3)
y = getattr(x, 'a')
setattr(x, 'a', y+1)
print(x.a)
#7
=======================
class test:
     def __init__(self,a):
         self.a=a
 
     def display(self):
         print(self.a)
obj=test()
obj.display()
#TypeError: __init__() missing 1 required positional argument: 'a'
===========================
class test:
     def __init__(self,a):
         self.a=a
 
     def display(self):
         print(self.a)
obj=test(10)
obj.display()

#10

=============================
class A:
	def __init__(self,b):
		self.b=b
	def display(self):
		print(self.b)
obj=A("Hello")
del obj
#Nothing will print
===============================
class A:
	def __init__(self,b):
		self.b=b
	def display(self):
		print(self.b)
obj=A("Hello")
obj.display()
del obj
obj.display()
#Hello
#Traceback (most recent call last):
#  File "python", line 9, in <module>
#NameError: name 'obj' is not defined
================================
class test:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var):
        var = 'New'
obj=test()
print(obj.variable)
#Old
===================================
class test:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var):
        var = 'New'
obj=test()
print(obj.variable)
#print(obj.var) #AttributeError: 'test' object has no attribute 'var'
#print(obj.change) #AttributeError: 'test' object has no attribute 'change'


#old

===================================
class fruits:
    def __init__(self, price):
        self.price = price
obj=fruits(50)
obj.quantity=10
obj.bags=2
print(obj.quantity+len(obj.__dict__))
#13
#In the above code, obj.quantity has been
#initialised to 10. There are a total of 
#three items in the dictionary, price, quantity 
#and bags. Hence, len(obj.__dict__) is 3.
=======================================
class Demo:
    def __init__(self):
        pass
 
    def test(self):
        print(__name__)
obj = Demo()
obj.test()
#__main__
=========================================
class Demo:
    def __init__(self):
        pass
 
    def test(self):
        print(__name__)
obj = Demo()
obj.test()
#__main__
=======================================
class fruits():
  def __init__(self,name):
    self.name = name
  def getname(self):
    return self.name
  def isfruit(self):
    return True
class taste(fruits):
  def isfruit(self):
    return False
object1 = fruits("apple")
print(object1.getname(), object1.isfruit())
object2 = taste("sweet")
print(object1.getname(), object2.isfruit())
print(object2.getname(), object2.isfruit())
#apple True
#apple False
#sweet False
========================
class test():
  def __init__(self, name, age, city):
    self.name = name 
    self.age = age 
    self.city = city
object = test("anuj",25,"patna")
print(object.__dict__)
#{'name': 'anuj', 'age': 25, 'city': 'patna'}
==============================
class outer():
  pass
class inner(outer):
  pass
print(issubclass(inner,outer))
print(issubclass(outer,inner))
#True
#False
===================================
class outer():
  def __init__(self):
    self.first = "kumar"
    print("first name")
class inner():
  def __init__(self):
    self.last = "anuj"
    print("last name")
class final(inner,outer):
  def __init__(self):
    outer.__init__(self)
    inner.__init__(self)
    print("final class")
  def print(self):
    print(self.first, self.last)
object = final()
object.print()
#first name
#last name
#final class
#kumar anuj
==============================
class outer():
  def __init__(self):
    self.first = "kumar"
    #print("first name")
class inner():
  def __init__(self):
    self.last = "anuj"
    #print("last name")
class final(inner,outer):
  def __init__(self):
    outer.__init__(self)
    inner.__init__(self)
    print("final class")
  def print(self):
    print(self.first, self.last)
object = final()
object.print()
#final class
#kumar anuj
============================
class outer():
  def __init__(self,name):
    self.name = name 
    print("name is ",name)
class inner(outer):
  def __init__(self,city):
    self.city = city
    print("city name is ",city)
object1 = inner("patna")
object2 = outer("anuj")
#city name is  patna
#name is  anuj
===========================
#how to access parent member in sub class
class outer():
  def __init__(self,name):
    self.name = name 
    #print("name is ",name)
class inner(outer):
  def __init__(self,name,city):
    outer.name = name  #we can use class name to access other elements in child class
    self.city = city
    #print("city name is ",city)
  def combine(self):
    print("my name is ",outer.name ,"and my city is ", self.city)
object = inner("anuj","patna")
object.combine()
#my name is  anuj and my city is  patna
========================================
class outer():
  def __init__(self,name):
    self.name = name 
    print("name is ",name)
class inner(outer):
  def __init__(self,name,city):
    outer.name = name  #we can use class name to access other elements in child class
    self.city = city
    print("city name is ",city)
  def combine(self):
    print("my name is ",outer.name ,"and my city is ", self.city)
object = inner("anuj","patna")
object.combine()

#city name is  patna
#my name is  anuj and my city is  patna
==================================
#how to access parent member ib=n sub class
class outer():
  def __init__(self,name):
    self.name = name 
    #print("name is ",name)
class inner(outer):
  def __init__(self,name,city):
    super(inner,self).__init__(name)
    self.city = city
    #print("city name is ",city)
  def combine(self):
    print("my name is ",self.name ,"and my city is ", self.city)
object = inner("anuj","patna")
object.combine()
#my name is  anuj and my city is  patna
===========================================
#how to access parent member in sub class
class outer():
  def __init__(self,name,age):
    self.name = name
    self.age = age
    #print("name is ",name)
class inner(outer):
  def __init__(self,name,age,city):
    super(inner,self).__init__(name,age)
    self.city = city
    #print("city name is ",city)
  def combine(self):
    print("name",self.name ,"age", self.age,"city",self.city)
object = inner("anuj",25,"patna")
object.combine()
#name anuj age 25 city patna
==========================================
class outer():
  def __init__(self,number):
    self.number = number
  def double(self):
    self.number = self.number * 2
class inner(outer):
  def __init__(self,number):
    outer.__init__(self,number)
  def tripple(self):
    self.number = self.number * 3
object = inner(10)
print(object.number)
object.double()
print(object.number)
object.tripple()
print(object.number)
#10
#20
#60
====================================
class outer():
  def __init__(self,number):
    self.number = number
  def double(self):
    self.number = self.number * 2
    print(self.number)
  def tripple(self):
    self.number = self.number * 3
    print(self.number)
class inner(outer):
  def __init__(self,number):
    outer.__init__(self,number)
  def square(self):
    self.number = self.number ** 2
    print(self.number)
object = inner(10)
object.double()
object.tripple()
object.square()
#20
#60
#3600
====================================
class outer():
  def __init__(self,number):
    self.number = number
  def double(self):
    self.number = self.number * 2
    print(self.number)
  def tripple(self):
    self.number = self.number * 3
    print(self.number)
class inner(outer):
  def __init__(self,number):
    outer.__init__(self,number)
  def tripple(self):
    self.number = self.number * 3
object = inner(10)
object.double()
object.tripple()
#20
=====================================
class outer():
  def __init__(self,number):
    self.number = number
  def double(self):
    self.number = self.number * 2
    print(self.number)
  def tripple(self):
    self.number = self.number * 3
    print(self.number)
class inner(outer):
  def __init__(self,number):
    outer.__init__(self,number)
object = inner(10)
object.double()
object.tripple()
#20
#60
=====================================
class outer():
  def __init__(self,fName,lName,age):
    self.fName = fName
    self.lName = lName
    self.age = age
class inner(outer):
  def __init__(self,fName,lName,age,rollNo):
    super(inner,self).__init__(fName,lName,age)
    self.rollNo = rollNo
object = inner("kumar","anuj",25,101)
print(object.fName)
print(object.rollNo)
#kumar
#101
=============================
class outer():
  def __init__(self,fName,lName,age):
    self.fName = fName
    self.lName = lName
    self.age = age
  def pincode(self,pincode):
    self.pincode = pincode
class inner(outer):
  def __init__(self,fName,lName,age,rollNo):
    super(inner,self).__init__(fName,lName,age)
    outer.pincode(self,1001)
    self.rollNo = rollNo
object = inner("kumar","anuj",25,101)
print(object.fName)
print(object.rollNo)
#kumar
#101
=============================
class outer():
  def __init__(self,fName,lName,age):
    self.fName = fName
    self.lName = lName
    self.age = age
  def pincode(self,pincode):
    self.pincode = pincode
class inner(outer):
  def __init__(self,fName,lName,age,rollNo):
    outer.__init__(self,fName,lName,age)
    outer.pincode(self,1001)
    self.rollNo = rollNo
object = inner("kumar","anuj",25,101)
print(object.fName)
print(object.rollNo)
#kumar
#101
==============================
#Doc String
class test():
  "Hello world"
  "My name is Anuj"
  "I work in infosys"

  def inner(self):
    print("abc")
print(test.__doc__)
#Hello world
====================================
class test():
  "Hello World"
  def inner(self):
    print("Hello Anuj")
object = test()
print(object.inner())
print("+++++ next line +++")
object.inner()
#Hello Anuj
#None
#+++++ next line +++
#Hello Anuj
=======================================
class outer():

  def __init__(self):
    print("Hi i am anuj")
object = outer()
#Hi i am anuj
===============================
class outer():
  def __init__(self):
    print("Hello i am anuj")
  def __init__(self):
    print("Hello i am nitin")
  def __init__(self):
    print("Hello i am satya")
object = outer()
#Hello i am satya
===================================
class outer():
  def __init__(self):
    self.__update01()
  def __init__(self):
    self.__update02()
  def __update01(self):
    print("Hrllo World")
  def __update02(self):
    print("Hii world")
object = outer()
#Hii world
=======================================
class test():
  name = "kumar"
  city = "patna"
  def __init__(self):
    self.__name = "anuj"
    self.__company = "infosys"
  def combine(self):
    print("roll no is ",self.__name,"and name is",self.__company)
object = test()
object.combine()
#roll no is  anuj and name is infosys
==========================================
class test():
  name = "kumar"
  city = "patna"
  def __init__(self):
    self.__name = "anuj"
    self.__city = "patna"
  def combine(self):
    print("name is ",self.__name,"city is ",self.__city)
  def final(self):
    self.__name = "anuj kumar"
    self.__city = "patna patna"
    print("name is ",self.__name,"city is ",self.__city)
object = test()
object.combine()
object.final()
#name is  anuj city is  patna
#name is  anuj kumar city is  patna patna
=========================================
class A:
    def __init__(self):
        self.abc(30)

    def abc(self, i):
        self.i = 2 * i;
class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)
b = B()
#i from B is 60
===================================
class Test:
    def __init__(self, s):
        self.s = s

    def print(self):
        print(self.s)
msg = Test("anuj")
msg.print()
#anuj
================================
class Test:
    def __init__(self, s):
        self.s = "kumar"

    def print(self):
        print(self.s)
msg = Test("anuj")
msg.print()
#kumar
=================================
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
===================================
class A:
    def __init__(self, x = 0):
        self.x = x

    def func1(self):
        self.x += 1
class B(A):
    def __init__(self, y = 0):
        A.__init__(self, 3)
        self.y = y
def main():
    b = B()
    b.func1()
    print(b.x, b.y)
main()
#4 0
===========================================
class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "A"

    def __eq__(self, num ):
        return self.x * self.y == num.x * num.y
def main():
    a = A(1, 2)
    b = A(2, 1)
    print(a == b)
main()
#True
==================================
class A:
    def getInfo(self):
        return "A's getInfo is called"
class B(A):
    def printInfo(self):
        print(self.getInfo(), end = ' ')

    def getInfo(self):
        return "B's getInfo is called"
def main():
    A().printInfo()
    B().printInfo()
main()
#AttributeError: 'A' object has no attribute 'printInfo'
=======================================
class A:
    def getInfo(self):
        return "A's getInfo is called"
    def printInfo(self):
        print(self.getInfo(), end = ' ')
class B(A):
    def printInfo(self):
        print(self.getInfo(), end = ' ')

    def getInfo(self):
        return "B's getInfo is called"
def main():
    A().printInfo()
    B().printInfo()
main()
#A's getInfo is called B's getInfo is called    
=========================================
class fruits:
    def __init__(self, price):
        self.price = price
obj=fruits(5)
obj.quantity=50
obj.bags=500
print(obj.quantity+len(obj.__dict__))
#53
========================================
class fruits:
    def __init__(self, price):
        self.price = price
obj=fruits(5)
obj.quantity=50
obj.bags=500
obj.abc = 5000
print(obj.quantity+len(obj.__dict__))
#54
==================================
class fruits():
  def __init__(self,name):
    self.name = name
  def getname(self):
    return self.name
  def isfruit(self):
    return True
class taste(fruits):
   pass
object1 = fruits("apple")
print(object1.getname(), object1.isfruit())
object2 = taste("sweet")
print(object1.getname(), object2.isfruit())
print(object2.getname(), object2.isfruit())
#apple True
#apple True
#sweet True
==========================================
896
class outer():
  def __init__(self,name="anuj"):
    self.name = name 
    #print("name is ",name)
class inner(outer):
  def __init__(self,city):
    outer.__init__(self)  #we can use class name to access other elements in child class
    self.city = city
    #print("city name is ",city)
  def combine(self):
    print("my name is ",self.name ,"and my city is ", self.city)
object = inner("anuj")
object.combine()
#my name is  anuj and my city is  anuj
=============================================
class outer():
  def __init__(self,number):
    self.number = number
  def double(self):
    self.number = self.number * 2
    print(self.number)
  def tripple(self):
    self.number = self.number * 3
    print(self.number)
class inner(outer):
  def __init__(self,number):
    super(inner,self).__init__(number)
  def square(self):
    self.number = self.number ** 2
    print(self.number)
object = inner(10)
object.double()
object.tripple()
object.square()
#20
#60
#3600
=================================================
class outer():
  def __init__(self,fName,lName,age):
    self.fName = fName
    self.lName = lName
    self.age = age
  def pincode(self,pincode):
    self.pincode = pincode
class inner(outer):
  def __init__(self,fName,lName,age,rollNo):
    super(inner,self).__init__(fName,lName,age)
    outer.pincode(self,1001)
    self.rollNo = rollNo
object = inner("kumar","anuj",25,101)
print(object.fName)
print(object.rollNo)
print(object.pincode)
#kumar
#101
#1001
================================================
class test():
  "Hello World"
  def inner(self):
    print("Hello Anuj")
object = test()
print(object.inner)
print(object.inner())
print("+++++ next line +++")
object.inner()

#<bound method test.inner of <__main__.test object at 0x7f43fe3bb588>>
#Hello Anuj
#None
#+++++ next line +++
#Hello Anuj
===================================
===================================
===================================
© 2018 GitHub, Inc.
===================================
===================================
===================================
