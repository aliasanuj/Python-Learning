1. Python abs()
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
2. Python any()
The any() method returns True if any element of an iterable is True. If not, any() returns False.
==================================
3. Python all()
The all() method returns True when all elements in the given iterable are true. If not, it returns False.
================================
4. Python ascii()
The ascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the 
string using \x, \u or \U escapes.
normalText = 'Python is interesting'
print(ascii(normalText))
otherText = 'Pythön is interesting'
print(ascii(otherText))
print('Pyth\xf6n is interesting')
'Python is interesting'
'Pyth\xf6n is interesting'
Pythön is interesting
===========================
5. Python bin()
The bin() method converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has
to implement __index__() method to return an integer.
number = 5
print('The binary equivalent of 5 is:', bin(number))
The binary equivalent of 5 is: 0b101
==========================
6. Python bool()
The bool() method converts a value to Boolean (True or False) using the standard truth testing procedure.
==============================
7. Python bytearray()
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
8. Python callable()
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
9. Python bytes()
The bytes() method returns a immutable bytes object initialized with the given size and data
string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)
b'Python is interesting.'
====================================
10. Python chr()
The chrt() method returns a character (a string) from an integer (represents unicode code point of the character).
print(chr(97))
print(chr(65))
print(chr(1200))
a
A
Ұ
====================================
11. Python compile()
The compile() method returns a Python code object from the source (normal string, a byte string, or an AST object).
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')
exec(codeObejct)
sum = 11
=====================================
12. Python classmethod()
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
13. Python complex()
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
14. Python delattr()
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
15. Python dict()
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
16. Python dir()
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
17. Python divmod()
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
18. Python enumerate()
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
19. Python staticmethod()
The staticmethod() built-in function returns a static method for a given function.
class Mathematics:

    def addNumbers(x, y):
        return x + y
# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)
print('The sum is:', Mathematics.addNumbers(5, 10))
The sum is: 15
==========================================
20. Python filter()
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
21. Python eval()
The eval() method parses the expression passed to this method and runs python expression (code) within the program.
x = 1
print(eval('x + 1')) #it must be string
2
==========================================
22. Python float()
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
23. Python format()
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
24. Python frozenset()
The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable.
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u','u')
fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
The frozen set is: frozenset({'u', 'e', 'o', 'i', 'a'})
The empty frozen set is: frozenset()
===============================================
25. Python getattr()
The getattr() method returns the value of the named attribute of an object. If not found, it returns the default value provided to the
function.
class Person:
    age = 23
    name = "Adam"
person = Person()
# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))
# when no default value is provided
print('The sex is:', getattr(person, 'sex'))
The sex is: Male
AttributeError: 'Person' object has no attribute 'sex'
==========================================
26. Python globals()
The globals() method returns the dictionary of the current global symbol table.
======================================
27. Python exec()
The exec() method executes the dynamically created program, which is either a string or a code object.
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
Sum = 15
===========================================
28. Python hasattr()
The hasattr() method returns true if an object has the given named attribute and false if it does not.
class Person:
    age = 23
    name = 'Adam'
person = Person()
print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))
Person has age?: True
Person has salary?: False
==============================================
29. Python help()
The help() method calls the built-in Python help system.
help(list)
class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 ===========================================
 30. Python hex()
The hex() function converts an integer number to the corresponding hexadecimal string.
number = 435
print(number, 'in hex =', hex(number))
number = 0
print(number, 'in hex =', hex(number))
number = -34
print(number, 'in hex =', hex(number))
returnType = type(hex(number))
print('Return type from hex() is', returnType)
435 in hex = 0x1b3
0 in hex = 0x0
-34 in hex = -0x22
Return type from hex() is <class 'str'>
============================================
31. Python hash()
The hash() method returns the hash value of an object if it has one.
# hash for integer unchanged
print('Hash for 181 is:', hash(181))
# hash for decimal
print('Hash for 181.23 is:',hash(181.23))
# hash for string
print('Hash for Python is:', hash('Python'))
Hash for 181 is: 181
Hash for 181.23 is: 530343892119126197
Hash for Python is: 2230730083538390373 
==============================================
32. Python input()
The input() method reads a line from input, converts into a string and returns it.
=====================================
33. Python id()
The id() function returns identity (unique integer) of an object.
class Foo:
    b = 5
dummyFoo = Foo()
print('id of dummyFoo =',id(dummyFoo))
id of dummyFoo = 140343867415240

class Foo:
    b = 5
dummyFoo = Foo()
a = Foo()
print('id of dummyFoo =',id(dummyFoo))
print('id of dummyFoo =',id(a))
id of dummyFoo = 85187952
id of dummyFoo = 85241584

a = 10
print(id(a))
b = a
print(id(b))
1880017168
1880017168
=========================================
34. Python isinstance()
The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
class Foo:
  a = 5
fooInstance = Foo()
print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))
True
False
True
=========================================
35. Python int()
The int() method returns an integer object from any number or string.
# integer
print("int(123) is:", int(123))
# float
print("int(123.23) is:", int(123.23))
# string
print("int('123') is:", int('123'))
int(123) is: 123
int(123.23) is: 123
int('123') is: 123
======================================
36. Python issubclass()
The issubclass() function checks if the object argument (first argument) is a subclass of classinfo class (second argument).
class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')
print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))
print(issubclass(Polygon, Polygon))
True
False
True
True
True
====================================
37. Python iter()
The iter() method returns an iterator for the given object.
# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
vowelsIter = iter(vowels)
# prints 'a'
print(next(vowelsIter))
# prints 'e'
print(next(vowelsIter))
# prints 'i'
print(next(vowelsIter))
# prints 'o'
print(next(vowelsIter))
# prints 'u'
print(next(vowelsIter))
print(next(vowelsIter)) #error stopIteration
a
e
i
o
u
error stopIteration
=======================================
38. Python list() Function
The list() constructor creates a list in Python.
======================================
39. Python locals()
The locals() method updates and returns a dictionary of the current local symbol table.
========================================
40. Python len()
The len() function returns the number of items (length) in an object.
testList = []
print(testList, 'length is', len(testList))
testList = [1, 2, 3]
print(testList, 'length is', len(testList))
testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))
testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))
[] length is 0
[1, 2, 3] length is 3
(1, 2, 3) length is 3
Length of range(1, 10) is 9
==========================================
41. Python max()
The max() method returns the largest element in an iterable or largest of two or more parameters.
# using max(arg1, arg2, *args)
print('Maximum is:', max(1, 3, 2, 5, 4))
# using max(iterable)
num = [1, 3, 2, 8, 5, 10, 6]
print('Maximum is:', max(num))
Maximum is: 5
Maximum is: 10
=========================================
42. Python min()
The min() method returns the smallest element in an iterable or smallest of two or more parameters.
# using min(arg1, arg2, *args)
print('Minimum is:', min(1, 3, 2, 5, 4))
# using min(iterable)
num = [3, 2, 8, 5, 10, 6]
print('Minimum is:', min(num))
Minimum is: 1
Minimum is: 2
=========================================
43. Python map()
The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
def calculateSquare(n):
  return n*n
numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)
# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
<map object at 0x00E8FE50>
{16, 1, 4, 9}
====================================
44. Python next()
The next() function returns the next item from the iterator.
====================================
45. Python memoryview()
The memoryview() method returns a memory view object of the given argument.
#random bytearray
randomByteArray = bytearray('ABC', 'utf-8')
mv = memoryview(randomByteArray)
# access memory view's zeroth index
print(mv[0])
# create byte from memory view
print(bytes(mv[0:2]))
# create list from memory view
print(list(mv[0:3]))
65
b'AB'
[65, 66, 67]
===================================
46. Python object()
This returns a featureless object which is a base for all classes.
test = object()
print(type(test))
print(dir(test))
<class 'object'>
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__']
=====================================
47. Python oct()
The oct() method takes an integer number and returns its octal representation. If the given number is an int, it must 
implement __index__() method to return an integer.
# decimal number
print('oct(10) is:', oct(10))
# binary number
print('oct(0b101) is:', oct(0b101))
# hexadecimal number
print('oct(0XA) is:', oct(0XA))
oct(10) is: 0o12
oct(0b101) is: 0o5
oct(0XA) is: 0o12
=========================================
48. Python ord()
The ord() method returns an integer representing Unicode code point for the given Unicode character.
# code point of integer
print(ord('5'))
# code point of alphabet 
print(ord('A'))
# code point of character
print(ord('$'))
53
65
36
=====================================
49. Python open()
The open() function opens the file (if possible) and returns a corresponding file object.
# opens for read
f = open("path_to_file", mode='r')
# opens for write 
f = open("path_to_file", mode = 'w')
# opens for writing to the end 
f = open("path_to_file", mode = 'a')
===================================
50. Python pow()
The pow() method returns x to the power of y. If the third argument (z) is given, it returns x to the power of y
modulus z, i.e. pow(x, y) % z.
# positive x, positive y (x**y)
print(pow(2, 2))
# negative x, positive y
print(pow(-2, 2))
# positive x, negative y (x**-y)
print(pow(2, -2))
# negative x, negative y
print(pow(-2, -2))
4
4
0.25
0.25

x = 7
y = 2
z = 5
print(pow(x, y, z))
4
==================================
51. Python print()
The print() function prints the given object to the standard output device (screen) or to the text stream file.
==================================
52. Python property()
The property() method a returns a property attribute.
==================================
53. Python range()
The range() type returns an immutable sequence of numbers between the given start integer to the stop integer.
===================================
54. Python repr()
The repr() method returns a printable representation of the given object.
var = 'foo'
print(repr(var))
'foo'
===================================
55. Python reversed()
The reversed() method returns the reversed iterator of the given sequence.
===================================
56. Python round()
The round() method returns the floating point number rounded off to the given ndigits digits after the decimal point.
If no ndigits is provided, it rounds off the number to the nearest integer.
# for integers
print(round(10))
# for floating point
print(round(10.7))
# even choice
print(round(5.5))
print(round(5.4))
10
11
6
5
==============================
57. Python set()
The set() constructor constructs a Python set from the given iterable and returns it.
# empty set
print(set())
# from string
print(set('Python'))
# from tuple
print(set(('a', 'e', 'i', 'o', 'u')))
# from list
print(set(['a', 'e', 'i', 'o', 'u']))
# from range
print(set(range(5)))
set()
{'P', 'o', 't', 'n', 'y', 'h'}
{'a', 'o', 'e', 'u', 'i'}
{'a', 'o', 'e', 'u', 'i'}
{0, 1, 2, 3, 4}
================================
58. Python setattr()
The setattr() method sets the value of given attribute of an object.
class Person:
    name = 'Adam'
p = Person()
print('Before modification:', p.name)
# setting name to 'John'
setattr(p, 'name', 'John')
print('After modification:', p.name)
Before modification: Adam
After modification: John
==================================
59. Python slice()
The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step).
=================================
60. Python sorted()
The sorted() method returns a sorted list from the given iterable.
=================================
61. Python str()
The str() method returns the "informal" or nicely printable representation of a given object.
=================================
62. Python sum()
The sum() function adds the items of an iterable and returns the sum.
==================================
63. Python tuple() Function
The tuple() built-in is used to create a tuple in Python.
t1 = tuple()
print('t1=', t1)
# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2=', t2)
# creating a tuple from a string
t1 = tuple('Python')
print('t1=',t1)
# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1=',t1)
t1= ()
t2= (1, 4, 6)
t1= ('P', 'y', 't', 'h', 'o', 'n')
t1= (1, 2)
===================================
64. Python type()
If a single argument (object) is passed to type() built-in, it returns type of the given object. If three arguments 
(name, bases and dict) are passed, it returns a new type object.
===================================
65. Python vars()
The vars() function returns the __dict__ attribute of the given object if the object has __dict__ attribute.
class Foo:
  def __init__(self, a = 5, b = 10):
    self.a = a
    self.b = b
InstanceOfFoo = Foo()
print(vars(InstanceOfFoo))
{'a': 5, 'b': 10}
===================================
66. Python zip()
The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the 
iterables passed, and returns an iterator of tuples.
===================================
67. Python __import__()
The __import__() is an advanced function that is called by the import statement.
===================================
68. Python super()
The super() builtin returns a proxy object that allows you to refer parent class by 'super'.
==================================
