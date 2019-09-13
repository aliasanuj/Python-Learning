=========================
Encapsulation:===========
=========================

1. In an object oriented python program, you can restrict access to methods and variables. 
This can prevent the data from being modified by accident and is known as encapsulation.
2. Python does not have the private keyword, unlike some other object oriented languages, but encapsulation can be done.
3. Encapsulation is a mechanism that restricts direct access to objects’ data and methods. But at the same time, it 
facilitates operation on that data (objects’ methods).
=============================
class Robot(object):
   def __init__(self):
      self.a = 123
      self._b = 123
      self.__c = 123
obj = Robot()
print(obj.a)
print(obj._b)
print(obj.__c)
#123
#123
Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    print(obj.__c)
AttributeError: 'Robot' object has no attribute '__c' 
==============================
==>A single underscore: Private variable, it should not be accessed directly. But nothing stops you from doing that (except convention).
==>A double underscore: Private variable, harder to access but still possible.
==============================
=====================
Private methods :====
=====================
We create a class Car which has two methods:  drive() and updateSoftware().
When a car object is created, it will call the private methods __updateSoftware().  
This function cannot be called on the object directly, only from within the class.
=======================
class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')
redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object.

#updating software
#driving
==============================
class Car:
    def __init__(self):
        #self.__updateSoftware()
        pass
    def drive(self):
        self.__updateSoftware()
        print('driving')
    def __updateSoftware(self):
        print('updating software')
redcar = Car()
redcar.drive()
#updating software
#driving
==============================
class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')
redcar = Car()
redcar.drive()
redcar.__updatesoftware() #error ==>AttributeError: 'Car' object has no attribute '__updatesoftware'

#updating software
#driving
#AttributeError: 'Car' object has no attribute '__updatesoftware'
==============================
class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')
        self.__updateSoftware()

    def __updateSoftware(self):
        print('updating software')
redcar = Car()
redcar.drive()

#updating software
#driving
#updating software
==============================
class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving  maxspeed ' + str(self.__maxspeed))
redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive()

#driving  maxspeed 200
#driving  maxspeed 200
=============================
class abc:
    def __init__(self):
        self.__variable = 20
        self.__abc03()

    def abc01(self):
        print(self.__variable)

    def __abc03(self):
        print("abc03")

obj = abc()
obj.abc01()


#abc03
#20
===================================
class abc:
    def __init__(self):
        self.__variable = 20
        self.__abc03()

    def abc01(self):
        print(self.__variable)
        self.__variable = 10
        print(self.__variable)
    def __abc03(self):
        print("abc03")

obj = abc()
obj.abc01()
# 
# abc03
# 20
# 10
=========================================
Type			Description
=========================================
public methods		Accessible from anywhere
private methods		Accessible only in their own class. starts with two underscores
public variables	Accessible from anywhere
private variables	Accesible only in their own class or by a method if defined. starts with two underscores
========================================
class Person:
    def __init__(self):
        self.name = 'Manjula'
        self.__lastname = 'Dube'

    def PrintName(self):
        return self.name + ' ' + self.__lastname #we can access the private variable in any method.
# Outside class
P = Person()
print(P.name)  # Manjula
print(P.PrintName())  # Manjula Dube
#print(P.__lastname)  # error

#Manjula
#Manjula Dube
========================================
class Robot(object):
   def __init__(self):
      self.__version = 22

   def getVersion(self):
      print(self.__version)

   def setVersion(self, version):
      self.__version = version

obj = Robot()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.__version)

#22
#23
#error
=====================================
class outer:
    def __init__(self):
        self.__fname = "anuj"
        self.lname = "kumar"
        print("init")

    def abc(self):
        print("abc method")
        print(self.__fname)

    def changeValue(self,aaa):
        self.__fname = aaa
obj = outer()
obj.abc()
obj.changeValue("zzz")
obj.abc()

#init
#abc method
#anuj
#abc method
#zzz
