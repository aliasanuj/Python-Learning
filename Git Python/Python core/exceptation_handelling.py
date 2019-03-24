#exceptation_handelling.py
========================================================
An exception is an event, which occurs during the execution of a program that disrupts the normal flow
of the program's instructions.In general, when a Python script encounters a situation that it cannot
cope with, it raises an exception. An exception is a Python object that represents an error.
When a Python script raises an exception, it must either handle the exception immediately
otherwise it terminates and quits.
==========================================================
Handling an exception : 
If you have some suspicious code that may raise an exception,
you can defend your program by placing the suspicious code in a 
try: block. After the try: block, include an except: statement, 
followed by a block of code which handles the problem as elegantly as possible.
==========================================================
try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
 ==========================================================
1. A single try statement can have multiple except statements.
2. This is useful when the try block contains statements that may throw different types of exceptions.
3. You can also provide a generic except clause, which handles any exception.
4. After the except clause(s), you can include an else-clause. The code in
5. The else-block executes if the code in the try: block does not raise an exception.
6. The else-block is a good place for code that does not need the try: block's protection.
==========================================================
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
==========================================================   
The except Clause with No Exceptions
You can also use the except statement with no exceptions defined as follows −
try:
   You do your operations here;
   ......................
except:
   If there is any exception, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
1. This kind of a try-except statement catches all the exceptions that occur.
2. Using this kind of try-except statement is not considered a good programming
practice though, because it catches all exceptions but does not make the programmer
Identify the root cause of the problem that may occur.
==========================================================
1. The try-finally Clause :
2. You can use a finally: block along with a try: block.
3. The finally block is a place to put any code that must execute, 
whether the try-block raised an exception or not. 
4. The syntax of the try-finally statement is this −
==========================================================
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
   ......................
You cannot use else clause as well along with a finally clause.
==========================================================
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print "Error: can\'t find file or read data"
If you do not have permission to open the file in writing mode,
then this will produce the following result −
Error: can't find file or read data
==========================================================
try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print "Going to close the file"
      fh.close()
except IOError:
   print "Error: can\'t find file or read data"
==========================================================   
User-Defined Exceptions
Python also allows you to create your own exceptions by deriving 
classes from the standard built-in exceptions.
Here is an example related to RuntimeError. Here, a class is created 
that is subclassed from RuntimeError. This is useful when you need to 
display more specific information when an exception is caught.
In the try block, the user-defined exception is raised and caught in the 
except block. The variable e is used to create an instance of the class Networkerror.
==========================================================
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
#So once you defined above class, you can raise the exception as follows −

try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args

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
Exceptions versus Syntax Errors :
Syntax errors occur when the parser detects an incorrect statement. Observe the following example:
==========================================================
>>> print( 0 / 0 ))
  File "<stdin>", line 1
    print( 0 / 0 ))
                  ^
SyntaxError: invalid syntax
The arrow indicates where the parser ran into the syntax error. 
In this example, there was one bracket too many. Remove it and run your code again:
==========================================================
>>> print( 0 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
==========================================================
This time, you ran into an exception error. This type of error occurs whenever 
syntactically correct Python code results in an error. 
The last line of the message indicated what type of exception error you ran into.
Instead of showing the message exception error, Python details what type 
of exception error was encountered. In this case, it was a ZeroDivisionError.
Python comes with various built-in exceptions as well as the possibility to create self-defined exceptions.
==========================================================
Raising an Exception :
We can use raise to throw an exception if a condition occurs.
The statement can be complemented with a custom exception.
If you want to throw an error when a certain condition occurs using raise, 
you could go about it like this:
==========================================================
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

	When you run this code, the output will be the following:
Traceback (most recent call last):
  File "<input>", line 4, in <module>
Exception: x should not exceed 5. The value of x was: 10
The program comes to a halt and displays our exception to screen, 
offering clues about what went wrong.
==========================================================
The AssertionError Exception :
Instead of waiting for a program to crash midway, you can also start by making an assertion in Python.
We assert that a certain condition is met. If this condition turns out to be True, then that
is excellent! The program can continue. If the condition turns out to be False, you can have the program 
throw an AssertionError exception.
==========================================================
Python assert statement :
Have a look at the following example, where it is asserted that the code will be executed on a Linux system:
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
If you run this code on a Linux machine, the assertion passes.
If you were to run this code on a Windows machine, the outcome of the
assertion would be False and the result would be the following:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError: This code runs on Linux only.
In this example, throwing an AssertionError exception is the last thing that the program will do. The program will come to halt and will not continue. What if that is not what you want?
==========================================================
The try and except Block: Handling Exceptions
The try and except block in Python is used to catch and handle exceptions. 
Python executes code following the try statement as a “normal” part of the program. 
The code that follows the except statement is the program’s response to any exceptions 
in the preceding try clause.
As you saw earlier, when syntactically correct code runs into an error,
Python will throw an exception error. This exception error will crash the 
program if it is unhandled. The except clause determines how your program responds to exceptions.
==========================================================
The following function can help you understand the try and except block:
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
The linux_interaction() can only run on a Linux system. 
The assert in this function will throw an AssertionError exception 
if you call it on an operating system other then Linux.
You can give the function a try using the following code:
==========================================================
try:
    linux_interaction()
except:
    pass
The way you handled the error here is by handing out a pass. 
If you were to run this code on a Windows machine, you would get the following output:

Summing Up :
1. After seeing the difference between syntax errors and exceptions, you learned about 
various ways to raise, catch, and handle exceptions in Python. In this article, you saw the following options:
2. raise allows you to throw an exception at any time.
3. assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
4. In the try clause, all statements are executed until an exception is encountered.
5. except is used to catch and handle the exception(s) that are encountered in the try clause.
6. else lets you code sections that should run only when no exceptions are encountered in the try clause.
7. finally enables you to execute sections of code that should always run, 
with or without any previously encountered exceptions.
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
try:
    result = 5 / 2
except ZeroDivisionError:
    print ("division by zero!")
else:
    print ("result is", result)
finally:
    print ("executing finally clause")
#result is 2.5
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
====================================================
class Error(Exception):
  pass
class ValueTooSmallError(Error):
  pass
class ValueTooLargeError(Error):
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
x = int(input("enter any number"))
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
