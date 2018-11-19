OOPS
==========================
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
