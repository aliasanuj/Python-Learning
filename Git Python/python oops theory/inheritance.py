======================================
======================================
======================================
Inheritance :
======================================
======================================
======================================
1. Inheritance enable us to define a class that takes all the functionality from parent class and allows us to add more.
2. Inheritance is a powerful feature in object oriented programming.
3. class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
4. Derived class inherits features from the base class, adding new features to it. This results into re=usability of code.
5. It provides reusability of a code. We don’t have to write the same code again and again. Also, it allows us to
add more features to a class without modifying it.
6. It is transitive in nature, which means that if class B inherits from another class A, 
then all the subclasses of B would automatically inherit from class A.
7. A process of using details from a new class without modifying existing class

=================================
Multiple Inheritance in Python :
=================================
1. In multiple inheritance, the features of all the base classes are inherited into the derived class
2. class Base1:
    pass
class Base2:
    pass
class MultiDerived(Base1, Base2):
    pass
Here, MultiDerived is derived from classes Base1 and Base2.
3. In the multiple inheritance scenario, any specified attribute is searched first in the current class. 
If not found, the search continues into parent classes in depth=first, left=right fashion without searching same class twice

===================================
class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)
class Student:
    def __init__(self, studentId):
        self.studentId = studentId

    def getId(self):
        return self.studentId

class Resident(Person, Student):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)
resident1 = Resident('John', 30, '102')
resident1.showName()
print(resident1.getId())
#John
#102
==========================================
class outer:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def Fname(self):
        print(self.fname)
    def Lname(self):
        print(self.lname)
class inner:
    def __init__(self,rollno):
        self.rollno = rollno

    def rol(self):
        print(self.rollno)
class final(outer,inner):
    def __init__(self,firstname,lastname,rollno):
        outer.__init__(self,firstname,lastname)
        inner.__init__(self,rollno)
obj = final("kumar","anuj",101)
obj.Fname()
obj.Lname()
obj.rol()
#kumar
#anuj
#101

====================================
Multilevel Inheritance in Python :
====================================
1. On the other hand, we can also inherit form a derived class. This is called multilevel inheritance. 
It can be of any depth in Python.
2. In multilevel inheritance, features of the base class and the derived class is inherited into the new derived class.
3. class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Derived1):
    pass

Method Resolution Order in Python:
==================================
1. Every class in Python is derived from the class object. It is the most base type in Python.
2. So technically, all other class, either built=in or user=defines, are derived classes and all objects are instances of object class.
# Output: True
print(issubclass(list,object))
# Output: True
print(isinstance(5.5,object))
# Output: True
print(isinstance("Hello",object))

