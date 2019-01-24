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
Python dir()
The dir() method tries to return a list of valid attributes of the object.
number = "anuj"
print(dir(number))
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
# '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
# 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
=====================================
Python divmod()
The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.

print('divmod(8, 3) = ', divmod(8, 3))
print('divmod(3, 8) = ', divmod(3, 8))
print('divmod(5, 5) = ', divmod(5, 5))
# divmod() with Floats
print('divmod(8.0, 3) = ', divmod(8.0, 3))
print('divmod(3, 8.0) = ', divmod(3, 8.0))
print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))
divmod(8, 3) =  (2, 2)
divmod(3, 8) =  (0, 3)
divmod(5, 5) =  (1, 0)
divmod(8.0, 3) =  (2.0, 2.0)
divmod(3, 8.0) =  (0.0, 3.0)
divmod(7.5, 2.5) =  (3.0, 0.0)
divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)
=============================================
Python enumerate()
The enumerate() method adds counter to an iterable and returns it (the enumerate object).
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
# converting to list
print(list(enumerateGrocery))
# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
for i in enumerate(grocery):
    print(i)
<class 'enumerate'>
[(0, 'bread'), (1, 'milk'), (2, 'butter')]
[(10, 'bread'), (11, 'milk'), (12, 'butter')]
(0, 'bread')
(1, 'milk')
(2, 'butter')
==========================================
Python staticmethod()
The staticmethod() built-in function returns a static method for a given function.
class Mathematics:

    def addNumbers(x, y):
        return x + y
# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)
print('The sum is:', Mathematics.addNumbers(5, 10))
The sum is: 15
==========================================
Python filter()
The filter() method constructs an iterator from elements of an iterable for which a function returns true.

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False
filteredVowels = filter(filterVowels, alphabets)
print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

The filtered vowels are:
a
e
i
o
===========================================
Python eval()
The eval() method parses the expression passed to this method and runs python expression (code) within the program.
x = 1
print(eval('x + 1')) #it must be string
2
==========================================
Python float()
The float() method returns a floating point number from a number or a string.
# for integers
print(float(10))
# for floats
print(float(11.22))
# for string floats
print(float("-13.33"))
# for string floats with whitespaces
print(float("     -24.45\n"))
# string float error
print(float("abc"))
10.0
11.22
-13.33
-24.45
ValueError: could not convert string to float: 'abc'
===========================================
Python format()
The built-in format() method returns a formatted representation of the given value controlled by the format specifier.
# d, f and b are type
# integer
print(format(123, "d"))
# float arguments
print(format(123.4567898, "f"))
# binary format
print(format(12, "b"))
123
123.456790
1100
==========================================
Python frozenset()
The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable.
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u','u')
fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
The frozen set is: frozenset({'u', 'e', 'o', 'i', 'a'})
The empty frozen set is: frozenset()
===============================================







8880943943


































