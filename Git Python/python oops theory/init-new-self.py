================================
========__init__================
================================
1. The __init__ function is called a constructor, or initializer, and is 
automatically called when you create a new instance of a class.
Within that function, the newly created object is assigned to the parameter self .
The notation self.legs is an attribute called legs of the object in the variable self
2. __init__ is called when ever an object of the class is constructed.
That means when ever we will create a student object we will see the message 
“A student object is created” in the prompt
3. All classes have a function called __init__(), which is always executed when the class is being initiated.
4. Use the __init__() function to assign values to object properties, or other operations that are necessary 
to do when the object is being created
5. def __new__(self,p1,p2) or def __new__(cls,p1,p2)

====================================
===========self=====================
====================================
1. self represents the instance of the class. By using the "self" keyword we can access 
the attributes and methods of the class in python.


==>Use __new__ when you need to control the creation of a new instance. 
==>Use __init__ when you need to control initialization of a new instance.

==>__new__ is the first step of instance creation. 
It's called first, and is responsible for returning a new instance of your class. 
In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance 
after it's been created.
=============================
https://spyhce.com/blog/understanding=new=and=init
https://howto.lintel.in/python=__new__=magic=method=explained/
=============================
class parent:
    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)

    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    def __new__(self):
        self.a = "aaaa"
        self.b = "bbbbbb"
        print(self.a)
        print(self.b)
obj = parent()
#obj.inner() ==>error
#aaaa
#bbbbbb
==========================================
class parent:
    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)

    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    def __new__(self):
        self.a = "aaaa"
        self.b = "bbbbbb"
        print(self.a)
        print(self.b)
obj = parent()
obj1 = parent()
obj.__init__() #no output
# aaaa
# bbbbbb
# aaaa
# bbbbbb
============================
class parent:
    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)

    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    def __new__(cls):
        cls.a = "aaaa"
        cls.b = "bbbbbb"
        print(cls.a)
        print(cls.b)
obj = parent()
#obj.inner() ==>error
#aaaa
#bbbbbb
==============================
class parent:
    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)

    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    def __new__(self):
        self.a = "aaaa"
        self.b = "bbbbbb"
        print(self.a)
        print(self.b)
parent()
print(parent())
#aaaa
#bbbbbb
#aaaa
#bbbbbb
#None
==============================
class parent:
    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)

    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    def __new__(cls):
        print("__new__")
obj = parent()
#__new__
===============================
class parent:
    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)

    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    def __new__(cls):
        print("__new__")
parent()
#__new__
======================================
class A(object):

    def __new__(cls):
        print("A.__new__ called")

    def __init__(self):
        print("A.__init__ called")  # => is actually never called

print(A())
A()
#A.__new__ called
#None
#A.__new__ called
===============================
class A:

    def __new__(cls):
        print("A.__new__ called")

    def __init__(self):
        print("A.__init__ called")  # => is actually never called
print(A())
A()
#A.__new__ called
#None
#A.__new__ called
===============================
class A:

    def __new__(cls):
        print("A.__new__ called")

    def __init__(self):
        print("A.__init__ called")  # => is actually never called
obj = A()
#A.__new__ called
=============================
class parent:
    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)

    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    #def __new__(cls):
     #   print("__new__")
obj = parent()
#this is constructor call
==========================
class parent:
    def inner(self):
        print("this is inner class")
        print("first name is ",self.fname)
        print("last name is ",self.lname)

    def __init__(self):
        self.fname = "kumar"
        self.lname = "anuj"
        self.roll = 101
        print("this is constructor call")

    #def __new__(cls):
     #   print("__new__")
parent()
#this is constructor call
==========================
class A:  # => don't forget the object specified as base

    def __new__(cls):
        print("A.__new__ called")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("A.__init__ called")
A()
#A.__new__ called
#A.__init__ called
===========================
class A(object):

    def __init__(self):
        print("A.__init__ called")
        return 33  # => TypeError: __init__ should return None
A()
#A.__init__ called
#TypeError: __init__() should return None, not 'int'
==========================
class Sample(object):
    def __str__(self):
        return "SAMPLE"
class A(object):
    def __new__(cls):
        return Sample()
print(A())
#SAMPLE
========================
class Sample(object):
    def __str__(self):
        return "SAMPLE"
class A(object):
    def __new__(cls):
        return super(A, cls).__new__(Sample)
print(A())
#SAMPLE
========================
class Animal(object):
    def __new__(cls, name):
        print('__new__() called.')
        obj = super().__new__(cls)
        obj.name = name
        return obj
a = Animal('Bob')
print(a.name)
#__new__() called.
#Bob
========================
class Animal(object):
    def __new__(cls, name):
        print('__new__() called.')
        obj = super().__new__(cls)
        obj.name = name
        return obj
a = Animal('Bob')
print(a.name)
#__new__() called.
#Bob
========================
#You can create instance inside __new__  method either by using super function or by directly calling __new__
method over object  Where if parent class is object. That is,

instance = super(MyClass, cls).__new__(cls, *args, **kwargs)
or
instance = object.__new__(cls, *args, **kwargs)
