===================================
==========methods==================
===================================
1. It's a function which is a member of a class:
class C:
    def my_method(self):
        print("I am a C")
c = C()
c.my_method()  # Prints "I am a C"

2. Method is called by its name, but it is associated to an object (dependent).
3. A method is implicitly passed the object on which it is invoked.
4. It may or may not return any data.
5. A method can operate on the data (instance variables) that is contained by the corresponding class

# Basic Python method  
class class_name 
    def method_name () : 
        ...... 
        # method body 
        ......    
class ABC : 
    def method_abc (self): 
        print("I am in method_abc of ABC class. ") 
  class_ref = ABC() # object of ABC class 
class_ref.method_abc() 
============================
===========Functions========
============================
1. Function is block of code that is also called by its name. (independent)
2. The function can have different parameters or may not have any at all. If any data (parameters) 
are passed, they are passed explicitly.
3. It may or may not return any data.
4. Function does not deal with Class and its instance concept.
5. Basic Function Structure in Python :

def function_name ( arg1, arg2, ...) : 
    ...... 
    # function body 

def Subtract (a, b): 
    return (a-b) 
print( Subtract(10, 12) ) # prints -2 
print( Subtract(15, 6) ) # prints 9 
============================================
Difference between method and function:=====
============================================
1. Simply, function and method both look similar as they perform in almost similar way, 
but the key difference is the concept of ‘Class and its Object‘.
2. Functions can be called only by its name, as it is defined independently. 
But methods can’t be called by its name only, we need to invoke the class by a 
reference of that class in which it is defined, i.e. method is defined within a class and 
hence they are dependent on that class.


============================
============================
============================
============================
===============================
==========super================
===============================

super().__init__('Dog') ==> super().__init__("argument")
Mammal.__init__(self, 'Dog') ==> baseclassName.__init__(self,"argument")


1. The super() builtin returns a proxy object that allows you to refer parent class by 'super'.
2. In Python, super() built-in has two major use cases:
==>Allows us to avoid using base class explicitly
==>Working with Multiple Inheritance
3. If your program contains multi-level inheritance, then this super() function is helpful for you.
4. super() is useful for accessing inherited methods that have been overridden in a class. 
5. The search order is same as that used by getattr() except that the type itself is skipped.


super() with Single Inheritance:
==================================
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print( 2 * self.length + 2 * self.width)

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

square = Square(4)
square.area()
#16
====================================
class abc():
    def __init__(self,name,age):
        self.sjsh = name
        self.jjhdj = age
        print("name is ",name)
        print("name is ",age)
class abc01(abc):
    def __init__(self):
        super().__init__("anuj",54)
obj1 = abc01()
# name is  anuj
# name is  54
====================================
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm=blooded animal.')
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
d1 = Dog()
#Dog has four legs.
#Dog is a warm=blooded animal.
=================================
class Mammal(object):
    def __init__(self, mammalName):
      print(mammalName, 'is a warm=blooded animal.')
    def abc(self,parameter):
       print("the parameter is ",parameter)
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().abc('parameter1')
d1 = Dog()

#Dog has four legs.
#the parameter is  parameter1
=================================
class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm=blooded animal.')
    def abc(self,parameter):
        print("the parameter is ",parameter)
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().abc('parameter1')
        Mammal.abc(self,'parameter1')
d1 = Dog()
# Dog has four legs.
# the parameter is  parameter1
# the parameter is  parameter1
=================================
class Mammal(object):
    def __init__(self, mammalName):
      print(mammalName, 'is a warm=blooded animal.')
    def abc(self,parameter):
       print("the parameter is ",parameter)
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().abc('parameter1')
        super().__init__("parameter 2 ")
d1 = Dog()

#Dog has four legs.
#the parameter is  parameter1
#parameter 2  is a warm=blooded animal.
=================================
class Mammal(object):
    def __init__(self, mammalName):
      print(mammalName, 'is a warm=blooded animal.')
    def abc(self,parameter):
       print("the parameter is ",parameter)
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        Mammal.abc(self,'parameter1')
d1 = Dog()

#Dog has four legs.
#the parameter is  parameter1
=================================
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm=blooded animal.')
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    Mammal.__init__(self,'Dog')
d1 = Dog()

#Dog has four legs.
#Dog is a warm=blooded animal.

==================================
class Mammal(object):
  def __init__(self, mammalName):
      self.mammalName = mammalName
      print(self.mammalName, 'is a warm=blooded animal.')
      print(mammalName, 'is a warm=blooded animal.')
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
d1 = Dog()

#Dog has four legs.
#Dog is a warm=blooded animal.
#Dog is a warm=blooded animal.
=================================

class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm=blooded animal.')
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    Mammal.__init__(self, 'Dog')    
d1 = Dog()
#Dog has four legs.
#Dog is a warm=blooded animal.
=====================================
super() with Multiple Inheritance:
=================================
class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.');
class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm=blooded animal.')
    super().__init__(mammalName)
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super().__init__(NonWingedMammalName)
class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super().__init__(NonMarineMammalName)
class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
d = Dog()
print('')
bat = NonMarineMammal('Bat') 

#Dog has 4 legs.
#Dog can't swim.
#Dog can't fly.
#Dog is a warm=blooded animal.
#Dog is an animal.
#
#Bat can't swim.
#Bat is a warm=blooded animal.
#Bat is an animal.
=============================
class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm=blooded animal.')
    super().__init__(mammalName)

class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super().__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super().__init__(NonMarineMammalName)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')

d = Dog()
print('')
bat = NonMarineMammal('Bat')

#Dog has 4 legs.
#Dog can't swim.
#Dog can't fly.
#Dog is a warm=blooded animal.
#Dog is an animal.

#Bat can't swim.
#Bat is a warm=blooded animal.
#Bat is an animal.
==============================
class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm=blooded animal.')
    super().__init__(mammalName)

class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super().__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super().__init__(NonMarineMammalName)

class Dog(NonWingedMammal,NonMarineMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')

d = Dog()
print('')
bat = NonMarineMammal('Bat')

#Dog has 4 legs.
#Dog can't fly.
#Dog can't swim.
#Dog is a warm=blooded animal.
#Dog is an animal.

#Bat can't swim.
#Bat is a warm=blooded animal.
#Bat is an animal.
==============================

Method Resolution Order (MRO):
=============================
It's the order in which method should be inherited in the presence of multiple inheritance. 
You can view the MRO by using __mro__ attribute.

print(Dog.__mro__)
(<class 'Dog'>, 
<class 'NonMarineMammal'>, 
<class 'NonWingedMammal'>, 
<class 'Mammal'>, 
<class 'Animal'>, 
<class 'object'>)

==========================
class parent:
    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)
class child(parent):
    def __init__(self):
        self.city = "patna"
        print("child class constructor")
        parent.__init__(self) #super().__init__() it will also work
    def inner1(self):
        print("another inner class")
obj = child()
obj.inner()


#child class constructor
#this is constructor call
#this is inner class
#first name is  kumar
#last name is  anuj
