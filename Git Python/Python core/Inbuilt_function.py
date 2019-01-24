Python abs()
The abs() method returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
# random integer
integer = -20
print('Absolute value of -20 is:', abs(integer))
#random floating number
floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))
Absolute value of -20 is: 20
Absolute value of -30.33 is: 30.33
===================================
Python any()
The any() method returns True if any element of an iterable is True. If not, any() returns False.
==================================
Python all()
The all() method returns True when all elements in the given iterable are true. If not, it returns False.
================================
Python ascii()
The ascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the string using \x, \u or \U escapes.
normalText = 'Python is interesting'
print(ascii(normalText))
otherText = 'Pythön is interesting'
print(ascii(otherText))
print('Pyth\xf6n is interesting')
'Python is interesting'
'Pyth\xf6n is interesting'
Pythön is interesting
===========================
Python bin()
The bin() method converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.
number = 5
print('The binary equivalent of 5 is:', bin(number))
The binary equivalent of 5 is: 0b101
==========================
Python bool()
The bool() method converts a value to Boolean (True or False) using the standard truth testing procedure.
==============================
Python bytearray()
The bytearray() method returns a bytearray object which is an array of the given bytes.
bytearray() Parameters
The bytearray() takes three optional parameters:

source (Optional) - source to initialize the array of bytes.
encoding (Optional) - if source is a string, the encoding of the string.
errors (Optional) - if source is a string, the action to take when the encoding conversion fails (Read more: String encoding)

string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)
bytearray(b'Python is interesting.')
==============================
Python callable()
The callable() method returns True if the object passed appears callable. If not, it returns False.
x = 5
print(callable(x))
def testFunction():
  print("Test")
y = testFunction
print(callable(y))
False
True
==================================
Python bytes()
The bytes() method returns a immutable bytes object initialized with the given size and data
string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)
b'Python is interesting.'
====================================
Python chr()
The chrt() method returns a character (a string) from an integer (represents unicode code point of the character).
print(chr(97))
print(chr(65))
print(chr(1200))
a
A
Ұ
====================================
Python compile()
The compile() method returns a Python code object from the source (normal string, a byte string, or an AST object).
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')
exec(codeObejct)
sum = 11
=====================================
Python classmethod()
The classmethod() method returns a class method for the given function.
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)
# create printAge class method
Person.printAge = classmethod(Person.printAge)
Person.printAge()
Person().printAge()
#The age is: 25
#The age is: 25
=========================================
Python complex()
The complex() method returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number.
z = complex(2, -3)
print(z)
z = complex(1)
print(z)
z = complex()
print(z)
z = complex('5-9j')
print(z)
(2-3j)
(1+0j)
0j
(5-9j)
========================================
Python delattr()
The delattr() deletes an attribute from the object (if the object allows it).
class Coordinate:
  x = 10
  y = -5
  z = 0
point1 = Coordinate() 
print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)
delattr(Coordinate, 'z')
print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)
# Raises Error
print('z = ',point1.z)
x =  10
y =  -5
z =  0
--After deleting z attribute--
x =  10
y =  -5
Traceback (most recent call last):
  File "python", line 19, in <module>
AttributeError: 'Coordinate' object has no attribute 'z'
=======================================
Python dict()
The dict() constructor creates a dictionary in Python.
numbers = dict(x=5, y=0)
print('numbers = ',numbers)
print(type(numbers))
empty = dict()
print('empty = ',empty)
print(type(empty))
numbers =  {'x': 5, 'y': 0}
<class 'dict'>
empty =  {}
<class 'dict'>
=======================================














