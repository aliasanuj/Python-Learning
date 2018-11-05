#exceptation_handelling.py
========================================================




========================================================
Exception
========================================================
Sr.No.	Exception Name & Description
1	Exception Base class for all exceptions
2	StopIteration Raised when the next() method of an iterator does not point to any object.
3	SystemExitRaised by the sys.exit() function.
4	StandardError Base class for all built-in exceptions except StopIteration and SystemExit.
5	ArithmeticError Base class for all errors that occur for numeric calculation.
6	OverflowError Raised when a calculation exceeds maximum limit for a numeric type.
7	FloatingPointError Raised when a floating point calculation fails.
8	ZeroDivisionError Raised when division or modulo by zero takes place for all numeric types.
9	AssertionError Raised in case of failure of the Assert statement.
10	AttributeError Raised in case of failure of attribute reference or assignment.
11	EOFError Raised when there is no input from either the raw_input() or input() function and the end of file is reached.
12	ImportError Raised when an import statement fails.
13	KeyboardInterrupt Raised when the user interrupts program execution, usually by pressing Ctrl+c.
14	LookupError Base class for all lookup errors.
15	IndexError Raised when an index is not found in a sequence.
16	KeyError Raised when the specified key is not found in the dictionary.
17	NameError Raised when an identifier is not found in the local or global namespace.
18	UnboundLocalError Raised when trying to access a local variable in a function or method but no value has been assigned to it.
19	EnvironmentError Base class for all exceptions that occur outside the Python environment.
20	IOError Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.
21	IOError Raised for operating system-related errors.
22	SyntaxError Raised when there is an error in Python syntax.
23	IndentationError Raised when indentation is not specified properly.
24	SystemError Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.
25	SystemExit Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.
26	TypeError Raised when an operation or function is attempted that is invalid for the specified data type.
27	ValueError Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.
28	RuntimeError Raised when a generated error does not fall into any category.
29	NotImplementedError Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.
====================================================
Exception Class	Event
====================================================
Exception		Base class for all exceptions
ArithmeticError		Raised when numeric calculations fails
FloatingPointError	Raised when a floating point calculation fails
ZeroDivisionError	Raised when division or modulo by zero takes place for all numeric types
AssertionError		Raised when Assert statement fails
OverflowError		Raised when result of an arithmetic operation is too large to be represented
ImportError		Raised when the imported module is not found
IndexError		Raised when index of a sequence is out of range
KeyboardInterrupt	Raised when the user interrupts program execution, generally by pressing Ctrl+c
IndentationError	Raised when there is incorrect indentation
SyntaxError		Raised by parser when syntax error is encountered
KeyError		Raised when the specified key is not found in the dictionary
NameError		Raised when an identifier is not found in the local or global namespace
TypeError		Raised when a function or operation is applied to an object of incorrect type
ValueError		Raised when a function gets argument of correct type but improper value
IOError			Raised when an input/ output operation fails
RuntimeError		Raised when a generated error does not fall into any category
=======================================================
========================================================
try:
    print (1/0)
except ZeroDivisionError:
    print ("You can't divide by zero, you're silly.")
#You can't divide by zero, you're silly.
================================================
import sys
try:
    number = int(input("Enter a number between 1 - 10 "))
except ValueError:
    print ("Err.. numbers only")
    sys.exit()
print ("you entered number ", number)
#Enter a number between 1 - 10 54
#you entered number  54
================================================
try:
    print (1/0)
except ZeroDivisionError:
    print ("You can't divide by zero!")
#You can't divide by zero!
==================================================
try:
    result = None
    try:
        result = (4/6)
    except ZeroDivisionError:
        print ("division by zero!")
    print ("result is ", result)
finally:
    print ("executing finally clause")
#result is  0.6666666666666666
#executing finally clause
==================================================
try:
    result = 0 / 5
except ZeroDivisionError:
    print ("division by zero!")
else:
    print ("result is", result)
finally:
    print ("executing finally clause")
#result is 0.0
#executing finally clause
===================================================
import sys
randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)
#The entry is a
#Oops! <class 'ValueError'> occured.
#Next entry.

#The entry is 0
#Oops! <class 'ZeroDivisionError'> occured.
#Next entry.

#The entry is 2
#The reciprocal of 2 is 0.5
======================================================
try:
   # do something
   pass
except ValueError:
   # handle ValueError exception
   pass
except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass
except:
   # handle all other exceptions
   pass
===================================================
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
#Enter a positive integer: 12
====================================================
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
#Enter a positive integer: -5
#That is not a positive number!
===================================================
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
#Enter a positive integer: gh
#invalid literal for int() with base 10: 'gh'
===================================================
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
number = 10
while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()
print("Congratulations! You guessed it correctly.")
#Enter a number: 45
#This value is too large, try again!
=======================================================
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
number = 10
while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()
print("Congratulations! You guessed it correctly.")
#Enter a number: -5
#This value is too small, try again!
=======================================================
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
number = 10
while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()
   except ValueError:
       print("please enter appropriate input")
print("Congratulations! You guessed it correctly.")
#Enter a number: dfdf
#please enter appropriate input
#Enter a number: 
========================================================
# = int(input("enter any number"))
try:
    x = int(input("enter any number"))
    if x > 5:
        print("correct")
    else:
        print("appropriate number")
except ValueError:
        print("enter appropriate value")
        
#enter any numbergdfgdf
#enter appropriate value
=============================================================
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
================================================
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')


  
