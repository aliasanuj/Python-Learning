#OOPS
===============================
===============================
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
class fruits:
    def __init__(self, price):
        self.price = price
obj=fruits(5)
obj.quantity=50
obj.bags=500
#obj.abc = 5000
print(obj.quantity+len(obj.__dict__))
#53
===================================
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
class test:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var):
        var = 'New'
obj=test()
print(obj.variable)
#old
=====================
class A:
    pass
#Empty Class
=====================
class A:
    return
#SyntaxError: 'return' outside function
=====================
class A:
SyntaxError: unexpected EOF while parsing
======================
class B(object):
  def first(self):
    print("First method called")
  def second():
    print("Second method called")
ob = B()
B.first(ob)
#First method called 
#Explanation: The method may be created in 
#the method demonstrated in the code as well 
#and this is called as the unbounded method call. 
#Calling the method using obj.one() is the bounded method call.
=============================
class B(object):
  def first(self):
    print("First method called")
  def second():
    print("Second method called")
ob = B()
B.first(ob) #ob.first()

#First method called

====================================
class demo():
	def __repr__(self):
		return '__repr__ built-in function called'
	def __str__(self):
		return '__str__ built-in function called'
s=demo()
print(s)
#__str__ built-in function called
=============================
class demo():
	def __repr__(self):
		return '__repr__ built-in function called'
	def __str__(self):
		return '__str__ built-in function called'
s=demo()
s()
#TypeError: 'demo' object is not callable
==============================
class demo():
	def __repr__(self):
		return '__repr__ built-in function called'
	def __str__(self):
		return '__str__ built-in function called'
obj = demo()
obj
#Nothing will print
===================================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.age=7
print(hasattr(stud1, 'age'))
#True
=======================================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.age=7
print(hasattr(stud1, 'roll_no'))
#True
==========================================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.age=7
print(hasattr(stud1, ('roll_no','age','grade')))
#TypeError: hasattr(): attribute name must be string
==========================================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.age=7
print(hasattr(stud1, 'roll_no','age','grade'))
#TypeError: hasattr expected 2 arguments, got 4
====================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.age=7
print(hasattr(stud1, 'roll_no','age'))
#TypeError: hasattr expected 2 arguments, got 3
=======================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.age=7
print(hasattr(stud1, 'zzz'))

#false
====================================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.grade=7
print(hasattr(stud1, 'zzz'))

#false
=================================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.grade=7
print(hasattr(stud1, 'grade'))

#True
===================================
class stud:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = stud(34, 'S')
stud1.abc=7
print(hasattr(stud1, 'abc'))

#True
====================================
class Demo:
    def __new__(self):
        self.__init__(self)
        print("Demo's __new__() invoked")
    def __init__(self):
        print("Demo's __init__() invoked")
class Derived_Demo(Demo):
    def __new__(self):
        print("Derived_Demo's __new__() invoked")
    def __init__(self):
        print("Derived_Demo's __init__() invoked")
def main():
    obj1 = Derived_Demo()
    obj2 = Demo()
main()
#Derived_Demo’s __new__() invoked
#Demo’s __init__() invoked
#Demo’s __new__() invoked

#Since the object for the derived class is 
#declared first, __new__() method of the derived 
#class is invoked first, followed by the constructor 
#and the __new__() method of main class.
===============================
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()
#Error because class B inherits A but variable x isn’t inherited
#Since the invoking method, Test.__init__(self), isn’t present in
#the derived class, variable x can’t be inherited.
===============================
class A():
    def disp(self):
        print("A disp()")
class B(A):
    pass
obj = B()
obj.disp()
#A disp()
#Class B inherits class A hence the function disp ()
#becomes part of class B’s definition. Hence disp() 
#method is properly executed and the line is printed
==================================
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()
#01
#Since the invoking method has been 
#properly invoked, variable x from the main 
#class has been properly inherited and it can also be accessed.
================================
class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main()
#1 2
#In the above piece of code, 
#the invoking method has been 
#properly implemented and hence x=1 and y=2.
=======================
class A:
    def one(self):
        return self.two()
 
    def two(self):
        return 'A'
class B(A):
    def two(self):
        return 'B'
obj1=A()
obj2=B()
print(obj1.two(),obj2.two())
#A B
========================
class A():
    pass
class B():
    pass
class C(A,B):
    pass
#IT IS MULTIPLE INHERITANCE 
#In multiple inheritance, two or more 
#subclasses are derived from the superclass 
#as shown in the above piece of code.
=============================
class A():
    pass
class B(A):
    pass
class C(B):
    pass
#MULYILEVEL Inheritance
#In multi-level inheritance, a subclass
#derives from another class which itself 
#is derived from another class.
==============================
class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)
class B(A):
     def __init__(self):
         super().__init__()
         self.__i = 2
         self.j = 7  
c = B()
c.display()
#1 7
#Any change made in variable i isn’t reflected 
#as it is the private member of the superclass
==========================
class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)
class B(A):
     def __init__(self):
         super().__init__()
         self.__i = 2
         self.j = 7  
         print("abc")
c = B()
c.display()

#abc
#1 7
==========================
class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main()
#3 1
==============================
class A:
	pass
class B(A):
	pass
obj=B()
isinstance(obj,A)
#True
============================
class A:
	pass
class B(A):
	pass
obj=B()
print(isinstance(obj,B))
print(isinstance(obj,A))

#True
#True
============================
class A:
    def __init__(self):
        self.__x = 1
class B(A):
    def display(self):
        print(self.__x)
def main():
    obj = B()
    obj.display()
main()
#Error, private class member can’t be accessed in a subclass
#Private class members in the superclass can’t be accessed in the subclass.
==============================
class A:
    def __init__(self):
        self._x = 5       
class B(A):
    def display(self):
        print(self._x)
def main():
    obj = B()
    obj.display()
main()
#5
#The class member x is protected, 
#not private and hence can be accessed by subclasses
===============================
class A:
    def __init__(self,x=3):
        self._x = x        
class B(A):
    def __init__(self):
        super().__init__(5)
    def display(self):
        print(self._x)
def main():
    obj = B()
    obj.display()
main()
#5
#The super() method re-assigns the variable x 
#with value 5. Hence 5 is printed.
============================
class A:
    def test1(self):
        print(" test of A called ")
class B(A):
    def test(self):
        print(" test of B called ")
class C(A):
    def test(self):
        print(" test of C called ")
class D(C,B):
    def test2(self):
        print(" test of D called ")        
obj=D()
obj.test()
#test of C called 
=================================
class A:
    def test1(self):
        print(" test of A called ")
class B(A):
    def test1(self):
        print(" test of B called ")
class C(A):
    def test(self):
        print(" test of C called ")
class D(C,B):
    def test2(self):
        print(" test of D called ")        
obj=D()
obj.test1()

# test of B called 
=================================
class A:
    def test1(self):
        print(" test of A called ")
class B(A):
    def test(self):
        print(" test of B called ")
class C(A):
    def test(self):
        print(" test of C called ")
class D(B,C):
    def test2(self):
        print(" test of D called ")        
obj=D()
obj.test()
#test of B called 
=================================
class A:
    def test(self):
        print("test of A called")
class B(A):
    def test(self):
        print("test of B called")
        super().test()  
class C(A):
    def test(self):
        print("test of C called")
        super().test()
class D(B,C):
    def test2(self):
        print("test of D called")      
obj=D()
obj.test()
#test of B called
#test of C called
#test of A called
#Since the invoking method, super().test() 
#is called in the subclasses, all the three 
#methods of test() in three different classes is called.
=================================
class A:
    def test(self):
        print("test of A called")
class B(A):
    def test(self):
        print("test of B called")
        super().test()  
class C(A):
    def test1(self):
        print("test of C called")
        super().test()
class D(B,C):
    def test2(self):
        print("test of D called")      
obj=D()
obj.test()

#test of B called
#test of A called
=================================
class A:
    def __str__(self):
        return '1'
class B(A):
    def __init__(self):
        super().__init__()
class C(B):
    def __init__(self):
        super().__init__()
def main():
    obj1 = B()
    obj2 = A()
    obj3 = C()
    print(obj1, obj2,obj3)
main()
#1 1 1
====================
class Demo:
    def __init__(self):
        self.x = 1
    def change(self):
        self.x = 10
class Demo_derived(Demo):
    def change(self):
        self.x=self.x+1
        return self.x
def main():
    obj = Demo_derived()
    print(obj.change())
main()
#2
=======================
class A:
    def __repr__(self):
        return "1"
class B(A):
    def __repr__(self):
        return "2"
class C(B):
    def __repr__(self):
        return "3"
o1 = A()
o2 = B()
o3 = C()
print(obj1, obj2, obj3)
#1 2 3
#When different objects are invoked, each of the individual 
#classes return their individual values and hence it is printed.
======================
class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)
 
    def multiply(self, i):
        self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()
 
    def multiply(self, i):
        self.i = 2 * i;
obj = B()
#30
========================
class Demo:
    def check(self):
        return " Demo's check "  
    def display(self):
        print(self.check())
class Demo_Derived(Demo):
    def check(self):
        return " Derived's check "
Demo().display()
Demo_Derived().display()
#Demo’s check Derived’s check
#Demo().display() invokes the display() 
#method in class Demo and Demo_Derived().display() 
#invokes the display() method in class Demo_Derived.
=========================
class A:
    def __init__(self):
        self.multiply(15)
    def multiply(self, i):
        self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()
        print(self.i)
 
    def multiply(self, i):
        self.i = 2 * i;
obj = B()
#30
============================
class A:
    def __init__(self):
        self.multiply(15)
        print("aaa")
    def multiply(self, i):
        self.i = 4 * i;
        print("sss")
class B(A):
    def __init__(self):
        super().__init__()
        print(self.i)
        print("vvv")
 
    def multiply(self, i):
        self.i = 2 * i;
obj = B()

#aaa
#30
#vvv
============================
class Demo:
    def __check(self):
        return " Demo's check "
    def display(self):
        print(self.__check())
class Demo_Derived(Demo):
    def __check(self):
        return " Derived's check "
Demo().display()
Demo_Derived().display()
#Demo’s check Demo’s check
==========================
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 1
    def __eq__(self, other):
        return self.x * self.y == other.x * other.y
obj1 = A(5, 2)
obj2 = A(2, 5)
print(obj1 == obj2)
#True
==============================
class A:
    def one(self):
        return self.two()    	
    def two(self):
        return 'A'   
class B(A):
    def two(self):
        return 'B'
obj2=B()
print(obj2.two())
#B
=============================
class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
 
    def display(self):
        return self.__b
 
obj = Demo()
print(obj.__b)
#AttributeError: 'Demo' object has no attribute '__b'
#The program has an error because b is private and hence can’t be printed
===========================
def Demo:
def __init__(self):
    __a = 1
    self.__b = 1
    self.__c__ = 1
    __d__= 1
#Variables such as self.__b are private members of the class.
=============================
class Demo:
     def __init__(self):
         self.a = 1
         self.__b = 1
 
     def get(self):
         return self.__b
 obj = Demo()
print(obj.get())
#1 
#Here, get(self) is a member of the class. 
#Hence, it can even return a private member of the class.
#Because of this reason, the program runs fine and 1 is printed.
=============================
class Demo:
     def __init__(self):
         self.a = 1
         self.__b = 1
     def get(self):
         return self.__b
obj = Demo()
obj.a=45
print(obj.a)
#45
#It is possible to change the values of 
#public class members using the object of the class.
===============================
class fruits:
    def __init__(self):
        self.price = 100
        self.__bags = 5
    def display(self):
        print(self.__bags)
obj=fruits()
obj.display()
#The program runs fine and 5 is printed
#Private class members can be printed by 
#methods which are members of the class.
============================
class student:
    def __init__(self):
        self.marks = 97
        self.__cgpa = 8.7
    def display(self):
        print(self.marks)
obj=student()
print(obj._student__cgpa)
#8.7
=========================
class objects:
    def __init__(self):
        self.colour = None
        self._shape = "Circle" 
 
    def display(self, s):
        self._shape = s
obj=objects()
print(obj._objects_shape)
#AttributeError: 'objects' object has no attribute '_objects_shape'
=================================
209 
class A:
    def one(self):
        return self.two()
 
    def two(self):
        return 'A'
class B(A):
    def two(self):
        return 'B'
obj1=A()
obj2=B()
print(obj1.one(),obj2.two())
#A B
================================
class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)
class B(A):
      def __init__(self):
         super().__init__()
         self.__i = 2
         self.j = 7
      def display(self):
        print(self.__i, self.j)
c = B()
c.display()  
#2 7
========================================
class A:
	pass
class B(A):
	pass
obj=B()
print(isinstance(obj,B))
#True
============================================
class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)
class B(A):
     def __init__(self):
         A.__init__(self)
         self.__i = 2
         self.j = 7  
c = B()
c.display()
#1 7
=================================
class A:
    def test1(self):
        print(" test of A called ")
class B(A):
    def test(self):
        print(" test of B called ")
class C(A):
    def test2(self):
        print(" test of C called ")
class D(C,B):
    def test3(self):
        print(" test of D called ")        
obj=D()
obj.test()
# test of B called 
============================
class Demo:
    def __init__(self):
        self.x = 1
    def change(self):
        self.x = 10
class Demo_derived(Demo):
    def change(self):
        self.x=self.x+1
def main():
    obj = Demo_derived()
    print(obj.change())
main()
#None
====================================
class base:
    def __init__(self,x):
        self.x = "anuj"
class derived(base):
    def __init__(self,x,y):
        super(derived,self).__init__(x)
        self.y = y
    def combine(self):
        print(self.x,self.y)
obj = derived("abc",20)
obj.combine()
#anuj 20
======================================
class base:
    def __init__(self,x):
        self.x = x
class derived(base):
    def __init__(self,x,y):
        super(derived,self).__init__(x)
        self.y = y
    def combine(self):
        print(self.x,self.y)
obj = derived("abc",20)
obj.combine()
#abc 20
===================================
===================================
===================================
===================================
© 2018 GitHub, Inc.
===================================
===================================
===================================
