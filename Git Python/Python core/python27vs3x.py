Difference between python 2.7 vs 3.x
=======================================
=======================================
1. THERE IS BETTER UNICODE SUPPORT IN PYTHON 3
2. In Python 3, text strings are Unicode by default.
3. In Python 2, strings are stored as ASCII by default–you have to add a “u” if you want to store strings as Unicode in Python 2.x.
4. This is important because Unicode is more versatile than ASCII.
5. Unicode strings can store foreign language letters, Roman letters and numerals, symbols, emojis, etc., offering you more choices.
=======================================
1. In Python 2, if you write a number without any digits after the decimal point, it rounds your calculation down to the nearest 
whole number.
2. For example, if you’re trying to perform the calculation 5 divided by 2, and you type 5 / 2, the result will be 2 due to rounding. 
3. You would have to write it as 5.0 / 2.0 to get the exact answer of 2.5.
4 However, in Python 3, the expression 5 / 2 will return the expected result of 2.5 without having to worry about adding those 
extra zeroes.
5. This is one example of how Python 3 syntax can be more intuitive, making it easier for newcomers to learn Python programming.
========================================
1. THE TWO VERSIONS HAVE DIFFERENT PRINT STATEMENT SYNTAXES
2. This is only a syntactical difference–and some may consider it trivial–so it doesn’t affect the functionality of Python.
3. That said, it is still a big and visible difference you should know about.
4. Essentially, in Python 3, the print statement has been replaced with a print () function.
5. For example, in Python 2 it is print “hello” but in Python 3 it is print (“hello”).
===========================================
Division operator
1. If we are porting our code or executing the python 3.x code in python 2.x,
it can be dangerous if integer division changes go unnoticed (since it doesn’t raise any error).
2. It is preferred to use the floating value (like 7.0/5 or 7/5.0) to get the expected result when porting our code.
print 7 / 5
print -7 / 5    
  ''' 
Output in Python 2.x 
1 
-2 
Output in Python 3.x : 
1.4 
-1.4''' 
===========================================
print function
1. This is the most well known change.
2. In this the print function in Python 2.x is replaced by print() function in Python 3.x,i.e,
3. to print in Python 3.x an extra pair of parenthesis is required.
print 'Hello, Geeks'      # Python 3.x doesn't support 
print('Hope You like these facts') 
============================================
Unicode:
In Python 2, implicit str type is ASCII. But in Python 3.x implicit str type is Unicode.
print(type('default string ')) 
print(type(b'string with b ')) 
  ''' 
Output in Python 2.x (Bytes is same as str) 
<type 'str'> 
<type 'str'> 
  
Output in Python 3.x (Bytes and str are different) 
<class 'str'> 
<class 'bytes'> 
'''
==============================================
xrange:
1. xrange() of Python 2.x doesn’t exist in Python 3.x. In Python 2.x, range returns a list i.e. range(3) returns [0, 1, 2] 
2. while xrange returns a xrange object i. e., xrange(3) returns iterator object which work similar to Java iterator and generates
number when needed.
3. If we need to iterate over the same sequence multiple times, we prefer range() 
4. As range provides a static list. xrange() reconstructs the sequence every time. xrange() doesn’t support slices and other list
methods. 
5. The advantage of xrange() is, it saves memory when task is to iterate over a large range.
6. In Python 3.x, the range function now does what xrange does in Python 2.x, so to keep our code portable, 
7. we might want to stick to using range instead. So Python 3.x’s range function is xrange from Python 2.x.
for x in xrange(1, 5): 
    print(x), 
  
for x in range(1, 5): 
    print(x), 
  
''' 
Output in Python 2.x 
1 2 3 4 1 2 3 4 
  
Output in Python 3.x 
NameError: name 'xrange' is not defined 
'''
========================================
Error Handling:
1. There is a small change in error handling in both versions. In python 3.x, ‘as’ keyword is required.
try: 
    trying_to_check_error 
except NameError, err: 
    print err, 'Error Caused'   # Would not work in Python 3.x 
  ''' 
Output in Python 2.x: 
name 'trying_to_check_error' is not defined Error Caused 
  
Output in Python 3.x : 
File "a.py", line 3 
    except NameError, err: 
                    ^ 
SyntaxError: invalid syntax 
'''

try: 
     trying_to_check_error 
except NameError as err: # 'as' is needed in Python 3.x 
     print (err, 'Error Caused') 
  
''' 
Output in Python 2.x: 
(NameError("name 'trying_to_check_error' is not defined",), 'Error Caused') 
  
Output in Python 3.x : 
name 'trying_to_check_error' is not defined Error Caused 
'''
=======================================
_future_module:
1. This is basically not a difference between two version, but useful thing to mention here.
2. The idea of __future__ module is to help in migration. We can use Python 3.x
3. If we are planning Python 3.x support in our 2.x code,we can ise_future_ imports it in our code.
For example, in below Python 2.x code, we use Python 3.x’s integer division behavior using __future__ module
 In below python 2.x code, division works 
 same as Python 3.x because we use  __future__ 
from __future__ import division 
print 7 / 5
print -7 / 5
=================================
Another example where we use brackets in Python 2.x using __future__ module
from __future__ import print_function     
print('GeeksforGeeks') 
